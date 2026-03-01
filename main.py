import os
from fasthtml.common import *
from starlette.staticfiles import StaticFiles

app = FastHTML()

# ----------------------------
# STATIC FILES
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ----------------------------
# DATA
# ----------------------------

experiences = [
    {
        "title": "LFX'25",
        "role": "SDE Intern — Headlamp",
        "duration": "June 2025 – Aug 2025 · Remote",
        "points": [
            "Built a Golang-based caching layer for Kubernetes APIs.",
            "Improved CI reliability with 61% test coverage.",
            "Integrated optional in-memory cache layer.",
            "Laid foundation for pagination & search."
        ],
    },
    {
        "title": "Open Source",
        "role": "Backend Contributor",
        "duration": "2024 – Present",
        "points": [
            "Contributed to distributed system modules.",
            "Optimized performance-critical APIs.",
            "Improved documentation and test coverage."
        ],
    },
    {
        "title": "Open Source",
        "role": "Backend Contributor",
        "duration": "2024 – Present",
        "points": [
            "Contributed to distributed system modules.",
            "Optimized performance-critical APIs.",
            "Improved documentation and test coverage."
        ],
    }
]

projects = [
    {
        "name": "DevOps Platform",
        "desc": "CI/CD automation platform with Docker & Kubernetes deployment.",
        "github": "https://github.com/yourrepo",
        "live": "https://yourliveapp.com",
        "tech": ["Go", "Docker", "Kubernetes"]
    },
    {
        "name": "AI Analytics Engine",
        "desc": "Real-time analytics system powered by Python and ML models.",
        "github": "https://github.com/yourrepo",
        "live": "https://yourliveapp.com",
        "tech": ["Python", "FastAPI", "PostgreSQL"]
    },
    {
        "name": "Cloud Dashboard",
        "desc": "Modern cloud monitoring dashboard with RBAC system.",
        "github": "https://github.com/yourrepo",
        "live": "https://yourliveapp.com",
        "tech": ["React", "Node.js", "MongoDB"]
    },
    {
        "name": "Automation Toolkit",
        "desc": "Task automation and background job processing system.",
        "github": "https://github.com/yourrepo",
        "live": "https://yourliveapp.com",
        "tech": ["Python", "Redis", "Docker"]
    },
]

# ----------------------------
# ROUTE
# ----------------------------

@app.route("/")
def home():
    return Html(
        Head(
            Title("Devarsya Shah | Portfolio"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Script(src="https://unpkg.com/lucide@latest"),
            Link(rel="stylesheet", href="/static/style.css"),
        ),

        Body(

            # ---------------- HERO ----------------
            Div(
                Div(
                    P("> ", Span(id="typing"), cls="typewriter"),
                    H1("Devarsya Shah"),
                    P(
                        "AI Systems · Software Engineer · Distributed Systems",
                        cls="subtitle"
                    ),
                    P(
                        "Software engineer building AI-driven systems and distributed architectures, "
                        "focused on scalable backend engineering and production-ready applications.",
                        cls="description"
                    ),

                    Div(
                        Div(
                            I(**{"data-lucide": "map-pin"}),
                            Span("Thuringia, Germany"),
                            cls="location"
                        ),
                        A(I(**{"data-lucide": "mail"}), href="mailto:test@gmail.com"),
                        A(I(**{"data-lucide": "linkedin"}), href="#"),
                        A(I(**{"data-lucide": "github"}), href="#"),
                        Button(I(**{"data-lucide": "moon"}), id="themeToggle"),
                        cls="icons"
                    ),
                    cls="left"
                ),

                Div(
                    Img(src="/static/profile.png"),
                    cls="right"
                ),

                cls="container"
            ),

            # ---------------- EXPERIENCE ----------------
            Div(
                H2("$ experience", cls="section-title"),

                *[
                    Div(
                        H3(exp["title"]),
                        P(exp["role"], cls="exp-role"),
                        P(exp["duration"], cls="exp-duration"),
                        Ul(*[Li(point) for point in exp["points"]]),
                        cls="exp-card"
                    )
                    for exp in experiences
                ],

                cls="experience-section"
            ),

            # ---------------- PROJECTS GRID ----------------
            Div(
                H2("$ projects", cls="section-title"),

                Div(
                    *[
                        Div(
                            Div(p["name"], cls="card-title"),
                            Div(p["desc"], cls="card-desc"),

                            Div(
                                *[Span(t, cls="tech-badge") for t in p["tech"]],
                                cls="tech-row"
                            ),

                            Div(
                                A("GitHub", href=p["github"], target="_blank",
                                  cls="card-btn github"),
                                A("Live", href=p["live"], target="_blank",
                                  cls="card-btn live"),
                                cls="card-actions"
                            ),

                            cls="project-card"
                        )
                        for p in projects
                    ],
                    cls="projects-grid"
                ),

                cls="projects-section"
            ),

            Script(src="/static/script.js")
        )
    )
serve()