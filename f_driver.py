#!/usr/bin/env python

"""
A driver for the fruitbox module.
"""

import time
import fruitbox

if __name__ == "__main__":
    start = time.time()

    # create the first bags of fruit

    apples0 = fruitbox.fruit_bag._make("apples", 7, "Knott's Berry Farm")
    apples1 = fruitbox.fruit_bag._make("apples", 3, "Astroworld")
    oranges = fruitbox.fruit_bag._make("oranges", 7, "Beantown")
    pears0  = fruitbox.fruit_bag._make("pears", 3, "Kroger")
    pears1  = fruitbox.fruit_bag._make("pears", 2, "Randall's")
    lemons  = fruitbox.fruit_bag._make("lemons", 2, "The Moone")

    bags1   = [apples0, apples1, oranges, pears1]
    bags2   = [pears0, lemons]

    first_sell  = fruitbox.fruit_order._make("sell", "merchant1", bags1)
    second_sell = fruitbox.fruit_order._make("sell", "merchant2", bags2)
    first_buy   = fruitbox.fruit_order._make("buy", "merchant3", 9)
    second_buy  = fruitbox.fruit_order._make("buy", "merchant4", 8)
    third_buy   = fruitbox.fruit_order._make("buy", "merchant5", 4)
    fourth_buy  = fruitbox.fruit_order._make("buy", "merchant6", 3)

    # create the first FruitBox

    fb0 = fruitbox.FruitBox()

    fb0.add_orders([first_sell, second_sell,
                    first_buy, second_buy, third_buy, fourth_buy])

    fb0.divvy()

    print fb0.registry

    end = time.time()

    print "Running time: %.2f seconds." % (end-start)
