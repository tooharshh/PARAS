import pandas as pd
import numpy as np

def get_intervention_suggestions(student_data, risk_score, top_factors):
    
    interventions = []
    risk_level = "Low"
    
    if risk_score > 0.7:
        risk_level = "High"
    elif risk_score > 0.4:
        risk_level = "Medium"
    
    engagement_score = student_data.get('engagement_score', 0)
    is_absent = student_data.get('is_absent_frequently', 0)
    parent_engaged = student_data.get('parent_engaged', 0)
    parent_satisfied = student_data.get('parent_satisfied', 0)
    
    if engagement_score < 50:
        interventions.append({
            'category': 'Engagement',
            'priority': 'High',
            'action': 'Schedule one-on-one mentoring sessions',
            'description': 'Student shows low engagement. Regular check-ins can help identify barriers to participation.'
        })
        interventions.append({
            'category': 'Engagement',
            'priority': 'High',
            'action': 'Assign a peer buddy for collaborative learning',
            'description': 'Peer support can boost motivation and participation in class activities.'
        })
    
    if is_absent == 1:
        interventions.append({
            'category': 'Attendance',
            'priority': 'Critical',
            'action': 'Contact family immediately to address attendance issues',
            'description': 'High absence rate is strongly correlated with poor performance. Understand root causes.'
        })
        interventions.append({
            'category': 'Attendance',
            'priority': 'High',
            'action': 'Create attendance improvement plan with specific goals',
            'description': 'Work with student and family to set achievable attendance targets.'
        })
    
    if parent_engaged == 0:
        interventions.append({
            'category': 'Parent Involvement',
            'priority': 'Medium',
            'action': 'Reach out to parents for engagement',
            'description': 'Parents not responding to surveys. Schedule a meeting to discuss student progress.'
        })
        interventions.append({
            'category': 'Parent Involvement',
            'priority': 'Medium',
            'action': 'Share weekly progress reports with parents',
            'description': 'Keep parents informed to encourage their involvement in student learning.'
        })
    
    if parent_satisfied == 0 and parent_engaged == 1:
        interventions.append({
            'category': 'Parent Satisfaction',
            'priority': 'Medium',
            'action': 'Schedule parent-teacher conference',
            'description': 'Parents have concerns. Address their dissatisfaction to improve support at home.'
        })
    
    if engagement_score < 50 and is_absent == 1:
        interventions.append({
            'category': 'Combined Risk',
            'priority': 'Critical',
            'action': 'Immediate intervention required - assign to counselor',
            'description': 'Multiple risk factors present. Student needs comprehensive support plan.'
        })
    
    if student_data.get('raisedhands', 0) < 20:
        interventions.append({
            'category': 'Classroom Participation',
            'priority': 'Medium',
            'action': 'Encourage classroom participation with positive reinforcement',
            'description': 'Use strategies like think-pair-share to build confidence in speaking up.'
        })
    
    if student_data.get('VisITedResources', 0) < 20:
        interventions.append({
            'category': 'Resource Utilization',
            'priority': 'Medium',
            'action': 'Provide guided tour of learning resources',
            'description': 'Student not utilizing available materials. Show how to access and use them effectively.'
        })
    
    if len(interventions) == 0:
        interventions.append({
            'category': 'Monitoring',
            'priority': 'Low',
            'action': 'Continue regular monitoring',
            'description': 'Student showing positive engagement. Maintain current support level.'
        })
    
    return {
        'risk_level': risk_level,
        'risk_score': round(risk_score, 3),
        'interventions': interventions,
        'total_interventions': len(interventions)
    }


def generate_summary_report(student_data, risk_score, top_factors):
    
    result = get_intervention_suggestions(student_data, risk_score, top_factors)
    
    summary = "Risk Assessment: " + result['risk_level'] + " (Score: " + str(result['risk_score']) + ")\n"
    summary = summary + "Total Recommended Actions: " + str(result['total_interventions']) + "\n\n"
    
    summary = summary + "Top Contributing Factors:\n"
    for factor in top_factors[:5]:
        summary = summary + "  - " + factor + "\n"
    
    summary = summary + "\nRecommended Interventions:\n"
    for idx, intervention in enumerate(result['interventions'], 1):
        summary = summary + "\n" + str(idx) + ". [" + intervention['priority'] + "] " + intervention['action'] + "\n"
        summary = summary + "   Category: " + intervention['category'] + "\n"
        summary = summary + "   Details: " + intervention['description'] + "\n"
    
    return summary
