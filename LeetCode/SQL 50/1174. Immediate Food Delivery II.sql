/* Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places. */

SELECT 
    ROUND(100*SUM(IF(b.min_order_date = b.min_delivery_date,1,0))/COUNT(*), 2)
    AS immediate_percentage
FROM (
    SELECT MIN(order_date) as min_order_date, MIN(customer_pref_delivery_date) as min_delivery_date
  FROM delivery
  GROUP BY customer_id
) b;
