# Emotonal_Stock_Trader
This is a project that I am undertaking to run an experiment
Start date: Sep/25/24

Before starting notes:
Hello! Thank you for looking at the readme, my name is Kevin and I a undertaking a pretty hard personal project that deals with different Ai models.

Houskeeping tasks first:
I don't know if anyone is going to check this out, but if you do! Hello! It's really nice of you to join me.
This readme is going to act more like a journal entries just so that I can keep an emotional feelings and tracker until I finish this project.

With that being said,lets begin


Entry #1) 
This entry is to start the repo, as well as act as a guideline on what this project is doing.

This is the synopsis of the project:
	I want to compare how different Ai models react to a news articles between different new's sites and their biases on wheter they will buy/sell a certain stock.

I hope that makes sense?
I have class in like 10 minutes so I may add stuff later in the day but the way I want to approach this is by splitting this project into 3 distinct sections

1) Getting the trader and its api so that we can buy/sell the stock (I am starting with this since it will probably be the easiest to implement first)
	I think my first step is to find a website that I can buy and sell fake stokes
	There are a couple constraints I am looking for
	1) It must have an api I can interact with
	2) It should show real time data
	3) It should be of the nasdaq or other major trader.
		


2) Making a web sraper that findes the article's
3) The ai api and response.


Entry #2) Sep/26/24

Ok this in entry number two, so this is where I breakdown the trader and api.

So here is where I see the problem, I need to get api's of stock prices in real time, there is a thing I have been seeing lately and that is paper tradeing, so will look more into that.
Update, so I looked into it, the best application I found that would fit my need seems to be TD-ameritrade. So will look into that.

entry #3) Sep/27/24

This is getting more and more infuriating, TD ameritrade doesn't seem to have multiple paper-trdaing account, so back to the drawing board. I think I found a cool one called we-bull?
Update #1: Ok so I have found one that seems to work, its called Alpaca, this has an api which is huge. Will have to look at the documentation to get the api up and running

entry #4) Sep/29/24

It was hoco last night so..... yea i didn't get too much work done yesterday.

Anyway, that's fine, what I want to do do today is try and get the api key working for my project from apacha. Lets see how this goes.

entry #5) I need to update this soon. Sometimes I wonder what my purpose is? What is the reason why I was put on this plaent? and why is it that I was put on this during the most "peaceful"
time in human history? I have no idea, but I feel as if that is for me to find out. Do i believe in a god? I don't know. All science points to the answer no, but maybe it's because I started going to church 
at a very young age, but I still hold out hope for a god. Anyway, I should probably not make this my personal diary, but I mean what can you do? Probably no one is going to be reading this, so i wonder if 
it even matters, but at that point, does anything matter? Truly? Anyway, I need to do my other projects and then I will start working on this. 

entry #6) Oct,1,24
I managed to get the alpaca api working and it is responidng to my computer, but there is still a lot I do not understand, so onwards and upwards I guess.
Ok this is the 6th entry in the very slow progress that i am making, it is offically the first day of october, I hope to have this project operational soon, but who knows? My goal is by 
the 20th (that gives me 20 more days to finish this project). So I have to make sure that I stay on the grind and continue moving forward. The goal of today is to get the code running so
that I may be able to buy a single stock. That is the idea. 
Ok ciao.


entry #7) Oct,2,24
so I watched the vice presidential debate last night and I have to say, kind of happy that debates are boring agian. I honestly think that it was a very 
fair and balanced debate. I have to get a ton of school work done today, so there might be a bit of non-project work done today.
Other than that will update if I do end up getting some work for this done.


entry #8) Oct/5/24
I took a lot of time to think about this yestreday, and I think that I am going to stop html, css and js right now. In terms of priority, its not as important in the moment. My #1 priority outside of school is trying
to get this project up and running. I got some school work to do today, but I will be back I promise. 

entry #9) oct/7/24
This is the first entry ina a LONG time that has actual good news in it. It took a little bit of figuring out, but I am happy to say, that I can now offically submit market orders that are reflected
on the website. This is HUGE and i'm really happy that the code is somewhat working. There is still a lot of work that I need to do, but I am happy that there is a little bit of progress that is 
happening. There are a few kinks I need to work out, such as submitting price orders rather than share orders. Because in my mind, every buy or sell I do will be with $1000 ( an arbritary num I decided). I also thought about it, and I don't know if news bias between different news site would be a good thing to use because I worry that markets will already
resolve themselves before I get the three different news confirmations. So I might do every single news article. But I do think that I will be doing an almost day trading but will have a max
of two trades of a certain stock per day. Maybe, just maybe. Anyway. Off to continue with my work. cheers!

