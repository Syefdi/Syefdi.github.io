#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CV Generator - Clean ATS-Friendly PDF
Output: /mnt/user-data/outputs/cv_syefdi.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Design constants
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 2 * cm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
ACCENT_COLOR = HexColor('#0ea5e9')  # Sky blue
GRAY_COLOR = HexColor('#64748b')
BLACK_COLOR = HexColor('#000000')

# Font sizes
HEADER_NAME_SIZE = 16
HEADER_CONTACT_SIZE = 9
SECTION_HEADER_SIZE = 11
JOB_TITLE_SIZE = 10.5
COMPANY_SIZE = 10
DATE_SIZE = 9.5
BODY_SIZE = 9.5

# Line spacing
LINE_SPACING = 1.3


def create_cv():
    """Generate the CV PDF"""
    
    # Ensure output directory exists - try multiple locations
    possible_dirs = [
        "/mnt/user-data/outputs",
        "/mnt/c/outputs",
        os.path.expanduser("~/outputs"),
        "./outputs"
    ]
    
    output_dir = None
    for dir_path in possible_dirs:
        try:
            os.makedirs(dir_path, exist_ok=True)
            # Test if we can write
            test_file = os.path.join(dir_path, ".test")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            output_dir = dir_path
            break
        except:
            continue
    
    if output_dir is None:
        # Fallback to current directory
        output_dir = "."
    
    output_path = os.path.join(output_dir, "cv_syefdi.pdf")
    
    # Create canvas
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle("CV - SYEFDI FASMAWI SYABAN")
    c.setAuthor("Syefdi Fasmawi Syaban")
    
    # Starting Y position (from top)
    y = PAGE_HEIGHT - MARGIN
    
    # ========== HEADER ==========
    y = draw_header(c, y)
    y -= 0.6 * cm
    
    # ========== SUMMARY ==========
    y = draw_section_header(c, y, "PROFESSIONAL SUMMARY")
    y -= 0.35 * cm
    summary_text = (
        "Fresh QA professional with hands-on experience testing enterprise web systems in a production environment. "
        "Identified and documented 50+ bugs across ERM and CRM platforms, contributing to zero critical issues on "
        "monitored releases. Currently pursuing S1 Informatics Engineering at Universitas Pamulang while working full time. "
        "Detail-oriented, fast learner, available Monday to Friday."
    )
    y = draw_paragraph(c, y, summary_text, BODY_SIZE)
    y -= 0.5 * cm
    
    # ========== WORK EXPERIENCE ==========
    y = draw_section_header(c, y, "WORK EXPERIENCE")
    y -= 0.35 * cm
    
    # Junior QA Tester
    y = draw_job_header(c, y, "Junior QA Tester", "CV Gemilang Inti Teknologi", "Mei 2025 - Present")
    y -= 0.25 * cm
    
    bullets = [
        "Performed functional and regression testing on 2 enterprise web systems (ERM and CRM), covering revamp and legacy production versions simultaneously",
        "Identified, documented, and reported 50+ bugs with detailed reproduction steps, severity classification, and environment info to minimize developer back-and-forth",
        "Coordinated with developers across the full dev-to-production pipeline, contributing to zero critical issues on monitored production releases",
        "Handled minor fixes and adjustments directly on the live CRM system beyond standard QA responsibilities",
        "Contributed to build process of a web-based Document Management System alongside the core development team",
        "Involved in early development and functional testing of HRIS attendance application from project kickoff phase",
        "Created and managed digital content for company social media using Canva and CapCut"
    ]
    
    y = draw_bullets(c, y, bullets)
    y -= 0.5 * cm
    
    # ========== PROJECTS ==========
    y = draw_section_header(c, y, "PROJECTS")
    y -= 0.35 * cm
    
    projects = [
        ("ERM System", "erm.gemilangteknologi.com", "QA testing across two active versions (revamp + legacy production). Tools: Chrome DevTools, Bug Reporting, Regression Testing"),
        ("CRM System", "crms.gemilangteknologi.com", "QA testing, minor functionality fixes on live production system. Tools: Chrome DevTools, Bug Reporting, PHP"),
        ("Document Management System", "github.com/Syefdi/Document_Management_System", "Contributed to build process and system architecture. Tools: GitHub, HTML/CSS/JS, Git"),
        ("HRIS Attendance System", "absensi.intipowerabadi.com", "Early development involvement and functional testing. Tools: Chrome DevTools, Functional Testing")
    ]
    
    for project_name, url, description in projects:
        y = draw_project(c, y, project_name, url, description)
        y -= 0.3 * cm
    
    y -= 0.2 * cm
    
    # ========== EDUCATION ==========
    y = draw_section_header(c, y, "EDUCATION")
    y -= 0.35 * cm
    
    y = draw_education(c, y, "S1 Informatics Engineering", "Universitas Pamulang (UNPAM)", "Aug 2025 - Present", "Working-class program, Saturday class only")
    y -= 0.3 * cm
    
    y = draw_education(c, y, "Computer and Network Engineering (Vocational)", "SMK Fajar Ciseeng", "2022 - 2025", "")
    y -= 0.5 * cm
    
    # ========== CERTIFICATIONS ==========
    y = draw_section_header(c, y, "CERTIFICATIONS")
    y -= 0.35 * cm
    
    certs = [
        "Spec-Driven Development dengan Kiro - Dicoding x AWS (2026)",
        "Prompt Engineering untuk Software Developer - Dicoding (2025)",
        "Belajar Dasar SQL - Dicoding (2025)",
        "Belajar Dasar Data Science - Dicoding x Google Developers (2025)",
        "Belajar Dasar Visualisasi Data - Dicoding x Google Developers (2025)"
    ]
    
    y = draw_certifications_two_column(c, y, certs)
    y -= 0.5 * cm
    
    # ========== SKILLS ==========
    y = draw_section_header(c, y, "SKILLS")
    y -= 0.35 * cm
    
    skills = [
        ("QA & Testing", "Functional Testing, Regression Testing, Bug Reporting, SDLC, Web Application Testing, Dev-to-Prod Pipeline"),
        ("Tools", "Chrome DevTools, Browser DevTools, Git, GitHub, Kiro (AWS IDE), Microsoft Excel, Google Sheets, Canva, CapCut"),
        ("Currently Learning", "SQL for Data Validation, Postman (API Testing), Test Automation Fundamentals"),
        ("Languages", "Bahasa Indonesia (Native), English (Intermediate)")
    ]
    
    y = draw_skills(c, y, skills)
    
    # Save PDF
    c.save()
    print(f"✓ CV successfully generated: {output_path}")
    return output_path


