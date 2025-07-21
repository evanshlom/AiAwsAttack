from src.crew import MarketingCrew # AI Agents for Content Marketing (Cross-Platform Market Entry Analysis)
import os

def run():
    inputs = {
        'topic': os.environ.get('TOPIC', 'I want to create content for VC investors in tech. Focus on AI startups, market analysis, and early-stage investing.')
    }
    
    crew = MarketingCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    print("\n" + "="*50)
    print("CONTENT STRATEGY RESULTS")
    print("="*50 + "\n")
    print(result)

if __name__ == "__main__":
    run()