#!/usr/bin/env python3
"""
Multilingual CV Generator for Alpine Skiing Coaching Positions
Creating improved versions in Slovak (SK), German (DE), and Spanish (SP)
Based on deep research and industry best practices
"""

import json
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class LanguageContent:
    """Immutable language-specific content"""
    language_code: str
    language_name: str
    title: str
    subtitle: str
    sections: Dict[str, str]
    achievements: List[Dict[str, str]]
    skills: List[Dict[str, str]]
    keywords: List[str]

class MultilingualCVGenerator:
    """Multilingual CV generator with improved research-based design"""

    def __init__(self):
        self.language_contents = self._create_language_contents()

    def _create_language_contents(self) -> Dict[str, LanguageContent]:
        """Create language-specific content"""
        return {
            "SK": LanguageContent(
                language_code="SK",
                language_name="Slovenský",
                title="Andrej Gyure",
                subtitle="Elitný Tréner Alpského Lyžovania",
                sections={
                    "professional_summary": "Profesionálny Prehľad",
                    "value_proposition": "Kľúčové Výhody",
                    "key_achievements": "Kľúčové Úspechy",
                    "technical_expertise": "Technická Odbornosť",
                    "industry_keywords": "Odborné Kľúčové Slová"
                },
                achievements=[
                    {
                        "title": "Účasť na Olympijských Hrách",
                        "description": "Trénoval slovenskú reprezentáciu na Zimných olympijských hrách v Soči 2014",
                        "impact": "Medzinárodné uznanie a skúsenosti z elitných súťaží",
                        "year": "2014",
                        "category": "Olympijské Hry"
                    },
                    {
                        "title": "Skúsenosti z Majstrovstiev Svetu",
                        "description": "Viedol tím na Majstrovstvách sveta v Schladmingu",
                        "impact": "Preukázaná schopnosť pôsobiť na najvyššej medzinárodnej úrovni",
                        "year": "2013",
                        "category": "Majstrovstvá Svetu"
                    },
                    {
                        "title": "Úspech v Svetovom Pohlári",
                        "description": "Trénoval športovcov v Svetovom pohári a Európskom pohári",
                        "impact": "Preukázaný úspech v elitných medzinárodných súťažiach",
                        "year": "1992-2023",
                        "category": "Svetový Pohár"
                    },
                    {
                        "title": "Medzinárodné Trénerské Skúsenosti",
                        "description": "Trénoval tím provincie Québec v Kanade (2014-2018)",
                        "impact": "Medzikultúrne trénerské skúsenosti a medzinárodná prispôsobivosť",
                        "year": "2014-2018",
                        "category": "Medzinárodné"
                    },
                    {
                        "title": "30+ Rokov Profesionálnych Skúseností",
                        "description": "Komplexné skúsenosti v trénovaní alpského lyžovania",
                        "impact": "Hlboká odbornosť a preukázaná dlhodobosť v odbore",
                        "year": "1992-2023",
                        "category": "Skúsenosti"
                    }
                ],
                skills=[
                    {
                        "skill": "Správa Lyžiarskeho Vybavenia",
                        "proficiency": "Expert",
                        "description": "Pokročilé znalosti prípravy, údržby a optimalizácie lyží",
                        "category": "Technické"
                    },
                    {
                        "skill": "Analýza Výkonnosti",
                        "proficiency": "Pokročilé",
                        "description": "Dátovo orientovaný prístup k hodnoteniu a zlepšovaniu výkonnosti športovcov",
                        "category": "Analytické"
                    },
                    {
                        "skill": "Vedenie Tímu",
                        "proficiency": "Expert",
                        "description": "Preukázaná schopnosť viesť a motivovať elitných športovcov v náročných podmienkach",
                        "category": "Vedenie"
                    },
                    {
                        "skill": "Bezpečnosť",
                        "proficiency": "Expert",
                        "description": "Komplexné pochopenie hodnotenia rizík a protokolov bezpečnosti športovcov",
                        "category": "Bezpečnosť"
                    }
                ],
                keywords=[
                    "Alpské lyžovanie",
                    "Svetový pohár",
                    "Olympijské hry",
                    "FIS",
                    "Analýza výkonnosti",
                    "Vedenie tímu",
                    "Správa vybavenia",
                    "Medzinárodné skúsenosti",
                    "Elitní športovci",
                    "Súťažné trénovanie"
                ]
            ),
            "DE": LanguageContent(
                language_code="DE",
                language_name="Deutsch",
                title="Andrej Gyure",
                subtitle="Elite-Alpinski-Trainer",
                sections={
                    "professional_summary": "Berufliche Zusammenfassung",
                    "value_proposition": "Wertversprechen",
                    "key_achievements": "Wichtige Erfolge",
                    "technical_expertise": "Technische Expertise",
                    "industry_keywords": "Branchenspezifische Schlüsselwörter"
                },
                achievements=[
                    {
                        "title": "Olympische Spiele Erfahrung",
                        "description": "Trainierte die slowakische Nationalmannschaft bei den Olympischen Winterspielen in Sotschi 2014",
                        "impact": "Internationale Anerkennung und Elite-Wettkampferfahrung",
                        "year": "2014",
                        "category": "Olympische Spiele"
                    },
                    {
                        "title": "Weltmeisterschafts-Erfahrung",
                        "description": "Führte das Team bei den Weltmeisterschaften in Schladming",
                        "impact": "Bewiesene Fähigkeit, auf höchstem internationalem Niveau zu arbeiten",
                        "year": "2013",
                        "category": "Weltmeisterschaft"
                    },
                    {
                        "title": "Weltcup-Erfolg",
                        "description": "Trainierte Athleten bei Weltcup- und Europacup-Wettbewerben",
                        "impact": "Bewiesene Erfolgsbilanz in Elite-Internationalen Wettbewerben",
                        "year": "1992-2023",
                        "category": "Weltcup"
                    },
                    {
                        "title": "Internationale Trainererfahrung",
                        "description": "Trainierte das Québec Provincial Team in Kanada (2014-2018)",
                        "impact": "Interkulturelle Trainererfahrung und internationale Anpassungsfähigkeit",
                        "year": "2014-2018",
                        "category": "International"
                    },
                    {
                        "title": "30+ Jahre Berufserfahrung",
                        "description": "Umfassende Erfahrung im Alpinski-Training",
                        "impact": "Tiefgreifende Expertise und bewiesene Langlebigkeit im Bereich",
                        "year": "1992-2023",
                        "category": "Erfahrung"
                    }
                ],
                skills=[
                    {
                        "skill": "Ski-Ausrüstungsmanagement",
                        "proficiency": "Experte",
                        "description": "Fortgeschrittene Kenntnisse in Ski-Vorbereitung, Wartung und Optimierung",
                        "category": "Technisch"
                    },
                    {
                        "skill": "Leistungsanalyse",
                        "proficiency": "Fortgeschritten",
                        "description": "Datengetriebener Ansatz zur Bewertung und Verbesserung der Athletenleistung",
                        "category": "Analytisch"
                    },
                    {
                        "skill": "Teamführung",
                        "proficiency": "Experte",
                        "description": "Bewiesene Fähigkeit, Elite-Athleten in Hochdruckumgebungen zu führen und zu motivieren",
                        "category": "Führung"
                    },
                    {
                        "skill": "Sicherheitsmanagement",
                        "proficiency": "Experte",
                        "description": "Umfassendes Verständnis von Risikobewertung und Athletensicherheitsprotokollen",
                        "category": "Sicherheit"
                    }
                ],
                keywords=[
                    "Alpinski",
                    "Weltcup",
                    "Olympische Spiele",
                    "FIS",
                    "Leistungsanalyse",
                    "Teamführung",
                    "Ausrüstungsmanagement",
                    "Internationale Erfahrung",
                    "Elite-Athleten",
                    "Wettkampftraining"
                ]
            ),
            "SP": LanguageContent(
                language_code="SP",
                language_name="Español",
                title="Andrej Gyure",
                subtitle="Entrenador Elite de Esquí Alpino",
                sections={
                    "professional_summary": "Resumen Profesional",
                    "value_proposition": "Propuesta de Valor",
                    "key_achievements": "Logros Clave",
                    "technical_expertise": "Experiencia Técnica",
                    "industry_keywords": "Palabras Clave de la Industria"
                },
                achievements=[
                    {
                        "title": "Experiencia en Juegos Olímpicos",
                        "description": "Entrenó al equipo nacional eslovaco en los Juegos Olímpicos de Invierno de Sochi 2014",
                        "impact": "Reconocimiento internacional y experiencia en competiciones de élite",
                        "year": "2014",
                        "category": "Juegos Olímpicos"
                    },
                    {
                        "title": "Experiencia en Campeonatos Mundiales",
                        "description": "Dirigió el equipo en los Campeonatos Mundiales de Schladming",
                        "impact": "Capacidad demostrada para trabajar al más alto nivel internacional",
                        "year": "2013",
                        "category": "Campeonatos Mundiales"
                    },
                    {
                        "title": "Éxito en Copa del Mundo",
                        "description": "Entrenó atletas en competiciones de Copa del Mundo y Copa Europea",
                        "impact": "Historial probado en competiciones internacionales de élite",
                        "year": "1992-2023",
                        "category": "Copa del Mundo"
                    },
                    {
                        "title": "Experiencia Internacional de Entrenamiento",
                        "description": "Entrenó al equipo provincial de Québec en Canadá (2014-2018)",
                        "impact": "Experiencia de entrenamiento intercultural y adaptabilidad internacional",
                        "year": "2014-2018",
                        "category": "Internacional"
                    },
                    {
                        "title": "30+ Años de Experiencia Profesional",
                        "description": "Experiencia integral en entrenamiento de esquí alpino",
                        "impact": "Experiencia profunda y longevidad probada en el campo",
                        "year": "1992-2023",
                        "category": "Experiencia"
                    }
                ],
                skills=[
                    {
                        "skill": "Gestión de Equipamiento de Esquí",
                        "proficiency": "Experto",
                        "description": "Conocimiento avanzado de preparación, mantenimiento y optimización de esquís",
                        "category": "Técnico"
                    },
                    {
                        "skill": "Análisis de Rendimiento",
                        "proficiency": "Avanzado",
                        "description": "Enfoque basado en datos para evaluación y mejora del rendimiento de atletas",
                        "category": "Analítico"
                    },
                    {
                        "skill": "Liderazgo de Equipo",
                        "proficiency": "Experto",
                        "description": "Capacidad probada para liderar y motivar atletas de élite en entornos de alta presión",
                        "category": "Liderazgo"
                    },
                    {
                        "skill": "Gestión de Seguridad",
                        "proficiency": "Experto",
                        "description": "Comprensión integral de evaluación de riesgos y protocolos de seguridad de atletas",
                        "category": "Seguridad"
                    }
                ],
                keywords=[
                    "Esquí alpino",
                    "Copa del Mundo",
                    "Juegos Olímpicos",
                    "FIS",
                    "Análisis de rendimiento",
                    "Liderazgo de equipo",
                    "Gestión de equipamiento",
                    "Experiencia internacional",
                    "Atletas de élite",
                    "Entrenamiento de competición"
                ]
            }
        }

    def generate_html_cv(self, language_code: str) -> str:
        """Generate HTML CV for specific language"""

        content = self.language_contents[language_code]

        # Create achievement HTML
        achievements_html = "".join(f"""
        <div class="achievement-item">
            <div class="achievement-header">
                <h4>{achievement["title"]}</h4>
                <span class="year">{achievement["year"]}</span>
            </div>
            <p class="achievement-description">{achievement["description"]}</p>
            <p class="achievement-impact"><strong>Dopad:</strong> {achievement["impact"]}</p>
            <span class="category-badge">{achievement["category"]}</span>
        </div>
        """ for achievement in content.achievements)

        # Create skills HTML
        skills_html = "".join(f"""
        <div class="skill-item">
            <div class="skill-header">
                <h4>{skill["skill"]}</h4>
                <span class="proficiency">{skill["proficiency"]}</span>
            </div>
            <p>{skill["description"]}</p>
            <span class="category-badge">{skill["category"]}</span>
        </div>
        """ for skill in content.skills)

        # Create keywords HTML
        keywords_html = "".join(f'<span class="keyword-badge">{keyword}</span>' for keyword in content.keywords)

        # Generate professional summary based on language
        if language_code == "SK":
            professional_summary = """
            Elitný tréner alpského lyžovania s viac ako 30 rokmi medzinárodných skúseností na najvyšších úrovniach súťaží.
            Preukázaný úspech v trénovaní olympijských športovcov, súťažiacich v Svetovom pohári a národných tímov v rôznych krajinách.
            Expert v analýze výkonnosti, správe lyžiarskeho vybavenia a vývoji elitných športovcov s preukázaným úspechom
            na Majstrovstvách sveta, Olympijských hrách a medzinárodných súťažiach. Multilingválny profesionál s rozsiahlymi
            skúsenosťami v vedení rôznorodých tímov v náročných prostrediach.
            """
        elif language_code == "DE":
            professional_summary = """
            Elite-Alpinski-Trainer mit über 30 Jahren internationaler Erfahrung auf höchstem Wettkampfniveau.
            Bewiesene Erfolgsbilanz im Training von Olympia-Athleten, Weltcup-Teilnehmern und Nationalmannschaften
            in verschiedenen Ländern. Experte für Leistungsanalyse, Ski-Ausrüstungsmanagement und Elite-Athletenentwicklung
            mit nachgewiesenem Erfolg bei Weltmeisterschaften, Olympischen Spielen und internationalen Wettbewerben.
            Mehrsprachiger Profi mit umfangreicher Erfahrung in der Führung verschiedener Teams in Hochdruckumgebungen.
            """
        else:  # SP
            professional_summary = """
            Entrenador élite de esquí alpino con más de 30 años de experiencia internacional en los niveles más altos de competición.
            Historial probado entrenando atletas olímpicos, competidores de Copa del Mundo y equipos nacionales en varios países.
            Experto en análisis de rendimiento, gestión de equipamiento de esquí y desarrollo de atletas de élite con éxito demostrado
            en Campeonatos Mundiales, Juegos Olímpicos y competiciones internacionales. Profesional multilingüe con extensa experiencia
            liderando equipos diversos en entornos de alta presión.
            """

        html_content = f"""
        <!DOCTYPE html>
        <html lang="{content.language_code.lower()}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{content.title} - {content.subtitle}</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}

                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #2c3e50;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    padding: 20px;
                }}

                .container {{
                    max-width: 1000px;
                    margin: 0 auto;
                    background: white;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                    border-radius: 15px;
                    overflow: hidden;
                }}

                .header {{
                    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                    color: white;
                    padding: 50px;
                    text-align: center;
                    position: relative;
                }}

                .header-content {{
                    position: relative;
                    z-index: 1;
                }}

                .header h1 {{
                    font-size: 3em;
                    margin-bottom: 10px;
                    font-weight: 300;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                }}

                .header h2 {{
                    font-size: 1.5em;
                    margin-bottom: 20px;
                    font-weight: 300;
                    opacity: 0.9;
                }}

                .contact-info {{
                    display: flex;
                    justify-content: center;
                    gap: 30px;
                    flex-wrap: wrap;
                    margin-top: 30px;
                }}

                .contact-info p {{
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    font-size: 1.1em;
                }}

                .content {{
                    padding: 50px;
                }}

                .section {{
                    margin-bottom: 50px;
                }}

                .section h3 {{
                    color: #2c3e50;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                    margin-bottom: 30px;
                    font-size: 1.8em;
                    position: relative;
                }}

                .section h3::after {{
                    content: '';
                    position: absolute;
                    bottom: -3px;
                    left: 0;
                    width: 50px;
                    height: 3px;
                    background: #e74c3c;
                }}

                .value-proposition {{
                    background: linear-gradient(135deg, #ecf0f1 0%, #bdc3c7 100%);
                    padding: 30px;
                    border-radius: 10px;
                    margin-bottom: 40px;
                    border-left: 5px solid #3498db;
                }}

                .value-proposition h4 {{
                    color: #2c3e50;
                    margin-bottom: 20px;
                    font-size: 1.4em;
                }}

                .value-proposition ul {{
                    list-style: none;
                    padding: 0;
                }}

                .value-proposition li {{
                    padding: 8px 0;
                    position: relative;
                    padding-left: 25px;
                    font-size: 1.1em;
                }}

                .value-proposition li::before {{
                    content: "🏆";
                    position: absolute;
                    left: 0;
                    font-size: 1.2em;
                }}

                .achievements-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 25px;
                    margin-top: 30px;
                }}

                .achievement-item {{
                    background: #f8f9fa;
                    padding: 25px;
                    border-radius: 10px;
                    border-left: 4px solid #3498db;
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }}

                .achievement-item:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                }}

                .achievement-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 15px;
                }}

                .achievement-header h4 {{
                    color: #2c3e50;
                    font-size: 1.2em;
                }}

                .year {{
                    background: #3498db;
                    color: white;
                    padding: 5px 12px;
                    border-radius: 20px;
                    font-size: 0.9em;
                    font-weight: 500;
                }}

                .achievement-description {{
                    margin-bottom: 10px;
                    color: #555;
                }}

                .achievement-impact {{
                    font-size: 0.9em;
                    color: #666;
                    font-style: italic;
                }}

                .category-badge {{
                    display: inline-block;
                    background: #e74c3c;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 15px;
                    font-size: 0.8em;
                    margin-top: 10px;
                }}

                .skills-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 25px;
                    margin-top: 30px;
                }}

                .skill-item {{
                    background: #f8f9fa;
                    padding: 25px;
                    border-radius: 10px;
                    border-left: 4px solid #27ae60;
                    transition: transform 0.3s ease;
                }}

                .skill-item:hover {{
                    transform: translateY(-3px);
                }}

                .skill-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 15px;
                }}

                .skill-header h4 {{
                    color: #2c3e50;
                    font-size: 1.1em;
                }}

                .proficiency {{
                    background: #27ae60;
                    color: white;
                    padding: 4px 10px;
                    border-radius: 15px;
                    font-size: 0.8em;
                }}

                .keywords-section {{
                    background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                    padding: 30px;
                    border-radius: 10px;
                    margin-top: 30px;
                }}

                .keywords-grid {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    margin-top: 20px;
                }}

                .keyword-badge {{
                    background: #1976d2;
                    color: white;
                    padding: 6px 15px;
                    border-radius: 20px;
                    font-size: 0.9em;
                    font-weight: 500;
                }}

                @media (max-width: 768px) {{
                    .contact-info {{
                        flex-direction: column;
                        gap: 15px;
                    }}

                    .achievements-grid,
                    .skills-grid {{
                        grid-template-columns: 1fr;
                    }}

                    .header h1 {{
                        font-size: 2.5em;
                    }}

                    .content {{
                        padding: 30px;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <div class="header-content">
                        <h1>{content.title}</h1>
                        <h2>{content.subtitle}</h2>
                        <div class="contact-info">
                            <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                            <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                            <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
                        </div>
                    </div>
                </div>

                <div class="content">
                    <div class="section">
                        <h3>{content.sections["professional_summary"]}</h3>
                        <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
                            {professional_summary.strip()}
                        </p>
                    </div>

                    <div class="section">
                        <h3>{content.sections["value_proposition"]}</h3>
                        <div class="value-proposition">
                            <h4>Kľúčové Výhody</h4>
                            <ul>
                                <li>Skúsenosti z Olympijských hier (Soči 2014)</li>
                                <li>Vedenie na Majstrovstvách sveta (Schladming 2013)</li>
                                <li>30+ rokov medzinárodných súťažných skúseností</li>
                                <li>Vedenie viacerých tímov (mužské, ženské, juniorské tímy)</li>
                                <li>Medzikultúrne trénerské skúsenosti (Kanada 2014-2018)</li>
                                <li>Expertné technické znalosti a manažérstvo bezpečnosti</li>
                            </ul>
                        </div>
                    </div>

                    <div class="section">
                        <h3>{content.sections["key_achievements"]}</h3>
                        <div class="achievements-grid">
                            {achievements_html}
                        </div>
                    </div>

                    <div class="section">
                        <h3>{content.sections["technical_expertise"]}</h3>
                        <div class="skills-grid">
                            {skills_html}
                        </div>
                    </div>

                    <div class="section">
                        <h3>{content.sections["industry_keywords"]}</h3>
                        <div class="keywords-section">
                            <p style="margin-bottom: 20px; font-size: 1.1em;">
                                <strong>Špecializovaná odbornosť v trénovaní alpského lyžovania a vývoji elitných športovcov.</strong>
                            </p>
                            <div class="keywords-grid">
                                {keywords_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        return html_content

def main():
    """Main function to generate multilingual CVs"""

    print("🌍 Generating Multilingual CVs (SK/DE/SP)...")
    print("=" * 50)

    generator = MultilingualCVGenerator()

    # Generate CVs for each language
    languages = ["SK", "DE", "SP"]

    for lang in languages:
        html_cv = generator.generate_html_cv(lang)
        filename = f"cv_{lang.lower()}.html"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_cv)

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