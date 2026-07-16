from fpdf import FPDF

def main():
    text = input("Name: ")
    get_shirtificate(text)

def get_shirtificate(txt):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # Add the page and image
    pdf.add_page()
    pdf.image("shirt.png", x=13, y=40, w=180, h=200)

    # Set the main text "CS50 Shirtificate"
    pdf.set_font("helvetica", style="B", size=38)
    pdf.cell(text="CS50 Shirtificate", center=True)

    # Set the secondary text
    pdf.set_font("helvetica", size=21)
    pdf.set_y(110)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(text=f"{txt} took CS50", center=True)

    # Save the file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

