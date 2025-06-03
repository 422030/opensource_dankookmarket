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
//index.html 코드 정리 위해서 옮김
const username = localStorage.getItem("username");
const loginArea = document.getElementById("loginArea");
const myBooksSection = document.getElementById("myBooksSection");
const myBooksEl = document.getElementById("myBooks");

if (username) {
  loginArea.innerHTML = `<p><strong>${username}님 환영합니다!</strong></p><button onclick="logout()">로그아웃</button>`;
  myBooksSection.style.display = "block";

  const books = JSON.parse(localStorage.getItem("books") || "[]");
  const myBooks = books.filter(book => book.writer === username);

  if (myBooks.length === 0) {
    myBooksEl.innerHTML = "<p>등록한 교재가 없습니다.</p>";
  } else {
    myBooksEl.innerHTML = myBooks.map((book, i) => `
      <div style="border:1px solid #ccc; padding:10px; margin:10px 0;">
        ${i + 1}. <strong>${book.title}</strong> - ${book.price}원 (${book.category})<br/>
        💬 ${book.comment}
      </div>
    `).join('');
  }
}

function logout() {
  localStorage.removeItem("username");
  localStorage.removeItem("isAdmin");
  location.reload();
}

// 백엔드 API 연결 확인
fetch('http://127.0.0.1:8000/users/ping/')
  .then(res => res.json())
  .then(data => {
    console.log('✅ API 연결 성공:', data);
  })
  .catch(err => {
    console.error('❌ API 호출 실패:', err);
  });
//여기까지 정리용 코드

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
