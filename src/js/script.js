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
async function getCurrentUser() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/accounts/me/", {
      credentials: "include", // 세션 기반 인증에 필요
    });
    if (!response.ok) throw new Error("로그인 필요");
    const user = await response.json();

    localStorage.setItem("username", user.username);
    return user.username;
  } catch (err) {
    alert("로그인이 필요합니다.");
    window.location.href = "index.html";
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  const username = await getCurrentUser();

  if (window.location.pathname.includes('search_book.html')) {
    fetchBooks();
  }
});

function fetchBooks() {
  fetch('http://127.0.0.1:8000/api/books/')
    .then(response => response.json())
    .then(data => {
      const bookList = document.getElementById('book-list');
      if (!bookList) return;

      bookList.innerHTML = '';
      data.forEach(book => {
        const li = document.createElement('li');
        li.textContent = `${book.title} - ${book.description}`;
        bookList.appendChild(li);
      });
    })
    .catch(error => console.error('책 목록 불러오기 실패:', error));
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
