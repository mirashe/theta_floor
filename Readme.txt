Description:
	You might have heard about "Mills' constant" in number theory:
		https://en.wikipedia.org/wiki/Mills%27_constant

	Here we played with a similar concept:
	We "assumed" there is a number we call it theta,
	defined as the smallest positive real number θ such that
	the floor function of every natural powers of it is a prime number.

	It means [θ^n] for every natural number n is a prime number.

	In this project we are trying to find the minimum possible amount of it.

Usage:
	To run the project it is enough to run the find_theta_floor.py file.
	To test the prime operation just run tests_and_checks.py file.

Output:
	After running the app for hours and growing the primes file to 1.12 GB,
	this was the last output:

	----------------------------------------------------
	Check index: 810
	Theta value: 17.53695387737836288733855530
	Theta form: 4,563,650,703,502,319,197 ^ 1/15
	Biggest worked power: 15
	Last number (failed): 80,032,531,899,785,490,177
	Failed power: 16
	Max prime: 2,158,957,777
	Max distance: 292
	Primes count: 105,631,417
	----------------------------------------------------
