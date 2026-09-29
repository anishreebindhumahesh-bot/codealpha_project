const questions = [
    {
        question: "You receive an email asking for your OTP. What should you do?",
        options: [
            "Share the OTP",
            "Ignore and verify through the official website",
            "Reply with your password",
            "Forward it to friends"
        ],
        answer: 1
    },

    {
        question: "Which is a common sign of phishing?",
        options: [
            "Urgent request for sensitive information",
            "Normal newsletter",
            "Expected message from a known contact",
            "Official website bookmark"
        ],
        answer: 0
    },

    {
        question: "What should you check before clicking a link?",
        options: [
            "The message color",
            "The sender's profile picture",
            "The destination URL",
            "The font size"
        ],
        answer: 2
    },

    {
        question: "What is social engineering?",
        options: [
            "A programming language",
            "Manipulating people to reveal information",
            "A type of antivirus",
            "A computer operating system"
        ],
        answer: 1
    },

    {
        question: "What is a good way to protect online accounts?",
        options: [
            "Share passwords with friends",
            "Use the same password everywhere",
            "Enable multi-factor authentication",
            "Disable security updates"
        ],
        answer: 2
    }
];

let currentQuestion = 0;
let score = 0;

function startQuiz() {
    currentQuestion = 0;
    score = 0;
    showQuestion();
}

function showQuestion() {
    const q = questions[currentQuestion];

    let message = q.question + "\n\n";

    q.options.forEach((option, index) => {
        message += (index + 1) + ". " + option + "\n";
    });

    const answer = prompt(message);

    if (answer === null) {
        return;
    }

    const selected = parseInt(answer) - 1;

    if (selected === q.answer) {
        score++;
        alert("✅ Correct!");
    } else {
        alert("❌ Incorrect.\nCorrect answer: " + q.options[q.answer]);
    }

    currentQuestion++;

    if (currentQuestion < questions.length) {
        showQuestion();
    } else {
        alert(
            "🎉 Quiz completed!\n\n" +
            "Your score: " + score + "/" + questions.length
        );
    }
}