def draw_header(c, y):
    """Draw the header section with name and contact info"""
    # Name
    c.setFont("Helvetica-Bold", HEADER_NAME_SIZE)
    c.setFillColor(BLACK_COLOR)
    c.drawString(MARGIN, y, "SYEFDI FASMAWI SYABAN")
    y -= 0.5 * cm
    
    # Contact info - line 1
    c.setFont("Helvetica", HEADER_CONTACT_SIZE)
    c.setFillColor(GRAY_COLOR)
    contact_line1 = "South Jakarta | +62 821-2343-9121 | syefdifasmawi@gmail.com"
    c.drawString(MARGIN, y, contact_line1)
    y -= 0.35 * cm
    
    # Contact info - line 2
    contact_line2 = "LinkedIn: linkedin.com/in/syefdi-fasmawi-syaban-6b6531337 | GitHub: github.com/Syefdi"
    c.drawString(MARGIN, y, contact_line2)
    y -= 0.25 * cm
    
    return y


def draw_section_header(c, y, title):
    """Draw a section header with accent color and underline"""
    c.setFont("Helvetica-Bold", SECTION_HEADER_SIZE)
    c.setFillColor(ACCENT_COLOR)
    c.drawString(MARGIN, y, title)
    y -= 0.15 * cm
    
    # Draw underline
    c.setStrokeColor(ACCENT_COLOR)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, PAGE_WIDTH - MARGIN, y)
    y -= 0.1 * cm
    
    return y


def draw_paragraph(c, y, text, font_size, max_width=None):
    """Draw a paragraph with text wrapping"""
    if max_width is None:
        max_width = CONTENT_WIDTH
    
    c.setFont("Helvetica", font_size)
    c.setFillColor(BLACK_COLOR)
    
    # Simple word wrapping
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if c.stringWidth(test_line, "Helvetica", font_size) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines:
        c.drawString(MARGIN, y, line)
        y -= font_size * LINE_SPACING / 2.835  # Convert pt to cm approx
    
    return y


def draw_job_header(c, y, title, company, date):
    """Draw job title, company, and date"""
    # Job title (left)
    c.setFont("Helvetica-Bold", JOB_TITLE_SIZE)
    c.setFillColor(BLACK_COLOR)
    c.drawString(MARGIN, y, title)
    
    # Date (right)
    c.setFont("Helvetica", DATE_SIZE)
    c.setFillColor(GRAY_COLOR)
    date_width = c.stringWidth(date, "Helvetica", DATE_SIZE)
    c.drawString(PAGE_WIDTH - MARGIN - date_width, y, date)
    
    y -= 0.35 * cm
    
    # Company
    c.setFont("Helvetica", COMPANY_SIZE)
    c.setFillColor(GRAY_COLOR)
    c.drawString(MARGIN, y, company)
    y -= 0.15 * cm
    
    return y


