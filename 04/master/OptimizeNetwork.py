import GeneticFunctions
import numpy as np
import random
class OptimizeNetwork (GeneticFunctions.GeneticFunctions):
	def __init__(self, limit=500,  prob_crossover=0.9, prob_mutation=0.2,scale_mutation=0.33333):
	#	self.D = D
		self.counter = 0
		self.limit = limit
	#	self.size = size
		self.prob_crossover = prob_crossover
		self.prob_mutation = prob_mutation
		self.scale_mutation = scale_mutation
		self.best = ( [],np.inf,0) #Add in class diagrams
		self.fits_pops=None

	def probability_crossover(self):
		return self.prob_crossover

	def probability_mutation(self):
		return self.prob_mutation

	def crossover(self, parents):
		father, mother = parents
		

		alpha = random.uniform(0,1)
		child1 = alpha*father+(1-alpha)*mother
		child2 = alpha*mother+(1-alpha)*father		
		return (child1, child2)

	def selection(self,popul):
		if not len(popul.fits_pops):
			popul.set_fitness()
		ranks = sorted(popul.fits_pops, reverse = True)
		rank_array = []
		for i in range(len(ranks)):
			for x in range(i+1):
				rank_array.append(ranks[i][1])

		father = rank_array[random.randint(0, len(rank_array)-1)]
		mother = rank_array[random.randint(0, len(rank_array)-1)]
		return (father, mother)

	def mutation(self, chromosome):
		mutated = chromosome
		for x in range(len(chromosome)):
			if np.random.random() < self.prob_mutation:
				vary = np.random.normal()*self.scale_mutation
				mutated[x] += vary
		return mutated
	
	def terminate(self,popul):
		self.counter += 1

		#f = sorted(fits_populations, reverse = True)
		f=popul.get_best()# a tuple with first being x and second being fitness
		if f[1] < self.best[1]:
			self.best = (f[0],f[1],popul.net.hid_nodes)



		if self.counter < 300:
			self.prob_mutation = 0.2
		else:
			self.prob_mutation = 0.02

		if self.counter % 10 == 0:  
			#fits = [f for f, ch in fits_populations]
			best = f[1]
			ave = popul.get_average()
			print(
				"[G %3d] score=(%.4f, %.4f)" %
				(self.counter, best, ave))

		if self.counter >= self.limit:
			#print("Best fitness achieved: " + str(self.best))
			#print(type(self.best[1]))
			print(popul.net.test(hid_nodes,self.best[0]))
			return True
		return False
	def run(self,popul):

		while not terminate(self,popul):
			lis=[]
			for i in range(popul.size//2):
				parent_tup=selection(self,popul)
				newborn_tup=crossover(self,parent_tup)
				child1=mutation(self,newborn_tup[0])
				child2=mutation(self,newborn_tup[1])
				lis.append(child1)
				lis.append(child2)
			popul.set_list_chromo(np.array(lis))

def main():
	on=OptimizeNetwork()
	parents=(np.array([1,2,3,4]),np.array([5,6,7,8]))
	print(on.crossover(parents))
	print(on.mutation(parents[0].astype(float)))
if __name__=="__main__":
	main()