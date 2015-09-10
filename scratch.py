# !/usr/bin/env python
# coding=utf-8
"""Computes binary data confusion matrix probabilities"""
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from argparse import ArgumentTypeError

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

"""
Takes three probabilities from a confusion table and returns the other
probabilities.
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


"""
rework the three below since we are going to use all the probabilities
"""


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


"""
to parse command line arguments passed to program
"""

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

"""
move from argument parser to probability dict
need to rename namespace_args probs if vars() returns correct shape
"""

# pass from argsArgumentParser to dict
namespace_args = vars(parser.parse_args())

# remove verbose dict item
namespace_args = dict([(k, v) for (k, v) in namespace_args.items() if v is
                       not True])

"""
probably don't need next assignment expression
"""
# # remove dict items with no values
# namespace_args = dict(
#     [(k, v) for (k, v) in namespace_args.items() if v is not None])

"""
can't use two items below until the functions at program head are rebuilt
"""
# # check to see that number of arguments passed to module is 3
# is_num_arguments_3(namespace_args)
#
# # check to see that sum of the three arguments is less than or equal to 1
# is_prob_sum_lteq_1(namespace_args)

###

"""declare probabilities dictionary"""

probs = {'a': .5, 'na': None, 'b': None, 'nb': None,
         'ab': None, 'anb': None, 'nab': None, 'nanb': None,
         'agb': None, 'agnb': None, 'nagb': None, 'nagnb': None,
         'bga': None, 'nbga': 1, 'bgna': None, 'nbgna': None}

"""
at this point pass arguments to the probs dictionary so it can be used against
 the switch dict
"""

"""declare the dispatch dict"""

dispatch = {
    # a and b
    ('ab', 'a', 'bga'): lambda ab, a, bga:
    float(a) * float(bga) if ab is None and a is not None and bga is not None
    else ab,
    ('ab', 'b', 'agb'): lambda ab, b, agb:
    float(b) * float(agb) if ab is None and b is not None and agb is not None
    else ab,
    ('ab', 'a', 'anb'): lambda ab, a, anb:
    float(a) - float(anb) if ab is None and a is not None and anb is not None
    else ab,
    ('ab', 'b', 'nab'): lambda ab, b, nab:
    float(b) - float(nab) if ab is None and b is not None and nab is not None
    else ab,
    # a and not b
    ('anb', 'a', 'nbga'): lambda anb, a, nbga:
    float(a) * float(nbga) if anb is None and a is not None and nbga is not None
    else anb
}

"""
may need while loop for the dispatches
"""

probs['ab'] = dispatch[('ab', 'a', 'bga')](probs['ab'], probs['a'], probs['bga'])
probs['ab'] = dispatch[('ab', 'b', 'agb')](probs['ab'], probs['b'], probs['agb'])
probs['ab'] = dispatch[('ab', 'a', 'anb')](probs['ab'], probs['a'], probs['anb'])
probs['ab'] = dispatch[('ab', 'b', 'nab')](probs['ab'], probs['b'], probs['nab'])
probs['anb'] = dispatch[('anb', 'a', 'nbga')](probs['anb'], probs['a'], probs['nbga'])

print(probs['anb'])
