select customers.customer_id,
customers.cust_name,
customers.occupation,
customers.income,
customers.qualification,
orders.order_id_id,
orders.date1,
orders.price

from customers
left join orders 
on customers.customer_id = orders.cust_id;