function toggleContent(contentId) {
    let content = document.getElementById(contentId);

    if (content.style.display === "block") {
        content.style.display = "none"; 
    } else {
        content.style.display = "block"; 
    }
}

function checkAnswers() {
    const answers = {
        q1: 'b',
        q2: 'a',
        q3: 'b',
        q4: 'b',
        q5: 'a',
        q6: 'b',
        q7: 'a',
        q8: 'c',
        q9: 'a',
        q10: 'a'
    };

    let score = 0;
    for (let q in answers) {
        const selected = document.querySelector(`input[name="${q}"]:checked`);
        if (selected && selected.value === answers[q]) {
            score++;
        }
    }

    document.getElementById("result").innerText = "You got " + score + " out of 10 correct!";
}
