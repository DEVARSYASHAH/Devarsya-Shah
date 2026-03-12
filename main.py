import os
from fasthtml.common import *
from starlette.staticfiles import StaticFiles

from data import experiences, projects, education, services

app = FastHTML(
    hdrs=(
        Title("Devarsya Shah"),
        Link(rel="icon", type="image/svg+xml", href="/static/favicon.svg"),
    )
)

# ---------------- STATIC FILES ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# ---------------- COMPONENTS ----------------

def ExperienceCard(exp):
    return Div(
        H3(exp["title"]),
        P(exp["role"], cls="exp-role"),
        P(exp["duration"], cls="exp-duration"),
        Ul(*[Li(point) for point in exp["points"]]),
        cls="exp-card"
    )


def ProjectCard(p):

    actions = [
        A("GitHub", href=p["github"], target="_blank", cls="card-btn github")
    ]

    # Show Live button only if it exists
    if p.get("live"):
        actions.append(
            A("Live", href=p["live"], target="_blank", cls="card-btn live")
        )

    return Div(
        Div(p["name"], cls="card-title"),
        Div(p["desc"], cls="card-desc"),

        Div(
            *[Span(t, cls="tech-badge") for t in p["tech"]],
            cls="tech-row"
        ),

        Div(
            *actions,
            cls="card-actions"
        ),

        cls="project-card"
    )


def EducationItem(ed):
    return Div(
        Div(cls="timeline-dot"),
        Div(
            H3(ed["degree"]),
            P(ed["school"], cls="edu-school"),
            P(ed["duration"], cls="edu-duration"),
            P(ed["desc"], cls="edu-desc"),
            cls="timeline-content"
        ),
        cls="timeline-item"
    )


def ServiceCard(s):
    return Div(
        H3(s["title"]),
        P(s["desc"]),
        cls="service-card"
    )

# ---------------- ROUTE ----------------


@app.route("/")
def home():

    return Html(
        Head(

            Title("Devarsya Shah | Portfolio"),

            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Meta(name="description",
                 content="Portfolio of Devarsya Shah – AI Systems and Distributed Engineering"),

            # Icons
            Script(src="https://unpkg.com/lucide@latest"),

            # CSS (cache busting)
            Link(rel="stylesheet", href="/static/style.css?v=2"),

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
                        "Software engineer building AI-driven systems and distributed "
                        "architectures focused on scalable backend engineering.",
                        cls="description"
                    ),

                    Div(

                        Div(
                            I(**{"data-lucide": "map-pin"}),
                            Span("Thuringia, Germany"),
                            cls="location"
                        ),

                        A(I(**{"data-lucide": "mail"}),
                          href="mailto:test@gmail.com"),

                        A(I(**{"data-lucide": "linkedin"}), href="#"),

                        A(I(**{"data-lucide": "github"}), href="#"),

                        Button(
                            I(**{"data-lucide": "moon"}),
                            id="themeToggle"
                        ),

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

                *[ExperienceCard(exp) for exp in experiences],

                cls="experience-section"

            ),

            # ---------------- PROJECTS ----------------

            Div(

                H2("$ projects", cls="section-title"),

                Div(
                    *[ProjectCard(p) for p in projects],
                    cls="projects-grid"
                ),

                cls="projects-section"

            ),

            # ---------------- EDUCATION ----------------

            Div(

                H2("$ education", cls="section-title"),

                Div(
                    *[EducationItem(ed) for ed in education],
                    cls="timeline"
                ),

                cls="education-section"
            ),

            # ---------------- SERVICES ----------------
            Div(

                H2("$ services", cls="section-title"),

                Div(
                    *[ServiceCard(s) for s in services],
                    cls="services-grid"
                ),

                cls="services-section"
            ),

            # ---------------- Footer ----------------
            Footer(

                Div(

                    # -------- Currently Building --------
                    Div(

                        H3("$ currently-building", cls="footer-title"),

                        Ul(
                            Li("AI Infrastructure for scalable ML systems"),
                            Li("Research on distributed AI pipelines"),
                            Li("Cloud-native ML deployments"),
                            cls="footer-list"
                        ),

                        cls="footer-building"

                    ),

                    # -------- Contact / Advertisement --------
                    Div(

                        P(
                            "Have a strong project idea, research opportunity, "
                            "or collaboration in AI systems or distributed engineering?",
                            cls="footer-note"
                        ),

                        P(
                            "Feel free to reach out — I'm always open to meaningful projects.",
                            cls="footer-note"
                        ),

                        Div(
                            A(I(**{"data-lucide": "mail"}),
                              href="mailto:test@gmail.com"),
                            A(I(**{"data-lucide": "github"}),
                              href="#", target="_blank"),
                            A(I(**{"data-lucide": "linkedin"}),
                              href="#", target="_blank"),
                            cls="footer-icons"
                        ),

                        cls="footer-contact"

                    ),

                    cls="footer-container"

                ),

                Div(
                    P("© 2026 Devarsya Shah · Built with FastHTML"),
                    cls="footer-bottom"
                ),

                cls="footer"

            ),

            # Script (loaded last)
            Script(src="/static/script.js")

        )
    )


serve()
