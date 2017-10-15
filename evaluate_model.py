import tensorflow as tf
import argparse
from dateutil.parser import parse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description='Evaluate model.')
    parser.add_argument('data', metavar='X', type=str, nargs='+',
                        help='variables for the model')

    #print(sys.argv)

    #args = parser.parse_args()

    #print(str(len(args.data)))


    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '4'

    marital_status = int(sys.argv[1])
    sex = int(sys.argv[2])
    longitude = float(sys.argv[3]) / 40
    latitude = float(sys.argv[4]) / 40
    date_added = parse(sys.argv[5])
    date_added = int(date_added.strftime("%s")) / 31536000 / 30
    birth_date = parse(sys.argv[6])
    birth_date = int(birth_date.strftime("%s")) / 31536000 / 30
    insurance_coverage = int(sys.argv[7])
    insurance_premium = int(sys.argv[8]) / 20
    insurance_plan = int(sys.argv[9])
    policy_start_date = parse(sys.argv[10])
    policy_start_date = int(policy_start_date.strftime("%s")) / 31536000 / 30
    state = float(sys.argv[11])



    x = [marital_status, sex, longitude, latitude, date_added, birth_date, insurance_coverage, insurance_premium,
         insurance_plan, policy_start_date, state]



    sess = tf.Session()


    #Load meta graph and restore weights
    saver = tf.train.import_meta_graph('/Users/tysovsky/Desktop/HackRU/model.meta')


    kl = tf.train.latest_checkpoint('/Users/tysovsky/Desktop/HackRU/')

    saver.restore(sess, kl)


    graph = tf.get_default_graph()
    X = graph.get_tensor_by_name("X:0")
    Y = graph.get_tensor_by_name("Y:0")

    x = tf.reshape(x, [1, 11])
    x = sess.run(x)
    a = sess.run(Y, feed_dict={X: x})

    if a[0][0] < a[0][1]:
        print('Unlikely')
    else:
        print('Likely')


if __name__ == '__main__':
    main()
