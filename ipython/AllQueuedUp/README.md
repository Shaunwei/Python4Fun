Programming Challenge - All Queued Up
Write a program that simulates a number of people waiting line. The input will be a text file that contains the instructions "add " "next" and "remove "

add [name] -- place the specified person at the end of the line
next -- remove the first person in line from the line (this name is printed to the output)
remove [name] -- remove the specified person from wherever they are in the line
Assume that there will never be any duplicate names. All operations should perform in less than than O(n) time.

Use any language you choose. Focus on efficiency and readability. Use any library methods you choose, but be aware of the runtime of methods that you use.

Your submission should contain (preferably zipped together) source files, any special instructions needed to run, and a sample run of your program

//Email the solution, a resume, and any supplemental material to software_jobs@atypon.com.

Testing files: sample.txt, testing.txt, stresstest.txt

Combined zip file: AllQueuedUp.zip

Here is an example file:

        add amy
        add bill
        add zoe
        next
        remove bill
        next
        add james
        next
        add mary
        add jill
        add bob
        next
        add rob
        remove bob
        next
        next
        
The output of the program using this file should be:

        amy
        zoe
        james
        mary
        jill
        rob