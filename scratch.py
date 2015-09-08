# !/usr/bin/env python
# coding=utf-8
"""Computes binary data confusion matrix probabilities"""
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from argparse import ArgumentTypeError

__author__ = "Russ Robbins"
__date__ = "9/6/2015"
__copyright__ = "None"
__credits__ = ["None"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Russ Robbins"
__email__ = "russ.robbins@outlook.com"
__status__ = "Sandbox"
__encoding__ = "UTF-8"

"""
Calculate
#
#
#
"""

parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)


def probability(value):
    """
    Validates that value is between 0 and 1
    :param value: the number as string to be validated as a probability
    :return value: the number as float validated as a probability
    :raise ArgumentTypeError: if value is not between 0 and 1
    """
    value = float(value)
    if not -0.00001 < value < 1.00001:
        raise ArgumentTypeError(
            'Input value {} should be between 0 and 1'.format(value))
    return value


parser.add_argument("-ab", "--a_and_b", dest="a_and_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is both predicted to be "
                         "true (e.g., a) and found or assumed to be true "
                         "(e.g., b)",
                    metavar="prob of a and b",
                    action="store",
                    type=probability)

parser.add_argument("-anb", "--a_and_not_b", dest="a_and_not_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of an case that is predicted to be true "
                         "(e.g., a) and is found or assumed to be not true "
                         "(e.g., not b)", metavar="prob of a and not b",
                    action="store", type=probability)

parser.add_argument("-nab", "--not_a_and_b", dest="not_a_and_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of an "
                         "case that is predicted to be not true (e.g., "
                         "not a) and is found or assumed to be true ("
                         "e.g., b)",
                    metavar="prob of not a and b",
                    action="store",
                    type=probability)

parser.add_argument("-nanb", "--not_a_and_not_b", dest="not_a_and_not_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of an case that is predicted "
                         "to be not true (e.g., not a) and is found or is "
                         "assumed to not be true (e.g., not b)",
                    metavar="prob of not a and not b",
                    action="store",
                    type=probability)

# arguments for conditional probabilities

parser.add_argument("-agb", "--a_giv_b", dest="a_giv_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is predicted to be true"
                         "(e.g., a) given the case is found or is assumed to "
                         "be true"
                         "(e.g., b)",
                    metavar="prob of a given b",
                    action="store",
                    type=probability)

parser.add_argument("-agnb", "--a_giv_not_b", dest="a_giv_not_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is predicted to be true "
                         "(e.g., a) given the case is found or is assumed to "
                         "be not true (e.g., not b)",
                    metavar="prob of a given not b",
                    action="store",
                    type=probability)

parser.add_argument("-nagb", "--not_a_giv_b", dest="not_a_giv_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is predicted "
                         "to be not true (e.g., not a) given the case "
                         "is found or is assumed to be true (e.g., b)",
                    metavar="prob of not a given b",
                    action="store",
                    type=probability)

parser.add_argument("-nagnb", "--not_a_giv_not_b", dest="not_a_giv_not_b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is predicted "
                         "to be not true (e.g., not a) given the case is found "
                         "or is assumed to be not true (e.g., not b)",
                    metavar="prob of not a given not b",
                    action="store",
                    type=probability)

parser.add_argument("-bga", "--b_giv_a", dest="b_giv_a",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is found or is assumed "
                         "to be true (e.g., b) given the case is predicted "
                         "to be true (e.g., a)",
                    metavar="prob of b given a",
                    action="store",
                    type=probability)

parser.add_argument("-bgna", "--b_giv_not_a", dest="b_giv_not_a",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is found or is assumed "
                         "to be true (e.g., b) given the case is predicted "
                         "to be true (e.g., a)",
                    metavar="prob of b given a",
                    action="store",
                    type=probability)

parser.add_argument("-nbga", "--not_b_giv_a", dest="not_b_giv_a",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is found or is assumed "
                         "to be not true (e.g., not b) given the case "
                         "is predicted to be true (e.g., a)",
                    metavar="prob of not b given a",
                    action="store",
                    type=probability)

parser.add_argument("-nbgna", "--not_b_giv_not_a", dest="not_b_giv_not_a",

                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is is found or is assumed"
                         "to be not true (e.g., not b) given the case is "
                         "predicted to be not true (e.g., not a)",
                    metavar="prob of not b given not a",
                    action="store", type=probability)

