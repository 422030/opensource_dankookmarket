function login() {
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  if (!username || !password) {
    alert("아이디와 비밀번호를 입력하세요.");
    return;
  }

  fetch("http://127.0.0.1:8000/users/login_api/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include", // 중요: 세션/쿠키 정보 포함
    body: JSON.stringify({ username, password }),
  })
    .then((res) => {
      if (!res.ok) throw new Error("로그인 실패");
      return res.json();
    })
    .then((data) => {
      localStorage.setItem("username", username);
      localStorage.setItem("isAdmin", data.is_admin);
      window.location.href = "index.html";
    })
    .catch((err) => {
      alert("서버 오류로 로그인할 수 없습니다.");
      console.error(err);
    });
}
