"""
PDF Report Generator
Generates professional PDF reports for battery analysis
"""

import os
from datetime import datetime
from typing import Dict, Any
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_pdf_report(data: Dict[str, Any], filepath: str):
    """
    Generate a professional PDF report from battery analysis data
    
    Args:
        data: Battery analysis data from the API
        filepath: Output file path for the PDF
    """
    
    # Create PDF document
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkblue,
        spaceBefore=20
    )
    
    # Title
    story.append(Paragraph("S2S - SCRAP TO SPARK BATTERY ANALYSIS REPORT", title_style))
    story.append(Spacer(1, 12))
    
    # Generated date
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))
    
    battery_summary = data.get('battery_summary', {})
    summary_data = [
        ['Grade:', battery_summary.get('grade', 'N/A')],
        ['Predicted RUL:', f"{battery_summary.get('predicted_rul', 'N/A')} cycles"],
        ['Confidence Score:', f"{battery_summary.get('confidence_score', 'N/A')}%"],
        ['Recommended Use:', battery_summary.get('recommended_use', 'N/A')]
    ]
    
    summary_table = Table(summary_data, colWidths=[2*inch, 4*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Sustainability Impact
    story.append(Paragraph("SUSTAINABILITY IMPACT", heading_style))
    
    sustainability = data.get('sustainability', {})
    sus_data = [
        ['Usable Energy:', f"{sustainability.get('usable_energy_kwh', 'N/A')} kWh"],
        ['CO₂ Saved:', f"{sustainability.get('co2_saved_kg', 'N/A')} kg"],
        ['Lithium Saved:', f"{sustainability.get('lithium_saved_kg', 'N/A')} kg"],
        ['Tree Equivalent:', f"{sustainability.get('tree_equivalent', 'N/A')} trees"]
    ]
    
    sus_table = Table(sus_data, colWidths=[2*inch, 4*inch])
    sus_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(sus_table)
    story.append(Spacer(1, 20))
    
    # AI Analysis Report
    story.append(Paragraph("AI ANALYSIS REPORT", heading_style))
    
    ai_report = data.get('ai_report', {})
    if ai_report:
        # Executive Summary from AI
        exec_summary = ai_report.get('executive_summary', {})
        if exec_summary:
            story.append(Paragraph("Health Status:", styles['Heading3']))
            story.append(Paragraph(exec_summary.get('health_status', 'N/A'), styles['Normal']))
            story.append(Paragraph(exec_summary.get('health_description', 'N/A'), styles['Normal']))
            story.append(Spacer(1, 12))
        
        # Technical Analysis
        tech_analysis = ai_report.get('technical_analysis', {})
        if tech_analysis:
            story.append(Paragraph("Technical Analysis:", styles['Heading3']))
            
            deg = tech_analysis.get('degradation', {})
            if deg:
                story.append(Paragraph(f"Degradation Level: {deg.get('level', 'N/A')}", styles['Normal']))
                story.append(Paragraph(deg.get('description', 'N/A'), styles['Normal']))
            
            thermal = tech_analysis.get('thermal_performance', {})
            if thermal:
                story.append(Paragraph(f"Thermal Stability: {thermal.get('stability', 'N/A')}", styles['Normal']))
                story.append(Paragraph(thermal.get('description', 'N/A'), styles['Normal']))
            
            story.append(Spacer(1, 12))
        
        # AI Insights
        insights = ai_report.get('ai_insights', {})
        if insights and insights.get('key_findings'):
            story.append(Paragraph("Key Findings:", styles['Heading3']))
            for finding in insights['key_findings']:
                story.append(Paragraph(f"• {finding}", styles['Normal']))
            story.append(Spacer(1, 12))
        
        # Recommendations
        recommendations = ai_report.get('recommendations', {})
        if recommendations and recommendations.get('deployment_options'):
            story.append(Paragraph("Deployment Recommendations:", styles['Heading3']))
            for rec in recommendations['deployment_options']:
                story.append(Paragraph(f"• {rec}", styles['Normal']))
            story.append(Spacer(1, 12))
        
        # Risk Assessment
        risk = ai_report.get('risk_assessment', {})
        if risk:
            story.append(Paragraph("Risk Assessment:", styles['Heading3']))
            story.append(Paragraph(f"Overall Risk Level: {risk.get('overall_risk_level', 'N/A')}", styles['Normal']))
            
            if risk.get('identified_risks'):
                story.append(Paragraph("Identified Risks:", styles['Normal']))
                for risk_item in risk['identified_risks']:
                    story.append(Paragraph(f"  - {risk_item}", styles['Normal']))
            story.append(Spacer(1, 12))
    else:
        story.append(Paragraph("AI analysis not available", styles['Normal']))
        story.append(Spacer(1, 12))
    
    # Recommendations
    story.append(Paragraph("RECOMMENDATIONS", heading_style))
    story.append(Paragraph(f"Based on the analysis, this battery is suitable for:", styles['Normal']))
    story.append(Paragraph(battery_summary.get('recommended_use', 'N/A'), styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Next Steps
    story.append(Paragraph("NEXT STEPS", heading_style))
    next_steps = [
        "1. Verify deployment requirements and specifications",
        "2. Schedule initial performance baseline testing",
        "3. Prepare monitoring and data collection systems",
        "4. Plan for end-of-life recycling after second-life use"
    ]
    
    for step in next_steps:
        story.append(Paragraph(step, styles['Normal']))
    
    story.append(Spacer(1, 20))
    
    # Footer
    story.append(Paragraph("---", styles['Normal']))
    story.append(Paragraph("Report generated by S2S - Scrap to Spark AI Battery Evaluation System", styles['Normal']))
    story.append(Paragraph("For questions or support, contact the development team.", styles['Normal']))
    
    # Build PDF
    try:
        doc.build(story)
        print(f"PDF report generated successfully: {filepath}")
    except Exception as e:
        print(f"Error generating PDF: {e}")
        # Fallback to text file if PDF generation fails
        generate_text_fallback(data, filepath)

def generate_text_fallback(data: Dict[str, Any], filepath: str):
    """Fallback text-based report if PDF generation fails"""
    
    report_content = f"""
S2S - SCRAP TO SPARK BATTERY ANALYSIS REPORT
=====================================

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

EXECUTIVE SUMMARY
-----------------
Grade: {data.get('battery_summary', {}).get('grade', 'N/A')}
Predicted RUL: {data.get('battery_summary', {}).get('predicted_rul', 'N/A')} cycles
Confidence Score: {data.get('battery_summary', {}).get('confidence_score', 'N/A')}%
Recommended Use: {data.get('battery_summary', {}).get('recommended_use', 'N/A')}

SUSTAINABILITY IMPACT
--------------------
Usable Energy: {data.get('sustainability', {}).get('usable_energy_kwh', 'N/A')} kWh
CO₂ Saved: {data.get('sustainability', {}).get('co2_saved_kg', 'N/A')} kg
Lithium Saved: {data.get('sustainability', {}).get('lithium_saved_kg', 'N/A')} kg
Tree Equivalent: {data.get('sustainability', {}).get('tree_equivalent', 'N/A')} trees

AI ANALYSIS REPORT
------------------
{format_ai_report(data.get('ai_report', {}))}

RECOMMENDATIONS
---------------
Based on the analysis, this battery is suitable for:
{data.get('battery_summary', {}).get('recommended_use', 'N/A')}

NEXT STEPS
----------
1. Verify deployment requirements and specifications
2. Schedule initial performance baseline testing
3. Prepare monitoring and data collection systems
4. Plan for end-of-life recycling after second-life use

---
Report generated by S2S - Scrap to Spark AI Battery Evaluation System
For questions or support, contact the development team.
"""
    
    # Write the report to file with .txt extension to avoid confusion
    txt_filepath = filepath.replace('.pdf', '.txt')
    with open(txt_filepath, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Text report generated as fallback: {txt_filepath}")

def format_ai_report(ai_report: Dict[str, Any]) -> str:
    """Format AI report data into readable text"""
    
    if not ai_report:
        return "AI analysis not available"
    
    sections = []
    
    # Executive Summary
    exec_summary = ai_report.get('executive_summary', {})
    if exec_summary:
        sections.append(f"Health Status: {exec_summary.get('health_status', 'N/A')}")
        sections.append(f"Overall Assessment: {exec_summary.get('overall_assessment', 'N/A')}")
    
    # Technical Analysis
    tech_analysis = ai_report.get('technical_analysis', {})
    if tech_analysis:
        deg = tech_analysis.get('degradation', {})
        thermal = tech_analysis.get('thermal_performance', {})
        sections.append(f"Degradation Level: {deg.get('level', 'N/A')}")
        sections.append(f"Thermal Stability: {thermal.get('stability', 'N/A')}")
    
    # AI Insights
    insights = ai_report.get('ai_insights', {})
    if insights and insights.get('key_findings'):
        sections.append("Key Findings:")
        for finding in insights['key_findings']:
            sections.append(f"  - {finding}")
    
    # Risk Assessment
    risk = ai_report.get('risk_assessment', {})
    if risk:
        sections.append(f"Overall Risk Level: {risk.get('overall_risk_level', 'N/A')}")
        if risk.get('identified_risks'):
            sections.append("Identified Risks:")
            for risk_item in risk['identified_risks']:
                sections.append(f"  - {risk_item}")
    
    return '\n'.join(sections) if sections else "AI analysis data incomplete"