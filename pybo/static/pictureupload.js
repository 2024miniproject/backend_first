function handleFile(event) {
    const files = event.target.files;
    const container = document.getElementById('image-container');

    // 기존 이미지 미리보기 삭제
    container.innerHTML = '';

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.className = 'image-preview';
            container.appendChild(img);
        };

        reader.readAsDataURL(file);
    }
}