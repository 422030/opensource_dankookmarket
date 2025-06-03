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
  body: JSON.stringify({ username, password }),
  })
    .then(async (res) => {
      if (!res.ok) {
        const errorData = await res.json().catch(() => null);
        const message = errorData?.error || "해당 로그인 정보가 없습니다.";
        throw new Error(message);
      }
      return res.json();
    })
    .then((data) => {
      localStorage.setItem("username", username);
      localStorage.setItem("isAdmin", data.is_admin);
      localStorage.setItem("user_id", data.user_id);
      window.location.href = "index.html";
    })
    .catch((err) => {
      alert(err.message || "서버 오류로 로그인할 수 없습니다.");
      console.error(err);
    });
}
