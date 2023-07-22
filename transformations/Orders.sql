--simple orders
SELECT po.order_id,
	po."ordered_by",
	po."is_mobile_order",
	po."subtotal",
	po."subtotal_discount",
	po."total",
	po."outstanding_amount",
	po."status",
	po."bc_status",
	po."notes",
	po."storefront_id",
	po."company_id",
	po."user_id"
FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
where "parent_order_id" = 0 and is_parent_order='N'
limit 10

--parent orders items breakdown
SELECT po.order_id,
	po."ordered_by",
	po."is_mobile_order",
	po."subtotal",
	po."subtotal_discount",
	po."total",
	po."outstanding_amount",
	po."status",
	po."bc_status",
	po."notes",
	po."storefront_id",
	po."company_id",
	po."user_id",
	od.product_id,
	od.product_code,
	od.amount,
	od."price"
	FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
	inner join "pom_store_prd_cscart_order_details" od on po."order_id" = od.order_id
where "parent_order_id" = 0 and is_parent_order='N'
limit 10

--complex orders
SELECT po.parent_order_id
FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
where is_parent_order='Y' and "parent_order_id" = 0
limit 10

--complex orders and their items
SELECT po.order_id,
	po."ordered_by",
	po."is_mobile_order",
	po."subtotal",
	po."subtotal_discount",
	po."total",
	po."outstanding_amount",
	po."status",
	po."bc_status",
	po."notes",
	po."storefront_id",
	po."company_id",
	po."user_id",
	od.product_id,
	od.product_code,
	od.amount,
	od."price"
	FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
	inner join "pom_store_prd_cscart_order_details" od on po."order_id" = od.order_id
where po.is_parent_order='Y' and po."parent_order_id" = 0
limit 10

--sub orders
SELECT po.parent_order_id
FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
where "parent_order_id" != 0
limit 10

--sub orders and their items
SELECT po.order_id,
	po."ordered_by",
	po."is_mobile_order",
	po."subtotal",
	po."subtotal_discount",
	po."total",
	po."outstanding_amount",
	po."status",
	po."bc_status",
	po."notes",
	po."storefront_id",
	po."company_id",
	po."user_id",
	od.product_id,
	od.product_code,
	od.amount,
	od."price"
	FROM "AwsDataCatalog"."mocked_dashboard_1"."pom_store_prd_cscart_orders" po
	inner join "pom_store_prd_cscart_order_details" od on po."order_id" = od.order_id
where po."parent_order_id" != 0
limit 10

