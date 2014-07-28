"""
This relates to posted oDesk and Elance projects.
"""
import collections

fruit_bag_fields = ['fruit_type', 'fruit_qty', 'source_id']

# fruit_type is an arbitrary type of fruit, e.g. 'banana', 'apple', or 'asdgaj'
# fruit_qty is how many of that fruit are included in that bag
# source_id is an arbitrary unique identifier

fruit_bag = collections.namedtuple('fruit_bag', fruit_bag_fields)

fruit_order_fields = ['order_type', 'participant_id', 'order_content']

# order_type can EITHER be 'buy' OR 'sell', but nothing else
# participant_id is an arbitrary unique identifier
#  (we only care about buy order participant_id's; the seller's participant_ids
#   can be discarded)
# for sell orders, order_content is a list of fruit_bag namedtuples
# for buy orders, order_content is a quantity of fruit pieces
#  (because buyers do not get to select fruit types; they only get the roughly
#   proportional split that is the objective of this algorithm)

fruit_order = collections.namedtuple("fruit_order", fruit_order_fields)

class FruitBox(object):
    """
    Keeping FruitBox 
    """
    def __init__(self):
        """
        Basic constructor
        """
        
        self.undivided_fruit_bags = []
        self.buy_quantities = {}  # buyer's participant_id:
                                  # quantity desired
        self.registry   = {} # buyer_id : [new_smaller_fruit_bags]

        #...?

    def add_orders(self, order_list):
        """
        Figure out whether each is a buy or a sell order, then register it.
        """
        pass
        
    def register_sell(self, sell_order):
        """
        # add the fruit bags to self.undivided_fruit_bags
        """
        pass

    def register_buy(self, buy_order):
        """
        Add the buy order to the ordered list of buys. Update (or create) the
        unsold buy_quantity item in self.buy_quantities and make sure that
        isn't negative (or raise an exception).
        """
        pass

    def divvy(self):
        """
        Make the magic happen here. Assign a new list of fruit_bags to each
        buyer's participant_id, including one list of fruit_bags to an
        unsold id (if the buy order total is less than the total qty of fruit
        being sold).
        """
        pass
