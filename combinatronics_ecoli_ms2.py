import itertools

f=open('Ecoli_evenchains_ms2.csv', 'w')

onePosition = [61.9558, -18.0106]
disaccharidePosition = [872.5011]
fourPrimePosition = [61.9558, -18.0106]

twoBPosition = [237.2218, -18.0106]
twoPrimeBPosition = [182.1671, -18.0106]

threePosition = [226.1932, -18.0106, 0.0, 208.1827]
threePrimeAndThreePrimeBPosition = [436.3916, -18.0106, 0.0, 208.1827]

f.write('One, Disaccharide, FourPrime, TwoB, TwoPrimeB, Three, ThreePrimeAndThreePrimeB, Total\n')

for one, disacch, fourprime, twob, twoprimeb, three, threeprimeandthreeprimeb, in itertools.product(onePosition, disaccharidePosition, fourPrimePosition, twoBPosition, twoPrimeBPosition, threePosition, threePrimeAndThreePrimeBPosition):
	#print onepp, op, dp, threep, threepp, twobp, threebpp, twobp
	total = one + disacch + fourprime + twob + twoprimeb + three + threeprimeandthreeprimeb
	f.write("%s, %s, %s, %s, %s, %s, %s, %s \n" % (one, disacch, fourprime, twob, twoprimeb, three, threeprimeandthreeprimeb, total))
f.close()