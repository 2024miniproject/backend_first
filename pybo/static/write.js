// 제목 입력 필드의 너비를 텍스트 길이에 따라 조정하는 함수
const titleField = document.getElementById('titlearea');
titleField.addEventListener('input', function() {
  this.style.width = 'auto'; // 너비 재설정
  this.style.width = this.scrollWidth + 'px'; // 텍스트 길이에 맞춰 확장
});

// 가격 입력 필드에 숫자만 입력되도록 제한 (텍스트 필드 사용 중)
const priceField = document.getElementById('pricearea');
priceField.addEventListener('input', function(e) {
  // 입력 값 중 숫자가 아닌 문자는 제거
  this.value = this.value.replace(/[^0-9]/g, '');
});

//하고 싶었는데 왜인지 적용안됨 아 눈물나 