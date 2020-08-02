from threading import Thread, Lock
import time

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lock = Lock()

class player(Thread):
  def __init__(self, name):
    Thread.__init__(self)
    self.name = name
    self.mycards = []
  def run(self):
    global cards
    while True:
      lock.acquire()
      if len(cards) > 0:
        self.mycards.append( cards.pop() )
        lock.release()
        time.sleep(0.1)
      else:
        lock.release()
        break

players = []
for name in ['player1', 'player2']:
  p = player(name)
  players.append(p)
  p.start()
for p in players:
  p.join()
  print(p.name, p.mycards)