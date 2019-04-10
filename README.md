# Models Warehouse

This repository contains different Reinforcement Learning models.

### Installation:
```
git clone https://github.com/shakedzy/warehouse.git
cd warehouse
pip install .
```
**Requirements:**
* `numpy`
* `tensorflow` (either CPU or GPU)

## Models:
### Deep Q-Network:
A simple implementation of a Deep Q-Network model (an introduction to this model can be found 
[in this blogpost](https://medium.com/@shakedzy/qrash-course-deep-q-networks-from-the-ground-up-1bbda41d3677)). 

Simple usage example:
```
from warehouse.dqn import DeepQNetworkModel
model = DeepQNetworkModel(session=tf.Session(),
                          layers_size=[9,20,50,10,9],
                          memory=memory_buffer.ExperienceReplayMemory(1000),
                          default_batch_size=250,
                          default_learning_rate=0.001,
                          default_epsilon=0.1,
                          gamma=0.99)
```
Extensions:
* _Double Deep Q Network:_ Based on [[1]](#ref1). The actual Q-target update rule is performed in the following way:
![ddqn_update](readme_images/ddqn_update.png)
as suggested [here](https://github.com/awjuliani/DeepRL-Agents/blob/master/Double-Dueling-DQN.ipynb). 
`tau=1` will yield the theoretical Double Deep Q-Network model.

* _Maximun Entropy:_ Based on [[2]](#ref2) and designed according to this post.

## Auxiliaries:
### Memory Buffers:
All memory buffers inherit form the `memory_buffers.MemoryTemplate` class. 

For all memory buffer types, `len(memory)`
yields the number of elements within the buffer, while `memory.counter` yields the number of elements seen
by the memory buffer, even if these elements whrere removed or never inserted. 

* `ExperienceReplayMemory`: A basic cyclic-buffer memory buffer
* `ReservoirSamplingMemory`: A memory buffer based on 
[reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling).

---------------------

### References:
<a id="ref1"></a>
1} Lillicrap _et al._, Continuous control with deep reinforcement learning [[arXiv](https://arxiv.org/abs/1509.02971)]

<a name="ref2"></a>
2} Haarnoja _et al._, Reinforcement Learning with Deep Energy-Based Policies [[arXiv](https://arxiv.org/abs/1702.08165)]