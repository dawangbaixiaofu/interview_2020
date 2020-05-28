select 
客户编号,签约日期,组合名称
from order_test_201909 
where 客户编号 = '14091020'
order by 客户编号,签约日期;


select *
from event_visit_test_201909
where 客户编号 = '14091020'
and 事件发生时间 >='2019-09-03'
and 事件发生时间 <'2019-09-17'
 ;

select distinct 事件名称 from event_visit_test_201909;
select distinct 访问的页面 from page_visit_test_201909;
select * from order_test_201909 where 客户编号='14091020';

2019-03-26
2019-09-03
2019-04-01
2019-04-17
2019-09-17
select * from page_visit_test_201909
where 客户编号='14091020';


