import itertools

f=open('Ecoli_evenchains_ms1.csv', 'w')

onePosition = [79.9663, 143.9377, 0.0]
disaccharidePosition = [680.4095, 736.4721, 792.5347, 848.5973, 904.6599, 960.7225, 1016.7851]
fourPrimePosition = [79.9663, 143.9377, 0.0]

twoBPosition = [0.0, 238.2296]
twoPrimeBPosition = [0.0, 154.1358, 182.1671, 210.1984, 238.2297, 266.2610, 294.2923]

threePosition = [0.0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184]
threePrimePosition = [0.0, 170.1306, 198.1619, 226.1932, 254.2245, 282.2558, 310.2871, 338.3184, 226.1933]
threePrimeBPosition = [0.0, 154.1358, 182.1671, 210.1984, 238.2297, 266.2610, 294.2923]


f.write('One, Disaccharide, FourPrime, TwoB, TwoPrimeB, Three, ThreePrime, ThreePrimeB, Total\n')

for one, disacch, fourprime, twob, twoprimeb, three, threeprime, threeprimeb in itertools.product(onePosition, disaccharidePosition, fourPrimePosition, twoBPosition, twoPrimeBPosition, threePosition, threePrimePosition, threePrimeBPosition):
	#print onepp, op, dp, threep, threepp, twobp, threebpp, twobp
	total = one + disacch + fourprime + twob + twoprimeb + three + threeprime + threeprimeb - 1.0078
	f.write("%s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (one, disacch, fourprime, twob, twoprimeb, three, threeprime, threeprimeb, total))
f.close()