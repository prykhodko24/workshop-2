--query1
select count(store_number),country
from Stores
group by country
order by count(store_number) desc
fetch first 3 rows only;

--query2
select count(store_number) AS procent,ownership_type
from stores
group by ownership_type;
--query3
SELECT longitude,latitude
FROM Stores
WHERE brand_name='Teavana';
