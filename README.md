# HighlyCompositeNumber
#This code was written when I was first learning python.  Hence why it is so ugly.

I found a free course, that posted daily challenges.  Most of them where data formatting but they also posted mathematical problems.
The challenge was to find highly composite numbers.  Your program would need to find the number with the most composites up to a given number, in a given time.
My first try I use a simple dividing algorithm, which failed on time.  My next few failed on logic.  So I want back to the drawing board, read a little about Srinivasa Ramanujan, and taught myself a little bit about number theory. 

This algorithm uses prime factors to basally brute force the problem.  To make the brute force approach faster rules are added in.  An example of this, you will never have more factors of 5 then you will have of factors of 3, nor will you have more factors of 3 then you will have factors of 2.

Originally this code read from a text file and out put to a text file.
