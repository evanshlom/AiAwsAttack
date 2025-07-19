import json
import time
from src.crew import ContentCrew

def lambda_handler(event, context):
    start_time = time.time()
    
    # Get topic from event or use default
    topic = event.get('topic', 'VC content for tech investors focusing on AI')
    
    # Log structured data for CloudWatch
    print(json.dumps({
        "event": "crew_start",
        "topic": topic,
        "request_id": context.request_id
    }))
    
    try:
        crew = ContentCrew().crew()
        result = crew.kickoff(inputs={'topic': topic})
        
        # Log completion with metrics
        print(json.dumps({
            "event": "crew_complete",
            "duration": time.time() - start_time,
            "topic": topic,
            "request_id": context.request_id,
            "result_length": len(str(result))
        }))
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': str(result),
                'topic': topic,
                'duration': time.time() - start_time
            })
        }
    
    except Exception as e:
        print(json.dumps({
            "event": "crew_error",
            "error": str(e),
            "topic": topic,
            "request_id": context.request_id
        }))
        raise