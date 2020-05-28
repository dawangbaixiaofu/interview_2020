# 对订单表按照客户编码和签约日期进行升序排序，方便后续表格处理使用

with order_temp_sort as 
(select 
客户编号,签约日期
from order_test_201909 
order by 客户编号,签约日期)

#统计客户是否购买
, is_purchase as
(select 客户编号,count(组合名称) 购买次数
from order_test_201909
group by 客户编号
)
# 找到签约日期的前一个相邻签约日期，没有为''
, order_processed as (
select base.客户编号,base.签约日期,before_date
from (
select 
if(@kehu=t.客户编号,@lagdate:=@origin_date,@lagdate:='') as before_date,
(@kehu:=t.客户编号) as tkehu,
(@origin_date:=t.签约日期) as tdate,
t.*
from order_temp_sort t ,
(select @kehu:=0,@lagdate:=null,@origin_date:=null) r
) base)

#统计在每次签约时间前用户点击事件次数 
,event_visit_num as 
(
select a.客户编号,a.签约日期,b.事件名称,
sum(case when a.before_date = '' and b.事件发生时间<a.签约日期 then 1
		 when a.before_date != '' and b.事件发生时间>=a.before_date and b.事件发生时间<a.签约日期 then 1 
         else 0 end) event_visit_num
from order_processed a
left join event_visit_test_201909 b
on a.客户编号 = b.客户编号
group by a.客户编号,a.签约日期,b.事件名称
order by a.客户编号,a.签约日期,b.事件名称
)

#点击事件次数行列转置
,event_visit_transform as 
(
select 客户编号,
sum(case when 事件名称 = '关注投顾' then event_visit_num else 0 end) as 关注投顾,
sum(case when 事件名称 = '签约投顾' then event_visit_num else 0 end) as 签约投顾,
sum(case when 事件名称 = 'IM联系投顾' then event_visit_num else 0 end) as IM联系投顾,
sum(case when 事件名称 = '组合详情页点击调仓历史' then event_visit_num else 0 end) as 组合详情页点击调仓历史,
sum(case when 事件名称 = '投顾业务适当性匹配' then event_visit_num else 0 end) as 投顾业务适当性匹配,
sum(case when 事件名称 = '关注组合' then event_visit_num else 0 end) as 关注组合,
sum(case when 事件名称 = '投顾观点活跃' then event_visit_num else 0 end) as 投顾观点活跃
from event_visit_num 
group by 客户编号)

#统计在每次签约时间前用户页面访问次数
, page_visit_num as
(
select a.客户编号,a.签约日期,b.访问的页面,
sum(case when a.before_date = '' and b.页面访问时间<a.签约日期 then 1
		 when a.before_date != '' and b.页面访问时间>=a.before_date and b.页面访问时间<a.签约日期 then 1 
         else 0 end) page_visit_num
from order_processed a
left join page_visit_test_201909 b
on a.客户编号 = b.客户编号
group by a.客户编号,a.签约日期,b.访问的页面
order by a.客户编号,a.签约日期,b.访问的页面
)
#页面访问次数行列转置
,page_visit_transform as
(
select 客户编号,
sum(case when 访问的页面 = '找投顾' then page_visit_num else 0 end) as 找投顾,
sum(case when 访问的页面 = '选组合' then page_visit_num else 0 end) as 选组合,
sum(case when 访问的页面 = '投顾观点详情页' then page_visit_num else 0 end) as 投顾观点详情页,
sum(case when 访问的页面 = '投顾观点列表' then page_visit_num else 0 end) as 投顾观点列表,
sum(case when 访问的页面 = '投顾个人页' then page_visit_num else 0 end) as 投顾个人页,
sum(case when 访问的页面 = '投顾观点评论页' then page_visit_num else 0 end) as 投顾观点评论页,
sum(case when 访问的页面 = '投顾组合评论页' then page_visit_num else 0 end) as 投顾组合评论页,
sum(case when 访问的页面 = '投顾组合详情页' then page_visit_num else 0 end) as 投顾组合详情页,
sum(case when 访问的页面 = '互联网投顾首页' then page_visit_num else 0 end) as 互联网投顾首页

from page_visit_num 
group by 客户编号
)
#合并表格，形成统计结果
select b.*,c.*,
case when a.购买次数=0 then 0 
	 when a.购买次数>0 then 1 end as 是否购买

from is_purchase a
left join page_visit_transform b
on a.客户编号 = b.客户编号
left join event_visit_transform c
on a.客户编号 = c.客户编号
;

-- use test;
-- select count(*) from page_visit_test_201909;



