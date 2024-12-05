#!/usr/bin/env python
# coding: utf-8

# ## AAC project

# In[1]:


from utils.input_generator_util import InputGeneratorUtil
from utils.testing_util import TestingUtil
from algorithms.graph_size import GraphSizeCalculator
from utils.input_parser_util import InputParserUtil
from algorithms.distance_between_graphs import GraphDistanceCalculator
from algorithms.cycles import find_all_cycles, approximate_max_cycles, normalize_cycle
from algorithms.hamiltonian_cycles_min_extension import min_num_hamiltonian_extension_exact, min_num_hamiltonian_extension_approx
from algorithms.hamiltonian_cycles_number import count_hamiltonian_cycles_backtrack,count_hamiltonian_cycles_randomized_biased,count_hamiltonian_cycles_genetic


# ### General utils initialisation

# In[2]:


inputGeneratorUtil =  InputGeneratorUtil()
inputParserUtil = InputParserUtil()


# ## 3.1 Finding the Size of the Graph

# #### Data preparation

# In[3]:


is_3x3_directed, graph_3x3 = inputGeneratorUtil.generate_random_graph(3)
graph_3x3_parsed = inputParserUtil.parse_single_graph(graph_3x3)

is_10x10_directed, graph_10x10 = inputGeneratorUtil.generate_random_graph(10)
graph_10x10_parsed = inputParserUtil.parse_single_graph(graph_10x10)


is_100x100_directed, graph_100x100 = inputGeneratorUtil.generate_random_graph(100)
graph_100x100_parsed = inputParserUtil.parse_single_graph(graph_100x100)


# #### Testing utils preparation

# In[4]:


graphSizeTestingUtil = TestingUtil(GraphSizeCalculator.graph_size)


# #### Testing different inputs

# In[5]:


graphSizeTestingUtil.run_test((graph_3x3_parsed['adjacency_matrix'],graph_3x3_parsed['is_directed']), "Finding the Size of the Graph - 3x3 graph")
graphSizeTestingUtil.run_test((graph_10x10_parsed['adjacency_matrix'],graph_10x10_parsed['is_directed']), "Finding the Size of the Graph - 10x10 graph")
graphSizeTestingUtil.run_test((graph_100x100_parsed['adjacency_matrix'],graph_100x100_parsed['is_directed']), "Finding the Size of the Graph - 100x100 graph")


# ## 3.2 Finding the Distance Between Two Graphs

# #### Data preparation

# In[6]:


is_a_3x3_directed, graph_a_3x3 = inputGeneratorUtil.generate_random_graph(3,False)
graph_a_3x3_parsed = inputParserUtil.parse_single_graph(graph_a_3x3)
is_b_3x3_directed, graph_b_3x3 = inputGeneratorUtil.generate_random_graph(3,False)
graph_b_3x3_parsed = inputParserUtil.parse_single_graph(graph_b_3x3)

is_a_10x10_directed, graph_a_10x10 = inputGeneratorUtil.generate_random_graph(10,False)
graph_a_10x10_parsed = inputParserUtil.parse_single_graph(graph_a_10x10)
is_b_10x10_directed, graph_b_10x10 = inputGeneratorUtil.generate_random_graph(10,False)
graph_b_10x10_parsed = inputParserUtil.parse_single_graph(graph_b_10x10)

is_a_100x100_directed, graph_a_100x100 = inputGeneratorUtil.generate_random_graph(100,False)
graph_a_100x100_parsed = inputParserUtil.parse_single_graph(graph_a_100x100)
is_b_100x100_directed, graph_b_100x100= inputGeneratorUtil.generate_random_graph(100,False)
graph_b_100x100_parsed = inputParserUtil.parse_single_graph(graph_b_100x100)


# #### Testing utils preparation

# In[7]:


graphDistanceCalculator = GraphDistanceCalculator(is_directed=False)
graphDistanceTestingUtil = TestingUtil(graphDistanceCalculator.calculate_distance)


# #### Testing different inputs

# In[8]:


graphDistanceTestingUtil.run_test((graph_a_3x3_parsed['adjacency_matrix'],graph_b_3x3_parsed['adjacency_matrix']), "Finding the Distance Between Two Graphs - 3x3 graph")
graphDistanceTestingUtil.run_test((graph_a_10x10_parsed['adjacency_matrix'],graph_b_10x10_parsed['adjacency_matrix']), "Finding the Distance Between Two Graphs - 10x10 graph")
graphDistanceTestingUtil.run_test((graph_a_100x100_parsed['adjacency_matrix'],graph_b_100x100_parsed['adjacency_matrix']), "Finding the Distance Between Two Graphs - 100x100 graph")


# ## 3.3 Finding the Max Cycle in the Graph

# #### Data preparation

# In[9]:


is_3x3_directed, graph_3x3 = inputGeneratorUtil.generate_random_graph(3)
graph_3x3_parsed = inputParserUtil.parse_single_graph(graph_3x3)

