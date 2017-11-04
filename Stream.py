#import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.models import Status
import json
#override tweepy.StreamListener to add logic to on_status

consumer_key = 'WSI12n4qUbs0dNKYL5DqdvBal'
consumer_secret = 'PeEydgl6NBORLpZ8j1xeyeHGj6Fp9iguVkWXI1tx4GeyjPIvvr'
access_token_key = '3178263232-vIZ0HwSi5yCsSzv6WKzsNuBDP6WdhhLZXNbxEld'
access_token_secret = 'O3lREESEUcVMZiLU2cskYDJMuVhtMxzR4cxSXVHikePF9'


class MyStreamListener(StreamListener):

    def __init__(self,tema):
       self.tema = tema
       self.ver_limit = False
       self.number_limit = 20
       self.init_limit = 0
       self.training_data = []

    def on_data(self,raw_data): # Se ejecuta cada ves que se recibe un tweet

        if not self.ver_limit:
            data = json.loads(raw_data)
            if not data.get('retweeted',True):
                self.init_limit += 1
                print(data['text'])
                self.training_data.append(data['text'])
                if self.number_limit < self.init_limit:
                	self.ver_limit = True
                	return False
            return True
        return False

        #data = data.dumps(data)
        #print(type(data))

        #print(data['user']['name'])
        #print("----------------")
        #print(data['text'])
        #print("------------------")
        #return True
    
    def on_status(self, status):
        print(status.text)
        return

    def on_error(self, status):
        print(status)



if __name__ == '__main__':

   #Verificar cuenta
   auth = OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token_key, access_token_secret)

   #myStreamListener = MyStreamListener()
   #myStream = tweepy.Stream(auth = auth, listener=myStreamListener)

   smite_listener = MyStreamListener('PaoloGuerrero')
   smite_stream = Stream(auth, smite_listener)

   #api = tweepy.API(auth)
   #api.update_status('Tweepy Get Started!')

   lista = [smite_listener]

   smite_stream.filter(track=['%s'], async=True) # Busqueda -> Track


   blocking_call = input(' Aprete cualquier tecla')


   for i in lista:
       print(i)
       for k in i.training_data:
       	  print(k)

   #ready = input("Presione Enter cuando este listo")

   #for l in lista:
   #	print(l['created_at'])

   # ,locations = [-12.082295837363576,-77.05810546875, -12.392317571033677, -76.75941467285156]