CHAPTER 7 

Simon Peyton Jone

One of the instigators, back in 1987, of the project that led to the definition of the programming language Haskell, Simon Peyton Jones is a Principal Researcher at Microsoft Research’s lab in Cambridge, England. He edited the Haskell 98 Revised Report, the current stable definition of the language; he is the architect and lead developer of the Glasgow Haskell Compiler (GHC), the “de facto standard compiler” according to haskell.org; and he gave Haskell its widely cited unofficial motto: “Avoid success at all costs.” 

A high-powered researcher and former professor who never got a PhD, Peyton Jones values both the practical and the theoretically beautiful. He learned to program on a machine with no permanent storage and only 100 memory locations, and in college he worked on both writing high-level compilers for the school’s big iron and building his own primitive computers out of parts he could afford on a student’s budget. But he was drawn to functional programming by a professor’s demonstration of how to build doubly linked lists without using mutation and the beauty of the idea of lazy evaluation. Peyton Jones saw the ideas of functional programming “as a radical and elegant attack on the whole enterprise of writing programs”: a way, rather than “just putting one more brick in the wall,” to “build a whole new wall.” In 2004 the Association for Computing Machinery elected him a Fellow, citing his “contributions to functional programming languages.” 

Among the topics we covered in this interview are why he thinks functional programming shows increasing promise of changing the way software is written, why Software Transactional Memory is a much better way of writing concurrent software than locks and condition variables, and why it is so difficult, even at a place like Microsoft Research, to do real studies of whether different programming languages make programmers more or less productive.

Seibel: When did you learn to program?

Peyton Jones: When I was at school. Intel had just about produced the 4004—the world’s first microprocessor. We didn’t have a 4004 or anything like it—it was really a chip that hobbyists could barely get at that stage. The only computer they had available was an IBM schools computer, which was a strange machine built out of spare parts from mainframes. It had no permanent storage whatsoever so you had to type in your program every time you ran it.

It had 100 storage locations, total, which would each store, I think, eight-digit decimal numbers. And this stored both your program and your data. So the name of the game of programming that was to simply to fit the program into 100 storage locations. I can’t quite remember how I got to write my first program. I think I and one other enthusiast at the school spent a lot of time on the schools computer. This would have been when I was about 15, 1974, ’73—that kind of era.

Then after we’d been programming this machine for a little bit we discovered there was a computer at the technical college in Swindon. So we spent an hour on a very slow bus one afternoon a week and went to Swindon where there was this enormous machine—an Elliot 803—which lived in half a dozen large, white, fridge-sized cabinets in a room all its own with a white-coated operator.

After a bit the white-coated operator learned that we could figure out how to use the machine so she went away while we played with this vast engine.

 
It worked with paper tape and teletype so you had your program on a paper tape. We wrote in Algol, so that was my first high-level language. You wrote your program on the tape, you edited on the tape. You wanted to change it, you had to run the tape through the teletype, make it print out a new tape, stop it at the right place, type the new bit—an extremely laborious way to edit your program. A kind of line editor with physical medium. So that was my first experience of programming. It was very motivating.

Seibel: That wasn’t a course at school though.

Peyton Jones: Oh, no! Zero, absolutely no teaching about computers at school.

Seibel: So it was just—“Hey kids, here’s a computer, knock yourself out.” 

Peyton Jones: Absolutely. It was there in a large locked cupboard and you could borrow the key and there it was with a screen and it just displayed a fixed display of what was in the registers and these decimal numbers of what was in memory locations. You could set the program and press Go. You could single-step it. That was really it. So it wasn’t even assembly language programming because there was no ASCII characters at all. It was literally the machine code, displayed in decimal, not even in hexadecimal.

Seibel: But it had a screen?

Peyton Jones: It did have a television screen. That was its sole output medium.

Seibel: And what was the input?

Peyton Jones: It was a kind of touch keyboard. You touched these buttons and they sensed that your finger touched. So that was rather sophisticated—no mechanical keys. It was some kind of capacitive thing— you touched the key and there it was. There were a total of about 20 buttons.

Seibel: So these buttons were just for numbers?

 
Peyton Jones: Numbers and Go and Step. And “show me this memory location.” It was really extremely primitive. And all the more exciting for that.

Seibel: I assume you had to plan your program, probably in excruciating detail, before you get up to this machine and start keying stuff in.

Peyton Jones: First of all you draw a flow diagram. Then you’d break it down into instructions. Then you’d encode the instructions into this strange digital format. And then you type in the numbers. You type in essentially an 800-digit number, which is your program. And then you press Go. If you were lucky you hadn’t mistyped one of those 800 digits and you were in good shape. So we spent a lot of time just looking down the thing with one guy looking at the screen and checking and the other guy saying, “Go to the next location.” 

Then when I went to university at Cambridge, microprocessors were just beginning to take off. So there was a university computing club. There was a big university computing mainframe kind of machine, called Phoenix, with an extremely elaborate accounting system.

The time at which you used it was very significant. You were given a certain amount of units of the machine’s currency and the more memory your program took, the more units you consumed; the longer your program took, the more units you consumed. But the lower the load was, the fewer units your program consumed. So as a result, us undergraduates, who didn’t get a very large allocation, simply spent our nights there because from abou9:00 at night it became rather cheap to run your program. So we would be there 9:00 to 3:00 a.m., writing our programs. And what did we write in mainly? BCPL, I think. So this again was completely hobbyist stuff. I was doing a maths degree at the time. So zero formal teaching in computer science.

There wasn’t a whole undergraduate degree at that time either. That was 1976 to ’79. There was a final year course so you could graduate in computer science. But you couldn’t do three years of computer science— you had to do something else like maths or natural sciences beforehand. In fact I did maths and finished up with a year of electrical sciences. Mainlbecause I thought computing was my hobby—it’d be a bit like cheating to do it as your degree as well; degrees should be hard.

But maths turned out to be a bit too hard because Cambridge is stuffed with extremely brainy mathematicians so I switched to electrical sciences.

Seibel: And electrical sciences—that’s what we’d call electrical engineering in the U.S.?

Peyton Jones: That’s right. At that stage my same friend that I was at school with, Thomas Clarke, was also here at Cambridge. So Thomas and I built various computers. You would buy yourself a microprocessor and lots of 7400 series TTL and wire it up. Our biggest problem, I remember, was printers. Printers and screens. Those were the hard bits.

Seibel: Because they’re expensive.

Peyton Jones: They’re so expensive—yes. You could get the electrical parts for the kind of money students could afford but printers were typically big, fridge-sized line printer things. They had a lot of mechanics in them that made them completely out of our price bracket. That and storage devices— any kind of permanent storage device tended to be tricky. So we tended to have computers with a keyboard, a screen, and not much else. And some kind of primitive tape mechanism.

Seibel: You guys were building these computers from scratch in ’76 to ’79. Isn’t that about the same time the Altair was coming out?

Peyton Jones: That’s right. Hobbyist computers were definitely starting to come out. But we considered those to be rather cheating.

The thing about this machine that we built ourselves was that software was the problem. I think my most advanced program for this machine was Conway’s Game of Life. That worked very nicely. But writing any kind of serious program, like a programming language, was just too much work because it had very limited permanent storage medium. And it was all typing in hexadecimal stuff—no assembler.

Seibel: So more raw machine code.

 
Peyton Jones: Of course the Cambridge mainframe understood BCPL so we were writing lots of BCPL programs. We were actually writing a compiler then for a programming language that we’d invented. We never completed this compiler—it was very elaborate. There were these two completely divorced worlds. Writing compilers in a high-level language for a mainframe and diddling with hardware on the other end.

Seibel: What was the first interesting program you remember writing?

Peyton Jones: A program to extract 24-digit square roots on this schools computer and fit it into 99 memory locations.

Seibel: So you had one spare! 

Peyton Jones: That’s right. It was some kind of Newton-Raphson approximation to do square roots. I was terribly proud of it. What after that? I suppose the next scale up must have been this compiler that we never completed. It was written in BCPL and it was extremely elaborate. We were extremely ambitious with it. There was no type system so we just had enormous sheets of printout with pictures, diagrams of structures and arrows between them.

Seibel: You mean in BCPL there was no type system.

Peyton Jones: Yeah, that’s right. So essentially we wrote out our types by drawing them on large sheets of papers with arrows. That was our type system. That was a pretty large program—in fact it was over ambitious; we never completed it.

Seibel: Do you think you learned any lessons from that failure?

Peyton Jones: That was probably when I first became aware that writing a really big program you could end up with problems of scale—you couldn’t keep enough of it in your head at the same time. Previously all the things I had written, you could keep the whole thing in your head without any trouble. So it was probably the first time I’d done any serious attempt at long-standing documentation.

Seibel: But even that wasn’t enough, in this case?

 
Peyton Jones: Well, we had a lot of other things to do, like get degrees. This was all between 9:00 p.m. and 3:00 a.m.

Seibel: And is there anything you wish you had done differently about learning to program?

Peyton Jones: Well, nobody every taught me to program. I’m not sure I ever really missed that. Today I feel as if my main programming blank spot is that I don’t have a deep, visceral feel for object-oriented programming. Of course I know how to write object-oriented programs and all that. But something different happens when you do something at scale. When you build big programs that last for a long time and you use class hierarchies in a complex way and you build frameworks—that’s what I mean by a deep, visceral understanding. Not the kind of stuff that you’d learn immediately from a book.

