// script.js

function isLoggedIn() {
  return !!localStorage.getItem('username');
}

function getUser() {
  return localStorage.getItem('username');
}

function isAdmin() {
  return localStorage.getItem('isAdmin') === 'true';
}

function logout() {
  localStorage.removeItem('username');
  localStorage.removeItem('isAdmin');
  window.location.href = 'index.html';
}
