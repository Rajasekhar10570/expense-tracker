import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ExpenseCalc:

    def __init__(self):
        self.name = 'Hello World'

    def display(self):
        print('Hello How are You!')

    def get_this_month_total_expense(self):
        logger.info('Function get_this_month_total_expense starts ')
        
        logger.info('Function get_this_month_total_expense ends ')