I feel that as a lack because I don’t feel I can really be authoritative about what you can and can’t do with object-oriented programming. I’m always very careful in what I say, particularly not to be negative about imperative programming because it’s an incredibly sophisticated and rich programming paradigm. But somehow because of the way my life developed, I never really spent several years writing big C++ programs. That’s how you get some kind of deep, visceral feel and I never have.

Seibel: I think that feeling is usually revulsion.

Peyton Jones: That’s right—but it’s a well-informed revulsion rather than a superficial, “Oh, that sucks” kind of revulsion.

Seibel: So you finished your three years at Cambridge, then what?

Peyton Jones: Then I thought, “Alright, better do a little bit of work on computing.” So I spent one year doing a postgraduate diploma in computer science—my sole formal education in computer science.

Seibel: Is that kind of like a master’s degree?

Peyton Jones: Kind of like a master’s degree. I had a great year. I suspect it was very similar to the computer science tripos, the undergraduate degree.

 
But it was intended for students who hadn’t done any other computer science.

Seibel: Then you spent a couple years in industry before getting back into research. What were you doing then?

Peyton Jones: That was a very small process control and monitoring company. We built hardware and software that sat in microprocessor-based computers that were physically sitting in weigh scale controllers for conveyor belts. One thing I built watched a load cell on a conveyor belt that carried coal; it controlled the speed of the belt and listened to what the load cell was saying and adjusted the speed to make the flow rate what it should be. It was a little real-time operating system, which I wrote in a language called PL/Z. It was a little bit like Algol. I wrote it on a Z80 machine that ran a sort of cut-down Unix called Chromix.

It was a very small company—it was like half a dozen people. Varied up to 15 at times. But because it was small everything was quite volatile. Sometimes we had plenty of money, other times we had none. After two years I’d decided that the entrepreneurial life was not for me. This was my main insight about small companies: to be an entrepreneur you need to get energy from stressful situations involving money, whereas my energy is sapped by stressful situations involving money. My boss was the managing director of this company. The worse things got, the more energetic he would be. He’d come bouncing around and he’d have new technical ideas for software. He was just as happy as a bee. And I realized, that’s what you need, because if it saps your energy, you spend your whole time in a slump.

So I decided that was all much too hard work and looked around for a job and ended up getting a job as a lecturer at University College London. And when I was there I had no PhD, I had no research training. So my head of department gave me time off to do research. Gave me a light teaching load so I could get my research gig started. But I hadn’t the faintest idea what to do. So I would sit in my office with a blank sheet of paper and a sharpened pencil and wait for great ideas. And there was this sort of silence while I would sort of stare around the room waiting for great ideas to come. And nothing much would happen.

 
John Washbrook, who was himself a senior academic in the department, took me under his wing and he told me something that was very important. He said, “Just start something, no matter how humble.” This is not really about programming, this is about research. But no matter how humble and unoriginal and unimportant it may seem, start something and write a paper about it. So that’s what I did. It turned out to be a very significant piece of advice.

I’ve told that to every research student I’ve ever had since. Because it’s how you get started. Once you start the mill turning then computer science is very fractal—almost everything turns out to be interesting, because the subject grows ahead of you. It’s not like a fixed thing that’s there that you’ve got to discover. It just expands.

Seibel: So you came back into academia but you never did get a PhD. How was that possible?

Peyton Jones: These days getting a faculty post without a PhD would be very hard. This must have been 1982, 1983. I applied to UCL because my sister was studying computer science there and she said, “Oh, there are a couple of lectureships at UCL, why don’t you apply?” Much to my astonishment, I was appointed. I can only assume that at the time there must have been a desperate shortage and that anyone that could give a plausible account of himself, in a computing sense, could get hired. Because otherwise, how did they manage to hire somebody without a PhD?

After seven years at UCL I began to think maybe I should get a PhD. But it was a big hassle writing a thesis, really. But, it turns out at Cambridge you can get a PhD by special regulation, which means that you just submit your published work and, with luck, they say, “You are a fine person who should have a PhD.” So I was just getting geared up to do that when I got appointed as a professor at Glasgow. Full professor. So by that time I was called “Professor” so nobody would know whether I had a PhD or not so I dropped the idea. Robin Milner doesn’t have a PhD; it must be a distinguished company. I’ve stuck like that every since.

Seibel: These days, is getting a PhD valuable? Someone once told me a PhD is really a vocational degree—if you want to be a professor, you’ve got tget one but if you don’t want to be a professor, there’s no point. Do you think that analysis applies to computer science?

Peyton Jones: That part is certainly true. It’s necessary but not sufficient if you want to stick with research as a career—either academic or at somewhere like Microsoft Research or Google’s research labs—a serious industrial research lab. You really need a PhD to get past the starting post.

If you don’t want to pursue a career in research, then I think it becomes a follow-your-heart kind of thing. You’re five times as productive if you’re working on something that makes you enthusiastic. So if you find yourself thinking, “I just love this and I’d just like to have some time to dig into it some more,” a PhD is a fantastic opportunity to spend three years in Britain, or rather longer in the States, just studying something. It’s an incredible freedom really because you’re sort of a parasite on society. If you know you don’t want to do full-time research as a career then the reason to do a PhD is because you’re just enthusiastic and inquisitive and interested. But PhDs are rather strange anyway. They force you to work on your own and produce a substantial thesis that most people won’t read—they’ll read your papers. So it’s an unusual research mode.

Once you’ve finished a PhD you start working much more collaboratively with lots of other people on typically smaller, more bite-sized pieces of work. I think in some ways a PhD is an odd preparation, even for research. Odder in Britain because of its compressed timescale. I think in the States you can be more collaborative for a while until you zero in on your own research program.

Seibel: Speaking of research and academics, functional programming is quite popular within the research community but I think a lot of people outside that community see functional programming as being driven by ideas that, while neat, can be very mathematical and divorced from day-to-day programming. Is that a fair characterization?

Peyton Jones: I think it’s about half fair. I characterize functional programming—that is, purely functional programming, where side effects are somehow really relegated to a world of their own—as a radical and elegant attack on the whole enterprise of writing programs. Things that arradical are by definition not evolutionary from the state of where things are at.

Today “where things are at” is that big companies are pouring immense resources into ecosystems and editors and profilers and tools and programmers and skills and all that kind of stuff. The mainstream is, by definition, deeply practical. Meanwhile this radical and elegant stuff of functional programming has much less of that deep, infrastructural support. But at the same time that doesn’t necessarily make it self-indulgent to pursue it. Because, after all, unless some people are working on radical and elegant things you’re going to end up in a local optimum, incrementally optimizing the mainstream but stuck on a low hill.

So I think that one of the good things about the whole business of academic research is that professors can go off and do sort of loopy things without being asked how it’s benefiting the bottom line. Some will do things that turn out to be fantastically important, and some less so; but you can’t tell which is which in advance! So my big-picture justification for why it’s worth some people, like me, spending a lot of time on purely functional programming, is that it shows promise. I don’t want to claim that it’s exactly the way that everyone will be writing programs in the future, but it shows promise. And actually I’ll make the case that it shows increasing promise. I see it as, when the limestone of imperative programming is worn away, the granite of functional programming will be observed.

That said, I think purely functional programming started quite geeky and academic and mathematical. The story of the last, really, 20 years—all the time I’ve been working on it—has been a story of becoming increasingly practical, focusing not just on abstract ideas but trying to overcome, one by one, the obstacles that prevent real-life programmers using functional programming languages for real applications. The development of Haskell itself is an example of that.

It’s good that there are a bunch of people out here, maybe slightly impractical, who are heading towards the mainstream and maybe the perspectives you learn over here in the purely functional world can inform and illuminate the mainstream. That, you can see, has happened. Lots of stuff about type systems and generics were originally developed in the context of functional programming languages. It was a kind of laboratory iwhich some of those ideas were developed. Generators and lazy streams are another example. Python has list comprehensions at the syntactic level. There are lots of individual things. Usually they’ve been rebranded and sometimes, to fit the mainstream context, they’ve been changed quite a bit. I don’t want to claim a kind of exclusive genealogy but I do think a lot of ideas have nevertheless percolated across. So it’s been useful.

Seibel: For you, what about the relation between research and actually programming?

Peyton Jones: Oh, they interact a lot. My area of study is programming languages. What are programming languages for in the end? They’re to make it easier to program. They’re the user interface of programming, in effect. So programming and programming language research are deeply related. One thing we’re not good about is this: the proof of the pudding is in the eating, so you should watch programmers eating. That is, you should do proper, formalized studies of programmers programming and see what they do. And that’s jolly expensive. And it’s also more “squishy.” It’s harder to come up with unequivocal results.

So the culture of the programming-language community is much more, “prove that your type system is sound and complete,” kind of stuff. We dodge, probably, the more important but much harder to answer questions about whether, in practice, they make people more productive. But they are questions that are really hard to give convincing answers to. Are you more productive writing a functional program or an object-oriented program to do the same thing? Even if you could spend a lot of money on doing serious experiments, I’m not sure you’d come up with results which people would actually buy.

Seibel: Do you guys do any, even small-scale experiments? You’re working for Microsoft, who has plenty of cash, so why not get a team of experienced Haskellites and a team of experienced people and give them the same task and see what happens? That’s the kind of test you would need, right?

