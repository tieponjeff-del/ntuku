from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NTUKU - Maasai Mara Travels</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
header{background:#111;color:#fff;padding:18px 6%;display:flex;justify-content:space-between;align-items:center}
header b{color:#ffb400;font-size:26px;letter-spacing:2px}
nav a{color:#fff;text-decoration:none;margin-left:20px;font-weight:600}
.hero{background:linear-gradient(rgba(0,0,0,.65),rgba(0,0,0,.65)),url('https://images.unsplash.com/photo-1523805009345-7448845a9e53');background-size:cover;background-position:center;height:88vh;display:flex;flex-direction:column;justify-content:center;align-items:center;color:#fff;text-align:center}
.hero h1{font-size:48px}.hero p{font-size:19px;margin:15px 0 25px}
.btn{background:#ffb400;color:#000;padding:12px 28px;border-radius:30px;text-decoration:none;font-weight:bold}
.cards{display:flex;gap:20px;flex-wrap:wrap;justify-content:center;padding:50px 6%}
.card{width:320px;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 8px 20px rgba(0,0,0,.1)}
.card img{width:100%;height:200px;object-fit:cover}
.card div{padding:16px}.price{color:green;font-weight:bold;margin-top:8px}
footer{background:#111;color:#fff;text-align:center;padding:25px}
</style>
</head>
<body>
<header><b>NTUKU TOURS</b><nav><a href="/">Home</a><a href="#safari">Safaris</a><a href="#contact">Book</a></nav></header>
<div class="hero">
<h1>Explore The Wild Maasai Mara</h1>
<p>Game Drives | Hot Air Balloon | Maasai Culture | Luxury Lodges</p>
<a href="#safari" class="btn">View Packages</a>
</div>
<div class="cards" id="safari">
<div class="card"><img src="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e"><div><h3>Day Game Drive</h3><p>Full day drive with guide & lunch in the Mara.</p><p class="price">From $150</p></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1516026672322-bc52d61a55e5"><div><h3>3 Days Mara Explorer</h3><p>2 Nights, All meals, Transport, Park Fees Included.</p><p class="price">From $450</p></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1504196606672-aef5c9cefc92"><div><h3>Culture & Bush Dinner</h3><p>Maasai village, nature walk & bush dinner.</p><p class="price">From $200</p></div></div>
</div>
<div id="contact" style="text-align:center;padding:40px;background:#fff3cd">
<h2>Book Now</h2><p>WhatsApp: +2547XX XXX XXX | info@ntuku.co.ke</p><br><a class="btn" href="https://wa.me/254700000000">Book on WhatsApp</a>
</div>
<footer>&copy; 2026 NTUKU Travels - Maasai Mara National Reserve</footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
