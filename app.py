from flask import Flask, request, render_template
from weasyprint import HTML
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    summary = request.form['summary']
    experience = request.form.getlist('experience')
    education = request.form.getlist('education')
    skills = request.form['skills']

    html = render_template('resume.html', 
                           name=name, 
                           email=email, 
                           phone=phone,
                           summary=summary,
                           experience=experience,
                           education=education,
                           skills=skills)
    pdf = HTML(string=html).write_pdf()

    output_path = 'resumes'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    pdf_path = os.path.join(output_path, f'{name}_resume.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf)
    
    return f'Resume generated successfully: <a href="/{pdf_path}">Download PDF</a>'

if __name__ == '__main__':
    app.run(debug=True)