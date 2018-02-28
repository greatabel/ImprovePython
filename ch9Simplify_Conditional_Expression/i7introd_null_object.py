from mycolor import show

class Customer(object):
    def get_plan(self):
        return 'A goal without a plan is just a wish'
        
class BillingPlan:
    def basic(self):
        return 'By failing to prepare, you are preparing to fail.'

customer = Customer()
billing_plan = BillingPlan()

print('-·--·--·--·-正文部分-·-·-·-·-·-·-·')

if customer == None:
    plan = billing_plan.basic()
else:
    plan = customer.get_plan()

print(show(plan))