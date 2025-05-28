// script.js

// 로그인 관련 유틸
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

// 페이지 이동 버튼
const addBookBtn = document.getElementById('addBookBtn');
if (addBookBtn) {
  addBookBtn.addEventListener('click', function () {
    window.location.href = 'add_book.html';
  });
}

const groupBuyBtn = document.getElementById('groupBuyBtn');
if (groupBuyBtn) {
  groupBuyBtn.addEventListener('click', function () {
    window.location.href = 'group_buy.html';
  });
}

// 검색 필터 (예시)
const searchBtn = document.querySelector('.search-filter button');
if (searchBtn) {
  searchBtn.addEventListener('click', function () {
    const searchValue = document.getElementById('searchBar')?.value || '';
    const categoryValue = document.getElementById('categoryFilter')?.value || '';
    console.log('검색어:', searchValue);
    console.log('카테고리:', categoryValue);
    // TODO: 검색 필터링 로직 구현 예정
  });
}
