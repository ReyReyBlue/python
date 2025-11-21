# Koosta tõeväärtustabel kahele avaldisele
# A AND (B OR C)
# (A ~ B) OR NOT(C AND A)

#				alamavaldis			alamavaldised			
#   A	B	C		B OR C	A AND (B OR C)		A ~ B	C AND A	    NOT(C AND A)	(A ~ B) OR NOT(C AND A)
#   0	0	0		    0	    0	        	1	        0	        1	            1
#   0	0	1		    1	    0		        1	        0	        1	            1
#   0	1	0		    1	    0		        0	        0	        1	            1
#   0	1	1		    1	    0		        0	        0	        1	            1
#   1	0	0		    0	    0		        0	        0	        1	            1
#   1	0	1		    1	    1		        0	        1	        0	            0
#   1	1	0		    1	    1		        1	        0	        1	            1
#   1	1	1		    1	    1		        1	        1	        0	            1