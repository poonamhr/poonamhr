function showInfo(id) {
    const boxes = document.querySelectorAll('.info-box');

    boxes.forEach(box => {
        if (box.id === id) {
            if (box.classList.contains('show')) {
                box.classList.remove('show'); 
            } else {
                box.classList.add('show'); 
            }
        } else {
            box.classList.remove('show'); 
        }
    });
}