def draw_bullets(c, y, bullets):
    """Draw bullet points"""
    c.setFont("Helvetica", BODY_SIZE)
    c.setFillColor(BLACK_COLOR)
    
    bullet_indent = 0.4 * cm
    text_indent = 0.6 * cm
    max_width = CONTENT_WIDTH - text_indent
    
    for bullet_text in bullets:
        # Draw bullet point
        c.drawString(MARGIN + bullet_indent, y, "•")
        
        # Wrap and draw bullet text
        words = bullet_text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, "Helvetica", BODY_SIZE) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for i, line in enumerate(lines):
            c.drawString(MARGIN + text_indent, y, line)
            y -= BODY_SIZE * LINE_SPACING / 2.835
        
        y += BODY_SIZE * LINE_SPACING / 2.835  # Remove last spacing
        y -= 0.25 * cm  # Add spacing between bullets
    
    return y


def draw_project(c, y, name, url, description):
    """Draw a project entry"""
    # Project name (bold)
    c.setFont("Helvetica-Bold", BODY_SIZE)
    c.setFillColor(BLACK_COLOR)
    c.drawString(MARGIN, y, name)
    y -= 0.3 * cm
    
    # URL (gray, smaller)
    c.setFont("Helvetica", BODY_SIZE - 0.5)
    c.setFillColor(GRAY_COLOR)
    c.drawString(MARGIN, y, url)
    y -= 0.3 * cm
    
    # Description
    c.setFont("Helvetica", BODY_SIZE)
    c.setFillColor(BLACK_COLOR)
    y = draw_paragraph(c, y, description, BODY_SIZE)
    
    return y


def draw_education(c, y, degree, institution, date, note):
    """Draw an education entry"""
    # Degree (bold, left) and date (right)
    c.setFont("Helvetica-Bold", JOB_TITLE_SIZE)
    c.setFillColor(BLACK_COLOR)
    c.drawString(MARGIN, y, degree)
    
    c.setFont("Helvetica", DATE_SIZE)
    c.setFillColor(GRAY_COLOR)
    date_width = c.stringWidth(date, "Helvetica", DATE_SIZE)
    c.drawString(PAGE_WIDTH - MARGIN - date_width, y, date)
    
    y -= 0.35 * cm
    
    # Institution
    c.setFont("Helvetica", COMPANY_SIZE)
    c.setFillColor(GRAY_COLOR)
    institution_text = institution
    if note:
        institution_text += f" - {note}"
    c.drawString(MARGIN, y, institution_text)
    y -= 0.15 * cm
    
    return y


def draw_certifications_two_column(c, y, certs):
    """Draw certifications in two columns to save space"""
    c.setFont("Helvetica", BODY_SIZE)
    c.setFillColor(BLACK_COLOR)
    
    col_width = (CONTENT_WIDTH - 0.5 * cm) / 2
    left_col_x = MARGIN
    right_col_x = MARGIN + col_width + 0.5 * cm
    
    bullet_offset = 0.4 * cm
    text_offset = 0.6 * cm
    
    # Split into two columns
    mid = (len(certs) + 1) // 2
    left_certs = certs[:mid]
    right_certs = certs[mid:]
    
    start_y = y
    
    # Draw left column
    y_left = start_y
    for cert in left_certs:
        c.drawString(left_col_x + bullet_offset, y_left, "•")
        # Wrap text if needed
        max_width = col_width - text_offset
        words = cert.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, "Helvetica", BODY_SIZE) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for line in lines:
            c.drawString(left_col_x + text_offset, y_left, line)
            y_left -= BODY_SIZE * LINE_SPACING / 2.835
        
        y_left -= 0.05 * cm
    
    # Draw right column
    y_right = start_y
    for cert in right_certs:
        c.drawString(right_col_x + bullet_offset, y_right, "•")
        # Wrap text if needed
        max_width = col_width - text_offset
        words = cert.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, "Helvetica", BODY_SIZE) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        for line in lines:
            c.drawString(right_col_x + text_offset, y_right, line)
            y_right -= BODY_SIZE * LINE_SPACING / 2.835
        
        y_right -= 0.05 * cm
    
    # Return the lower of the two columns
    return min(y_left, y_right)


def draw_skills(c, y, skills):
    """Draw skills section with categories"""
    c.setFont("Helvetica", BODY_SIZE)
    
    for category, items in skills:
        # Category (bold)
        c.setFont("Helvetica-Bold", BODY_SIZE)
        c.setFillColor(BLACK_COLOR)
        c.drawString(MARGIN, y, f"{category}:")
        y -= 0.3 * cm
        
        # Items (normal, indented)
        c.setFont("Helvetica", BODY_SIZE)
        c.setFillColor(BLACK_COLOR)
        y = draw_paragraph(c, y, items, BODY_SIZE, max_width=CONTENT_WIDTH - 0.4 * cm)
        y -= 0.25 * cm
    
    return y


if __name__ == "__main__":
    try:
        output_file = create_cv()
        print(f"\n✓ Done! Your CV is ready at: {output_file}")
    except Exception as e:
        print(f"\n✗ Error generating CV: {e}")
        import traceback
        traceback.print_exc()