Peyton Jones: Yeah, yeah, that’s right. It’s partly a question of money. But it’s not just a question of money. It’s also sort of time and attention. To do that kind of experiment your whole methodology is different. And you need to shift culturally as well. And, while Microsoft, from the outside, appears thave plenty of cash, in fact the story here is largely one researcher and his workstation. We can’t just turn on money for any particular thing. Be nice if we could. Nearer the coalface, as it were, there are big usability labs in Redmond where they do perform experiments on things that are proto products. New versions of Visual Studio are extensively usability tested.

Seibel: Presumably that’s more for the total user interaction, rather than for programming language issues.

Peyton Jones: Well, they also do some interesting work on testing APIs. Steven Clarke and his colleagues at Redmond have made systematic attempts to watch programmers, given a new API, talk through what they’re trying to do. And they get the people who designed the API to sit behind a glass screen and watch them.

And the guys sitting there behind the glass screen say, “No, no, don’t do that! That’s not the right way!” But it’s soundproof. That turns out often to be very instructive. They go and change their API. To be honest, programming language research is weak on that score. But it is partly because these are difficult questions to answer. And culturally we’re not well adapted to do it. I regard it as a weakness. But not one that I personally feel terribly well equipped to address.

Seibel: So if researchers are coming up with interesting ideas about how to improve programming, are the best of those good ideas from research labs and universities percolating into practice fast enough?

Peyton Jones: Well, fast enough. I don’t know. Whenever I talk to people who are actually involved in building products that customers want and are therefore prepared to pay for, I’m very conscious that many of the things that bother me just aren’t on their radar at all.

They have to do something this week that their customers are going to value; they just don’t have time to mess about with something that might work or that might even work in some ways but in total isn’t yet ready for prime time.

There’s a bit of a disconnect—it’s sort of a chicken-and-egg problem there. Sometimes the ideas that are developed in research need quite a bit oengineering effort around the edges that isn’t fundamental research in order to be directly useful.

I wouldn’t like to imply that developers on the ground are being dopey about this, just not taking up good ideas that would benefit their lives. They’re doing what they’re doing for quite good reasons. There is sometimes a bit of a gap between research prototypes and stuff that you can build in reality. And I think that Microsoft is actually doing quite well here because Microsoft Research does fill that gap a bit and does have quite a bit of mechanism—incubation groups and so forth—whose aim is to put researchers and developers in closer touch with each other and perhaps to help provide some extra effort to lift things across the boundary. So MSR is kind of as good as it gets, I think, as far as crossing that boundary is concerned.

There are layers to this kind of onion. For a mainstream developer shop that’s stuffed with Java, not only is functional programming a radically different way of thinking about programming but also there are lots of interop questions. And have you got enough books and are there enough libraries? So there’s this whole ecosystem that goes with programming, people and skills and libraries and frameworks and tools and so forth.

If you have enough of those blockers you get sort of stuck. So I think different pieces of research technology in programming language live on different points on a spectrum. Some are more evolutionary from where we are. You can say, “It just plugs right into your existing framework, it works on unmodified Java, it’s a static analysis that points you to bugs in your code and yipee!” That’s much easier to absorb than, “Here’s a whole new way of thinking about programming.” 

That said, I think that if we’re specifically discussing functional programming then I do think that we have seen a qualitative sea change in people’s attitude. Many more people have heard about functional programming than ever used to. Suddenly rather than always having to explain what Haskell is, sometimes people say, “Oh, I’ve heard about that. In fact I was reading about it on Slashdot the other week and I gather it’s rather cool.” That just didn’t happen a few years ago.

 
But what’s underlying that? Is it just a random popularity thing? Or maybe part of it is that more students have been taught about functional programming in university and are now in managerial or seniorish positions. Perhaps. But perhaps it’s also to do with as we scale up software dealing with the bad consequences of unrestricted side effects and as we want to deal with more verification and parallelism, all those issues become more pressing. I think that leads to this greater level of interest. I think gradually the needle is moving across this cost/benefit tradeoff.

Seibel: When did you get introduced to functional programming?

Peyton Jones: I didn’t learn about functional programming until something like my final year at Cambridge when I went to a short course given by Arthur Norman. Arthur Norman was a brilliant and slightly eccentric lecturer in the department. Wonderful guy, interested in symbolic algebra so he was big into Lisp as well. He gave a short course on functional programming in which he showed us how to build doubly linked lists without using any side effects at all. I vividly remember this because this was my first notion that you could do something that weird—you’d think if you build a doubly-linked list you have to allocate the cells and then you have to fill them in to make them point to each other. It looks as if you just have to use side effects somehow.

But he showed how, in a purely functional language, you could actually write it without using any side effects. So that opened my eyes to the fact that functional programming, which at that stage I knew very little about, was a medium you could really write quite interesting programs in rather than just little toy ones.

Seibel: I think a lot of people might look at that demonstration and say, “Oh, isn’t that interesting,” and then still go back to hacking BCPL. Why do you think you were able to take the leap so much farther, spending most of your career trying to show how folks can really use this stuff?

Peyton Jones: There was one other component, which was David Turner’s papers on S-K combinators. S-K combinators are a way of translating and then executing the lambda calculus. I’d learned a little bit about the lambda calculus, probably by osmosis at the time. What Turner’s papers showed was how to translate lambda calculus into the threcombinators, S, K, and I. S, K, and I are all just closed lambda terms. So in effect it says, “You can translate these arbitrary complicated lambda terms into just these three.” In fact, you can get rid of I as well because I equals SKK.

So there’s this strange compilation step in which you take a lambda term that you can kind of understand and turn it into a complete mess of S’s and K’s that you can’t understand at all. But when you apply it to an argument, miraculously, it computes the same answer as the original lambda stuff did. And that was another example of something that was very clever and, to me at the time, implausible. But nevertheless you could see that it would just always work.

I don’t know quite what it was that turned me on about this. I found it completely inspirational. It’s partly, I suppose, because, being interested in hardware, it felt like this is a way you could implement the lambda calculus. Because the lambda calculus doesn’t look like it’s an implementation mechanism at all. It’s a bit of a mathematical way of thinking, a bit remote from the machine. This S-K stuff looks as if you could just run it and indeed you can.

Seibel: So, you had a sense that, OK, I’ll just build a machine that has S and K hardwired and then all I’ve got to do is compile things to a series of S and K ops.

Peyton Jones: In fact that’s exactly what my friends did. William Stoye and Thomas Clarke and a couple others, built this machine, SKIM, the SKI Machine, which directly executed S and K. For some reason I wasn’t directly involved in that project. But at the time there was this feeling developing. John Backus’s paper, called, “Can Programming Be Liberated from the von Neumann Style” was extremely influential at the time. It was his Turing Award lecture and he was this guy who had invented Fortran saying, in effect, “Functional programming is the way of the future.” 

Furthermore, he said, “Maybe we should develop new computer architectures to execute this stuff on.” So this very high-level endorsement of this research area meant we cited that paper like crazy. And so SKIM was an example of such a thing. We thought maybe this unusual way of going about executing, or at least thinking about, programs turns into completely different sort of computer architecture. That phase lasted from about 1980 to 1990—radical architectures for functional programming. I now regard it as slightly misdirected but nevertheless it was terribly exciting.

Lazy evaluation was another huge motivating factor. With the benefit of hindsight I now think lazy evaluation is just wonderful but at that time it was sort of pivotal. Lazy evaluation is this idea that functions don’t evaluate their arguments. Again the motivating factor was something to do with it being beautiful or elegant and unusual and radical.

That’s kind of good for catching the imagination: it looks as if this might be a way of thinking about programming in a whole new way. Rather than just putting one more brick in the wall, we can build a whole new wall. That’s very exciting. I was strongly motivated by that. Was it just that it was a neat trick? In some ways I think neat tricks are very significant. Lazy evaluation was just so neat and you could do such remarkable different things that you wouldn’t think were possible.

Seibel: Like what?

Peyton Jones: I remember my friend John Hughes wrote a program for me. For a project I was doing two implementations of the lambda calculus and comparing their performance, so John gave me some test programs. One of them was a program that computed the decimal expansion of e to arbitrary precision. It was a lazy program—it was rather beautiful because it produced all the digits of e.

Seibel: Eventually.

Peyton Jones: Eventually, that’s right. But it was up to the consumer. You didn’t have to say how many digits to produce in advance. You just got given this list and you kept hauling on elements of the list and it wouldn’t give you another digit until it had spent enough cycles computing it. So that’s not something that’s very obvious to do if you’re writing a C program. Actually you can do it with enough cleverness. But it’s not a natural programming paradigm for C. You can almost only do it once you’ve seen the lazy functional program. Whereas John’s program was just about four or five lines. Amazing.

 
Seibel: Other languages have since special-cased that kind of computation with, for example, generators in Python or something where you can yield values. Was there something that made you say, “Aha; there are lots of things that could be fruitfully looked at as an infinite series of computations from which we just want to draw answers until we’re tired of it?” As opposed to saying, “Oh, that’s an interesting technique for certain problems but not the basis for everything.” 

Peyton Jones: I think at this stage I wasn’t as reflective as that. I just thought it was so cool. And fun. I think it’s important to do what you find motivating and interesting and follow it. I just found it very inspiring. I don’t think I really thought there are deep principled reasons why this is the way to do programming. I just thought it was a rather wonderful way to do programming. I like skiing. Well, why do I like skiing? Not because it’s going to change the world—just because it’s a lot of fun.

