dependencies
	we use ==comet_ml== to track iteration, records individual runs
	torch
		torch.optim -> optimizing/ tuning current paramaters
		simplify gradient steps with 
			loss.backward() -> gradietn calc
			optimizer.step() -> take step base on intial step size
	mitdeeplearning (bc we r folling  mit course)
	import numpy as np
	import os
		interaction with operation system
	import time
		manage time related like start time or pause stuff
	import functools
		utilities for working with functions
	from IPython import display as ipythondisplay
		allow jyupter to display things like images audio html...
	from tqdm import tqdm
		create a progress bar for loops
		ex: for i in tqdm(range(1000)): provide a bar on progress
	from scipy.io.wavfile import write
		help save audio files

vectorizing
	create dict that is capable of text-> number and number -> text
	jumbo all the training data together & convert each uniques symbol to array of number
	``
	regrouping and train with random position at a fixed length
	we could then use rnn to predict the next letter every time


==rnn model
==
==
we first need to embed the numbers so 531dont mean 3 times of  17
			use embedding = nn.Embedding(4,3)
				means we have 4 possible char, want each char to be represented by a vector of 3 number 
				``
we then use lstn instead of rnn 
	this will allow use to escape exploding/vanishing gradient by using different path for long term and working memories
	more here [[ALG - LSTM]]