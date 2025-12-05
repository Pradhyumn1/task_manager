// To-Do App JavaScript
const API_BASE_URL = 'http://127.0.0.1:8000/api';
let authToken = localStorage.getItem('authToken');
let currentUser = JSON.parse(localStorage.getItem('currentUser') || 'null');
let allTasks = [];
let currentFilter = 'all';

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    if (authToken && currentUser) {
        showApp();
        loadTasks();
    } else {
        showAuth();
    }
});

// Authentication Functions
async function register(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    const data = {
        username: formData.get('username'),
        email: formData.get('email'),
        password: formData.get('password'),
        password2: formData.get('password2'),
        first_name: formData.get('first_name') || '',
        last_name: formData.get('last_name') || ''
    };
    
    try {
        showLoading('register-btn');
        const response = await fetch(`${API_BASE_URL}/auth/register/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            authToken = result.token;
            currentUser = result.user;
            localStorage.setItem('authToken', authToken);
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            showAlert('Registration successful! Welcome!', 'success');
            setTimeout(() => {
                showApp();
                loadTasks();
            }, 1000);
        } else {
            const errorMsg = Object.values(result).flat().join(' ');
            showAlert(errorMsg || 'Registration failed', 'error');
        }
    } catch (error) {
        showAlert('Network error. Please try again.', 'error');
    } finally {
        hideLoading('register-btn', 'Register');
    }
}

async function login(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    const data = {
        username: formData.get('username'),
        password: formData.get('password')
    };
    
    try {
        showLoading('login-btn');
        const response = await fetch(`${API_BASE_URL}/auth/login/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            authToken = result.token;
            currentUser = {
                id: result.user_id,
                username: result.username,
                email: result.email
            };
            localStorage.setItem('authToken', authToken);
            localStorage.setItem('currentUser', JSON.stringify(currentUser));
            showAlert('Login successful!', 'success');
            setTimeout(() => {
                showApp();
                loadTasks();
            }, 1000);
        } else {
            showAlert(result.error || 'Login failed', 'error');
        }
    } catch (error) {
        showAlert('Network error. Please try again.', 'error');
    } finally {
        hideLoading('login-btn', 'Login');
    }
}

async function logout() {
    try {
        await fetch(`${API_BASE_URL}/auth/logout/`, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            }
        });
    } catch (error) {
        console.error('Logout error:', error);
    } finally {
        authToken = null;
        currentUser = null;
        localStorage.removeItem('authToken');
        localStorage.removeItem('currentUser');
        showAlert('Logged out successfully', 'success');
        setTimeout(() => {
            showAuth();
        }, 1000);
    }
}

// Task Functions
async function loadTasks() {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/`, {
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            allTasks = data.results || data;
            renderTasks();
            updateStats();
        } else if (response.status === 401) {
            showAlert('Session expired. Please login again.', 'error');
            logout();
        }
    } catch (error) {
        showAlert('Error loading tasks', 'error');
    }
}

async function addTask(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    const data = {
        title: formData.get('title'),
        description: formData.get('description') || '',
        completed: false
    };
    
    try {
        showLoading('add-task-btn');
        const response = await fetch(`${API_BASE_URL}/tasks/`, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Task added successfully!', 'success');
            form.reset();
            await loadTasks();
        } else {
            showAlert('Failed to add task', 'error');
        }
    } catch (error) {
        showAlert('Network error', 'error');
    } finally {
        hideLoading('add-task-btn', '+ Add Task');
    }
}

async function toggleTaskComplete(taskId, currentStatus) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/`, {
            method: 'PATCH',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ completed: !currentStatus })
        });
        
        if (response.ok) {
            await loadTasks();
        }
    } catch (error) {
        showAlert('Error updating task', 'error');
    }
}

async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task?')) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Token ${authToken}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (response.ok) {
            showAlert('Task deleted successfully', 'success');
            await loadTasks();
        }
    } catch (error) {
        showAlert('Error deleting task', 'error');
    }
}

