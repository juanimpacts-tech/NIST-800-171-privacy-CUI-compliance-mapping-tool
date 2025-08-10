from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

def generate_report(results):
    env = Environment(loader=FileSystemLoader("."))
    template = env.from_string("""
    <html>
    <head><title>NIST 800-171 Compliance Report</title></head>
    <body>
        <h1>NIST 800-171 Compliance Report</h1>
        <p><strong>Compliance Score:</strong> {{ score }}%</p>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr><th>Control ID</th><th>Name</th><th>Status</th><th>Risk</th><th>Mitigation</th></tr>
            {% for _, row in details.iterrows() %}
            <tr>
                <td>{{ row.Control_ID }}</td>
                <td>{{ row.Control_Name }}</td>
                <td>{{ row.status }}</td>
                <td>{{ row.Risk_Level }}</td>
                <td>{{ row.Mitigation }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """)

    html_content = template.render(score=results["score"], details=results["details"])
    os.makedirs("output", exist_ok=True)
    with open("output/compliance_report.html", "w") as f:
        f.write(html_content)
    HTML(string=html_content).write_pdf("output/compliance_report.pdf")
