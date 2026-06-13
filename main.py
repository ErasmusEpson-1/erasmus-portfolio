import flet as ft
import webbrowser
import os
import subprocess
import sys

def main(page: ft.Page):
    page.title = "Erasmus Episona S Portfolio"
    page.scroll = ft.ScrollMode.AUTO

    # Set assets directory to the folder where this script lives
    # Put IMG1.jpg, IMG2.jpg, project_video.mp4, and all PDFs in that same folder
    ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
    page.assets_dir = ASSETS_DIR

    content = ft.Column([
        ft.Text("Welcome to my portfolio!", size=18)
    ])

    def open_file(filename):
        """Open any file (PDF, video, image) using the OS default application."""
        filepath = os.path.join(ASSETS_DIR, filename)
        if not os.path.exists(filepath):
            page.snack_bar = ft.SnackBar(ft.Text(f"File not found: {filename}"), open=True)
            page.update()
            return
        if sys.platform == "win32":
            os.startfile(filepath)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", filepath])
        else:
            subprocess.Popen(["xdg-open", filepath])

    def open_cert1(e):
        open_file("1. Calculations with Vectors and Matrices.pdf")

    def open_cert2(e):
        open_file("2. Explore Data with MATLAB Plots.pdf")

    def open_cert3(e):
        open_file("3. Machine learning Onramp.pdf")

    def open_cert4(e):
        open_file("4. Make and Manipulate Matrices.pdf")

    def open_cert5(e):
        open_file("5. MATLAB Onramp.pdf")

    def open_cert6(e):
        open_file("6. Simulink Onramp.pdf")

    def open_video(e):
        open_file("project_video.mp4")

    def set_content(controls):
        content.controls.clear()
        content.controls.extend(controls)
        page.update()

    def show_home(e):
        set_content([
            ft.Text("Welcome to my portfolio homepage.", size=18),
            ft.Text("I am Erasmus Episona S, an Electrical Engineering student at JEDS Campus."),
            ft.Text("This portfolio showcases my engineering, programming, MATLAB and project work."),
        ])

    def show_timeline(e):
        set_content([
            ft.Text("PROJECT TIMELINE", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Week 1:\n- Installed Python\n- Installed Flet\n- Created portfolio project"),
            ft.Text("Week 2:\n- Added homepage\n- Added profile picture\n- Added navigation menu"),
            ft.Text("Week 3:\n- Developed Project Timeline section\n- Started portfolio improvements"),
            ft.Text("Week 4:\n- Preparing MATLAB Achievement Hub\n- Preparing Technical Blog\n- Preparing GitHub Evidence"),
        ])

    def show_matlab(e):
        set_content([
            ft.Text("MATLAB ACHIEVEMENT HUB", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("1. Calculations with Vectors and Matrices", on_click=open_cert1),
            ft.ElevatedButton("2. Explore Data with MATLAB Plots", on_click=open_cert2),
            ft.ElevatedButton("3. Machine Learning Onramp", on_click=open_cert3),
            ft.ElevatedButton("4. Make and Manipulate Matrices", on_click=open_cert4),
            ft.ElevatedButton("5. MATLAB Onramp", on_click=open_cert5),
            ft.ElevatedButton("6. Simulink Onramp", on_click=open_cert6),
        ])

    def show_blog(e):
        set_content([
            ft.Text("TECHNICAL BLOG", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Topics to be added:"),
            ft.Text("- MATLAB Basics\n- Circuit Analysis\n- Superposition Theorem\n- MOSFET Fundamentals\n- Electrical Engineering Concepts"),
        ])

    def show_github(e):
        # Use absolute paths so Flet can find the images regardless of working directory
        img1_path = os.path.join(ASSETS_DIR, "IMG1.png").replace("\\", "/")
        img2_path = os.path.join(ASSETS_DIR, "IMG2.png").replace("\\", "/")
        set_content([
            ft.Text("GITHUB EVIDENCE", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("My GitHub contributions and commits:"),
            ft.Image(src=img1_path, width=400, error_content=ft.Text("IMG1.png not found")),
            ft.Image(src=img2_path, width=400, error_content=ft.Text("IMG2.png not found")),
            ft.Text(
                "- Created portfolio repository\n"
                "- Made multiple commits\n"
                "- Uploaded Electrical Engineering portfolio project\n"
                "- Tracked version control using Git"
            ),
        ])

    def show_video(e):
        set_content([
            ft.Text("PROJECT CONTRIBUTION VIDEO", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Click the button below to play the video in your media player."),
            ft.ElevatedButton(
                "▶  Play project_video.mp4",
                on_click=open_video,
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
                height=48,
            ),
            ft.Divider(),
            ft.Text("My Contributions:", weight=ft.FontWeight.BOLD),
            ft.Text(
                "- Created portfolio homepage\n"
                "- Added profile picture\n"
                "- Added MATLAB Achievement Hub\n"
                "- Added Project Timeline\n"
                "- Added Technical Blog\n"
                "- Added GitHub Evidence\n\n"
                "This video demonstrates my contribution to the project."
            ),
        ])

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
            ft.ElevatedButton("Project Video", on_click=show_video),
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

    # Show home content by default
    show_home(None)

ft.app(target=main)