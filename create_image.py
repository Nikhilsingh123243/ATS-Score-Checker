from PIL import Image, ImageDraw, ImageFont

# Create image
width, height = 1200, 630
img = Image.new('RGB', (width, height), color='#0f172a')
draw = ImageDraw.Draw(img)

# Try to load a font
try:
    title_font = ImageFont.truetype("arial.ttf", 48)
    subtitle_font = ImageFont.truetype("arial.ttf", 28)
    body_font = ImageFont.truetype("arial.ttf", 22)
    small_font = ImageFont.truetype("arial.ttf", 18)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Background gradient effect (simple rectangles)
for i in range(0, width, 4):
    r = int(15 + (i / width) * 30)
    g = int(23 + (i / width) * 10)
    b = int(42 + (i / width) * 50)
    draw.line([(i, 0), (i, height)], fill=(r, g, b))

# Accent bar at top
draw.rectangle([(0, 0), (width, 6)], fill='#667eea')

# Title
draw.text((60, 60), "ATS Score Checker", fill='#ffffff', font=title_font)

# Subtitle
draw.text((60, 130), "Built with LCEL (LangChain Expression Language)", fill='#94a3b8', font=subtitle_font)

# Divider line
draw.line([(60, 180), (400, 180)], fill='#667eea', width=3)

# Features
y = 220
features = [
    "Upload Resume (PDF) + Job Description",
    "Extract Keywords using LCEL Pipelines", 
    "Calculate ATS Compatibility Score",
    "Show Matched & Missing Keywords",
    "Optimize Resume Before Applying"
]

for feat in features:
    draw.ellipse([(70, y + 6), (82, y + 18)], fill='#667eea')
    draw.text((95, y), feat, fill='#e2e8f0', font=body_font)
    y += 45

# Tech stack box
draw.rounded_rectangle([(60, 470), (500, 560)], radius=10, fill='#1e293b', outline='#334155')
draw.text((80, 485), "Tech Stack:", fill='#667eea', font=small_font)
draw.text((80, 515), "Python | LCEL | NLP | PDF Parsing", fill='#e2e8f0', font=small_font)

# GitHub link
draw.text((60, 590), "https://github.com/Nikhilsingh123243/ATS_Score_Checker", fill='#60a5fa', font=small_font)

# Right side - decorative code snippet
code_x = 580
code_y = 80
code_lines = [
    "from langchain_core.runnables import",
    "  RunnablePassthrough, RunnableLambda",
    "",
    "# LCEL Pipeline",
    "chain = (",
    "  extract_keywords",
    "  | compute_similarity",
    "  | generate_score",
    ")",
    "",
    "result = chain.invoke({",
    "  'resume': resume_text,",
    "  'job_desc': job_description",
    "})",
    "",
    "# Output: ATS Score = 85%",
]

for i, line in enumerate(code_lines):
    color = '#667eea' if line.strip().startswith(('from', 'import', '#', 'chain', 'result')) else '#94a3b8'
    if '(' in line or ')' in line or '|' in line:
        color = '#f59e0b'
    draw.text((code_x, code_y + i * 26), line, fill=color, font=small_font)

# Save
output_path = r"C:\Users\pc\Desktop\GEN_AI\ats_score\ats_score_post.png"
img.save(output_path, quality=95)
print(f"Image saved to: {output_path}")
