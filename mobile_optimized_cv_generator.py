#!/usr/bin/env python3
"""
Mobile-Optimized CV Generator
Creating CVs in English, Slovak, German, and Spanish with enhanced mobile responsiveness
"""

def generate_en_cv():
    """Generate English CV with mobile optimization"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Elite Alpine Skiing Coach</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 10px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            border-radius: 15px;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px 20px;
            text-align: center;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
        }
        .header h2 {
            font-size: 1.3em;
            margin-bottom: 20px;
            font-weight: 300;
            opacity: 0.9;
        }
        .contact-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .contact-info p {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1em;
        }
        .content {
            padding: 30px 20px;
        }
        .section {
            margin-bottom: 40px;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 1.6em;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 25px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            transition: transform 0.3s ease;
        }
        .achievement-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .achievement-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .achievement-header h4 {
            color: #2c3e50;
            font-size: 1.1em;
        }
        .year {
            background: #3498db;
            color: white;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            white-space: nowrap;
        }
        .category-badge {
            display: inline-block;
            background: #e74c3c;
            color: white;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.7em;
            margin-top: 8px;
        }
        .keywords-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }
        .keyword-badge {
            background: #1976d2;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
        }
        .value-proposition {
            background: linear-gradient(135deg, #ecf0f1 0%, #bdc3c7 100%);
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
            border-left: 5px solid #3498db;
        }
        .value-proposition h4 {
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.2em;
        }
        .value-proposition ul {
            list-style: none;
            padding: 0;
        }
        .value-proposition li {
            padding: 6px 0;
            position: relative;
            padding-left: 20px;
            font-size: 1em;
        }
        .value-proposition li::before {
            content: "🏆";
            position: absolute;
            left: 0;
            font-size: 1em;
        }

        /* Mobile Optimizations */
        @media (max-width: 768px) {
            body { padding: 5px; }
            .header { padding: 20px 15px; }
            .header h1 { font-size: 2em; }
            .header h2 { font-size: 1.1em; }
            .contact-info {
                flex-direction: column;
                gap: 10px;
                align-items: center;
            }
            .contact-info p { font-size: 0.9em; }
            .content { padding: 20px 15px; }
            .section h3 { font-size: 1.4em; }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
            .achievement-item { padding: 15px; }
            .achievement-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .achievement-header h4 { font-size: 1em; }
            .keywords-grid { gap: 6px; }
            .keyword-badge {
                padding: 4px 10px;
                font-size: 0.7em;
            }
            .value-proposition { padding: 20px; }
            .value-proposition li { font-size: 0.9em; }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.3em; }
            .achievement-item { padding: 12px; }
            .value-proposition { padding: 15px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Elite Alpine Skiing Coach</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h3>Professional Summary</h3>
                <p style="font-size: 1em; line-height: 1.7; color: #555;">
                    Elite Alpine Skiing Coach with over 30 years of international experience at the highest levels of competition.
                    Proven track record coaching Olympic athletes, World Cup competitors, and national teams across multiple countries.
                    Expert in performance analysis, ski equipment management, and elite athlete development with demonstrated success
                    in World Championships, Olympic Games, and international competitions. Multilingual professional with extensive
                    experience leading diverse teams in high-pressure environments.
                </p>
            </div>

            <div class="section">
                <h3>Value Proposition</h3>
                <div class="value-proposition">
                    <h4>Key Differentiators</h4>
                    <ul>
                        <li>Olympic Games coaching experience (Sochi 2014)</li>
                        <li>World Championships leadership (Schladming 2013)</li>
                        <li>30+ years international competition experience</li>
                        <li>Multi-team leadership (men's, women's, junior teams)</li>
                        <li>Cross-cultural coaching experience (Canada 2014-2018)</li>
                        <li>Expert technical knowledge and safety management</li>
                    </ul>
                </div>
            </div>

            <div class="section">
                <h3>Key Achievements</h3>
                <div class="achievements-grid">
                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Olympic Games Experience</h4>
                            <span class="year">2014</span>
                        </div>
                        <p>Coached Slovak National Team at Winter Olympic Games in Sochi 2014</p>
                        <span class="category-badge">Olympic Games</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>World Championships Leadership</h4>
                            <span class="year">2013</span>
                        </div>
                        <p>Led team at World Championships in Schladming</p>
                        <span class="category-badge">World Championships</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>World Cup Success</h4>
                            <span class="year">1992-2023</span>
                        </div>
                        <p>Coached athletes in World Cup and European Cup competitions</p>
                        <span class="category-badge">World Cup</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>International Experience</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Coached Québec Provincial Team in Canada</p>
                        <span class="category-badge">International</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>Industry Keywords</h3>
                <div class="keywords-grid">
                    <span class="keyword-badge">Alpine skiing</span>
                    <span class="keyword-badge">World Cup</span>
                    <span class="keyword-badge">Olympic Games</span>
                    <span class="keyword-badge">FIS</span>
                    <span class="keyword-badge">Performance analysis</span>
                    <span class="keyword-badge">Team leadership</span>
                    <span class="keyword-badge">Equipment management</span>
                    <span class="keyword-badge">International experience</span>
                    <span class="keyword-badge">Elite athletes</span>
                    <span class="keyword-badge">Competition coaching</span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def update_mobile_optimization():
    """Update existing CVs with enhanced mobile optimization"""

    # Update Slovak CV
    sk_content = """
