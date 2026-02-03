# Write your MySQL query statement below
with salary_ranks as(    
    select name, departmentId, salary,
    rank() over (partition by departmentId order by salary desc) as sal_rank
    from employee
)
select d.name as Department,
sr.name as Employee,
sr.salary
 from salary_ranks sr
left join Department d on d.id=sr.departmentId
where sal_rank=1