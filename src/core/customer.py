from src.utils import load_data, filter_by_options

class CustomerCore:
    def get_customer(by, value):
        if not by or not value:
            raise Exception('you need to inform a filter')
        customer_data = load_data('customers')
        return list(filter(lambda customer: customer.get(by) == value, customer_data))

    def get_customers(last=None):
        customer_data = load_data('customers')
        return filter_by_options(last=last, content=customer_data)

    def get_views(id, category, last):
        if not id:
            raise Exception('you need to inform a filter')
        views_data = load_data('views')
        customer_views = list(filter(lambda views: views.get('customer_id') == id, views_data))

        return filter_by_options(last=last, category=category, content=customer_views)