entry #10) oct/8/24
There is a lot of issues that are still in the air, but I have made some progress on getting the news article aspect of my project. There is a news website called NewsApi, which could be 
a good source, however the problem righ now is that 1)I do more api call's then the free teir and the next teir is like $1000 a month for like half a million api calls,2) It has a 24 hours news delay
so that's not good. Another idea is to use Microsoft power automate, so will look into that. Anyway, it is what it is. Will come back if I finish my work for the day.


entry #11) oct/14/24
I have been adding stuff to the repo I promise you, its just that I forget to keep updating the readme lol. Anyway, today I started making headwind towards the webscraper/ new's articles. I found
a site but it has its problems, I found another one, and it looks promising and for the price, its actually not bad, we might have stumbled onto gold here team. Anyway, I feel mentally drained
but thats life right? Anyway, going to sleep lol. Have a good night!

entry #12) oct/18/24
I have made some decent progress, the Ai api has finally started working (needed to spend $5 on it, what kind of scam is that). Now I need to figure out how the program should flow and
what edge cases I need to worry about. What I am thinking is that, first the news file looks for new news headlines, then we send a request to the Ai file, (will probably need to use threading
because there are a couple different Ai models, and then finally we need to send it to the paper trading account. Anyway, a lot to figure out, but at least I am figuring out how it slowly works
so there is that. I have decided that I am going to do a different Readme document because lord knows, if someone tries to read this, it is going to sound like the mumblings of a madman.
Anyway, back to the grind (or lack thereof hahahahah)

entry #13) oct/21/24
Well the day has finally come where I now need to figure out the flow of the program. I am going to be acting on the thinking that I have already set up the serverless and the program is going to
going to be running continually. Every 15 minutes, my program will call a function in the news.py, this function will return a headline back to the program. The program will then check the headline
with preexsting headlines. (This is what I am also thinking, to avoid conflict, you can only trade a certain stock once per day.) (ie: 24 hours since the last trade??). but lets forget about
edge cases right now. The next part of this program is to then to call on the Ai portion of this code, this Ai functoin will take in the headline and spit back out a output with a number. With this
I will then call upon the paper trading account and it will execute the trade. I have to figure out if I can even sell a stock without buying it first?. Ok I am back and here are some of the changes
that I was able to make. The first change lets me see the position of each stock, therefore I can now start getting some logic to ensure that I only buy if I already own the stock. Secondly, I now
have the code set up in such a fashion that the news articles will be spit out by popularity first. This is to ensure that I do not get some back water news channel reporting misinformation.
Finally, I want to make another TODO which will write each Ai transaction as well as some other key features onto a excel file, I think that would be cool to see in the future. The companies that I
am mostly going to trade is Apple, Microsoft, Amazon, google, Tesla, Meta, Nvida, Netflix, Walmart, and JP morgan, (I might also toss in an elon for tesla). Thank you for sticking with another entry
and I will see you later. 

entry #14) oct/22/24
Another day another dollar am I right? Bahahahahah. I worked on these files a bit more, and I figured out how to get the current stock price and hopefully I will be able to do some math logic to
see if I have the money to actually buy the stock. I have a fear that I will buy a lot of stock and not actually sell any. But we wll corss that bridge when we get to it right? Anyway, did my work for
today. I want to have an end date by nov,1st, 2024.

entry #15) Oct/23/24
"Ceaser Wept, for there were no more worlds to conquer". I am a genius, there is no other way to say it (I made my program work for once lol). In all seriousness, this is a huge moment for me,
because my program will now look at the stock, figure out a value, judge if we have enough cash and then send it through. Which in my eyes is actually kind of crazy. So BIG DUBS for today.
There is a still a LOT of work that need to be done on this program, but the fact that it is actually working brings a tear to my seriously. As much as I want to celebrate, I have a LOOOONG day
ahead of me because Wednesday's are THE WORST. Therefore I have to log off. Proud of myself none-the-less. Cheers!!
