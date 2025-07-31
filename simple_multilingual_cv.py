#!/usr/bin/env python3
"""
Simple Multilingual CV Generator
Creating CVs in Slovak (SK), German (DE), and Spanish (SP)
"""

def generate_sk_cv():
    """Generate Slovak CV"""
    return """
<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Elitný Tréner Alpského Lyžovania</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; background: white; box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-radius: 15px; overflow: hidden; }
        .header { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 50px; text-align: center; }
        .header h1 { font-size: 3em; margin-bottom: 10px; font-weight: 300; }
        .header h2 { font-size: 1.5em; margin-bottom: 20px; font-weight: 300; opacity: 0.9; }
        .contact-info { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin-top: 30px; }
        .contact-info p { display: flex; align-items: center; gap: 10px; font-size: 1.1em; }
        .content { padding: 50px; }
        .section { margin-bottom: 50px; }
        .section h3 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 30px; font-size: 1.8em; }
        .achievements-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px; }
        .achievement-item { background: #f8f9fa; padding: 25px; border-radius: 10px; border-left: 4px solid #3498db; transition: transform 0.3s ease; }
        .achievement-item:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
        .achievement-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .achievement-header h4 { color: #2c3e50; font-size: 1.2em; }
        .year { background: #3498db; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; }
        .category-badge { display: inline-block; background: #e74c3c; color: white; padding: 4px 12px; border-radius: 15px; font-size: 0.8em; margin-top: 10px; }
        .keywords-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
        .keyword-badge { background: #1976d2; color: white; padding: 6px 15px; border-radius: 20px; font-size: 0.9em; }
        @media (max-width: 768px) { .contact-info { flex-direction: column; gap: 15px; } .achievements-grid { grid-template-columns: 1fr; } .header h1 { font-size: 2.5em; } .content { padding: 30px; } }
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
                <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
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

def generate_de_cv():
    """Generate German CV"""
    return """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Elite-Alpinski-Trainer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; background: white; box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-radius: 15px; overflow: hidden; }
        .header { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 50px; text-align: center; }
        .header h1 { font-size: 3em; margin-bottom: 10px; font-weight: 300; }
        .header h2 { font-size: 1.5em; margin-bottom: 20px; font-weight: 300; opacity: 0.9; }
        .contact-info { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin-top: 30px; }
        .contact-info p { display: flex; align-items: center; gap: 10px; font-size: 1.1em; }
        .content { padding: 50px; }
        .section { margin-bottom: 50px; }
        .section h3 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 30px; font-size: 1.8em; }
        .achievements-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px; }
        .achievement-item { background: #f8f9fa; padding: 25px; border-radius: 10px; border-left: 4px solid #3498db; transition: transform 0.3s ease; }
        .achievement-item:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
        .achievement-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .achievement-header h4 { color: #2c3e50; font-size: 1.2em; }
        .year { background: #3498db; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; }
        .category-badge { display: inline-block; background: #e74c3c; color: white; padding: 4px 12px; border-radius: 15px; font-size: 0.8em; margin-top: 10px; }
        .keywords-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
        .keyword-badge { background: #1976d2; color: white; padding: 6px 15px; border-radius: 20px; font-size: 0.9em; }
        @media (max-width: 768px) { .contact-info { flex-direction: column; gap: 15px; } .achievements-grid { grid-template-columns: 1fr; } .header h1 { font-size: 2.5em; } .content { padding: 30px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Elite-Alpinski-Trainer</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h3>Berufliche Zusammenfassung</h3>
                <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
                    Elite-Alpinski-Trainer mit über 30 Jahren internationaler Erfahrung auf höchstem Wettkampfniveau.
                    Bewiesene Erfolgsbilanz im Training von Olympia-Athleten, Weltcup-Teilnehmern und Nationalmannschaften
                    in verschiedenen Ländern. Experte für Leistungsanalyse, Ski-Ausrüstungsmanagement und Elite-Athletenentwicklung
                    mit nachgewiesenem Erfolg bei Weltmeisterschaften, Olympischen Spielen und internationalen Wettbewerben.
                </p>
            </div>

            <div class="section">
                <h3>Wichtige Erfolge</h3>
                <div class="achievements-grid">
                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Olympische Spiele Erfahrung</h4>
                            <span class="year">2014</span>
                        </div>
                        <p>Trainierte die slowakische Nationalmannschaft bei den Olympischen Winterspielen in Sotschi 2014</p>
                        <span class="category-badge">Olympische Spiele</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Weltmeisterschafts-Erfahrung</h4>
                            <span class="year">2013</span>
                        </div>
                        <p>Führte das Team bei den Weltmeisterschaften in Schladming</p>
                        <span class="category-badge">Weltmeisterschaft</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Weltcup-Erfolg</h4>
                            <span class="year">1992-2023</span>
                        </div>
                        <p>Trainierte Athleten bei Weltcup- und Europacup-Wettbewerben</p>
                        <span class="category-badge">Weltcup</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Internationale Trainererfahrung</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Trainierte das Québec Provincial Team in Kanada</p>
                        <span class="category-badge">International</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>Branchenspezifische Schlüsselwörter</h3>
                <div class="keywords-grid">
                    <span class="keyword-badge">Alpinski</span>
                    <span class="keyword-badge">Weltcup</span>
                    <span class="keyword-badge">Olympische Spiele</span>
                    <span class="keyword-badge">FIS</span>
                    <span class="keyword-badge">Leistungsanalyse</span>
                    <span class="keyword-badge">Teamführung</span>
                    <span class="keyword-badge">Ausrüstungsmanagement</span>
                    <span class="keyword-badge">Internationale Erfahrung</span>
                    <span class="keyword-badge">Elite-Athleten</span>
                    <span class="keyword-badge">Wettkampftraining</span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def generate_sp_cv():
    """Generate Spanish CV"""
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Entrenador Elite de Esquí Alpino</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; background: white; box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-radius: 15px; overflow: hidden; }
        .header { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 50px; text-align: center; }
        .header h1 { font-size: 3em; margin-bottom: 10px; font-weight: 300; }
        .header h2 { font-size: 1.5em; margin-bottom: 20px; font-weight: 300; opacity: 0.9; }
        .contact-info { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin-top: 30px; }
        .contact-info p { display: flex; align-items: center; gap: 10px; font-size: 1.1em; }
        .content { padding: 50px; }
        .section { margin-bottom: 50px; }
        .section h3 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-bottom: 30px; font-size: 1.8em; }
        .achievements-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 30px; }
        .achievement-item { background: #f8f9fa; padding: 25px; border-radius: 10px; border-left: 4px solid #3498db; transition: transform 0.3s ease; }
        .achievement-item:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
        .achievement-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .achievement-header h4 { color: #2c3e50; font-size: 1.2em; }
        .year { background: #3498db; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.9em; }
        .category-badge { display: inline-block; background: #e74c3c; color: white; padding: 4px 12px; border-radius: 15px; font-size: 0.8em; margin-top: 10px; }
        .keywords-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
        .keyword-badge { background: #1976d2; color: white; padding: 6px 15px; border-radius: 20px; font-size: 0.9em; }
        @media (max-width: 768px) { .contact-info { flex-direction: column; gap: 15px; } .achievements-grid { grid-template-columns: 1fr; } .header h1 { font-size: 2.5em; } .content { padding: 30px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Entrenador Elite de Esquí Alpino</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h3>Resumen Profesional</h3>
                <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
                    Entrenador élite de esquí alpino con más de 30 años de experiencia internacional en los niveles más altos de competición.
                    Historial probado entrenando atletas olímpicos, competidores de Copa del Mundo y equipos nacionales en varios países.
                    Experto en análisis de rendimiento, gestión de equipamiento de esquí y desarrollo de atletas de élite con éxito demostrado
                    en Campeonatos Mundiales, Juegos Olímpicos y competiciones internacionales.
                </p>
            </div>

            <div class="section">
                <h3>Logros Clave</h3>
                <div class="achievements-grid">
                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Experiencia en Juegos Olímpicos</h4>
                            <span class="year">2014</span>
                        </div>
                        <p>Entrenó al equipo nacional eslovaco en los Juegos Olímpicos de Invierno de Sochi 2014</p>
                        <span class="category-badge">Juegos Olímpicos</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Campeonatos Mundiales</h4>
                            <span class="year">2013</span>
                        </div>
                        <p>Dirigió el equipo en los Campeonatos Mundiales de Schladming</p>
                        <span class="category-badge">Campeonatos Mundiales</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Copa del Mundo</h4>
                            <span class="year">1992-2023</span>
                        </div>
                        <p>Entrenó atletas en competiciones de Copa del Mundo y Copa Europea</p>
                        <span class="category-badge">Copa del Mundo</span>
                    </div>

                    <div class="achievement-item">
                        <div class="achievement-header">
                            <h4>Experiencia Internacional</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Entrenó al equipo provincial de Québec en Canadá</p>
                        <span class="category-badge">Internacional</span>
                    </div>
                </div>
            </div>

            <div class="section">
                <h3>Palabras Clave de la Industria</h3>
                <div class="keywords-grid">
                    <span class="keyword-badge">Esquí alpino</span>
                    <span class="keyword-badge">Copa del Mundo</span>
                    <span class="keyword-badge">Juegos Olímpicos</span>
                    <span class="keyword-badge">FIS</span>
                    <span class="keyword-badge">Análisis de rendimiento</span>
                    <span class="keyword-badge">Liderazgo de equipo</span>
                    <span class="keyword-badge">Gestión de equipamiento</span>
                    <span class="keyword-badge">Experiencia internacional</span>
                    <span class="keyword-badge">Atletas de élite</span>
                    <span class="keyword-badge">Entrenamiento de competición</span>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def main():
    """Main function to generate multilingual CVs"""

    print("🌍 Generating Multilingual CVs (SK/DE/SP)...")
    print("=" * 50)

    # Generate CVs for each language
    cv_files = [
        ("cv_sk.html", generate_sk_cv()),
        ("cv_de.html", generate_de_cv()),
        ("cv_sp.html", generate_sp_cv())
    ]

    for filename, content in cv_files:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Generated: {filename}")

    print("\n🎯 Key Features:")
    print("   • Language-specific content and terminology")
    print("   • Industry-specific achievements and keywords")
    print("   • Professional gradient design")
    print("   • Mobile-responsive layout")
    print("   • ATS-optimized structure")

    print("\n📊 Research-Based Improvements:")
    print("   • Emphasized international experience")
    print("   • Highlighted Olympic/World Cup experience")
    print("   • Added technical expertise sections")
    print("   • Included industry-specific keywords")
    print("   • Created value proposition sections")

if __name__ == "__main__":
    main()