{
    "status": "success",
    "message": "Generated 3 tables, 14 measures, 0 relationships, 4 pages, 59 visuals; needs review: 1 visual(s) substituted. | Successfully deployed to github ()",
    "target": "fabric",
    "deploy": "github",
    "app_id": "4f2a34e4-9e34-4213-b3e2-2ab1b212bc87",
    "app_name": "Weather Analytics",
    "run_id": "run-krle-test",
    "output_path": null,
    "file_count": 100,
    "summary": {
        "semantic_model": {
            "tables": 3,
            "measures": 14,
            "calculated_columns": 0,
            "relationships_written": 0,
            "relationships_skipped": [],
            "orphan_measures_table": false,
            "shared_expressions": [
                "Google_BigQuery_ordinal-avatar-497006-v6"
            ],
            "dax_needs_rewrite": 0,
            "dax_problems": []
        },
        "report": {
            "pages": 4,
            "visuals": 59,
            "native": 58,
            "substituted": 1,
            "manual": 0,
            "filters_applied": 0,
            "top_n_filters": 0,
            "categorical_filters": 0,
            "bookmarks": 0,
            "navigation_buttons": 16
        }
    },
    "visual_notes": [
        {
            "object_id": null,
            "sheet": "Temperature Analysis",
            "title": "Temperature Distribution by City",
            "qlik_type": "boxplot",
            "mapped_to": "columnChart",
            "severity": "substituted",
            "reason": "Power BI has no native box plot.",
            "suggestion": "Rendered as a column chart of the median. For true quartiles install the 'Box and Whisker chart' visual from AppSource, or add DAX measures for P25/P50/P75 and use an error-bar enabled visual."
        }
    ],
    "deployment": {
        "status": "success",
        "provider": "github",
        "repo": "krishnau2097-byte/Fabrics-Report-s",
        "branch": "main",
        "commit": "ff221c8995a1c2c792d947b7f04790db7eefd4c2",
        "path": "weather-analytics",
        "file_count": 100
    },
    "total_bytes": 191366,
    "validation": {
        "ok": true,
        "errors": [],
        "warnings": []
    },
    "artifacts": {
        "pbip": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",
            "version": "1.0",
            "artifacts": [
                {
                    "report": {
                        "path": "Weather Analytics.Report"
                    }
                }
            ],
            "settings": {
                "enableAutoRecovery": true
            }
        },
        "semantic_model": {
            ".pbi/diagramLayout.json": {
                "version": "1.0.0",
                "diagrams": [
                    {
                        "name": "All tables",
                        "zoomValue": 100,
                        "isDefault": true,
                        "tables": [],
                        "layout": {
                            "boundingBoxWidth": 0,
                            "boundingBoxHeight": 0,
                            "boundingBoxPosition": {
                                "x": 0,
                                "y": 0
                            },
                            "nodes": []
                        }
                    }
                ]
            },
            ".pbi/editorSettings.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/editorSettings/1.0.0/schema.json",
                "autodetectRelationships": true,
                "parallelQueryLoading": true,
                "typeDetectionEnabled": true,
                "relationshipImportEnabled": true,
                "shouldNotifyUserOfNameConflictResolution": true
            },
            ".pbi/localSettings.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/localSettings/1.1.0/schema.json",
                "userConsent": {
                    "compositeModel": true
                }
            },
            ".platform": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
                "metadata": {
                    "type": "SemanticModel",
                    "displayName": "Weather Analytics"
                },
                "config": {
                    "version": "2.0",
                    "logicalId": "ef51f684-2bf1-51e3-8c43-f503b5752ebc"
                }
            },
            "definition.pbism": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
                "version": "4.0",
                "settings": {}
            },
            "definition/cultures/en-US.tmdl": "cultureInfo en-US\n\tlinguisticMetadata =\n\t\t\t{\n\t\t\t  \"Version\": \"1.0.0\",\n\t\t\t  \"Language\": \"en-US\"\n\t\t\t}\n\t\tcontentType: json\n",
            "definition/database.tmdl": "database\n\tcompatibilityLevel: 1567\n",
            "definition/expressions.tmdl": "expression 'Google_BigQuery_ordinal-avatar-497006-v6' =\n\t\tlet\n\t\t    Source = Web.Contents(\"https://orcqwbokkvelxgmkagpz.supabase.co/storage/v1/object/public/migration-data-files\")\n\t\tin\n\t\t    Source\n\tlineageTag: d25a2bd4-7f6c-5e4f-9706-170e0663f36d\n\n\tannotation PBI_NavigationStepName = Navigation\n\n\tannotation PBI_ResultType = Table\n",
            "definition/model.tmdl": "model Model\n\tculture: en-US\n\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\tdiscourageImplicitMeasures\n\tsourceQueryCulture: en-US\n\n\tannotation PBI_QueryOrder = [\"Weather_Data\", \"WeatherCodeMap\", \"Parameters\"]\n\tannotation PBI_ProTooling = [\"DevMode\"]\n\nref table Weather_Data\nref table WeatherCodeMap\nref table Parameters\n\nref cultureInfo en-US\n",
            "definition/tables/Parameters.tmdl": "table Parameters\n\tlineageTag: 0fe49ea5-fe5c-5a45-9ff7-e50b75dc067a\n\n\tcolumn Parameter\n\t\tdataType: string\n\t\tlineageTag: 22a0bd0b-9463-5b42-9a2d-5cfbd1cf63df\n\t\tsummarizeBy: none\n\t\tsourceColumn: Parameter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Value\n\t\tdataType: string\n\t\tlineageTag: 70b4627b-915e-51c1-9f8a-945f135294b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: Value\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Label\n\t\tdataType: string\n\t\tlineageTag: 5946bfca-d13d-5640-80d8-f86e9e9334a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: Label\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Order\n\t\tdataType: int64\n\t\tlineageTag: 3a397789-8015-5220-bf8f-5696fa2e68c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: Order\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Parameters = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table(\n\t\t\t\t        type table [Parameter = text, Value = text, Label = text, #\"Order\" = Int64.Type],\n\t\t\t\t        {\n\t\t\t            {\"DateFormat\", \"M/D/YYYY\", \"DateFormat\", 1},\n\t\t\t            {\"FirstMonthOfYear\", \"1\", \"FirstMonthOfYear\", 2},\n\t\t\t            {\"StripComments\", \"1\", \"StripComments\", 3},\n\t\t\t            {\"DecimalSep\", \".\", \"DecimalSep\", 4},\n\t\t\t            {\"MoneyThousandSep\", \",\", \"MoneyThousandSep\", 5},\n\t\t\t            {\"CreateSearchIndexOnReload\", \"1\", \"CreateSearchIndexOnReload\", 6},\n\t\t\t            {\"MonthNames\", \"Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec\", \"MonthNames\", 7},\n\t\t\t            {\"LongMonthNames\", \"January;February;March;April;May;June;July;August;September;October;November;December\", \"LongMonthNames\", 8},\n\t\t\t            {\"ThousandSep\", \",\", \"ThousandSep\", 9},\n\t\t\t            {\"currentName\", \"Weather_Data\", \"currentName\", 10},\n\t\t\t            {\"ErrorMode\", \"1\", \"ErrorMode\", 11},\n\t\t\t            {\"BrokenWeeks\", \"1\", \"BrokenWeeks\", 12},\n\t\t\t            {\"MoneyFormat\", \"$ ###0.00;-$ ###0.00\", \"MoneyFormat\", 13},\n\t\t\t            {\"TimestampFormat\", \"M/D/YYYY h\\:mm\\:ss TT\", \"TimestampFormat\", 14},\n\t\t\t            {\"ReferenceDay\", \"0\", \"ReferenceDay\", 15},\n\t\t\t            {\"name\", \"Weather_Data\", \"name\", 16},\n\t\t\t            {\"LongDayNames\", \"Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday\", \"LongDayNames\", 17},\n\t\t\t            {\"FirstWeekDay\", \"6\", \"FirstWeekDay\", 18},\n\t\t\t            {\"ScriptErrorCount\", \"0\", \"ScriptErrorCount\", 19},\n\t\t\t            {\"MoneyDecimalSep\", \".\", \"MoneyDecimalSep\", 20},\n\t\t\t            {\"TimeFormat\", \"h\\:mm\\:ss TT\", \"TimeFormat\", 21},\n\t\t\t            {\"matches\", \"0\", \"matches\", 22},\n\t\t\t            {\"index\", \"0\", \"index\", 23},\n\t\t\t            {\"OpenUrlTimeout\", \"86400\", \"OpenUrlTimeout\", 24},\n\t\t\t            {\"DayNames\", \"Mon;Tue;Wed;Thu;Fri;Sat;Sun\", \"DayNames\", 25},\n\t\t\t            {\"NumericalAbbreviation\", \"3\\:k;6\\:M;9\\:G;12\\:T;15\\:P;18\\:E;21\\:Z;24\\:Y;-3\\:m;-6:μ;-9\\:n;-12\\:p;-15\\:f;-18\\:a;-21\\:z;-24\\:y\", \"NumericalAbbreviation\", 26},\n\t\t\t            {\"CollationLocale\", \"en-US\", \"CollationLocale\", 27}\n\t\t\t\t        }\n\t\t\t\t    )\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/WeatherCodeMap.tmdl": "table WeatherCodeMap\n\tlineageTag: 0f865172-4c2c-5b8d-9160-b1544c0758d1\n\n\tcolumn '*'\n\t\tdataType: double\n\t\tlineageTag: 636bb897-ee6d-53f1-86e3-21fbe5bc492e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: *\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition WeatherCodeMap = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"*\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Weather_Data.tmdl": "table Weather_Data\n\tlineageTag: dbd151ef-a8dd-5c97-8dae-3b7cf3f2dbb1\n\n\tmeasure 'Average Temperature' = AVERAGE('Weather_Data'[Temperature])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 715ee4c7-aacb-5079-8874-3168fbac245c\n\n\tmeasure 'Rainy Records' = CALCULATE(COUNT('Weather_Data'[City]), 'Weather_Data'[Rain_Flag] = \"1\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 32b53991-6abe-5396-9ffe-7f08b36b41f6\n\n\tmeasure 'Weather Records' = COUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 3f52af7c-2cb4-5481-ac0a-e817eaab92af\n\n\tmeasure 'Minimum Temperature' = MIN('Weather_Data'[Temp_Min])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c805e5fe-d1d7-5af1-91b1-8cee7cc2d401\n\n\tmeasure 'Maximum Temperature' = MAX('Weather_Data'[Temp_Max])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c5659451-09f4-5d18-8a26-78ee442a0cd5\n\n\tmeasure 'Total Precipitation' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 8f6cef07-481d-50a6-b76d-a9e682f7c013\n\n\tmeasure 'Cities Monitored' = DISTINCTCOUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5e93dcab-179e-5118-983f-e1038bdd811f\n\n\tmeasure 'Average Precipitation' = AVERAGE('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: db8c2c6e-d368-55b4-80da-40cf76d3313e\n\n\tmeasure 'Temperature Range' = MAX('Weather_Data'[Temp_Max]) - MIN('Weather_Data'[Temp_Min])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: eed10315-b026-55c0-9038-563cb15c57af\n\n\tmeasure 'Count(City)' = DISTINCTCOUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 56fc6384-fe0e-5bfe-8e1c-dd0e934329f0\n\n\tmeasure 'Avg(Temperature)' = AVERAGE('Weather_Data'[Temperature])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 54f4d1ef-b749-5f69-9ffd-c670ab3c6cf5\n\n\tmeasure 'Sum(Precipitation)' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: dc5e6360-1e12-5fa5-836b-16359bfe5945\n\n\tmeasure 'Historical Precipitation' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 3e63d918-0ef7-54fa-9e64-014df888a005\n\n\tmeasure 'Count({<Rain_Flag={1}>} DISTINCT Date)' = DISTINCTCOUNT('Weather_Data'[Date])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 119c92d6-6136-50a0-a859-ec7455f668a9\n\n\tcolumn City\n\t\tdataType: string\n\t\tlineageTag: 066b2111-3e9a-5a9f-93cb-2dfc0606251e\n\t\tsummarizeBy: none\n\t\tsourceColumn: City\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Date\n\t\tdataType: dateTime\n\t\tlineageTag: 0cb60ea5-f9d6-5c73-9734-6a9cd16948cb\n\t\tsummarizeBy: none\n\t\tsourceColumn: Date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Year\n\t\tdataType: int64\n\t\tlineageTag: 77cd5276-9f06-523b-9ed2-fb18195bb182\n\t\tsummarizeBy: none\n\t\tsourceColumn: Year\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Month\n\t\tdataType: int64\n\t\tlineageTag: 261c3a72-e787-5ccb-a4dd-941060e3b3a1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Month\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthYear\n\t\tdataType: int64\n\t\tlineageTag: d445ee7d-ac82-57da-b8fb-202434065abb\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthYear\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Record_Type\n\t\tdataType: string\n\t\tlineageTag: 7a4be3b5-ab17-5eca-a9d6-958f5da84bef\n\t\tsummarizeBy: none\n\t\tsourceColumn: Record_Type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temperature\n\t\tdataType: double\n\t\tlineageTag: 86ecbaeb-cc20-53e7-b98e-4976d641ae46\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temperature\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temp_Min\n\t\tdataType: double\n\t\tlineageTag: 1ce83239-2300-54d1-a100-bddfc92a0967\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temp_Min\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temp_Max\n\t\tdataType: double\n\t\tlineageTag: 1c5e45fa-4890-5b75-a90b-1c12f26bf179\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temp_Max\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Precipitation\n\t\tdataType: double\n\t\tlineageTag: 58098013-ffec-5d12-a48d-e22aea6feb54\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Precipitation\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Weather_Code\n\t\tdataType: double\n\t\tlineageTag: 8cd8eaee-ee1e-555b-ac14-eade1591c22a\n\t\tsummarizeBy: none\n\t\tsourceColumn: Weather_Code\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Weather_Condition = RELATED('WeatherCodes'[Weather_Code])\n\t\tdataType: string\n\t\tlineageTag: 5d5d8545-1c00-55eb-9b09-f7373a07815b\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Rain_Flag = SWITCH(TRUE(), 'Weather_Data'[Precipitation] > 0, 1, 0)\n\t\tdataType: double\n\t\tlineageTag: a1ce8987-547f-57ef-ab2c-8990a7c4096b\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Latitude\n\t\tdataType: double\n\t\tlineageTag: 7a65aa3f-7901-57f5-beb2-29c1ce37c1d4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Latitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Longitude\n\t\tdataType: double\n\t\tlineageTag: 6a4394df-979a-56fa-bd5d-d26ad478ee01\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Longitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Longitude_Latitude\n\t\tdataType: string\n\t\tlineageTag: 1ef97ebd-054e-507e-bcb7-e378c7e463b7\n\t\tsummarizeBy: none\n\t\tsourceColumn: Longitude_Latitude\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Observation_Time\n\t\tdataType: dateTime\n\t\tlineageTag: be26d057-09a2-551d-bcf8-5d568c04b160\n\t\tsummarizeBy: none\n\t\tsourceColumn: Observation_Time\n\t\tformatString: M/D/YYYY h\\:mm\\:ss TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Weather_Data = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"City\", \"Date\", \"Year\", \"Month\", \"MonthYear\", \"Record_Type\", \"Temperature\", \"Temp_Min\", \"Temp_Max\", \"Precipitation\", \"Weather_Code\", \"Latitude\", \"Longitude\", \"Longitude_Latitude\", \"Observation_Time\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table"
        },
        "report": {
            ".pbi/localSettings.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/localSettings/1.0.0/schema.json"
            },
            ".platform": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
                "metadata": {
                    "type": "Report",
                    "displayName": "Weather Analytics"
                },
                "config": {
                    "version": "2.0",
                    "logicalId": "535e2ca8-28cc-51a9-a1a8-62359cde14a1"
                }
            },
            "StaticResources/SharedResources/BaseThemes/CY24SU10.json": {
                "name": "CY24SU10",
                "dataColors": [
                    "#004B87",
                    "#00A3E0",
                    "#702082",
                    "#E87722",
                    "#50B848"
                ],
                "foreground": "#252423",
                "foregroundNeutralSecondary": "#605E5C",
                "foregroundNeutralTertiary": "#B3B0AD",
                "background": "#F8F9FA",
                "backgroundLight": "#F8F9FA",
                "backgroundNeutral": "#EDEBE9",
                "tableAccent": "#004B87",
                "good": "#009845",
                "neutral": "#FF9900",
                "bad": "#E60000",
                "maximum": "#004B87",
                "center": "#FF9900",
                "minimum": "#C7E0F4",
                "null": "#FF7F48",
                "hyperlink": "#004B87",
                "visitedHyperlink": "#004B87",
                "textClasses": {
                    "callout": {
                        "fontSize": 32,
                        "fontFace": "Segoe UI, sans-serif",
                        "color": "#004B87"
                    },
                    "title": {
                        "fontSize": 12,
                        "fontFace": "Segoe UI, sans-serif Semibold",
                        "color": "#252423"
                    },
                    "header": {
                        "fontSize": 11,
                        "fontFace": "Segoe UI, sans-serif Semibold",
                        "color": "#252423"
                    },
                    "label": {
                        "fontSize": 10,
                        "fontFace": "Segoe UI, sans-serif",
                        "color": "#605E5C"
                    }
                },
                "visualStyles": {
                    "*": {
                        "*": {
                            "*": [
                                {
                                    "wordWrap": true
                                }
                            ],
                            "title": [
                                {
                                    "show": true,
                                    "fontColor": {
                                        "solid": {
                                            "color": "#252423"
                                        }
                                    },
                                    "fontSize": 12,
                                    "fontFamily": "Segoe UI, sans-serif Semibold",
                                    "titleWrap": true
                                }
                            ],
                            "background": [
                                {
                                    "show": true,
                                    "color": {
                                        "solid": {
                                            "color": "#FFFFFF"
                                        }
                                    },
                                    "transparency": 0
                                }
                            ],
                            "border": [
                                {
                                    "show": true,
                                    "color": {
                                        "solid": {
                                            "color": "#E5E5E5"
                                        }
                                    },
                                    "radius": 4
                                }
                            ],
                            "categoryAxis": [
                                {
                                    "showAxisTitle": true,
                                    "gridlineStyle": "dotted",
                                    "concatenateLabels": false
                                }
                            ],
                            "valueAxis": [
                                {
                                    "showAxisTitle": true,
                                    "gridlineStyle": "dotted"
                                }
                            ],
                            "legend": [
                                {
                                    "show": true,
                                    "position": "Top"
                                }
                            ]
                        }
                    },
                    "card": {
                        "*": {
                            "labels": [
                                {
                                    "color": {
                                        "solid": {
                                            "color": "#004B87"
                                        }
                                    },
                                    "fontSize": 28,
                                    "fontFamily": "Segoe UI, sans-serif Bold"
                                }
                            ],
                            "categoryLabels": [
                                {
                                    "show": true,
                                    "color": {
                                        "solid": {
                                            "color": "#605E5C"
                                        }
                                    },
                                    "fontSize": 10
                                }
                            ],
                            "card": [
                                {
                                    "outlineColor": {
                                        "solid": {
                                            "color": "#E5E5E5"
                                        }
                                    },
                                    "outlineWeight": 1
                                }
                            ]
                        }
                    },
                    "slicer": {
                        "*": {
                            "header": [
                                {
                                    "show": true,
                                    "fontColor": {
                                        "solid": {
                                            "color": "#252423"
                                        }
                                    },
                                    "fontSize": 10,
                                    "fontFamily": "Segoe UI, sans-serif Semibold"
                                }
                            ],
                            "items": [
                                {
                                    "fontColor": {
                                        "solid": {
                                            "color": "#252423"
                                        }
                                    },
                                    "fontSize": 10
                                }
                            ]
                        }
                    },
                    "page": {
                        "*": {
                            "background": [
                                {
                                    "transparency": 0,
                                    "color": {
                                        "solid": {
                                            "color": "#F4F5F7"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            "definition.pbir": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/1.0.0/schema.json",
                "version": "4.0",
                "datasetReference": {
                    "byPath": {
                        "path": "../Weather Analytics.SemanticModel"
                    }
                }
            },
            "definition/pages/executive-overview/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "executive-overview",
                "displayName": "Executive Overview",
                "displayOption": "FitToWidth",
                "height": 1600,
                "width": 1280
            },
            "definition/pages/executive-overview/visuals/1f1995e7/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "1f1995e7",
                "position": {
                    "x": 533,
                    "y": 120,
                    "width": 213,
                    "height": 240,
                    "z": 3,
                    "tabOrder": 3
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/376e42aa/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "376e42aa",
                "position": {
                    "x": 0,
                    "y": 1200,
                    "width": 1280,
                    "height": 360,
                    "z": 14,
                    "tabOrder": 14
                },
                "visual": {
                    "visualType": "tableEx",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Date"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Date",
                                        "nativeQueryRef": "Date",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Temperature",
                                        "nativeQueryRef": "Temperature",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Temp_Max"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Temp_Max",
                                        "nativeQueryRef": "Temp_Max",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Temp_Min"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Temp_Min",
                                        "nativeQueryRef": "Temp_Min",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Precipitation",
                                        "nativeQueryRef": "Precipitation",
                                        "active": false
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather Data Details'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/37e498f3/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "37e498f3",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 1280,
                    "height": 120,
                    "z": 0,
                    "tabOrder": 0
                },
                "visual": {
                    "visualType": "textbox",
                    "query": {
                        "queryState": {}
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'WEATHER ANALYTICS'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "general": [
                            {
                                "properties": {
                                    "paragraphs": [
                                        {
                                            "textRuns": [
                                                {
                                                    "value": "WEATHER ANALYTICS\n\n[text-image]"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/3c9ad7ec/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "3c9ad7ec",
                "position": {
                    "x": 960,
                    "y": 360,
                    "width": 320,
                    "height": 180,
                    "z": 9,
                    "tabOrder": 9
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Cities Monitored"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Cities Monitored",
                                        "nativeQueryRef": "Cities Monitored"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Cities Monitored'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/5b052536/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "5b052536",
                "position": {
                    "x": 640,
                    "y": 900,
                    "width": 640,
                    "height": 300,
                    "z": 13,
                    "tabOrder": 13
                },
                "visual": {
                    "visualType": "lineClusteredColumnComboChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            },
                            "Y2": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature & Precipitation Trend'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/614834b0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "614834b0",
                "position": {
                    "x": 0,
                    "y": 540,
                    "width": 640,
                    "height": 360,
                    "z": 10,
                    "tabOrder": 10
                },
                "visual": {
                    "visualType": "lineChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Date"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Date",
                                        "nativeQueryRef": "Date",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature Trend'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/77a8537e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "77a8537e",
                "position": {
                    "x": 267,
                    "y": 120,
                    "width": 267,
                    "height": 240,
                    "z": 2,
                    "tabOrder": 2
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Record Type'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/8ca3b57e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8ca3b57e",
                "position": {
                    "x": 0,
                    "y": 120,
                    "width": 267,
                    "height": 240,
                    "z": 1,
                    "tabOrder": 1
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/9178eea8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9178eea8",
                "position": {
                    "x": 320,
                    "y": 360,
                    "width": 320,
                    "height": 180,
                    "z": 7,
                    "tabOrder": 7
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Maximum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Maximum Temperature",
                                        "nativeQueryRef": "Maximum Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Maximum Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/98a0d8d2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "98a0d8d2",
                "position": {
                    "x": 640,
                    "y": 540,
                    "width": 640,
                    "height": 360,
                    "z": 11,
                    "tabOrder": 11
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/9c8a2ae1/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9c8a2ae1",
                "position": {
                    "x": 640,
                    "y": 360,
                    "width": 320,
                    "height": 180,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Total Precipitation'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/a63f92e9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a63f92e9",
                "position": {
                    "x": 0,
                    "y": 900,
                    "width": 640,
                    "height": 300,
                    "z": 12,
                    "tabOrder": 12
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Count(City)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Count(City)",
                                        "nativeQueryRef": "Count(City)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather Conditions'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/e3674992/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3674992",
                "position": {
                    "x": 1013,
                    "y": 120,
                    "width": 267,
                    "height": 240,
                    "z": 5,
                    "tabOrder": 5
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather_Condition'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/e3ac69a0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3ac69a0",
                "position": {
                    "x": 747,
                    "y": 120,
                    "width": 267,
                    "height": 240,
                    "z": 4,
                    "tabOrder": 4
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Month-Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/f7610270/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "f7610270",
                "position": {
                    "x": 0,
                    "y": 360,
                    "width": 320,
                    "height": 180,
                    "z": 6,
                    "tabOrder": 6
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/executive-overview/visuals/nav00c936e5/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav00c936e5",
                "position": {
                    "x": 8,
                    "y": 8,
                    "z": 1000,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1000
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Executive Overview'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#FFFFFF'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#118DFF'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/executive-overview/visuals/nav01f658d3/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav01f658d3",
                "position": {
                    "x": 166,
                    "y": 8,
                    "z": 1001,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1001
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/executive-overview/visuals/nav0256130c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav0256130c",
                "position": {
                    "x": 324,
                    "y": 8,
                    "z": 1002,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1002
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation & Weather Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/executive-overview/visuals/nav03df6cb9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav03df6cb9",
                "position": {
                    "x": 482,
                    "y": 8,
                    "z": 1003,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1003
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Geographic Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/geographic-analysis/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "geographic-analysis",
                "displayName": "Geographic Analysis",
                "displayOption": "FitToWidth",
                "height": 1420,
                "width": 1280
            },
            "definition/pages/geographic-analysis/visuals/061c0bca/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "061c0bca",
                "position": {
                    "x": 960,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Cities Monitored"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Cities Monitored",
                                        "nativeQueryRef": "Cities Monitored"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Cities Monitored'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/1f1995e7/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "1f1995e7",
                "position": {
                    "x": 640,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 3,
                    "tabOrder": 3
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/5342c1b1/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "5342c1b1",
                "position": {
                    "x": 960,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 4,
                    "tabOrder": 4
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather_Condition'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/626ad454/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "626ad454",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 1280,
                    "height": 120,
                    "z": 0,
                    "tabOrder": 0
                },
                "visual": {
                    "visualType": "textbox",
                    "query": {
                        "queryState": {}
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Text-Image'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "general": [
                            {
                                "properties": {
                                    "paragraphs": [
                                        {
                                            "textRuns": [
                                                {
                                                    "value": "Text-Image\n\n[text-image]"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/76421b23/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "76421b23",
                "position": {
                    "x": 0,
                    "y": 480,
                    "width": 1280,
                    "height": 480,
                    "z": 9,
                    "tabOrder": 9
                },
                "visual": {
                    "visualType": "map",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Longitude_Latitude"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Longitude_Latitude",
                                        "nativeQueryRef": "Longitude_Latitude",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature by Location'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/77a8537e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "77a8537e",
                "position": {
                    "x": 320,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 2,
                    "tabOrder": 2
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Record Type'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/8ca3b57e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8ca3b57e",
                "position": {
                    "x": 0,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 1,
                    "tabOrder": 1
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/a31b9e13/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a31b9e13",
                "position": {
                    "x": 0,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 5,
                    "tabOrder": 5
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/a4795ecd/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a4795ecd",
                "position": {
                    "x": 320,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 6,
                    "tabOrder": 6
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Maximum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Maximum Temperature",
                                        "nativeQueryRef": "Maximum Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Maximum Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/b08e7afe/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "b08e7afe",
                "position": {
                    "x": 640,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 7,
                    "tabOrder": 7
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Total Precipitation'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/e48c95c6/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e48c95c6",
                "position": {
                    "x": 0,
                    "y": 960,
                    "width": 1280,
                    "height": 420,
                    "z": 10,
                    "tabOrder": 10
                },
                "visual": {
                    "visualType": "tableEx",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Latitude"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Latitude",
                                        "nativeQueryRef": "Latitude",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Longitude"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Longitude",
                                        "nativeQueryRef": "Longitude",
                                        "active": false
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Geographic Weather Details'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/geographic-analysis/visuals/nav00c936e5/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav00c936e5",
                "position": {
                    "x": 8,
                    "y": 8,
                    "z": 1000,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1000
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Executive Overview'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/geographic-analysis/visuals/nav01f658d3/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav01f658d3",
                "position": {
                    "x": 166,
                    "y": 8,
                    "z": 1001,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1001
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/geographic-analysis/visuals/nav0256130c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav0256130c",
                "position": {
                    "x": 324,
                    "y": 8,
                    "z": 1002,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1002
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation & Weather Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/geographic-analysis/visuals/nav03df6cb9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav03df6cb9",
                "position": {
                    "x": 482,
                    "y": 8,
                    "z": 1003,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1003
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Geographic Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#FFFFFF'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#118DFF'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/pages.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
                "pageOrder": [
                    "executive-overview",
                    "temperature-analysis",
                    "precipitation-weather-analysis",
                    "geographic-analysis"
                ],
                "activePageName": "executive-overview"
            },
            "definition/pages/precipitation-weather-analysis/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "precipitation-weather-analysis",
                "displayName": "Precipitation & Weather Analysis",
                "displayOption": "FitToWidth",
                "height": 2380,
                "width": 1280
            },
            "definition/pages/precipitation-weather-analysis/visuals/11ce2179/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "11ce2179",
                "position": {
                    "x": 0,
                    "y": 1440,
                    "width": 1280,
                    "height": 360,
                    "z": 15,
                    "tabOrder": 15
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Count({<Rain_Flag={1}>} DISTINCT Date)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Count({<Rain_Flag={1}>} DISTINCT Date)",
                                        "nativeQueryRef": "Count({<Rain_Flag={1}>} DISTINCT Date)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Rainy Days by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/1f1995e7/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "1f1995e7",
                "position": {
                    "x": 533,
                    "y": 120,
                    "width": 213,
                    "height": 180,
                    "z": 3,
                    "tabOrder": 3
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/241be119/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "241be119",
                "position": {
                    "x": 0,
                    "y": 480,
                    "width": 640,
                    "height": 360,
                    "z": 10,
                    "tabOrder": 10
                },
                "visual": {
                    "visualType": "lineChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Monthly Precipitation Trend'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/4be8638c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "4be8638c",
                "position": {
                    "x": 0,
                    "y": 1140,
                    "width": 640,
                    "height": 300,
                    "z": 14,
                    "tabOrder": 14
                },
                "visual": {
                    "visualType": "scatterChart",
                    "query": {
                        "queryState": {
                            "Details": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": false
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": false
                                    }
                                ]
                            },
                            "X Axis": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Historical Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Historical Precipitation",
                                        "nativeQueryRef": "Historical Precipitation"
                                    }
                                ]
                            },
                            "Y Axis": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Historical Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Historical Precipitation",
                                        "nativeQueryRef": "Historical Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Historical vs Forecast Precipitation'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/6973fdf7/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "6973fdf7",
                "position": {
                    "x": 960,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 9,
                    "tabOrder": 9
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather Records"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather Records",
                                        "nativeQueryRef": "Weather Records"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather Records'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/6ed51779/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "6ed51779",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 1280,
                    "height": 120,
                    "z": 0,
                    "tabOrder": 0
                },
                "visual": {
                    "visualType": "textbox",
                    "query": {
                        "queryState": {}
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PRECIPITATION & WEATHER'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "general": [
                            {
                                "properties": {
                                    "paragraphs": [
                                        {
                                            "textRuns": [
                                                {
                                                    "value": "PRECIPITATION & WEATHER\n\n[text-image]"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/75cce93f/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "75cce93f",
                "position": {
                    "x": 640,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Rainy Records"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Rainy Records",
                                        "nativeQueryRef": "Rainy Records"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Rainy Records'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/77a8537e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "77a8537e",
                "position": {
                    "x": 267,
                    "y": 120,
                    "width": 267,
                    "height": 180,
                    "z": 2,
                    "tabOrder": 2
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Record Type'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/8ae9c8b6/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8ae9c8b6",
                "position": {
                    "x": 0,
                    "y": 1800,
                    "width": 1280,
                    "height": 540,
                    "z": 16,
                    "tabOrder": 16
                },
                "visual": {
                    "visualType": "treemap",
                    "query": {
                        "queryState": {
                            "Group": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            },
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Count(City)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Count(City)",
                                        "nativeQueryRef": "Count(City)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather Condition Distribution'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/8ca3b57e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8ca3b57e",
                "position": {
                    "x": 0,
                    "y": 120,
                    "width": 267,
                    "height": 180,
                    "z": 1,
                    "tabOrder": 1
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/ab1f3219/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "ab1f3219",
                "position": {
                    "x": 640,
                    "y": 840,
                    "width": 640,
                    "height": 300,
                    "z": 13,
                    "tabOrder": 13
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Sum(Precipitation)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Sum(Precipitation)",
                                        "nativeQueryRef": "Sum(Precipitation)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation by Weather Condition'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/b9e3251b/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "b9e3251b",
                "position": {
                    "x": 640,
                    "y": 1140,
                    "width": 640,
                    "height": 300,
                    "z": 17,
                    "tabOrder": 17
                },
                "visual": {
                    "visualType": "gauge",
                    "query": {
                        "queryState": {
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/c721257d/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c721257d",
                "position": {
                    "x": 0,
                    "y": 840,
                    "width": 640,
                    "height": 300,
                    "z": 12,
                    "tabOrder": 12
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Count(City)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Count(City)",
                                        "nativeQueryRef": "Count(City)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather Condition Frequency'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/c8015b56/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c8015b56",
                "position": {
                    "x": 320,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 7,
                    "tabOrder": 7
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Precipitation",
                                        "nativeQueryRef": "Average Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Precipitation (mm)'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/c9cadd6e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c9cadd6e",
                "position": {
                    "x": 640,
                    "y": 480,
                    "width": 640,
                    "height": 360,
                    "z": 11,
                    "tabOrder": 11
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/e3674992/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3674992",
                "position": {
                    "x": 1013,
                    "y": 120,
                    "width": 267,
                    "height": 180,
                    "z": 5,
                    "tabOrder": 5
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Weather_Condition"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Weather_Condition",
                                        "nativeQueryRef": "Weather_Condition",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Weather_Condition'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/e3ac69a0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3ac69a0",
                "position": {
                    "x": 747,
                    "y": 120,
                    "width": 267,
                    "height": 180,
                    "z": 4,
                    "tabOrder": 4
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Month-Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/f5a87c92/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "f5a87c92",
                "position": {
                    "x": 0,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 6,
                    "tabOrder": 6
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Total Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Total Precipitation",
                                        "nativeQueryRef": "Total Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Total Precipitation (mm)'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/nav00c936e5/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav00c936e5",
                "position": {
                    "x": 8,
                    "y": 8,
                    "z": 1000,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1000
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Executive Overview'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/nav01f658d3/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav01f658d3",
                "position": {
                    "x": 166,
                    "y": 8,
                    "z": 1001,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1001
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/nav0256130c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav0256130c",
                "position": {
                    "x": 324,
                    "y": 8,
                    "z": 1002,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1002
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation & Weather Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#FFFFFF'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#118DFF'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/precipitation-weather-analysis/visuals/nav03df6cb9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav03df6cb9",
                "position": {
                    "x": 482,
                    "y": 8,
                    "z": 1003,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1003
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Geographic Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/temperature-analysis/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "temperature-analysis",
                "displayName": "Temperature Analysis",
                "displayOption": "FitToWidth",
                "height": 2200,
                "width": 1280
            },
            "definition/pages/temperature-analysis/visuals/1f1995e7/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "1f1995e7",
                "position": {
                    "x": 693,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 3,
                    "tabOrder": 3
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/77a8537e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "77a8537e",
                "position": {
                    "x": 320,
                    "y": 120,
                    "width": 373,
                    "height": 180,
                    "z": 2,
                    "tabOrder": 2
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Record Type'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/8ca3b57e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8ca3b57e",
                "position": {
                    "x": 0,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 1,
                    "tabOrder": 1
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/8d4b0af8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "8d4b0af8",
                "position": {
                    "x": 0,
                    "y": 1800,
                    "width": 1280,
                    "height": 360,
                    "z": 14,
                    "tabOrder": 14
                },
                "visual": {
                    "visualType": "columnChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Avg(Temperature)"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Avg(Temperature)",
                                        "nativeQueryRef": "Avg(Temperature)"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Distribution by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "false"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/9178eea8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9178eea8",
                "position": {
                    "x": 960,
                    "y": 480,
                    "width": 320,
                    "height": 180,
                    "z": 7,
                    "tabOrder": 7
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Maximum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Maximum Temperature",
                                        "nativeQueryRef": "Maximum Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Maximum Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/98a0d8d2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "98a0d8d2",
                "position": {
                    "x": 0,
                    "y": 1020,
                    "width": 640,
                    "height": 300,
                    "z": 11,
                    "tabOrder": 11
                },
                "visual": {
                    "visualType": "barChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/9bbc798a/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9bbc798a",
                "position": {
                    "x": 480,
                    "y": 300,
                    "width": 480,
                    "height": 360,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "gauge",
                    "query": {
                        "queryState": {
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Temperature Range"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Temperature Range",
                                        "nativeQueryRef": "Temperature Range"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Range'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/a31b9e13/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a31b9e13",
                "position": {
                    "x": 0,
                    "y": 300,
                    "width": 480,
                    "height": 360,
                    "z": 5,
                    "tabOrder": 5
                },
                "visual": {
                    "visualType": "gauge",
                    "query": {
                        "queryState": {
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/b960282e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "b960282e",
                "position": {
                    "x": 640,
                    "y": 1020,
                    "width": 640,
                    "height": 300,
                    "z": 12,
                    "tabOrder": 12
                },
                "visual": {
                    "visualType": "columnChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Temperature",
                                        "nativeQueryRef": "Temperature",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Distribution'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "false"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/bca23bd8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "bca23bd8",
                "position": {
                    "x": 640,
                    "y": 660,
                    "width": 640,
                    "height": 360,
                    "z": 10,
                    "tabOrder": 10
                },
                "visual": {
                    "visualType": "lineChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Date"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Date",
                                        "nativeQueryRef": "Date",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Minimum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Minimum Temperature",
                                        "nativeQueryRef": "Minimum Temperature"
                                    },
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Maximum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Maximum Temperature",
                                        "nativeQueryRef": "Maximum Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Minimum vs Maximum Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/cda422f1/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "cda422f1",
                "position": {
                    "x": 960,
                    "y": 300,
                    "width": 320,
                    "height": 180,
                    "z": 6,
                    "tabOrder": 6
                },
                "visual": {
                    "visualType": "card",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Minimum Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Minimum Temperature",
                                        "nativeQueryRef": "Minimum Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Minimum Temperature'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "14.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "valueLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "categoryLabel": [
                            {
                                "properties": {
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/ce4bdcc4/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "ce4bdcc4",
                "position": {
                    "x": 0,
                    "y": 1320,
                    "width": 1280,
                    "height": 480,
                    "z": 13,
                    "tabOrder": 13
                },
                "visual": {
                    "visualType": "scatterChart",
                    "query": {
                        "queryState": {
                            "Details": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "City"
                                            }
                                        },
                                        "queryRef": "Weather_Data.City",
                                        "nativeQueryRef": "City",
                                        "active": true
                                    }
                                ]
                            },
                            "X Axis": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            },
                            "Y Axis": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Precipitation"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Precipitation",
                                        "nativeQueryRef": "Average Precipitation"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature vs Precipitation by City'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/e3ac69a0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3ac69a0",
                "position": {
                    "x": 1013,
                    "y": 120,
                    "width": 267,
                    "height": 180,
                    "z": 4,
                    "tabOrder": 4
                },
                "visual": {
                    "visualType": "slicer",
                    "query": {
                        "queryState": {
                            "Values": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Year"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Year",
                                        "nativeQueryRef": "Year",
                                        "active": true
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Month-Year'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "slicerSettings": [
                            {
                                "properties": {
                                    "orientation": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'vertical'"
                                            }
                                        }
                                    },
                                    "mode": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'basic'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/e52056c2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e52056c2",
                "position": {
                    "x": 0,
                    "y": 660,
                    "width": 640,
                    "height": 360,
                    "z": 9,
                    "tabOrder": 9
                },
                "visual": {
                    "visualType": "lineChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Date"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Date",
                                        "nativeQueryRef": "Date",
                                        "active": true
                                    }
                                ]
                            },
                            "Y": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Weather_Data"
                                                    }
                                                },
                                                "Property": "Average Temperature"
                                            }
                                        },
                                        "queryRef": "Weather_Data.Average Temperature",
                                        "nativeQueryRef": "Average Temperature"
                                    }
                                ]
                            }
                        }
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Average Temperature Trend'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/ef3df80b/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "ef3df80b",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 1280,
                    "height": 120,
                    "z": 0,
                    "tabOrder": 0
                },
                "visual": {
                    "visualType": "textbox",
                    "query": {
                        "queryState": {}
                    },
                    "objects": {
                        "title": [
                            {
                                "properties": {
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'TEMPERATURE ANALYSIS'"
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Segoe UI'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "general": [
                            {
                                "properties": {
                                    "paragraphs": [
                                        {
                                            "textRuns": [
                                                {
                                                    "value": "TEMPERATURE ANALYSIS\n\n[text-image]"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "drillFilterOtherVisuals": true
                },
                "filterConfig": {
                    "filters": []
                }
            },
            "definition/pages/temperature-analysis/visuals/nav00c936e5/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav00c936e5",
                "position": {
                    "x": 8,
                    "y": 8,
                    "z": 1000,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1000
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Executive Overview'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'executive-overview'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/temperature-analysis/visuals/nav01f658d3/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav01f658d3",
                "position": {
                    "x": 166,
                    "y": 8,
                    "z": 1001,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1001
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Temperature Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#FFFFFF'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#118DFF'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'temperature-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/temperature-analysis/visuals/nav0256130c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav0256130c",
                "position": {
                    "x": 324,
                    "y": 8,
                    "z": 1002,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1002
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Precipitation & Weather Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'precipitation-weather-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/temperature-analysis/visuals/nav03df6cb9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav03df6cb9",
                "position": {
                    "x": 482,
                    "y": 8,
                    "z": 1003,
                    "width": 150,
                    "height": 40,
                    "tabOrder": 1003
                },
                "visual": {
                    "visualType": "actionButton",
                    "objects": {
                        "text": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "text": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Geographic Analysis'"
                                            }
                                        }
                                    },
                                    "fontSize": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "10D"
                                            }
                                        }
                                    },
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#252423'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#F3F2F1'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "page": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    },
                    "visualContainerObjects": {
                        "visualLink": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    },
                                    "navigationSection": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'geographic-analysis'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/report.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.2.0/schema.json",
                "themeCollection": {
                    "baseTheme": {
                        "name": "CY24SU10",
                        "reportVersionAtImport": {
                            "visual": "2.4.0",
                            "report": "3.0.0",
                            "page": "2.3.0"
                        },
                        "type": "SharedResources"
                    }
                },
                "objects": {
                    "section": [
                        {
                            "properties": {
                                "verticalAlignment": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Top'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "resourcePackages": [
                    {
                        "name": "SharedResources",
                        "type": "SharedResources",
                        "items": [
                            {
                                "name": "CY24SU10",
                                "path": "BaseThemes/CY24SU10.json",
                                "type": "BaseTheme"
                            }
                        ]
                    }
                ],
                "settings": {
                    "useStylableVisualContainerHeader": true,
                    "exportDataMode": "AllowSummarized",
                    "defaultDrillFilterOtherVisuals": true,
                    "allowChangeFilterTypes": true,
                    "useEnhancedTooltips": true,
                    "useDefaultAggregateDisplayName": true
                }
            },
            "definition/version.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
                "version": "2.0.0"
            }
        },
        "other": {
            ".gitignore": "# Power BI Desktop local state\n*.pbix\n.pbi/localSettings.json\n.pbi/cache.abf\n"
        }
    },
    "semantic_model": {
        ".pbi/diagramLayout.json": {
            "version": "1.0.0",
            "diagrams": [
                {
                    "name": "All tables",
                    "zoomValue": 100,
                    "isDefault": true,
                    "tables": [],
                    "layout": {
                        "boundingBoxWidth": 0,
                        "boundingBoxHeight": 0,
                        "boundingBoxPosition": {
                            "x": 0,
                            "y": 0
                        },
                        "nodes": []
                    }
                }
            ]
        },
        ".pbi/editorSettings.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/editorSettings/1.0.0/schema.json",
            "autodetectRelationships": true,
            "parallelQueryLoading": true,
            "typeDetectionEnabled": true,
            "relationshipImportEnabled": true,
            "shouldNotifyUserOfNameConflictResolution": true
        },
        ".pbi/localSettings.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/localSettings/1.1.0/schema.json",
            "userConsent": {
                "compositeModel": true
            }
        },
        ".platform": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
            "metadata": {
                "type": "SemanticModel",
                "displayName": "Weather Analytics"
            },
            "config": {
                "version": "2.0",
                "logicalId": "ef51f684-2bf1-51e3-8c43-f503b5752ebc"
            }
        },
        "definition.pbism": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
            "version": "4.0",
            "settings": {}
        },
        "definition/cultures/en-US.tmdl": "cultureInfo en-US\n\tlinguisticMetadata =\n\t\t\t{\n\t\t\t  \"Version\": \"1.0.0\",\n\t\t\t  \"Language\": \"en-US\"\n\t\t\t}\n\t\tcontentType: json\n",
        "definition/database.tmdl": "database\n\tcompatibilityLevel: 1567\n",
        "definition/expressions.tmdl": "expression 'Google_BigQuery_ordinal-avatar-497006-v6' =\n\t\tlet\n\t\t    Source = Web.Contents(\"https://orcqwbokkvelxgmkagpz.supabase.co/storage/v1/object/public/migration-data-files\")\n\t\tin\n\t\t    Source\n\tlineageTag: d25a2bd4-7f6c-5e4f-9706-170e0663f36d\n\n\tannotation PBI_NavigationStepName = Navigation\n\n\tannotation PBI_ResultType = Table\n",
        "definition/model.tmdl": "model Model\n\tculture: en-US\n\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\tdiscourageImplicitMeasures\n\tsourceQueryCulture: en-US\n\n\tannotation PBI_QueryOrder = [\"Weather_Data\", \"WeatherCodeMap\", \"Parameters\"]\n\tannotation PBI_ProTooling = [\"DevMode\"]\n\nref table Weather_Data\nref table WeatherCodeMap\nref table Parameters\n\nref cultureInfo en-US\n",
        "definition/tables/Parameters.tmdl": "table Parameters\n\tlineageTag: 0fe49ea5-fe5c-5a45-9ff7-e50b75dc067a\n\n\tcolumn Parameter\n\t\tdataType: string\n\t\tlineageTag: 22a0bd0b-9463-5b42-9a2d-5cfbd1cf63df\n\t\tsummarizeBy: none\n\t\tsourceColumn: Parameter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Value\n\t\tdataType: string\n\t\tlineageTag: 70b4627b-915e-51c1-9f8a-945f135294b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: Value\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Label\n\t\tdataType: string\n\t\tlineageTag: 5946bfca-d13d-5640-80d8-f86e9e9334a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: Label\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Order\n\t\tdataType: int64\n\t\tlineageTag: 3a397789-8015-5220-bf8f-5696fa2e68c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: Order\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Parameters = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table(\n\t\t\t\t        type table [Parameter = text, Value = text, Label = text, #\"Order\" = Int64.Type],\n\t\t\t\t        {\n\t\t\t            {\"DateFormat\", \"M/D/YYYY\", \"DateFormat\", 1},\n\t\t\t            {\"FirstMonthOfYear\", \"1\", \"FirstMonthOfYear\", 2},\n\t\t\t            {\"StripComments\", \"1\", \"StripComments\", 3},\n\t\t\t            {\"DecimalSep\", \".\", \"DecimalSep\", 4},\n\t\t\t            {\"MoneyThousandSep\", \",\", \"MoneyThousandSep\", 5},\n\t\t\t            {\"CreateSearchIndexOnReload\", \"1\", \"CreateSearchIndexOnReload\", 6},\n\t\t\t            {\"MonthNames\", \"Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec\", \"MonthNames\", 7},\n\t\t\t            {\"LongMonthNames\", \"January;February;March;April;May;June;July;August;September;October;November;December\", \"LongMonthNames\", 8},\n\t\t\t            {\"ThousandSep\", \",\", \"ThousandSep\", 9},\n\t\t\t            {\"currentName\", \"Weather_Data\", \"currentName\", 10},\n\t\t\t            {\"ErrorMode\", \"1\", \"ErrorMode\", 11},\n\t\t\t            {\"BrokenWeeks\", \"1\", \"BrokenWeeks\", 12},\n\t\t\t            {\"MoneyFormat\", \"$ ###0.00;-$ ###0.00\", \"MoneyFormat\", 13},\n\t\t\t            {\"TimestampFormat\", \"M/D/YYYY h\\:mm\\:ss TT\", \"TimestampFormat\", 14},\n\t\t\t            {\"ReferenceDay\", \"0\", \"ReferenceDay\", 15},\n\t\t\t            {\"name\", \"Weather_Data\", \"name\", 16},\n\t\t\t            {\"LongDayNames\", \"Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday\", \"LongDayNames\", 17},\n\t\t\t            {\"FirstWeekDay\", \"6\", \"FirstWeekDay\", 18},\n\t\t\t            {\"ScriptErrorCount\", \"0\", \"ScriptErrorCount\", 19},\n\t\t\t            {\"MoneyDecimalSep\", \".\", \"MoneyDecimalSep\", 20},\n\t\t\t            {\"TimeFormat\", \"h\\:mm\\:ss TT\", \"TimeFormat\", 21},\n\t\t\t            {\"matches\", \"0\", \"matches\", 22},\n\t\t\t            {\"index\", \"0\", \"index\", 23},\n\t\t\t            {\"OpenUrlTimeout\", \"86400\", \"OpenUrlTimeout\", 24},\n\t\t\t            {\"DayNames\", \"Mon;Tue;Wed;Thu;Fri;Sat;Sun\", \"DayNames\", 25},\n\t\t\t            {\"NumericalAbbreviation\", \"3\\:k;6\\:M;9\\:G;12\\:T;15\\:P;18\\:E;21\\:Z;24\\:Y;-3\\:m;-6:μ;-9\\:n;-12\\:p;-15\\:f;-18\\:a;-21\\:z;-24\\:y\", \"NumericalAbbreviation\", 26},\n\t\t\t            {\"CollationLocale\", \"en-US\", \"CollationLocale\", 27}\n\t\t\t\t        }\n\t\t\t\t    )\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/WeatherCodeMap.tmdl": "table WeatherCodeMap\n\tlineageTag: 0f865172-4c2c-5b8d-9160-b1544c0758d1\n\n\tcolumn '*'\n\t\tdataType: double\n\t\tlineageTag: 636bb897-ee6d-53f1-86e3-21fbe5bc492e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: *\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition WeatherCodeMap = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"*\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Weather_Data.tmdl": "table Weather_Data\n\tlineageTag: dbd151ef-a8dd-5c97-8dae-3b7cf3f2dbb1\n\n\tmeasure 'Average Temperature' = AVERAGE('Weather_Data'[Temperature])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 715ee4c7-aacb-5079-8874-3168fbac245c\n\n\tmeasure 'Rainy Records' = CALCULATE(COUNT('Weather_Data'[City]), 'Weather_Data'[Rain_Flag] = \"1\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 32b53991-6abe-5396-9ffe-7f08b36b41f6\n\n\tmeasure 'Weather Records' = COUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 3f52af7c-2cb4-5481-ac0a-e817eaab92af\n\n\tmeasure 'Minimum Temperature' = MIN('Weather_Data'[Temp_Min])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c805e5fe-d1d7-5af1-91b1-8cee7cc2d401\n\n\tmeasure 'Maximum Temperature' = MAX('Weather_Data'[Temp_Max])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c5659451-09f4-5d18-8a26-78ee442a0cd5\n\n\tmeasure 'Total Precipitation' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 8f6cef07-481d-50a6-b76d-a9e682f7c013\n\n\tmeasure 'Cities Monitored' = DISTINCTCOUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5e93dcab-179e-5118-983f-e1038bdd811f\n\n\tmeasure 'Average Precipitation' = AVERAGE('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: db8c2c6e-d368-55b4-80da-40cf76d3313e\n\n\tmeasure 'Temperature Range' = MAX('Weather_Data'[Temp_Max]) - MIN('Weather_Data'[Temp_Min])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: eed10315-b026-55c0-9038-563cb15c57af\n\n\tmeasure 'Count(City)' = DISTINCTCOUNT('Weather_Data'[City])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 56fc6384-fe0e-5bfe-8e1c-dd0e934329f0\n\n\tmeasure 'Avg(Temperature)' = AVERAGE('Weather_Data'[Temperature])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 54f4d1ef-b749-5f69-9ffd-c670ab3c6cf5\n\n\tmeasure 'Sum(Precipitation)' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: dc5e6360-1e12-5fa5-836b-16359bfe5945\n\n\tmeasure 'Historical Precipitation' = SUM('Weather_Data'[Precipitation])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 3e63d918-0ef7-54fa-9e64-014df888a005\n\n\tmeasure 'Count({<Rain_Flag={1}>} DISTINCT Date)' = DISTINCTCOUNT('Weather_Data'[Date])\n\t\tformatString: \"#,##0\"\n\t\tlineageTag: 119c92d6-6136-50a0-a859-ec7455f668a9\n\n\tcolumn City\n\t\tdataType: string\n\t\tlineageTag: 066b2111-3e9a-5a9f-93cb-2dfc0606251e\n\t\tsummarizeBy: none\n\t\tsourceColumn: City\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Date\n\t\tdataType: dateTime\n\t\tlineageTag: 0cb60ea5-f9d6-5c73-9734-6a9cd16948cb\n\t\tsummarizeBy: none\n\t\tsourceColumn: Date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Year\n\t\tdataType: int64\n\t\tlineageTag: 77cd5276-9f06-523b-9ed2-fb18195bb182\n\t\tsummarizeBy: none\n\t\tsourceColumn: Year\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Month\n\t\tdataType: int64\n\t\tlineageTag: 261c3a72-e787-5ccb-a4dd-941060e3b3a1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Month\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthYear\n\t\tdataType: int64\n\t\tlineageTag: d445ee7d-ac82-57da-b8fb-202434065abb\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthYear\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Record_Type\n\t\tdataType: string\n\t\tlineageTag: 7a4be3b5-ab17-5eca-a9d6-958f5da84bef\n\t\tsummarizeBy: none\n\t\tsourceColumn: Record_Type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temperature\n\t\tdataType: double\n\t\tlineageTag: 86ecbaeb-cc20-53e7-b98e-4976d641ae46\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temperature\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temp_Min\n\t\tdataType: double\n\t\tlineageTag: 1ce83239-2300-54d1-a100-bddfc92a0967\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temp_Min\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Temp_Max\n\t\tdataType: double\n\t\tlineageTag: 1c5e45fa-4890-5b75-a90b-1c12f26bf179\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Temp_Max\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Precipitation\n\t\tdataType: double\n\t\tlineageTag: 58098013-ffec-5d12-a48d-e22aea6feb54\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Precipitation\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Weather_Code\n\t\tdataType: double\n\t\tlineageTag: 8cd8eaee-ee1e-555b-ac14-eade1591c22a\n\t\tsummarizeBy: none\n\t\tsourceColumn: Weather_Code\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Weather_Condition = RELATED('WeatherCodes'[Weather_Code])\n\t\tdataType: string\n\t\tlineageTag: 5d5d8545-1c00-55eb-9b09-f7373a07815b\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Rain_Flag = SWITCH(TRUE(), 'Weather_Data'[Precipitation] > 0, 1, 0)\n\t\tdataType: double\n\t\tlineageTag: a1ce8987-547f-57ef-ab2c-8990a7c4096b\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Latitude\n\t\tdataType: double\n\t\tlineageTag: 7a65aa3f-7901-57f5-beb2-29c1ce37c1d4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Latitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Longitude\n\t\tdataType: double\n\t\tlineageTag: 6a4394df-979a-56fa-bd5d-d26ad478ee01\n\t\tsummarizeBy: sum\n\t\tsourceColumn: Longitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Longitude_Latitude\n\t\tdataType: string\n\t\tlineageTag: 1ef97ebd-054e-507e-bcb7-e378c7e463b7\n\t\tsummarizeBy: none\n\t\tsourceColumn: Longitude_Latitude\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Observation_Time\n\t\tdataType: dateTime\n\t\tlineageTag: be26d057-09a2-551d-bcf8-5d568c04b160\n\t\tsummarizeBy: none\n\t\tsourceColumn: Observation_Time\n\t\tformatString: M/D/YYYY h\\:mm\\:ss TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Weather_Data = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"City\", \"Date\", \"Year\", \"Month\", \"MonthYear\", \"Record_Type\", \"Temperature\", \"Temp_Min\", \"Temp_Max\", \"Precipitation\", \"Weather_Code\", \"Latitude\", \"Longitude\", \"Longitude_Latitude\", \"Observation_Time\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table"
    },
    "report": {
        ".pbi/localSettings.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/localSettings/1.0.0/schema.json"
        },
        ".platform": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
            "metadata": {
                "type": "Report",
                "displayName": "Weather Analytics"
            },
            "config": {
                "version": "2.0",
                "logicalId": "535e2ca8-28cc-51a9-a1a8-62359cde14a1"
            }
        },
        "StaticResources/SharedResources/BaseThemes/CY24SU10.json": {
            "name": "CY24SU10",
            "dataColors": [
                "#004B87",
                "#00A3E0",
                "#702082",
                "#E87722",
                "#50B848"
            ],
            "foreground": "#252423",
            "foregroundNeutralSecondary": "#605E5C",
            "foregroundNeutralTertiary": "#B3B0AD",
            "background": "#F8F9FA",
            "backgroundLight": "#F8F9FA",
            "backgroundNeutral": "#EDEBE9",
            "tableAccent": "#004B87",
            "good": "#009845",
            "neutral": "#FF9900",
            "bad": "#E60000",
            "maximum": "#004B87",
            "center": "#FF9900",
            "minimum": "#C7E0F4",
            "null": "#FF7F48",
            "hyperlink": "#004B87",
            "visitedHyperlink": "#004B87",
            "textClasses": {
                "callout": {
                    "fontSize": 32,
                    "fontFace": "Segoe UI, sans-serif",
                    "color": "#004B87"
                },
                "title": {
                    "fontSize": 12,
                    "fontFace": "Segoe UI, sans-serif Semibold",
                    "color": "#252423"
                },
                "header": {
                    "fontSize": 11,
                    "fontFace": "Segoe UI, sans-serif Semibold",
                    "color": "#252423"
                },
                "label": {
                    "fontSize": 10,
                    "fontFace": "Segoe UI, sans-serif",
                    "color": "#605E5C"
                }
            },
            "visualStyles": {
                "*": {
                    "*": {
                        "*": [
                            {
                                "wordWrap": true
                            }
                        ],
                        "title": [
                            {
                                "show": true,
                                "fontColor": {
                                    "solid": {
                                        "color": "#252423"
                                    }
                                },
                                "fontSize": 12,
                                "fontFamily": "Segoe UI, sans-serif Semibold",
                                "titleWrap": true
                            }
                        ],
                        "background": [
                            {
                                "show": true,
                                "color": {
                                    "solid": {
                                        "color": "#FFFFFF"
                                    }
                                },
                                "transparency": 0
                            }
                        ],
                        "border": [
                            {
                                "show": true,
                                "color": {
                                    "solid": {
                                        "color": "#E5E5E5"
                                    }
                                },
                                "radius": 4
                            }
                        ],
                        "categoryAxis": [
                            {
                                "showAxisTitle": true,
                                "gridlineStyle": "dotted",
                                "concatenateLabels": false
                            }
                        ],
                        "valueAxis": [
                            {
                                "showAxisTitle": true,
                                "gridlineStyle": "dotted"
                            }
                        ],
                        "legend": [
                            {
                                "show": true,
                                "position": "Top"
                            }
                        ]
                    }
                },
                "card": {
                    "*": {
                        "labels": [
                            {
                                "color": {
                                    "solid": {
                                        "color": "#004B87"
                                    }
                                },
                                "fontSize": 28,
                                "fontFamily": "Segoe UI, sans-serif Bold"
                            }
                        ],
                        "categoryLabels": [
                            {
                                "show": true,
                                "color": {
                                    "solid": {
                                        "color": "#605E5C"
                                    }
                                },
                                "fontSize": 10
                            }
                        ],
                        "card": [
                            {
                                "outlineColor": {
                                    "solid": {
                                        "color": "#E5E5E5"
                                    }
                                },
                                "outlineWeight": 1
                            }
                        ]
                    }
                },
                "slicer": {
                    "*": {
                        "header": [
                            {
                                "show": true,
                                "fontColor": {
                                    "solid": {
                                        "color": "#252423"
                                    }
                                },
                                "fontSize": 10,
                                "fontFamily": "Segoe UI, sans-serif Semibold"
                            }
                        ],
                        "items": [
                            {
                                "fontColor": {
                                    "solid": {
                                        "color": "#252423"
                                    }
                                },
                                "fontSize": 10
                            }
                        ]
                    }
                },
                "page": {
                    "*": {
                        "background": [
                            {
                                "transparency": 0,
                                "color": {
                                    "solid": {
                                        "color": "#F4F5F7"
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        },
        "definition.pbir": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/1.0.0/schema.json",
            "version": "4.0",
            "datasetReference": {
                "byPath": {
                    "path": "../Weather Analytics.SemanticModel"
                }
            }
        },
        "definition/pages/executive-overview/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "executive-overview",
            "displayName": "Executive Overview",
            "displayOption": "FitToWidth",
            "height": 1600,
            "width": 1280
        },
        "definition/pages/executive-overview/visuals/1f1995e7/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "1f1995e7",
            "position": {
                "x": 533,
                "y": 120,
                "width": 213,
                "height": 240,
                "z": 3,
                "tabOrder": 3
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/376e42aa/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "376e42aa",
            "position": {
                "x": 0,
                "y": 1200,
                "width": 1280,
                "height": 360,
                "z": 14,
                "tabOrder": 14
            },
            "visual": {
                "visualType": "tableEx",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Date"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Date",
                                    "nativeQueryRef": "Date",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Temperature",
                                    "nativeQueryRef": "Temperature",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Temp_Max"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Temp_Max",
                                    "nativeQueryRef": "Temp_Max",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Temp_Min"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Temp_Min",
                                    "nativeQueryRef": "Temp_Min",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Precipitation",
                                    "nativeQueryRef": "Precipitation",
                                    "active": false
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather Data Details'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/37e498f3/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "37e498f3",
            "position": {
                "x": 0,
                "y": 0,
                "width": 1280,
                "height": 120,
                "z": 0,
                "tabOrder": 0
            },
            "visual": {
                "visualType": "textbox",
                "query": {
                    "queryState": {}
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'WEATHER ANALYTICS'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "general": [
                        {
                            "properties": {
                                "paragraphs": [
                                    {
                                        "textRuns": [
                                            {
                                                "value": "WEATHER ANALYTICS\n\n[text-image]"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/3c9ad7ec/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "3c9ad7ec",
            "position": {
                "x": 960,
                "y": 360,
                "width": 320,
                "height": 180,
                "z": 9,
                "tabOrder": 9
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Cities Monitored"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Cities Monitored",
                                    "nativeQueryRef": "Cities Monitored"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Cities Monitored'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/5b052536/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "5b052536",
            "position": {
                "x": 640,
                "y": 900,
                "width": 640,
                "height": 300,
                "z": 13,
                "tabOrder": 13
            },
            "visual": {
                "visualType": "lineClusteredColumnComboChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        },
                        "Y2": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature & Precipitation Trend'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/614834b0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "614834b0",
            "position": {
                "x": 0,
                "y": 540,
                "width": 640,
                "height": 360,
                "z": 10,
                "tabOrder": 10
            },
            "visual": {
                "visualType": "lineChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Date"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Date",
                                    "nativeQueryRef": "Date",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature Trend'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/77a8537e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "77a8537e",
            "position": {
                "x": 267,
                "y": 120,
                "width": 267,
                "height": 240,
                "z": 2,
                "tabOrder": 2
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Record Type'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/8ca3b57e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8ca3b57e",
            "position": {
                "x": 0,
                "y": 120,
                "width": 267,
                "height": 240,
                "z": 1,
                "tabOrder": 1
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/9178eea8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9178eea8",
            "position": {
                "x": 320,
                "y": 360,
                "width": 320,
                "height": 180,
                "z": 7,
                "tabOrder": 7
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Maximum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Maximum Temperature",
                                    "nativeQueryRef": "Maximum Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Maximum Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/98a0d8d2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "98a0d8d2",
            "position": {
                "x": 640,
                "y": 540,
                "width": 640,
                "height": 360,
                "z": 11,
                "tabOrder": 11
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/9c8a2ae1/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9c8a2ae1",
            "position": {
                "x": 640,
                "y": 360,
                "width": 320,
                "height": 180,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Total Precipitation'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/a63f92e9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a63f92e9",
            "position": {
                "x": 0,
                "y": 900,
                "width": 640,
                "height": 300,
                "z": 12,
                "tabOrder": 12
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Count(City)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Count(City)",
                                    "nativeQueryRef": "Count(City)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather Conditions'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/e3674992/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3674992",
            "position": {
                "x": 1013,
                "y": 120,
                "width": 267,
                "height": 240,
                "z": 5,
                "tabOrder": 5
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather_Condition'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/e3ac69a0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3ac69a0",
            "position": {
                "x": 747,
                "y": 120,
                "width": 267,
                "height": 240,
                "z": 4,
                "tabOrder": 4
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Month-Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/f7610270/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "f7610270",
            "position": {
                "x": 0,
                "y": 360,
                "width": 320,
                "height": 180,
                "z": 6,
                "tabOrder": 6
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/executive-overview/visuals/nav00c936e5/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav00c936e5",
            "position": {
                "x": 8,
                "y": 8,
                "z": 1000,
                "width": 150,
                "height": 40,
                "tabOrder": 1000
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Executive Overview'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#FFFFFF'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#118DFF'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/executive-overview/visuals/nav01f658d3/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav01f658d3",
            "position": {
                "x": 166,
                "y": 8,
                "z": 1001,
                "width": 150,
                "height": 40,
                "tabOrder": 1001
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/executive-overview/visuals/nav0256130c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav0256130c",
            "position": {
                "x": 324,
                "y": 8,
                "z": 1002,
                "width": 150,
                "height": 40,
                "tabOrder": 1002
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation & Weather Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/executive-overview/visuals/nav03df6cb9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav03df6cb9",
            "position": {
                "x": 482,
                "y": 8,
                "z": 1003,
                "width": 150,
                "height": 40,
                "tabOrder": 1003
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Geographic Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/geographic-analysis/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "geographic-analysis",
            "displayName": "Geographic Analysis",
            "displayOption": "FitToWidth",
            "height": 1420,
            "width": 1280
        },
        "definition/pages/geographic-analysis/visuals/061c0bca/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "061c0bca",
            "position": {
                "x": 960,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Cities Monitored"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Cities Monitored",
                                    "nativeQueryRef": "Cities Monitored"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Cities Monitored'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/1f1995e7/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "1f1995e7",
            "position": {
                "x": 640,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 3,
                "tabOrder": 3
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/5342c1b1/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "5342c1b1",
            "position": {
                "x": 960,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 4,
                "tabOrder": 4
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather_Condition'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/626ad454/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "626ad454",
            "position": {
                "x": 0,
                "y": 0,
                "width": 1280,
                "height": 120,
                "z": 0,
                "tabOrder": 0
            },
            "visual": {
                "visualType": "textbox",
                "query": {
                    "queryState": {}
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Text-Image'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "general": [
                        {
                            "properties": {
                                "paragraphs": [
                                    {
                                        "textRuns": [
                                            {
                                                "value": "Text-Image\n\n[text-image]"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/76421b23/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "76421b23",
            "position": {
                "x": 0,
                "y": 480,
                "width": 1280,
                "height": 480,
                "z": 9,
                "tabOrder": 9
            },
            "visual": {
                "visualType": "map",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Longitude_Latitude"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Longitude_Latitude",
                                    "nativeQueryRef": "Longitude_Latitude",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature by Location'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/77a8537e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "77a8537e",
            "position": {
                "x": 320,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 2,
                "tabOrder": 2
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Record Type'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/8ca3b57e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8ca3b57e",
            "position": {
                "x": 0,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 1,
                "tabOrder": 1
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/a31b9e13/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a31b9e13",
            "position": {
                "x": 0,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 5,
                "tabOrder": 5
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/a4795ecd/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a4795ecd",
            "position": {
                "x": 320,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 6,
                "tabOrder": 6
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Maximum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Maximum Temperature",
                                    "nativeQueryRef": "Maximum Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Maximum Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/b08e7afe/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "b08e7afe",
            "position": {
                "x": 640,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 7,
                "tabOrder": 7
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Total Precipitation'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/e48c95c6/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e48c95c6",
            "position": {
                "x": 0,
                "y": 960,
                "width": 1280,
                "height": 420,
                "z": 10,
                "tabOrder": 10
            },
            "visual": {
                "visualType": "tableEx",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Latitude"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Latitude",
                                    "nativeQueryRef": "Latitude",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Longitude"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Longitude",
                                    "nativeQueryRef": "Longitude",
                                    "active": false
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Geographic Weather Details'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/geographic-analysis/visuals/nav00c936e5/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav00c936e5",
            "position": {
                "x": 8,
                "y": 8,
                "z": 1000,
                "width": 150,
                "height": 40,
                "tabOrder": 1000
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Executive Overview'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/geographic-analysis/visuals/nav01f658d3/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav01f658d3",
            "position": {
                "x": 166,
                "y": 8,
                "z": 1001,
                "width": 150,
                "height": 40,
                "tabOrder": 1001
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/geographic-analysis/visuals/nav0256130c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav0256130c",
            "position": {
                "x": 324,
                "y": 8,
                "z": 1002,
                "width": 150,
                "height": 40,
                "tabOrder": 1002
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation & Weather Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/geographic-analysis/visuals/nav03df6cb9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav03df6cb9",
            "position": {
                "x": 482,
                "y": 8,
                "z": 1003,
                "width": 150,
                "height": 40,
                "tabOrder": 1003
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Geographic Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#FFFFFF'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#118DFF'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/pages.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
            "pageOrder": [
                "executive-overview",
                "temperature-analysis",
                "precipitation-weather-analysis",
                "geographic-analysis"
            ],
            "activePageName": "executive-overview"
        },
        "definition/pages/precipitation-weather-analysis/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "precipitation-weather-analysis",
            "displayName": "Precipitation & Weather Analysis",
            "displayOption": "FitToWidth",
            "height": 2380,
            "width": 1280
        },
        "definition/pages/precipitation-weather-analysis/visuals/11ce2179/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "11ce2179",
            "position": {
                "x": 0,
                "y": 1440,
                "width": 1280,
                "height": 360,
                "z": 15,
                "tabOrder": 15
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Count({<Rain_Flag={1}>} DISTINCT Date)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Count({<Rain_Flag={1}>} DISTINCT Date)",
                                    "nativeQueryRef": "Count({<Rain_Flag={1}>} DISTINCT Date)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Rainy Days by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/1f1995e7/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "1f1995e7",
            "position": {
                "x": 533,
                "y": 120,
                "width": 213,
                "height": 180,
                "z": 3,
                "tabOrder": 3
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/241be119/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "241be119",
            "position": {
                "x": 0,
                "y": 480,
                "width": 640,
                "height": 360,
                "z": 10,
                "tabOrder": 10
            },
            "visual": {
                "visualType": "lineChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Monthly Precipitation Trend'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/4be8638c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "4be8638c",
            "position": {
                "x": 0,
                "y": 1140,
                "width": 640,
                "height": 300,
                "z": 14,
                "tabOrder": 14
            },
            "visual": {
                "visualType": "scatterChart",
                "query": {
                    "queryState": {
                        "Details": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": false
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": false
                                }
                            ]
                        },
                        "X Axis": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Historical Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Historical Precipitation",
                                    "nativeQueryRef": "Historical Precipitation"
                                }
                            ]
                        },
                        "Y Axis": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Historical Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Historical Precipitation",
                                    "nativeQueryRef": "Historical Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Historical vs Forecast Precipitation'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/6973fdf7/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "6973fdf7",
            "position": {
                "x": 960,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 9,
                "tabOrder": 9
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather Records"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather Records",
                                    "nativeQueryRef": "Weather Records"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather Records'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/6ed51779/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "6ed51779",
            "position": {
                "x": 0,
                "y": 0,
                "width": 1280,
                "height": 120,
                "z": 0,
                "tabOrder": 0
            },
            "visual": {
                "visualType": "textbox",
                "query": {
                    "queryState": {}
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PRECIPITATION & WEATHER'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "general": [
                        {
                            "properties": {
                                "paragraphs": [
                                    {
                                        "textRuns": [
                                            {
                                                "value": "PRECIPITATION & WEATHER\n\n[text-image]"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/75cce93f/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "75cce93f",
            "position": {
                "x": 640,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Rainy Records"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Rainy Records",
                                    "nativeQueryRef": "Rainy Records"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Rainy Records'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/77a8537e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "77a8537e",
            "position": {
                "x": 267,
                "y": 120,
                "width": 267,
                "height": 180,
                "z": 2,
                "tabOrder": 2
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Record Type'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/8ae9c8b6/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8ae9c8b6",
            "position": {
                "x": 0,
                "y": 1800,
                "width": 1280,
                "height": 540,
                "z": 16,
                "tabOrder": 16
            },
            "visual": {
                "visualType": "treemap",
                "query": {
                    "queryState": {
                        "Group": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        },
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Count(City)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Count(City)",
                                    "nativeQueryRef": "Count(City)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather Condition Distribution'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/8ca3b57e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8ca3b57e",
            "position": {
                "x": 0,
                "y": 120,
                "width": 267,
                "height": 180,
                "z": 1,
                "tabOrder": 1
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/ab1f3219/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "ab1f3219",
            "position": {
                "x": 640,
                "y": 840,
                "width": 640,
                "height": 300,
                "z": 13,
                "tabOrder": 13
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Sum(Precipitation)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Sum(Precipitation)",
                                    "nativeQueryRef": "Sum(Precipitation)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation by Weather Condition'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/b9e3251b/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "b9e3251b",
            "position": {
                "x": 640,
                "y": 1140,
                "width": 640,
                "height": 300,
                "z": 17,
                "tabOrder": 17
            },
            "visual": {
                "visualType": "gauge",
                "query": {
                    "queryState": {
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/c721257d/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c721257d",
            "position": {
                "x": 0,
                "y": 840,
                "width": 640,
                "height": 300,
                "z": 12,
                "tabOrder": 12
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Count(City)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Count(City)",
                                    "nativeQueryRef": "Count(City)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather Condition Frequency'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/c8015b56/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c8015b56",
            "position": {
                "x": 320,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 7,
                "tabOrder": 7
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Precipitation",
                                    "nativeQueryRef": "Average Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Precipitation (mm)'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/c9cadd6e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c9cadd6e",
            "position": {
                "x": 640,
                "y": 480,
                "width": 640,
                "height": 360,
                "z": 11,
                "tabOrder": 11
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/e3674992/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3674992",
            "position": {
                "x": 1013,
                "y": 120,
                "width": 267,
                "height": 180,
                "z": 5,
                "tabOrder": 5
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Weather_Condition"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Weather_Condition",
                                    "nativeQueryRef": "Weather_Condition",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Weather_Condition'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/e3ac69a0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3ac69a0",
            "position": {
                "x": 747,
                "y": 120,
                "width": 267,
                "height": 180,
                "z": 4,
                "tabOrder": 4
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Month-Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/f5a87c92/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "f5a87c92",
            "position": {
                "x": 0,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 6,
                "tabOrder": 6
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Total Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Total Precipitation",
                                    "nativeQueryRef": "Total Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Total Precipitation (mm)'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/nav00c936e5/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav00c936e5",
            "position": {
                "x": 8,
                "y": 8,
                "z": 1000,
                "width": 150,
                "height": 40,
                "tabOrder": 1000
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Executive Overview'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/nav01f658d3/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav01f658d3",
            "position": {
                "x": 166,
                "y": 8,
                "z": 1001,
                "width": 150,
                "height": 40,
                "tabOrder": 1001
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/nav0256130c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav0256130c",
            "position": {
                "x": 324,
                "y": 8,
                "z": 1002,
                "width": 150,
                "height": 40,
                "tabOrder": 1002
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation & Weather Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#FFFFFF'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#118DFF'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/precipitation-weather-analysis/visuals/nav03df6cb9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav03df6cb9",
            "position": {
                "x": 482,
                "y": 8,
                "z": 1003,
                "width": 150,
                "height": 40,
                "tabOrder": 1003
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Geographic Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/temperature-analysis/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "temperature-analysis",
            "displayName": "Temperature Analysis",
            "displayOption": "FitToWidth",
            "height": 2200,
            "width": 1280
        },
        "definition/pages/temperature-analysis/visuals/1f1995e7/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "1f1995e7",
            "position": {
                "x": 693,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 3,
                "tabOrder": 3
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/77a8537e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "77a8537e",
            "position": {
                "x": 320,
                "y": 120,
                "width": 373,
                "height": 180,
                "z": 2,
                "tabOrder": 2
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Record Type'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/8ca3b57e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8ca3b57e",
            "position": {
                "x": 0,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 1,
                "tabOrder": 1
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/8d4b0af8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "8d4b0af8",
            "position": {
                "x": 0,
                "y": 1800,
                "width": 1280,
                "height": 360,
                "z": 14,
                "tabOrder": 14
            },
            "visual": {
                "visualType": "columnChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Avg(Temperature)"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Avg(Temperature)",
                                    "nativeQueryRef": "Avg(Temperature)"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Distribution by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "false"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/9178eea8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9178eea8",
            "position": {
                "x": 960,
                "y": 480,
                "width": 320,
                "height": 180,
                "z": 7,
                "tabOrder": 7
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Maximum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Maximum Temperature",
                                    "nativeQueryRef": "Maximum Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Maximum Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/98a0d8d2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "98a0d8d2",
            "position": {
                "x": 0,
                "y": 1020,
                "width": 640,
                "height": 300,
                "z": 11,
                "tabOrder": 11
            },
            "visual": {
                "visualType": "barChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/9bbc798a/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9bbc798a",
            "position": {
                "x": 480,
                "y": 300,
                "width": 480,
                "height": 360,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "gauge",
                "query": {
                    "queryState": {
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Temperature Range"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Temperature Range",
                                    "nativeQueryRef": "Temperature Range"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Range'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/a31b9e13/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a31b9e13",
            "position": {
                "x": 0,
                "y": 300,
                "width": 480,
                "height": 360,
                "z": 5,
                "tabOrder": 5
            },
            "visual": {
                "visualType": "gauge",
                "query": {
                    "queryState": {
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/b960282e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "b960282e",
            "position": {
                "x": 640,
                "y": 1020,
                "width": 640,
                "height": 300,
                "z": 12,
                "tabOrder": 12
            },
            "visual": {
                "visualType": "columnChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Temperature",
                                    "nativeQueryRef": "Temperature",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Distribution'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "false"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/bca23bd8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "bca23bd8",
            "position": {
                "x": 640,
                "y": 660,
                "width": 640,
                "height": 360,
                "z": 10,
                "tabOrder": 10
            },
            "visual": {
                "visualType": "lineChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Date"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Date",
                                    "nativeQueryRef": "Date",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Minimum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Minimum Temperature",
                                    "nativeQueryRef": "Minimum Temperature"
                                },
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Maximum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Maximum Temperature",
                                    "nativeQueryRef": "Maximum Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Minimum vs Maximum Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/cda422f1/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "cda422f1",
            "position": {
                "x": 960,
                "y": 300,
                "width": 320,
                "height": 180,
                "z": 6,
                "tabOrder": 6
            },
            "visual": {
                "visualType": "card",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Minimum Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Minimum Temperature",
                                    "nativeQueryRef": "Minimum Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Minimum Temperature'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "14.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "valueLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "categoryLabel": [
                        {
                            "properties": {
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/ce4bdcc4/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "ce4bdcc4",
            "position": {
                "x": 0,
                "y": 1320,
                "width": 1280,
                "height": 480,
                "z": 13,
                "tabOrder": 13
            },
            "visual": {
                "visualType": "scatterChart",
                "query": {
                    "queryState": {
                        "Details": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "City"
                                        }
                                    },
                                    "queryRef": "Weather_Data.City",
                                    "nativeQueryRef": "City",
                                    "active": true
                                }
                            ]
                        },
                        "X Axis": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        },
                        "Y Axis": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Precipitation"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Precipitation",
                                    "nativeQueryRef": "Average Precipitation"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature vs Precipitation by City'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/e3ac69a0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3ac69a0",
            "position": {
                "x": 1013,
                "y": 120,
                "width": 267,
                "height": 180,
                "z": 4,
                "tabOrder": 4
            },
            "visual": {
                "visualType": "slicer",
                "query": {
                    "queryState": {
                        "Values": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Year"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Year",
                                    "nativeQueryRef": "Year",
                                    "active": true
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Month-Year'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "slicerSettings": [
                        {
                            "properties": {
                                "orientation": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'vertical'"
                                        }
                                    }
                                },
                                "mode": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'basic'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/e52056c2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e52056c2",
            "position": {
                "x": 0,
                "y": 660,
                "width": 640,
                "height": 360,
                "z": 9,
                "tabOrder": 9
            },
            "visual": {
                "visualType": "lineChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Date"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Date",
                                    "nativeQueryRef": "Date",
                                    "active": true
                                }
                            ]
                        },
                        "Y": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Weather_Data"
                                                }
                                            },
                                            "Property": "Average Temperature"
                                        }
                                    },
                                    "queryRef": "Weather_Data.Average Temperature",
                                    "nativeQueryRef": "Average Temperature"
                                }
                            ]
                        }
                    }
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Average Temperature Trend'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "legend": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/ef3df80b/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "ef3df80b",
            "position": {
                "x": 0,
                "y": 0,
                "width": 1280,
                "height": 120,
                "z": 0,
                "tabOrder": 0
            },
            "visual": {
                "visualType": "textbox",
                "query": {
                    "queryState": {}
                },
                "objects": {
                    "title": [
                        {
                            "properties": {
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'TEMPERATURE ANALYSIS'"
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Segoe UI'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "general": [
                        {
                            "properties": {
                                "paragraphs": [
                                    {
                                        "textRuns": [
                                            {
                                                "value": "TEMPERATURE ANALYSIS\n\n[text-image]"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                },
                "drillFilterOtherVisuals": true
            },
            "filterConfig": {
                "filters": []
            }
        },
        "definition/pages/temperature-analysis/visuals/nav00c936e5/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav00c936e5",
            "position": {
                "x": 8,
                "y": 8,
                "z": 1000,
                "width": 150,
                "height": 40,
                "tabOrder": 1000
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Executive Overview'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'executive-overview'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/temperature-analysis/visuals/nav01f658d3/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav01f658d3",
            "position": {
                "x": 166,
                "y": 8,
                "z": 1001,
                "width": 150,
                "height": 40,
                "tabOrder": 1001
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Temperature Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#FFFFFF'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#118DFF'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'temperature-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/temperature-analysis/visuals/nav0256130c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav0256130c",
            "position": {
                "x": 324,
                "y": 8,
                "z": 1002,
                "width": 150,
                "height": 40,
                "tabOrder": 1002
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Precipitation & Weather Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'precipitation-weather-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/temperature-analysis/visuals/nav03df6cb9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav03df6cb9",
            "position": {
                "x": 482,
                "y": 8,
                "z": 1003,
                "width": 150,
                "height": 40,
                "tabOrder": 1003
            },
            "visual": {
                "visualType": "actionButton",
                "objects": {
                    "text": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "text": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Geographic Analysis'"
                                        }
                                    }
                                },
                                "fontSize": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "10D"
                                        }
                                    }
                                },
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#252423'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#F3F2F1'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "page": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "visualContainerObjects": {
                    "visualLink": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                },
                                "navigationSection": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'geographic-analysis'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/report.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.2.0/schema.json",
            "themeCollection": {
                "baseTheme": {
                    "name": "CY24SU10",
                    "reportVersionAtImport": {
                        "visual": "2.4.0",
                        "report": "3.0.0",
                        "page": "2.3.0"
                    },
                    "type": "SharedResources"
                }
            },
            "objects": {
                "section": [
                    {
                        "properties": {
                            "verticalAlignment": {
                                "expr": {
                                    "Literal": {
                                        "Value": "'Top'"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "resourcePackages": [
                {
                    "name": "SharedResources",
                    "type": "SharedResources",
                    "items": [
                        {
                            "name": "CY24SU10",
                            "path": "BaseThemes/CY24SU10.json",
                            "type": "BaseTheme"
                        }
                    ]
                }
            ],
            "settings": {
                "useStylableVisualContainerHeader": true,
                "exportDataMode": "AllowSummarized",
                "defaultDrillFilterOtherVisuals": true,
                "allowChangeFilterTypes": true,
                "useEnhancedTooltips": true,
                "useDefaultAggregateDisplayName": true
            }
        },
        "definition/version.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
            "version": "2.0.0"
        }
    },
    "artifact_index": null
}