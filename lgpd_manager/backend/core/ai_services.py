# ...existing code...
# core/ai_services.py

import os
import logging
import openai
from django.conf import settings

logger = logging.getLogger(__name__)

# Configurar API Key
openai.api_key = settings.OPENAI_API_KEY

class AIService:
    """
    Serviço para integração com OpenAI para sugestões relacionadas à LGPD
    """
    
    @staticmethod
    def suggest_processing_activities(process_description):
        """
        Sugere atividades de tratamento com base na descrição do processo
        
        Args:
            process_description (str): Descrição do processo de negócio
            
        Returns:
            list: Lista de atividades de tratamento sugeridas
        """
        try:
            prompt = f"""
            Com base na seguinte descrição de um processo de negócio, sugira atividades de tratamento de dados pessoais 
            relevantes no contexto da LGPD (Lei Geral de Proteção de Dados do Brasil). 
            Para cada atividade, forneça:
            1. Nome da atividade
            2. Descrição breve
            3. Finalidade do tratamento
            
            Descrição do processo: {process_description}
            
            Formato da resposta:
            [
                {{
                    "name": "Nome da Atividade 1",
                    "description": "Descrição da atividade 1",
                    "purposes": "Finalidades da atividade 1"
                }},
                ...
            ]
            """
            
            response = openai.Completion.create(
                model=settings.OPENAI_MODEL,
                prompt=prompt,
                max_tokens=1000,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            # Extrair e retornar as atividades sugeridas
            # Nota: Na implementação real, você precisaria parsear a resposta em JSON
            return response.choices[0].text.strip()
            
        except Exception as e:
            logger.error(f"Erro ao gerar sugestões de atividades: {str(e)}")
            return []
    
    @staticmethod
    def suggest_legal_basis(activity_description):
        """
        Sugere bases legais adequadas para uma atividade de tratamento
        
        Args:
            activity_description (str): Descrição da atividade de tratamento
            
        Returns:
            list: Lista de bases legais sugeridas com justificativas
        """
        try:
            prompt = f"""
            Com base na seguinte descrição de uma atividade de tratamento de dados pessoais, 
            sugira as bases legais mais adequadas conforme a LGPD (Lei Geral de Proteção de Dados do Brasil).
            Para cada base legal sugerida, forneça uma justificativa.
            
            Descrição da atividade: {activity_description}
            
            Formato da resposta:
            [
                {{
                    "legal_basis": "consent",
                    "name": "Consentimento",
                    "justification": "Justificativa para usar essa base legal"
                }},
                ...
            ]
            
            Considere apenas as seguintes bases legais da LGPD:
            - consent (Consentimento)
            - legal_obligation (Obrigação Legal)
            - contract (Execução de Contrato)
            - legitimate_interest (Interesse Legítimo)
            - public_interest (Interesse Público)
            - vital_interest (Proteção da Vida)
            - research (Pesquisa)
            - credit_protection (Proteção ao Crédito)
            """
            
            response = openai.Completion.create(
                model=settings.OPENAI_MODEL,
                prompt=prompt,
                max_tokens=1000,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            # Extrair e retornar as bases legais sugeridas
            # Nota: Na implementação real, você precisaria parsear a resposta em JSON
            return response.choices[0].text.strip()
            
        except Exception as e:
            logger.error(f"Erro ao gerar sugestões de bases legais: {str(e)}")
            return []