I now think the important thing about laziness is that it kept us pure. You’ll have seen this in several of my talks probably. But I actually really like laziness. Given a choice I’d choose a lazy language. I think it’s really helpful for all kinds of programming things. I’m sure you’ve read John Hughes’s paper, “Why Functional Programming Matters.” It’s probably the earliest articulate exposition of why laziness might be important in more than a cute way. And his main story is that it helps you write modular programs.

Lazy evaluation lets you write generators—his example is generate all the possible moves in your chess game—separately from your consumer, which walks over the tree and does alpha-beta minimaxing or something. Or if you’re generating all the sequence of approximations of an answer, then you have a consumer who says when to stop. It turns out that by separating generators from consumers you can modularly decompose your program. Whereas, if you’re having to generate it along with a consumer that’s saying when to stop, that can make your program much less modular. Modular in the sense of separate thoughts in separate places that can be composed together. John’s paper gives some nice examples of ways in which you can change the consumer or change the generator, independently from each other, and that lets you plug together new programs that would have been more difficult to get by modifying one tightly interwoven one.

 
So that’s all about why laziness is a good thing. It’s also very helpful in a very local level in your program. You tend to find Haskell programmers will write down a function definition with some local definitions. So they’ll say “f of x equals blah, blah, blah where . . .” And in the where clause they write down a bunch of definitions and of these definitions, not all are needed in all cases. But you just write them down anyway. The ones that are needed will get evaluated; the ones that aren’t needed won’t. So you don’t have to think, “Oh, goodness, all of these sub expressions are going to be evaluated but I can’t evaluate that because that would crash because of a divide by zero so I have to move the definition into the right branch of the conditional.” 

There’s none of that. You tend to just write down auxiliary definitions that might be needed and the ones that are needed will be evaluated. So that’s a kind of programming convenience thing. It’s a very, very convenient mechanism.

But getting back to the big picture, if you have a lazy evaluator, it’s harder to predict exactly when an expression is going to be evaluated. So that means if you want to print something on the screen, every call-by-value language, where the order of evaluation is completely explicit, does that by having an impure “function”—I’m putting quotes around it because it now isn’t a function at all—with type something like string to unit. You call this function and as a side effect it puts something on the screen. That’s what happens in Lisp; it also happens in ML. It happens in essentially every call-by-value language.

Now in a pure language, if you have a function from string to unit you would never need to call it because you know that it just gives the answer unit. That’s all a function can do, is give you the answer. And you know what the answer is. But of course if it has side effects, it’s very important that you do call it. In a lazy language the trouble is if you say, “f applied to print "hello",” then whether f evaluates its first argument is not apparent to the caller of the function. It’s something to do with the innards of the function. And if you pass it two arguments, f of print "hello" and print "goodbye", then you might print either or both in either order or neither. So somehow, with lazy evaluation, doing input/output by side effect just isn’t feasible. You can’t write sensible, reliable, predictable programs that way. So, we had to put up with that. It was a bit embarrassing really because you couldn’t realldo any input/output to speak of. So for a long time we essentially had programs which could just take a string to a string. That was what the whole program did. The input string was the input and result string was the output and that’s all the program could really ever do.

You could get a bit clever by making the output string encode some output commands that were interpreted by some outer interpreter. So the output string might say, “Print this on the screen; put that on the disk.” An interpreter could actually do that. So you imagine the functional program is all nice and pure and there’s sort of this evil interpreter that interprets a string of commands. But then, of course, if you read a file, how do you get the input back into the program? Well, that’s not a problem, because you can output a string of commands that are interpreted by the evil interpreter and using lazy evaluation, it can dump the results back into the input of the program. So the program now takes a stream of responses to a stream of requests. The stream of requests go to the evil interpreter that does the things to the world. Each request generates a response that’s then fed back to the input. And because evaluation is lazy, the program has emitted a response just in time for it to come round the loop and be consumed as an input. But it was a bit fragile because if you consumed your response a bit too eagerly, then you get some kind of deadlock. Because you’d be asking for the answer to a question you hadn’t yet spat out of your back end yet.

The point of this is laziness drove us into a corner in which we had to think of ways around this I/O problem. I think that that was extremely important. The single most important thing about laziness was it drove us there. But that wasn’t the way it started. Where it started was, laziness is cool; what a great programming idiom.

Seibel: Since you started programming, what’s changed about how you think about programming?

Peyton Jones: I think probably the big changes in how I think about programming have been to do with monads and type systems. Compared to the early 80s, thinking about purely functional programming with relatively simple type systems, now I think about a mixture of purely functional, imperative, and concurrent programming mediated by monads. And the types have become a lot more sophisticated, allowing you to express much wider range of programs than I think, at that stage, I’d envisaged. You can view both of those as somewhat evolutionary, I suppose.

Seibel: For instance, since your first abortive attempt at writing a compiler you’ve written lots of compilers. You must have learned some things about how to do that that enable you to do it successfully now.

Peyton Jones: Yes. Well, lots of things. Of course that was a compiler for an imperative language written in an imperative language. Now I’m writing a compiler for a functional language in a functional language. But a big feature of GHC, our compiler for Haskell, is that the intermediate language it uses is itself typed.

Seibel: And is the typing on the intermediate representation just carrying through the typing from the original source?

Peyton Jones: It is, but it’s much more explicit. In the original source, lots of type inference is going on and the source language is carefully crafted so that type inference is possible. In the intermediate language, the type system is much more general, much more expressive because it’s more explicit: every function argument is decorated with its type. There’s no type inference, there’s just type checking for the intermediate language. So it’s an explicitly typed language whereas the source language is implicitly typed.

Type inference is based on a carefully chosen set of rules that make sure that it just fits within what the type inference engine can figure out. If you transform the program by a source-to-source transformation, maybe you’ve now moved outside that boundary. Type inference can’t reach it any more. So that’s bad for an optimization. You don’t want optimizations to have to worry about whether you might have just gone out of the boundaries of type inference.

Seibel: So that points out that there are programs that are correct, because you’re assuming a legitimate source-to-source transformation, which, if you had written it by hand, the compiler would have said, “I’m sorry; I can’t type this.” 

Peyton Jones: Right. That’s the nature of static type systems—and why dynamic languages are still interesting and important. There are programyou can write which can’t be typed by a particular type system but which nevertheless don’t “go wrong” at runtime, which is the gold standard— don’t segfault, don’t add integers to characters. They’re just fine.

Seibel: So when advocates of dynamic and static typing bicker the dynamic folks say, “Well, there are lots of those programs—static typing gets in the way of writing the program I want to write.” And then the fans of static typing say, “No, they exist but in reality it’s not a problem.” What’s your take on that?

Peyton Jones: It’s partly to do with simple familiarity. It’s very like me saying I’ve not got a visceral feel for writing C++ programs. Or, you don’t miss lazy evaluation because you’ve never had it whereas I’d miss it because I’m going to use it a lot. Maybe dynamic typing is a bit like that. My feeling— for what it’s worth, given that I’m biased culturally—is that large chunks of programs can be perfectly well statically typed, particularly in these very rich type systems. And where it’s possible, it’s very valuable for reasons that have been extensively rehearsed.

But one that is less often rehearsed is maintenance. When you have a blob of code that you wrote three years ago and you want to make a systemic change to it—not just a little tweak to one procedure, but something that is going to have pervasive effects—I find type systems are incredibly helpful.

This happens in our own compiler. I can make a change to GHC, to data representations that pervade the compiler, and can be confident that I’ve found all the places where they’re used. And I’d be very anxious about that in a more dynamic language. I’d be anxious that I’d missed one and shipped a compiler where somebody feeds in some data that I never had and it just fell over something that I hadn’t consistently changed.

I suppose static types, for me, also perform part of my explanation of what the program does. It’s a little language in which I can say something, but not too much, about what this program does. People often ask, “What’s the equivalent of UML diagrams for a functional language?” And I think the best answer I’ve ever been able to come up with is, it’s the type system. When an object-oriented programmer might draw some pictures, I’m sitting there writing type signatures. They’re not diagrammatic, to be sure, but because they are a formal language, they form a permanent part of the program texand are statically checked against the code that I write. So they have all sorts of good properties, too. It’s almost an architectural description of part of what your program does.

Seibel: So do you ever write a program that you know is correct but somehow falls outside the bounds of the type checker?

Peyton Jones: This comes up when you’re doing generic programming, where you want to write functions that will take data of any type and just walk over it and serialize it, say. So that’s a time when types can be a bit awkward and an untyped language is particularly straightforward. It couldn’t be easier to write a serializer in an untyped language.

Now there’s a small cottage industry of people describing clever typed ways of writing generic programs. I think such things are fascinating. But it’s somehow just isn’t as simple as writing it in a dynamically typed language. I’m trying to persuade John Hughes to write a paper for the Journal of Functional Programming on why static typing is bad. Because I think it would be very interesting to have a paper from John, who’s a mainstream, strongly typed, very sophisticated functional programmer, who is now doing a lot of work in untyped Erlang, saying why static types are bad. I think he would write a very reflective and interesting paper. I don’t know quite where we’ll end up.

I think I would still say, “Where static typing fits, do it every time because it has just fantastic maintenance benefits.” It helps you think about your program; it helps you write it, all that kind of stuff. But the fact that we keep generating more and more sophisticated type systems is an indication that we’re trying to keep pushing the boundary out to say more in the world— to cover more programs. So the story hasn’t finished yet.

