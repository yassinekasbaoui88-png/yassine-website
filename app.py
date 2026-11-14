
from flask import Flask

app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def home():
    return """
    <h1>مرحبا ياسين 🔥</h1>
    <p>هذا أول موقع ديالي</p>
    <a href="/contact">Contact</a>
    """

# صفحة Contact
@app.route("/contact")
def contact():
    return """
    <html>
    <head>
        <title>صفحة Contact</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                padding: 20px;
            }

            h1 { color: #ff4500; }
            h2 { color: #333333; }
            p { line-height: 1.6; }

            a.button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #0077cc;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>صفحة Contact</h1>
        <p>هنا تقدر تتواصل معانا بكل سهولة.</p>

        <h2>مقال: كيفاش تحمي الواي فاي ديالك</h2>
        <p>حماية الواي فاي ديالك مهمة بزاف.
        خاصك تبدل الباسورد بشكل دوري.</p>

        <p>استعمل WPA2 أو WPA3،
        وما تستعملش WEP لأنه ضعيف.</p>

        <h2>خطوات بسيطة:</h2>
        <ul>
            <li>دخل لإعدادات الروتر</li>
            <li>بدل الباسورد</li>
            <li>فعل WPA2/WPA3</li>
            <li>سد WPS</li>
        </ul>

        <a href="/" class="button">
            رجوع للصفحة الرئيسية
        </a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)