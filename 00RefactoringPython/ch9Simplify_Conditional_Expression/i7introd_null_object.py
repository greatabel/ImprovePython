from mycolor import show

class Customer(object):
    def get_plan(self):
        return 'A goal without a plan is just a wish'
        
class BillingPlan:
    def basic(self):
        return 'By failing to prepare, you are preparing to fail.'

customer = None
billing_plan = BillingPlan()

print('-·--·--·--·-正文部分-·-·-·-·-·-·-·')

if customer == None:
    plan = billing_plan.basic()
else:
    plan = customer.get_plan()

print(show(plan))
print('- · - - · 开始改造 - - · - - · - ')


class NullCustomer(Customer):
    def get_plan(self):
        return BillingPlan().basic()

print(customer, customer == None)
customer1 = NullCustomer() if customer == None else Customer()

plan = customer1.get_plan()
print(show(plan, 'red'))

