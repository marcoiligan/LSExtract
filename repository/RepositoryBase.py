import mysql.connector as conn
from repository.config import Config


class RepositoryBase:

    def __init__(self):
        conf = Config()
        self.con = conn.connect(host=conf.host, database=conf.database, user=conf.user, password=conf.password)
        if self.con.is_connected():
            print("Connection Successful!!!")
        else:
            print("Connection Failed!!!")

    def insert_to_customer_table(self, customer):
        #Insert to Customer Table
        query_insert = "INSERT INTO Customer (id, created, modified, company, email, homepage, is_company, credit_hold, new_import, new_update, birthday, credit_limit, customer_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (customer.id,customer.created,customer.modified,customer.company,customer.email,customer.homepage,customer.is_company,customer.credit_hold,customer.new_import,customer.new_update,customer.birthday,customer.credit_limit,customer.customer_id)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Name Table
        query_insert = "INSERT INTO Name (customer_id,first,last) VALUES (%s,%s,%s);"
        val = (customer.customer_id,customer.name.first,customer.name.last)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to PhoneNumber Table
        for x in range(0, len(customer.phoneNumbers)):
            query_insert = "INSERT INTO PhoneNumber(customer_id,id,main,type,list_order,number) VALUES(%s,%s,%s,%s,%s,%s);"
            val = (customer.customer_id,customer.phoneNumbers[x].id,customer.phoneNumbers[x].main,customer.phoneNumbers[x].type,customer.phoneNumbers[x].list_order,customer.phoneNumbers[x].number)
            cur = self.con.cursor()
            cur.execute(query_insert, val)
            self.con.commit()
        #Insert to Billing Table
        query_insert = "INSERT INTO Billing(customer_id,address1,address2,city,state,country,zip) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val = (customer.customer_id,customer.billing.address1,customer.billing.address2,customer.billing.city,customer.billing.state,customer.billing.country,customer.billing.zip)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Shipping Table
        query_insert = "INSERT INTO Shipping(customer_id,address1,address2,city,state,country,zip) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val = (customer.customer_id,customer.shipping.address1,customer.shipping.address2,customer.shipping.city,customer.shipping.state,customer.shipping.country,customer.shipping.zip)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted!!!")

    def insert_to_product_table(self, product):
        #Insert to Product Table
        query_insert = "INSERT INTO Product (id, class_id, currency_id, code,sell_price,created,modified,long_web_description,family,product_id,import_id,margin,minimum_margin,notes,supplier,supplier_code,upc,multi_store_label,multi_store_master_label,serial_numbers) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (product.id,product.class_id,product.currency_id,product.code,product.sell_price,product.created,product.modified,product.long_web_description,product.family,product.product_id,product.import_id,product.margin,product.minimum_margin,product.notes,product.supplier,product.supplier_code,product.upc,product.multi_store_label,product.multi_store_master_label,product.serial_numbers)
        cur = self.con.cursor()
        cur.execute(query_insert,val)
        self.con.commit()
        #Insert to Costs Table
        query_insert = "INSERT INTO Costs(product_id,cost,average,raw) VALUES(%s,%s,%s,%s);"
        val = (product.product_id,product.costs.cost,product.costs.average,product.costs.raw)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Supplier_Cost Table
        if product.supplier_costs is not None:
            for x in range(0, len(product.supplier_costs)):
                query_insert = "INSERT INTO Supplier_Cost(product_id, id, raw, currency_id, cost, supplier, supplier_product_code, is_default) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
                val = (product.product_id,product.supplier_costs[x].id,product.supplier_costs[x].raw,product.supplier_costs[x].currency_id,product.supplier_costs[x].cost,product.supplier_costs[x].supplier,product.supplier_costs[x].supplier_product_code,product.supplier_costs[x].default)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
                """query_insert = "INSERT INTO Currency(supplier_cost_id,id,name,rate,symbol) VALUES(%s,%s,%s,%s,%s)"
                val = (product.supplier_costs[x].id,product.supplier_costs[x].currency.id,product.supplier_costs[x].currency.name,product.supplier_costs[x].currency.rate,product.supplier_costs[x].currency.symbol)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()"""
        #Insert to Pricing_Level Table
        if product.pricing_levels is not None:
            for x in range(0,len(product.pricing_levels)):
                query_insert = "INSERT INTO Pricing_Level(product_id,pl_index,name,sell_price) VALUES(%s,%s,%s,%s);"
                val = (product.product_id,product.pricing_levels[x].index,product.pricing_levels[x].name,product.pricing_levels[x].sell_price)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Flags Table
        query_insert = "INSERT INTO FLags(product_id,current,editable,gift_card,inventoried,new_cost,new_update,no_live_rules,no_profit,serialized,web,editable_sell,master_model) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (product.product_id,product.flags.current,product.flags.editable,product.flags.gift_card,product.flags.inventoried,product.flags.new_cost,product.flags.new_update,product.flags.no_live_rules,product.flags.no_profit,product.flags.serialized,product.flags.web,product.flags.editable_sell,product.flags.master_model)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Description Table
        query_insert = "INSERT INTO Description(product_id, short, desc_text) VALUES(%s,%s,%s);"
        val = (product.product_id,product.description.short,product.description.text)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to GL_Product Table
        query_insert = "INSERT INTO GL_Product(product_id,asset,cogs_expense,income,payable_expense) VALUES(%s,%s,%s,%s,%s);"
        val = (product.product_id, product.gl_product.asset,product.gl_product.cogs_expense,product.gl_product.income,product.gl_product.payable_expense)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Product_Info Table
        query_insert = "INSERT INTO Product_Info(product_id,color,height,length,size,weight,width) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        val = (product.product_id,product.product_info.color,product.product_info.height,product.product_info.length,product.product_info.size,product.product_info.weight,product.product_info.width)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Reorder Table
        query_insert = "INSERT INTO Reorder(product_id,amount,calc,point,type) VALUES(%s,%s,%s,%s,%s);"
        val = (product.product_id,product.reorder.amount,product.reorder.calc,product.reorder.point,product.reorder.type)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Sells Table
        query_insert = "INSERT INTO Sells(product_id,sell,sell_tax_inclusive,sell_web) VALUES(%s,%s,%s,%s);"
        val = (product.product_id,product.sells.sell,product.sells.sell_tax_inclusive,product.sells.sell_web)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")

    def insert_to_classes(self, classes):
        query_insert = "INSERT INTO Classes(id, name) VALUES(%s, %s);"
        val = (classes.id,classes.name)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")

    def insert_to_currencies(self, currency):
        query_insert = "INSERT INTO Currency(id, name, rate, symbol) VALUES(%s,%s,%s,%s);"
        val = (currency.id,currency.name,currency.rate,currency.symbol)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")

    def insert_to_invoice_table(self, invoice):
        #Insert to Invoice Table
        query_insert = "INSERT INTO Invoice(id, document_id, date_created, datetime_created, date_modified, datetime_modified, storecode, invoice_id, customer_id, margin, primary_user_id, secondary_user_id, printed_notes, internal_notes, currency_id, terms, due, import_id, status, pricing_level, c_discount_percentage, cc_info, exported, posted, station) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (invoice.id, invoice.document_id, invoice.date_created, invoice.datetime_created, invoice.date_modified, invoice.datetime_modified, invoice.storecode, invoice.invoice_id, invoice.customer_id, invoice.margin, invoice.primary_user_id, invoice.secondary_user_id, invoice.printed_notes, invoice.internal_notes, invoice.currency_id, invoice.terms, invoice.due, invoice.import_id, invoice.status, invoice.pricing_level, invoice.c_discount_percentage, invoice.cc_info, invoice.exported, invoice.posted, invoice.station)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Payment Table
        if invoice.payments is not None:
            for payment in invoice.payments:
                query_insert = "INSERT INTO Invoice_Payment(invoice_id, id, type, payment_method, datetime_created, datetime_modified, exported, posted, number, amount, tendered, authcode, avs_result, till) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val = (invoice.invoice_id, payment.id, payment.type, payment.payment_method, payment.datetime_created, payment.datetime_modified, payment.exported, payment.posted, payment.number, payment.amount, payment.tendered, payment.authcode, payment.avs_result, payment.till)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
                #Insert to Payment Flags Tbl
                query_insert = "INSERT INTO Payment_Flags(payment_id, exported, posted, voided) VALUES(%s,%s,%s,%s);"
                val = (payment.id, payment.flags.exported, payment.flags.posted, payment.flags.voided)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Lineitem Table
        if invoice.lineitems is not None:
            for lineitem in invoice.lineitems:
                query_insert = "INSERT INTO Invoice_Lineitem(invoice_id, id, quantity, sell_price, pricing_calculations, product_product_id, quantity_backordered) VALUES(%s,%s,%s,%s,%s,%s,%s);"
                val = (invoice.invoice_id, lineitem.id, lineitem.quantity, lineitem.sell_price, lineitem.pricing_calculations, lineitem.product_product_id, lineitem.quantity_backordered)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
                #Insert to Lineitem Sells Table
                query_insert = "INSERT INTO Lineitem_Sells(lineitem_id, sell, base, total, sell_quantity_discount, sell_tax_inclusive_quantity_discount, sell_tax_inclusive, sell_tax_inclusive_total, sell_tax_inclusive_discounted) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val = (lineitem.id, lineitem.sells.sell, lineitem.sells.base, lineitem.sells.total, lineitem.sells.sell_quantity_discount, lineitem.sells.sell_tax_inclusive_quantity_discount, lineitem.sells.sell_tax_inclusive, lineitem.sells.sell_tax_inclusive_total, lineitem.sells.sell_tax_inclusive_discounted)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Invoice Flags Table
        query_insert = "INSERT INTO Invoice_Flags(invoice_id, drop_shipment, exported, pay_backorders, posted, voided) VALUES(%s,%s,%s,%s,%s,%s);"
        val = (invoice.invoice_id, invoice.flags.drop_shipment, invoice.flags.exported, invoice.flags.pay_backorders, invoice.flags.posted, invoice.flags.voided)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Invoice Totals Table
        query_insert = "INSERT INTO Invoice_Totals(invoice_id, cost, subtotal, profit, tax, total, owing, paid, total_backordered, remaining_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (invoice.invoice_id, invoice.totals.cost, invoice.totals.subtotal, invoice.totals.profit, invoice.totals.tax, invoice.totals.total, invoice.totals.owing, invoice.totals.paid, invoice.totals.total_backordered, invoice.totals.remaining_balance)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Invoice Source Table
        if invoice.source is not None:
            for source in invoice.source:
                query_insert = "INSERT INTO Invoice_Source(invoice_id, id) VALUES(%s,%s);"
                val = (invoice.invoice_id, source.id)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Invoice Returned Invoice Table
        if invoice.returned_invoice is not None:
            for inv in invoice.returned_invoice:
                query_insert = "INSERT INTO Returned_Invoice(invoice_id, id) VALUES(%s,%s);"
                val = (invoice.invoice_id, inv.id)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        print("Inserted")

    def insert_to_order_table(self, order):
        # Insert to Order Table
        query_insert = "INSERT INTO OrderTbl(id, document_id, date_created, datetime_created, date_modified, datetime_modified, storecode, order_id, customer_id, margin, primary_user_id, secondary_user_id, printed_notes, internal_notes, currency_id, terms, due, import_id, status, pricing_level, c_discount_percentage, web_order_number, order_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (order.id, order.document_id, order.date_created, order.datetime_created, order.date_modified,
               order.datetime_modified, order.storecode, order.order_id, order.customer_id, order.margin,
               order.primary_user_id, order.secondary_user_id, order.printed_notes, order.internal_notes,
               order.currency_id, order.terms, order.due, order.import_id, order.status,
               order.pricing_level, order.c_discount_percentage, order.web_order_number, order.order_type)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        # Insert to Payment Table
        if order.payments is not None:
            for payment in order.payments:
                query_insert = "INSERT INTO Order_Payments(order_id, id, type, payment_method, datetime_created, datetime_modified, exported, posted, number, amount, tendered, authcode, avs_result, till) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val = (order.order_id, payment.id, payment.type, payment.payment_method, payment.datetime_created,
                       payment.datetime_modified, payment.exported, payment.posted, payment.number, payment.amount,
                       payment.tendered, payment.authcode, payment.avs_result, payment.till)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
                # Insert to Payment Flags Tbl
                query_insert = "INSERT INTO Order_Payment_Flags(payment_id, exported, posted, voided) VALUES(%s,%s,%s,%s);"
                val = (payment.id, payment.flags.exported, payment.flags.posted, payment.flags.voided)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Lineitem Table
        if order.lineitems is not None:
            for lineitem in order.lineitems:
                query_insert = "INSERT INTO Order_Lineitem(order_id, id, quantity, sell_price, pricing_calculations, product_product_id) VALUES(%s,%s,%s,%s,%s,%s);"
                val = (order.order_id, lineitem.id, lineitem.quantity, lineitem.sell_price, lineitem.pricing_calculations, lineitem.product_product_id)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
                #Insert to Lineitem Sells Table
                query_insert = "INSERT INTO Order_Lineitem_Sells(lineitem_id, sell, base, total, sell_quantity_discount, sell_tax_inclusive_quantity_discount, sell_tax_inclusive, sell_tax_inclusive_total, sell_tax_inclusive_discounted) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                val = (lineitem.id, lineitem.sells.sell, lineitem.sells.base, lineitem.sells.total, lineitem.sells.sell_quantity_discount, lineitem.sells.sell_tax_inclusive_quantity_discount, lineitem.sells.sell_tax_inclusive, lineitem.sells.sell_tax_inclusive_total, lineitem.sells.sell_tax_inclusive_discounted)
                cur = self.con.cursor()
                cur.execute(query_insert, val)
                self.con.commit()
        #Insert to Order Flags Table
        query_insert = "INSERT INTO Order_Flags(order_id, drop_shipment) VALUES(%s,%s);"
        val = (order.order_id,order.flags.drop_shipment)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to Order Totals Table
        query_insert = "INSERT INTO Order_Totals(order_id, cost, subtotal, profit, tax, credit, total, paid, remaining_balance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (order.order_id, order.totals.cost, order.totals.subtotal, order.totals.profit, order.totals.tax, order.totals.credit, order.totals.total, order.totals.paid, order.totals.remaining_balance)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")


    def insert_to_inventory_table(self, inventory):
        query_insert = "INSERT INTO Product_Inventory(id, available, reserved, coming_for_stock, coming_for_customer, warehouses, in_transit, total, product_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (inventory.id,inventory.available,inventory.reserved,inventory.coming_for_stock,inventory.coming_for_customer,inventory.warehouses,inventory.in_transit,inventory.total,inventory.product_id)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")

    def insert_to_user_table(self, user):
        query_insert = "INSERT INTO User(id,username,password,pin,email,account_locked,privilege,read_eula,hidden,enabled,phone,product,product_code,open_to_pos,gsx_apple_id,gsx_tech_id,can_open_from_otr,can_discount,internal_user,active,expired,display_welcome) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (user.id,user.username,user.password,user.pin,user.email,user.account_locked,user.privilege_id,user.read_eula,user.hidden,user.enabled,user.phone,user.product,user.product_code,user.open_to_pos,user.gsx_apple_id,user.gsx_tech_id,user.can_open_from_otr,user.can_discount,user.internal_user,user.active,user.expired,user.display_welcome)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        #Insert to User Name table
        query_insert = "INSERT INTO User_Name(user_id, first, last) VALUES(%s,%s,%s);"
        val = (user.id,user.name.first,user.name.last)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")

    def insert_to_privilege_groups_table(self, privilege_group):
        query_insert = "INSERT INTO Privilege_Groups(id, name, type) VALUES(%s,%s,%s);"
        val = (privilege_group.id, privilege_group.name, privilege_group.type)
        cur = self.con.cursor()
        cur.execute(query_insert, val)
        self.con.commit()
        print("Inserted")