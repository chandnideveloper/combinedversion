{
    "status": "success",
    "message": "Mapping completed successfully",
    "error_message": null,
    "contract_version": "2.0",
    "workbook_metadata": {
        "project_id": "4f2a34e4-9e34-4213-b3e2-2ab1b212bc87",
        "app_id": "4f2a34e4-9e34-4213-b3e2-2ab1b212bc87",
        "space_id": "personal",
        "name": "Weather Analytics",
        "app_name": "Weather Analytics",
        "run_id": "run-krle-test",
        "created_at": "2026-09-01T03:53:51.562511",
        "file_type": "qlik",
        "tenant": null,
        "qlik_version": "12.2897.0",
        "report_version": "12.2897.0"
    },
    "app_layout": {
        "theme": {
            "theme_name": "Sense Horizon",
            "background_color": "#F8F9FA",
            "primary_color": "#004B87",
            "color_palette": [
                "#004B87",
                "#00A3E0",
                "#702082",
                "#E87722",
                "#50B848"
            ],
            "font_family": "Segoe UI, sans-serif",
            "source": "default"
        }
    },
    "app_metadata": {
        "qlik_version": "12.2897.0",
        "report_version": "12.2897.0",
        "owner_name": "Ankush Kumar",
        "status": "private",
        "last_modified": "2026-09-01T01:48:42.165Z"
    },
    "connections": [
        {
            "name": "Google_BigQuery_ordinal-avatar-497006-v6",
            "connection_id": "91c6323f-2b08-464f-b153-1e5ce23dad19",
            "lib_name": "Google_BigQuery_ordinal-avatar-497006-v6",
            "driver": "gbq",
            "source_connector": "gbq",
            "server": null,
            "port": "5439",
            "database": "dev",
            "schema": null,
            "warehouse": null,
            "role": null,
            "project": null,
            "dataset": null,
            "http_path": null,
            "path": null,
            "username": null,
            "fabric": {
                "m_expression": "Folder.Files(\"datafiles\")",
                "m_source_function": "Folder.Files",
                "gateway_required": true,
                "privacy_level": "Organizational"
            },
            "confidence": {
                "score": 0.5,
                "band": "medium",
                "llm_score": 0.5,
                "checks": [],
                "penalties": [],
                "requires_review": true,
                "rationale": "Unrecognized driver fallback to Folder.Files."
            }
        }
    ],
    "tables": [
        {
            "name": "Weather_Data",
            "table_name": "Weather_Data",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "gbq",
                "name": "Google_BigQuery_ordinal-avatar-497006-v6",
                "connector_type": "gbq",
                "driver": "gbq",
                "source_connector": "gbq",
                "connection_id": "91c6323f-2b08-464f-b153-1e5ce23dad19"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nWeather_Data:\r\nLOAD\r\n    City,\r\n\r\n    Date(Date) AS Date,\r\n\r\n    Year(Date(Date#(Date, 'YYYY-MM-DD'))) AS Year,\r\n\r\n    Month(Date(Date#(Date, 'YYYY-MM-DD'))) AS Month,\r\n\r\n    MonthName(Date(Date#(Date, 'YYYY-MM-DD'))) AS MonthYear,\r\n\r\n    Record_Type,\r\n\r\n    Temperature,\r\n    Temp_Min,\r\n    Temp_Max,\r\n    Precipitation,\r\n\r\n    Weather_Code,\r\n\r\n    ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition,\r\n\r\n    If(Precipitation > 0, 1, 0) AS Rain_Flag,\r\n\r\n    Latitude,\r\n    Longitude,\r\n\r\n    GeoMakePoint(\r\n        Latitude,\r\n        Longitude\r\n    ) AS Longitude_Latitude,\r\n\r\n    Observation_Time;\nSELECT\r\n    City,\r\n    `Date`,\r\n    `Record_Type`,\r\n    Temperature,\r\n    `Temp_Min`,\r\n    `Temp_Max`,\r\n    Precipitation,\r\n    `Weather_Code`,\r\n    Latitude,\r\n    Longitude,\r\n    `Observation_Time`\r\nFROM `ordinal-avatar-497006-v6`.`Weather_001`.`Weather_Data`",
            "custom_sql": "SELECT\r\n    City,\r\n    `Date`,\r\n    `Record_Type`,\r\n    Temperature,\r\n    `Temp_Min`,\r\n    `Temp_Max`,\r\n    Precipitation,\r\n    `Weather_Code`,\r\n    Latitude,\r\n    Longitude,\r\n    `Observation_Time`\r\nFROM `ordinal-avatar-497006-v6`.`Weather_001`.`Weather_Data`",
            "columns": [
                {
                    "qlik_column_name": "City",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "City",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "Date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "Year",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "Year",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Month",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "Month",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "MonthYear",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "MonthYear",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Record_Type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "Record_Type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Temperature",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Temperature",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Temp_Min",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Temp_Min",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Temp_Max",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Temp_Max",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Precipitation",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Precipitation",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Weather_Code",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Weather_Code",
                    "fabric_datatype": "double",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "Weather_Condition",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "Weather_Condition",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Rain_Flag",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Rain_Flag",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "Latitude",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Latitude",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Longitude",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "Longitude",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "Longitude_Latitude",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "Longitude_Latitude",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "Observation_Time",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "Observation_Time",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY h\\:mm\\:ss TT"
                }
            ],
            "confidence": {
                "score": 0.65,
                "score_out_of_100": 65,
                "percentage": "65%",
                "band": "medium",
                "llm_score": 0.65,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "skip"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "fail"
                    },
                    {
                        "id": "schema_present",
                        "status": "pass"
                    },
                    {
                        "id": "column_data_types",
                        "status": "pass"
                    }
                ],
                "penalties": [
                    "M query has no real connector call (Value.NativeQuery/.Database/.Files) - likely an unresolved placeholder."
                ],
                "requires_review": true,
                "rationale": "All Qlik date and conditional functions mapped directly. However, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition, ApplyMap(\r\n        'WeatherCodeMap',\r\n        Weather_Code,\r\n        'Unknown'\r\n    ) AS Weather_Condition cannot be resolved, so field is set to null."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Weather_Data in Source"
                }
            ]
        },
        {
            "name": "WeatherCodeMap",
            "table_name": "WeatherCodeMap",
            "load_type": "inline",
            "source_type": "inline",
            "connection": null,
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nWeatherCodeMap:\r\nMAPPING LOAD * INLINE [\r\nWeather_Code, Weather_Condition\r\n0, Clear Sky\r\n1, Mainly Clear\r\n2, Partly Cloudy\r\n3, Overcast\r\n45, Fog\r\n48, Depositing Rime Fog\r\n51, Light Drizzle\r\n53, Moderate Drizzle\r\n55, Dense Drizzle\r\n61, Slight Rain\r\n63, Moderate Rain\r\n65, Heavy Rain\r\n71, Slight Snowfall\r\n73, Moderate Snowfall\r\n75, Heavy Snowfall\r\n80, Slight Rain Showers\r\n81, Moderate Rain Showers\r\n82, Violent Rain Showers\r\n95, Thunderstorm\r\n96, Thunderstorm with Hail\r\n99, Thunderstorm with Heavy Hail\r\n]",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "*",
                    "qlik_datatype": "NUMERIC",
                    "fabric_column_name": "*",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.78,
                "score_out_of_100": 78,
                "percentage": "78%",
                "band": "medium",
                "llm_score": 0.78,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "skip"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "fail"
                    },
                    {
                        "id": "schema_present",
                        "status": "pass"
                    },
                    {
                        "id": "column_data_types",
                        "status": "pass"
                    }
                ],
                "penalties": [
                    "M query has no real connector call (Value.NativeQuery/.Database/.Files) - likely an unresolved placeholder."
                ],
                "requires_review": true,
                "rationale": "One or more validation checks failed: M query has no real connector call (Value.NativeQuery/.Database/.Files) - likely an unresolved placeholder."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = #table({\"*\"}, {}) in Source"
                }
            ]
        }
    ],
    "relationships": [],
    "measures": [
        {
            "name": "Average Temperature",
            "qlik_expression": "Avg(Temperature)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('Weather_Data'[Temperature])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "715ee4c7-aacb-5079-8874-3168fbac245c"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Avg(Temperature)' was converted to DAX 'AVERAGE('Weather_Data'[Temperature])' with all syntax checks passing."
            }
        },
        {
            "name": "Rainy Records",
            "qlik_expression": "Count({<Rain_Flag={1}>} City)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(COUNT('Weather_Data'[City]), 'Weather_Data'[Rain_Flag] = \"1\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "32b53991-6abe-5396-9ffe-7f08b36b41f6"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Count({<Rain_Flag={1}>} City)' was converted to DAX 'CALCULATE(COUNT('Weather_Data'[City]), 'Weather_Data'[Rain_Flag] = \"1\")' with all syntax checks passing."
            }
        },
        {
            "name": "Weather Records",
            "qlik_expression": "Count(City)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "COUNT('Weather_Data'[City])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "3f52af7c-2cb4-5481-ac0a-e817eaab92af"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Count(City)' was converted to DAX 'COUNT('Weather_Data'[City])' with all syntax checks passing."
            }
        },
        {
            "name": "Minimum Temperature",
            "qlik_expression": "Min(Temp_Min)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "MIN('Weather_Data'[Temp_Min])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "c805e5fe-d1d7-5af1-91b1-8cee7cc2d401"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Min(Temp_Min)' was converted to DAX 'MIN('Weather_Data'[Temp_Min])' with all syntax checks passing."
            }
        },
        {
            "name": "Maximum Temperature",
            "qlik_expression": "Max(Temp_Max)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "MAX('Weather_Data'[Temp_Max])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "c5659451-09f4-5d18-8a26-78ee442a0cd5"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Max(Temp_Max)' was converted to DAX 'MAX('Weather_Data'[Temp_Max])' with all syntax checks passing."
            }
        },
        {
            "name": "Total Precipitation",
            "qlik_expression": "Sum(Precipitation)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "SUM('Weather_Data'[Precipitation])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "8f6cef07-481d-50a6-b76d-a9e682f7c013"
            },
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Sum(Precipitation)' was converted to DAX 'SUM('Weather_Data'[Precipitation])' with all syntax checks passing."
            }
        },
        {
            "name": "Cities Monitored",
            "qlik_expression": "Count(DISTINCT City)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "DISTINCTCOUNT('Weather_Data'[City])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "5e93dcab-179e-5118-983f-e1038bdd811f"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Count(DISTINCT City)' was converted to DAX 'DISTINCTCOUNT('Weather_Data'[City])' with all syntax checks passing."
            }
        },
        {
            "name": "Average Precipitation",
            "qlik_expression": "Avg(Precipitation)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('Weather_Data'[Precipitation])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "db8c2c6e-d368-55b4-80da-40cf76d3313e"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Avg(Precipitation)' was converted to DAX 'AVERAGE('Weather_Data'[Precipitation])' with all syntax checks passing."
            }
        },
        {
            "name": "Temperature Range",
            "qlik_expression": "Max(Temp_Max) - Min(Temp_Min)",
            "qlik_number_format": {},
            "tables": [
                "Weather_Data"
            ],
            "fabric": {
                "dax_expression": "MAX('Weather_Data'[Temp_Max]) - MIN('Weather_Data'[Temp_Min])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "eed10315-b026-55c0-9038-563cb15c57af"
            },
            "confidence": {
                "score": 0.8,
                "score_out_of_100": 80,
                "percentage": "80%",
                "band": "medium",
                "llm_score": 0.8,
                "checks": [
                    {
                        "id": "dax_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_banned_functions",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_qlik_leftovers",
                        "status": "pass"
                    },
                    {
                        "id": "dax_columns_exist",
                        "status": "pass"
                    },
                    {
                        "id": "dax_no_bare_columns",
                        "status": "pass"
                    },
                    {
                        "id": "dax_related_direction",
                        "status": "skip",
                        "detail": "no RELATED() call"
                    },
                    {
                        "id": "dax_iterator_related_wrapping",
                        "status": "skip",
                        "detail": "no iterator"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "The Qlik expression 'Max(Temp_Max) - Min(Temp_Min)' was converted to DAX 'MAX('Weather_Data'[Temp_Max]) - MIN('Weather_Data'[Temp_Min])' with all syntax checks passing."
            }
        },
        {
            "name": "Count(City)",
            "qlik_expression": "Count(City)",
            "dax_expression": "DISTINCTCOUNT('Weather_Data'[City])",
            "tables": [
                "Weather_Data"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Weather_Data",
                "dax_expression": "DISTINCTCOUNT('Weather_Data'[City])",
                "format_string": "#,##0",
                "tmdl": "measure 'Count(City)' = DISTINCTCOUNT('Weather_Data'[City])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Count(City)'."
            }
        },
        {
            "name": "Avg(Temperature)",
            "qlik_expression": "Avg(Temperature)",
            "dax_expression": "AVERAGE('Weather_Data'[Temperature])",
            "tables": [
                "Weather_Data"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Weather_Data",
                "dax_expression": "AVERAGE('Weather_Data'[Temperature])",
                "format_string": "#,##0.00",
                "tmdl": "measure 'Avg(Temperature)' = AVERAGE('Weather_Data'[Temperature])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Avg(Temperature)'."
            }
        },
        {
            "name": "Sum(Precipitation)",
            "qlik_expression": "Sum(Precipitation)",
            "dax_expression": "SUM('Weather_Data'[Precipitation])",
            "tables": [
                "Weather_Data"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Weather_Data",
                "dax_expression": "SUM('Weather_Data'[Precipitation])",
                "format_string": "#,##0",
                "tmdl": "measure 'Sum(Precipitation)' = SUM('Weather_Data'[Precipitation])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Sum(Precipitation)'."
            }
        },
        {
            "name": "Historical Precipitation",
            "qlik_expression": "Sum({<Record_Type={'Historical'}>} Precipitation)",
            "dax_expression": "SUM('Weather_Data'[Precipitation])",
            "tables": [
                "Weather_Data"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Weather_Data",
                "dax_expression": "SUM('Weather_Data'[Precipitation])",
                "format_string": "#,##0",
                "tmdl": "measure 'Historical Precipitation' = SUM('Weather_Data'[Precipitation])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Historical Precipitation'."
            }
        },
        {
            "name": "Count({<Rain_Flag={1}>} DISTINCT Date)",
            "qlik_expression": "Count({<Rain_Flag={1}>} DISTINCT Date)",
            "dax_expression": "DISTINCTCOUNT('Weather_Data'[Date])",
            "tables": [
                "Weather_Data"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Weather_Data",
                "dax_expression": "DISTINCTCOUNT('Weather_Data'[Date])",
                "format_string": "#,##0",
                "tmdl": "measure 'Count({<Rain_Flag={1}>} DISTINCT Date)' = DISTINCTCOUNT('Weather_Data'[Date])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Count({<Rain_Flag={1}>} DISTINCT Date)'."
            }
        }
    ],
    "dimensions": [
        {
            "name": "Weather_Condition",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Weather_Data",
                "lineage_tag": "2952071a-001f-4f05-ad6e-1aecd5d67a56"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        },
        {
            "name": "Date",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER",
            "nature": "INTEGER",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "Weather_Data",
                "lineage_tag": "2f199d66-d303-4448-ae99-5aeeeb383166"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        },
        {
            "name": "Year",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER",
            "nature": "INTEGER",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "Weather_Data",
                "lineage_tag": "acf57e12-387e-4515-9ee6-56e8e9aa9f87"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        },
        {
            "name": "Month-Year",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER",
            "nature": "INTEGER",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "Weather_Data",
                "lineage_tag": "8a1af885-75fa-41ac-9d63-5fe59f424647"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        },
        {
            "name": "Record Type",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Weather_Data",
                "lineage_tag": "b74bf028-c72b-4f2e-b0c9-0fa932e11610"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        },
        {
            "name": "City",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Weather_Data"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Weather_Data",
                "lineage_tag": "7a1e353f-a182-40d6-b68e-165913245bf9"
            },
            "confidence": {
                "score": 1,
                "score_out_of_100": 100,
                "percentage": "100%",
                "band": "high",
                "checks": [
                    {
                        "id": "dim_table_resolved",
                        "status": "pass"
                    },
                    {
                        "id": "dim_direct_mapping",
                        "status": "pass"
                    }
                ],
                "penalties": [],
                "requires_review": false,
                "rationale": "Plain field dimension maps directly to a model column."
            }
        }
    ],
    "calculated_columns": [],
    "custom_sql": [],
    "visuals": {
        "sheet_visuals": [
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "ekNAa",
                    "visual_name": "ekNAa",
                    "object_category": "other",
                    "chart_type": "text-image",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 24,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "WEATHER ANALYTICS",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "textbox",
                    "bi_type": "textbox",
                    "supported": true,
                    "status": "mapped",
                    "title": "WEATHER ANALYTICS",
                    "name": "WEATHER ANALYTICS",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 24,
                        "rowspan": 2,
                        "x": 0,
                        "y": 0,
                        "width": 1280,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "textbox",
                        "title": {
                            "text": "WEATHER ANALYTICS",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 1280,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "WEATHER ANALYTICS",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "wssfxF",
                    "visual_name": "wssfxF",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "City",
                    "name": "City",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 4,
                        "x": 0,
                        "y": 34,
                        "width": 267,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 34,
                            "width": 267,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "pYTmej",
                    "visual_name": "pYTmej",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 5,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Record Type",
                    "name": "Record Type",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 5,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 4,
                        "x": 267,
                        "y": 34,
                        "width": 267,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Record Type",
                            "visible": true
                        },
                        "general": {
                            "x": 267,
                            "y": 34,
                            "width": 267,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "YbmvyYp",
                    "visual_name": "YbmvyYp",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 10,
                    "row": 2,
                    "colspan": 4,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Year",
                    "name": "Year",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 10,
                        "row": 2,
                        "colspan": 4,
                        "rowspan": 4,
                        "x": 533,
                        "y": 34,
                        "width": 213,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Year",
                            "visible": true
                        },
                        "general": {
                            "x": 533,
                            "y": 34,
                            "width": 213,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "YPBfGA",
                    "visual_name": "YPBfGA",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 14,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Month-Year",
                    "name": "Month-Year",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 14,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 4,
                        "x": 747,
                        "y": 34,
                        "width": 267,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Month-Year",
                            "visible": true
                        },
                        "general": {
                            "x": 747,
                            "y": 34,
                            "width": 267,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "WumAV",
                    "visual_name": "WumAV",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 19,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather_Condition",
                    "name": "Weather_Condition",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 19,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 4,
                        "x": 1013,
                        "y": 34,
                        "width": 267,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Weather_Condition",
                            "visible": true
                        },
                        "general": {
                            "x": 1013,
                            "y": 34,
                            "width": 267,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "QNDGVdb",
                    "visual_name": "QNDGVdb",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 6,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature",
                    "name": "Average Temperature",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 6,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 0,
                        "y": 103,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 103,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "ZksTVL",
                    "visual_name": "ZksTVL",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 6,
                    "row": 6,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Maximum Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Maximum Temperature",
                    "name": "Maximum Temperature",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 6,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 320,
                        "y": 103,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Maximum Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 103,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Maximum Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "JvJTedB",
                    "visual_name": "JvJTedB",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 6,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Precipitation",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Total Precipitation",
                    "name": "Total Precipitation",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 6,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 640,
                        "y": 103,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Precipitation",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 103,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Precipitation",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "mnCmjkJ",
                    "visual_name": "mnCmjkJ",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 18,
                    "row": 6,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Cities Monitored"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Cities Monitored",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Cities Monitored",
                    "name": "Cities Monitored",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 6,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 103,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Cities Monitored",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 103,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Cities Monitored"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Cities Monitored",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jRqXyp",
                    "visual_name": "jRqXyp",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 9,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "lineChart",
                    "bi_type": "lineChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature Trend",
                    "name": "Average Temperature Trend",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 9,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 0,
                        "y": 154,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "Average Temperature Trend",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 154,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10,
                                "logarithmic": false
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "NuqCJea",
                    "visual_name": "NuqCJea",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 9,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature by City",
                    "name": "Average Temperature by City",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 9,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 640,
                        "y": 154,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Average Temperature by City",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 154,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "LvSNThL",
                    "visual_name": "LvSNThL",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 15,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Count(City)"
                    ],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Conditions",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather Conditions",
                    "name": "Weather Conditions",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 15,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 257,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Weather Conditions",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 257,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Count(City)"
                    ],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Conditions",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "components": [
                            {
                                "key": "general"
                            }
                        ],
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "JJFwBL",
                    "visual_name": "JJFwBL",
                    "object_category": "chart",
                    "chart_type": "combochart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 15,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation",
                        "Average Temperature"
                    ],
                    "x_axis": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature & Precipitation Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "lineClusteredColumnComboChart",
                    "bi_type": "lineClusteredColumnComboChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Temperature & Precipitation Trend",
                    "name": "Temperature & Precipitation Trend",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 15,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 257,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineClusteredColumnComboChart",
                        "title": {
                            "text": "Temperature & Precipitation Trend",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 257,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'combochart' visual maps directly to Fabric 'lineClusteredColumnComboChart' visual.",
                    "y_axis_fields": [
                        "Total Precipitation",
                        "Average Temperature"
                    ],
                    "x_axis_fields": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature & Precipitation Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "axis": 0,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            },
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'combochart' visual maps directly to Fabric 'lineClusteredColumnComboChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "CuXvsKp",
                    "visual_name": "CuXvsKp",
                    "object_category": "other",
                    "chart_type": "sn-table",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 20,
                    "colspan": 24,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "City",
                        "Date",
                        "Record Type",
                        "Weather_Condition",
                        "Temperature",
                        "Temp_Max",
                        "Temp_Min",
                        "Precipitation"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Data Details",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "tableEx",
                    "bi_type": "tableEx",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather Data Details",
                    "name": "Weather Data Details",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 20,
                        "colspan": 24,
                        "rowspan": 6,
                        "x": 0,
                        "y": 343,
                        "width": 1280,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "tableEx",
                        "title": {
                            "text": "Weather Data Details",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 343,
                            "width": 1280,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "City",
                        "Date",
                        "Record Type",
                        "Weather_Condition",
                        "Temperature",
                        "Temp_Max",
                        "Temp_Min",
                        "Precipitation"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Data Details",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        },
                        "null_value_representation": {
                            "text": "-"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "JDqmPzF",
                    "visual_name": "JDqmPzF",
                    "object_category": "other",
                    "chart_type": "text-image",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 24,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "TEMPERATURE ANALYSIS",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "textbox",
                    "bi_type": "textbox",
                    "supported": true,
                    "status": "mapped",
                    "title": "TEMPERATURE ANALYSIS",
                    "name": "TEMPERATURE ANALYSIS",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 24,
                        "rowspan": 2,
                        "x": 0,
                        "y": 0,
                        "width": 1280,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "textbox",
                        "title": {
                            "text": "TEMPERATURE ANALYSIS",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 1280,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "TEMPERATURE ANALYSIS",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "GneYPhR",
                    "visual_name": "GneYPhR",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "City",
                    "name": "City",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 0,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "EYg",
                    "visual_name": "EYg",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 6,
                    "row": 2,
                    "colspan": 7,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Record Type",
                    "name": "Record Type",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 2,
                        "colspan": 7,
                        "rowspan": 3,
                        "x": 320,
                        "y": 34,
                        "width": 373,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Record Type",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 34,
                            "width": 373,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "VZLmXX",
                    "visual_name": "VZLmXX",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 13,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Year",
                    "name": "Year",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 13,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 693,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Year",
                            "visible": true
                        },
                        "general": {
                            "x": 693,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "LjYvLK",
                    "visual_name": "LjYvLK",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 19,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Month-Year",
                    "name": "Month-Year",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 19,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 3,
                        "x": 1013,
                        "y": 34,
                        "width": 267,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Month-Year",
                            "visible": true
                        },
                        "general": {
                            "x": 1013,
                            "y": 34,
                            "width": 267,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "yfXjh",
                    "visual_name": "yfXjh",
                    "object_category": "other",
                    "chart_type": "gauge",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 5,
                    "colspan": 9,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "gauge",
                    "bi_type": "gauge",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature",
                    "name": "Average Temperature",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 5,
                        "colspan": 9,
                        "rowspan": 6,
                        "x": 0,
                        "y": 86,
                        "width": 480,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "gauge",
                        "title": {
                            "text": "Average Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 86,
                            "width": 480,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "palette_scheme": "qlik_default_12",
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "colorScheme": {
                            "useBaseColors": "measure",
                            "mode": "primary",
                            "auto": true
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "measure_axis": {
                                "min": 0,
                                "max": 100,
                                "show": "all",
                                "spacing": 1
                            }
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jCxMjr",
                    "visual_name": "jCxMjr",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 18,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Minimum Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Minimum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Minimum Temperature",
                    "name": "Minimum Temperature",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Minimum Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Minimum Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Minimum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "fzuMt",
                    "visual_name": "fzuMt",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 18,
                    "row": 8,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Maximum Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Maximum Temperature",
                    "name": "Maximum Temperature",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 8,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 137,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Maximum Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 137,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Maximum Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "YmbEAfn",
                    "visual_name": "YmbEAfn",
                    "object_category": "other",
                    "chart_type": "gauge",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 9,
                    "row": 5,
                    "colspan": 9,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Temperature Range"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Temperature Range",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "gauge",
                    "bi_type": "gauge",
                    "supported": true,
                    "status": "mapped",
                    "title": "Temperature Range",
                    "name": "Temperature Range",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 9,
                        "row": 5,
                        "colspan": 9,
                        "rowspan": 6,
                        "x": 480,
                        "y": 86,
                        "width": 480,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "gauge",
                        "title": {
                            "text": "Temperature Range",
                            "visible": true
                        },
                        "general": {
                            "x": 480,
                            "y": 86,
                            "width": 480,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                    "y_axis_fields": [
                        "Temperature Range"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Temperature Range",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "palette_scheme": "qlik_default_12",
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "colorScheme": {
                            "useBaseColors": "measure",
                            "mode": "primary",
                            "auto": true
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "measure_axis": {
                                "min": 0,
                                "max": 100,
                                "show": "all",
                                "spacing": 1
                            }
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "LGvwDWQ",
                    "visual_name": "LGvwDWQ",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 11,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "lineChart",
                    "bi_type": "lineChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature Trend",
                    "name": "Average Temperature Trend",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 11,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 0,
                        "y": 189,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "Average Temperature Trend",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 189,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10,
                                "logarithmic": false
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "PhFvet",
                    "visual_name": "PhFvet",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 11,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Minimum Temperature",
                        "Maximum Temperature"
                    ],
                    "x_axis": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Minimum vs Maximum Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "lineChart",
                    "bi_type": "lineChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Minimum vs Maximum Temperature",
                    "name": "Minimum vs Maximum Temperature",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 11,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 640,
                        "y": 189,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "Minimum vs Maximum Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 189,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "Minimum Temperature",
                        "Maximum Temperature"
                    ],
                    "x_axis_fields": [
                        "Date"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Minimum vs Maximum Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10,
                                "logarithmic": false
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            },
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "PZsAh",
                    "visual_name": "PZsAh",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 17,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature by City",
                    "name": "Average Temperature by City",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 17,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 291,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Average Temperature by City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 291,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "pAcEMx",
                    "visual_name": "pAcEMx",
                    "object_category": "other",
                    "chart_type": "histogram",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 17,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Temperature"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature Distribution",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "columnChart",
                    "bi_type": "columnChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Temperature Distribution",
                    "name": "Temperature Distribution",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 17,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 291,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "columnChart",
                        "title": {
                            "text": "Temperature Distribution",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 291,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'histogram' visual maps directly to Fabric 'columnChart' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Temperature"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature Distribution",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "bar": {
                                "paletteColor": {
                                    "index": 6,
                                    "color": "#4477aa"
                                }
                            }
                        },
                        "axes": {
                            "dimension_axis": {
                                "show": "all",
                                "label": "auto",
                                "dock": "near"
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'histogram' visual maps directly to Fabric 'columnChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "WgJGPG",
                    "visual_name": "WgJGPG",
                    "object_category": "other",
                    "chart_type": "scatterplot",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 22,
                    "colspan": 24,
                    "rowspan": 8,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature",
                        "Average Precipitation"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature vs Precipitation by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "scatterChart",
                    "bi_type": "scatterChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Temperature vs Precipitation by City",
                    "name": "Temperature vs Precipitation by City",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 22,
                        "colspan": 24,
                        "rowspan": 8,
                        "x": 0,
                        "y": 377,
                        "width": 1280,
                        "height": 137
                    },
                    "power_bi_visual_type": {
                        "visualType": "scatterChart",
                        "title": {
                            "text": "Temperature vs Precipitation by City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 377,
                            "width": 1280,
                            "height": 137
                        }
                    },
                    "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual.",
                    "y_axis_fields": [
                        "Average Temperature",
                        "Average Precipitation"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature vs Precipitation by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            },
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "labels": {
                            "mode": 1
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "DpesV",
                    "visual_name": "DpesV",
                    "object_category": "other",
                    "chart_type": "boxplot",
                    "sheet_name": "Temperature Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 30,
                    "colspan": 24,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Avg(Temperature)"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature Distribution by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "boxPlot",
                    "bi_type": "boxPlot",
                    "supported": true,
                    "status": "mapped",
                    "title": "Temperature Distribution by City",
                    "name": "Temperature Distribution by City",
                    "object_category": "standard",
                    "sheet_name": "Temperature Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 30,
                        "colspan": 24,
                        "rowspan": 6,
                        "x": 0,
                        "y": 514,
                        "width": 1280,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "boxPlot",
                        "title": {
                            "text": "Temperature Distribution by City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 514,
                            "width": 1280,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual.",
                    "y_axis_fields": [
                        "Avg(Temperature)"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Temperature Distribution by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "show": "all",
                                "label": "auto",
                                "dock": "near"
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jwbHr",
                    "visual_name": "jwbHr",
                    "object_category": "other",
                    "chart_type": "text-image",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 24,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "PRECIPITATION & WEATHER",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "textbox",
                    "bi_type": "textbox",
                    "supported": true,
                    "status": "mapped",
                    "title": "PRECIPITATION & WEATHER",
                    "name": "PRECIPITATION & WEATHER",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 24,
                        "rowspan": 2,
                        "x": 0,
                        "y": 0,
                        "width": 1280,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "textbox",
                        "title": {
                            "text": "PRECIPITATION & WEATHER",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 1280,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "PRECIPITATION & WEATHER",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "bzrJadX",
                    "visual_name": "bzrJadX",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "City",
                    "name": "City",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 3,
                        "x": 0,
                        "y": 34,
                        "width": 267,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 34,
                            "width": 267,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "BKgyyJ",
                    "visual_name": "BKgyyJ",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 5,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Record Type",
                    "name": "Record Type",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 5,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 3,
                        "x": 267,
                        "y": 34,
                        "width": 267,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Record Type",
                            "visible": true
                        },
                        "general": {
                            "x": 267,
                            "y": 34,
                            "width": 267,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "puPXJMe",
                    "visual_name": "puPXJMe",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 10,
                    "row": 2,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Year",
                    "name": "Year",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 10,
                        "row": 2,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 533,
                        "y": 34,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Year",
                            "visible": true
                        },
                        "general": {
                            "x": 533,
                            "y": 34,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "PPJHbjc",
                    "visual_name": "PPJHbjc",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 14,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Month-Year",
                    "name": "Month-Year",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 14,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 3,
                        "x": 747,
                        "y": 34,
                        "width": 267,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Month-Year",
                            "visible": true
                        },
                        "general": {
                            "x": 747,
                            "y": 34,
                            "width": 267,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Month-Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "LPeGw",
                    "visual_name": "LPeGw",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 19,
                    "row": 2,
                    "colspan": 5,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather_Condition",
                    "name": "Weather_Condition",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 19,
                        "row": 2,
                        "colspan": 5,
                        "rowspan": 3,
                        "x": 1013,
                        "y": 34,
                        "width": 267,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Weather_Condition",
                            "visible": true
                        },
                        "general": {
                            "x": 1013,
                            "y": 34,
                            "width": 267,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "dQWmpm",
                    "visual_name": "dQWmpm",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Total Precipitation (mm)",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Total Precipitation (mm)",
                    "name": "Total Precipitation (mm)",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 0,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Precipitation (mm)",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Total Precipitation (mm)",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": true
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "CXrXTJ",
                    "visual_name": "CXrXTJ",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 6,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Precipitation"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Precipitation (mm)",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Precipitation (mm)",
                    "name": "Average Precipitation (mm)",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 320,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Precipitation (mm)",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Precipitation"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Precipitation (mm)",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": true
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "tPVf",
                    "visual_name": "tPVf",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Rainy Records"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Rainy Records",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Rainy Records",
                    "name": "Rainy Records",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 640,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Rainy Records",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Rainy Records"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Rainy Records",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": true
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jFZexU",
                    "visual_name": "jFZexU",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 18,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Weather Records"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Records",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather Records",
                    "name": "Weather Records",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Weather Records",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Weather Records"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Records",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": true
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.00",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "HXtNcM",
                    "visual_name": "HXtNcM",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 8,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation"
                    ],
                    "x_axis": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Monthly Precipitation Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "lineChart",
                    "bi_type": "lineChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Monthly Precipitation Trend",
                    "name": "Monthly Precipitation Trend",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 8,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 0,
                        "y": 137,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "Monthly Precipitation Trend",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 137,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Monthly Precipitation Trend",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10,
                                "logarithmic": false
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "PKrnduH",
                    "visual_name": "PKrnduH",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 8,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Precipitation by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Precipitation by City",
                    "name": "Precipitation by City",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 8,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 640,
                        "y": 137,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Precipitation by City",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 137,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Precipitation by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "PYpyRVX",
                    "visual_name": "PYpyRVX",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 14,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Count(City)"
                    ],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Condition Frequency",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather Condition Frequency",
                    "name": "Weather Condition Frequency",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 14,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 240,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Weather Condition Frequency",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 240,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Count(City)"
                    ],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Condition Frequency",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "UrPWmk",
                    "visual_name": "UrPWmk",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 14,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Sum(Precipitation)"
                    ],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Precipitation by Weather Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Precipitation by Weather Condition",
                    "name": "Precipitation by Weather Condition",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 14,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 240,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Precipitation by Weather Condition",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 240,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Sum(Precipitation)"
                    ],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Precipitation by Weather Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "mxryL",
                    "visual_name": "mxryL",
                    "object_category": "other",
                    "chart_type": "distributionplot",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 19,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Historical Precipitation",
                        "Historical Precipitation"
                    ],
                    "x_axis": [
                        "Month-Year",
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Historical vs Forecast Precipitation",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "scatterChart",
                    "bi_type": "scatterChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Historical vs Forecast Precipitation",
                    "name": "Historical vs Forecast Precipitation",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 19,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 326,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "scatterChart",
                        "title": {
                            "text": "Historical vs Forecast Precipitation",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 326,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'distributionplot' visual maps directly to Fabric 'scatterChart' visual.",
                    "y_axis_fields": [
                        "Historical Precipitation",
                        "Historical Precipitation"
                    ],
                    "x_axis_fields": [
                        "Month-Year",
                        "Month-Year"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Historical vs Forecast Precipitation",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useMeasureGradient": true,
                            "point": {
                                "auto": true,
                                "mode": "primary",
                                "useBaseColors": "off",
                                "paletteColor": {
                                    "index": 6
                                },
                                "useDimColVal": true,
                                "persistent": false,
                                "expressionIsColor": true,
                                "measureScheme": "sg",
                                "reverseScheme": false,
                                "dimensionScheme": "12",
                                "autoMinMax": true,
                                "measureMin": 0,
                                "measureMax": 10
                            },
                            "box": {
                                "paletteColor": {
                                    "color": "#e6e6e6",
                                    "index": -1
                                }
                            }
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            },
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'distributionplot' visual maps directly to Fabric 'scatterChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "sqMeV",
                    "visual_name": "sqMeV",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 24,
                    "colspan": 24,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Count({<Rain_Flag={1}>} DISTINCT Date)"
                    ],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Rainy Days by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "barChart",
                    "bi_type": "barChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Rainy Days by City",
                    "name": "Rainy Days by City",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 24,
                        "colspan": 24,
                        "rowspan": 6,
                        "x": 0,
                        "y": 411,
                        "width": 1280,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Rainy Days by City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 411,
                            "width": 1280,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Count({<Rain_Flag={1}>} DISTINCT Date)"
                    ],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Rainy Days by City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "axes": {
                            "dimension_axis": {
                                "continuousAuto": true,
                                "show": "all",
                                "label": "auto",
                                "dock": "near",
                                "axisDisplayMode": "auto",
                                "maxVisibleItems": 10
                            },
                            "measure_axis": {
                                "show": "all",
                                "dock": "near",
                                "spacing": 1,
                                "autoMinMax": true,
                                "minMax": "min",
                                "min": 0,
                                "max": 10
                            },
                            "gridlines": {
                                "auto": true,
                                "spacing": 2
                            }
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "vertical",
                        "bar_grouping": {
                            "grouping": "grouped"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "namAbjW",
                    "visual_name": "namAbjW",
                    "object_category": "other",
                    "chart_type": "treemap",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 30,
                    "colspan": 24,
                    "rowspan": 9,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Count(City)"
                    ],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Condition Distribution",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "treemap",
                    "bi_type": "treemap",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather Condition Distribution",
                    "name": "Weather Condition Distribution",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 30,
                        "colspan": 24,
                        "rowspan": 9,
                        "x": 0,
                        "y": 514,
                        "width": 1280,
                        "height": 154
                    },
                    "power_bi_visual_type": {
                        "visualType": "treemap",
                        "title": {
                            "text": "Weather Condition Distribution",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 514,
                            "width": 1280,
                            "height": 154
                        }
                    },
                    "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                    "y_axis_fields": [
                        "Count(City)"
                    ],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Weather Condition Distribution",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false,
                            "dock": "auto"
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "auto": true,
                        "mode": "primary",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": true,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10
                        },
                        "data_colors": {
                            "mode": "primary",
                            "auto": true
                        },
                        "legend": {
                            "show": false,
                            "dock": "auto"
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "labels": {
                            "auto": true,
                            "headers": true,
                            "overlay": true,
                            "leaves": true,
                            "values": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "JGksv",
                    "visual_name": "JGksv",
                    "object_category": "other",
                    "chart_type": "gauge",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 19,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "gauge",
                    "bi_type": "gauge",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature",
                    "name": "Average Temperature",
                    "object_category": "standard",
                    "sheet_name": "Precipitation & Weather Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 19,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 326,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "gauge",
                        "title": {
                            "text": "Average Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 326,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "useBaseColors": "measure"
                        },
                        "axes": {
                            "measure_axis": {
                                "min": 0,
                                "max": 100,
                                "show": "all",
                                "spacing": 1
                            }
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "orientation": "horizontal"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "mVnpjq",
                    "visual_name": "mVnpjq",
                    "object_category": "other",
                    "chart_type": "text-image",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 24,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Text-Image",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "textbox",
                    "bi_type": "textbox",
                    "supported": true,
                    "status": "mapped",
                    "title": "Text-Image",
                    "name": "Text-Image",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 24,
                        "rowspan": 2,
                        "x": 0,
                        "y": 0,
                        "width": 1280,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "textbox",
                        "title": {
                            "text": "Text-Image",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 1280,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Text-Image",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "apzrRt",
                    "visual_name": "apzrRt",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "City",
                    "name": "City",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 0,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "City",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "City"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "City",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "mSfQc",
                    "visual_name": "mSfQc",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 6,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Record Type",
                    "name": "Record Type",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 320,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Record Type",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Record Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Record Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "eqDgtEL",
                    "visual_name": "eqDgtEL",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Year",
                    "name": "Year",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 640,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Year",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Year"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Year",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "TmcWUs",
                    "visual_name": "TmcWUs",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 18,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "Weather_Condition",
                    "name": "Weather_Condition",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 2,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 34,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Weather_Condition",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 34,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Weather_Condition"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Weather_Condition",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "ZgPuTS",
                    "visual_name": "ZgPuTS",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature",
                    "name": "Average Temperature",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 0,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jMmUXA",
                    "visual_name": "jMmUXA",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 6,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Maximum Temperature"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Maximum Temperature",
                    "name": "Maximum Temperature",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 320,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Maximum Temperature",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Maximum Temperature"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Maximum Temperature",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "jVeANM",
                    "visual_name": "jVeANM",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 12,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Precipitation"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Precipitation",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Total Precipitation",
                    "name": "Total Precipitation",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 640,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Precipitation",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Precipitation",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "NePj",
                    "visual_name": "NePj",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 18,
                    "row": 5,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Cities Monitored"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Cities Monitored",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "card",
                    "bi_type": "card",
                    "supported": true,
                    "status": "mapped",
                    "title": "Cities Monitored",
                    "name": "Cities Monitored",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 18,
                        "row": 5,
                        "colspan": 6,
                        "rowspan": 3,
                        "x": 960,
                        "y": 86,
                        "width": 320,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Cities Monitored",
                            "visible": true
                        },
                        "general": {
                            "x": 960,
                            "y": 86,
                            "width": 320,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Cities Monitored"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Cities Monitored",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "font_size": "M",
                            "show": false
                        },
                        "kpi": {
                            "align": "center"
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            }
                        ],
                        "text_align": "center",
                        "fontSize": "M"
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "dQDeKpZ",
                    "visual_name": "dQDeKpZ",
                    "object_category": "other",
                    "chart_type": "map",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 8,
                    "colspan": 24,
                    "rowspan": 8,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Longitude_Latitude"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by Location",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "map",
                    "bi_type": "map",
                    "supported": true,
                    "status": "mapped",
                    "title": "Average Temperature by Location",
                    "name": "Average Temperature by Location",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 8,
                        "colspan": 24,
                        "rowspan": 8,
                        "x": 0,
                        "y": 137,
                        "width": 1280,
                        "height": 137
                    },
                    "power_bi_visual_type": {
                        "visualType": "map",
                        "title": {
                            "text": "Average Temperature by Location",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 137,
                            "width": 1280,
                            "height": 137
                        }
                    },
                    "rationale": "The Qlik Sense 'map' visual maps directly to Fabric 'map' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Longitude_Latitude"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Average Temperature by Location",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'map' visual maps directly to Fabric 'map' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "FhNaRL",
                    "visual_name": "FhNaRL",
                    "object_category": "other",
                    "chart_type": "sn-table",
                    "sheet_name": "Geographic Analysis",
                    "layout": {},
                    "col": 0,
                    "row": 16,
                    "colspan": 24,
                    "rowspan": 7,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Temperature",
                        "Maximum Temperature",
                        "Total Precipitation"
                    ],
                    "x_axis": [
                        "City",
                        "Latitude",
                        "Longitude"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Geographic Weather Details",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "tableEx",
                    "bi_type": "tableEx",
                    "supported": true,
                    "status": "mapped",
                    "title": "Geographic Weather Details",
                    "name": "Geographic Weather Details",
                    "object_category": "standard",
                    "sheet_name": "Geographic Analysis",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 16,
                        "colspan": 24,
                        "rowspan": 7,
                        "x": 0,
                        "y": 274,
                        "width": 1280,
                        "height": 120
                    },
                    "power_bi_visual_type": {
                        "visualType": "tableEx",
                        "title": {
                            "text": "Geographic Weather Details",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 274,
                            "width": 1280,
                            "height": 120
                        }
                    },
                    "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                    "y_axis_fields": [
                        "Average Temperature",
                        "Maximum Temperature",
                        "Total Precipitation"
                    ],
                    "x_axis_fields": [
                        "City",
                        "Latitude",
                        "Longitude"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Geographic Weather Details",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    },
                    "kpi_styling": {
                        "value_font_family": "Segoe UI, sans-serif",
                        "label_font_family": "Segoe UI, sans-serif",
                        "align": "center"
                    },
                    "color": {
                        "is_multicolor": false,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "legend": {
                            "show": false
                        },
                        "number_formats": [
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            },
                            {
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
                            },
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "#,##0.0",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "null_value_representation": {
                            "text": "-"
                        }
                    },
                    "custom_coloring": {},
                    "reference_lines": []
                },
                "confidence": {
                    "score": 0.95,
                    "band": "high",
                    "llm_score": 0.95,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "pass"
                        }
                    ],
                    "penalties": [],
                    "requires_review": false,
                    "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual."
                }
            }
        ],
        "sheets": [
            {
                "sheet_id": "paKLEj",
                "title": "Executive Overview",
                "visualization_count": 15,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "ekNAa",
                            "visual_name": "ekNAa",
                            "object_category": "other",
                            "chart_type": "text-image",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 24,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "WEATHER ANALYTICS",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "textbox",
                            "bi_type": "textbox",
                            "supported": true,
                            "status": "mapped",
                            "title": "WEATHER ANALYTICS",
                            "name": "WEATHER ANALYTICS",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 24,
                                "rowspan": 2,
                                "x": 0,
                                "y": 0,
                                "width": 1280,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "textbox",
                                "title": {
                                    "text": "WEATHER ANALYTICS",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 1280,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "WEATHER ANALYTICS",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "wssfxF",
                            "visual_name": "wssfxF",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "City",
                            "name": "City",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 4,
                                "x": 0,
                                "y": 34,
                                "width": 267,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 34,
                                    "width": 267,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "pYTmej",
                            "visual_name": "pYTmej",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 5,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Record Type",
                            "name": "Record Type",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 5,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 4,
                                "x": 267,
                                "y": 34,
                                "width": 267,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Record Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 267,
                                    "y": 34,
                                    "width": 267,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "YbmvyYp",
                            "visual_name": "YbmvyYp",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 10,
                            "row": 2,
                            "colspan": 4,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Year",
                            "name": "Year",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 10,
                                "row": 2,
                                "colspan": 4,
                                "rowspan": 4,
                                "x": 533,
                                "y": 34,
                                "width": 213,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 533,
                                    "y": 34,
                                    "width": 213,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "YPBfGA",
                            "visual_name": "YPBfGA",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 14,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Month-Year",
                            "name": "Month-Year",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 14,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 4,
                                "x": 747,
                                "y": 34,
                                "width": 267,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Month-Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 747,
                                    "y": 34,
                                    "width": 267,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "WumAV",
                            "visual_name": "WumAV",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 19,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather_Condition",
                            "name": "Weather_Condition",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 19,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 4,
                                "x": 1013,
                                "y": 34,
                                "width": 267,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Weather_Condition",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1013,
                                    "y": 34,
                                    "width": 267,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "QNDGVdb",
                            "visual_name": "QNDGVdb",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 6,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature",
                            "name": "Average Temperature",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 6,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 0,
                                "y": 103,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 103,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "ZksTVL",
                            "visual_name": "ZksTVL",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 6,
                            "row": 6,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Maximum Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Maximum Temperature",
                            "name": "Maximum Temperature",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 6,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 320,
                                "y": 103,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Maximum Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 103,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Maximum Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "JvJTedB",
                            "visual_name": "JvJTedB",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 6,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Precipitation",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Total Precipitation",
                            "name": "Total Precipitation",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 6,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 640,
                                "y": 103,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Precipitation",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 103,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Precipitation",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "mnCmjkJ",
                            "visual_name": "mnCmjkJ",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 18,
                            "row": 6,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Cities Monitored"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Cities Monitored",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Cities Monitored",
                            "name": "Cities Monitored",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 6,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 103,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Cities Monitored",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 103,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Cities Monitored"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Cities Monitored",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jRqXyp",
                            "visual_name": "jRqXyp",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 9,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "lineChart",
                            "bi_type": "lineChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature Trend",
                            "name": "Average Temperature Trend",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 9,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 0,
                                "y": 154,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "Average Temperature Trend",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 154,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10,
                                        "logarithmic": false
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "NuqCJea",
                            "visual_name": "NuqCJea",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 9,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature by City",
                            "name": "Average Temperature by City",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 9,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 640,
                                "y": 154,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Average Temperature by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 154,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "LvSNThL",
                            "visual_name": "LvSNThL",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 15,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Count(City)"
                            ],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Conditions",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather Conditions",
                            "name": "Weather Conditions",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 15,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 257,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Weather Conditions",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 257,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Count(City)"
                            ],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Conditions",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "components": [
                                    {
                                        "key": "general"
                                    }
                                ],
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "JJFwBL",
                            "visual_name": "JJFwBL",
                            "object_category": "chart",
                            "chart_type": "combochart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 15,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation",
                                "Average Temperature"
                            ],
                            "x_axis": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature & Precipitation Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "lineClusteredColumnComboChart",
                            "bi_type": "lineClusteredColumnComboChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Temperature & Precipitation Trend",
                            "name": "Temperature & Precipitation Trend",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 15,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 257,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineClusteredColumnComboChart",
                                "title": {
                                    "text": "Temperature & Precipitation Trend",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 257,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'combochart' visual maps directly to Fabric 'lineClusteredColumnComboChart' visual.",
                            "y_axis_fields": [
                                "Total Precipitation",
                                "Average Temperature"
                            ],
                            "x_axis_fields": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature & Precipitation Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "axis": 0,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    },
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'combochart' visual maps directly to Fabric 'lineClusteredColumnComboChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "CuXvsKp",
                            "visual_name": "CuXvsKp",
                            "object_category": "other",
                            "chart_type": "sn-table",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 20,
                            "colspan": 24,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "City",
                                "Date",
                                "Record Type",
                                "Weather_Condition",
                                "Temperature",
                                "Temp_Max",
                                "Temp_Min",
                                "Precipitation"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Data Details",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "tableEx",
                            "bi_type": "tableEx",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather Data Details",
                            "name": "Weather Data Details",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 20,
                                "colspan": 24,
                                "rowspan": 6,
                                "x": 0,
                                "y": 343,
                                "width": 1280,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "tableEx",
                                "title": {
                                    "text": "Weather Data Details",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 343,
                                    "width": 1280,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "City",
                                "Date",
                                "Record Type",
                                "Weather_Condition",
                                "Temperature",
                                "Temp_Max",
                                "Temp_Min",
                                "Precipitation"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Data Details",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                },
                                "null_value_representation": {
                                    "text": "-"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual."
                        }
                    }
                ]
            },
            {
                "sheet_id": "RpszwC",
                "title": "Temperature Analysis",
                "visualization_count": 15,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "JDqmPzF",
                            "visual_name": "JDqmPzF",
                            "object_category": "other",
                            "chart_type": "text-image",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 24,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "TEMPERATURE ANALYSIS",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "textbox",
                            "bi_type": "textbox",
                            "supported": true,
                            "status": "mapped",
                            "title": "TEMPERATURE ANALYSIS",
                            "name": "TEMPERATURE ANALYSIS",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 24,
                                "rowspan": 2,
                                "x": 0,
                                "y": 0,
                                "width": 1280,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "textbox",
                                "title": {
                                    "text": "TEMPERATURE ANALYSIS",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 1280,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "TEMPERATURE ANALYSIS",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "GneYPhR",
                            "visual_name": "GneYPhR",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "City",
                            "name": "City",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 0,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "EYg",
                            "visual_name": "EYg",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 6,
                            "row": 2,
                            "colspan": 7,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Record Type",
                            "name": "Record Type",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 2,
                                "colspan": 7,
                                "rowspan": 3,
                                "x": 320,
                                "y": 34,
                                "width": 373,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Record Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 34,
                                    "width": 373,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "VZLmXX",
                            "visual_name": "VZLmXX",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 13,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Year",
                            "name": "Year",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 13,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 693,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 693,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "LjYvLK",
                            "visual_name": "LjYvLK",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 19,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Month-Year",
                            "name": "Month-Year",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 19,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 3,
                                "x": 1013,
                                "y": 34,
                                "width": 267,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Month-Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1013,
                                    "y": 34,
                                    "width": 267,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "yfXjh",
                            "visual_name": "yfXjh",
                            "object_category": "other",
                            "chart_type": "gauge",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 5,
                            "colspan": 9,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "gauge",
                            "bi_type": "gauge",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature",
                            "name": "Average Temperature",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 5,
                                "colspan": 9,
                                "rowspan": 6,
                                "x": 0,
                                "y": 86,
                                "width": 480,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "gauge",
                                "title": {
                                    "text": "Average Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 86,
                                    "width": 480,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "palette_scheme": "qlik_default_12",
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "colorScheme": {
                                    "useBaseColors": "measure",
                                    "mode": "primary",
                                    "auto": true
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "measure_axis": {
                                        "min": 0,
                                        "max": 100,
                                        "show": "all",
                                        "spacing": 1
                                    }
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jCxMjr",
                            "visual_name": "jCxMjr",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 18,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Minimum Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Minimum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Minimum Temperature",
                            "name": "Minimum Temperature",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Minimum Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Minimum Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Minimum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "fzuMt",
                            "visual_name": "fzuMt",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 18,
                            "row": 8,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Maximum Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Maximum Temperature",
                            "name": "Maximum Temperature",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 8,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 137,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Maximum Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 137,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Maximum Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "YmbEAfn",
                            "visual_name": "YmbEAfn",
                            "object_category": "other",
                            "chart_type": "gauge",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 9,
                            "row": 5,
                            "colspan": 9,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Temperature Range"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Temperature Range",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "gauge",
                            "bi_type": "gauge",
                            "supported": true,
                            "status": "mapped",
                            "title": "Temperature Range",
                            "name": "Temperature Range",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 9,
                                "row": 5,
                                "colspan": 9,
                                "rowspan": 6,
                                "x": 480,
                                "y": 86,
                                "width": 480,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "gauge",
                                "title": {
                                    "text": "Temperature Range",
                                    "visible": true
                                },
                                "general": {
                                    "x": 480,
                                    "y": 86,
                                    "width": 480,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                            "y_axis_fields": [
                                "Temperature Range"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Temperature Range",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "palette_scheme": "qlik_default_12",
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "colorScheme": {
                                    "useBaseColors": "measure",
                                    "mode": "primary",
                                    "auto": true
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "measure_axis": {
                                        "min": 0,
                                        "max": 100,
                                        "show": "all",
                                        "spacing": 1
                                    }
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "LGvwDWQ",
                            "visual_name": "LGvwDWQ",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 11,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "lineChart",
                            "bi_type": "lineChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature Trend",
                            "name": "Average Temperature Trend",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 11,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 0,
                                "y": 189,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "Average Temperature Trend",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 189,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10,
                                        "logarithmic": false
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "PhFvet",
                            "visual_name": "PhFvet",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 11,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Minimum Temperature",
                                "Maximum Temperature"
                            ],
                            "x_axis": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Minimum vs Maximum Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "lineChart",
                            "bi_type": "lineChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Minimum vs Maximum Temperature",
                            "name": "Minimum vs Maximum Temperature",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 11,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 640,
                                "y": 189,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "Minimum vs Maximum Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 189,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "Minimum Temperature",
                                "Maximum Temperature"
                            ],
                            "x_axis_fields": [
                                "Date"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Minimum vs Maximum Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10,
                                        "logarithmic": false
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    },
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "PZsAh",
                            "visual_name": "PZsAh",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 17,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature by City",
                            "name": "Average Temperature by City",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 17,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 291,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Average Temperature by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 291,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "pAcEMx",
                            "visual_name": "pAcEMx",
                            "object_category": "other",
                            "chart_type": "histogram",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 17,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Temperature"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature Distribution",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "columnChart",
                            "bi_type": "columnChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Temperature Distribution",
                            "name": "Temperature Distribution",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 17,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 291,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "columnChart",
                                "title": {
                                    "text": "Temperature Distribution",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 291,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'histogram' visual maps directly to Fabric 'columnChart' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Temperature"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature Distribution",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "bar": {
                                        "paletteColor": {
                                            "index": 6,
                                            "color": "#4477aa"
                                        }
                                    }
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near"
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'histogram' visual maps directly to Fabric 'columnChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "WgJGPG",
                            "visual_name": "WgJGPG",
                            "object_category": "other",
                            "chart_type": "scatterplot",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 22,
                            "colspan": 24,
                            "rowspan": 8,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature",
                                "Average Precipitation"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature vs Precipitation by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "scatterChart",
                            "bi_type": "scatterChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Temperature vs Precipitation by City",
                            "name": "Temperature vs Precipitation by City",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 22,
                                "colspan": 24,
                                "rowspan": 8,
                                "x": 0,
                                "y": 377,
                                "width": 1280,
                                "height": 137
                            },
                            "power_bi_visual_type": {
                                "visualType": "scatterChart",
                                "title": {
                                    "text": "Temperature vs Precipitation by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 377,
                                    "width": 1280,
                                    "height": 137
                                }
                            },
                            "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual.",
                            "y_axis_fields": [
                                "Average Temperature",
                                "Average Precipitation"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature vs Precipitation by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    },
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "labels": {
                                    "mode": 1
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "DpesV",
                            "visual_name": "DpesV",
                            "object_category": "other",
                            "chart_type": "boxplot",
                            "sheet_name": "Temperature Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 30,
                            "colspan": 24,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Avg(Temperature)"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature Distribution by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "boxPlot",
                            "bi_type": "boxPlot",
                            "supported": true,
                            "status": "mapped",
                            "title": "Temperature Distribution by City",
                            "name": "Temperature Distribution by City",
                            "object_category": "standard",
                            "sheet_name": "Temperature Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 30,
                                "colspan": 24,
                                "rowspan": 6,
                                "x": 0,
                                "y": 514,
                                "width": 1280,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "boxPlot",
                                "title": {
                                    "text": "Temperature Distribution by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 514,
                                    "width": 1280,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual.",
                            "y_axis_fields": [
                                "Avg(Temperature)"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Temperature Distribution by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near"
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual."
                        }
                    }
                ]
            },
            {
                "sheet_id": "gPYXUP",
                "title": "Precipitation & Weather Analysis",
                "visualization_count": 18,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jwbHr",
                            "visual_name": "jwbHr",
                            "object_category": "other",
                            "chart_type": "text-image",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 24,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "PRECIPITATION & WEATHER",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "textbox",
                            "bi_type": "textbox",
                            "supported": true,
                            "status": "mapped",
                            "title": "PRECIPITATION & WEATHER",
                            "name": "PRECIPITATION & WEATHER",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 24,
                                "rowspan": 2,
                                "x": 0,
                                "y": 0,
                                "width": 1280,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "textbox",
                                "title": {
                                    "text": "PRECIPITATION & WEATHER",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 1280,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "PRECIPITATION & WEATHER",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "bzrJadX",
                            "visual_name": "bzrJadX",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "City",
                            "name": "City",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 3,
                                "x": 0,
                                "y": 34,
                                "width": 267,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 34,
                                    "width": 267,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "BKgyyJ",
                            "visual_name": "BKgyyJ",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 5,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Record Type",
                            "name": "Record Type",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 5,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 3,
                                "x": 267,
                                "y": 34,
                                "width": 267,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Record Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 267,
                                    "y": 34,
                                    "width": 267,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "puPXJMe",
                            "visual_name": "puPXJMe",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 10,
                            "row": 2,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Year",
                            "name": "Year",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 10,
                                "row": 2,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 533,
                                "y": 34,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 533,
                                    "y": 34,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "PPJHbjc",
                            "visual_name": "PPJHbjc",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 14,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Month-Year",
                            "name": "Month-Year",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 14,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 3,
                                "x": 747,
                                "y": 34,
                                "width": 267,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Month-Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 747,
                                    "y": 34,
                                    "width": 267,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Month-Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "LPeGw",
                            "visual_name": "LPeGw",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 19,
                            "row": 2,
                            "colspan": 5,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather_Condition",
                            "name": "Weather_Condition",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 19,
                                "row": 2,
                                "colspan": 5,
                                "rowspan": 3,
                                "x": 1013,
                                "y": 34,
                                "width": 267,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Weather_Condition",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1013,
                                    "y": 34,
                                    "width": 267,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "dQWmpm",
                            "visual_name": "dQWmpm",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Total Precipitation (mm)",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Total Precipitation (mm)",
                            "name": "Total Precipitation (mm)",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 0,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Precipitation (mm)",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Total Precipitation (mm)",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": true
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "CXrXTJ",
                            "visual_name": "CXrXTJ",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 6,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Precipitation"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Precipitation (mm)",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Precipitation (mm)",
                            "name": "Average Precipitation (mm)",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 320,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Precipitation (mm)",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Precipitation"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Precipitation (mm)",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": true
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "tPVf",
                            "visual_name": "tPVf",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Rainy Records"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Rainy Records",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Rainy Records",
                            "name": "Rainy Records",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 640,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Rainy Records",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Rainy Records"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Rainy Records",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": true
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jFZexU",
                            "visual_name": "jFZexU",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 18,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Weather Records"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Records",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather Records",
                            "name": "Weather Records",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Weather Records",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Weather Records"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Records",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": true
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.00",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "HXtNcM",
                            "visual_name": "HXtNcM",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 8,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation"
                            ],
                            "x_axis": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Monthly Precipitation Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "lineChart",
                            "bi_type": "lineChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Monthly Precipitation Trend",
                            "name": "Monthly Precipitation Trend",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 8,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 0,
                                "y": 137,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "Monthly Precipitation Trend",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 137,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Monthly Precipitation Trend",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10,
                                        "logarithmic": false
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "PKrnduH",
                            "visual_name": "PKrnduH",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 8,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Precipitation by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Precipitation by City",
                            "name": "Precipitation by City",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 8,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 640,
                                "y": 137,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Precipitation by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 137,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Precipitation by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "PYpyRVX",
                            "visual_name": "PYpyRVX",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 14,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Count(City)"
                            ],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Condition Frequency",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather Condition Frequency",
                            "name": "Weather Condition Frequency",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 14,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 240,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Weather Condition Frequency",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 240,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Count(City)"
                            ],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Condition Frequency",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "UrPWmk",
                            "visual_name": "UrPWmk",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 14,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Sum(Precipitation)"
                            ],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Precipitation by Weather Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Precipitation by Weather Condition",
                            "name": "Precipitation by Weather Condition",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 14,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 240,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Precipitation by Weather Condition",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 240,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Sum(Precipitation)"
                            ],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Precipitation by Weather Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "mxryL",
                            "visual_name": "mxryL",
                            "object_category": "other",
                            "chart_type": "distributionplot",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 19,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Historical Precipitation",
                                "Historical Precipitation"
                            ],
                            "x_axis": [
                                "Month-Year",
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Historical vs Forecast Precipitation",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "scatterChart",
                            "bi_type": "scatterChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Historical vs Forecast Precipitation",
                            "name": "Historical vs Forecast Precipitation",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 19,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 326,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "scatterChart",
                                "title": {
                                    "text": "Historical vs Forecast Precipitation",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 326,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'distributionplot' visual maps directly to Fabric 'scatterChart' visual.",
                            "y_axis_fields": [
                                "Historical Precipitation",
                                "Historical Precipitation"
                            ],
                            "x_axis_fields": [
                                "Month-Year",
                                "Month-Year"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Historical vs Forecast Precipitation",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useMeasureGradient": true,
                                    "point": {
                                        "auto": true,
                                        "mode": "primary",
                                        "useBaseColors": "off",
                                        "paletteColor": {
                                            "index": 6
                                        },
                                        "useDimColVal": true,
                                        "persistent": false,
                                        "expressionIsColor": true,
                                        "measureScheme": "sg",
                                        "reverseScheme": false,
                                        "dimensionScheme": "12",
                                        "autoMinMax": true,
                                        "measureMin": 0,
                                        "measureMax": 10
                                    },
                                    "box": {
                                        "paletteColor": {
                                            "color": "#e6e6e6",
                                            "index": -1
                                        }
                                    }
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    },
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'distributionplot' visual maps directly to Fabric 'scatterChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "sqMeV",
                            "visual_name": "sqMeV",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 24,
                            "colspan": 24,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Count({<Rain_Flag={1}>} DISTINCT Date)"
                            ],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Rainy Days by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "barChart",
                            "bi_type": "barChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Rainy Days by City",
                            "name": "Rainy Days by City",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 24,
                                "colspan": 24,
                                "rowspan": 6,
                                "x": 0,
                                "y": 411,
                                "width": 1280,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Rainy Days by City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 411,
                                    "width": 1280,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Count({<Rain_Flag={1}>} DISTINCT Date)"
                            ],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Rainy Days by City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "axes": {
                                    "dimension_axis": {
                                        "continuousAuto": true,
                                        "show": "all",
                                        "label": "auto",
                                        "dock": "near",
                                        "axisDisplayMode": "auto",
                                        "maxVisibleItems": 10
                                    },
                                    "measure_axis": {
                                        "show": "all",
                                        "dock": "near",
                                        "spacing": 1,
                                        "autoMinMax": true,
                                        "minMax": "min",
                                        "min": 0,
                                        "max": 10
                                    },
                                    "gridlines": {
                                        "auto": true,
                                        "spacing": 2
                                    }
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "vertical",
                                "bar_grouping": {
                                    "grouping": "grouped"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "namAbjW",
                            "visual_name": "namAbjW",
                            "object_category": "other",
                            "chart_type": "treemap",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 30,
                            "colspan": 24,
                            "rowspan": 9,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Count(City)"
                            ],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Condition Distribution",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "treemap",
                            "bi_type": "treemap",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather Condition Distribution",
                            "name": "Weather Condition Distribution",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 30,
                                "colspan": 24,
                                "rowspan": 9,
                                "x": 0,
                                "y": 514,
                                "width": 1280,
                                "height": 154
                            },
                            "power_bi_visual_type": {
                                "visualType": "treemap",
                                "title": {
                                    "text": "Weather Condition Distribution",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 514,
                                    "width": 1280,
                                    "height": 154
                                }
                            },
                            "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                            "y_axis_fields": [
                                "Count(City)"
                            ],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Weather Condition Distribution",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false,
                                    "dock": "auto"
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "auto": true,
                                "mode": "primary",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": true,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10
                                },
                                "data_colors": {
                                    "mode": "primary",
                                    "auto": true
                                },
                                "legend": {
                                    "show": false,
                                    "dock": "auto"
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "labels": {
                                    "auto": true,
                                    "headers": true,
                                    "overlay": true,
                                    "leaves": true,
                                    "values": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "JGksv",
                            "visual_name": "JGksv",
                            "object_category": "other",
                            "chart_type": "gauge",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 19,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "gauge",
                            "bi_type": "gauge",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature",
                            "name": "Average Temperature",
                            "object_category": "standard",
                            "sheet_name": "Precipitation & Weather Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 19,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 326,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "gauge",
                                "title": {
                                    "text": "Average Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 326,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "useBaseColors": "measure"
                                },
                                "axes": {
                                    "measure_axis": {
                                        "min": 0,
                                        "max": 100,
                                        "show": "all",
                                        "spacing": 1
                                    }
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "orientation": "horizontal"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'gauge' visual maps directly to Fabric 'gauge' visual."
                        }
                    }
                ]
            },
            {
                "sheet_id": "BhGdWU",
                "title": "Geographic Analysis",
                "visualization_count": 11,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "mVnpjq",
                            "visual_name": "mVnpjq",
                            "object_category": "other",
                            "chart_type": "text-image",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 24,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Text-Image",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "textbox",
                            "bi_type": "textbox",
                            "supported": true,
                            "status": "mapped",
                            "title": "Text-Image",
                            "name": "Text-Image",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 24,
                                "rowspan": 2,
                                "x": 0,
                                "y": 0,
                                "width": 1280,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "textbox",
                                "title": {
                                    "text": "Text-Image",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 1280,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Text-Image",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'text-image' visual maps directly to Fabric 'textbox' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "apzrRt",
                            "visual_name": "apzrRt",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "City",
                            "name": "City",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 0,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "City",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "City"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "City",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "mSfQc",
                            "visual_name": "mSfQc",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 6,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Record Type",
                            "name": "Record Type",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 320,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Record Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Record Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Record Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "eqDgtEL",
                            "visual_name": "eqDgtEL",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Year",
                            "name": "Year",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 640,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Year",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Year"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Year",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "TmcWUs",
                            "visual_name": "TmcWUs",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 18,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "Weather_Condition",
                            "name": "Weather_Condition",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 2,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 34,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Weather_Condition",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 34,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Weather_Condition"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Weather_Condition",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "ZgPuTS",
                            "visual_name": "ZgPuTS",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature",
                            "name": "Average Temperature",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 0,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jMmUXA",
                            "visual_name": "jMmUXA",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 6,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Maximum Temperature"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Maximum Temperature",
                            "name": "Maximum Temperature",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 320,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Maximum Temperature",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Maximum Temperature"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Maximum Temperature",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "jVeANM",
                            "visual_name": "jVeANM",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 12,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Precipitation"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Precipitation",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Total Precipitation",
                            "name": "Total Precipitation",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 640,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Precipitation",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Precipitation",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "NePj",
                            "visual_name": "NePj",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 18,
                            "row": 5,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Cities Monitored"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Cities Monitored",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "card",
                            "bi_type": "card",
                            "supported": true,
                            "status": "mapped",
                            "title": "Cities Monitored",
                            "name": "Cities Monitored",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 18,
                                "row": 5,
                                "colspan": 6,
                                "rowspan": 3,
                                "x": 960,
                                "y": 86,
                                "width": 320,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Cities Monitored",
                                    "visible": true
                                },
                                "general": {
                                    "x": 960,
                                    "y": 86,
                                    "width": 320,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Cities Monitored"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Cities Monitored",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "font_size": "M",
                                    "show": false
                                },
                                "kpi": {
                                    "align": "center"
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    }
                                ],
                                "text_align": "center",
                                "fontSize": "M"
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "dQDeKpZ",
                            "visual_name": "dQDeKpZ",
                            "object_category": "other",
                            "chart_type": "map",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 8,
                            "colspan": 24,
                            "rowspan": 8,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Longitude_Latitude"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by Location",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "map",
                            "bi_type": "map",
                            "supported": true,
                            "status": "mapped",
                            "title": "Average Temperature by Location",
                            "name": "Average Temperature by Location",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 8,
                                "colspan": 24,
                                "rowspan": 8,
                                "x": 0,
                                "y": 137,
                                "width": 1280,
                                "height": 137
                            },
                            "power_bi_visual_type": {
                                "visualType": "map",
                                "title": {
                                    "text": "Average Temperature by Location",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 137,
                                    "width": 1280,
                                    "height": 137
                                }
                            },
                            "rationale": "The Qlik Sense 'map' visual maps directly to Fabric 'map' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Longitude_Latitude"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Average Temperature by Location",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'map' visual maps directly to Fabric 'map' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "FhNaRL",
                            "visual_name": "FhNaRL",
                            "object_category": "other",
                            "chart_type": "sn-table",
                            "sheet_name": "Geographic Analysis",
                            "layout": {},
                            "col": 0,
                            "row": 16,
                            "colspan": 24,
                            "rowspan": 7,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Temperature",
                                "Maximum Temperature",
                                "Total Precipitation"
                            ],
                            "x_axis": [
                                "City",
                                "Latitude",
                                "Longitude"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Geographic Weather Details",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "tableEx",
                            "bi_type": "tableEx",
                            "supported": true,
                            "status": "mapped",
                            "title": "Geographic Weather Details",
                            "name": "Geographic Weather Details",
                            "object_category": "standard",
                            "sheet_name": "Geographic Analysis",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 16,
                                "colspan": 24,
                                "rowspan": 7,
                                "x": 0,
                                "y": 274,
                                "width": 1280,
                                "height": 120
                            },
                            "power_bi_visual_type": {
                                "visualType": "tableEx",
                                "title": {
                                    "text": "Geographic Weather Details",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 274,
                                    "width": 1280,
                                    "height": 120
                                }
                            },
                            "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                            "y_axis_fields": [
                                "Average Temperature",
                                "Maximum Temperature",
                                "Total Precipitation"
                            ],
                            "x_axis_fields": [
                                "City",
                                "Latitude",
                                "Longitude"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Geographic Weather Details",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            },
                            "kpi_styling": {
                                "value_font_family": "Segoe UI, sans-serif",
                                "label_font_family": "Segoe UI, sans-serif",
                                "align": "center"
                            },
                            "color": {
                                "is_multicolor": false,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "legend": {
                                    "show": false
                                },
                                "number_formats": [
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    },
                                    {
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
                                    },
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "#,##0.0",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "null_value_representation": {
                                    "text": "-"
                                }
                            },
                            "custom_coloring": {},
                            "reference_lines": []
                        },
                        "confidence": {
                            "score": 0.95,
                            "band": "high",
                            "llm_score": 0.95,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "pass"
                                }
                            ],
                            "penalties": [],
                            "requires_review": false,
                            "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual."
                        }
                    }
                ]
            }
        ]
    },
    "filters": [
        {
            "name": "City",
            "qlik_source": {
                "name": "City",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Record_Type",
            "qlik_source": {
                "name": "Record_Type",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Year",
            "qlik_source": {
                "name": "Year",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Observation_Time.autoCalendar.YearMonth",
            "qlik_source": {
                "name": "Observation_Time.autoCalendar.YearMonth",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Weather_Condition",
            "qlik_source": {
                "name": "Weather_Condition",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "City",
            "qlik_source": {
                "name": "City",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Record_Type",
            "qlik_source": {
                "name": "Record_Type",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Year",
            "qlik_source": {
                "name": "Year",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Observation_Time.autoCalendar.YearMonth",
            "qlik_source": {
                "name": "Observation_Time.autoCalendar.YearMonth",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "City",
            "qlik_source": {
                "name": "City",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Record_Type",
            "qlik_source": {
                "name": "Record_Type",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Year",
            "qlik_source": {
                "name": "Year",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Observation_Time.autoCalendar.YearMonth",
            "qlik_source": {
                "name": "Observation_Time.autoCalendar.YearMonth",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Weather_Condition",
            "qlik_source": {
                "name": "Weather_Condition",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "City",
            "qlik_source": {
                "name": "City",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Record_Type",
            "qlik_source": {
                "name": "Record_Type",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Year",
            "qlik_source": {
                "name": "Year",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        },
        {
            "name": "Weather_Condition",
            "qlik_source": {
                "name": "Weather_Condition",
                "field": null,
                "sheet_name": null
            },
            "fabric": {
                "filter_scope": "report",
                "target_table": null,
                "target_column": null,
                "sheet_name": null,
                "powerbi_filter_type": "categorical",
                "replacement_strategy": "Field 'None' did not match any column in the mapped tables. Confirm the field name against the source schema (it may live in a table that failed to load, or under a different alias), then add it as a slicer bound to the correct table.column manually."
            },
            "confidence": {
                "score": 0.4,
                "score_out_of_100": 40,
                "percentage": "40%",
                "band": "low",
                "llm_score": 0.4,
                "checks": [
                    {
                        "id": "filter_field_resolved",
                        "status": "fail"
                    }
                ],
                "penalties": [
                    "Unresolved field 'None'"
                ],
                "requires_review": true,
                "rationale": "Filter field 'None' could not be resolved against any known table column; left unbound."
            }
        }
    ],
    "limitations": [],
    "variables": {
        "count": 29,
        "converted_items": [
            {
                "id": "d726b562-5eea-41c8-9e5f-e961e70e132b",
                "name": "DateFormat",
                "definition": "M/D/YYYY",
                "value": "M/D/YYYY",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DateFormat='M/D/YYYY';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "d726b562-5eea-41c8-9e5f-e961e70e132b",
                    "qType": "variable"
                }
            },
            {
                "id": "e67cd8a7-0f66-4cb8-9ae6-504772537e3a",
                "name": "FirstMonthOfYear",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET FirstMonthOfYear=1;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "e67cd8a7-0f66-4cb8-9ae6-504772537e3a",
                    "qType": "variable"
                }
            },
            {
                "id": "ebb36033-d5c1-4851-b366-603e1bc1ea84",
                "name": "StripComments",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "ebb36033-d5c1-4851-b366-603e1bc1ea84",
                    "qType": "variable"
                }
            },
            {
                "id": "79dbeffa-2539-46e2-94e1-00da06d28066",
                "name": "DecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "79dbeffa-2539-46e2-94e1-00da06d28066",
                    "qType": "variable"
                }
            },
            {
                "id": "c97f1baa-748d-4165-9f7f-80df3b43f80b",
                "name": "MoneyThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "c97f1baa-748d-4165-9f7f-80df3b43f80b",
                    "qType": "variable"
                }
            },
            {
                "id": "447e3348-caf7-4bbf-9e70-7b51a68f0aa7",
                "name": "CreateSearchIndexOnReload",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET CreateSearchIndexOnReload=1;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "447e3348-caf7-4bbf-9e70-7b51a68f0aa7",
                    "qType": "variable"
                }
            },
            {
                "id": "2c207247-07c6-409f-9cc8-c567e8bc33d0",
                "name": "MonthNames",
                "definition": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "value": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "2c207247-07c6-409f-9cc8-c567e8bc33d0",
                    "qType": "variable"
                }
            },
            {
                "id": "c5c900f9-1e3d-441a-bfa2-1e923f44ce8e",
                "name": "LongMonthNames",
                "definition": "January;February;March;April;May;June;July;August;September;October;November;December",
                "value": "January;February;March;April;May;June;July;August;September;October;November;December",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "c5c900f9-1e3d-441a-bfa2-1e923f44ce8e",
                    "qType": "variable"
                }
            },
            {
                "id": "7825c30d-06f1-4674-bc4f-7fe57e7ff400",
                "name": "ThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET ThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "7825c30d-06f1-4674-bc4f-7fe57e7ff400",
                    "qType": "variable"
                }
            },
            {
                "id": "93d31d86-a640-4afb-83ac-076ff9a121f6",
                "name": "ScriptError",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "93d31d86-a640-4afb-83ac-076ff9a121f6",
                    "qType": "variable"
                }
            },
            {
                "id": "b447f4d9-0016-4105-be06-b202d51df5ca",
                "name": "currentName",
                "definition": "Weather_Data",
                "value": "Weather_Data",
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "script_line": "Let currentName = name;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "b447f4d9-0016-4105-be06-b202d51df5ca",
                    "qType": "variable"
                }
            },
            {
                "id": "fea4b67c-512b-4e3f-be3f-9047f3e55a5f",
                "name": "ErrorMode",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "fea4b67c-512b-4e3f-be3f-9047f3e55a5f",
                    "qType": "variable"
                }
            },
            {
                "id": "00c83192-c183-4620-960c-22d64fead510",
                "name": "BrokenWeeks",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET BrokenWeeks=1;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "00c83192-c183-4620-960c-22d64fead510",
                    "qType": "variable"
                }
            },
            {
                "id": "088c1f33-46f3-4b1d-8fa3-05b949816fbd",
                "name": "ScriptErrorList",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "088c1f33-46f3-4b1d-8fa3-05b949816fbd",
                    "qType": "variable"
                }
            },
            {
                "id": "705cdc30-7a2b-4e97-9ef5-d200a08eee6f",
                "name": "MoneyFormat",
                "definition": "$ ###0.00;-$ ###0.00",
                "value": "$ ###0.00;-$ ###0.00",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyFormat='$ ###0.00;-$ ###0.00';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "705cdc30-7a2b-4e97-9ef5-d200a08eee6f",
                    "qType": "variable"
                }
            },
            {
                "id": "ad217f6b-da67-4bc8-b14c-7713c269f48b",
                "name": "TimestampFormat",
                "definition": "M/D/YYYY h\\:mm\\:ss TT",
                "value": "M/D/YYYY h\\:mm\\:ss TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimestampFormat='M/D/YYYY h\\:mm\\:ss TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "ad217f6b-da67-4bc8-b14c-7713c269f48b",
                    "qType": "variable"
                }
            },
            {
                "id": "c4d66108-5aae-4b65-92e0-0c6c9f721afc",
                "name": "ReferenceDay",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET ReferenceDay=0;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "c4d66108-5aae-4b65-92e0-0c6c9f721afc",
                    "qType": "variable"
                }
            },
            {
                "id": "adf6adcd-bd63-456a-85bc-203815184ea8",
                "name": "name",
                "definition": "Weather_Data",
                "value": "Weather_Data",
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "used_in_sheets": [
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis"
                    }
                ],
                "used_in_visualizations": [
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "DpesV",
                        "visualization_title": "Temperature Distribution by City",
                        "visualization_type": "boxplot"
                    }
                ],
                "usage_count": 2,
                "qInfo": {
                    "qId": "adf6adcd-bd63-456a-85bc-203815184ea8",
                    "qType": "variable"
                }
            },
            {
                "id": "96f4e19f-9662-4867-b389-96f63107846c",
                "name": "LongDayNames",
                "definition": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "value": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "96f4e19f-9662-4867-b389-96f63107846c",
                    "qType": "variable"
                }
            },
            {
                "id": "460432fe-3317-40e9-ae94-efe0150e43cc",
                "name": "FirstWeekDay",
                "definition": "6",
                "value": "6",
                "num_value": 6,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET FirstWeekDay=6;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "460432fe-3317-40e9-ae94-efe0150e43cc",
                    "qType": "variable"
                }
            },
            {
                "id": "38596f77-4efc-49b6-894f-70539a5a79a2",
                "name": "ScriptErrorCount",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "38596f77-4efc-49b6-894f-70539a5a79a2",
                    "qType": "variable"
                }
            },
            {
                "id": "9886cebb-62b4-4449-a226-3f0f2cca0198",
                "name": "MoneyDecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyDecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "9886cebb-62b4-4449-a226-3f0f2cca0198",
                    "qType": "variable"
                }
            },
            {
                "id": "fdf18d96-f4f9-4f85-b58e-a9ce3055829d",
                "name": "TimeFormat",
                "definition": "h\\:mm\\:ss TT",
                "value": "h\\:mm\\:ss TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimeFormat='h\\:mm\\:ss TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "fdf18d96-f4f9-4f85-b58e-a9ce3055829d",
                    "qType": "variable"
                }
            },
            {
                "id": "276d1dc2-2252-4e4b-a6c1-1fd53b5b9272",
                "name": "matches",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "script_line": "Let matches = 0;",
                "usage_count": 0,
                "qInfo": {
                    "qId": "276d1dc2-2252-4e4b-a6c1-1fd53b5b9272",
                    "qType": "variable"
                }
            },
            {
                "id": "5eff3430-1b0b-43e1-b4e6-b353d356605f",
                "name": "index",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "script_line": "Let index = 0;",
                "used_in_sheets": [
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis"
                    }
                ],
                "used_in_visualizations": [
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "QNDGVdb",
                        "visualization_title": "Average Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "ZksTVL",
                        "visualization_title": "Maximum Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "JvJTedB",
                        "visualization_title": "Total Precipitation",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "mnCmjkJ",
                        "visualization_title": "Cities Monitored",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "jRqXyp",
                        "visualization_title": "Average Temperature Trend",
                        "visualization_type": "linechart"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "NuqCJea",
                        "visualization_title": "Average Temperature by City",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "LvSNThL",
                        "visualization_title": "Weather Conditions",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "paKLEj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "JJFwBL",
                        "visualization_title": "Temperature & Precipitation Trend",
                        "visualization_type": "combochart"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "yfXjh",
                        "visualization_title": "Average Temperature",
                        "visualization_type": "gauge"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "jCxMjr",
                        "visualization_title": "Minimum Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "fzuMt",
                        "visualization_title": "Maximum Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "YmbEAfn",
                        "visualization_title": "Temperature Range",
                        "visualization_type": "gauge"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "LGvwDWQ",
                        "visualization_title": "Average Temperature Trend",
                        "visualization_type": "linechart"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "PhFvet",
                        "visualization_title": "Minimum vs Maximum Temperature",
                        "visualization_type": "linechart"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "PZsAh",
                        "visualization_title": "Average Temperature by City",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "pAcEMx",
                        "visualization_title": "Temperature Distribution",
                        "visualization_type": "histogram"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "WgJGPG",
                        "visualization_title": "Temperature vs Precipitation by City",
                        "visualization_type": "scatterplot"
                    },
                    {
                        "sheet_id": "RpszwC",
                        "sheet_title": "Temperature Analysis",
                        "visualization_id": "DpesV",
                        "visualization_title": "Temperature Distribution by City",
                        "visualization_type": "boxplot"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "dQWmpm",
                        "visualization_title": "Total Precipitation (mm)",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "CXrXTJ",
                        "visualization_title": "Average Precipitation (mm)",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "tPVf",
                        "visualization_title": "Rainy Records",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "jFZexU",
                        "visualization_title": "Weather Records",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "HXtNcM",
                        "visualization_title": "Monthly Precipitation Trend",
                        "visualization_type": "linechart"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "PKrnduH",
                        "visualization_title": "Precipitation by City",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "PYpyRVX",
                        "visualization_title": "Weather Condition Frequency",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "UrPWmk",
                        "visualization_title": "Precipitation by Weather Condition",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "mxryL",
                        "visualization_title": "Historical vs Forecast Precipitation",
                        "visualization_type": "distributionplot"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "sqMeV",
                        "visualization_title": "Rainy Days by City",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "namAbjW",
                        "visualization_title": "Weather Condition Distribution",
                        "visualization_type": "treemap"
                    },
                    {
                        "sheet_id": "gPYXUP",
                        "sheet_title": "Precipitation & Weather Analysis",
                        "visualization_id": "JGksv",
                        "visualization_title": "Average Temperature",
                        "visualization_type": "gauge"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "ZgPuTS",
                        "visualization_title": "Average Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "jMmUXA",
                        "visualization_title": "Maximum Temperature",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "jVeANM",
                        "visualization_title": "Total Precipitation",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "NePj",
                        "visualization_title": "Cities Monitored",
                        "visualization_type": "kpi"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "dQDeKpZ",
                        "visualization_title": "Average Temperature by Location",
                        "visualization_type": "map"
                    },
                    {
                        "sheet_id": "BhGdWU",
                        "sheet_title": "Geographic Analysis",
                        "visualization_id": "FhNaRL",
                        "visualization_title": "Geographic Weather Details",
                        "visualization_type": "sn-table"
                    }
                ],
                "usage_count": 40,
                "qInfo": {
                    "qId": "5eff3430-1b0b-43e1-b4e6-b353d356605f",
                    "qType": "variable"
                }
            },
            {
                "id": "7e32d301-8312-4b4c-a0bd-37744a3ae225",
                "name": "OpenUrlTimeout",
                "definition": "86400",
                "value": "86400",
                "num_value": 86400,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "7e32d301-8312-4b4c-a0bd-37744a3ae225",
                    "qType": "variable"
                }
            },
            {
                "id": "d15896ca-2a2d-4301-a688-1049cf4ebf38",
                "name": "DayNames",
                "definition": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "value": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "d15896ca-2a2d-4301-a688-1049cf4ebf38",
                    "qType": "variable"
                }
            },
            {
                "id": "263564a9-f28d-426d-b83b-f003e37493ac",
                "name": "NumericalAbbreviation",
                "definition": "3\\:k;6\\:M;9\\:G;12\\:T;15\\:P;18\\:E;21\\:Z;24\\:Y;-3\\:m;-6:μ;-9\\:n;-12\\:p;-15\\:f;-18\\:a;-21\\:z;-24\\:y",
                "value": "3\\:k;6\\:M;9\\:G;12\\:T;15\\:P;18\\:E;21\\:Z;24\\:Y;-3\\:m;-6:μ;-9\\:n;-12\\:p;-15\\:f;-18\\:a;-21\\:z;-24\\:y",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET NumericalAbbreviation='3\\:k;6\\:M;9\\:G;12\\:T;15\\:P;18\\:E;21\\:Z;24\\:Y;-3\\:m;-6:μ;-9\\:n;-12\\:p;-15\\:f;-18\\:a;-21\\:z;-24\\:y';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "263564a9-f28d-426d-b83b-f003e37493ac",
                    "qType": "variable"
                }
            },
            {
                "id": "27d0efcc-ad69-4b83-bd97-93f618915d7d",
                "name": "CollationLocale",
                "definition": "en-US",
                "value": "en-US",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET CollationLocale='en-US';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "27d0efcc-ad69-4b83-bd97-93f618915d7d",
                    "qType": "variable"
                }
            }
        ]
    },
    "section_access": {
        "count": 0,
        "converted_items": []
    },
    "stories": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No stories found"
    },
    "bookmarks": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No bookmarks found"
    },
    "themes": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No themes found"
    },
    "extensions": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No extensions found"
    },
    "master_item_tags": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No master_item_tags found"
    },
    "hypercube_samples": {
        "count": 0,
        "converted_items": []
    },
    "script": {},
    "data_load_editor": {},
    "fields": [],
    "rls": {},
    "data_model": {},
    "lineage": [],
    "limitations_summary": [],
    "object_inventory": {},
    "section_status": [],
    "extraction": {},
    "master_objects": [],
    "media": {
        "content_libraries": [
            {
                "name": "appcontent",
                "app_specific": true
            }
        ]
    },
    "snapshots": [],
    "data_files": [],
    "conversion_summary": {
        "total_items": 16,
        "converted": 16,
        "failed": 0,
        "confidence": 0.83,
        "confidence_score": 83,
        "confidence_percentage": "83%",
        "score_out_of_100": 83,
        "requires_review": true,
        "by_section": {
            "tables": {
                "total": 2,
                "converted": 2,
                "failed": 0
            },
            "measures": {
                "total": 14,
                "converted": 14,
                "failed": 0
            },
            "relationships": {
                "total": 0,
                "converted": 0,
                "failed": 0
            }
        },
        "dax_confidence_scores": [
            0.8,
            0.8,
            0.8,
            0.8,
            0.8,
            0.98,
            0.8,
            0.8,
            0.8,
            0.9,
            0.9,
            0.9,
            0.9,
            0.9
        ],
        "dax_count": 14
    },
    "llm_status": {
        "converted": true,
        "model": "groq:openai/gpt-oss-120b",
        "prompt_version": "2.0",
        "reason": "Mapping and conversion completed successfully with full Contract 2.0 formatting."
    },
    "source": "fresh"
}