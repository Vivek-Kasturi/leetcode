# Write your MySQL query statement below
select t.request_at as Day,
round(
    sum(
        case
        when t.status in ('cancelled_by_driver','cancelled_by_client')
        then 1 else 0
        end
    )
    /count(*),
    2
)as 'Cancellation Rate'
from Trips t
where t.request_at between '2013-10-01' AND '2013-10-03'
and t.client_id in(
    select users_id
    from users
    where banned='No'
)
and t.driver_id in(
    select users_id
    from users
    where banned='No'
)
group by t.request_at