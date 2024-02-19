SELECT toStartOfDay(toDateTime(aggregate_date)) AS __timestamp,
       dynamic_column_1 AS dynamic_column_1,
       sum(distro_points) AS "Store/Distro Count"
FROM
  (WITH client_filter AS
     (SELECT DISTINCT(clientcode) clientcode
      FROM stage.tr1_clientcode_mapping
      WHERE username = 'hezekiah' ),
        daily AS
     (SELECT `const_date` `const_date`,
             DATEADD(MONTH, DATEDIFF(MONTH, DATE(0), `const_date`), DATE(0)) `aggregate_date`,
             `store_id` `a.storeid`,
             concat(product_jid, ' (', `product_size`, ')') `dynamic_column_1`,
             CONCAT(product_jid, product_size, store_id) distro_points,
             '' `dynamic_column_2`,
                h.clientcode clientcode
      FROM dbt.tr1_prod_history2_distro h
      INNER JOIN client_filter c ON c.clientcode = h.clientcode
      WHERE h.product_id != ''
        AND h.product_jid NOT LIKE 'zz_%'
        AND (const_date >= CAST(1708300800000 / 1000 AS DATE)
             AND const_date <= CAST(1708300800000/ 1000 AS DATE))
        AND h.const_date > CAST('2023-01-01' AS date) ) SELECT `aggregate_date`,
                                                               COUNT(DISTINCT(`a.storeid`)) `store_count`,
                                                               COUNT(DISTINCT(distro_points)) `distro_points`,
                                                               `dynamic_column_1`,
                                                               `dynamic_column_2`,
                                                               clientcode
   FROM daily
   GROUP BY aggregate_date,
            dynamic_column_1,
            dynamic_column_2,
            clientcode) AS virtual_table
INNER JOIN
  (SELECT dynamic_column_1 AS dynamic_column_1__,
          sum(distro_points) AS mme_inner__
   FROM
     (WITH client_filter AS
        (SELECT DISTINCT(clientcode) clientcode
         FROM stage.tr1_clientcode_mapping
         WHERE username = 'hezekiah' ),
           daily AS
        (SELECT `const_date` `const_date`,
                DATEADD(MONTH, DATEDIFF(MONTH, DATE(0), `const_date`), DATE(0)) `aggregate_date`,
                `store_id` `a.storeid`,
                concat(product_jid, ' (', `product_size`, ')') `dynamic_column_1`,
                CONCAT(product_jid, product_size, store_id) distro_points,
                '' `dynamic_column_2`,
                   h.clientcode clientcode
         FROM dbt.tr1_prod_history2_distro h
         INNER JOIN client_filter c ON c.clientcode = h.clientcode
         WHERE h.product_id != ''
           AND h.product_jid NOT LIKE 'zz_%'
           AND (const_date >= CAST(1708300800000 / 1000 AS DATE)
                AND const_date <= CAST(1708300800000/ 1000 AS DATE))
           AND h.const_date > CAST('2023-01-01' AS date) ) SELECT `aggregate_date`,
                                                                  COUNT(DISTINCT(`a.storeid`)) `store_count`,
                                                                  COUNT(DISTINCT(distro_points)) `distro_points`,
                                                                  `dynamic_column_1`,
                                                                  `dynamic_column_2`,
                                                                  clientcode
      FROM daily
      GROUP BY aggregate_date,
               dynamic_column_1,
               dynamic_column_2,
               clientcode) AS virtual_table
   WHERE (clientcode = 'CM24')
   GROUP BY dynamic_column_1
   ORDER BY mme_inner__ DESC
   LIMIT 10) AS anon_1 ON dynamic_column_1 = dynamic_column_1__
WHERE (clientcode = 'CM24')
GROUP BY dynamic_column_1,
         toStartOfDay(toDateTime(aggregate_date))
ORDER BY "Store/Distro Count" DESC
LIMIT 10000;