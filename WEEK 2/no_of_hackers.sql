SET @rownum=0;
select x.submission_date, (select count(distinct ls.hacker_id) from
                           Submissions ls where x.rownum =
                           (select count(distinct q.submission_date) from Submissions q
                            where q.hacker_id = ls.hacker_id and q.submission_date <= x.submission_date)
                           ) as zz, h.hacker_id, h.name from
(
select w.*, @rownum:=@rownum+1 as rownum from
(
select * from
(
select * from
(
select * from
(select s.submission_date, count(*) as co, s.hacker_id from Submissions s group by s.submission_date, s.hacker_id) t
order by t.co desc, t.hacker_id asc
    ) u group by u.submission_date
) v
order by v.submission_date asc
    ) w
) x
 inner join Hackers h on h.hacker_id = x.hacker_id
order by x.submission_date asc;