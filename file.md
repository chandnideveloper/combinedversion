{
    "status": "success",
    "source_type": "qlik",
    "run_id": "8990-clean",
    "run_no": "8990-clean",
    "app_id": "b18efaa0-697b-4616-937a-430dacbaed69",
    "app_name": "Spark Electronics - Sales Dashboard",
    "workspace_id": "6a8d0f4ef5f61a1cd74d155f",
    "space_id": "6a8d0f4ef5f61a1cd74d155f",
    "summary": {
        "tables": 3,
        "dimensions": 3,
        "measures": 1,
        "relationships": 2,
        "sheets": 1,
        "visualizations": 14,
        "empty_keys": 0,
        "populated_keys": 2591,
        "view": "compact"
    },
    "parsing_result": {
        "app_id": "b18efaa0-697b-4616-937a-430dacbaed69",
        "metadata": {
            "qlik_version": "12.2897.0",
            "report_version": "12.2886.0",
            "owner_name": "Ankush Kumar",
            "status": "private",
            "last_modified": "2026-08-25T03:43:11.739Z"
        },
        "connection_details": {
            "driver": "redshift",
            "source_connector": "redshift",
            "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
            "port": "5439",
            "database": "dev",
            "warehouse": "COMPUTE_WH",
            "role": "ACCOUNTADMIN"
        },
        "sheets": [
            {
                "sheet_id": "dRKtK",
                "title": "Sales Dashboard",
                "visualization_count": 14,
                "visualization_ids": [
                    "gsdTj",
                    "wLKGHd",
                    "pskCcp",
                    "HnPr",
                    "zmePAE",
                    "Zktknb",
                    "PkCUyU",
                    "tCCX",
                    "kJjznzb",
                    "yUjsQd",
                    "HJXQPk",
                    "MTaN",
                    "ucFxL",
                    "aQjWrZy"
                ]
            }
        ],
        "sheet_count": 1,
        "visualizations": [
            {
                "qlik_name": "gsdTj",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 0,
                "row": 0,
                "colspan": 5,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Date_year"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Date_year",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "Date_year",
                        "field_defs": [
                            "Date_year"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "2024",
                            "2025"
                        ],
                        "sample_values": [
                            "2024",
                            "2025"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "Date_year",
                        "field_defs": [
                            "Date_year"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "2024",
                            "2025"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "wLKGHd",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 10,
                "row": 0,
                "colspan": 6,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Date_monthLabel"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Date_monthLabel",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "Date_monthLabel",
                        "field_defs": [
                            "Date_monthLabel"
                        ],
                        "field_labels": [
                            "Date_monthLabel"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Jan",
                            "Feb",
                            "Mar",
                            "Apr",
                            "May",
                            "Jun",
                            "Jul",
                            "Aug",
                            "Sep",
                            "Oct"
                        ],
                        "sample_values": [
                            "Jan",
                            "Feb",
                            "Mar",
                            "Apr",
                            "May",
                            "Jun",
                            "Jul",
                            "Aug",
                            "Sep",
                            "Oct"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "Date_monthLabel",
                        "field_defs": [
                            "Date_monthLabel"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Jan",
                            "Feb",
                            "Mar",
                            "Apr",
                            "May",
                            "Jun",
                            "Jul",
                            "Aug",
                            "Sep",
                            "Oct"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "pskCcp",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 5,
                "row": 0,
                "colspan": 5,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Date_quarterLabel"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Date_quarterLabel",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "Date_quarterLabel",
                        "field_defs": [
                            "Date_quarterLabel"
                        ],
                        "field_labels": [
                            "Date_quarterLabel"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Q1",
                            "Q2",
                            "Q3",
                            "Q4"
                        ],
                        "sample_values": [
                            "Q1",
                            "Q2",
                            "Q3",
                            "Q4"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "Date_quarterLabel",
                        "field_defs": [
                            "Date_quarterLabel"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Q1",
                            "Q2",
                            "Q3",
                            "Q4"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "HnPr",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 0,
                "row": 6,
                "colspan": 16,
                "rowspan": 12,
                "source": "Sales Dashboard",
                "x_axis": [
                    "MonthYear"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "MonthYear",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "MonthYear",
                        "field_defs": [
                            "MonthYear"
                        ],
                        "field_labels": [
                            "MonthYear"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": false,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "EXPRESSION",
                                    "direction": "DESCENDING",
                                    "expression": "=Num(Date#(Trim(MonthYear), 'YYYY-MM'))"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1,
                                "qSortByExpression": -1,
                                "qExpression": {
                                    "qv": "=Num(Date#(Trim(MonthYear), 'YYYY-MM'))"
                                }
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "2024-01",
                            "2024-02",
                            "2024-03",
                            "2024-04",
                            "2024-05",
                            "2024-06",
                            "2024-07",
                            "2024-08",
                            "2024-09",
                            "2024-10"
                        ],
                        "sample_values": [
                            "2024-01",
                            "2024-02",
                            "2024-03",
                            "2024-04",
                            "2024-05",
                            "2024-06",
                            "2024-07",
                            "2024-08",
                            "2024-09",
                            "2024-10"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "MonthYear",
                        "field_defs": [
                            "MonthYear"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": false,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "EXPRESSION",
                                    "direction": "DESCENDING",
                                    "expression": "=Num(Date#(Trim(MonthYear), 'YYYY-MM'))"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1,
                                "qSortByExpression": -1,
                                "qExpression": {
                                    "qv": "=Num(Date#(Trim(MonthYear), 'YYYY-MM'))"
                                }
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "2024-01",
                            "2024-02",
                            "2024-03",
                            "2024-04",
                            "2024-05",
                            "2024-06",
                            "2024-07",
                            "2024-08",
                            "2024-09",
                            "2024-10"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "zmePAE",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 0,
                "row": 18,
                "colspan": 16,
                "rowspan": 12,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Category"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Category",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "Category",
                        "field_defs": [
                            "Category"
                        ],
                        "field_labels": [
                            "Category"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Accessories",
                            "Audio",
                            "Computing",
                            "Home Entertainment",
                            "Mobile",
                            "Smart Home"
                        ],
                        "sample_values": [
                            "Accessories",
                            "Audio",
                            "Computing",
                            "Home Entertainment",
                            "Mobile",
                            "Smart Home"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "Category",
                        "field_defs": [
                            "Category"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Accessories",
                            "Audio",
                            "Computing",
                            "Home Entertainment",
                            "Mobile",
                            "Smart Home"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "Zktknb",
                "qlik_type": "filterpane",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 0,
                "row": 30,
                "colspan": 16,
                "rowspan": 12,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Region"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Region",
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
                "style_and_formatting": {
                    "title": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "name": "Region",
                        "field_defs": [
                            "Region"
                        ],
                        "field_labels": [
                            "Region"
                        ],
                        "source": "listbox",
                        "definition_path": "qListObjectDef",
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Midwest",
                            "Northeast",
                            "Southeast",
                            "Southwest",
                            "West"
                        ],
                        "sample_values": [
                            "Midwest",
                            "Northeast",
                            "Southeast",
                            "Southwest",
                            "West"
                        ]
                    }
                ],
                "filters": [
                    {
                        "type": "field_filter",
                        "name": "Region",
                        "field_defs": [
                            "Region"
                        ],
                        "source": "inline",
                        "frequency_mode": "N",
                        "show_alternatives": true,
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "qlik": {
                                "qNullSuppression": false
                            }
                        },
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "STATE",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByState": 1,
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "values": [
                            "Midwest",
                            "Northeast",
                            "Southeast",
                            "Southwest",
                            "West"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "PkCUyU",
                "qlik_type": "kpi",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 16,
                "row": 0,
                "colspan": 17,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "y_axis": [
                    "Total Revenue"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Total Revenue",
                    "title_font_size": "M",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_size": "M",
                        "font_family": "Inter, sans-serif",
                        "show": false
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "center"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif"
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
                    "fontSize": "M"
                },
                "measures": [
                    {
                        "index": 0,
                        "name": "Total Revenue",
                        "expression": "=If(\r\nSum(TotalAmount) >= 1000000000,\n'$' & Num(Sum(TotalAmount)/1000000000, '#,##0.0') & 'B',\nIf(\nSum(TotalAmount) >= 1000000,\n'$' & Num(Sum(TotalAmount)/1000000, '#,##0.0') & 'M',\nIf(\nSum(TotalAmount) >= 1000,\n'$' & Num(Sum(TotalAmount)/1000, '#,##0.0') & 'K',\n'$' & Num(Sum(TotalAmount), '#,##0')\n)\n)\n)",
                        "label": "Total Revenue",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "yZQKYx",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Total Revenue",
                        "expression": "=If(\r\nSum(TotalAmount) >= 1000000000,\n'$' & Num(Sum(TotalAmount)/1000000000, '#,##0.0') & 'B',\nIf(\nSum(TotalAmount) >= 1000000,\n'$' & Num(Sum(TotalAmount)/1000000, '#,##0.0') & 'M',\nIf(\nSum(TotalAmount) >= 1000,\n'$' & Num(Sum(TotalAmount)/1000, '#,##0.0') & 'K',\n'$' & Num(Sum(TotalAmount), '#,##0')\n)\n)\n)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "tCCX",
                "qlik_type": "kpi",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 33,
                "row": 0,
                "colspan": 17,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "y_axis": [
                    "Transactions"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Transactions",
                    "title_font_size": "M",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_size": "M",
                        "font_family": "Inter, sans-serif",
                        "show": false
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "center"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif",
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
                "measures": [
                    {
                        "index": 0,
                        "name": "Transactions",
                        "expression": "Count(TransactionID)\r\n",
                        "label": "Transactions",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "yZQKYx",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Transactions",
                        "expression": "Count(TransactionID)\r\n",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "kJjznzb",
                "qlik_type": "kpi",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 50,
                "row": 0,
                "colspan": 17,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "y_axis": [
                    "Avg Transaction Value"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Avg Transaction Value",
                    "title_font_size": "M",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_size": "M",
                        "font_family": "Inter, sans-serif",
                        "show": false
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "center"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif",
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
                            "qFmt": "$#,##0.0",
                            "qDec": ".",
                            "qThou": ","
                        }
                    ],
                    "text_align": "center",
                    "fontSize": "M"
                },
                "measures": [
                    {
                        "index": 0,
                        "name": "Avg Transaction Value",
                        "expression": "Avg(TotalAmount)",
                        "label": "Avg Transaction Value",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "yZQKYx",
                        "num_format": {
                            "qType": "R",
                            "qnDec": 2,
                            "qUseThou": 0,
                            "qFmt": "$#,##0.0",
                            "qDec": ".",
                            "qThou": ","
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Avg Transaction Value",
                        "expression": "Avg(TotalAmount)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "yUjsQd",
                "qlik_type": "kpi",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 67,
                "row": 0,
                "colspan": 17,
                "rowspan": 6,
                "source": "Sales Dashboard",
                "y_axis": [
                    "Units Sold"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": false,
                    "title": "Units Sold",
                    "title_font_size": "M",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_size": "M",
                        "font_family": "Inter, sans-serif",
                        "show": false
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "center"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif",
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
                "measures": [
                    {
                        "index": 0,
                        "name": "Units Sold",
                        "expression": "Sum(Quantity)",
                        "label": "Units Sold",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "yZQKYx",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Units Sold",
                        "expression": "Sum(Quantity)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "HJXQPk",
                "qlik_type": "linechart",
                "bi_type": "chart",
                "bi_name_prefix": "GEN_",
                "col": 16,
                "row": 6,
                "colspan": 34,
                "rowspan": 17,
                "source": "Sales Dashboard",
                "x_axis": [
                    "MonthYear"
                ],
                "y_axis": [
                    "Revneue"
                ],
                "color": {
                    "auto": false,
                    "mode": "primary",
                    "single_color": "#009845",
                    "raw_single_color": "#009845",
                    "dimension_scheme": "12",
                    "measure_scheme": "sg",
                    "palette_index": -1,
                    "palette_scheme": "12",
                    "is_multicolor": true,
                    "use_base_colors": "on"
                },
                "formatting": {
                    "show_titles": true,
                    "title": "Monthly Revenue Trend",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": true,
                        "dock": "auto"
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_family": "Inter, sans-serif",
                        "show": true
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "left"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "colorScheme": {
                        "auto": false,
                        "mode": "primary",
                        "formatting": {
                            "numFormatFromTemplate": true
                        },
                        "useBaseColors": "off",
                        "paletteColor": {
                            "index": -1,
                            "color": "#009845",
                            "alpha": 1
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
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif"
                    },
                    "data_colors": {
                        "primary": "#009845",
                        "mode": "primary",
                        "auto": false
                    },
                    "axes": {
                        "dimension_axis": {
                            "continuousAuto": true,
                            "show": "labels",
                            "label": "auto",
                            "dock": "near",
                            "axisDisplayMode": "auto",
                            "maxVisibleItems": 10
                        },
                        "measure_axis": {
                            "show": "labels",
                            "dock": "near",
                            "spacing": 2,
                            "autoMinMax": true,
                            "minMax": "min",
                            "min": 0,
                            "max": 10,
                            "logarithmic": false
                        },
                        "gridlines": {
                            "auto": false,
                            "spacing": 0
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
                "dimensions": [
                    {
                        "index": 0,
                        "name": "MonthYear",
                        "field_defs": [
                            "MonthYear"
                        ],
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "grouping": "N",
                        "is_calculated": false,
                        "cId": "VCFxp",
                        "null_suppression": false,
                        "other_total_spec": {
                            "qOtherMode": "OTHER_OFF",
                            "qOtherCounted": {
                                "qv": "10"
                            },
                            "qOtherLimit": {
                                "qv": "0"
                            },
                            "qOtherLimitMode": "OTHER_GE_LIMIT",
                            "qForceBadValueKeeping": true,
                            "qApplyEvenWhenPossiblyWrongResult": true,
                            "qOtherSortMode": "OTHER_SORT_DESCENDING",
                            "qTotalMode": "TOTAL_OFF"
                        },
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "sort_mode": "OTHER_SORT_DESCENDING",
                            "limit_mode": "OTHER_GE_LIMIT",
                            "qlik": {
                                "qOtherMode": "OTHER_OFF",
                                "qOtherCounted": {
                                    "qv": "10"
                                },
                                "qOtherLimit": {
                                    "qv": "0"
                                },
                                "qOtherLimitMode": "OTHER_GE_LIMIT",
                                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                                "qTotalMode": "TOTAL_OFF",
                                "qOtherLabel": {
                                    "qv": "Others"
                                },
                                "qForceBadValueKeeping": true,
                                "qApplyEvenWhenPossiblyWrongResult": true,
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "sort_position": 0,
                        "values": [
                            "2024-01",
                            "2024-02",
                            "2024-03",
                            "2024-04",
                            "2024-05",
                            "2024-06",
                            "2024-07",
                            "2024-08",
                            "2024-09",
                            "2024-10"
                        ],
                        "sample_values": [
                            "2024-01",
                            "2024-02",
                            "2024-03",
                            "2024-04",
                            "2024-05",
                            "2024-06",
                            "2024-07",
                            "2024-08",
                            "2024-09",
                            "2024-10"
                        ]
                    }
                ],
                "measures": [
                    {
                        "index": 0,
                        "name": "Revneue",
                        "expression": "Sum({<MonthYear=>}TotalAmount)",
                        "label": "Revneue",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "BvKvp",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Revneue",
                        "expression": "Sum({<MonthYear=>}TotalAmount)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "MTaN",
                "qlik_type": "map",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 16,
                "row": 23,
                "colspan": 34,
                "rowspan": 19,
                "source": "Sales Dashboard",
                "x_axis": [
                    "City",
                    "State"
                ],
                "color": {
                    "is_multicolor": false,
                    "use_base_colors": "off"
                },
                "formatting": {
                    "show_titles": true,
                    "title": "Stores",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_family": "Inter, sans-serif",
                        "show": true
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "left"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif"
                    },
                    "legend": {
                        "show": false
                    }
                },
                "dimensions": [
                    {
                        "index": 0,
                        "name": "City",
                        "field_defs": [
                            "City"
                        ],
                        "source": "inline",
                        "definition_path": "qUndoExclude.layers[0].qHyperCubeDef",
                        "nested": true,
                        "grouping": "N",
                        "is_calculated": false,
                        "cId": "JHANC",
                        "null_suppression": false,
                        "other_total_spec": {
                            "qOtherMode": "OTHER_OFF",
                            "qOtherLimitMode": "OTHER_GT_LIMIT",
                            "qForceBadValueKeeping": true,
                            "qApplyEvenWhenPossiblyWrongResult": true,
                            "qOtherSortMode": "OTHER_SORT_DESCENDING",
                            "qTotalMode": "TOTAL_OFF"
                        },
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "sort_mode": "OTHER_SORT_DESCENDING",
                            "limit_mode": "OTHER_GT_LIMIT",
                            "qlik": {
                                "qOtherMode": "OTHER_OFF",
                                "qOtherLimitMode": "OTHER_GT_LIMIT",
                                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                                "qTotalMode": "TOTAL_OFF",
                                "qForceBadValueKeeping": true,
                                "qApplyEvenWhenPossiblyWrongResult": true,
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "sort_position": 0,
                        "values": [
                            "Atlanta",
                            "Austin",
                            "Boston",
                            "Brooklyn",
                            "Charlotte",
                            "Chicago",
                            "Columbus",
                            "Dallas",
                            "Denver",
                            "Detroit"
                        ],
                        "sample_values": [
                            "Atlanta",
                            "Austin",
                            "Boston",
                            "Brooklyn",
                            "Charlotte",
                            "Chicago",
                            "Columbus",
                            "Dallas",
                            "Denver",
                            "Detroit"
                        ]
                    },
                    {
                        "index": 0,
                        "name": "State",
                        "field_defs": [
                            "State"
                        ],
                        "source": "inline",
                        "definition_path": "qUndoExclude.layers[1].qHyperCubeDef",
                        "nested": true,
                        "grouping": "N",
                        "is_calculated": false,
                        "cId": "fVhSDA",
                        "null_suppression": false,
                        "other_total_spec": {
                            "qOtherMode": "OTHER_OFF",
                            "qOtherLimitMode": "OTHER_GT_LIMIT",
                            "qForceBadValueKeeping": true,
                            "qApplyEvenWhenPossiblyWrongResult": true,
                            "qOtherSortMode": "OTHER_SORT_DESCENDING",
                            "qTotalMode": "TOTAL_OFF"
                        },
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "sort_mode": "OTHER_SORT_DESCENDING",
                            "limit_mode": "OTHER_GT_LIMIT",
                            "qlik": {
                                "qOtherMode": "OTHER_OFF",
                                "qOtherLimitMode": "OTHER_GT_LIMIT",
                                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                                "qTotalMode": "TOTAL_OFF",
                                "qForceBadValueKeeping": true,
                                "qApplyEvenWhenPossiblyWrongResult": true,
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "sort_position": 0,
                        "values": [
                            "AZ",
                            "CA",
                            "CO",
                            "CT",
                            "FL",
                            "GA",
                            "IL",
                            "IN",
                            "MA",
                            "MI"
                        ],
                        "sample_values": [
                            "AZ",
                            "CA",
                            "CO",
                            "CT",
                            "FL",
                            "GA",
                            "IL",
                            "IN",
                            "MA",
                            "MI"
                        ]
                    }
                ]
            },
            {
                "qlik_name": "ucFxL",
                "qlik_type": "barchart",
                "bi_type": "chart",
                "bi_name_prefix": "BAR_",
                "col": 50,
                "row": 23,
                "colspan": 34,
                "rowspan": 19,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Region Drill-down"
                ],
                "y_axis": [
                    "Revenue"
                ],
                "color": {
                    "auto": false,
                    "mode": "primary",
                    "single_color": "#009845",
                    "raw_single_color": "#009845",
                    "dimension_scheme": "12",
                    "measure_scheme": "dg",
                    "palette_index": -1,
                    "palette_scheme": "12",
                    "is_multicolor": true,
                    "use_base_colors": "on"
                },
                "formatting": {
                    "show_titles": true,
                    "title": "Revenue by Region",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": false,
                        "dock": "auto"
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_family": "Inter, sans-serif",
                        "show": true
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "left"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "colorScheme": {
                        "auto": false,
                        "mode": "primary",
                        "formatting": {
                            "numFormatFromTemplate": true
                        },
                        "useBaseColors": "off",
                        "paletteColor": {
                            "index": -1,
                            "color": "#009845",
                            "alpha": 1
                        },
                        "useDimColVal": true,
                        "useMeasureGradient": true,
                        "persistent": false,
                        "expressionIsColor": true,
                        "measureScheme": "dg",
                        "reverseScheme": false,
                        "dimensionScheme": "12",
                        "autoMinMax": true,
                        "measureMin": 0,
                        "measureMax": 10,
                        "altLabel": "Revenue",
                        "byMeasureDef": {
                            "label": "Revenue",
                            "key": "Sum(TotalAmount)",
                            "type": "expression"
                        }
                    },
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif"
                    },
                    "data_colors": {
                        "primary": "#009845",
                        "mode": "primary",
                        "auto": false,
                        "by_measure": {
                            "label": "Revenue",
                            "key": "Sum(TotalAmount)",
                            "type": "expression"
                        }
                    },
                    "axes": {
                        "dimension_axis": {
                            "continuousAuto": true,
                            "show": "labels",
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
                    "orientation": "horizontal",
                    "bar_grouping": {
                        "grouping": "grouped"
                    }
                },
                "dimensions": [
                    {
                        "index": 0,
                        "name": "Region Drill-down",
                        "field_defs": [
                            "=Region",
                            "=State",
                            "=City"
                        ],
                        "source": "master",
                        "library_id": "JeqfUpL",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "grouping": "N",
                        "is_calculated": false,
                        "cId": "WXwSyP",
                        "null_suppression": false,
                        "other_total_spec": {
                            "qOtherMode": "OTHER_OFF",
                            "qOtherCounted": {
                                "qv": "10"
                            },
                            "qOtherLimit": {
                                "qv": "0"
                            },
                            "qOtherLimitMode": "OTHER_GE_LIMIT",
                            "qForceBadValueKeeping": true,
                            "qApplyEvenWhenPossiblyWrongResult": true,
                            "qOtherSortMode": "OTHER_SORT_DESCENDING",
                            "qTotalMode": "TOTAL_OFF"
                        },
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "sort_mode": "OTHER_SORT_DESCENDING",
                            "limit_mode": "OTHER_GE_LIMIT",
                            "qlik": {
                                "qOtherMode": "OTHER_OFF",
                                "qOtherCounted": {
                                    "qv": "10"
                                },
                                "qOtherLimit": {
                                    "qv": "0"
                                },
                                "qOtherLimitMode": "OTHER_GE_LIMIT",
                                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                                "qTotalMode": "TOTAL_OFF",
                                "qOtherLabel": {
                                    "qv": "Others"
                                },
                                "qForceBadValueKeeping": true,
                                "qApplyEvenWhenPossiblyWrongResult": true,
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "sort_position": 1,
                        "coloring": {
                            "changeHash": "0.02489744739661881",
                            "hasValueColors": false
                        },
                        "values": [
                            "Northeast",
                            "Southeast",
                            "Midwest",
                            "West",
                            "Southwest"
                        ],
                        "sample_values": [
                            "Northeast",
                            "Southeast",
                            "Midwest",
                            "West",
                            "Southwest"
                        ]
                    }
                ],
                "measures": [
                    {
                        "index": 0,
                        "name": "Revenue",
                        "expression": "Sum(TotalAmount)",
                        "label": "Revenue",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "AewLW",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Revenue",
                        "expression": "Sum(TotalAmount)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            },
            {
                "qlik_name": "aQjWrZy",
                "qlik_type": "piechart",
                "bi_type": "other",
                "bi_name_prefix": "GEN_",
                "col": 50,
                "row": 6,
                "colspan": 34,
                "rowspan": 17,
                "source": "Sales Dashboard",
                "x_axis": [
                    "Category -> Sub Category"
                ],
                "y_axis": [
                    "Revenue"
                ],
                "color": {
                    "auto": true,
                    "mode": "byDimension",
                    "single_color": "#19426c",
                    "raw_single_color": "#19426c",
                    "dimension_scheme": "12",
                    "measure_scheme": "sg",
                    "palette_index": -1,
                    "palette_scheme": "12",
                    "is_multicolor": true,
                    "use_base_colors": "on"
                },
                "formatting": {
                    "show_titles": true,
                    "title": "Revenue by Category",
                    "title_font_family": "Inter, sans-serif",
                    "border": {
                        "show": false
                    },
                    "legend": {
                        "show": true,
                        "dock": "auto"
                    }
                },
                "kpi_styling": {
                    "value_font_size": "36",
                    "value_font_family": "Inter, sans-serif",
                    "label_color": "#54565a",
                    "label_font_size": "14",
                    "label_font_family": "Inter, sans-serif",
                    "align": "center"
                },
                "style_and_formatting": {
                    "title": {
                        "font_family": "Inter, sans-serif",
                        "show": true
                    },
                    "components": [
                        {
                            "key": "general",
                            "borderWidth": "0px",
                            "title": {
                                "main": {
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "textAlignment",
                            "textAlignment": "left"
                        },
                        {
                            "key": "textBehavior",
                            "textBehavior": "fixed"
                        },
                        {
                            "key": "useAdvancedMode",
                            "useAdvancedMode": true
                        },
                        {
                            "key": "simpleSettings"
                        },
                        {
                            "key": "firstMeasureTitle",
                            "label": {
                                "name": {
                                    "fontSize": {
                                        "fixed": "14"
                                    },
                                    "color": {
                                        "index": -1,
                                        "color": "#54565a",
                                        "alpha": 1
                                    },
                                    "fontFamily": "Inter, sans-serif"
                                }
                            }
                        },
                        {
                            "key": "firstMeasureValue",
                            "label": {
                                "value": {
                                    "fontSize": {
                                        "fixed": "36"
                                    },
                                    "fontFamily": "Inter, sans-serif",
                                    "fontStyle": [
                                        "bold"
                                    ]
                                }
                            }
                        },
                        {
                            "key": "secondMeasureTitle"
                        },
                        {
                            "key": "secondMeasureValue"
                        }
                    ],
                    "colorScheme": {
                        "auto": true,
                        "mode": "byDimension",
                        "formatting": {
                            "numFormatFromTemplate": true
                        },
                        "useBaseColors": "off",
                        "paletteColor": {
                            "index": -1,
                            "color": "#19426c",
                            "alpha": 1
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
                        "measureMax": 10,
                        "altLabel": "Category Colored",
                        "byMeasureDef": {
                            "label": "Revenue",
                            "key": "Avg(TotalAmount)",
                            "type": "expression"
                        },
                        "byDimDef": {
                            "label": "Category Colored",
                            "key": "yFMU",
                            "type": "libraryItem"
                        }
                    },
                    "kpi": {
                        "value_font_size": "36",
                        "value_font_family": "Inter, sans-serif",
                        "label_color": "#54565a",
                        "label_font_size": "14",
                        "label_font_family": "Inter, sans-serif"
                    },
                    "data_colors": {
                        "primary": "#19426c",
                        "mode": "byDimension",
                        "auto": true,
                        "by_measure": {
                            "label": "Revenue",
                            "key": "Avg(TotalAmount)",
                            "type": "expression"
                        },
                        "by_dimension": {
                            "label": "Category Colored",
                            "key": "yFMU",
                            "type": "libraryItem"
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
                    ]
                },
                "dimensions": [
                    {
                        "index": 0,
                        "name": "Category -> Sub Category",
                        "field_defs": [
                            "=Category",
                            "=SubCategory"
                        ],
                        "source": "master",
                        "library_id": "xtBsadm",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "grouping": "N",
                        "is_calculated": false,
                        "cId": "pPJmvs",
                        "null_suppression": false,
                        "other_total_spec": {
                            "qOtherMode": "OTHER_OFF",
                            "qOtherCounted": {
                                "qv": "10"
                            },
                            "qOtherLimit": {
                                "qv": "0"
                            },
                            "qOtherLimitMode": "OTHER_GE_LIMIT",
                            "qForceBadValueKeeping": true,
                            "qApplyEvenWhenPossiblyWrongResult": true,
                            "qOtherSortMode": "OTHER_SORT_DESCENDING",
                            "qTotalMode": "TOTAL_OFF"
                        },
                        "limitation": {
                            "limitation_type": "None",
                            "show_others": false,
                            "others_label": "Others",
                            "include_null_values": true,
                            "show_total": false,
                            "mode": "OTHER_OFF",
                            "show_other": false,
                            "other_label": "Others",
                            "suppress_null": false,
                            "sort_mode": "OTHER_SORT_DESCENDING",
                            "limit_mode": "OTHER_GE_LIMIT",
                            "qlik": {
                                "qOtherMode": "OTHER_OFF",
                                "qOtherCounted": {
                                    "qv": "10"
                                },
                                "qOtherLimit": {
                                    "qv": "0"
                                },
                                "qOtherLimitMode": "OTHER_GE_LIMIT",
                                "qOtherSortMode": "OTHER_SORT_DESCENDING",
                                "qTotalMode": "TOTAL_OFF",
                                "qOtherLabel": {
                                    "qv": "Others"
                                },
                                "qForceBadValueKeeping": true,
                                "qApplyEvenWhenPossiblyWrongResult": true,
                                "qNullSuppression": false
                            }
                        },
                        "include_null_values": true,
                        "sorting": {
                            "auto": true,
                            "criteria": [
                                {
                                    "key": "NUMERIC",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "ALPHABETICAL",
                                    "direction": "ASCENDING"
                                },
                                {
                                    "key": "LOAD_ORDER",
                                    "direction": "ASCENDING"
                                }
                            ],
                            "raw": {
                                "qSortByNumeric": 1,
                                "qSortByAscii": 1,
                                "qSortByLoadOrder": 1
                            },
                            "mode": "explicit"
                        },
                        "sort_position": 1,
                        "coloring": {
                            "changeHash": "0.7098929872275918",
                            "hasValueColors": false
                        },
                        "values": [
                            "Computing",
                            "Home Entertainment",
                            "Mobile",
                            "Smart Home",
                            "Audio",
                            "Accessories"
                        ],
                        "sample_values": [
                            "Computing",
                            "Home Entertainment",
                            "Mobile",
                            "Smart Home",
                            "Audio",
                            "Accessories"
                        ]
                    }
                ],
                "measures": [
                    {
                        "index": 0,
                        "name": "Revenue",
                        "expression": "Avg(TotalAmount)",
                        "label": "Revenue",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef",
                        "nested": false,
                        "cId": "AewLW",
                        "num_format": {
                            "qType": "U",
                            "qnDec": 10,
                            "qUseThou": 0
                        },
                        "is_custom_formatted": false,
                        "grouping": "N",
                        "active_expression": 0,
                        "sorting": {
                            "auto": true,
                            "mode": "auto"
                        },
                        "sort_position": 0
                    }
                ],
                "expressions_and_formulas": [
                    {
                        "name": "Revenue",
                        "expression": "Avg(TotalAmount)",
                        "source": "inline",
                        "definition_path": "qHyperCubeDef"
                    }
                ]
            }
        ],
        "visualization_count": 14,
        "filter_panes": [
            {
                "id": "cae59556-f77f-4e67-8643-e262ccdfa278",
                "title": "Date_year"
            },
            {
                "id": "7e0a2adc-dc0d-4447-b57b-eac3e614a25c",
                "title": "Date_monthLabel"
            },
            {
                "id": "bb302939-c204-4265-9ccd-2a34e7c2b6d9",
                "title": "Date_quarterLabel"
            },
            {
                "id": "1a4cb80b-8fa1-4561-ba55-af343096d8a1",
                "title": "MonthYear"
            },
            {
                "id": "e11be670-7608-4e88-8352-915e4c1801a3",
                "title": "Category"
            },
            {
                "id": "d571a81e-109e-401f-b745-a6c479cf7531",
                "title": "Region"
            }
        ],
        "filter_pane_count": 6,
        "measures": [
            {
                "name": "Total Revenue",
                "expression": "Sum(TotalAmount)",
                "tables": [
                    "Sales"
                ],
                "numFormat": {
                    "qType": "F",
                    "qnDec": 2,
                    "qUseThou": 1,
                    "qFmt": "#,##0.00",
                    "qDec": ".",
                    "qThou": ","
                }
            }
        ],
        "measure_count": 1,
        "dimensions": [
            {
                "name": "Region Drill-down",
                "expression": "=Region",
                "dataType": "STRING",
                "nature": "TEXT",
                "tables": [
                    "Stores"
                ]
            },
            {
                "name": "Category -> Sub Category",
                "expression": "=Category",
                "dataType": "STRING",
                "nature": "TEXT",
                "tables": [
                    "Products"
                ]
            },
            {
                "name": "Category",
                "expression": "=Category",
                "dataType": "STRING (CALCULATED)",
                "nature": "TEXT",
                "tables": [
                    "Products"
                ]
            }
        ],
        "dimension_count": 3,
        "relationships": [
            {
                "key_field": "StoreID",
                "cardinality": "many-to-one",
                "references": [
                    {
                        "table": "Sales",
                        "column": "StoreID"
                    },
                    {
                        "table": "Stores",
                        "column": "StoreID"
                    }
                ]
            },
            {
                "key_field": "ProductID",
                "cardinality": "many-to-one",
                "references": [
                    {
                        "table": "Sales",
                        "column": "ProductID"
                    },
                    {
                        "table": "Products",
                        "column": "ProductID"
                    }
                ]
            }
        ],
        "relationship_count": 2,
        "tables": [
            {
                "name": "Sales",
                "table_name": "Sales",
                "load_type": "source",
                "source_type": "file",
                "qlik_query": "\n\n// --- Source Part ---\nLOAD\r\n    TransactionID,\r\n    \"Date\",\r\n    Date_monthLabel,\r\n    Date_quarterLabel,\r\n    Date_yearMonth as MonthYear,\r\n    Date_year,\r\n    StoreID,\r\n    ProductID,\r\n    EmployeeID,\r\n    Quantity,\r\n    UnitPrice,\r\n    DiscountPct,\r\n    TotalAmount,\r\n    PaymentMethod\r\nFROM [lib://Trial:DataFiles/Sales.qvd]\r\n(qvd)",
                "query": "\n\n// --- Source Part ---\nLOAD\r\n    TransactionID,\r\n    \"Date\",\r\n    Date_monthLabel,\r\n    Date_quarterLabel,\r\n    Date_yearMonth as MonthYear,\r\n    Date_year,\r\n    StoreID,\r\n    ProductID,\r\n    EmployeeID,\r\n    Quantity,\r\n    UnitPrice,\r\n    DiscountPct,\r\n    TotalAmount,\r\n    PaymentMethod\r\nFROM [lib://Trial:DataFiles/Sales.qvd]\r\n(qvd)",
                "load_statement": "\n\n// --- Source Part ---\nLOAD\r\n    TransactionID,\r\n    \"Date\",\r\n    Date_monthLabel,\r\n    Date_quarterLabel,\r\n    Date_yearMonth as MonthYear,\r\n    Date_year,\r\n    StoreID,\r\n    ProductID,\r\n    EmployeeID,\r\n    Quantity,\r\n    UnitPrice,\r\n    DiscountPct,\r\n    TotalAmount,\r\n    PaymentMethod\r\nFROM [lib://Trial:DataFiles/Sales.qvd]\r\n(qvd)",
                "source": "lib://Trial:DataFiles/Sales.qvd",
                "sourceType": "file",
                "connection": "DataFiles",
                "connection_details": "DataFiles",
                "fields": [
                    {
                        "Name": "TransactionID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "Date",
                        "dataType": "DATE",
                        "nature": "DATE_SERIAL",
                        "format": "YYYY-MM-DD"
                    },
                    {
                        "Name": "Date_monthLabel",
                        "dataType": "TIME",
                        "nature": "TIME_SECONDS",
                        "format": "YYYY-MM-DD"
                    },
                    {
                        "Name": "Date_quarterLabel",
                        "dataType": "TIME",
                        "nature": "TIME_SECONDS",
                        "format": "YYYY-MM-DD"
                    },
                    {
                        "Name": "MonthYear",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "Date_year",
                        "dataType": "NUMBER",
                        "nature": "INTEGER",
                        "format": "###0"
                    },
                    {
                        "Name": "StoreID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "ProductID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "EmployeeID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "Quantity",
                        "dataType": "NUMBER",
                        "nature": "INTEGER",
                        "format": "#,##0"
                    },
                    {
                        "Name": "UnitPrice",
                        "dataType": "NUMBER",
                        "nature": "DECIMAL",
                        "format": "#,##0.00"
                    },
                    {
                        "Name": "DiscountPct",
                        "dataType": "NUMBER",
                        "nature": "INTEGER",
                        "format": "#,##0"
                    },
                    {
                        "Name": "TotalAmount",
                        "dataType": "NUMBER",
                        "nature": "DECIMAL",
                        "format": "#,##0.00"
                    },
                    {
                        "Name": "PaymentMethod",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    }
                ]
            },
            {
                "name": "Stores",
                "table_name": "Stores",
                "load_type": "source",
                "source_type": "file",
                "qlik_query": "\n\n// --- Source Part ---\nLOAD\r\n    StoreID,\r\n    StoreName,\r\n    City,\r\n    State,\r\n    Region,\r\n    StoreType,\r\n    SquareFootage,\r\n    StoreManager\r\nFROM [lib://Trial:DataFiles/Stores.qvd]\r\n(qvd)",
                "query": "\n\n// --- Source Part ---\nLOAD\r\n    StoreID,\r\n    StoreName,\r\n    City,\r\n    State,\r\n    Region,\r\n    StoreType,\r\n    SquareFootage,\r\n    StoreManager\r\nFROM [lib://Trial:DataFiles/Stores.qvd]\r\n(qvd)",
                "load_statement": "\n\n// --- Source Part ---\nLOAD\r\n    StoreID,\r\n    StoreName,\r\n    City,\r\n    State,\r\n    Region,\r\n    StoreType,\r\n    SquareFootage,\r\n    StoreManager\r\nFROM [lib://Trial:DataFiles/Stores.qvd]\r\n(qvd)",
                "source": "lib://Trial:DataFiles/Stores.qvd",
                "sourceType": "file",
                "connection": "DataFiles",
                "connection_details": "DataFiles",
                "fields": [
                    {
                        "Name": "StoreID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "StoreName",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "City",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "State",
                        "dataType": "STRING",
                        "nature": "STATE",
                        "format": "General Text"
                    },
                    {
                        "Name": "Region",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "StoreType",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "SquareFootage",
                        "dataType": "NUMBER",
                        "nature": "INTEGER",
                        "format": "#,##0"
                    },
                    {
                        "Name": "StoreManager",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    }
                ]
            },
            {
                "name": "Products",
                "table_name": "Products",
                "load_type": "source",
                "source_type": "file",
                "qlik_query": "\n\n// --- Source Part ---\nLOAD\r\n    ProductID,\r\n    ProductName,\r\n    Category,\r\n    SubCategory,\r\n    Brand,\r\n    UnitCost,\r\n    RetailPrice,\r\n    MarginPct,\r\n    Supplier\r\nFROM [lib://Trial:DataFiles/Products.qvd]\r\n(qvd)",
                "query": "\n\n// --- Source Part ---\nLOAD\r\n    ProductID,\r\n    ProductName,\r\n    Category,\r\n    SubCategory,\r\n    Brand,\r\n    UnitCost,\r\n    RetailPrice,\r\n    MarginPct,\r\n    Supplier\r\nFROM [lib://Trial:DataFiles/Products.qvd]\r\n(qvd)",
                "load_statement": "\n\n// --- Source Part ---\nLOAD\r\n    ProductID,\r\n    ProductName,\r\n    Category,\r\n    SubCategory,\r\n    Brand,\r\n    UnitCost,\r\n    RetailPrice,\r\n    MarginPct,\r\n    Supplier\r\nFROM [lib://Trial:DataFiles/Products.qvd]\r\n(qvd)",
                "source": "lib://Trial:DataFiles/Products.qvd",
                "sourceType": "file",
                "connection": "DataFiles",
                "connection_details": "DataFiles",
                "fields": [
                    {
                        "Name": "ProductID",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "ProductName",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "Category",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "SubCategory",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "Brand",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    },
                    {
                        "Name": "UnitCost",
                        "dataType": "NUMBER",
                        "nature": "DECIMAL",
                        "format": "#,##0.00"
                    },
                    {
                        "Name": "RetailPrice",
                        "dataType": "NUMBER",
                        "nature": "DECIMAL",
                        "format": "#,##0.00"
                    },
                    {
                        "Name": "MarginPct",
                        "dataType": "NUMBER",
                        "nature": "DECIMAL",
                        "format": "#,##0.00"
                    },
                    {
                        "Name": "Supplier",
                        "dataType": "STRING",
                        "nature": "TEXT",
                        "format": "General Text"
                    }
                ]
            }
        ],
        "queries": [
            "\n\n// --- Source Part ---\nLOAD\r\n    TransactionID,\r\n    \"Date\",\r\n    Date_monthLabel,\r\n    Date_quarterLabel,\r\n    Date_yearMonth as MonthYear,\r\n    Date_year,\r\n    StoreID,\r\n    ProductID,\r\n    EmployeeID,\r\n    Quantity,\r\n    UnitPrice,\r\n    DiscountPct,\r\n    TotalAmount,\r\n    PaymentMethod\r\nFROM [lib://Trial:DataFiles/Sales.qvd]\r\n(qvd)",
            "\n\n// --- Source Part ---\nLOAD\r\n    StoreID,\r\n    StoreName,\r\n    City,\r\n    State,\r\n    Region,\r\n    StoreType,\r\n    SquareFootage,\r\n    StoreManager\r\nFROM [lib://Trial:DataFiles/Stores.qvd]\r\n(qvd)",
            "\n\n// --- Source Part ---\nLOAD\r\n    ProductID,\r\n    ProductName,\r\n    Category,\r\n    SubCategory,\r\n    Brand,\r\n    UnitCost,\r\n    RetailPrice,\r\n    MarginPct,\r\n    Supplier\r\nFROM [lib://Trial:DataFiles/Products.qvd]\r\n(qvd)"
        ],
        "datasources": [
            {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            {
                "datasource_id": "ds_2",
                "name": "MyDataFiles",
                "connector_type": "qix-datafiles.exe",
                "connection_id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc"
            },
            {
                "datasource_id": "ds_3",
                "name": "DataFiles",
                "connector_type": "qix-datafiles.exe",
                "connection_id": "6f93cda1-15c4-4321-94e7-ac3cdcab5e4c"
            }
        ],
        "calculated_columns_count": 0,
        "stories": [
            {
                "qProperty": {
                    "qInfo": {
                        "qId": "wBvJeM",
                        "qType": "story"
                    },
                    "qMetaDef": {
                        "title": "My new story"
                    },
                    "creationDate": "2026-02-23T16:04:10.873Z",
                    "rank": -1,
                    "qChildListDef": {
                        "qData": {
                            "title": "/title",
                            "rank": "/rank"
                        }
                    }
                },
                "qChildren": [
                    {
                        "qProperty": {
                            "qInfo": {
                                "qId": "MUfWj",
                                "qType": "slide"
                            },
                            "rank": -1,
                            "qChildListDef": {
                                "qData": {
                                    "title": "/title",
                                    "sheetId": "/sheetId",
                                    "ratio": "/ratio",
                                    "position": "/position",
                                    "dataPath": "/dataPath",
                                    "srcPath": "/srcPath",
                                    "visualization": "/visualization",
                                    "visualizationType": "/visualizationType",
                                    "style": "/style"
                                }
                            }
                        }
                    }
                ],
                "id": "wBvJeM",
                "title": "My new story",
                "slides": [
                    {
                        "index": 0,
                        "id": "MUfWj",
                        "type": "slide",
                        "rank": -1,
                        "item_count": 0
                    }
                ],
                "slide_count": 1
            }
        ],
        "variables": [
            {
                "id": "59d141b1-cd89-4e93-8370-a3309785f13d",
                "name": "ErrorMode",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "59d141b1-cd89-4e93-8370-a3309785f13d",
                    "qType": "variable"
                }
            },
            {
                "id": "554e65e1-af7a-4fad-b963-33ff00c60049",
                "name": "ScriptErrorCount",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "554e65e1-af7a-4fad-b963-33ff00c60049",
                    "qType": "variable"
                }
            },
            {
                "id": "6f66acf3-0280-48e2-b5e0-30a3dbe8e488",
                "name": "DecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "6f66acf3-0280-48e2-b5e0-30a3dbe8e488",
                    "qType": "variable"
                }
            },
            {
                "id": "98dddcd3-dac8-4c8e-8014-433c7ca482e6",
                "name": "DateFormat",
                "definition": "M/D/YYYY",
                "value": "M/D/YYYY",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DateFormat='M/D/YYYY';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "98dddcd3-dac8-4c8e-8014-433c7ca482e6",
                    "qType": "variable"
                }
            },
            {
                "id": "fa5532e0-7dcd-4bfa-8d11-519331794ac0",
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
                    "qId": "fa5532e0-7dcd-4bfa-8d11-519331794ac0",
                    "qType": "variable"
                }
            },
            {
                "id": "b2ab4a3b-b522-4368-884c-3541ee05e9d9",
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
                    "qId": "b2ab4a3b-b522-4368-884c-3541ee05e9d9",
                    "qType": "variable"
                }
            },
            {
                "id": "0eb79812-4379-4600-a1b1-36ab6113039f",
                "name": "ScriptErrorList",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "0eb79812-4379-4600-a1b1-36ab6113039f",
                    "qType": "variable"
                }
            },
            {
                "id": "2afd3e94-aeee-4bc5-a61c-2f8d2e5b4785",
                "name": "MoneyThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "2afd3e94-aeee-4bc5-a61c-2f8d2e5b4785",
                    "qType": "variable"
                }
            },
            {
                "id": "1b8893ed-03a5-47d3-9a12-9c25b58ca118",
                "name": "MoneyFormat",
                "definition": "$ ###0.00;-$ ###0.00",
                "value": "$ ###0.00;-$ ###0.00",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyFormat='$ ###0.00;-$ ###0.00';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "1b8893ed-03a5-47d3-9a12-9c25b58ca118",
                    "qType": "variable"
                }
            },
            {
                "id": "c783cdaa-4fee-44cf-87ed-df955049438d",
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
                    "qId": "c783cdaa-4fee-44cf-87ed-df955049438d",
                    "qType": "variable"
                }
            },
            {
                "id": "72a2759b-b5b3-4759-a3f7-4fbfa2c2ba90",
                "name": "CollationLocale",
                "definition": "en-US",
                "value": "en-US",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET CollationLocale='en-US';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "72a2759b-b5b3-4759-a3f7-4fbfa2c2ba90",
                    "qType": "variable"
                }
            },
            {
                "id": "36393ef2-460e-4684-a210-8841dec8929f",
                "name": "MonthNames",
                "definition": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "value": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "36393ef2-460e-4684-a210-8841dec8929f",
                    "qType": "variable"
                }
            },
            {
                "id": "42cc9c6c-3210-4a99-abea-495b280ee39d",
                "name": "StripComments",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "42cc9c6c-3210-4a99-abea-495b280ee39d",
                    "qType": "variable"
                }
            },
            {
                "id": "f4c89936-ef87-4262-83dd-1b971372f12d",
                "name": "OpenUrlTimeout",
                "definition": "86400",
                "value": "86400",
                "num_value": 86400,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "f4c89936-ef87-4262-83dd-1b971372f12d",
                    "qType": "variable"
                }
            },
            {
                "id": "6d95f835-6a4e-4645-9737-ec513403bb59",
                "name": "ScriptError",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "6d95f835-6a4e-4645-9737-ec513403bb59",
                    "qType": "variable"
                }
            },
            {
                "id": "43601c6f-876e-4187-9906-04207a29acfa",
                "name": "ThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET ThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "43601c6f-876e-4187-9906-04207a29acfa",
                    "qType": "variable"
                }
            },
            {
                "id": "e200050a-0fb4-4640-a59e-e9c8d1053df4",
                "name": "TimeFormat",
                "definition": "h:mm:ss TT",
                "value": "h:mm:ss TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimeFormat='h:mm:ss TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "e200050a-0fb4-4640-a59e-e9c8d1053df4",
                    "qType": "variable"
                }
            },
            {
                "id": "60529632-c3bf-4ef4-9ed5-c0c4368bdc4c",
                "name": "TimestampFormat",
                "definition": "M/D/YYYY h:mm:ss[.fff] TT",
                "value": "M/D/YYYY h:mm:ss[.fff] TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "60529632-c3bf-4ef4-9ed5-c0c4368bdc4c",
                    "qType": "variable"
                }
            },
            {
                "id": "90311af4-5d33-46a2-ad89-b7b24b6c79f7",
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
                    "qId": "90311af4-5d33-46a2-ad89-b7b24b6c79f7",
                    "qType": "variable"
                }
            },
            {
                "id": "f9776463-d4a7-494c-96e5-ac078dec28d3",
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
                    "qId": "f9776463-d4a7-494c-96e5-ac078dec28d3",
                    "qType": "variable"
                }
            },
            {
                "id": "d26db1a4-75a9-49bb-bc58-8e5414618210",
                "name": "LongDayNames",
                "definition": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "value": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "d26db1a4-75a9-49bb-bc58-8e5414618210",
                    "qType": "variable"
                }
            },
            {
                "id": "eb549c77-435a-4193-bb41-6d54cacf5611",
                "name": "MoneyDecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyDecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "eb549c77-435a-4193-bb41-6d54cacf5611",
                    "qType": "variable"
                }
            },
            {
                "id": "a5c44c48-1789-47e2-9992-28485576a33e",
                "name": "LongMonthNames",
                "definition": "January;February;March;April;May;June;July;August;September;October;November;December",
                "value": "January;February;March;April;May;June;July;August;September;October;November;December",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "a5c44c48-1789-47e2-9992-28485576a33e",
                    "qType": "variable"
                }
            },
            {
                "id": "552e75a8-9354-4c57-8dc8-53adfd72ad14",
                "name": "DayNames",
                "definition": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "value": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "552e75a8-9354-4c57-8dc8-53adfd72ad14",
                    "qType": "variable"
                }
            },
            {
                "id": "0ada4e70-fecb-41a7-bde0-9e9371d4ec44",
                "name": "NumericalAbbreviation",
                "definition": "3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:\u03bc;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y",
                "value": "3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:\u03bc;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:\u03bc;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "0ada4e70-fecb-41a7-bde0-9e9371d4ec44",
                    "qType": "variable"
                }
            },
            {
                "id": "869ac7d2-261a-47cb-82a6-148fa0892877",
                "name": "vMaxDate",
                "definition": "46022",
                "value": "46022",
                "num_value": 46022,
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "869ac7d2-261a-47cb-82a6-148fa0892877",
                    "qType": "variable"
                }
            },
            {
                "id": "549d7ddc-90ce-48d5-9006-1e5a0a75ab1f",
                "name": "vNavBarActive",
                "definition": "overview",
                "value": "overview",
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "549d7ddc-90ce-48d5-9006-1e5a0a75ab1f",
                    "qType": "variable"
                }
            },
            {
                "id": "40950103-117c-4a01-8661-3d58e4307d77",
                "name": "vMinDate",
                "definition": "45292",
                "value": "45292",
                "num_value": 45292,
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "40950103-117c-4a01-8661-3d58e4307d77",
                    "qType": "variable"
                }
            },
            {
                "id": "f1d479a4-395d-458b-9567-fcecd78607f8",
                "name": "AnalysisAgentEnabled",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "f1d479a4-395d-458b-9567-fcecd78607f8",
                    "qType": "variable"
                }
            }
        ],
        "run_id": "8990-clean",
        "run_no": "8990-clean",
        "app_name": "Spark Electronics - Sales Dashboard",
        "workspace_id": "6a8d0f4ef5f61a1cd74d155f",
        "space_id": "6a8d0f4ef5f61a1cd74d155f"
    },
    "store_result": {
        "status": "success",
        "endpoint": "http://127.0.0.1:8008/parsing"
    }
}