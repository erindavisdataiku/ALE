SELECT 
    `Year`,
    `BU_ID`,
    ROUND(`Total_Assets`, 0) AS `Total_Assets`
  FROM `se-sandbox`.`sedemo`.`AssetLiabilityReconciliation_audit_local_dbx` `__input_table`