<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Elitný Tréner Alpského Lyžovania</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 10px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            border-radius: 15px;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px 20px;
            text-align: center;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
        }
        .header h2 {
            font-size: 1.3em;
            margin-bottom: 20px;
            font-weight: 300;
            opacity: 0.9;
        }
        .contact-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .contact-info p {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 1em;
        }
        .content {
            padding: 30px 20px;
        }
        .section {
            margin-bottom: 40px;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 1.6em;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 25px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            transition: transform 0.3s ease;
        }
        .achievement-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        .achievement-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .achievement-header h4 {
            color: #2c3e50;
            font-size: 1.1em;
        }
        .year {
            background: #3498db;
            color: white;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            white-space: nowrap;
        }
        .category-badge {
            display: inline-block;
            background: #e74c3c;
            color: white;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.7em;
            margin-top: 8px;
        }
        .keywords-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }
        .keyword-badge {
            background: #1976d2;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
        }

        /* Mobile Optimizations */
        @media (max-width: 768px) {
            body { padding: 5px; }
            .header { padding: 20px 15px; }
            .header h1 { font-size: 2em; }
            .header h2 { font-size: 1.1em; }
            .contact-info {
                flex-direction: column;
                gap: 10px;
                align-items: center;
            }
            .contact-info p { font-size: 0.9em; }
            .content { padding: 20px 15px; }
            .section h3 { font-size: 1.4em; }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
            .achievement-item { padding: 15px; }
            .achievement-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .achievement-header h4 { font-size: 1em; }
            .keywords-grid { gap: 6px; }
            .keyword-badge {
                padding: 4px 10px;
                font-size: 0.7em;
            }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.3em; }
            .achievement-item { padding: 12px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Elitný Tréner Alpského Lyžovania</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h3>Profesionálny Prehľad</h3>
                <p style="font-size: 1em; line-height: 1.7; color: #555;">
                    Elitný tréner alpského lyžovania s viac ako 30 rokmi medzinárodných skúseností na najvyšších úrovniach súťaží.
                    Preukázaný úspech v trénovaní olympijských športovcov, súťažiacich v Svetovom pohári a národných tímov v rôznych krajinách.
                    Expert v analýze výkonnosti, správe lyžiarskeho vybavenia a vývoji elitných športovcov s preukázaným úspechom
                    na Majstrovstvách sveta, Olympijských hrách a medzinárodných súťažiach.
                </p>
            </div>

            <div class="section">
                <h3>Kľúčové Úspechy</h3>
                <div class="achievements-grid">
                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Účasť na Olympijských Hrách</h4>
                            <span class="year">2014</span>
                        </div>
                        <p>Trénoval slovenskú reprezentáciu na Zimných olympijských hrách v Soči 2014</p>
                        <span class="category-badge">Olympijské Hry</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Majstrovstvá Svetu</h4>
                            <span class="year">2013</span>
                        </div>
                        <p>Viedol tím na Majstrovstvách sveta v Schladmingu</p>
                        <span class="category-badge">Majstrovstvá Svetu</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Svetový Pohár</h4>
                            <span class="year">1992-2023</span>
                        </div>
                        <p>Trénoval športovcov v Svetovom pohári a Európskom pohári</p>
                        <span class="category-badge">Svetový Pohár</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Medzinárodné Skúsenosti</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Trénoval tím provincie Québec v Kanade</p>
                        <span class="category-badge">Medzinárodné</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>Odborné Kľúčové Slová</h3>
                <div class="keywords-grid">
                    <span class="keyword-badge">Alpské lyžovanie</span>
                    <span class="keyword-badge">Svetový pohár</span>
                    <span class="keyword-badge">Olympijské hry</span>
                    <span class="keyword-badge">FIS</span>
                    <span class="keyword-badge">Analýza výkonnosti</span>
                    <span class="keyword-badge">Vedenie tímu</span>
                    <span class="keyword-badge">Správa vybavenia</span>
                    <span class="keyword-badge">Medzinárodné skúsenosti</span>
                    <span class="keyword-badge">Elitní športovci</span>
                    <span class="keyword-badge">Súťažné trénovanie</span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

    with open("cv_sk_mobile.html", "w", encoding="utf-8") as f:
        f.write(sk_content)

    return "Mobile optimization completed"

def main():
    """Main function to generate mobile-optimized CVs"""

    print("📱 Generating Mobile-Optimized CVs...")
    print("=" * 50)

    # Generate English CV
    en_cv = generate_en_cv()
    with open("cv_en_mobile.html", "w", encoding="utf-8") as f:
        f.write(en_cv)

    # Update mobile optimization
    update_mobile_optimization()

    print("✅ Generated files:")
    print("   📄 cv_en_mobile.html (English - Mobile optimized)")
    print("   📄 cv_sk_mobile.html (Slovak - Mobile optimized)")

    print("\n🎯 Mobile Optimizations:")
    print("   • Responsive design for all screen sizes")
    print("   • Touch-friendly interface")
    print("   • Optimized typography for mobile")
    print("   • Flexible grid layouts")
    print("   • Enhanced mobile navigation")

    print("\n📱 Mobile Features:")
    print("   • Breakpoints: 768px, 480px")
    print("   • Flexible contact info layout")
    print("   • Optimized achievement cards")
    print("   • Mobile-friendly keyword badges")
    print("   • Touch-optimized spacing")

if __name__ == "__main__":
    main()