The dependently typed programming people would say, “Ultimately the type system should be able to express absolutely anything.” But types are funny things—types are like a very compact specification language. They say something about the function but not so much that you can’t fit it in your head at one time. So an important thing about a type is it’s kind of crisp. If it goes on for two pages, then it stops conveying all the information it should.

 
I think the direction I’d like to see things go is to have still crisp and compact types which are a little bit weak, precisely so that they can be crisp, along with invariants, perhaps stated in a rather richer language than the inferable type system, but which are still amenable to static checking. Something I’m working on in another project is to try to do static verification for pre- and post-conditions and data-type invariants.

Seibel: Similar to Design by Contract in Eiffel?

Peyton Jones: That’s right. You’d like to be able to write a contract for a function like, “You give me arguments that are bigger than zero and I’ll give you a result that is smaller than zero.” 

Seibel: How do you go about designing software?

Peyton Jones: I suppose I would say that usually the dominant problem when I’m thinking about writing a program—thinking about writing some new piece of GHC—is not how to get the idea into code. But it’s rather, what is the idea?

To take an example, at the moment we’re in mid-flight for moving GHC’s back end, the code generation part, to refactor it in a new way. At the moment there’s a step in the compiler that takes essentially a functional language and translates it into C--, which is an imperative language. And that’s a pretty big step. It’s called C-- because it’s like a subset of C. But it’s really meant to be a portable assembly language. And it’s not printed out in ASCII—it’s just an internal data type. So this step in the compiler is a function from a data structure representing a functional program to a data structure representing an imperative program. How do you make that step?

Well, I have a pretty complicated bit of code that does that at the moment. But a couple of days ago I realized that it could be separated into two parts: first transform it into a dialect of C--, which allows procedure calls—inside a procedure, you can call a procedure. Then translate that into a sub-language that has no calls—only has tail calls.

Then the name of the game is figuring out, just what is the data type? This C-- stuff, what is it? It’s a data structure representing an imperative program.And as you make the second step, you walk over the program, 

 
looking at each bit, one at a time. So your focus of attention moves down the control flow, or perhaps back up through the control flow. A good data structure for representing that is called a “zipper”—which is a very useful purely functional data structure for moving the focus around a purely functional data structure.

Norman Ramsey at Harvard found a way to use this for walking around data structures that represent imperative control flow graphs. So he and I and John Dias then spent a while reengineering GHC’s back end to adopt essentially this factored technology. And in doing so making it much more general so we can now use this same back end as a back end for other languages.

A lot of our discussion was essentially at the type level. Norman would say, “Here’s the API,”—by giving a type signature—and I would say, “That looks way complicated, why is it like that?” And he’d explain why and I’d say, “Couldn’t it be simpler this way.” So we spent a lot of time to’ing and fro’ing at the level of describing types.

But a lot of the time it wasn’t really about programming as such—it was about, what is the idea? What are we trying to do with this dataflow analysis, anyway? You try to say in a clear way what this step of the program is meant to do. So we spent quite a lot of time just being clear on what the inputs and the outputs are and working on the data types of the inputs and the outputs. Just getting the data types right, already you’ve said quite a lot about what your program does. A surprisingly large amount, in fact.

Seibel: How does thinking about the types relate to actually sitting down and coding? Once you sketch out the types can you sit down and write the code? Or does the act of writing the code feed back into your understanding of the types?

Peyton Jones: Oh, more the latter, yes. I’ll start writing type signatures into a file right away. Actually I’ll probably start writing some code that manipulates values of those types. Then I’ll go back and change the data types. It’s not a two-stage process where we say, “Now I’ve done the types, I can write the code.” 

 
If anything I’m a bit ill-disciplined about this. This comes from not working as part of a large team. You can do things when you’re working on code that one person can still get their head around that you probably couldn’t in a much bigger team.

Seibel: You mentioned that in this latest code upheaval in GHC, things got much more general. GHC is a big program that’s evolved over time so you’ve had the chance to benefit from generality and the chance to pay the cost of over-generality. Have you learned anything about how to strike the balance between over- and under- generalization?

Peyton Jones: I think my default is not to write something very general to begin with. So I try to make my programs as beautiful as I can but not necessarily as general as I can. There’s a difference. I try to write code that will do the task at hand in a way that’s as clear and perspicuous as I can make it. Only when I’ve found myself writing essentially the same code more than once, then I’ll think, “Oh, let’s just do it once, passing some extra arguments to parameterize it over the bits that are different between the two.” 

Seibel: What is your actual programming environment? What tools do you use?

Peyton Jones: Oh, terribly primitive. I just sit there with Emacs and compile with GHC. That’s just about it. There are profiling tools that come with our compiler and people often use those for profiling Haskell programs. And we do that for profiling the compiler itself. GHC dumps a lot of intermediate output so I can see what’s going on.

Debugging, for me, is often, the compiler isn’t generating good code so I’m eyeballing the state of its entrails. Or, take this little source program; compile it this far; look at that. That’s debugging for me. It’s seldom single-stepping through the program—it’s more looking at values of different parts in compilation.

I don’t even have any very sophisticated Emacs jiggery-pokery. Which some people do. There’s also a whole world of people out there who are used to Visual Studio and Eclipse kind of IDEs. I think a cultural barrier to adoption of functional programming languages is partly that we haven’t got the IDstory sorted out. There’s a bit of a chicken-and-egg problem here. At the moment the chicken is getting busier—there’s more interest in functional programming generally. I’m hoping that will provoke work on the egg. It’s a lot of engineering to build an IDE for Haskell. Even with Visual Studio as a shell or Eclipse as a shell, there’s quite a lot of work in making a plugin that’s really smooth and does everything right.

Seibel: GHC has a read-eval-print loop, GHCI. Do you tend program Haskell interactively?

Peyton Jones: Actually, I tend to mostly edit and compile. But other people just live their whole lives in GHCI.

Seibel: When it comes to testing, I suppose one of the nice things about functional languages is when you want to test some little function in the bowels of your program, you just have to figure out what form is its input going to be.

Peyton Jones: Well, for me, if the input data is simple enough that you could do that, it’s probably not going to be the problem with my program. The problem with my program is going to be some fairly humongous input program that GHC is trying to compile and getting the wrong answer for it.

Testing is, I think, frightfully important for writing down properties and QuickCheck properties are really useful—QuickCheck is a Haskell library for generating random tests for a function based on its type. But I was trying to think why I don’t use QuickCheck—which is a very nice tool—more. I think it’s because the situations that cause me trouble are ones that I would find it difficult to generate test data for. In any case, there are loads of people out there generating programs that make GHC barf in one way or another. That’s what GHC’s bug tracker is about.

So typically I’m starting with something that’s not right, already. Maybe the compiler could just fall over altogether or reject a program when it shouldn’t. Or it could just generate suboptimal code. If it’s just generating bad code, I’ll look at the code at various stages in the compilation pipeline and say, “It looks good then; it looks good then. Bah, it’s gone bad here; what’s gone wrong?” 

 
Seibel: So how do you actually look at it?

Peyton Jones: GHC has flags that let you say, in rather a batch-dumpy kind of way, “Just print out various things.” 

Seibel: Built-in print statement debugging?

Peyton Jones: Yes. And it’s aided by the fact that the structure is like most compilers: it has this top-level structure of a pipeline of things that happen. If something’s gone wrong in the middle of one of these passes, then that could be a bit trickier. But I tend to use rather unsophisticated debugging techniques. Just show me the program before and after this pass. Aaah, I see what’s going wrong. Or sometimes I don’t see what’s going wrong so then I might scatter a few unsafe printfs around to show me what’s actually going on.

There are various debugging environments for Haskell—a summer student, Pepe Iborra, did a nice one earlier this year which now comes with GHC, which is an interactive debugger of some kind. Which I’ve not used very much yet. Partly because we haven’t had one for so long, because it’s less obvious how do you single-step a functional program.

It’s been a kind of interesting research question of how you go about debugging functional programs for some time. It’s a bit embarrassing that we can’t tick that box in a straightforward way, but that makes it an interesting research problem.

That was the long way around of saying that I tend to use terribly crude debugging techniques with unsafe printfs. And I’m not very proud of that. But for a long time we didn’t have anything else. At least as far as GHC is concerned, I’ve evolved mechanisms that mean that’s the shortest path to completion for me.

Seibel: That seems to be a common story. It sort of makes you wonder about the utility of writing better debuggers if so many people get by with print statement debugging.

Peyton Jones: There’s a cultural thing though. On the .NET platform with debuggers that people have put tens or hundreds of man-years intengineering, I think it’s a qualitatively different experience. I think debuggers do require perhaps more engineering cycles to get to work well. But if you put them in, you do get something that is really quite remarkably more helpful.

Maybe the people that you’ve been mainly talking to are more in the academic software mold. And also perhaps have grown up with sophisticated debugging environments less. I wouldn’t like to draw any general lessons. I certainly wouldn’t wish to denigrate or downplay the importance of good debugging environments. Particularly in these rather complicated ecosystems where there are many, many, many layers of software. GHC is a very simple system compared to a full-on .NET environment with layers of DOMs and UMLs and I don’t know what kind of goop. The real world gets so goopy that more mechanical support may well be really important.

Seibel: Another approach to getting correct software is to use formal proofs. What do you think about the prospect of that being useful?

Peyton Jones: Suppose you declare that your goal is for everything to have a machine-checked proof of correctness. It’s not even obvious what that would mean. Mechanically proved against what? Against some specification. Well how do you write the specification? This is now meant to be a specification of everything the program does. Otherwise you wouldn’t have proved that it does everything that it should do. So you must have a formal specification for everything it should do. Well now—how are you going to write that specification? You’ll probably write it in a functional language. In which case, maybe that’s your program.

