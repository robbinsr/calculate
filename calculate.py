# !/usr/bin/env python
# coding=utf-8
"""Computes binary data confusion matrix probabilities"""
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from argparse import ArgumentTypeError

# use lambdas not named functions

__author__ = "Russ Robbins"
__date__ = "9/9/2015"
__copyright__ = "None"
__credits__ = ["None"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Russ Robbins"
__email__ = "russ.robbins@outlook.com"
__status__ = "Sandbox"
__encoding__ = "UTF-8"
__todo__ = 'be sure to validate prior to returning'

"""
Calculate
#
#
#
"""

parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter)


def probability(value):
    """
    Validates that value passed to ArgumentParser is between 0 and 1
    Defines "ArgumentParser option type"
    :param value, the number as string to be validated as a probability
    :return value, the number as float validated as a probability
    :raise ArgumentTypeError, if value is not between 0 and 1
    """
    value = float(value)
    if not -0.00001 < value < 1.00001:
        raise ArgumentTypeError(
            'Input value {} should be between 0 and 1'.format(value))
    return value


def is_num_arguments_3(arguments: dict):
    """
    Validates that number of arguments passed to the parent module is 3
    :param arguments, from ArgumentParser
    :raise AssertionError if num of arguments is not 3
    """
    args = [args for args in arguments if args is not None]
    args_count = len(args)
    if args_count == 3:
        pass
    else:
        raise AssertionError('Number of probabilities input is {}, but should '
                             'be 3'.format(args_count))


def is_prob_sum_lteq_1(arguments: dict):
    """
    Validates that sum of arguments passed to the parent module is less than
    or equal to 1
    :param arguments
    :raise AssertionError if sum of probabilities greater than 1
    """
    # print(arguments)
    if sum([value for (key, value) in arguments.items()]) < 1.00001:
        pass
    else:
        raise AssertionError("Number of probabilities input is {}, but "
                             "should be 3".format(args_count))


parser.add_argument("-a", "--a", dest="a",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is classified/predicted "
                         "as A ",
                    metavar="prob of A",
                    action="store",
                    type=probability)

parser.add_argument("-na", "--not_a", dest="a",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is classified/predicted "
                         "as not A ",
                    metavar="prob of not A",
                    action="store",
                    type=probability)

parser.add_argument("-b", "--b", dest="b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is classified/predicted "
                         "as B ",
                    metavar="prob of B",
                    action="store",
                    type=probability)

parser.add_argument("-nb", "--not_b", dest="b",
                    help="Use this argument to input the probability "
                         "(e.g., 0.09) of a case that is classified/predicted "
                         "as not B ",
                    metavar="prob of not B",
                    action="store",
                    type=probability)

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

# pass from argsArgumentParser to dict
namespace_args = vars(parser.parse_args())

# remove verbose dict item
namespace_args = dict([(k, v) for (k, v) in namespace_args.items() if v is
                       not True])

# remove dict items with no values
namespace_args = dict(
    [(k, v) for (k, v) in namespace_args.items() if v is not None])

# check to see that number of arguments passed to module is 3
is_num_arguments_3(namespace_args)

# check to see that sum of the three arguments is less than or equal to 1
is_prob_sum_lteq_1(namespace_args)

