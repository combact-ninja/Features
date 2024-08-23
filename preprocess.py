from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_image_with_text(lines, output_path, image_size=(800, 600), font_path="arial.ttf", font_size=20):
    # Create a blank image with a white background
    img = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(img)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the height of each line
    _, _, _, line_height = draw.textbbox((0, 0), "Test", font=font)

    # Calculate the starting position
    current_height = 20  # Starting at 20 pixels from the top

    # Draw each line on the image
    for line in lines:
        draw.text((20, current_height), line, font=font, fill="black")
        current_height += line_height + 10  # Move down for the next line

    # Save the image
    img.save(output_path)


def slice_and_format_text(input_list, max_chars_per_line=70):
    text = ' '.join(input_list)  # Combine the list into a single string
    lines = textwrap.wrap(text, width=max_chars_per_line)  # Wrap text into lines based on max characters per line
    return lines


# Input list
x = ['Sir', 'Ganga', 'Ram', 'Hospital', 'Sir', 'New', 'Ganga', 'Ram', 'Hospital', 'Marg', 'Rajinder', 'Nagar',
     'Delhi', 'INDIA', 'Tel', '+', 'Sir', 'Medical', 'Ganga', 'Superintendent', 'Ram', 'Kolmet', 'Hospital',
     'Offg', 'B', 'Pusa', 'Road', 'New', 'Delhi', 'Tel', '+', 'D', 'Dr', 'Raj', 'Kamal', 'Agarwal', 'of',
     'Sr', 'Consultant', 'Pain', 'Deptt', 'Peri', 'Operative', 'Anaesthesiology', 'Medicine', 'Email',
     'kamaagarwagogmailcom', 'Mobile', '+', 'TO', 'WHOM', 'IT', 'MAY', 'CONCERN', 'the', 'conbacli', 'ICMR',
     'As', 'pex', 'guideline', 'COVID', 'tve', 'Canes', 'gliould', 'lar', 'pub', 'ow', 'HOME', 'Mild',
     'amuptone', 'ISOLATION', 'even', 'mth', 'It', 'io', 'aduised', 'Thal', 'evesybody', 'takeg', 'bheal',
     'medication', 'apont', 'trem', 'tolloning', 'prevestive', 'HAND', 'HYGIENE', 'WEARNG', 'SOCIAL',
     'DISTANCING', 'MASK', 'ky', 'Mg', 'enel', 'a', 'week', 'TAB', 'HYDROYYCHLDRDQUINE', 'VITAMIN', 'C',
     'INC', 'In', 'casl', 'TAB', 'one', 'omam', 'encl', 'O', 'TAB', 'TAB', 'doy', 'mg', 'onle', 'a', 'day',
     'evek', 'CROUN', 'CALPOL', 'SD', 'SDS', 'Ahaoat', 'pair', 'lomg', 'Once', 'a', 'Tea', 'obm', '[r',
     'casl', 'X', 'cot', 'e', 'SYRUP', 'TAB', 'CETRIZINE', 'ALEX', 'A', 'e', 'adoy', 'DR', 'RAIKAMALA',
     'DEPI', 'SIR', 'SALIT', 'AGARWAL', 'DA', 'a', 'S', 'PAIN', 'CO', 'Residence', 'Royalton', 'Tower',
     'Princeton', 'Estate', 'DLF', 'PhaseV', 'Gurugram', 'Na']

# Format the text into lines
lines = slice_and_format_text(x)

# Path to save the output image
output_image_path = "output_image.png"

# Create and save the image with the formatted text
create_image_with_text(lines, output_image_path)



# ----------------------------------------------------------- list of fonts --------------------------------------------------
# Dancing Script
# Pacifico
# Patrick Hand
# Great Vibes
# Homemade Apple
# Caveat
# Satisfy
# Amatic SC
# Shadows Into Light
# Indie Flower
# Kaushan Script
# Just Another Hand
# Reenie Beanie
# Rock Salt
# Sacramento
# Gloria Hallelujah
# Allura
# Zeyada
# Alex Brush
# Nanum Pen Script