// Render Functions
function renderTasks() {
    const taskList = document.getElementById('task-list');
    
    let filteredTasks = allTasks;
    
    // Apply filter
    if (currentFilter === 'active') {
        filteredTasks = allTasks.filter(task => !task.completed);
    } else if (currentFilter === 'completed') {
        filteredTasks = allTasks.filter(task => task.completed);
    }
    
    // Apply search
    const searchTerm = document.getElementById('search-input')?.value.toLowerCase() || '';
    if (searchTerm) {
        filteredTasks = filteredTasks.filter(task => 
            task.title.toLowerCase().includes(searchTerm) ||
            (task.description && task.description.toLowerCase().includes(searchTerm))
        );
    }
    
    if (filteredTasks.length === 0) {
        taskList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">📝</div>
                <p class="empty-message">No tasks found. Add one to get started!</p>
            </div>
        `;
        return;
    }
    
    taskList.innerHTML = filteredTasks.map(task => `
        <div class="glass-card task-item ${task.completed ? 'completed' : ''}">
            <div class="task-checkbox ${task.completed ? 'checked' : ''}" 
                 onclick="toggleTaskComplete(${task.id}, ${task.completed})">
            </div>
            <div class="task-content">
                <h3 class="task-title">${escapeHtml(task.title)}</h3>
                ${task.description ? `<p class="task-description">${escapeHtml(task.description)}</p>` : ''}
                <div class="task-meta">
                    <span>📅 ${formatDate(task.created_at)}</span>
                    ${task.completed ? '<span>✓ Completed</span>' : '<span>⏳ In Progress</span>'}
                </div>
            </div>
            <div class="task-actions">
                <button class="btn-icon btn-delete" onclick="deleteTask(${task.id})" title="Delete">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');
}

function updateStats() {
    const total = allTasks.length;
    const completed = allTasks.filter(task => task.completed).length;
    const active = total - completed;
    
    document.getElementById('stat-total').textContent = total;
    document.getElementById('stat-active').textContent = active;
    document.getElementById('stat-completed').textContent = completed;
}

function setFilter(filter) {
    currentFilter = filter;
    
    // Update button states
    document.querySelectorAll('.btn-filter').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-filter="${filter}"]`).classList.add('active');
    
    renderTasks();
}

function searchTasks() {
    renderTasks();
}

// UI Helper Functions
function showAuth() {
    document.getElementById('auth-view').classList.remove('hidden');
    document.getElementById('app-view').classList.add('hidden');
}

function showApp() {
    document.getElementById('auth-view').classList.add('hidden');
    document.getElementById('app-view').classList.remove('hidden');
    
    // Update user info
    if (currentUser) {
        document.getElementById('user-name').textContent = currentUser.username;
        document.getElementById('user-email').textContent = currentUser.email || 'user@example.com';
        document.getElementById('user-avatar').textContent = currentUser.username.charAt(0).toUpperCase();
    }
}

function showLoginForm() {
    document.getElementById('register-form-container').classList.add('hidden');
    document.getElementById('login-form-container').classList.remove('hidden');
}

function showRegisterForm() {
    document.getElementById('login-form-container').classList.add('hidden');
    document.getElementById('register-form-container').classList.remove('hidden');
}

function showAlert(message, type = 'success') {
    const alertContainer = document.getElementById('alert-container');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `
        <span>${type === 'success' ? '✓' : '✗'}</span>
        <span>${message}</span>
    `;
    
    alertContainer.appendChild(alert);
    
    setTimeout(() => {
        alert.remove();
    }, 4000);
}

function showLoading(buttonId) {
    const button = document.getElementById(buttonId);
    button.disabled = true;
    button.innerHTML = '<span class="loading"></span> Loading...';
}

function hideLoading(buttonId, text) {
    const button = document.getElementById(buttonId);
    button.disabled = false;
    button.innerHTML = text;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'Today';
    if (diffDays === 1) return 'Yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
