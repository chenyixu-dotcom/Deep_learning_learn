lstm instead of vanilla rnn
	lstm helps solve the exploding graident/ vanishing gradient
	use different path for long/short term memory
		in rnn, we calculate h with tanh(z)
		in lstm
			we use sigmoid activation function
			tanh give -1 , 1 outputs while sigmoid is 0,1
			sigmoid is more path or go/ activation energy while tanh is transformation matrix
		``
	we use cell state to track long term memories
		we can modify the long term memories with multiplications and addtions but we cant modify it with weight and biases directly
		this will make sure hte ltm's gradient wont explode or vanish
	and hidden states for working memories
		which is controlled directly by weight and biases	
		the current short term memory determine how much of the long term memory to keep
			the ==forget gate== -> terminology for this section of lstm
				determin what will be forget
		while adding the constant, we use the input to calculate teh potential long term memory and also to calculate the percent of that ltm to add to the existing ltm
			we use tanh when calculating potential ltm 
			we use the sigmoid function to spit a value between 0,1 to give a percentage on how much p ltm to keep
		``
			this provess is called the ==input gate==( the percentage)
				the potential here is called ==candidate memory==
				determine update toward the ltm
				note that input gate and candidate mem are element wise multiplication not dot
				``
		the last stage of calculating the lstm is updating the stm
			we plug the final forget gate output * ltm + input gate into tanh function to return a potential short term memory
			 we then use the stm to determine how much of the new potential stm to remember
			 this stage is called the ==output gate==
				 we use stm to determine percentage stm to remember and ltm to decide potential stm 
				 we use the new calculate stm and throw away the old one
			 we use the result of the output gate ot(percentage) to find ht( the new short term mem) ->
				stm =  ot dot product tanh( ct) 
		notice now out model have a lot more weights
			forget weight gate, input gate potential, input gate percentage, output gate
			to calculate loss, we use ht -> the new short term memory with its calculated weight and biases to find the final result/loss
				we take backward of the loss and update all of the weight like that
		
				