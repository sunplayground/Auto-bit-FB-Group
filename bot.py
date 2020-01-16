import fbchat
from datetime import datetime
from fbchat import Client
from fbchat.models import *

class make_bit:
    def __init__(self,group_id):
        self.group_thread_id = str(group_id)
        self.current_bit = 0
        self.my_current_bit = 0
        
    def call_auto_bit(self):

        messages = client.fetchThreadMessages(thread_id=self.group_thread_id, limit=1)
        # Since the message come in reversed order, reverse them
        messages.reverse()

        # Prints the content of all the messages
        for message in messages:
            if message.author == client.uid:
                self.my_current_bit = int(message.text)
                self.current_bit = self.my_current_bit
                #print('I bit')
            elif message.author != client.uid:
                self.current_bit = int(message.text)
                #check for higher bit value, avoid duplicated bit
                if self.my_current_bit < self.current_bit:
                    client.send(Message(text=str(int(self.current_bit) + 50)), thread_id=self.group_thread_id, thread_type=ThreadType.GROUP)
                    print('placed new bit')
                    self.my_current_bit = int(self.current_bit) + 50
             

class start_bit:
    def __init__(self,group_id):
        self.start_time = 0
        self.end_time = 0
        self.group_id = group_id
    def run(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        current_time = int(current_time)
        auto_bit = make_bit(self.group_id)
        print('running...')
        while current_time >= self.start_time and current_time <= self.end_time:
            try:
                auto_bit.call_auto_bit()
            except:
                print('err')
            

if __name__ == '__main__':

    cookies = {"c_user": "<value>",
           "datr": "<value>",
           "fr": "<value>",
           "noscript": "1",
           "sb": "<value>",
           "spin": "<value>",
           "xs": "<value>"}

    client = fbchat.Client("<fb_email>", "<fb_password>", session_cookies=cookies)
    print("Own id: {}".format(client.uid))
    client.send(Message(text="Hi me! Test Initial Test"), thread_id=client.uid, thread_type=ThreadType.USER)
    
    group_id = "<group_thread_id>"
    
    start_time = 140700
    # start time is 14:07:00
    end_time = 141600
    # end time is 14:16:00
    
    bot_runner = start_bit(group_id)
    bot_runner.run(start_time,end_time)
    print('stopped')
