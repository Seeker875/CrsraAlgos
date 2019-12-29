

--Sql hacker rank questions n points

--pivot
--rank over without partition by is possible
---filter by having without anything in select
/*
Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name,
 and the total number of challenges created by each student. Sort your results by the total number of 
 challenges in descending order. If more than one student created the same number of challenges, 
 then sort the result by hacker_id. If more than one student created the same number of challenges and
  the count is less than the maximum number of challenges created, 
  then exclude those students from the result.

*/


select h.hacker_id hacker_id,h.name name, count(c.hacker_id) as Challenges_created
from challenges c
left join hackers h
on c.hacker_id = h.hacker_id
group by  h.hacker_id, h.name          
---filtering on having
--- having on only challengers table 
--need. not join names table again
having count(c.hacker_id) = (select max(cntC) from ( 
    select count(c.hacker_id) as cntC from challenges c
                                             group by c.hacker_id ) as temp)
--- condition on having only
    or count(c.hacker_id) in (select cntC from (
                             select count(c.hacker_id) as cntC from challenges c
                                             group by c.hacker_id ) as temp
    -- nothing in select
                             group by cntC having count(cntC)=1
                             ) 
 order by Challenges_created desc, h.hacker_id 


/*

The total score of a hacker is the sum of their maximum scores for all of the challenges
Write a query to print the hacker_id, name, and total score of the hackers 
ordered by the descending scoreIf more than one hacker achieved the same total score, 
then sort the result by ascending hacker_id. Exclude all hackers with a total score of 0 from your result
*/

