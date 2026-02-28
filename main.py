import os
from fasthtml.common import *
from starlette.staticfiles import StaticFiles

app = FastHTML()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.route("/")
def home():
    return Html(
        Head(
            Title("Devarsya Shah | Portfolio"),

            # Lucide Icons CDN
            Script(src="https://unpkg.com/lucide@latest"),

            Style("""
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    background-color: #0d0d0d;
                    color: #e5e5e5;
                    font-family: 'Segoe UI', monospace;
                    transition: background 0.3s ease, color 0.3s ease;
                }

                .container {
                    max-width: 1200px;
                    margin: auto;
                    padding: 80px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 60px;
                }

                .left { flex: 1; }

                .typewriter {
                    color: #9ca3af;
                    font-size: 14px;
                    margin-bottom: 20px;
                    border-right: 2px solid #9ca3af;
                    white-space: nowrap;
                    overflow: hidden;
                    width: fit-content;
                    animation: blink 1s infinite;
                }

                @keyframes blink {
                    50% { border-color: transparent; }
                }

                h1 {
                    font-size: 56px;
                    font-weight: 700;
                    margin-bottom: 20px;
                }

                .subtitle {
                    color: #60a5fa;
                    font-size: 18px;
                    margin-bottom: 25px;
                }

                .description {
                    color: #a1a1aa;
                    line-height: 1.7;
                    max-width: 600px;
                    margin-bottom: 35px;
                }

                /* ICON SECTION */
                .icons {
                    display: flex;
                    align-items: center;
                    gap: 24px;
                }

                .icons a,
                .icons button,
                .location {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    text-decoration: none;
                    font-size: 14px;
                    color: #a1a1aa;
                    transition: all 0.25s ease;
                }

                .icons svg {
                    width: 20px;
                    height: 20px;
                    stroke-width: 1.8;
                }

                .icons a:hover,
                .icons button:hover {
                    color: #60a5fa;
                    transform: translateY(-2px);
                }

                .icons button {
                    background: none;
                    border: none;
                    cursor: pointer;
                }

                .location {
                    color: #d4d4d8;
                }
                



                .right img {
                    width: 280px;
                    border-radius: 10px;
                    filter: grayscale(100%);
                    transition: all 0.3s ease;
                }

                /* LIGHT MODE PHOTO BORDER */
                .light-mode .right img {
                    border: 3px solid #000100;
                    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
                }

                /* LIGHT MODE */
                .light-mode {
                    background-color: #ffffff;
                    color: #111;
                }

                .light-mode .description {
                    color: #444;
                }

                .light-mode .subtitle {
                    color: #2563eb;
                }

                .light-mode .icons a,
                .light-mode .icons button {
                    color: #444;
                }

                .light-mode .location {
                    color: #111;
                }

                .light-mode .icons a:hover,
                .light-mode .icons button:hover {
                    color: #2563eb;
                }

                @media (max-width: 900px) {
                    .container {
                        flex-direction: column;
                        text-align: center;
                    }

                    .description {
                        margin: auto;
                    }

                    .icons {
                        justify-content: center;
                    }

                    .right img {
                        width: 220px;
                        margin-top: 40px;
                    }
                }
            """)
        ),

        Body(
            Div(
                Div(
                    P("> ", Span(id="typing"), cls="typewriter"),

                    H1("Devarsya Shah"),

                    P("AI Systems · Software Engineer · Distributed Systems", cls="subtitle"),

                    P(
                        "Software engineer building AI-driven systems and distributed architectures, "
                        "focused on scalable backend engineering, performance optimization, and production-ready intelligent applications.",
                        cls="description"
                    ),

                    Div(
                        Div(
                            I(**{"data-lucide": "map-pin"}),
                            Span("Thuringia, Germany"),
                            cls="location"
                        ),

                        A(I(**{"data-lucide": "mail"}), href="mailto:yourmail@gmail.com", target="_blank"),
                        A(I(**{"data-lucide": "linkedin"}), href="https://linkedin.com/in/yourprofile", target="_blank"),
                        A(I(**{"data-lucide": "github"}), href="https://github.com/yourusername", target="_blank"),

                        Button(I(**{"data-lucide": "moon"}), id="themeToggle"),

                        cls="icons"
                    ),

                    cls="left"
                ),

                Div(
                    Img(src="/static/profile.jpeg"),
                    cls="right"
                ),

                cls="container"
            ),

            Script("""
                // Activate Lucide icons
                lucide.createIcons();

                // TYPEWRITER EFFECT
                const text = "> I work at the intersection of AI systems and distributed engineering";
                let index = 0;
                const speed = 50;

                function typeEffect() {
                    if (index < text.length) {
                        document.getElementById("typing").innerHTML += text.charAt(index);
                        index++;
                        setTimeout(typeEffect, speed);
                    }
                }
                typeEffect();

                // THEME SYSTEM
                const toggleBtn = document.getElementById("themeToggle");

                function setTheme(theme) {
                    if (theme === "light") {
                        document.body.classList.add("light-mode");
                        toggleBtn.innerHTML = '<i data-lucide="sun"></i>';
                    } else {
                        document.body.classList.remove("light-mode");
                        toggleBtn.innerHTML = '<i data-lucide="moon"></i>';
                    }
                    lucide.createIcons();
                }

                const savedTheme = localStorage.getItem("theme") || "dark";
                setTheme(savedTheme);

                toggleBtn.addEventListener("click", () => {
                    const newTheme = document.body.classList.contains("light-mode")
                        ? "dark"
                        : "light";
                    localStorage.setItem("theme", newTheme);
                    setTheme(newTheme);
                });
            """)
        )
    )


serve()
