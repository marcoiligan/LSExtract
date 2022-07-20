from repository.CustomerRepository import CustomerRepository
from repository.ProductRepository import ProductRepository
from repository.InvoiceRepository import InvoiceRepository
from repository.OrderRepository import OrderRepository
from repository.UserRepository import UserRepository



flag = True
while flag :
    choice = int(input("Choose from the Choices 1-Customer 2-Product 3-Invoices 4-Orders 5-Users 6-Exit: "))
    match choice:
        case 1:
            repo = CustomerRepository()
            print(repo.get_all_customer())
            customers = []
            flag2 = True
            while flag2:
                choiceC = int(input("Welcome to Customer 1-Get Customer 2-Get All Customer 3-List All Customers 4-Import Customers to DB 5-Exit: "))
                match choiceC:
                    case 1:
                        num = int(input("Enter ID: "))
                        customer = repo.get_customer(num)
                        print(f"Customer ID: {customer.id}")
                        print(f"Customer created: {customer.created}")
                        print(f"Customer modified: {customer.modified}")
                        print(f"Customer name: {customer.name.first}, {customer.name.last}")
                        print(f"Customer company: {customer.company}")
                        print(f"Customer email: {customer.email}")
                        print(f"Customer homepage: {customer.homepage}")
                        for x in range(0, len(customer.phoneNumbers)):
                            print(f"Customer Phone ID: {customer.phoneNumbers[x].id}")
                            print(f"Customer main: {customer.phoneNumbers[x].main}")
                            print(f"Customer type: {customer.phoneNumbers[x].type}")
                            print(f"Customer list_order: {customer.phoneNumbers[x].list_order}")
                            print(f"Customer number: {customer.phoneNumbers[x].number}")
                        print(f"Customer Is Company: {customer.is_company}")
                        print(f"Customer Is Billing address1: {customer.billing.address1}")
                        print(f"Customer Is Billing address2: {customer.billing.address2}")
                        print(f"Customer Is Billing city: {customer.billing.city}")
                        print(f"Customer Is Billing state: {customer.billing.state}")
                        print(f"Customer Is Billing country: {customer.billing.country}")
                        print(f"Customer Is Billing zip: {customer.billing.zip}")
                        print(f"Customer Is Shipping address1: {customer.shipping.address1}")
                        print(f"Customer Is Shipping address2: {customer.shipping.address2}")
                        print(f"Customer Is Shipping city: {customer.shipping.city}")
                        print(f"Customer Is Shipping state: {customer.shipping.state}")
                        print(f"Customer Is Shipping country: {customer.shipping.country}")
                        print(f"Customer Is Shipping zip: {customer.shipping.zip}")
                        print(f"Customer credit hold: {customer.credit_hold}")
                        print(f"Customer new import: {customer.new_import}")
                        print(f"Customer new update: {customer.new_update}")
                        print(f"Customer birthday: {customer.birthday}")
                        print(f"Customer credit_limit: {customer.credit_limit}")
                        print(f"Customer Customer ID: {customer.customer_id}")
                    case 2:
                        #customer 6
                        min = int(input("Min: "))
                        max = int(input("Max: "))
                        for x in range(min,max):
                            try:
                                customer = repo.get_customer(x)
                                customers.append(customer)
                            except AssertionError as msg:
                                pass
                        print(len(customers))
                    case 3:
                        #customers I can upload 1-136 & 139
                        if len(customers) != 0:
                            for x in customers:
                                print(f"Name: {x.name.first} {x.name.last}")

                        else:
                            print("No Records Found!!")
                    case 4:
                        if len(customers) != 0:
                            repo.importToDB(customers)
                            customers = []
                        else:
                            print("No Records Found!!")
                    case 5:
                        flag2 = False
                    case unknown_command:
                        print("Error")
        case 2:
            repo = ProductRepository()
            print(repo.get_all_product())
            products = []
            flag2 = True
            while flag2:
                choiceP = int(input("Welcome to Product 1-Get Product 2-Get All Product 3-List All Products 4-Import Products to DB 5-Get All Classes 6-Get All Currencies 7-Get Product_Inventory 8-Exit: "))
                match choiceP:
                    case 1:
                        num = int(input("Enter ID: "))
                        product = repo.get_product(num)
                        print(f"Product ID: {product.id}")
                        print(f"Product Class ID: {product.class_id}")
                        print(f"Product Currency ID: {product.currency_id}")
                        print(f"Product Code: {product.code}")
                        print(f"Product Costs cost: {product.costs.cost}")
                        print(f"Product Costs average: {product.costs.average}")
                        print(f"Product Costs raw: {product.costs.raw}")
                        for x in range(0,len(product.supplier_costs)):
                            print(f"Product Supplier Costs ID: {product.supplier_costs[x].id}")
                            print(f"Product Supplier Costs raw: {product.supplier_costs[x].raw}")
                            print(f"Product Supplier Costs Currency_ID: {product.supplier_costs[x].currency_id}")
                            print(f"Product Supplier Costs Currency ID: {product.supplier_costs[x].currency.id}")
                            print(f"Product Supplier Costs Currency name: {product.supplier_costs[x].currency.name}")
                            print(f"Product Supplier Costs Currency rate: {product.supplier_costs[x].currency.rate}")
                            print(f"Product Supplier Costs Currency symbol: {product.supplier_costs[x].currency.symbol}")
                            print(f"Product Supplier Costs cost: {product.supplier_costs[x].cost}")
                            print(f"Product Supplier Costs supplier: {product.supplier_costs[x].supplier}")
                            print(f"Product Supplier Costs supplier product code: {product.supplier_costs[x].supplier_product_code}")
                            print(f"Product Supplier Costs default: {product.supplier_costs[x].default}")
                        print(f"Product Flags current: {product.flags.current}")
                        print(f"Product Flags editable: {product.flags.editable}")
                        print(f"Product Flags gift card: {product.flags.gift_card}")
                        print(f"Product Flags inventoried: {product.flags.inventoried}")
                        print(f"Product Flags new cost: {product.flags.new_cost}")
                        print(f"Product Flags new update: {product.flags.new_update}")
                        print(f"Product Flags no live rules: {product.flags.no_live_rules}")
                        print(f"Product Flags no profit: {product.flags.no_profit}")
                        print(f"Product Flags serialized: {product.flags.serialized}")
                        print(f"Product Flags web: {product.flags.web}")
                        print(f"Product Flags editable sell: {product.flags.editable_sell}")
                        print(f"Product Flags master model: {product.flags.master_model}")
                        print(f"Product sell price: {product.sell_price}")
                        if product.pricing_levels is None:
                            print(f"Product pricing level: {product.pricing_levels}")
                        else:
                            for x in range(0,len(product.pricing_levels)):
                                print(f"Product pricing level index: {product.pricing_levels[x].index}")
                                print(f"Product pricing level name: {product.pricing_levels[x].name}")
                                print(f"Product pricing level sell_price: {product.pricing_levels[x].sell_price}")
                        print(f"Product created: {product.created}")
                        print(f"Product modified: {product.modified}")
                        print(f"Product Description short: {product.description.short}")
                        print(f"Product Description text: {product.description.text}")
                        print(f"Product long web description: {product.long_web_description}")
                        print(f"Product family: {product.family}")
                        print(f"Product GL Product asset: {product.gl_product.asset}")
                        print(f"Product GL Product cogs expense: {product.gl_product.cogs_expense}")
                        print(f"Product GL Product income: {product.gl_product.income}")
                        print(f"Product GL Product payable expense: {product.gl_product.payable_expense}")
                        print(f"Product Product ID: {product.product_id}")
                        print(f"Product import id: {product.import_id}")
                        print(f"Product Inventory available: {product.inventory.available}")
                        print(f"Product Inventory reserved: {product.inventory.reserved}")
                        print(f"Product Inventory coming for stock: {product.inventory.coming_for_stock}")
                        print(f"Product Inventory coming for customer: {product.inventory.coming_for_customer}")
                        print(f"Product Inventory warehouses: {product.inventory.warehouses}")
                        print(f"Product Inventory in transit: {product.inventory.in_transit}")
                        print(f"Product Inventory total: {product.inventory.total}")
                        print(f"Product margin: {product.margin}")
                        print(f"Product minimum margin: {product.minimum_margin}")
                        print(f"Product notes: {product.notes}")
                        print(f"Product Product Info color: {product.product_info.color}")
                        print(f"Product Product Info height: {product.product_info.height}")
                        print(f"Product Product Info length: {product.product_info.length}")
                        print(f"Product Product Info size: {product.product_info.size}")
                        print(f"Product Product Info weight: {product.product_info.weight}")
                        print(f"Product Product Info width: {product.product_info.width}")
                        print(f"Product Reorder amount: {product.reorder.amount}")
                        print(f"Product Reorder calc: {product.reorder.calc}")
                        print(f"Product Reorder point: {product.reorder.point}")
                        print(f"Product Reorder type: {product.reorder.type}")
                        print(f"Product Sells sell: {product.sells.sell}")
                        print(f"Product Sells sell tax inclusive: {product.sells.sell_tax_inclusive}")
                        print(f"Product Sells sell web: {product.sells.sell_web}")
                        print(f"Product supplier: {product.supplier}")
                        print(f"Product supplier code: {product.supplier_code}")
                        print(f"Product upc: {product.upc}")
                        print(f"Product multi store label: {product.multi_store_label}")
                        print(f"Product multi store master label: {product.multi_store_master_label}")
                        print(f"Product serial numbers: {product.serial_numbers}")

                    case 2:
                        #product 1-15038 & 15071-15096
                        min = int(input("Min: "))
                        max = int(input("Max: "))
                        for x in range(min, max):
                            try:
                                print(x)
                                product = repo.get_product(x)
                                products.append(product)
                            except AssertionError as msg:
                                print(msg)
                        print(len(products))
                    case 3:
                        if len(products) != 0:
                            for x in products:
                                print(f"Product Code: {x.code}")
                        else:
                            print("No Records Found!!")
                    case 4:
                        if len(products) != 0:
                            repo.import_to_db(products)
                            products = []
                        else:
                            print("No Records Found!!!")
                    case 5:
                        total_count = int(repo.get_all_classes())+1
                        classes = []
                        flag3 = True
                        while flag3:
                            choice = int(input("1-Get Class 2-Get All Classes 3-Import to DB 4-Exit: "))
                            match choice:
                                case 1:
                                    class_id = int(input("Class ID: "))
                                    print(repo.get_class(class_id).name)
                                case 2:
                                    for x in range(1,total_count):
                                        print(x)
                                        clas = repo.get_class(x)
                                        classes.append(clas)
                                    print(len(classes))
                                case 3:
                                    if len(classes) != 0:
                                        repo.import_to_db_classtbl(classes)
                                        classes = []
                                    else:
                                        print("No Records Found!!!")
                                case 4:
                                    flag3 = False
                                case unknown_command:
                                    print("Error")
                    case 6:
                        total_count = int(repo.get_all_currencies())+1
                        currencies = []
                        flag3 = True
                        while flag3:
                            choice = int(input("1-Get Currency 2-Get All Currencies 3-Import to DB 4-Exit: "))
                            match choice:
                                case 1:
                                    currency_id = int(input("Currency ID: "))
                                    print(repo.get_currency(currency_id).name)
                                case 2:
                                    for x in range(1,total_count):
                                        print(x)
                                        currency = repo.get_currency(x)
                                        currencies.append(currency)
                                    print(len(currencies))
                                case 3:
                                    if len(currencies) != 0:
                                        repo.import_to_db_currencytbl(currencies)
                                        currencies = []
                                    else:
                                        print("No Records Found!!!")
                                case 4:
                                    flag3 = False
                                case unknown_command:
                                    print("Error")
                    case 7:
                        product_inventories = []
                        flag3 = True
                        while flag3:
                            choice = int(input("1-Get Product Inventory 2-Get All Product Inventory 3-Import to DB 4-Exit: "))
                            match choice:
                                case 1:
                                    product_id = int(input("Product ID: "))
                                    print(repo.get_product_inventory(product_id).id)
                                case 2:
                                    # product 1-15038 & 15071-15096
                                    min = int(input("Min: "))
                                    max = int(input("Max: "))
                                    for x in range(min, max):
                                        try:
                                            print(x)
                                            product_inventory = repo.get_product_inventory(x)
                                            product_inventories.append(product_inventory)
                                        except AssertionError as msg:
                                            print(msg)
                                    print(len(product_inventories))
                                case 3:
                                    if len(product_inventories) != 0:
                                        repo.import_to_db_inventorytbl(product_inventories)
                                        product_inventories = []
                                    else:
                                        print("No Records Found!!!")
                                case 4:
                                    flag3 = False
                                case unknown_command:
                                    print("Error")
                    case 8:
                        flag2=False
                    case unknown_command:
                        print("Error")

        case 3:
            repo = InvoiceRepository()
            print(repo.get_all_customer())
            invoices = []
            flag2 = True
            while flag2:
                choice = int(input("Welcome to Invoice 1-Get Invoice 2-Get All Invoice 3-List All Invoices 4-Import Invoices to DB 5-Exit: "))
                match choice:
                    case 1:
                        invoice_id = int(input("Invoice ID: "))
                        invoice = repo.get_invoice(invoice_id)
                        print(f"Invoice ID: {invoice.id}")
                        print(f"Invoice Document ID: {invoice.document_id}")
                        print(f"Invoice date created: {invoice.date_created}")
                        print(f"Invoice datetime created: {invoice.datetime_created}")
                        print(f"Invoice date modified: {invoice.date_modified}")
                        print(f"Invoice storecode: {invoice.storecode}")
                        print(f"Invoice invoice id: {invoice.invoice_id}")
                        print(f"Invoice customer id: {invoice.customer_id}")
                        print(f"Invoice margin: {invoice.margin}")
                        print(f"Invoice primary user id: {invoice.primary_user_id}")
                        print(f"Invoice secondary user id: {invoice.secondary_user_id}")
                        print(f"Invoice printed notes: {invoice.printed_notes}")
                        print(f"Invoice internal notes: {invoice.internal_notes}")
                        print(f"Invoice currency id: {invoice.currency_id}")
                        print(f"Invoice terms: {invoice.terms}")
                        print(f"Invoice due: {invoice.due}")
                        print(f"Invoice import id: {invoice.import_id}")
                        print(f"Invoice status: {invoice.status}")
                        print(f"Invoice pricing level: {invoice.pricing_level}")
                        print(f"Invoice c discount percentage: {invoice.c_discount_percentage}")
                        if invoice.payments is not None:
                            for x in invoice.payments:
                                print(f"Invoice Payment ID: {x.id}")
                                print(f"Invoice Payment type: {x.type}")
                                print(f"Invoice Payment payment method: {x.payment_method}")
                                print(f"Invoice Payment datetime created: {x.datetime_created}")
                                print(f"Invoice Payment datetime modified: {x.datetime_modified}")
                                print(f"Invoice Payment exported: {x.exported}")
                                print(f"Invoice Payment posted: {x.posted}")
                                print(f"Invoice Payment Flags exported: {x.flags.exported}")
                                print(f"Invoice Payment Flags posted: {x.flags.posted}")
                                print(f"Invoice Payment Flags voided: {x.flags.voided}")
                                print(f"Invoice Payment number: {x.number}")
                                print(f"Invoice Payment amount: {x.amount}")
                                print(f"Invoice Payment tendered: {x.tendered}")
                                print(f"Invoice Payment authcode: {x.authcode}")
                                print(f"Invoice Payment avs_result: {x.avs_result}")
                                print(f"Invoice Payment till: {x.till}")
                        else:
                            print(f"Invoice Payment: None")
                        if invoice.lineitems is not None:
                            for x in invoice.lineitems:
                                print(f"Invoice Lineitem ID: {x.id}")
                                print(f"Invoice Lineitem quantity: {x.quantity}")
                                print(f"Invoice Lineitem sell price: {x.sell_price}")
                                print(f"Invoice Lineitem Sells sell: {x.sells.sell}")
                                print(f"Invoice Lineitem Sells base: {x.sells.base}")
                                print(f"Invoice Lineitem Sells total: {x.sells.total}")
                                print(f"Invoice Lineitem Sells sell quantity discount: {x.sells.sell_quantity_discount}")
                                print(f"Invoice Lineitem Sells sell tax inclusive quantity discount: {x.sells.sell_tax_inclusive_quantity_discount}")
                                print(f"Invoice Lineitem Sells sell tax inclusive: {x.sells.sell_tax_inclusive}")
                                print(f"Invoice Lineitem Sells sell tax inclusive total: {x.sells.sell_tax_inclusive_total}")
                                print(f"Invoice Lineitem Sells sell tax inclusive discounted: {x.sells.sell_tax_inclusive_discounted}")
                                print(f"Invoice Lineitem pricing calculations: {x.pricing_calculations}")
                                print(f"Invoice Lineitem Product Product ID: {x.product_product_id}")
                                print(f"Invoice Lineitem quantity backordered: {x.quantity_backordered}")
                        else:
                            print(f"Invoice Lineitems: None")
                        print(f"Invoice Flags drop shipment: {invoice.flags.drop_shipment}")
                        print(f"Invoice Flags exported: {invoice.flags.exported}")
                        print(f"Invoice Flags pay backorders: {invoice.flags.pay_backorders}")
                        print(f"Invoice Flags posted: {invoice.flags.posted}")
                        print(f"Invoice Flags voided: {invoice.flags.voided}")
                        print(f"Invoice Totals cost: {invoice.totals.cost}")
                        print(f"Invoice Totals subtotal: {invoice.totals.subtotal}")
                        print(f"Invoice Totals profit: {invoice.totals.profit}")
                        print(f"Invoice Totals tax: {invoice.totals.tax}")
                        print(f"Invoice Totals total: {invoice.totals.total}")
                        print(f"Invoice Totals owing: {invoice.totals.owing}")
                        print(f"Invoice Totals paid: {invoice.totals.paid}")
                        print(f"Invoice Totals total backordered: {invoice.totals.total_backordered}")
                        print(f"Invoice Totals remaining balance: {invoice.totals.remaining_balance}")
                        if invoice.source is not None:
                            for source in invoice.source:
                                print(f"Invoice Source ID: {source.id}")
                        else:
                            print(f"Invoice Source ID: None")
                        if invoice.returned_invoice is not None:
                            for inv in invoice.returned_invoice:
                                print(f"Invoice Returned Invoice: {inv.id}")
                        else:
                            print("Invoice Returned Invoice: None")
                        print(f"Invoice cc info: {invoice.cc_info}")
                        print(f"Invoice exported: {invoice.exported}")
                        print(f"Invoice posted: {invoice.posted}")
                        print(f"Invoice station: {invoice.station}")
                    case 2:
                        #can get upto 1-272 & 305-404
                        min = int(input("Min: "))
                        max = int(input("Max: "))
                        for x in range(min, max):
                            try:
                                print(x)
                                invoice = repo.get_invoice(x)
                                invoices.append(invoice)
                            except AssertionError as msg:
                                print(msg)
                        print(len(invoices))
                    case 3:
                        pass
                    case 4:
                        #insert 2 onwards
                        if len(invoices) != 0:
                            repo.import_to_invoice_table(invoices)
                            invoices = []
                        else:
                            print("No Records Found!!!")
                    case 5:
                        flag2 = False
                    case unknown_command:
                        print("Error")
        case 4:
            repo = OrderRepository()
            print(repo.get_all_orders())
            orders = []
            flag2 = True
            while flag2:
                choice = int(input("Welcome to Order 1-Get Order 2-Get All Order 3-List All Orders 4-Import Orders to DB 5-Exit: "))
                match choice:
                    case 1:
                        order_id = int(input("Order ID: "))
                        order = repo.get_order(order_id)
                        print(f"Order ID: {order.id}")
                        print(f"Order Document ID: {order.document_id}")
                        print(f"Order date created: {order.date_created}")
                        print(f"Order datetime created: {order.datetime_created}")
                        print(f"Order date modified: {order.date_modified}")
                        print(f"Order datetime modified: {order.datetime_modified}")
                        print(f"Order storecode: {order.storecode}")
                        print(f"Order Order ID: {order.order_id}")
                        print(f"Order Customer ID: {order.customer_id}")
                        print(f"Order margin: {order.margin}")
                        print(f"Order primary user ID: {order.primary_user_id}")
                        print(f"Order secondary user ID: {order.secondary_user_id}")
                        print(f"Order printed notes: {order.printed_notes}")
                        print(f"Order internal notes: {order.internal_notes}")
                        print(f"Order currency ID: {order.currency_id}")
                        print(f"Order terms: {order.terms}")
                        print(f"Order due: {order.due}")
                        print(f"Order import ID: {order.import_id}")
                        print(f"Order status: {order.status}")
                        print(f"Order pricing level: {order.pricing_level}")
                        print(f"Order c discount percentage: {order.c_discount_percentage}")
                        if order.payments is not None:
                            for x in order.payments:
                                print(f"Order Payment ID: {x.id}")
                                print(f"Order Payment type: {x.type}")
                                print(f"Order Payment payment method: {x.payment_method}")
                                print(f"Order Payment datetime created: {x.datetime_created}")
                                print(f"Order Payment datetime modified: {x.datetime_modified}")
                                print(f"Order Payment exported: {x.exported}")
                                print(f"Order Payment posted: {x.posted}")
                                print(f"Order Payment Flags exported: {x.flags.exported}")
                                print(f"Order Payment Flags posted: {x.flags.posted}")
                                print(f"Order Payment Flags voided: {x.flags.voided}")
                                print(f"Order Payment number: {x.number}")
                                print(f"Order Payment amount: {x.amount}")
                                print(f"Order Payment tendered: {x.tendered}")
                                print(f"Order Payment authcode: {x.authcode}")
                                print(f"Order Payment avs_result: {x.avs_result}")
                                print(f"Order Payment till: {x.till}")
                        else:
                            print(f"Order Payment: None")
                        if order.lineitems is not None:
                            for x in order.lineitems:
                                print(f"Order Lineitem ID: {x.id}")
                                print(f"Order Lineitem quantity: {x.quantity}")
                                print(f"Order Lineitem sell price: {x.sell_price}")
                                print(f"Order Lineitem Sells sell: {x.sells.sell}")
                                print(f"Order Lineitem Sells base: {x.sells.base}")
                                print(f"Order Lineitem Sells total: {x.sells.total}")
                                print(f"Order Lineitem Sells sell quantity discount: {x.sells.sell_quantity_discount}")
                                print(f"Order Lineitem Sells sell tax inclusive quantity discount: {x.sells.sell_tax_inclusive_quantity_discount}")
                                print(f"Order Lineitem Sells sell tax inclusive: {x.sells.sell_tax_inclusive}")
                                print(f"Order Lineitem Sells sell tax inclusive total: {x.sells.sell_tax_inclusive_total}")
                                print(f"Order Lineitem Sells sell tax inclusive discounted: {x.sells.sell_tax_inclusive_discounted}")
                                print(f"Order Lineitem pricing calculations: {x.pricing_calculations}")
                                print(f"Order Lineitem Product Product ID: {x.product_product_id}")
                        else:
                            print(f"Invoice Lineitems: None")
                        print(f"Order Flags drop shipment: {order.flags.drop_shipment}")
                        print(f"Order Totals cost: {order.totals.cost}")
                        print(f"Order Totals subtotal: {order.totals.subtotal}")
                        print(f"Order Totals profit: {order.totals.profit}")
                        print(f"Order Totals tax: {order.totals.tax}")
                        print(f"Order Totals credit: {order.totals.credit}")
                        print(f"Order Totals total: {order.totals.total}")
                        print(f"Order Totals paid: {order.totals.paid}")
                        print(f"Order Totals remaining balance: {order.totals.remaining_balance}")
                        print(f"Order web order number: {order.web_order_number}")
                        print(f"Order order type: {order.order_type}")
                    case 2:
                        #can get 1-35 & 37-75
                        min = int(input("Min: "))
                        max = int(input("Max: "))
                        for x in range(min, max):
                            try:
                                print(x)
                                order = repo.get_order(x)
                                orders.append(order)
                            except AssertionError as msg:
                                print(msg)
                        print(len(orders))
                    case 3:
                        pass
                    case 4:
                        if len(orders) != 0:
                            repo.import_to_order_table(orders)
                            orders = []
                        else:
                            print("No Records Found!!!")
                    case 5:
                        flag2 = False
                    case unknown_command:
                        print("Error")
        case 5:
            repo = UserRepository()
            users_id = repo.get_all_users()
            users = []
            flag2 = True
            while flag2:
                choice = int(input("Welcome to User 1-Get User 2-Get All User 3-List All Users 4-Import Users to DB 5-Exit: "))
                match choice:
                    case 1:
                        user_id = int(input("User ID: "))
                        user = repo.get_user(user_id)
                    case 2:
                        if users_id is not None:
                            for user_id in users_id:
                                user = repo.get_user(int(user_id))
                                users.append(user)
                            print(len(users))
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        flag2 = False
                    case unknown_command:
                        print("Error")
        case 6:
            flag = False
        case unknown_command:
            print("Error")