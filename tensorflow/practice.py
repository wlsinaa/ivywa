import tensorflow as tf

print(tf.__version__)
# 2.9.1
scalar = tf.constant(7)
# print(scalar.ndim)

# vector
v = tf.constant([10,10]) #list to vector
# print(v.ndim)
matrix = tf.constant([[10,6],[7,10]]) # default : int 32
# print(matrix.ndim)
# create another matrix
an_matrix = tf.constant([[10.,7.], [3.,2.], [8.,9.]], dtype = tf.float16)
# print(an_matrix.ndim)
# create 3-d list to get ndim == 3

print("-----------Variable--------------")
print(tf.Variable) # changeable tensor
changeable_tensor = tf.Variable([1,2])
# try .assign
changeable_tensor[0].assign(7)
changeable_tensor[1].assign(8)
# print(changeable_tensor)
print("-----------Random--------------")
# create random tensors
ran_1 = tf.random.Generator.from_seed(42) # set seed for reproducibility
ran_1 = ran_1.normal(shape= (3,2))
ran_2 = tf.random.Generator.from_seed(42)
ran_2 = ran_2.normal(shape= (3,2))
# print(ran_1,ran_2 ,ran_1==ran_2)
print("------------Shuffle the order-------------")
# shuffle a tensor (valuable for when you want to shuffle your data so the inherent order doesn't affect learning)
not_shu = tf.constant([[10,7],[3,4],[2,5]],dtype = tf.float32)
tf.random.set_seed(42) # ensure the order (global seed)
rand_3 = tf.random.shuffle(not_shu, seed = 42) # operational seed 
print(rand_3)
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")
print("-------------------------")