I’m being a bit fast and loose here because you can say some things in specification languages that you can’t say in programs like, “The result of the function is that y such that y squared equals x.” That’s a good specification for a square-root function but it’s not very executable. Nevertheless, I think to try to specify all that a program should do, you get specifications that are themselves so complicated that you’re no longer confident that they say what you intended.

I think much more productive for real life is to write down some properties that you’d like the program to have. You’d like to say, “This valve shoulnever be shut at the same time as that valve. This tree should always be balanced. This function should always return a result that’s bigger than zero.” These are all little partial specifications. They’re not complete specifications. They’re just things that you would like to be true.

How do you write those down? Well, functional languages are rather good at that. In fact this is exactly what happens when you write a QuickCheck specification; you write down properties as Haskell functions. Say we want to check that reverse is its own inverse—well, you might write checkreverse with type list of A to bool. So checkreverse of xs is reverse of reverse xs equals xs. So this is a function that should always return true. That’s what a property function is. But it’s just written in the same language—so that’s nice.

Now you might hope to do some static checking on this. It might be hard or easy. But even having the property written down in a formal way is a real help. You can test it by generating test data, which is, indeed, just what QuickCheck does.

So rather than trying to write down specifications for all that a program does I think it’s much more productive to write down partial specifications. Perhaps multiple partial specifications. And then check them either by testing or by dynamic checks or by static checks. You never prove that your program is right. You just increase your confidence that it’s right. And I think that’s all that anybody ever does.

Seibel: So you define however many properties, covering the things you care about. And then you can choose to confirm that those properties actually hold either statically or dynamically, depending on what’s actually feasible. Because we may not know how to statically check them all?

Peyton Jones: Right. But in a functional setting, you have a better chance. But we’ve still been dragging our feet a bit about demonstrating that. Nevertheless—step one is to write down these properties in the first place.

But I think the big thing is to get away from this monolithic, all-or-nothing story about specification and to say that you can do useful static and dynamic tests on partial specifications. These will increase your confidence in the correctness of your program and that is all you can possibly hope for.

 
Even the allegedly complete specifications miss out—you know, it has to work in .1 of a second. Or must fit in 10KB of memory. Resource things are often not covered. Or timing things. There’s endless little stuff that means the program might actually not function as desired even though it meets its formal specification. So I think we’re kidding ourselves to say we’ve actually proved the whole thing is completely right. Best thing to do is to acknowledge that and say we’re improving our confidence—that’s what we’re doing. And that can start quite modestly—you might have improved your confidence by 75 percent with only 5 percent of the effort. That’d be good.

Seibel: Let’s talk about concurrency a little bit. Guy Steele asked me to ask you: “Is STM going to save the world?” 

Peyton Jones: Oh, no. STM is not going to save the world on its own. Concurrency, and parallel programming generally, is a many-faceted beast and I don’t think it will be slain by a single bullet. I’m a diversifist when it comes to concurrency.

It’s tempting to say, “Use one programming paradigm for writing concurrent programs and implement it really well and that’s it;” people should just learn how to write concurrent programs using that paradigm. But I just don’t believe it. I think for some styles of programming you might want to use message passing. For others you might want to use STM. For others data parallelism is much better. The programmer is going to need to grapple with more than one way to do it.

But if you ask me, is STM better than locks and condition variables? Now you’re comparing like with like. Yes. I think it completely dominates locks and condition variables. So just forget locks and condition variables. For multiple program counters, multiple threads, diddling on shared memory on a shared-memory multicore: STM. But is that the only way to write concurrent programs? Absolutely not.

Seibel: A criticism I’ve heard of STM was that when it really gets down to it, optimistic concurrency won’t allow as much concurrency as you hope. I think the claim was you can fairly easily get in these situations where you’re really not making progress.

 
Peyton Jones: You do have to worry about starvation. My favorite example here is of one big transaction that keeps failing to commit because a little transaction gets in there and commits first. So an example would be a librarian who’s reorganizing their library. They start optimistically reorganizing their library. And they’ve got two-thirds of the way through and an undergraduate comes along and borrows a book. Well, he commits his transaction successfully because the library reorganization hasn’t committed. The librarian gets to the end and discovers, ah, I saw an inconsistent view of memory because the library changed while I was reorganizing it so I just have to go back and start again.

Seibel: In a locks-and-condition-variables program it would probably go the other way—the librarian would lock the library and nobody could check out books until it’s completely reorganized. So you would probably look at this problem and immediately say, “We can’t lock the library until we’re done,” disallowing checkouts so we have to come up with some hairier locking scheme.

Peyton Jones: Right. Make a little sub-library or something—put the commonly borrowed books out there so undergraduates can borrow them while you lock the main library and reorganize it or something. So now you’ve got to think of an application-specific strategy and now you’ve got to express it in some way. Well, the same problem arises in both cases—you need an application-specific strategy so you can reorganize the library despite not wanting to block out all sorts of borrowing. Once you’ve done the hard thinking about how you wish to do it, now you’ve got to express that. What is the medium in which to express it? STM is a clear win. It’s just much better than locks and condition variables for expressing concurrent programs.

Seibel: What if I don’t even want to allow for the possibility that someone comes in and looks for the 21st most-requested book and gets blocked? In the physical world you can imagine that when someone checks out a book we swap in a proxy for the book that the librarian then reorganizes and whenever a book comes back we put it back wherever the proxy is now. But you are modifying the library which seems, in an STM world, like it would cause the librarian to have to retry his whole transaction.

 
Peyton Jones: But there’s something that stayed the same—the key on the book is guaranteed not to change somehow, right? So there’s a number of ways you could do this. One is you could say, “What you do when you replace it with a proxy is you don’t modify the library at all”—that’s unchanged. What you do is you modify the book itself. And you don’t modify its key field—you only modify its value field, where it’s currently living. Now the index can be reorganized while the book is somewhere else. That’s cool—and you can express that perfectly naturally.

With STM, at the end the librarian looks through all the memory locations that he has read and sees if they contain now the same values that they did when he read them. So the locations that he has read will include the key field of the book because that determined where he put it. But he hasn’t read the contents of the book. So he’ll say, “Ah, this book—does this key field still contain 73; oh, yes it does.” 

But I don’t want to minimize the problem of starvation because it’s a bit insidious. You need good profiling tools that point you at transactions that are failing to commit because they keep getting bumped so that, rather than the program just silently not doing very much, you get some feedback about it. The same is true of a lock-based program. I hate it when those hourglasses appear.

Seibel: I guess in locked-based programs we’ve just learned to try hold locks for as short a duration as possible since that will give us the least contention.

Peyton Jones: Right. But, of course, then it’s harder to program. Finer-grained locking is tricky to get right. I think this is one of the huge wins of STM, is it gives you the fine granularity of very fine-grained locking along with very simple reasoning principles.

Here’s a reasoning principle that STM gives you that locks absolutely do not. I’ll establish my top-level invariants—I’ve got a bunch of bank accounts, the total sum of money in all the bank accounts added together is N. Money moves between bank accounts—that’s all. So there’s my invariant. Any transaction assumes that invariant at the beginning and restores it at the end. How do you reason that it does? We look at any one transaction that says, “Take three out of that one and put three into that one.” Good, 

 
invariant maintained. How is my reasoning in that done? Purely sequential reasoning. Once I’ve described some top-level invariants, I can reason completely sequentially about each transaction separately.

Seibel: Because you have transaction isolation.

Peyton Jones: Because they are put in isolation. So that’s really rather a powerful reasoning principle. Because it says you can use your sequential reasoning about imperative code despite the fact that the program’s concurrent. You’ve got to establish what those top-level invariants are, but that’s good for your soul, too. Because then you know what things you are trying to maintain. If you get an exception thrown in the middle of a transaction, that’s cool, too—that can’t destroy the invariants because the transaction is abandoned without effect. I think this is fabulous. Then reasoning about performance issues is a different level—you’ve guaranteed a certain sort of correctness; now you want to make sure you haven’t got any performance holes. Those are harder to get at—at the moment I don’t know anything better than profiling and directed feedback tools for doing that.

Seibel: It strikes me that while optimistic concurrency has been used from time to time in persistent databases, it’s never really gotten a foothold there compared to lock-based concurrency.

Peyton Jones: Of course STM can be implemented in all sorts of ways— optimistic concurrency is only one of them. You can lock as you go, which is more like a pessimistic concurrency model.

Seibel: But there’s also a reason that lock managers are the hairiest part of databases.

Peyton Jones: Right. So the thing about STM is you want to make sure that one person, or one team, gets to implement STM and everybody else gets to use it. You can pay them a lot of money and shut them in a small dark room for a year to try to make sure they do a really good job.

But then that work is usable by everybody through a very simple interface. That’s what I think is nice about it. What I want to avoid is having that level of expertise in everybody’s head. The example that I used at a talk I gavyesterday—this comes from Maurice Herlihy—is a double-ended queue: insert and delete elements.

A sequential implementation of a double-ended queue is a first-year undergraduate programming problem. For a concurrent implementation with a lock per node, it’s a research paper problem. That is too big a step. It’s absurd for something to be so hard. With transactional memory it’s an undergraduate problem again. You simply wrap “atomic” around the insert and delete operations—job done. That’s amazing, I think. It’s a qualitative difference. Now the people who implement the STM, they’d have to make sure they atomically commit a bunch of changes to memory as one. That’s not easy to do, just with compare and swaps. It can be done but you have to be careful about it.

