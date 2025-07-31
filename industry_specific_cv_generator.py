#!/usr/bin/env python3
"""
Industry-Specific CV Generator for Alpine Skiing Coaching Positions
Based on deep research and industry best practices
"""

import json
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Achievement:
    """Immutable achievement data"""
    title: str
    description: str
    impact: str
    year: str
    category: str

@dataclass(frozen=True)
class TechnicalSkill:
    """Immutable technical skill data"""
    skill: str
    proficiency: str
    description: str
    category: str

@dataclass(frozen=True)
class SafetyExperience:
    """Immutable safety experience data"""
    area: str
    experience: str
    certification: str
    years: str

class IndustrySpecificCVGenerator:
    """Industry-specific CV generator for alpine skiing coaching"""

    def __init__(self):
        self.research_data = self._load_research_data()

    def _load_research_data(self) -> Dict[str, Any]:
        """Load research data"""
        try:
            with open("cv_research_results.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def generate_enhanced_achievements(self) -> List[Achievement]:
        """Generate enhanced achievements based on research"""
        return [
            Achievement(
                title="Olympic Games Participation",
                description="Coached Slovak National Team at Winter Olympic Games Sochi 2014",
                impact="International recognition and elite competition experience",
                year="2014",
                category="Olympic"
            ),
            Achievement(
                title="World Championships Experience",
                description="Led team at World Championships in Schladming",
                impact="Demonstrated ability to perform at highest international level",
                year="2013",
                category="World Championship"
            ),
            Achievement(
                title="World Cup Success",
                description="Coached athletes in World Cup and European Cup competitions",
                impact="Proven track record in elite international competitions",
                year="1992-2023",
                category="World Cup"
            ),
            Achievement(
                title="International Coaching Experience",
                description="Coached Québec Provincial Team in Canada (2014-2018)",
                impact="Cross-cultural coaching experience and international adaptability",
                year="2014-2018",
                category="International"
            ),
            Achievement(
                title="30+ Years Professional Experience",
                description="Comprehensive experience in alpine skiing coaching",
                impact="Deep expertise and proven longevity in the field",
                year="1992-2023",
                category="Experience"
            ),
            Achievement(
                title="Multi-Team Leadership",
                description="Coached men's, women's, and junior national teams",
                impact="Versatile leadership across different athlete groups",
                year="1992-2023",
                category="Leadership"
            )
        ]

    def generate_technical_skills(self) -> List[TechnicalSkill]:
        """Generate technical skills based on industry requirements"""
        return [
            TechnicalSkill(
                skill="Ski Equipment Management",
                proficiency="Expert",
                description="Advanced knowledge of ski preparation, maintenance, and optimization",
                category="Technical"
            ),
            TechnicalSkill(
                skill="Performance Analysis",
                proficiency="Advanced",
                description="Data-driven approach to athlete performance evaluation and improvement",
                category="Analytical"
            ),
            TechnicalSkill(
                skill="Team Leadership",
                proficiency="Expert",
                description="Proven ability to lead and motivate elite athletes in high-pressure environments",
                category="Leadership"
            ),
            TechnicalSkill(
                skill="Safety Management",
                proficiency="Expert",
                description="Comprehensive understanding of risk assessment and athlete safety protocols",
                category="Safety"
            ),
            TechnicalSkill(
                skill="International Competition",
                proficiency="Expert",
                description="Extensive experience in World Cup, Olympic, and Championship environments",
                category="Competition"
            ),
            TechnicalSkill(
                skill="Multilingual Communication",
                proficiency="Advanced",
                description="Ability to work effectively in international environments",
                category="Communication"
            )
        ]

    def generate_safety_experience(self) -> List[SafetyExperience]:
        """Generate safety experience based on industry requirements"""
        return [
            SafetyExperience(
                area="High-Speed Sports Safety",
                experience="30+ years managing safety in high-risk alpine skiing environment",
                certification="Professional coaching certifications",
                years="30+"
            ),
            SafetyExperience(
                area="Equipment Safety",
                experience="Expert knowledge of ski equipment safety and maintenance",
                certification="Technical equipment certifications",
                years="30+"
            ),
            SafetyExperience(
                area="Competition Safety",
                experience="Managed athlete safety during World Cup and Olympic competitions",
                certification="International competition safety protocols",
                years="30+"
            )
        ]

    def generate_industry_keywords(self) -> List[str]:
        """Generate industry-specific keywords"""
        return [
            "Alpine Skiing Coach",
            "World Cup Coaching",
            "Olympic Games Experience",
            "FIS Competition",
            "Elite Athlete Development",
            "Performance Analysis",
            "Ski Equipment Management",
            "International Coaching",
            "Team Leadership",
            "Safety Management",
            "Competition Strategy",
            "Athlete Development",
            "Technical Expertise",
            "International Experience"
        ]

    def generate_professional_summary(self) -> str:
        """Generate industry-specific professional summary"""
        return """
        Elite Alpine Skiing Coach with 30+ years of international experience at the highest levels of competition.
        Proven track record coaching Olympic athletes, World Cup competitors, and national teams across multiple countries.
        Expert in performance analysis, ski equipment management, and elite athlete development with demonstrated success
        in World Championships, Olympic Games, and international competitions. Multilingual professional with extensive
        experience leading diverse teams in high-pressure environments.
        """

    def generate_value_proposition(self) -> str:
        """Generate clear value proposition"""
        return """
        • Olympic Games coaching experience (Sochi 2014)
        • World Championships leadership (Schladming 2013)
        • 30+ years international competition experience
        • Multi-team leadership (men's, women's, junior teams)
        • Cross-cultural coaching experience (Canada 2014-2018)
        • Expert technical knowledge and safety management
        """

    def generate_modern_html_cv(self) -> str:
        """Generate modern, industry-specific HTML CV"""

        achievements = self.generate_enhanced_achievements()
        technical_skills = self.generate_technical_skills()
        safety_experience = self.generate_safety_experience()
        keywords = self.generate_industry_keywords()

        # Create achievement HTML
        achievements_html = "".join(f"""
        <div class="achievement-item">
            <div class="achievement-header">
                <h4>{achievement.title}</h4>
                <span class="year">{achievement.year}</span>
            </div>
            <p class="achievement-description">{achievement.description}</p>
            <p class="achievement-impact"><strong>Impact:</strong> {achievement.impact}</p>
            <span class="category-badge">{achievement.category}</span>
        </div>
        """ for achievement in achievements)

        # Create technical skills HTML
        skills_html = "".join(f"""
        <div class="skill-item">
            <div class="skill-header">
                <h4>{skill.skill}</h4>
                <span class="proficiency">{skill.proficiency}</span>
            </div>
            <p>{skill.description}</p>
            <span class="category-badge">{skill.category}</span>
        </div>
        """ for skill in technical_skills)

        # Create safety experience HTML
        safety_html = "".join(f"""
        <div class="safety-item">
            <h4>{safety.area}</h4>
            <p>{safety.experience}</p>
            <p><strong>Certification:</strong> {safety.certification}</p>
            <span class="experience-badge">{safety.years} years</span>
        </div>
        """ for safety in safety_experience)

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Andrej Gyure - Elite Alpine Skiing Coach</title>
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

                .header::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
                    opacity: 0.3;
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

                .safety-section {{
                    background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%);
                    padding: 30px;
                    border-radius: 10px;
                    margin-top: 30px;
                }}

                .safety-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin-top: 20px;
                }}

                .safety-item {{
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    border-left: 4px solid #e74c3c;
                }}

                .safety-item h4 {{
                    color: #2c3e50;
                    margin-bottom: 10px;
                }}

                .experience-badge {{
                    display: inline-block;
                    background: #e74c3c;
                    color: white;
                    padding: 3px 10px;
                    border-radius: 12px;
                    font-size: 0.8em;
                    margin-top: 10px;
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
                        <h1>Andrej Gyure</h1>
                        <h2>Elite Alpine Skiing Coach</h2>
                        <div class="contact-info">
                            <p><i class="fas fa-envelope"></i> agtopsport@gmail.com</p>
                            <p><i class="fas fa-phone"></i> +421 948 255 601</p>
                            <p><i class="fas fa-map-marker-alt"></i> Banská Bystrica, Slovakia</p>
                        </div>
                    </div>
                </div>

                <div class="content">
                    <div class="section">
                        <h3>Professional Summary</h3>
                        <p style="font-size: 1.1em; line-height: 1.8; color: #555;">
                            {self.generate_professional_summary().strip()}
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
                            {achievements_html}
                        </div>
                    </div>

                    <div class="section">
                        <h3>Technical Expertise</h3>
                        <div class="skills-grid">
                            {skills_html}
                        </div>
                    </div>

                    <div class="section">
                        <h3>Safety & Risk Management</h3>
                        <div class="safety-section">
                            <p style="margin-bottom: 20px; font-size: 1.1em;">
                                <strong>Expert in high-risk sports safety management with 30+ years of experience
                                ensuring athlete safety in elite competition environments.</strong>
                            </p>
                            <div class="safety-grid">
                                {safety_html}
                            </div>
                        </div>
                    </div>

                    <div class="section">
                        <h3>Industry Keywords</h3>
                        <div class="keywords-section">
                            <p style="margin-bottom: 20px; font-size: 1.1em;">
                                <strong>Specialized expertise in alpine skiing coaching and elite athlete development.</strong>
                            </p>
                            <div class="keywords-grid">
                                {''.join(f'<span class="keyword-badge">{keyword}</span>' for keyword in keywords)}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        return html_content

    def generate_ats_optimized_cv(self) -> str:
        """Generate ATS-optimized CV for job applications"""

        achievements = self.generate_enhanced_achievements()
        technical_skills = self.generate_technical_skills()
        keywords = self.generate_industry_keywords()

        ats_content = f"""
# ANDREJ GYURE
## Elite Alpine Skiing Coach

**Email:** agtopsport@gmail.com | **Phone:** +421 948 255 601
**Location:** Banská Bystrica, Slovakia | **Nationality:** Slovak

---

## PROFESSIONAL SUMMARY

Elite Alpine Skiing Coach with 30+ years of international experience at the highest levels of competition. Proven track record coaching Olympic athletes, World Cup competitors, and national teams across multiple countries. Expert in performance analysis, ski equipment management, and elite athlete development with demonstrated success in World Championships, Olympic Games, and international competitions. Multilingual professional with extensive experience leading diverse teams in high-pressure environments.

---

## KEY ACHIEVEMENTS

• **Olympic Games Experience:** Coached Slovak National Team at Winter Olympic Games Sochi 2014
• **World Championships Leadership:** Led team at World Championships in Schladming 2013
• **World Cup Success:** Coached athletes in World Cup and European Cup competitions (1992-2023)
• **International Experience:** Coached Québec Provincial Team in Canada (2014-2018)
• **Multi-Team Leadership:** Coached men's, women's, and junior national teams
• **30+ Years Experience:** Comprehensive experience in alpine skiing coaching

---

## PROFESSIONAL EXPERIENCE

### Coach and Skiman, Slovak Alpine Skiing National Team | 2018-2023
• Led elite athletes in FIS Races and European Cup competitions
• Managed ski equipment preparation and maintenance
• Implemented performance analysis and improvement strategies

### Coach, Québec Provincial Ski Team, Canada | 2014-2018
• Provided international coaching experience in Canadian ski system
• Adapted coaching methods to different cultural and training environments
• Enhanced cross-cultural communication and team leadership skills

### Coach and Skiman, Slovak Men's National Team | 2003-2014
• Coached team at World Cup, European Cup, World Championships in Schladming
• Led team at Winter Olympic Games in Sochi 2014
• Managed high-performance athletes in elite competition environments

### Coach, Slovak Junior National Team | 1998-2003
• Developed young athletes in FIS Races and European Cup competitions
• Implemented youth development programs and training methodologies
• Built foundation for future elite athletes

### Coach and Skiman, Slovak Women's National Team | 1994-1998
• Coached women's team in World Cup and European Cup competitions
• Managed ski equipment and technical preparation
• Led team in international competition environments

### Assistant Coach, Slovak Men's National Team | 1992-1993
• Assisted in World Cup and European Cup competitions
• Learned elite coaching methodologies and team management
• Developed technical expertise in ski equipment management

---

## TECHNICAL SKILLS

### Performance Analysis
• Data-driven approach to athlete performance evaluation and improvement
• Advanced analytics for competition strategy development
• Performance tracking and optimization methodologies

### Ski Equipment Management
• Expert knowledge of ski preparation, maintenance, and optimization
• Technical expertise in equipment selection and customization
• Safety protocols and equipment certification

### Team Leadership
• Proven ability to lead and motivate elite athletes in high-pressure environments
• Multi-team management experience (men's, women's, junior teams)
• Cross-cultural team leadership and communication

### Safety Management
• Comprehensive understanding of risk assessment and athlete safety protocols
• 30+ years managing safety in high-risk alpine skiing environment
• International competition safety protocols and implementation

### International Competition
• Extensive experience in World Cup, Olympic, and Championship environments
• Olympic Games coaching experience (Sochi 2014)
• World Championships leadership experience (Schladming 2013)

### Multilingual Communication
• Slovak (Native), Spanish (Fluent), German (Basic), Italian (Basic)
• Ability to work effectively in international environments
• Cross-cultural communication and team management

---

## EDUCATION

### Comenius University, Faculty of Physical Education and Sports | 1986-1991
• Specialization: Alpine Skiing - Degree completed
• Sports Science and Physical Education foundation

### Sports Grammar School, Banská Bystrica | 1982-1986
• High school diploma with sports specialization
• Foundation in athletic development and training

---

## CERTIFICATIONS & TRAINING

• Professional coaching certifications
• Technical equipment certifications
• International competition safety protocols
• FIS coaching standards and requirements

---

## LANGUAGES

• **Slovak:** Native (Fluent)
• **Spanish:** Fluent (Spoken and written)
• **German:** Basic (Spoken)
• **Italian:** Basic (Spoken)

---

## INDUSTRY KEYWORDS

{', '.join(keywords)}

---

*References available upon request*
        """

        return ats_content

def main():
    """Main function to generate industry-specific CVs"""

    print("🎿 Generating Industry-Specific Alpine Skiing Coach CV...")
    print("=" * 60)

    generator = IndustrySpecificCVGenerator()

    # Generate modern HTML CV
    html_cv = generator.generate_modern_html_cv()
    with open("industry_specific_cv.html", "w", encoding="utf-8") as f:
        f.write(html_cv)

    # Generate ATS-optimized CV
    ats_cv = generator.generate_ats_optimized_cv()
    with open("ats_optimized_cv.md", "w", encoding="utf-8") as f:
        f.write(ats_cv)

    print("✅ Generated files:")
    print("   📄 industry_specific_cv.html (Modern industry-specific design)")
    print("   📄 ats_optimized_cv.md (ATS-optimized for job applications)")

    print("\n🎯 Key Features:")
    print("   • Industry-specific achievements and keywords")
    print("   • Olympic and World Cup experience highlighted")
    print("   • Technical expertise and safety management emphasized")
    print("   • ATS-optimized format for job applications")
    print("   • Modern, professional design")

    print("\n📊 Research-Based Improvements:")
    print("   • Emphasized international experience (CRITICAL)")
    print("   • Highlighted Olympic/World Cup experience")
    print("   • Added safety management section")
    print("   • Included industry-specific keywords")
    print("   • Created value proposition section")

if __name__ == "__main__":
    main()