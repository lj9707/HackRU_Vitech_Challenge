import tensorflow as tf
from data_helper import *
import math
import pickle

input_size = 11
l1 = 100
l2 = 60
l3 = 30
l4 = 10
output_size = 2

X = tf.placeholder(tf.float32, [None, input_size], name='X')

W1 = tf.Variable(tf.truncated_normal([input_size, l1], stddev=0.1))
B1 = tf.Variable(tf.zeros([l1]))

W2 = tf.Variable(tf.truncated_normal([l1, l2], stddev=0.1))
B2 = tf.Variable(tf.zeros([l2]))

W3 = tf.Variable(tf.truncated_normal([l2, l3], stddev=0.1))
B3 = tf.Variable(tf.zeros([l3]))

W4 = tf.Variable(tf.truncated_normal([l3, l4], stddev=0.1))
B4 = tf.Variable(tf.zeros([l4]))

W5 = tf.Variable(tf.truncated_normal([l4, output_size], stddev=0.1))
B5 = tf.Variable(tf.zeros([output_size]))

Y1 = tf.nn.relu(tf.matmul(X, W1) + B1)
Y2 = tf.nn.relu(tf.matmul(Y1, W2) + B2)
Y3 = tf.nn.relu(tf.matmul(Y2, W3) + B3)
Y4 = tf.nn.relu(tf.matmul(Y3, W4) + B4)
Ylogits = tf.matmul(Y4, W5) + B5
Y = tf.nn.softmax(Ylogits, name='Y')

Y_ = tf.placeholder(tf.float32, [None, output_size], name='Y_')

lr = tf.placeholder(tf.float32)



cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=Ylogits, labels=Y_)
cross_entropy = tf.reduce_mean(cross_entropy)*100

correct_prediction = tf.equal(tf.argmax(Y, 1), tf.argmax(Y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), name='accuracy')

train_step = tf.train.AdamOptimizer(lr).minimize(cross_entropy)

init = tf.initialize_all_variables()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

sess = tf.Session()
sess.run(init)

for i in range(2500):


    batch_x, batch_y = next_train_batch(100)
    # learning rate decay
    max_learning_rate = 0.003
    min_learning_rate = 0.0001
    decay_speed = 2000.0  # 0.003-0.0001-2000=>0.9826 done in 5000 iterations
    learning_rate = min_learning_rate + (max_learning_rate - min_learning_rate) * math.exp(-i / decay_speed)

    train_data = {X: batch_x, Y_: batch_y, lr: learning_rate}


    sess.run(train_step, feed_dict=train_data)

    a,c = sess.run([accuracy, cross_entropy], feed_dict=train_data)

    test_x, test_y = get_test_data()
    a,c = sess.run([accuracy, cross_entropy], feed_dict={X: test_x, Y_:test_y})


    print('Step ' + str(i) + '\n' + 'Accuracy: ' +str(a))

save_path = saver.save(sess, "model")