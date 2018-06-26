import pyttsx3
engine = pyttsx3.init()
def tinyCount():
    engine.say('Hold for six seconds.')
    engine.setProperty('rate', rate-10)
    for i in range(1,7):
        engine.say(i)
    engine.say('Now rest for five seconds')
    for i in range(1,6):
        engine.say(i)
 
def smallCount():
    
    for i in range(1,11):
        engine.say('Hold for six seconds.')
        engine.setProperty('rate', rate-10)
        for j in range(1,7):
            engine.say(j)
        engine.say('Now rest for five seconds')
        for k in range(1,6):
            engine.say(k)
        engine.setProperty('rate', rate)
        engine.say('Good job dude, keep going')
        if i<10:
            engine.say('Come On, Tighten your muscles and lift it up.')
        
def largeCount():
    for i in range(2):
        engine.say('Hold the stretch for twenty seconds.')
        engine.setProperty('rate', rate-10)
        for j in range(1,21):
            engine.say(j)
        engine.say('Now rest for five seconds')
        for k in range(1,6):
            engine.say(k)
    
        engine.say('Good job dude, keep going')
        if i<1:
            engine.say('Come On, Repeat it one more time.')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume)
engine.say('Hello Deep !')
engine.setProperty('rate',rate-20)
engine.say('General instruction: If you feel discomfort in your knee, place a small towel roll under your knee')

engine.setProperty('rate', rate)
engine.say('Are you ready dude?')
engine.setProperty('rate', rate)
engine.say('Okay,Lets start our exercise, Here we go')
engine.setProperty('volume', volume-0.25)
engine.setProperty('rate', rate-65)
engine.say('Exercise one, Quad Sets')
engine.say('Sit with your leg straight and supported on the floor.')
engine.say('Tighten the muscles on top of your thigh by pressing the back of your knee, flat down to the floor.')
tinyCount()
engine.setProperty('rate', rate-10)
engine.say('Good job dude')

"""***********Exercise Two**********"""
engine.setProperty('rate', rate-65)
engine.say('Now lets go to the next exercise')
engine.say('Exercise two, Straight leg raises to the front')
engine.say('Lie on your back with your good knee bent, so that your foot rests flat on the floor.')
engine.say('Your injured leg should be straight, Tighten the thigh and quadrceps muscles in the injured leg.')
engine.say('Lift the tightened leg twelve to eighteen inches off the floor.')
smallCount()
engine.setProperty('rate', rate-65)        
engine.say('Awesome!')

"""****************Exercise Three**************"""
engine.say('Now lets go to the next exercise')
engine.say('Exercise three, Straight-leg raises to the inside')
engine.say('Lie on your side with the leg you are going to exercise on the bottom')
engine.say('Your other foot up on a chair, both legs should be straight')
engine.say('Lift the tightened injured leg twelve to eighteen inches off the floor')
smallCount()
engine.setProperty('rate', rate-65)        
engine.say('Awesome, Deep')

"""*****************Exercise Four**********"""
engine.say('Now lets go to the fourth exercise')
engine.say('Straight-leg raises to the outside')
engine.say('Lie on your side with the leg you are going to exercise on the top')
engine.say('Keep your legs,hip and body straight')
engine.say('Lift the tightened injured leg twelve to eighteen inches off the floor')
smallCount()
engine.setProperty('rate', rate-65)        
engine.say('Very Good you are almost there')

"""**************Exercise Five*************"""
engine.say('Now lets go to the fifth exercise')
engine.say('Straight-leg raises to the back')
engine.say('Lie on your belly')
engine.say('Lift the tightened injured leg twelve to eighteen inches off the floor')
smallCount()
engine.setProperty('rate', rate-65)        
engine.say('Good job man')
"""**************Exercise Six*************"""
engine.say('Now lets go to the sixth exercise')
engine.say('Standing Quadriceps stretch')
engine.say('Position is your choice')
engine.say('Bend the knee of a leg, grab the front of your foot with the hands on the same side.')
engine.say('Pull your foot toward your buttock')
largeCount()
"""**************Exercise Seven*************"""
engine.say('Well Done, Last exercise of the day')
engine.say('Hamstring stretch in doorway')
engine.say('Lie on the floor near a doorway, keep your body straight')
engine.say('Let the not stretching extend through the doorway')
engine.say('Put the leg you want to stretch, up on the wall')
largeCount()
engine.say('You completed all seven exercises')
engine.say('Take care dude, See you tomorrow')
engine.runAndWait()