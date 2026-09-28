from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>OLKILORITI SENIOR SCHOOL</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="font-family:Arial; margin:0; background:#f0f4f8;">
        
        <div style="background:#0d47a1; color:white; padding:30px; text-align:center;">
            <h1 style="margin:0;">OLKILORITI SENIOR SCHOOL</h1>
            <p style="margin:10px 0; font-size:18px; background:#ffca28; color:#0d47a1; display:inline-block; padding:6px 18px; border-radius:20px; font-weight:bold;">
                MOTTO: STRIVE TO EXCELL
            </p>
            <p style="margin:5px 0;">P.O BOX 25 LOLGORIAN</p>
        </div>

        <div style="max-width:850px; margin:20px auto; padding:15px;">
            
            <div style="background:white; padding:25px; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center;">
                <h2 style="color:#0d47a1; margin-top:0;">Welcome to Olkiloriti Senior School</h2>
                <p>We offer Senior Secondary Education from <b>GRADE 10 TO GRADE 12</b></p>
                <div style="background:#e8f5e9; padding:15px; border-radius:10px; border-left:5px solid #2e7d32; margin-top:15px;">
                    <h3 style="color:#2e7d32; margin:0;">✅ FULLY EQUIPED FOR CBE LEARNING</h3>
                    <p style="margin:5px 0 0 0;">Competency Based Education (CBE) - Ready for All Pathways: STEM, Social Sciences & Arts and Sports</p>
                </div>
            </div>

            <div style="display:flex; gap:15px; margin-top:20px; flex-wrap:wrap;">
                <div style="flex:1; min-width:220px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3 style="color:#0d47a1;">🎓 Grades</h3>
                    <p><b>Grade 10</b><br><b>Grade 11</b><br><b>Grade 12</b><br>Senior School</p>
                </div>
                <div style="flex:1; min-width:220px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3 style="color:#0d47a1;">🏫 Facilities</h3>
                    <p>Fully Equiped Labs<br>Library & ICT Lab<br>CBE Classrooms</p>
                </div>
                <div style="flex:1; min-width:220px; background:white; padding:20px; border-radius:10px; text-align:center;">
                    <h3 style="color:#0d47a1;">📍 Our Address</h3>
                    <p><b>P.O BOX 25<br>LOLGORIAN</b><br>Transmara South<br>Narok County</p>
                </div>
            </div>

            <div style="background:#0d47a1; color:white; text-align:center; padding:20px; border-radius:15px; margin-top:20px;">
                <h3 style="margin:0;">ADMISSION OPEN FOR GRADE 10 - 12</h3>
                <p style="margin:5px 0 0 0;">Visit us at P.O BOX 25 LOLGORIAN | STRIVE TO EXCELL</p>
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("Olkiloriti Website Running on http://127.0.0.1:8000")
    app.run(debug=True, port=8000)