is_7x7_directed, graph_7x7 = inputGeneratorUtil.generate_random_graph(7)
graph_7x7_parsed = inputParserUtil.parse_single_graph(graph_7x7)

is_10x10_directed, graph_10x10 = inputGeneratorUtil.generate_random_graph(10)
graph_10x10_parsed = inputParserUtil.parse_single_graph(graph_10x10)

is_20x20_directed, graph_20x20 = inputGeneratorUtil.generate_random_graph(20) #approximation only
graph_20x20_parsed = inputParserUtil.parse_single_graph(graph_20x20)

is_100x100_directed, graph_100x100 = inputGeneratorUtil.generate_random_graph(100) #approximation only
graph_100x100_parsed = inputParserUtil.parse_single_graph(graph_100x100)


# #### Testing utils preparation

# In[10]:


allCyclesTestingUtil = TestingUtil(find_all_cycles)
approxCyclesTestingUtil = TestingUtil(approximate_max_cycles)


# ### 3.3.1 Finding the Max Cycle in the Graph - Exact Algorithm

# #### Testing different inputs

# In[11]:


allCyclesTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed']}, "Finding the Max Cycle in the Graph - Exact Algorithm - 3x3 graph")
allCyclesTestingUtil.run_test({"adjacency_matrix":graph_7x7_parsed['adjacency_matrix'],"is_directed":graph_7x7_parsed['is_directed']}, "Finding the Max Cycle in the Graph - Exact Algorithm - 7x7 graph")
allCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed']}, "Finding the Max Cycle in the Graph - Exact Algorithm - 10x10 graph")


# ### 3.3.2 Finding the Max Cycle in the Graph - Polynomial Time Approximation

# #### Testing different inputs - 1000 iterations

# In[12]:


approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed'],"iterations":1000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 3x3 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_7x7_parsed['adjacency_matrix'],"is_directed":graph_7x7_parsed['is_directed'],"iterations":1000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 7x7 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"iterations":1000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 10x10 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_20x20_parsed['is_directed'],"iterations":1000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 20x20 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_100x100_parsed['is_directed'],"iterations":1000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 100x100 graph")


# #### Testing different inputs - 5000 iterations

# In[13]:


approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed'],"iterations":5000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 3x3 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_7x7_parsed['adjacency_matrix'],"is_directed":graph_7x7_parsed['is_directed'],"iterations":5000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 7x7 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"iterations":5000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 10x10 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_20x20_parsed['is_directed'],"iterations":5000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 20x20 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_100x100_parsed['is_directed'],"iterations":5000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 100x100 graph")


# #### Testing different inputs - 10000 iterations

# In[14]:


approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed'],"iterations":10000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 3x3 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_7x7_parsed['adjacency_matrix'],"is_directed":graph_7x7_parsed['is_directed'],"iterations":10000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 7x7 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"iterations":10000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 10x10 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_20x20_parsed['is_directed'],"iterations":10000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 20x20 graph")
approxCyclesTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_100x100_parsed['is_directed'],"iterations":10000}, "Finding the Max Cycle in the Graph - Polynomial Time Approximation - 100x100 graph")


# ## 3.4 Finding the Minimum Extension to Achieve Hamiltonian Graph

# #### Data preparation

# In[15]:


is_3x3_directed, graph_3x3 = inputGeneratorUtil.generate_random_graph(3)
graph_3x3_parsed = inputParserUtil.parse_single_graph(graph_3x3)

is_6x6_directed, graph_6x6 = inputGeneratorUtil.generate_random_graph(6)
graph_6x6_parsed = inputParserUtil.parse_single_graph(graph_6x6)

is_10x10_directed, graph_10x10 = inputGeneratorUtil.generate_random_graph(10)
graph_10x10_parsed = inputParserUtil.parse_single_graph(graph_10x10)


# #### Testing utils preparation

# In[16]:


minNumExtensionExactTestingUtil = TestingUtil(min_num_hamiltonian_extension_exact)
minNumExtensionAproxTestingUtil = TestingUtil(min_num_hamiltonian_extension_approx)


# In[17]:


graph_6x6_parsed['adjacency_matrix']


# ### 3.4.1 Finding the Minimum Extension to Achieve Hamiltonian Graph - Exact Algorithm

# #### Testing different inputs

# In[18]:


minNumExtensionExactTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed']}, "Finding the Min Number of Hamiltonian Extension - Exact Algorithm - 3x3 graph")
minNumExtensionExactTestingUtil.run_test({"adjacency_matrix":graph_6x6_parsed['adjacency_matrix'],"is_directed":graph_6x6_parsed['is_directed']}, "Finding the Min Number of Hamiltonian Extension - Exact Algorithm - 6x6 graph")
minNumExtensionExactTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed']}, "Finding the Min Number of Hamiltonian Extension - Exact Algorithm - 10x10 graph")


# ### 3.4.2 Finding the Minimum Extension to Achieve Hamiltonian Graph - Polynomial Time Approach

# #### Testing different inputs

# In[19]:


minNumExtensionAproxTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed'],"iterations":1000}, "Finding the Min Number of Hamiltonian Extension - Polynomial Time Approximation - 3x3 graph")
minNumExtensionAproxTestingUtil.run_test({"adjacency_matrix":graph_6x6_parsed['adjacency_matrix'],"is_directed":graph_6x6_parsed['is_directed'],"iterations":1000}, "Finding the Min Number of Hamiltonian Extension - Polynomial Time Approximation - 6x6 graph")
minNumExtensionAproxTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"iterations":1000}, "Finding the Min Number of Hamiltonian Extension - Polynomial Time Approximation - 10x10 graph")


# ## 3.5 Finding All Hamiltonian Cycles

# #### Data preparation

# In[20]:


is_3x3_directed, graph_3x3 = inputGeneratorUtil.generate_random_graph(3)
graph_3x3_parsed = inputParserUtil.parse_single_graph(graph_3x3)

is_6x6_directed, graph_6x6 = inputGeneratorUtil.generate_random_graph(6)
graph_6x6_parsed = inputParserUtil.parse_single_graph(graph_6x6)

is_10x10_directed, graph_10x10 = inputGeneratorUtil.generate_random_graph(10)
graph_10x10_parsed = inputParserUtil.parse_single_graph(graph_10x10)

is_15x15_directed, graph_15x15 = inputGeneratorUtil.generate_random_graph(15)
graph_15x15_parsed = inputParserUtil.parse_single_graph(graph_15x15)


# #### Testing utils preparation

# In[21]:


# exact
countHamiltinianCyclesBacktrackTestingUtil = TestingUtil(count_hamiltonian_cycles_backtrack)
# polynomial approximation
countHamiltinianCyclesRandomizedBiasedTestingUtil = TestingUtil(count_hamiltonian_cycles_randomized_biased)
countHamiltinianCyclesGeneticTestingUtil = TestingUtil(count_hamiltonian_cycles_genetic)


# ### 3.5.1 Finding All Hamiltonian Cycles - Exact Algorithm

# #### Testing different inputs

# In[22]:


countHamiltinianCyclesBacktrackTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed']}, "Finding All Hamiltonian Cycles - Exact Algorithm - 3x3 graph")
countHamiltinianCyclesBacktrackTestingUtil.run_test({"adjacency_matrix":graph_6x6_parsed['adjacency_matrix'],"is_directed":graph_6x6_parsed['is_directed']}, "Finding All Hamiltonian Cycles - Exact Algorithm - 6x6 graph")
countHamiltinianCyclesBacktrackTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed']}, "Finding All Hamiltonian Cycles - Exact Algorithm - 10x10 graph")


# ### 3.5.2 Finding All Hamiltonian Cycles - Polynomial Time Approach

# #### Testing different inputs - randomized biased testing

# In[23]:


countHamiltinianCyclesRandomizedBiasedTestingUtil.run_test({"adjacency_matrix":graph_3x3_parsed['adjacency_matrix'],"is_directed":graph_3x3_parsed['is_directed'],"iterations":1000}, "Finding All Hamiltonian Cycles - Polynomial Time Approximation - 3x3 graph")
countHamiltinianCyclesRandomizedBiasedTestingUtil.run_test({"adjacency_matrix":graph_6x6_parsed['adjacency_matrix'],"is_directed":graph_6x6_parsed['is_directed'],"iterations":1000}, "Finding All Hamiltonian Cycles - Polynomial Time Approximation - 6x6 graph")
countHamiltinianCyclesRandomizedBiasedTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"iterations":1000}, "Finding All Hamiltonian Cycles - Polynomial Time Approximation - 10x10 graph")
countHamiltinianCyclesRandomizedBiasedTestingUtil.run_test({"adjacency_matrix":graph_15x15_parsed['adjacency_matrix'],"is_directed":graph_15x15_parsed['is_directed'],"iterations":1000}, "Finding All Hamiltonian Cycles - Polynomial Time Approximation - 15x15 graph")



# #### Testing different inputs - randomized testing

# In[24]:


graph_10x10_parsed={
  'number_of_vertices': 10,
 'adjacency_matrix': [[0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
  [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
  [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
  [1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
  [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]],
 'is_directed': True
 }
graph_12x12_parsed={
 'number_of_vertices': 12,
 'adjacency_matrix': [[0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
  [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
  [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
  [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]],
 'is_directed': False
 }


# In[25]:


countHamiltinianCyclesGeneticTestingUtil.run_test({"adjacency_matrix":graph_10x10_parsed['adjacency_matrix'],"is_directed":graph_10x10_parsed['is_directed'],"population_size":20, "generations":10}, "Finding All Hamiltonian Cycles - Genetic Algorithm - 10x10 graph, population size 20, generations 10")
countHamiltinianCyclesGeneticTestingUtil.run_test({"adjacency_matrix":graph_12x12_parsed['adjacency_matrix'],"is_directed":graph_12x12_parsed['is_directed'],"population_size":20, "generations":10}, "Finding All Hamiltonian Cycles - Genetic Algorithm - 12x12 graph, population size 20, generations 10")

