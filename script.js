// 단근마켓 기능 연결 스크립트

// 교재 등록 버튼 → add_book.html 이동
const addBookBtn = document.getElementById('addBookBtn');
if (addBookBtn) {
    addBookBtn.addEventListener('click', () => {
        window.location.href = 'add_book.html';
    });
}

// 공동구매 등록 버튼 → group_buy.html 이동
const groupBuyBtn = document.getElementById('groupBuyBtn');
if (groupBuyBtn) {
    groupBuyBtn.addEventListener('click', () => {
        window.location.href = 'group_buy.html';
    });
}

// 검색 필터 버튼 클릭
const searchButton = document.querySelector('.search-filter button');
if (searchButton) {
    searchButton.addEventListener('click', () => {
        const searchValue = document.getElementById('searchBar').value.trim();
        const categoryValue = document.getElementById('categoryFilter').value;

        console.log('검색어:', searchValue || '없음');
        console.log('선택한 카테고리:', categoryValue || '전체');
    });
}
