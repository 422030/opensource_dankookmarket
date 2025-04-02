document.getElementById('addBookBtn').addEventListener('click', function() {
    window.location.href = 'add_book.html'; // 교재 등록 페이지로 이동
});

document.getElementById('groupBuyBtn').addEventListener('click', function() {
    window.location.href = 'group_buy.html'; // 공동구매 등록 페이지로 이동
});

// 검색 필터 (단순화된 예시)
document.querySelector('.search-filter button').addEventListener('click', function() {
    const searchValue = document.getElementById('searchBar').value;
    const categoryValue = document.getElementById('categoryFilter').value;

    console.log('검색어:', searchValue);
    console.log('카테고리:', categoryValue);
    
    // 여기에 검색 결과 필터링 로직을 추가할 수 있습니다
});
