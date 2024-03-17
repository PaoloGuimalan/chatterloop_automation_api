import time
import datetime
from django_eventstream import send_event
from django.http import StreamingHttpResponse, HttpResponse
from ..modules.persistent import Persistent

class SSE: 
        def __init__(self, counter):
                self.counter = counter
                

        def initialize_sse_con(self, data, userID):
                # print("REQUEST", userID)
                # send_event('rs', 'message', datetime.datetime.now())
                
                response = StreamingHttpResponse(content_type='text/event-stream')
                
                # self.count += 1
                
                def event_generator():
                        while True:
                        #    print(self.counter.get_count())
                           yield f"{self.counter.get_stream(userID)}\n\n"
                           self.counter.rewrite_stream(userID, "")
                           time.sleep(2);
                        
                response.streaming_content = event_generator()
                response['Cache-Control'] = 'no-cache'
                #     response['Connection'] = 'keep-alive'
                return response
        
        def send_message(self, data, userID, to, message):
                # print(data, userID, message)
                
                self.counter.rewrite_stream(userID, f"data: {message}*")
                self.counter.rewrite_stream(to, f"data: {message}*")
                
                return HttpResponse("OK")