And then if there are performance problems to do with starvation then you may need to do some application-level thinking about how to avoid that. But then you express the results of your application-level thinking, again using STM. I do think for that kind of program it’s a leap forward.

There was one other thing I wanted to mention—this goes back to functional programming. STM, of course, has nothing directly to do with functional programming at all. It’s really about mutating shared state—that doesn’t sound very functional.

But what happened is this, I went to a talk given by Tim Harris about STM in Java. I’d never heard about STM before; I just happened to go to his talk. He was describing an STM in which he had “atomic” but really not much else. You could implement these atomic transactions.

I said, “Wow, that seems really neat. Ah, so you need to log every side effect on memory. Every load and store instruction. Gosh, well there are a lot of those in Java.” But in Haskell there are practically none because they occur in this monadic setting. So loads and stores in Haskell are extremely explicit—programmers think of them as a big deal.

So I thought, “Oh, we should just try replicating this atomic memory stuff in Haskell because it would be a very cool feature to have.” And off we went—I talked to Tim about how to do this. Before long, because of the kind of framework that we had—this kind of pure, rather sparer frameworthat we had—we’d invented retry and orElse. Retry is this mechanism that allows you to do blocking within a transaction and orElse is the bit that allows you to do choice within a transaction. Neither of these are things that had occurred to him or his colleagues in developing transactional memory for Java because the rest of their context was rather more complicated.

So they hadn’t really thought much about blocking. Or maybe they just assumed that the way you do blocking was you say, atomically, “Only run this transaction when this predicate holds.” But that’s very noncompositional—supposing you wanted to get something out of one bank account and put it in another, well, what’s the condition that the transaction can run under? Answer: well, if there’s enough money in the first bank account and there’s enough space in the second—let’s say that they’re limited at both ends. So that’s a rather complicated condition to figure out. And it gets even more complicated if there’s a third bank account involved. It’s very noncompositional—you have to look inside the methods and pull all their preconditions out to the front.

That’s what he had and it kind of worked fine for small programs but clearly wasn’t very satisfactory. So in a Haskell context we came up with this retry, orElse thing which we’ve since transplanted back into the mainstream imperative context and they’re busy doing retry and orElse as well. That’s great.

Seibel: So there’s nothing actually inherent about Haskell that enabled that concept? It was just that you were able to think of it?

Peyton Jones: That’s right. There was less crap, basically, so the cool idea stood out in higher relief. It became more disgusting that there was no way to do blocking without losing the abstraction. That’s what led us to retry and orElse. I think a really good place for functional programming to be, or a role for it to play, is as a kind of laboratory in which to examine the beast. And then ideas can feed back. And this STM was a particularly clear example because there was a transition in both directions. Here there was a loop that actually got closed, which I thought was lovely.

Seibel: What’s your desert-island list of books for programmers?

 
Peyton Jones: Well, you should definitely read Jon Bentley’s Programming Pearls. Speaking of pearls, Brian Hayes has a lovely chapter in this book Beautiful Code entitled, “Writing Programs for ‘The Book’” where I think by “The Book” he means a program that will have eternal beauty. You’ve got two points and a third point and you have to find which side of the line between the two points this third point is on. And several solutions don’t work very well. But then there’s a very simple solution that just does it right.

Of course, Don Knuth’s series, The Art of Computer Programming. I don’t think it was ever anything I read straight through; it’s not that kind of book. I certainly referred to it a lot at one stage. Chris Okasaki’s book Purely Functional Data Structures. Fantastic. It’s like Arthur Norman’s course only spread out to a whole book. It’s about how you can do queues and lookup tables and heaps without any side effects but with good complexity bounds. Really, really nice book. Everyone should read this. It’s also quite short and accessible as well. Structure and Interpretation of Computer Programs. Abelson and Sussman. I loved that. And Compiling with Continuations, Andrew Appel’s book about how to compile a functional program using continuation passing style. Also wonderful.

Books that were important to me but I haven’t read for a long time: A Discipline of Programming by Dijkstra. Dijkstra is very careful about writing beautiful programs. These ones are completely imperative but they have the “Hoare property” of rather than having no obvious bugs they obviously have no bugs. And it gives very nice, elegant reasoning to reason about it. That’s a book that introduced me for the first time to reasoning about programs in a pretty watertight way. Another book that at the time made a huge impression on me was Per Brinch Hansen’s book about writing concurrent operating systems. I read it lots of times.

Seibel: Do you still program a lot?

Peyton Jones: Oh yes. I write some code every day. It’s not actually every day, but that’s my mantra. I think there’s this horrible danger that people who are any good at anything get promoted or become more important until they don’t get to do the thing they’re any good at anymore. So one of the things I like about working here and working in research generally is that I can still work on the compiler that I’ve been working on since 1990.

 
It’s a big piece of code and there are large chunks of it that I’m really the person who knows most about it.

How much code do I write? Some days I spend the whole day programming, actually staring at code. Other days, none. So maybe, on average, a couple hours a day, certainly. Programming is such fun. Why would you ever want not to do it? Furthermore it keeps you honest—it’s a good reality check to use your own compiler and to use the language that you advocate as well.

Seibel: And you still enjoy programming just as much as when you started?

Peyton Jones: Oh, yes, yes. That’s the most fun thing. I think most programmers have the feeling that “there must be a good way to do this.” One of the nice things about working in research is that instead of some manager standing over me saying, “This has to be done this week—just get it done,” I can sit and look at something and say, “There must be a right way to do this.” 

So I spend a lot of time refactoring and moving interfaces around and writing new types or even just rewriting a whole blob to try to make it right. GHC is pretty large—it’s not large by industrial standards; it’s large by functional programming standards—it’s about 80,000 lines of Haskell, maybe a bit more. And it’s long-lived—it’s 15 years old now. The fact that it’s still actively developed is indicative that chunks have got rewritten. There are no untouchable bits. So it’s both challenging and good fun to look at something and think, “What is the right way to do this?” And often I’ll hold off for weeks on something but I just can’t think of a nice way to do it. But that’s tantalizing. Because there has to be a nice way.

Seibel: In those weeks, what happens?

Peyton Jones: Oh, I’m thinking about it in the back of my mind. And sometimes I’ll have a go at it—I sort of run up the hill. And then I remember why it was so complicated and then usually some other displacement activity takes place. So sometimes I run up this hill several times. Sometimes I’m thinking about it in the background. And sometimes I think, “Well, time’s up—just got to do something now.” And maybe it’s not quite as beautiful as it could be.

 
Seibel: Is it the kind of thing that you wake up in the morning and you say, “Ah, I’ve got it!” Or is it that you decide to take another run at it and this time you get to the top of the hill?

Peyton Jones: It’s more like that. It’s seldom that I just having a blinding insight in the morning. Another thing that happens as a researcher is you have the opportunity to reflect on what you’ve done and write it up. So quite often if something interesting has happened I try to write a paper about it. So an example of that is there’s a paper called “The Secrets of the GHC Inliner,” which is really a very implementation-oriented paper that describes some implementation techniques that we developed for a particular part of GHC’s innards which we thought might be reusable for others. The chance that you have as an academic is to abstract from the code that, the fourth time around, you’ve finally kicked into a shape that feels good, and write about it so other people can reuse that same technique.

Seibel: What is programming to you? Do you think of yourself as a scientist or an engineer or a craftsman? Or something else entirely?

Peyton Jones: Have you read Fred Brooks’s paper about this, the one called, “The Computer Scientist as Toolsmith”? I reread it recently. It’s very nice. I think it’s good to remember that we’re concerned with building things. I think that’s why programming is so interesting.

At the same time I’m really keen on trying to extract principles of enduring value. I have a paper about how to write a good paper or give a good research talk and one of the high-order bits is, don’t describe an artifact. An artifact is an implementation of an idea. What is the idea, the reusable brain-thing that you’re trying to transfer into the minds of your listeners? There’s something that’s useful to them. It’s the business of academics, I think, to abstract reusable ideas from concrete artifacts. Now that’s still not science in the sense of discovering laws. But it is a kind of abstraction into reusable thought-stuff out of the morass of real life that I think is very important.

Seibel: So what about engineering vs. craft. Should we expect to be like the guys who build bridges where, for the most part, bridges don’t fall down? Or are we really more like the guys making pottery—except the pottery ijust incredibly complex—where all you can do is apprentice yourself to someone and learn from them how they do it?

Peyton Jones: It’s a bit of a false dichotomy. It’s not truly an either-or choice. One thing that is hard, even for professional software engineers and developers, is to viscerally grok the size of the artifacts on which we work. You’re looking at the Empire State Building through a 1-foot-square porthole, so it’s difficult to have a real feel for how gigantic the structure you’re looking at is. And how it’s interconnected.

How big is GHC? I don’t have a feel for that in the same sense I have a feel for how big this building is. So I don’t think we’re anywhere near where the engineers are with building bridges. Their design patterns have now been boiled down to where they can pretty much be sure that the bridge isn’t going to fall down. We’re nowhere near that with software. But I don’t think that that’s a reason for saying we just shouldn’t worry about it at all.

In fact I think it’s somewhere where functional programming has a lot to offer. Because I think fundamentally it enables you to build more robust structures. Structures that are easier to comprehend and test and reason about. And here is something that I think functional programmers are lagging on: we talk about reasoning about functional programs but we don’t do it very much. I’d like to see much more by way of tools that understand Haskell programs and formally reason about them and give you guarantees beyond their types. We stand on a higher platform and we should be able to go further.

