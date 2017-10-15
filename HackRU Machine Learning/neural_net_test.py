import tensorflow as tf
import argparse

parser = argparse.ArgumentParser(description='Evaluate model.')
parser.add_argument('data', metavar='X', type=str, nargs='+',
                    help='variables for the model')

args = parser.parse_args()

marital_status = args.data[0]
marital_status = args.data[1]
marital_status = args.data[2]
marital_status = args.data[3]
marital_status = args.data[4]
marital_status = args.data[5]
marital_status = args.data[6]
marital_status = args.data[7]
marital_status = args.data[8]
marital_status = args.data[0]
marital_status = args.data[0]

sess=tf.Session()

#oad meta graph and restore weights
saver = tf.train.import_meta_graph('model.meta')
saver.restore(sess,tf.train.latest_checkpoint('./'))

graph = tf.get_default_graph()
X = graph.get_tensor_by_name("X:0")
Y = graph.get_tensor_by_name("Y:0")

test_x, test_y = get_test_data()
x = tf.reshape(test_x[0],[1, 11])
x = sess.run(x)
a = sess.run(Y, feed_dict={X: x})


if a[0] > a[1]:
    print('Unlikely')
else:
    print('Likely')

#0.994987