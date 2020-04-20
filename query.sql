--query1
select uu.country, uu.cnt
from(
    SELECT country ,count(*) as cnt
    FROM Stores
    GROUP BY country
    ORDER BY count(*) desc
) uu
where rownum < 3;

--query2
select count(store_number) AS procent,ownership_type
from stores
group by ownership_type;
--query3
SELECT brand_name, COUNT(*)
FROM Stores
GROUP BY brand_name;
