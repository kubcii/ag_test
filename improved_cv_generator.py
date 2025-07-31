#!/usr/bin/env python3
"""
Improved CV Generator with Natural Language and Two-Panel Layout
Creating CVs in English, Slovak, German, and Spanish with human-sounding content
"""

def generate_en_cv():
    """Generate English CV with natural language and two-panel layout"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Alpine Skiing Coach</title>
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
            max-width: 1200px;
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
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            padding: 30px 20px;
        }
        .left-panel, .right-panel {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .section {
            margin-bottom: 0;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.4em;
        }
        .about-me {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        .about-me p {
            font-size: 1em;
            line-height: 1.7;
            color: #555;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        .skill-category {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #3498db;
        }
        .skill-category h4 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        .skill-category ul {
            list-style: none;
            padding: 0;
        }
        .skill-category li {
            padding: 4px 0;
            font-size: 0.9em;
            color: #555;
        }
        .skill-category li::before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            margin-right: 8px;
        }
        .experience-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            margin-bottom: 20px;
        }
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .experience-header h4 {
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
        .experience-item p {
            font-size: 0.9em;
            color: #555;
            line-height: 1.6;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #e74c3c;
        }
        .achievement-item h4 {
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 1em;
        }
        .achievement-item p {
            font-size: 0.9em;
            color: #555;
        }
        .languages {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #27ae60;
        }
        .language-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0;
            font-size: 0.9em;
        }
        .language-level {
            color: #27ae60;
            font-weight: 500;
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
            .main-content {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 15px;
            }
            .section h3 { font-size: 1.3em; }
            .skills-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .experience-item { padding: 15px; }
            .experience-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .about-me { padding: 15px; }
            .skill-category { padding: 12px; }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.2em; }
            .experience-item { padding: 12px; }
            .about-me { padding: 12px; }
            .skill-category { padding: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Alpine Skiing Coach</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
            </div>
        </div>

        <div class="main-content">
            <!-- Left Panel - Skills & Expertise -->
            <div class="left-panel">
                <div class="section">
                    <h3>About Me</h3>
                    <div class="about-me">
                        <p>
                            I've spent over 30 years coaching alpine skiing at the highest levels of competition.
                            My journey has taken me from Olympic Games to World Championships, working with athletes
                            across different countries and cultures. I believe in developing not just great skiers,
                            but well-rounded athletes who understand both the technical and mental aspects of the sport.
                        </p>
                    </div>
                </div>

                <div class="section">
                    <h3>What I Bring</h3>
                    <div class="skills-grid">
                        <div class="skill-category">
                            <h4>Coaching Experience</h4>
                            <ul>
                                <li>Olympic Games coaching (Sochi 2014)</li>
                                <li>World Championships leadership</li>
                                <li>World Cup and European Cup</li>
                                <li>Junior team development</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Technical Skills</h4>
                            <ul>
                                <li>Performance analysis</li>
                                <li>Equipment management</li>
                                <li>Safety protocols</li>
                                <li>Training program design</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Leadership</h4>
                            <ul>
                                <li>Team management</li>
                                <li>Cross-cultural coaching</li>
                                <li>Mentoring young coaches</li>
                                <li>International collaboration</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h3>Languages</h3>
                    <div class="languages">
                        <div class="language-item">
                            <span>Slovak</span>
                            <span class="language-level">Native</span>
                        </div>
                        <div class="language-item">
                            <span>Spanish</span>
                            <span class="language-level">Fluent</span>
                        </div>
                        <div class="language-item">
                            <span>German</span>
                            <span class="language-level">Basic</span>
                        </div>
                        <div class="language-item">
                            <span>Italian</span>
                            <span class="language-level">Basic</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel - Experience & Achievements -->
            <div class="right-panel">
                <div class="section">
                    <h3>Work Experience</h3>
                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Slovak National Team Coach</h4>
                            <span class="year">2018-2023</span>
                        </div>
                        <p>Coached the national team in FIS races and European Cup competitions, focusing on developing young talent and maintaining high performance standards.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Québec Provincial Team Coach</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Worked in Canada's competitive skiing environment, adapting coaching methods to different cultural and sporting approaches.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Slovak Men's National Team</h4>
                            <span class="year">2003-2014</span>
                        </div>
                        <p>Led the team through World Cup competitions, European Cup events, World Championships in Schladming, and the 2014 Winter Olympics in Sochi.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Junior National Team Coach</h4>
                            <span class="year">1998-2003</span>
                        </div>
                        <p>Developed young athletes through FIS races and European Cup competitions, building the foundation for future elite competitors.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Women's National Team Coach</h4>
                            <span class="year">1994-1998</span>
                        </div>
                        <p>Coached the women's team in World Cup and European Cup competitions, managing both technical training and equipment.</p>
                    </div>
                </div>

                <div class="section">
                    <h3>Key Achievements</h3>
                    <div class="achievements-grid">
                        <div class="achievement-item">
                            <h4>Olympic Experience</h4>
                            <p>Coached at the 2014 Winter Olympics in Sochi, representing Slovakia on the world's biggest stage.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>World Championships</h4>
                            <p>Led the team at the 2013 World Championships in Schladming, Austria.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>International Experience</h4>
                            <p>Successfully coached in multiple countries, adapting to different skiing cultures and training methods.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Long-term Development</h4>
                            <p>Built and maintained successful programs across different age groups and competition levels.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

def generate_sk_cv():
    """Generate Slovak CV with natural language and two-panel layout"""
    return """<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Tréner Alpského Lyžovania</title>
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
            max-width: 1200px;
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
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            padding: 30px 20px;
        }
        .left-panel, .right-panel {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .section {
            margin-bottom: 0;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.4em;
        }
        .about-me {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        .about-me p {
            font-size: 1em;
            line-height: 1.7;
            color: #555;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        .skill-category {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #3498db;
        }
        .skill-category h4 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        .skill-category ul {
            list-style: none;
            padding: 0;
        }
        .skill-category li {
            padding: 4px 0;
            font-size: 0.9em;
            color: #555;
        }
        .skill-category li::before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            margin-right: 8px;
        }
        .experience-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            margin-bottom: 20px;
        }
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .experience-header h4 {
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
        .experience-item p {
            font-size: 0.9em;
            color: #555;
            line-height: 1.6;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #e74c3c;
        }
        .achievement-item h4 {
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 1em;
        }
        .achievement-item p {
            font-size: 0.9em;
            color: #555;
        }
        .languages {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #27ae60;
        }
        .language-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0;
            font-size: 0.9em;
        }
        .language-level {
            color: #27ae60;
            font-weight: 500;
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
            .main-content {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 15px;
            }
            .section h3 { font-size: 1.3em; }
            .skills-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .experience-item { padding: 15px; }
            .experience-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .about-me { padding: 15px; }
            .skill-category { padding: 12px; }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.2em; }
            .experience-item { padding: 12px; }
            .about-me { padding: 12px; }
            .skill-category { padding: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Tréner Alpského Lyžovania</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovensko</p>
            </div>
        </div>

        <div class="main-content">
            <!-- Left Panel - Skills & Expertise -->
            <div class="left-panel">
                <div class="section">
                    <h3>O Mne</h3>
                    <div class="about-me">
                        <p>
                            Viac ako 30 rokov sa venujem trénovaniu alpského lyžovania na najvyšších úrovniach súťaží.
                            Moja cesta ma zavedla od Olympijských hier až po Majstrovstvá sveta, pracoval som s atlétmi
                            z rôznych krajín a kultúr. Verím v rozvoj nielen výborných lyžiarov, ale aj všestranných
                            atlétov, ktorí chápu technické aj mentálne aspekty športu.
                        </p>
                    </div>
                </div>

                <div class="section">
                    <h3>Čo Prinášam</h3>
                    <div class="skills-grid">
                        <div class="skill-category">
                            <h4>Trénerské Skúsenosti</h4>
                            <ul>
                                <li>Trénovanie na Olympijských hrách (Soči 2014)</li>
                                <li>Vedenie na Majstrovstvách sveta</li>
                                <li>Svetový pohár a Európsky pohár</li>
                                <li>Rozvoj juniorských tímov</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Technické Zručnosti</h4>
                            <ul>
                                <li>Analýza výkonnosti</li>
                                <li>Správa vybavenia</li>
                                <li>Bezpečnostné protokoly</li>
                                <li>Návrh tréninkových programov</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Vedenie</h4>
                            <ul>
                                <li>Manažment tímov</li>
                                <li>Medzikultúrne trénovanie</li>
                                <li>Mentoring mladých trénerov</li>
                                <li>Medzinárodná spolupráca</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h3>Jazyky</h3>
                    <div class="languages">
                        <div class="language-item">
                            <span>Slovenský</span>
                            <span class="language-level">Rodný jazyk</span>
                        </div>
                        <div class="language-item">
                            <span>Španielsky</span>
                            <span class="language-level">Aktívne</span>
                        </div>
                        <div class="language-item">
                            <span>Nemecký</span>
                            <span class="language-level">Pasívne</span>
                        </div>
                        <div class="language-item">
                            <span>Taliansky</span>
                            <span class="language-level">Pasívne</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel - Experience & Achievements -->
            <div class="right-panel">
                <div class="section">
                    <h3>Pracovné Skúsenosti</h3>
                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Tréner Slovenskej Reprezentácie</h4>
                            <span class="year">2018-2023</span>
                        </div>
                        <p>Trénoval národný tím v FIS pretekoch a Európskom pohári, zameraný na rozvoj mladých talentov a udržanie vysokých výkonnostných štandardov.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Tréner Tímu Provincie Québec</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Pracoval v kanadskom konkurenčnom lyžovacom prostredí, prispôsoboval trénerské metódy rôznym kultúrnym a športovým prístupom.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Slovenská Mužská Reprezentácia</h4>
                            <span class="year">2003-2014</span>
                        </div>
                        <p>Viedol tím cez Svetový pohár, Európsky pohár, Majstrovstvá sveta v Schladmingu a Zimné olympijské hry v Soči 2014.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Tréner Juniorskej Reprezentácie</h4>
                            <span class="year">1998-2003</span>
                        </div>
                        <p>Rozvíjal mladých atlétov cez FIS preteky a Európsky pohár, budoval základ pre budúcich elitných súťažiacich.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Tréner Ženskej Reprezentácie</h4>
                            <span class="year">1994-1998</span>
                        </div>
                        <p>Trénoval ženský tím v Svetovom pohári a Európskom pohári, manažoval technický tréning aj vybavenie.</p>
                    </div>
                </div>

                <div class="section">
                    <h3>Kľúčové Úspechy</h3>
                    <div class="achievements-grid">
                        <div class="achievement-item">
                            <h4>Olympijské Skúsenosti</h4>
                            <p>Trénoval na Zimných olympijských hrách 2014 v Soči, reprezentoval Slovensko na najväčšej svetovej scéne.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Majstrovstvá Sveta</h4>
                            <p>Viedol tím na Majstrovstvách sveta 2013 v Schladmingu, Rakúsko.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Medzinárodné Skúsenosti</h4>
                            <p>Úspešne trénoval v viacerých krajinách, prispôsoboval sa rôznym lyžovacím kultúram a trénerským metódam.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Dlhodobý Rozvoj</h4>
                            <p>Budoval a udržiaval úspešné programy naprieč rôznymi vekovými skupinami a úrovňami súťaží.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

def generate_de_cv():
    """Generate German CV with natural language and two-panel layout"""
    return """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Alpinski-Trainer</title>
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
            max-width: 1200px;
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
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            padding: 30px 20px;
        }
        .left-panel, .right-panel {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .section {
            margin-bottom: 0;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.4em;
        }
        .about-me {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        .about-me p {
            font-size: 1em;
            line-height: 1.7;
            color: #555;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        .skill-category {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #3498db;
        }
        .skill-category h4 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        .skill-category ul {
            list-style: none;
            padding: 0;
        }
        .skill-category li {
            padding: 4px 0;
            font-size: 0.9em;
            color: #555;
        }
        .skill-category li::before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            margin-right: 8px;
        }
        .experience-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            margin-bottom: 20px;
        }
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .experience-header h4 {
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
        .experience-item p {
            font-size: 0.9em;
            color: #555;
            line-height: 1.6;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #e74c3c;
        }
        .achievement-item h4 {
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 1em;
        }
        .achievement-item p {
            font-size: 0.9em;
            color: #555;
        }
        .languages {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #27ae60;
        }
        .language-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0;
            font-size: 0.9em;
        }
        .language-level {
            color: #27ae60;
            font-weight: 500;
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
            .main-content {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 15px;
            }
            .section h3 { font-size: 1.3em; }
            .skills-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .experience-item { padding: 15px; }
            .experience-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .about-me { padding: 15px; }
            .skill-category { padding: 12px; }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.2em; }
            .experience-item { padding: 12px; }
            .about-me { padding: 12px; }
            .skill-category { padding: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Alpinski-Trainer</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slowakei</p>
            </div>
        </div>

        <div class="main-content">
            <!-- Left Panel - Skills & Expertise -->
            <div class="left-panel">
                <div class="section">
                    <h3>Über Mich</h3>
                    <div class="about-me">
                        <p>
                            Ich habe über 30 Jahre Alpinski auf höchstem Wettkampfniveau trainiert.
                            Meine Reise führte mich von Olympischen Spielen zu Weltmeisterschaften,
                            wo ich mit Athleten aus verschiedenen Ländern und Kulturen gearbeitet habe.
                            Ich glaube daran, nicht nur großartige Skifahrer zu entwickeln, sondern
                            vielseitige Athleten, die sowohl die technischen als auch mentalen
                            Aspekte des Sports verstehen.
                        </p>
                    </div>
                </div>

                <div class="section">
                    <h3>Was Ich Bringe</h3>
                    <div class="skills-grid">
                        <div class="skill-category">
                            <h4>Trainingserfahrung</h4>
                            <ul>
                                <li>Olympische Spiele Training (Sotschi 2014)</li>
                                <li>Weltmeisterschaften Führung</li>
                                <li>Weltcup und Europacup</li>
                                <li>Junioren-Team Entwicklung</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Technische Fähigkeiten</h4>
                            <ul>
                                <li>Leistungsanalyse</li>
                                <li>Ausrüstungsmanagement</li>
                                <li>Sicherheitsprotokolle</li>
                                <li>Trainingsprogramm-Design</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Führung</h4>
                            <ul>
                                <li>Team-Management</li>
                                <li>Interkulturelles Training</li>
                                <li>Mentoring junger Trainer</li>
                                <li>Internationale Zusammenarbeit</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h3>Sprachen</h3>
                    <div class="languages">
                        <div class="language-item">
                            <span>Slowakisch</span>
                            <span class="language-level">Muttersprache</span>
                        </div>
                        <div class="language-item">
                            <span>Spanisch</span>
                            <span class="language-level">Fließend</span>
                        </div>
                        <div class="language-item">
                            <span>Deutsch</span>
                            <span class="language-level">Grundkenntnisse</span>
                        </div>
                        <div class="language-item">
                            <span>Italienisch</span>
                            <span class="language-level">Grundkenntnisse</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel - Experience & Achievements -->
            <div class="right-panel">
                <div class="section">
                    <h3>Berufserfahrung</h3>
                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Slowakischer Nationaltrainer</h4>
                            <span class="year">2018-2023</span>
                        </div>
                        <p>Trainierte das Nationalteam bei FIS-Rennen und Europacup-Wettbewerben, konzentrierte mich auf die Entwicklung junger Talente und die Aufrechterhaltung hoher Leistungsstandards.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Trainer des Québec Provinzteams</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Arbeitete in Kanadas wettbewerbsorientierter Skiumgebung und passte Trainingsmethoden an verschiedene kulturelle und sportliche Ansätze an.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Slowakisches Männer-Nationalteam</h4>
                            <span class="year">2003-2014</span>
                        </div>
                        <p>Führte das Team durch Weltcup-Wettbewerbe, Europacup-Veranstaltungen, Weltmeisterschaften in Schladming und die Olympischen Winterspiele 2014 in Sotschi.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Junioren-Nationaltrainer</h4>
                            <span class="year">1998-2003</span>
                        </div>
                        <p>Entwickelte junge Athleten durch FIS-Rennen und Europacup-Wettbewerbe und baute die Grundlage für zukünftige Elite-Wettkämpfer.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Frauen-Nationaltrainer</h4>
                            <span class="year">1994-1998</span>
                        </div>
                        <p>Trainierte das Frauenteam bei Weltcup- und Europacup-Wettbewerben und verwaltete sowohl technisches Training als auch Ausrüstung.</p>
                    </div>
                </div>

                <div class="section">
                    <h3>Wichtige Erfolge</h3>
                    <div class="achievements-grid">
                        <div class="achievement-item">
                            <h4>Olympische Erfahrung</h4>
                            <p>Trainierte bei den Olympischen Winterspielen 2014 in Sotschi und vertrat die Slowakei auf der größten Weltbühne.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Weltmeisterschaften</h4>
                            <p>Führte das Team bei den Weltmeisterschaften 2013 in Schladming, Österreich.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Internationale Erfahrung</h4>
                            <p>Trainierte erfolgreich in mehreren Ländern und passte sich verschiedenen Skikulturen und Trainingsmethoden an.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Langfristige Entwicklung</h4>
                            <p>Baute und unterhielt erfolgreiche Programme in verschiedenen Altersgruppen und Wettkampfebenen.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

def generate_es_cv():
    """Generate Spanish CV with natural language and two-panel layout"""
    return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andrej Gyure - Entrenador de Esquí Alpino</title>
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
            max-width: 1200px;
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
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            padding: 30px 20px;
        }
        .left-panel, .right-panel {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }
        .section {
            margin-bottom: 0;
        }
        .section h3 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 1.4em;
        }
        .about-me {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        .about-me p {
            font-size: 1em;
            line-height: 1.7;
            color: #555;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        .skill-category {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #3498db;
        }
        .skill-category h4 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        .skill-category ul {
            list-style: none;
            padding: 0;
        }
        .skill-category li {
            padding: 4px 0;
            font-size: 0.9em;
            color: #555;
        }
        .skill-category li::before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            margin-right: 8px;
        }
        .experience-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
            margin-bottom: 20px;
        }
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .experience-header h4 {
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
        .experience-item p {
            font-size: 0.9em;
            color: #555;
            line-height: 1.6;
        }
        .achievements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }
        .achievement-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #e74c3c;
        }
        .achievement-item h4 {
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 1em;
        }
        .achievement-item p {
            font-size: 0.9em;
            color: #555;
        }
        .languages {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #27ae60;
        }
        .language-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0;
            font-size: 0.9em;
        }
        .language-level {
            color: #27ae60;
            font-weight: 500;
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
            .main-content {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 15px;
            }
            .section h3 { font-size: 1.3em; }
            .skills-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .achievements-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .experience-item { padding: 15px; }
            .experience-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
            .about-me { padding: 15px; }
            .skill-category { padding: 12px; }
        }

        @media (max-width: 480px) {
            .header h1 { font-size: 1.8em; }
            .header h2 { font-size: 1em; }
            .contact-info p { font-size: 0.8em; }
            .section h3 { font-size: 1.2em; }
            .experience-item { padding: 12px; }
            .about-me { padding: 12px; }
            .skill-category { padding: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Andrej Gyure</h1>
            <h2>Entrenador de Esquí Alpino</h2>
            <div class="contact-info">
                <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Eslovaquia</p>
            </div>
        </div>

        <div class="main-content">
            <!-- Left Panel - Skills & Expertise -->
            <div class="left-panel">
                <div class="section">
                    <h3>Sobre Mí</h3>
                    <div class="about-me">
                        <p>
                            He dedicado más de 30 años a entrenar esquí alpino en los niveles más altos de competición.
                            Mi trayectoria me ha llevado desde los Juegos Olímpicos hasta los Campeonatos Mundiales,
                            trabajando con atletas de diferentes países y culturas. Creo en desarrollar no solo
                            grandes esquiadores, sino atletas completos que entiendan tanto los aspectos técnicos
                            como mentales del deporte.
                        </p>
                    </div>
                </div>

                <div class="section">
                    <h3>Lo Que Aporto</h3>
                    <div class="skills-grid">
                        <div class="skill-category">
                            <h4>Experiencia de Entrenamiento</h4>
                            <ul>
                                <li>Entrenamiento en Juegos Olímpicos (Sochi 2014)</li>
                                <li>Liderazgo en Campeonatos Mundiales</li>
                                <li>Copa del Mundo y Copa Europea</li>
                                <li>Desarrollo de equipos junior</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Habilidades Técnicas</h4>
                            <ul>
                                <li>Análisis de rendimiento</li>
                                <li>Gestión de equipamiento</li>
                                <li>Protocolos de seguridad</li>
                                <li>Diseño de programas de entrenamiento</li>
                            </ul>
                        </div>
                        <div class="skill-category">
                            <h4>Liderazgo</h4>
                            <ul>
                                <li>Gestión de equipos</li>
                                <li>Entrenamiento intercultural</li>
                                <li>Mentoría de entrenadores jóvenes</li>
                                <li>Colaboración internacional</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="section">
                    <h3>Idiomas</h3>
                    <div class="languages">
                        <div class="language-item">
                            <span>Eslovaco</span>
                            <span class="language-level">Nativo</span>
                        </div>
                        <div class="language-item">
                            <span>Español</span>
                            <span class="language-level">Fluido</span>
                        </div>
                        <div class="language-item">
                            <span>Alemán</span>
                            <span class="language-level">Básico</span>
                        </div>
                        <div class="language-item">
                            <span>Italiano</span>
                            <span class="language-level">Básico</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Panel - Experience & Achievements -->
            <div class="right-panel">
                <div class="section">
                    <h3>Experiencia Laboral</h3>
                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Entrenador del Equipo Nacional Eslovaco</h4>
                            <span class="year">2018-2023</span>
                        </div>
                        <p>Entrené al equipo nacional en carreras FIS y competiciones de la Copa Europea, enfocándome en desarrollar talentos jóvenes y mantener altos estándares de rendimiento.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Entrenador del Equipo Provincial de Québec</h4>
                            <span class="year">2014-2018</span>
                        </div>
                        <p>Trabajé en el entorno competitivo de esquí de Canadá, adaptando métodos de entrenamiento a diferentes enfoques culturales y deportivos.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Equipo Nacional Masculino Eslovaco</h4>
                            <span class="year">2003-2014</span>
                        </div>
                        <p>Dirigí el equipo a través de competiciones de la Copa del Mundo, eventos de la Copa Europea, Campeonatos Mundiales en Schladming y los Juegos Olímpicos de Invierno 2014 en Sochi.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Entrenador del Equipo Nacional Junior</h4>
                            <span class="year">1998-2003</span>
                        </div>
                        <p>Desarrollé atletas jóvenes a través de carreras FIS y competiciones de la Copa Europea, construyendo la base para futuros competidores de élite.</p>
                    </div>

                    <div class="experience-item">
                        <div class="experience-header">
                            <h4>Entrenador del Equipo Nacional Femenino</h4>
                            <span class="year">1994-1998</span>
                        </div>
                        <p>Entrené al equipo femenino en competiciones de la Copa del Mundo y Copa Europea, gestionando tanto el entrenamiento técnico como el equipamiento.</p>
                    </div>
                </div>

                <div class="section">
                    <h3>Logros Clave</h3>
                    <div class="achievements-grid">
                        <div class="achievement-item">
                            <h4>Experiencia Olímpica</h4>
                            <p>Entrené en los Juegos Olímpicos de Invierno 2014 en Sochi, representando a Eslovaquia en el escenario mundial más grande.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Campeonatos Mundiales</h4>
                            <p>Dirigí el equipo en los Campeonatos Mundiales 2013 en Schladming, Austria.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Experiencia Internacional</h4>
                            <p>Entrené exitosamente en múltiples países, adaptándome a diferentes culturas de esquí y métodos de entrenamiento.</p>
                        </div>
                        <div class="achievement-item">
                            <h4>Desarrollo a Largo Plazo</h4>
                            <p>Construí y mantuve programas exitosos en diferentes grupos de edad y niveles de competición.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""


def main():
    """Generate all improved CV versions"""
    # Generate English CV
    with open('improved_cv_en_v4.html', 'w', encoding='utf-8') as f:
        f.write(generate_en_cv())

    # Generate Slovak CV
    with open('improved_cv_sk_v4.html', 'w', encoding='utf-8') as f:
        f.write(generate_sk_cv())

    # Generate German CV
    with open('improved_cv_de_v4.html', 'w', encoding='utf-8') as f:
        f.write(generate_de_cv())

    # Generate Spanish CV
    with open('improved_cv_es_v4.html', 'w', encoding='utf-8') as f:
        f.write(generate_es_cv())

    print("✅ Improved CVs generated successfully!")
    print("📄 Files created:")
    print("   - improved_cv_en_v4.html (English)")
    print("   - improved_cv_sk_v4.html (Slovak)")
    print("   - improved_cv_de_v4.html (German)")
    print("   - improved_cv_es_v4.html (Spanish)")
    print("\n🎯 Key improvements:")
    print("   - Natural, human-sounding language")
    print("   - Two-panel layout (Skills/Experience)")
    print("   - Mobile-responsive design")
    print("   - Replaced corporate jargon with conversational tone")

if __name__ == "__main__":
    main()