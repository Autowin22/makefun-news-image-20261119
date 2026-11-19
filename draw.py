#!/usr/bin/env python3
"""
draw.py - Generates the newspaper front page image entry.png for 19 November 2026.
Standard Library + PIL only. Deterministic, byte-identical output.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def wrap_text(text, font, max_width):
    """Wraps text into lines strictly fitting within max_width pixels using font.getlength."""
    words = text.split()
    if not words:
        return []
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if font.getlength(test_line) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def main():
    # Canvas setup: 1024x1024 pixels, white background
    img = Image.new("RGB", (1024, 1024), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Fonts configuration
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    reg_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

    font_title = ImageFont.truetype(bold_path, 34)
    font_sub = ImageFont.truetype(bold_path, 11)
    font_lead_head = ImageFont.truetype(bold_path, 16)
    font_lead_body = ImageFont.truetype(reg_path, 12)
    font_med_head = ImageFont.truetype(bold_path, 14)
    font_med_body = ImageFont.truetype(reg_path, 11)
    font_small_head = ImageFont.truetype(bold_path, 12)
    font_small_body = ImageFont.truetype(reg_path, 10)

    # Colors
    c_black = "#111111"
    c_red = "#990000"
    c_navy = "#1A2B4C"
    c_gray = "#666666"
    c_light_bg = "#F9F9F9"

    # --- MASTHEAD ---
    # Top decorative red bar
    draw.rectangle([20, 20, 1004, 28], fill=c_red)

    # Title
    draw.text((20, 36), "THE WORLD IN ONE PAGE", fill=c_black, font=font_title)

    # Date & edition info
    date_str = "THURSDAY, 19 NOVEMBER 2026  •  GLOBAL EDITION  •  ISSUE NO. 323"
    draw.text((20, 78), date_str, fill=c_navy, font=font_sub)

    # Horizontal double rule below masthead
    draw.line([(20, 96), (1004, 96)], fill=c_navy, width=3)
    draw.line([(20, 101), (1004, 101)], fill=c_black, width=1)

    # --- LAYOUT GEOMETRY ---
    # Left column: x = 20 to 650 (width = 630)
    # Right column: x = 674 to 1004 (width = 330)
    # Divider between columns at x = 662

    draw.line([(662, 110), (662, 1004)], fill=c_gray, width=1)

    # ----------------------------------------------------
    # LEFT COLUMN BLOCKS
    # ----------------------------------------------------

    # 1. LEAD STORY: TRUMP, XI & PUTIN TRILATERAL SUMMIT (y: 110 to 400)
    draw.rectangle([20, 110, 650, 400], fill=c_light_bg, outline=c_navy, width=1)
    
    # Lead badge / kicker
    draw.rectangle([30, 120, 180, 136], fill=c_red)
    draw.text((35, 122), "WORLD LEAD • APEC", fill="#FFFFFF", font=font_sub)

    lead_head = "TRUMP, XI & PUTIN HOLD FIRST-EVER TRILATERAL SUMMIT IN SHENZHEN ON NUCLEAR ARMS CONTROL"
    lead_lines = wrap_text(lead_head, font_lead_head, 610)
    y_curr = 144
    for line in lead_lines:
        draw.text((30, y_curr), line, fill=c_black, font=font_lead_head)
        y_curr += 20

    lead_body = (
        "Donald Trump, Xi Jinping, and Vladimir Putin convened for a historic first-ever three-way "
        "summit in Shenzhen on Thursday on the sidelines of APEC, with nuclear arms control at the centre "
        "of discussions. Trump also held a bilateral meeting and working lunch with Xi, and a one-on-one "
        "with Putin. Putin stated he expects 'big potential benefit' from the talks. Xi greeted Trump "
        "on the tarmac in Shenzhen on Wednesday."
    )
    lead_body_lines = wrap_text(lead_body, font_lead_body, 490)
    y_body = y_curr + 6
    for line in lead_body_lines:
        draw.text((30, y_body), line, fill=c_black, font=font_lead_body)
        y_body += 16

    # Pictogram for Summit (three flag podium on the right side of lead block)
    # Draw three mini podium pillars with flags
    box_x = 520
    box_y = y_curr + 4
    draw.rectangle([box_x, box_y, box_x + 100, box_y + 110], fill="#FFFFFF", outline=c_navy, width=1)
    # Flags
    draw.line([(box_x + 25, box_y + 90), (box_x + 25, box_y + 20)], fill=c_black, width=2)
    draw.rectangle([box_x + 25, box_y + 20, box_x + 50, box_y + 40], fill=c_red)

    draw.line([(box_x + 50, box_y + 90), (box_x + 50, box_y + 20)], fill=c_black, width=2)
    draw.rectangle([box_x + 50, box_y + 25, box_x + 75, box_y + 45], fill=c_navy)

    draw.line([(box_x + 75, box_y + 90), (box_x + 75, box_y + 20)], fill=c_black, width=2)
    draw.rectangle([box_x + 75, box_y + 20, box_x + 100, box_y + 40], fill="#006600")

    draw.text((box_x + 15, box_y + 92), "SHENZHEN APEC", fill=c_black, font=ImageFont.truetype(bold_path, 8))


    # 2. ANTHROPIC IPO (y: 410 to 625)
    draw.rectangle([20, 410, 650, 625], fill="#FFFFFF", outline=c_navy, width=1)
    draw.text((30, 418), "BUSINESS • TECH IPO", fill=c_red, font=font_sub)

    anth_head = "ANTHROPIC PRICES RECORD $81.3B IPO AT $1.5T VALUATION"
    anth_lines = wrap_text(anth_head, font_med_head, 500)
    y_curr = 434
    for line in anth_lines:
        draw.text((30, y_curr), line, fill=c_black, font=font_med_head)
        y_curr += 18

    anth_body = (
        "Anthropic priced its IPO at $83 a share on Wednesday evening, raising $81.3 billion — the largest "
        "IPO ever, topping SpaceX — at a valuation of about $1.5 trillion. Shares start trading Thursday on "
        "Nasdaq under the ticker ANT, marking the first major public listing by a frontier AI lab."
    )
    anth_body_lines = wrap_text(anth_body, font_med_body, 500)
    y_body = y_curr + 4
    for line in anth_body_lines:
        draw.text((30, y_body), line, fill=c_black, font=font_med_body)
        y_body += 15

    # Stock Chart Pictogram
    sc_x, sc_y = 540, 430
    draw.rectangle([sc_x, sc_y, sc_x + 90, sc_y + 90], fill=c_light_bg, outline=c_navy, width=1)
    draw.line([(sc_x + 10, sc_y + 75), (sc_x + 30, sc_y + 55), (sc_x + 50, sc_y + 65), (sc_x + 80, sc_y + 20)], fill=c_red, width=3)
    draw.text((sc_x + 15, sc_y + 75), "ANT $83", fill=c_black, font=ImageFont.truetype(bold_path, 9))


    # 3. GRAND THEFT AUTO VI (y: 635 to 850)
    draw.rectangle([20, 635, 650, 850], fill=c_light_bg, outline=c_navy, width=1)
    draw.text((30, 643), "CULTURE • GAMING", fill=c_red, font=font_sub)

    gta_head = "GTA VI BEGINS GLOBAL ROLLOUT AFTER $1B+ COST; SCORES 99"
    gta_lines = wrap_text(gta_head, font_med_head, 500)
    y_curr = 659
    for line in gta_lines:
        draw.text((30, y_curr), line, fill=c_black, font=font_med_head)
        y_curr += 18

    gta_body = (
        "Grand Theft Auto VI begins its global rollout on Thursday, unlocking at midnight in each market "
        "starting with New Zealand, 13 years after GTA V and after more than $1 billion in production costs. "
        "Early reviews give it a Metacritic score of 99. It plays on PlayStation 5 and Xbox Series X|S, "
        "set in Vice City, Leonida, with leads Lucia Caminos and Jason Duval."
    )
    gta_body_lines = wrap_text(gta_body, font_med_body, 500)
    y_body = y_curr + 4
    for line in gta_body_lines:
        draw.text((30, y_body), line, fill=c_black, font=font_med_body)
        y_body += 15

    # Game controller pictogram
    gc_x, gc_y = 540, 655
    draw.rectangle([gc_x, gc_y, gc_x + 90, gc_y + 90], fill="#FFFFFF", outline=c_navy, width=1)
    draw.rectangle([gc_x + 20, gc_y + 35, gc_x + 70, gc_y + 65], fill=c_navy)
    draw.ellipse([gc_x + 25, gc_y + 42, gc_x + 35, gc_y + 52], fill="#FFFFFF")
    draw.ellipse([gc_x + 55, gc_y + 42, gc_x + 65, gc_y + 52], fill=c_red)
    draw.text((gc_x + 22, gc_y + 72), "VICE CITY", fill=c_black, font=ImageFont.truetype(bold_path, 8))


    # 4. US AI CYBER WARNING (y: 860 to 1000)
    draw.rectangle([20, 860, 650, 1000], fill="#FFFFFF", outline=c_navy, width=1)
    draw.text((30, 868), "NATIONAL SECURITY • CYBER", fill=c_red, font=font_sub)

    cy_head = "SENATORS WARN AI CYBER THREATS OUTPACING US DEFENCES"
    cy_lines = wrap_text(cy_head, font_med_head, 610)
    y_curr = 884
    for line in cy_lines:
        draw.text((30, y_curr), line, fill=c_black, font=font_med_head)
        y_curr += 18

    cy_body = (
        "US senators warned the White House on Thursday that AI-enabled cyber threats are rapidly outpacing "
        "current US defense capabilities, urging immediate federal action."
    )
    cy_body_lines = wrap_text(cy_body, font_med_body, 610)
    y_body = y_curr + 2
    for line in cy_body_lines:
        draw.text((30, y_body), line, fill=c_black, font=font_med_body)
        y_body += 15


    # ----------------------------------------------------
    # RIGHT COLUMN BLOCKS (x: 674 to 1004)
    # ----------------------------------------------------

    right_x = 674
    right_w = 330

    def draw_right_story(y_top, y_bot, category, headline, body):
        draw.rectangle([right_x, y_top, right_x + right_w, y_bot], fill=c_light_bg, outline=c_navy, width=1)
        draw.text((right_x + 10, y_top + 6), category, fill=c_red, font=font_sub)
        
        h_lines = wrap_text(headline, font_small_head, right_w - 20)
        y = y_top + 20
        for line in h_lines:
            draw.text((right_x + 10, y), line, fill=c_black, font=font_small_head)
            y += 14

        b_lines = wrap_text(body, font_small_body, right_w - 20)
        y += 2
        for line in b_lines:
            if y < y_bot - 12:
                draw.text((right_x + 10, y), line, fill=c_black, font=font_small_body)
                y += 13

    # 1. ICJ Myanmar
    draw_right_story(
        110, 235,
        "INTERNATIONAL COURT • JUSTICE",
        "ICJ DELIVERS MYANMAR GENOCIDE RULING",
        "The International Court of Justice delivers its judgment on Thursday in The Gambia's case accusing Myanmar of genocide against the Rohingya, read from 10:00 in The Hague — the first major ruling in over a decade. 1.2M Rohingya live in Cox's Bazar."
    )

    # 2. Voyager 1
    draw_right_story(
        245, 370,
        "SPACE SCIENCE • VOYAGER",
        "VOYAGER 1 REACHES ONE LIGHT-DAY MARK",
        "NASA confirms Voyager 1 is one light-day from Earth — 16.1B miles, the first human-made object to reach that distance; radio signals now take 24 hours. Crossed mark Wednesday, 50 years after 1977 launch."
    )

    # 3. Cyclone Akvan
    draw_right_story(
        380, 505,
        "WEATHER • ASIA-PACIFIC",
        "CYCLONE AKVAN THREATENS INDIA COAST",
        "Cyclone Akvan strengthens into a very severe cyclonic storm in the Bay of Bengal, forecast to make landfall on India's Andhra Pradesh coast Friday noon with winds of 120-130 km/h gusting to 145 km/h."
    )

    # 4. EU Ukraine Loan
    draw_right_story(
        515, 635,
        "EUROPE • FINANCE",
        "EU PROPOSES €45B LOAN FOR UKRAINE",
        "The European Commission proposes a fresh 45 billion euro ($49.4B) loan for Ukraine to cover its 2027 budget gap amidst ongoing conflict."
    )

    # 5. Gaza Ground Operation
    draw_right_story(
        645, 770,
        "MIDDLE EAST • GAZA",
        "ISRAELI TANKS PUSH INTO CENTRAL GAZA",
        "Israeli tanks push into central Gaza near Bureij and Nuseirat camps, closing Salah al-Din Road. The US-led Board of Peace reports both sides failing key ceasefire commitments."
    )

    # 6. Australia Sanctions
    draw_right_story(
        780, 885,
        "DIPLOMACY • AUSTRALIA",
        "AUSTRALIA SANCTIONS SETTLERS",
        "Australia sanctions Israeli settlers and organisations over West Bank expansion amid escalating regional tensions."
    )

    # 7. Bottom Right summary / footer
    draw.rectangle([right_x, 895, right_x + right_w, 1000], fill="#FFFFFF", outline=c_navy, width=1)
    draw.text((right_x + 10, 903), "GLOBAL SUMMARY", fill=c_red, font=font_sub)
    summary_text = (
        "Verified world events of Thursday, 19 November 2026. Summarized for historical record "
        "across geopolitics, tech, science, and climate."
    )
    s_lines = wrap_text(summary_text, font_small_body, right_w - 20)
    y = 920
    for line in s_lines:
        draw.text((right_x + 10, y), line, fill=c_black, font=font_small_body)
        y = y + 13

    # Save output
    output_path = "entry.png"
    img.save(output_path, "PNG")
    print(f"Successfully generated {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    main()