So that’s about saying the material should become more robust. The more robust your materials, the less you need to concentrate on the minutia instead of the larger-scale structures. Of course that will just make us more ambitious to build larger structures until we get to the point where they fall apart again.

I think that’s sort of an invariant. As soon as you can do it, you stretch to the point where you can’t do it anymore. I suppose I don’t really see it as, is it this or is it that? There will always be a strong crafty element, I think, just because we’ll stretch our ambition. In the case of engineering structures, there are physical limits on how far you can stretch. Nobody’s going to build a bridge that traverses the Atlantic any time soon. And that reallmight fall down if you built it. But that’s not the reason people won’t build it—it’s just because it’d be too expensive. Whereas nowadays, with software, once you can build bridges over the Channel pretty quickly and cheaply, well then, that becomes a done deal and we now think that’s pretty cheap so we’ll now try the Atlantic. And now it falls apart again.

Seibel: Guy Steele was saying how Moore’s Law has been true for his whole career and he suspects it won’t be true for his son’s whole career and was speculating a bit about what that’s going to do to programming. I wonder will we eventually have to stop just saying, “If we can build a bridge over the Channel, we can build one over the Atlantic”?

Peyton Jones: No, no. Software’s different I think. Because if you write software that’s ten times as big that doesn’t mean you have to run it on a computer that’s ten times as fast. The program counter spends its time in a small portion of the code. Ninety percent of its time is spent in ten percent of the code or something. So the parts that are performance critical may be a relatively small part of the program.

It’s true that what tends to happen is you slap abstraction on abstraction on abstraction and before you know it pressing a single button on the screen a great number of things happen all the way down the chain before you finally get to some registers being moved.

So we may have to work on ways of collapsing out those layers by sophisticated compiler transformations so not so much happens. The abstraction boundary may be useful for people but machines don’t care. So I don’t think just because we may reach the boundaries of what computers can do that necessarily software will immediately halt from getting more complicated. Because by that time they’ll be pretty fast anyway. I think the primary limitation on software is not the speed of computers but our ability to get our heads around what it’s supposed to do.

Seibel: What do you enjoy about programming?

Peyton Jones: For me, part of what makes programming fun is trying to write programs that have an intellectual integrity to them. You can go on slapping mud on the side of a program and it just kind of makes it work for a long time but it’s not very satisfying. So I think a good attribute of a gooprogrammer, is they try to find a beautiful solution. Not everybody has the luxury of being able to not get the job done today because they can’t think of a beautiful way to do it.

But I really think it’s a funny medium because it’s so malleable. You can do virtually anything with it. But that means you can build ugly things as well as beautiful things and things that will be completely unmaintainable and undurable. I sometimes feel a bit afraid about the commercial world with, on the one hand, the imperatives of getting it done because the customer needs it next week and, on the other hand, the sheer breadth rather than depth of the systems that we build.

Systems are filled with so much goop—in order to build an ASP.NET web service-y thing you need to know about this API and this tool and you need to write in three different languages and you need to know about Silverlight and LINQ and you can go on doing acronyms forever. And each of them has a fat book that describes it.

This is a tension I don’t know how to resolve. These are useful systems— they’re not designed by accident. Each of them is there for a reason and each of them has a smart person who’s thinking hard about how this thing should be architected. But nevertheless, each, individually, has a broad interface. It may or may not be deep but it’s certainly broad. There’s a lot of stuff you need to just have in your head. It’s like learning a language—a human language—there’s a large vocabulary.

For me, that’s no fun. I never learned my multiplication tables. I always worked them out from first principles every time and I just developed enough tricks that I could do it quickly enough. When you do seven nines I still have to go, oh, seven nines, oh, seven tens and subtract, so it’s sixty-three. Whereas other people just learnt them. And that’s a relatively small thing. So I hate things were you just have to learn these big things. So instinctively I back away from these big goopy things. But at the same time I acknowledge that they’re useful and important in practice. The question in my mind is, if you were able to take a bit longer to design some of these things, could they be designed with smaller, less complicated, and less ad hoc interfaces?

 
Seibel: Sometimes it seems that it’s exactly because each of these blobs has some smart person or people working on it and each smart person wants their own little playground to play in, that things get so complicated.

Peyton Jones: I’m sure there’s an element of that. But to put a more positive construction on it, if you like, it’s a big, complicated world and there’s a lot to get done. If you had a grand Olympian vision—if you had a very large brain and enormous throughput—you might be able to do something with less overlap and more overall coherence.

But in practice we have to factor these problems into little chunks. And then the little chunks each have somebody who looks after it and who’s conditioned by the things they’ve done before and their heritage. So maybe they design something within that space that may not be as good as it could possibly be—they’re pressed for time. And certainly by the time you look at the combination of everything it’s maybe quite a lot less good than it could possibly be. And then before you know it you’re locked into a legacy problem—that’s another reason that things are not as good as they could possibly be.

So there’s a tremendous legacy ball and chain that’s being dragged around. It’s one of the nice things about Haskell. When I gave a retrospective on Haskell at, I think it was POPL 2004 or something, I put up a slide that said one of the things we’ve learned to do in Haskell is to “avoid success at all costs.” This is clearly a sort of meme because people remember that phrase and they quote it back to me.

It has a grain of truth in it because it means by not being too successful, too early, we’ve been able to morph Haskell quite a lot during its life. And part of the reason that I’m feeling a bit manic at the moment is because Haskell has become more successful and so I get more bug reports, more feature requests. And more people saying, “Don’t break my program please.” That didn’t use to happen.

Seibel: You’ve mentioned writing beautiful code a couple of times. What are the characteristics of beautiful code?

Peyton Jones: Tony Hoare has this wonderful turn of phrase in which he says your code should obviously have no bugs rather than having no obvioubugs. So for me I suppose beautiful code is code that is obviously right. It’s kind of limpidly transparent.

Seibel: What about those little jewels of code that you almost have to puzzle out how they work but once you do, it’s amazing. Are those also beautiful?

Peyton Jones: Sometimes to say that it’s obviously right doesn’t mean that you can see that it’s right without any mental scaffolding. It may be that you need to be told an insight to figure out why it’s right. If you look at the code for an AVL tree, if you didn’t know what it was trying to achieve, you really wouldn’t have a clue why those rotations were taking place. But once you know the invariant that it’s maintaining, you can see, ah, if we maintain that invariant then we’ll get log lookup time. And then you look at each line of code and you say, “Ah, yes, it maintains the invariant.” So the invariant is the thing that gave you the insight to say, “Oh, it’s obviously right.” 

I agree completely that just looking at the bare code may not be enough. And it’s not a characteristic, I think, of beautiful code, that you should be able to just look at the bare code and see why it’s right. You may need to be told why. But after you have that, now with that viewpoint, that invariant, that understanding of what’s going on, you can see, oh yeah, that’s right.

Seibel: Does that put an upper bound on how big a piece of software can be and still be beautiful?

Peyton Jones: I don’t know if it’s a bound on its size. The insights that you need in order to reassure yourself that it’s right, or at least right-ish, are along the lines of being more confident that it’s correct. Any really, really big piece of software is bound to have shortcomings or indeed outright things that you just know are wrong with it. But it’s not economic to fix them at the moment. It’s certainly true of GHC and it’s definitely true of Microsoft’s software.

But what makes big software manageable is having some global invariants or big-picture statements about what it’s supposed to do and what things are supposed to be true. So, to take GHC as another example, having this invariant that each of these intermediate programs should be well typed.

 
That can be checked, actually, at runtime if you like. That’s quite a powerful invariant about what’s going on. So I’m not sure it’s really necessarily to do with size.

Certainly interconnectedness makes big programs eventually crumble under their own weight. Sometimes one of the luxuries that you get from working in research is that you can sometimes take a chunk of code and simply rewrite it in the light of your improved insights into what you were trying to achieve and how you might try to achieve it. We talked about this business of refactoring GHC’s back end. If I was working in a more commercial setting, I might not be able to afford to do that. But I’m hoping that it will make GHC more maintainable and understandable in the long term.

Is there an upper bound on the size? I don’t know. I rather suspect that as long as we can go on building good abstractions we can keep building bridges across the Atlantic. We have software that works—not perfectly, but surprisingly well considering how big it is.

Seibel: So the question is, can you build an edifice that’s that large, and works, and is also beautiful.

Peyton Jones: It’s hard for it to maintain its beauty. Bits are often beautiful or at least acceptably non-ugly when they’re first built. In the face of protracted life—maintenance—it’s quite difficult to maintain that. That’s the worst thing about long-lived programs . . . that they gradually become ugly. So there’s no moment at which they become disfigured but nevertheless after a while they just become crappy.

Seibel: And is the only way out to say, “OK, this thing has lived long enough, start over”?

Peyton Jones: I think that eventually you have to reengineer chunks of it. And if you can afford to reengineer a bit as you go along, then—if you don’t do anything for ten years then the result may just be so daunting that you think, “I just have to throw it away and start again.” If you can afford to reengineer a bit as you go along, like the human cells regenerating themselves—that’s what I hope is happening to GHC.

 
The most depressing thing about life as a programmer, I think, is if you’re faced with a chunk of code that either someone else wrote or, worse still, you wrote yourself but you no longer dare to modify. That’s depressing.
