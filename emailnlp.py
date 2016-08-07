import email.parser
import codecs
#from stop_words import get_stop_words
from nltk.corpus import stopwords

from nltk.tag import pos_tag

content=""
stopwords = stopwords.words('english')



count = 0
max = 5

for line in codecs.open("jebemails.txt", 'r', errors='ignore',encoding='utf-8'):
    if line.startswith("From:")== True and content and count < max:
        msg = email.message_from_string(content)
        print("=============");
        print("To:", msg['to']);
        print ("From:", msg['from']);
        print ("Subject:", msg['subject']);
        #print ("Body:", repr(msg.get_payload().replace('\r',"").replace("\n","")));
        payload_tockens = repr(msg.get_payload()
                               .replace('\r',"")
                               .replace("\n","")
                               .replace("."," ")
                               .replace(","," ")
                               .replace("*","")
                               .replace(";"," ")).split();
        payload = [t for t in payload_tockens if t.lower() not in stopwords]
        print(payload)
        print("***************");
        tagged_sent = pos_tag(payload)
        propernouns = [(word,pos) for word,pos in tagged_sent ]
        print(propernouns)
        print("=============");
        content="";
        content += line;
        count+=1;
    else:
        content += line;








