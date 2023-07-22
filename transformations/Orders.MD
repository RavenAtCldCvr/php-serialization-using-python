Tactics to flatten the hierarchy.
Introduce a correlation_order_id in databrew using the following logic

when is_parent_order = 'N' and Order_Parent_Id=0
set correlation_order_id = order_id

when is_parent_order = 'N' and Order_Parent_Id!=0
set correlation_order_id = Order_Parent_Id

when is_parent_order = 'Y' and Order_Parent_Id=0
set correlation_order_id = order_id

there is no scenarios where is_parent_order = 'Y' and Order_Parent_Id!=0

For Example:
| Is_Parent_Order | Parent_Order_ID | Order_Id | correlation_order_id |
|-----------------|-----------------|----------|----------------------|
| N               | 0               | 43066    | 43066                |
| Y               | 0               | 43068    | 43068                |
| N               | 43068           | 43069    | 43068                |
| N               | 43068           | 43070    | 43068                |

Now we can inner join order_details on order_id and when we need to do perform analysis on 
order size, we can use the correlation_order_id