# define probability dictionary, which when complete will be returned
probs = {'a': None,
         'not_a': None,
         'b': None,
         'not_b': None,
         'a_and_b': None,
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

# print("namespace_args: {}".format(namespace_args))
# print("probs: {}".format(probs))

def update_probs_w_input_probs(probs, namespace_args):
    for (arg_key, arg_val) in namespace_args.items():
        #print((arg_key, arg_val))
        for (pk, pv) in probs.items():
            #print((pk, pv))
            if arg_key==pk:
                #print("hit")
                probs[pk] = arg_val
    return probs

probs = update_probs_w_input_probs(probs, namespace_args)

print(probs)

#four functions to determine the probability of A

def a_from_a_and_b_also_b_giv_a(a_and_b, b_giv_a):
    """
    Calculate the probability of a from a_and_b as well as b_giv_a
    :param a_and_b:
    :param b_giv_a:
    :return: a
    """
    a = None
    if a_and_b is not None and b_giv_a is not None:
        try:
            a = float(a_and_b) / float(b_giv_a)
        except ZeroDivisionError:
            print("WARNING: Value for B given A {} is zero, Value for A "
                "not computed".format(b_giv_a))
    return a

def a_from_a_and_not_b_also_not_b_giv_a(a_and_not_b, not_b_giv_a):
    """
    Calculate the probability of a from a_and_not_b as well as not_b_giv_a
    :param a_and_not_b:
    :param not_b_giv_a:
    :return: a
    """
    a = None
    if a_and_not_b is not None and not_b_giv_a is not None:
        try:
            a = float(a_and_not_b) / float(not_b_giv_a)
        except ZeroDivisionError:
            print("WARNING: Value for not B given A {} is zero, Value for A "
                "not computed".format(not_b_giv_a))
    return a

def a_from_a_and_b_also_a_and_not_b(a_and_b, a_and_not_b):
    """
    Calculate a from a_and_b as well as a_and_not_b
    :param a_and_b:
    :param a_and_not_b:
    :return: a
    """
    a = None
    if a_and_b is not None and a_and_not_b is not None:
        a = a_and_b + a_and_not_b

    return a

def a_from_not_a(not_a):
    """
    Calculate the probability of A from the probability of not A
    :param not_a:
    :return: a
    """
    a = None
    if not_a is not None:
        a = float(1) - float(not_a)

    return a

#four functions to determine the probablity of not A

def not_a_from_not_a_and_b_also_b_giv_not_a(not_a_and_b, b_giv_not_a):
    """
    Determine not_a from not_a_and_b as well as b_giv_not_a
    :param not_a_and_b:
    :param b_giv_not_a:
    :return: not_a
    """
    not_a = None
    if not_a_and_b is not None and b_giv_not_a is not None:
        try:
            not_a = not_a_and_b / b_giv_not_a
        except ZeroDivisionError:
            print("WARNING: Value for B given not A {} is zero, Value for not A "
                "not computed".format(b_giv_not_a))

    return not_a

#need not_a_and_b + not_a_and_not_b

#need not_a_and_not_b divided by not_b_and_not_a

#need 1 - a

#need four functions for computing B

#need four functions for computing not B

# four functions to determine the probability of a and b

def a_and_b_from_a_and_not_b_also_a(a_and_not_b, a):
    """ Calculate a_and_b from a_and_not_b as well as a
    :param a_and_not_b:
    :param a
    :return: a_and_b
    """
    a_and_b = None
    if a_and_not_b is not None and a is not None:
        a_and_b = float(a) - float(a_and_not_b)
    return a_and_b

def a_and_b_from_b_and_not_a_also_b(not_a_and_b, b):
    """ Calculate a_and_b from not_a_and_b as well as b
    :param not_a_and_b:
    :param b
    :return: a_and_b
    """
    a_and_b = None
    if not_a_and_b is not None and b is not None:
        a_and_b = float(b) - float(not_a_and_b)
    return a_and_b

def a_and_b_from_a_giv_b_also_b(a_giv_b, b):
    """ Calculate a_and_b from a_giv_b as well as b
    :rtype : float
    :param a_giv_b
    :param b
    :return a_and_b
    """
    a_and_b = None
    if a_giv_b is not None and b is not None:
        a_and_b = float(b) * float(a_giv_b)

    return a_and_b

def a_and_b_from_b_giv_a_also_a(b_giv_a, a):
    """ Calculate a_and_b from b_giv_a as well as a
    :param b_giv_a
    :param a
    :return a_and_b
    """
    a_and_b = None
    if b_giv_a is not None:
         a_and_b = float(b) * float(b_giv_a)

    return a_and_b

# four functions to determinine the probability of a and not b

def a_and_not_b_from_a_and_b_also_a(a_and_b, a):
    """ Calculate a_and_not_b from a_and_b as well as a
    :param a_and_b:
    :param a
    :return: a_and_not_b
    """
    a_and_not_b = None
    if a_and_b is not None:
        a_and_not_b = float(a) - float(a_and_b)
    return a_and_not_b

def a_and_not_b_from_not_a_and_not_b_also_not_b(not_a_and_not_b, not_b):
    """ Calculate a_and_not_b from not_a_and_not_b as well as not b
    :param not_a_and_not_b:
    :param not_b
    :return: a_and_not_b
    """
    a_and_not_b = None
    if not_a_and_not_b is not None:
        a_and_not_b = float(not_b) - float(not_a_and_not_b)
    return a_and_not_b

def a_and_not_b_from_a_giv_not_b_also_not_b(a_giv_not_b, not_b):
    """ Calculate a_and_b from a_giv_not_b as well as not_b
    :rtype : float
    :param a_giv_not_b
    :param not_b
    :return a_and_not_b
    """
    a_and_not_b = None
    if a_giv_not_b is not None and not_b is not None:
        a_and_not_b = float(not_b) * float(a_giv_not_b)
    return a_and_not_b

def a_and_not_b_from_not_b_giv_a_also_a(not_b_giv_a, a):
    """ Calculate a_and_b from not_b_giv_a
    :rtype : float
    :param not_b_giv_a
    :param a
    :return a_and_not_b
    """
    a_and_not_b = None
    if not_b_giv_a is not None:
         a_and_not_b = float(a) * float(not_b_giv_a)
    return a_and_not_b

# four functions to determine the probability of not a and b

def not_a_and_b_from_a_and_b_also_b(a_and_b, b):
    """ Calculate not_a_and_b from a_and_b as well as b
    :param a_and_b:
    :param b
    :return: not_a_and_b
    """
    not_a_and_b = None
    if a_and_b is not None:
        not_a_and_b = float(b) - float(a_and_b)
    return not_a_and_b

def not_a_and_b_from_not_a_and_not_b_also_not_a(not_a_and_not_b, not_a):
    """ Calculate not_a_and_b from not_a_and_not_b as well as not_a
    :param not_a_and_not_b:
    :param not_a
    :return: not_a_and_b
    """
    not_a_and_b = None
    if not_a_and_not_b is not None:
        not_a_and_b = float(not_a) - float(not_a_and_not_b)
    return not_a_and_b

def not_a_and_b_from_b_giv_not_a_also_not_a(b_giv_not_a, not_a):
    """Calculate not_a_and_b from b_giv_not_a as well as not_a
    :param b_giv_not_a
    :param not_a
    :return not_a_and_b
    """
    not_a_and_b = None
    if b_giv_not_a is not None and not_a is not None:
        not_a_and_b = float(not_a) * float(b_giv_not_a)
    return not_a_and_b

def not_a_and_b_from_not_a_giv_b_also_b(not_a_giv_b, b):
    """Calculate not_a_and_b from not_a_giv_b as well as b
    :param not_a_giv_b
    :param b
    :return: not_a_and_b
    """
    not_a_and_b = None
    if not_a_giv_b is not None and b is not None:
        not_a_and_b = float(b) * not_a_giv_b
    return not_a_and_b

switch = {  #functions to determine the probability of A
            ('a_and_b','b_giv_a','a')
            :a_from_a_and_b_also_b_giv_a,
            ('a_and_not_b','not_b_giv_a','a'):
             a_from_a_and_not_b_also_not_b_giv_a,
            ('a_and_b','a_and_not_b','a'):
            a_from_a_and_b_also_a_and_not_b,
            ('not_a', None, 'a'):
            a_from_not_a,

            #functions to determine the probability of not A

            ('not_a_and_b','b_giv_not_a','not_a'):
            not_a_from_not_a_and_b_also_b_giv_not_a,

            # need not_a_and_b + not_a_and_not_b

            # need not_a_and_not_b divided by not_b_and_not_a

            # need 1 - a

            # need four functions for computing B

            # need four functions for computing not B

            #functions to determine the probability of A and B
           ('a_and_not_b','a', 'a_and_b'):
               a_and_b_from_a_and_not_b_also_a,
           ('not_a_and_b','b', 'a_and_b'):
               a_and_b_from_b_and_not_a_also_b,
           ('a_giv_b', 'b', 'a_and_b'):
               a_and_b_from_a_giv_b_also_b,
           ('b_giv_a','a', 'a_and_b'):
               a_and_b_from_b_giv_a_also_a,
           #functions to determine the probability of A intersection Not B
           ('a_and_b', 'a','a_and_not_b'):
               a_and_b_from_a_and_not_b_also_a,
           ('not_a_and_not_b','not_b','a_and_not_b'):
              a_and_not_b_from_not_a_and_not_b_also_not_b,
           ('a_giv_not_b','not_b','a_and_not_b'):
               a_and_not_b_from_a_giv_not_b_also_not_b,
          ('not_b_giv_a','a','a_and_not_b'):
               a_and_not_b_from_not_b_giv_a_also_a,
           #functions to determine the probability of Not A and B
          ('a_and_b', 'b', 'not_a_and_b'):
               not_a_and_b_from_a_and_b_also_b,
          ('not_a_and_not_b','not_a', 'not_a_and_b'):
               not_a_and_b_from_not_a_and_not_b_also_not_a,
           ('b_giv_not_a','not_a','not_a_and_b'):
               not_a_and_b_from_b_giv_not_a_also_not_a,
           ('not_a_giv_b','b','not_a_and_b'):
                not_a_and_b_from_not_a_giv_b_also_b

            #need twelve functions for b_giv_a, not_b_giv_a, b_giv_not_a,
            # and not_b_giv_not_a

            #need twelve functions for a_giv_b, not_a_giv_b, a_giv_not_b,
            # and not_a_giv_not_b

            #ratios go here
            }


def dispatch(p: dict, s: dict):
    """ Update probabilites based on known probabilities
    :param p # probs
    :param s # switch
    """
    for (pk, pv) in p.items():
        if pv is None:
            for ((sk1, sk2), sv) in s.items():
                if sk2 == pk:
                    p[pk] = sv(p[sk1])

        else:
            pass

    return p

probs = dispatch(probs, switch)

print(probs)
