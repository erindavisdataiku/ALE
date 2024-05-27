# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Assets_Liabilities_Equity_prep = dataiku.Dataset("Assets_Liabilities_Equity_prep")
df = Assets_Liabilities_Equity_prep.get_dataframe()


# Perform the grouping and aggregation
aggregated_df = df.groupby("Year").agg({
    "Total Assets": "sum",
    "Cash": "sum",
    "Accounts Receivable": "sum",
    "Inventories": "sum",
    "Fixed Assets": "sum",
    "Goodwill": "sum",
    "BU ID": "count"  # Using 'BU ID' to count rows
}).reset_index()

# Rename the columns to match the SQL output
aggregated_df = aggregated_df.rename(columns={
    "Total Assets": "Total Assets_sum",
    "Cash": "Cash_sum",
    "Accounts Receivable": "Accounts Receivable_sum",
    "Inventories": "Inventories_sum",
    "Fixed Assets": "Fixed Assets_sum",
    "Goodwill": "Goodwill_sum",
    "BU ID": "count"
})

aggreated_df.head()


# Write recipe outputs
ALE_by_Year = dataiku.Dataset("ALE_by_Year")
ALE_by_Year.write_with_schema(aggregated_df)
