import flet as ft

def main(page: ft.Page):
    page.title = "Erasmus Episona S Portfolio"
    page.scroll = ft.ScrollMode.AUTO

    content = ft.Text(
        "Welcome to my portfolio!",
        size=18
    )

    def show_home(e):
        content.value = """
Welcome to my portfolio homepage.

I am Erasmus Episona S, an Electrical Engineering student at JEDS Campus.

This portfolio showcases my engineering, programming, MATLAB and project work.
"""
        page.update()

    def show_timeline(e):
        content.value = """
PROJECT TIMELINE

Week 1:
- Installed Python
- Installed Flet
- Created portfolio project

Week 2:
- Added homepage
- Added profile picture
- Added navigation menu

Week 3:
- Developed Project Timeline section
- Started portfolio improvements

Week 4:
- Preparing MATLAB Achievement Hub
- Preparing Technical Blog
- Preparing GitHub Evidence
"""
        page.update()

    def show_matlab(e):
        content.value = """
MATLAB ACHIEVEMENT HUB

MathWorks certificates will be displayed here.

Course : 1. Calculations with Vectors and Matrices.pdf
Course : 2. Exprole Data with MATLAB Plots.pdf 
Course : 3. Machine learning Onramp.pdf
Course : 4. Make and Manipulate Matrices.pdf
Course : 5. MATLAB Onramp.pdf
Course : 6. Simulink Onramp.
Course 7:
Course 8:
"""
        page.update()

    def show_blog(e):
        content.value = """
TECHNICAL BLOG

Topics to be added:

- MATLAB Basics
- Circuit Analysis
- Superposition Theorem
- MOSFET Fundamentals
- Electrical Engineering Concepts
"""
        page.update()

    def show_github(e):
        content.value = """
GITHUB EVIDENCE

GitHub commits, pull requests and project contributions will be displayed here.
"""
        page.update()

    profile_pic = ft.Image(
        src="IMG-20260304-WA0014.jpg.jpg",
        width=200,
        height=250,
    )

    menu = ft.Column(
        [
            ft.ElevatedButton("Home", on_click=show_home),
            ft.ElevatedButton("Project Timeline", on_click=show_timeline),
            ft.ElevatedButton("MATLAB Achievement Hub", on_click=show_matlab),
            ft.ElevatedButton("Technical Blog", on_click=show_blog),
            ft.ElevatedButton("GitHub Evidence", on_click=show_github),
        ],
        width=250
    )

    info = ft.Column(
        [
            ft.Text("Erasmus Episona S", size=30),
            ft.Text("Electrical Engineering"),
            ft.Text("JEDS Campus"),
            content,
        ]
    )

    page.add(
        ft.Row(
            [
                menu,
                profile_pic,
                info
            ]
        )
    )

ft.app(target=main)