# special case arguments

parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

namespace_args = vars(parser.parse_args())

namespace_args = dict([(k, v) for (k, v) in namespace_args.items() if v is
                       not True])

namespace_args = dict(
    [(k, v) for (k, v) in namespace_args.items() if v is not None])

probs = {'a_and_b': None,
         'a_and_not_b': None,
         'not_a_and_b': None,
         'not_a_and_not_b': None,
         'a_giv_b': None,
         'a_giv_not_b': None,
         'not_a_giv_b': None,
         'not_a_giv_not_b': None,
         'b_giv_a': None,
         'b_giv_not_a': None,
         'not_b_giv_a': None,
         'not_b_giv_not_a': None}

for (k, v) in namespace_args.items():
    probs[k] = v


# for (k, v) in probs.items():
#     print(k, v)


# functions to compute probability

def a_and_b_from_a_and_not_b(a_and_not_b):
    """ Calculate a_and_b from a_and_not_b
    :param a_and_not_b:
    :return: a_and_b
    """
    a_and_b = None
    if a_and_not_b is not None:
        a_and_b = float(1) - float(a_and_not_b)
    return a_and_b


def a_and_b_from_not_a_and_b(not_a_and_b):
    """ Calculate a_and_b from not_a_and_b
    :param not_a_and_b:
    :return: a_and_b
    """
    a_and_b = None
    if not_a_and_b is not None:
        a_and_b = float(1) - float(not_a_and_b)
    return a_and_b


def a_and_b_from_a_giv_b(a_giv_b):
    """ Calculate a_and_b from a_giv_b
    :param a_giv_b
    :return a_and_b
    """
    a_and_b = None
    try:
        if a_giv_b is not None:
            a_and_b = float(1) / float(a_giv_b)
    except ZeroDivisionError:
        print(
            "WARNING: Value for A given B {} is zero, Value for A and B "
            "not computed".format(a_giv_b))
    return a_and_b


def a_and_b_from_b_giv_a(b_giv_a):
    """ Calculate a_and_b from b_giv_a
    :param b_giv_a
    :return a_and_b
    """
    a_and_b = None
    try:
        if b_giv_a is not None:
            a_and_b = float(1) / float(b_giv_a)
    except ZeroDivisionError:
        print(
            "WARNING: Value for B given A {} is zero, Value for A and B "
            "not computed".format(b_giv_a))
    return a_and_b



switch = {('a_and_not_b', 'a_and_b'): a_and_b_from_a_and_not_b,
          ('not_a_and_b', 'a_and_b'): a_and_b_from_not_a_and_b,
          ('a_giv_b', 'a_and_b'): a_and_b_from_a_giv_b,
          ('b_giv_a', 'a_and_b'): a_and_b_from_b_giv_a}


# probs['a_and_b'] = switch['a_and_not_b'](probs['a_and_not_b'])
# probs['a_and_b'] = switch['not_a_and_b'](probs['not_a_and_b'])
# probs['a_and_b'] = switch['a_giv_b'](probs['a_giv_b'])
# probs['a_and_b'] = switch['b_giv_a'](probs['b_giv_a'])


def dispatch(p: dict, s:dict):
    """ Update probabilites based on known probabilities
    :param p # probs
    :param s # switch
    :return p # probs
    """
    #while None in p.values():
    for (pk, pv) in p.items():
        if pv is None:
            for ((sk1,sk2),sv) in s.items():
                if pk == sk2 and p[sk1] is not None:
                    print("pk is: {}".format(pk))
                    print("pv is: {}".format(pv))
                    print("sk1 is: {}".format(sk1))
                    print("sk2 is: {}".format(sk2))
                    print("sv is: {}".format(sv))
                    #p['a_and_b'] = s[('a_and_not_b', 'a_and_b')](p['a_and_not_b'])
                    p[pk] = s[(sk1,pk)](p[sk1])
                    # p['a_and_b'] = s['not_a_and_b'](p['not_a_and_b'])
                    # p['a_and_b'] = s['a_giv_b'](p['a_giv_b'])
                    # p['a_and_b'] = s['b_giv_a'](p['b_giv_a'])
                else:
                    pass

    return p


probs = dispatch(probs, switch)

for (k, v) in probs.items():
    if v is not None:
        print(k, v)
