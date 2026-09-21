{
    "status": "success",
    "message": "Generated 22 tables, 34 measures, 17 relationships, 3 pages, 49 visuals; needs review: 1 visual(s) substituted, 23 relationship(s) skipped. | Successfully deployed to github ()",
    "target": "fabric",
    "deploy": "github",
    "app_id": "afdeddc7-4dca-470b-bd3d-cdc279a1c408",
    "app_name": "FleetVision KSA",
    "run_id": "c-oihjb",
    "output_path": null,
    "file_count": 100,
    "summary": {
        "semantic_model": {
            "tables": 22,
            "measures": 34,
            "calculated_columns": 0,
            "relationships_written": 17,
            "relationships_skipped": [
                {
                    "relationship": "Trips.driver_id -> DriverPerformance.driver_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Trips.truck_id -> Maintenance.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Trips.truck_id -> TruckPerformance.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Trips.truck_id -> MaintenanceByTruck.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Maintenance.truck_id -> TruckPerformance.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Maintenance.truck_id -> MaintenanceByTruck.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "TruckPerformance.truck_id -> MaintenanceByTruck.truck_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelPurchases.trip_id -> DeliveryEvents.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelPurchases.trip_id -> SafetyIncidents.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelPurchases.trip_id -> FuelByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelPurchases.trip_id -> DeliveryByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelPurchases.trip_id -> SafetyByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "DeliveryEvents.trip_id -> SafetyIncidents.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "DeliveryEvents.trip_id -> FuelByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "DeliveryEvents.trip_id -> DeliveryByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "DeliveryEvents.trip_id -> SafetyByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "SafetyIncidents.trip_id -> FuelByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "SafetyIncidents.trip_id -> DeliveryByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "SafetyIncidents.trip_id -> SafetyByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelByTrip.trip_id -> DeliveryByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "FuelByTrip.trip_id -> SafetyByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "DeliveryByTrip.trip_id -> SafetyByTrip.trip_id",
                    "reason": "synthetic peer-to-peer fact relationship omitted in star schema to prevent duplicate key errors"
                },
                {
                    "relationship": "Trips.DispatchDate -> Calendar.DispatchDate",
                    "reason": "relationship endpoint is not a key column"
                }
            ],
            "orphan_measures_table": false,
            "shared_expressions": [
                "FleetVisionRedshift"
            ],
            "dax_needs_rewrite": 0,
            "dax_problems": []
        },
        "report": {
            "pages": 3,
            "visuals": 49,
            "native": 48,
            "substituted": 1,
            "manual": 0,
            "filters_applied": 0,
            "top_n_filters": 0,
            "categorical_filters": 0,
            "bookmarks": 3,
            "navigation_buttons": 3
        }
    },
    "visual_notes": [
        {
            "object_id": null,
            "sheet": "Fleet Operations",
            "title": "Idle Time Analysis",
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
        "commit": "08467c0c546d28ee0373d6b724921516fa39a1a3",
        "path": "fleetvision-ksa",
        "file_count": 100
    },
    "total_bytes": 196399,
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
                        "path": "FleetVision KSA.Report"
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
                    "displayName": "FleetVision KSA"
                },
                "config": {
                    "version": "2.0",
                    "logicalId": "ed16d0fb-208d-5b8f-97d5-5c2393c51ccb"
                }
            },
            "definition.pbism": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
                "version": "4.0",
                "settings": {}
            },
            "definition/cultures/en-US.tmdl": "cultureInfo en-US\n\tlinguisticMetadata =\n\t\t\t{\n\t\t\t  \"Version\": \"1.0.0\",\n\t\t\t  \"Language\": \"en-US\"\n\t\t\t}\n\t\tcontentType: json\n",
            "definition/database.tmdl": "database\n\tcompatibilityLevel: 1567\n",
            "definition/expressions.tmdl": "expression FleetVisionRedshift =\n\t\tlet\n\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")\n\t\tin\n\t\t    Source\n\tlineageTag: a127a1ae-58df-5e94-8b3c-f5853b9e3f44\n\n\tannotation PBI_NavigationStepName = Navigation\n\n\tannotation PBI_ResultType = Table\n",
            "definition/model.tmdl": "model Model\n\tculture: en-US\n\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\tdiscourageImplicitMeasures\n\tsourceQueryCulture: en-US\n\n\tannotation PBI_QueryOrder = [\"Trips\", \"Drivers\", \"DriverPerformance\", \"Trucks\", \"Maintenance\", \"TruckPerformance\", \"MaintenanceByTruck\", \"Trailers\", \"Customers\", \"Loads\", \"Facilities\", \"DeliveryEvents\", \"Routes\", \"FuelPurchases\", \"SafetyIncidents\", \"FuelByTrip\", \"DeliveryByTrip\", \"SafetyByTrip\", \"Calendar\", \"TruckMap\", \"TempCalendar\", \"Parameters\"]\n\tannotation PBI_ProTooling = [\"DevMode\"]\n\nref table Trips\nref table Drivers\nref table DriverPerformance\nref table Trucks\nref table Maintenance\nref table TruckPerformance\nref table MaintenanceByTruck\nref table Trailers\nref table Customers\nref table Loads\nref table Facilities\nref table DeliveryEvents\nref table Routes\nref table FuelPurchases\nref table SafetyIncidents\nref table FuelByTrip\nref table DeliveryByTrip\nref table SafetyByTrip\nref table Calendar\nref table TruckMap\nref table TempCalendar\nref table Parameters\n\nref cultureInfo en-US\n",
            "definition/relationships.tmdl": "relationship e4431242-a315-54fb-8d0f-4ca40ea1d8ac\n\tfromColumn: Trips.driver_id\n\ttoColumn: Drivers.driver_id\n\nrelationship e94bd60a-ba44-5e9d-9d9d-54e8e7fc72b8\n\tfromColumn: DriverPerformance.driver_id\n\ttoColumn: Drivers.driver_id\n\nrelationship c966bdbd-33b5-5391-8722-ab301da110ec\n\tfromColumn: Trips.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 3382a17c-41ec-58c0-9dc6-268e467b37ec\n\tfromColumn: Maintenance.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 090fed02-c19b-52dc-9a2f-9e7bb6424ff5\n\tfromColumn: TruckPerformance.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 00760774-0afa-5dc5-a227-3bec5e31b530\n\tfromColumn: MaintenanceByTruck.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 5af54763-ad58-5311-a102-731b876e0079\n\tfromColumn: Trips.trailer_id\n\ttoColumn: Trailers.trailer_id\n\nrelationship 758ef9e8-e22c-5c9a-a54b-f70629f369e3\n\tfromColumn: Trips.load_id\n\ttoColumn: Loads.load_id\n\nrelationship 008548d9-a777-5478-b6d2-ccc87322420a\n\tfromColumn: FuelPurchases.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship e2834fc3-650f-5d8b-b9b1-f3f8d0db0e41\n\tfromColumn: DeliveryEvents.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 95107944-0045-5bb1-920d-6c5a4a130564\n\tfromColumn: SafetyIncidents.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 3aba2506-7628-5e52-849b-53b3d55d34b7\n\tfromColumn: FuelByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship e6821b6d-3dab-5538-8c33-f599f6ccb3be\n\tfromColumn: DeliveryByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship a00d5fe6-2cc6-50c3-910e-8561f1cfaabc\n\tfromColumn: SafetyByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 2e86c837-0b84-5365-b1a1-921439cab523\n\tfromColumn: Loads.customer_id\n\ttoColumn: Customers.customer_id\n\nrelationship 866b89a5-0870-5faa-99c7-883cccfb3e58\n\tfromColumn: Loads.route_id\n\ttoColumn: Routes.route_id\n\nrelationship 9686f357-f377-5b44-a1b0-7499c90273e8\n\tfromColumn: DeliveryEvents.facility_id\n\ttoColumn: Facilities.facility_id\n",
            "definition/tables/Calendar.tmdl": "table Calendar\n\tlineageTag: 3e8768d4-2c5d-519b-a88b-9a72ddeafd79\n\n\tcolumn DispatchDate\n\t\tdataType: dateTime\n\t\tlineageTag: 384a1023-b3ac-5475-83c0-2919eaba147c\n\t\tsummarizeBy: none\n\t\tsourceColumn: DispatchDate\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarYear\n\t\tdataType: int64\n\t\tlineageTag: d6ee7cf6-bb79-55e2-83a1-4d5300e381b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarYear\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarQuarter\n\t\tdataType: string\n\t\tlineageTag: e7b59f15-82da-5553-b2f6-cc80d8adcba1\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarQuarter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonth\n\t\tdataType: double\n\t\tlineageTag: 35c59a6b-12fe-5d37-ae03-8cedef6fcd9f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarMonth\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonthYear\n\t\tdataType: int64\n\t\tlineageTag: c0e70147-64b5-5bfe-88b2-ec25cc1e77cd\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarMonthYear\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonthStart\n\t\tdataType: dateTime\n\t\tlineageTag: 8a16538b-80e4-5cb1-b3bb-6694129064f0\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarMonthStart\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarWeek\n\t\tdataType: double\n\t\tlineageTag: 36aeaadc-3b48-53be-82c6-e7c49d844dbc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarWeek\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarWeekDay\n\t\tdataType: double\n\t\tlineageTag: 3bd941a2-d151-5d89-a65e-b934854a9f33\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarWeekDay\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarDay\n\t\tdataType: double\n\t\tlineageTag: f4dfdae1-326c-5b35-930f-9fbf11c50547\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarDay\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Calendar = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    StartDate = #date(2020, 1, 1),\n\t\t\t\t    EndDate = #date(2026, 12, 31),\n\t\t\t\t    NumberOfDays = Duration.Days(EndDate - StartDate) + 1,\n\t\t\t\t    DateList = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0)),\n\t\t\t\t    #\"Converted to Table\" = Table.FromList(DateList, Splitter.SplitByNothing(), {\"DispatchDate\"}, null, ExtraValues.Error),\n\t\t\t\t    #\"Changed Type\" = Table.TransformColumnTypes(#\"Converted to Table\", {{\"DispatchDate\", type date}}),\n\t\t\t\t    #\"Added CalendarYear\" = Table.AddColumn(#\"Changed Type\", \"CalendarYear\", each Date.Year([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarQuarter\" = Table.AddColumn(#\"Added CalendarYear\", \"CalendarQuarter\", each \"Q\" & Text.From(Date.QuarterOfYear([DispatchDate])), type text),\n\t\t\t\t    #\"Added CalendarMonth\" = Table.AddColumn(#\"Added CalendarQuarter\", \"CalendarMonth\", each Date.Month([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarMonthYear\" = Table.AddColumn(#\"Added CalendarMonth\", \"CalendarMonthYear\", each Date.ToText([DispatchDate], \"MMM yyyy\"), type text),\n\t\t\t\t    #\"Added CalendarMonthStart\" = Table.AddColumn(#\"Added CalendarMonthYear\", \"CalendarMonthStart\", each Date.StartOfMonth([DispatchDate]), type date),\n\t\t\t\t    #\"Added CalendarWeek\" = Table.AddColumn(#\"Added CalendarMonthStart\", \"CalendarWeek\", each Date.WeekOfYear([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarWeekDay\" = Table.AddColumn(#\"Added CalendarWeek\", \"CalendarWeekDay\", each Date.DayOfWeekName([DispatchDate]), type text),\n\t\t\t\t    #\"Added CalendarDay\" = Table.AddColumn(#\"Added CalendarWeekDay\", \"CalendarDay\", each Date.Day([DispatchDate]), Int64.Type)\n\t\t\t\tin\n\t\t\t\t    #\"Added CalendarDay\"\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Customers.tmdl": "table Customers\n\tlineageTag: 38a9d5ed-6ca7-5ecb-8256-fc65bb46a03e\n\n\tmeasure 'Total Customers' = DISTINCTCOUNT('Customers'[customer_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 0902181d-1af0-50ef-8642-3b06b993e9f3\n\n\tcolumn customer_id\n\t\tdataType: string\n\t\tlineageTag: 3fb9a87c-1881-581d-a4ca-aa8d50ffbc83\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn customer_name\n\t\tdataType: string\n\t\tlineageTag: 710a38c7-6aa4-56b8-962c-c9b538f8b4a8\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn customer_type\n\t\tdataType: string\n\t\tlineageTag: e3f78ab5-00b6-5059-91c8-bcd16616c466\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn credit_terms_days\n\t\tdataType: double\n\t\tlineageTag: 6539a2f5-9455-5a2d-ae3f-1371438ee7af\n\t\tsummarizeBy: sum\n\t\tsourceColumn: credit_terms_days\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn primary_freight_type\n\t\tdataType: string\n\t\tlineageTag: 50ec5661-1be8-5744-8901-5e6496adca60\n\t\tsummarizeBy: none\n\t\tsourceColumn: primary_freight_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn account_status\n\t\tdataType: string\n\t\tlineageTag: 6c0a054a-3b09-59a4-bbb5-67aa33132010\n\t\tsummarizeBy: none\n\t\tsourceColumn: account_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn contract_start_date\n\t\tdataType: dateTime\n\t\tlineageTag: 6339cc9c-bb4e-5d95-9051-8df23c70e46a\n\t\tsummarizeBy: none\n\t\tsourceColumn: contract_start_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn annual_revenue_potential\n\t\tdataType: double\n\t\tlineageTag: 3c2ae234-c1c7-5e20-b644-1e03f1081517\n\t\tsummarizeBy: sum\n\t\tsourceColumn: annual_revenue_potential\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Customers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.customers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/DeliveryByTrip.tmdl": "table DeliveryByTrip\n\tlineageTag: 8467d34e-5c38-5c04-9b84-ada65dd67f05\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 1e9201d6-2ceb-5873-a19b-afc1d95b073c\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DeliveryEvents\n\t\tdataType: double\n\t\tlineageTag: 4ebf74f8-5423-54d5-9f39-cf91934e2320\n\t\tsummarizeBy: sum\n\t\tsourceColumn: DeliveryEvents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn OnTimeEvents = SWITCH(TRUE(), 'DeliveryByTrip'[on_time_flag], 1, 0)\n\t\tdataType: dateTime\n\t\tlineageTag: 16d2e960-c7b1-52e4-8527-0f11324b83c8\n\t\tsummarizeBy: none\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn LateEvents = SWITCH(TRUE(), 'DeliveryByTrip'[on_time_flag] = 0, 1, 0)\n\t\tdataType: double\n\t\tlineageTag: 5937a09b-82a4-54a7-b867-3512f025af6c\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn OnTimeRate = SWITCH(TRUE(), Count(DISTINCT 'DeliveryByTrip'[event_id]) > 0, Sum( If('DeliveryByTrip'[on_time_flag], 1, 0) ) / Count(DISTINCT event_id), 0)\n\t\tdataType: dateTime\n\t\tlineageTag: 8d7d28f8-bd6a-5b80-8e42-f59315501f58\n\t\tsummarizeBy: none\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalDetentionMinutes\n\t\tdataType: double\n\t\tlineageTag: 1b4d5f37-0adc-57cb-9131-bb3ebc44bf13\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalDetentionMinutes\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgDetentionMinutes\n\t\tdataType: double\n\t\tlineageTag: 3d3520f3-6ef4-5a73-9da7-884aa1bf0766\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgDetentionMinutes\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DeliveryByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = DeliveryEvents\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/DeliveryEvents.tmdl": "table DeliveryEvents\n\tlineageTag: a31b3de9-e3b3-5759-a0dd-2e97dd0eea8d\n\n\tmeasure 'On-Time Delivery %' = AVERAGE('DeliveryEvents'[on_time_flag])*100\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: fae51d1f-d8f9-5b55-99bd-a56967d5ec3d\n\n\tcolumn facility_id\n\t\tdataType: string\n\t\tlineageTag: 1d72730f-a012-591b-8eb9-423a7a53ec20\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: d01822dc-9b8a-5903-8c08-2e3235029ac6\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn event_id\n\t\tdataType: string\n\t\tlineageTag: 4bdc4e52-91af-552c-b08b-32bc059e3ad9\n\t\tsummarizeBy: none\n\t\tsourceColumn: event_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn event_type\n\t\tdataType: string\n\t\tlineageTag: 13085807-aaca-5f23-81cc-04f6447e7fe9\n\t\tsummarizeBy: none\n\t\tsourceColumn: event_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn scheduled_datetime\n\t\tdataType: dateTime\n\t\tlineageTag: 482c832f-a235-54f9-ac1b-009a261720a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: scheduled_datetime\n\t\tformatString: M/D/YYYY h:mm:ss[.fff] TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_datetime\n\t\tdataType: dateTime\n\t\tlineageTag: 03590705-13b4-5dc6-885d-a1f5ae637966\n\t\tsummarizeBy: none\n\t\tsourceColumn: actual_datetime\n\t\tformatString: M/D/YYYY h:mm:ss[.fff] TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn detention_minutes\n\t\tdataType: double\n\t\tlineageTag: e0ae6536-e685-504f-a3f5-6e7ae6717b9c\n\t\tsummarizeBy: sum\n\t\tsourceColumn: detention_minutes\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn on_time_flag\n\t\tdataType: string\n\t\tlineageTag: d3ca52eb-7d52-53f4-ad16-70b945ca2e19\n\t\tsummarizeBy: none\n\t\tsourceColumn: on_time_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn delivery_city\n\t\tdataType: string\n\t\tlineageTag: 4389c613-2b52-5490-81af-c783dd41d716\n\t\tsummarizeBy: none\n\t\tsourceColumn: delivery_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn delivery_state\n\t\tdataType: string\n\t\tlineageTag: ced951d9-a000-5e41-b483-647362840126\n\t\tsummarizeBy: none\n\t\tsourceColumn: delivery_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DeliveryEvents = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    event_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    event_type,\n\t\t\t\t    facility_id,\n\t\t\t\t    scheduled_datetime,\n\t\t\t\t    actual_datetime,\n\t\t\t\t    detention_minutes,\n\t\t\t\t    on_time_flag,\n\t\t\t\t    location_city     AS delivery_city,\n\t\t\t\t    location_state    AS delivery_state\n\t\t\t\t    FROM fleetvision.delivery_events\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/DriverPerformance.tmdl": "table DriverPerformance\n\tlineageTag: 45e4a570-977d-56a3-ba43-7e841ee0690b\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: 423ac404-8093-56ae-a1ae-3fd51b27ce71\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalTrips\n\t\tdataType: double\n\t\tlineageTag: 71074d0a-12be-5155-a402-d5c8f7494d29\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalTrips\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalMiles\n\t\tdataType: double\n\t\tlineageTag: ee2aca6e-5705-5d9f-b343-dfaec87438e1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalMiles\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalTripHours\n\t\tdataType: double\n\t\tlineageTag: d02e9eb5-9a8d-5eb1-9a1f-a41656414bda\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalTripHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalFuelGallons\n\t\tdataType: double\n\t\tlineageTag: 98b2f4a1-e0d8-5320-a2f7-3c5b586a27fc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalFuelGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FleetMPG\n\t\tdataType: double\n\t\tlineageTag: 4f766b95-c033-58ce-8574-cc99405efda3\n\t\tsummarizeBy: sum\n\t\tsourceColumn: FleetMPG\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgMPG\n\t\tdataType: double\n\t\tlineageTag: ca74523b-4db1-58fe-b4d1-6b4c09a65ad2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgMPG\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgIdleHours\n\t\tdataType: double\n\t\tlineageTag: dcdc5388-82cd-5894-9609-a100115039eb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgIdleHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalIdleHours\n\t\tdataType: double\n\t\tlineageTag: 1f7a1ac1-fdd6-5452-8b8f-1910ce867802\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalIdleHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DriverPerformance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trips\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Drivers.tmdl": "table Drivers\n\tlineageTag: b5a283ed-c128-51a0-8b2d-9cee846a3a5d\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: ff7ba233-3d4c-5538-ad67-86e8724f0ce9\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn first_name\n\t\tdataType: string\n\t\tlineageTag: 59e4ef1d-b004-59f4-8272-6058164eab60\n\t\tsummarizeBy: none\n\t\tsourceColumn: first_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn last_name\n\t\tdataType: string\n\t\tlineageTag: e9e84dd3-793c-52e1-8f4b-467e8774d911\n\t\tsummarizeBy: none\n\t\tsourceColumn: last_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn hire_date\n\t\tdataType: dateTime\n\t\tlineageTag: d3648a12-76b2-52f7-8a41-36102663f4b3\n\t\tsummarizeBy: none\n\t\tsourceColumn: hire_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn termination_date\n\t\tdataType: dateTime\n\t\tlineageTag: 1e242dce-d9ef-5a26-b670-d45337a4331d\n\t\tsummarizeBy: none\n\t\tsourceColumn: termination_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn license_number\n\t\tdataType: string\n\t\tlineageTag: c766caed-61a2-5537-aad0-3324fc8fc2d9\n\t\tsummarizeBy: none\n\t\tsourceColumn: license_number\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn license_state\n\t\tdataType: string\n\t\tlineageTag: a7311415-3759-506e-bdb6-f06a089ca0a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: license_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn date_of_birth\n\t\tdataType: dateTime\n\t\tlineageTag: 993f311d-1e16-576c-b412-e72821e2feda\n\t\tsummarizeBy: none\n\t\tsourceColumn: date_of_birth\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn home_terminal\n\t\tdataType: string\n\t\tlineageTag: 68634f9f-e5ae-586b-b168-1bb3cc4a147a\n\t\tsummarizeBy: none\n\t\tsourceColumn: home_terminal\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn employment_status\n\t\tdataType: string\n\t\tlineageTag: 87c433b3-8796-59a7-9447-09400ef28c74\n\t\tsummarizeBy: none\n\t\tsourceColumn: employment_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn cdl_class\n\t\tdataType: string\n\t\tlineageTag: 7afe4b3f-44b7-57e5-80a0-c67edc7827f2\n\t\tsummarizeBy: none\n\t\tsourceColumn: cdl_class\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn years_experience\n\t\tdataType: double\n\t\tlineageTag: 85797267-21b3-574a-a017-c3c943dbf581\n\t\tsummarizeBy: sum\n\t\tsourceColumn: years_experience\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Drivers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    driver_id,\n\t\t\t\t    first_name,\n\t\t\t\t    last_name,\n\t\t\t\t    hire_date,\n\t\t\t\t    termination_date,\n\t\t\t\t    license_number,\n\t\t\t\t    license_state,\n\t\t\t\t    date_of_birth,\n\t\t\t\t    home_terminal,\n\t\t\t\t    employment_status,\n\t\t\t\t    cdl_class,\n\t\t\t\t    years_experience\n\t\t\t\t    FROM fleetvision.drivers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Facilities.tmdl": "table Facilities\n\tlineageTag: eca24c6c-83b3-5419-a289-29e6960295aa\n\n\tcolumn facility_id\n\t\tdataType: string\n\t\tlineageTag: c700d0aa-3c5c-5b30-8f4e-c99a9a385da1\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_name\n\t\tdataType: string\n\t\tlineageTag: 356ad5c7-1cd3-5977-b34e-824fd53af81f\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_type\n\t\tdataType: string\n\t\tlineageTag: 3eca9b5c-5eac-58f4-9f2c-d16582ab3dd7\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn city\n\t\tdataType: string\n\t\tlineageTag: d71be1f5-b0f6-51f2-8f7b-a549cc2ab774\n\t\tsummarizeBy: none\n\t\tsourceColumn: city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn state\n\t\tdataType: string\n\t\tlineageTag: c0842320-6428-5c14-ae71-462eb7b1b698\n\t\tsummarizeBy: none\n\t\tsourceColumn: state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn latitude\n\t\tdataType: double\n\t\tlineageTag: 10ba13ce-58c1-5dd0-ad5a-863e782c5f21\n\t\tsummarizeBy: sum\n\t\tsourceColumn: latitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn longitude\n\t\tdataType: double\n\t\tlineageTag: 6f624232-1bfb-57e6-bb68-5688203ca06f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: longitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn dock_doors\n\t\tdataType: double\n\t\tlineageTag: cb2ce4bf-cdd3-5827-a116-649c76c6b9e7\n\t\tsummarizeBy: sum\n\t\tsourceColumn: dock_doors\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn operating_hours\n\t\tdataType: string\n\t\tlineageTag: 085355eb-63c6-56ba-a29d-e0bcf0dcdf27\n\t\tsummarizeBy: none\n\t\tsourceColumn: operating_hours\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn longitude_latitude\n\t\tdataType: string\n\t\tlineageTag: 3168d3a5-b189-536e-b479-e1c824a26724\n\t\tsummarizeBy: none\n\t\tsourceColumn: longitude_latitude\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Facilities = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.facilities\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/FuelByTrip.tmdl": "table FuelByTrip\n\tlineageTag: 92a3a65c-e644-527c-9742-7e68c00ed86a\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 727e8482-c80b-53b1-8673-26c365074440\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn PurchasedGallons\n\t\tdataType: double\n\t\tlineageTag: 1324fdf1-26e7-5e3c-a8f4-ca515e388028\n\t\tsummarizeBy: sum\n\t\tsourceColumn: PurchasedGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalFuelCost\n\t\tdataType: double\n\t\tlineageTag: 8125f77c-fd8f-5fd0-b14b-192a0bd182e4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalFuelCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgFuelPricePerGallon\n\t\tdataType: double\n\t\tlineageTag: 19375e2e-a18e-5c24-9538-f5e5a73f7c1e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgFuelPricePerGallon\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FuelTransactions\n\t\tdataType: double\n\t\tlineageTag: 67fec475-d41c-5346-8f5a-70764ccfc656\n\t\tsummarizeBy: sum\n\t\tsourceColumn: FuelTransactions\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition FuelByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = FuelPurchases\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/FuelPurchases.tmdl": "table FuelPurchases\n\tlineageTag: 6c3a21d2-b0ad-5e6a-94f0-aac32a8bf75c\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 3597cd69-ad08-56e1-a904-b02ab6b9f14a\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_purchase_id\n\t\tdataType: string\n\t\tlineageTag: 8c848f98-012f-55a8-a40f-669e3a6eddf8\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_purchase_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn purchase_date\n\t\tdataType: dateTime\n\t\tlineageTag: 86b98a74-c808-58e0-b7b2-ea8b715eac1b\n\t\tsummarizeBy: none\n\t\tsourceColumn: purchase_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_city\n\t\tdataType: string\n\t\tlineageTag: 5062cd58-fc08-5929-96f4-5d507e73d51d\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_state\n\t\tdataType: string\n\t\tlineageTag: 1ee79352-50e2-5aa3-81d0-26ae2b94df18\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn gallons\n\t\tdataType: double\n\t\tlineageTag: 093543c3-cc92-5ed8-9c34-51b52ceb0367\n\t\tsummarizeBy: sum\n\t\tsourceColumn: gallons\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn price_per_gallon\n\t\tdataType: double\n\t\tlineageTag: 44016af0-05fd-56a4-b01b-e9526d6ad4fb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: price_per_gallon\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_total_cost\n\t\tdataType: double\n\t\tlineageTag: b42d4880-553f-5dd1-9ba8-6876d0b1730e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_total_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_card_number\n\t\tdataType: string\n\t\tlineageTag: 2fb4b2c9-14b3-50b7-acd0-84a39588d6ea\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_card_number\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition FuelPurchases = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    fuel_purchase_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    purchase_date,\n\t\t\t\t    location_city     AS fuel_city,\n\t\t\t\t    location_state    AS fuel_state,\n\t\t\t\t    gallons,\n\t\t\t\t    price_per_gallon,\n\t\t\t\t    total_cost        AS fuel_total_cost,\n\t\t\t\t    fuel_card_number\n\t\t\t\t    FROM fleetvision.fuel_purchases\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Loads.tmdl": "table Loads\n\tlineageTag: 13e30a87-fa1f-5fb1-a4d4-f18fb28b9558\n\n\tmeasure 'Total Revenue' = DIVIDE(SUM('Loads'[revenue]), 1000000, 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 91098b09-6315-5012-8cb4-76e719439999\n\n\tmeasure 'Customer Analytics' = MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5a444008-2977-58aa-8afd-9a301f70d1f2\n\n\tmeasure 'Highest Revenue by Customer' = MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 1b63a406-2922-5cb0-9dcf-d471af1453d0\n\n\tmeasure 'Average Revenue per Load' = AVERAGE('Loads'[revenue])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: ec7cf70c-2291-5cbb-9d68-2b9728cb6e1a\n\n\tmeasure 'High Value Revenue' = CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 9e0aa5db-e86e-5f58-b721-d6dbdd9858ce\n\n\tmeasure 'Average Revenue per Customer' = DIVIDE(SUM('Loads'[revenue]), DISTINCTCOUNT('Customers'[customer_id]), 0)\n\t\tformatString: \"$#,##0\"\n\t\tlineageTag: 290c931b-09a5-5f54-b1d3-6d67170e6f7f\n\n\tmeasure 'Driver Analytics' = AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e05a035d-85ce-5856-a036-1afbc7f0beb3\n\n\tmeasure 'High Value Revenue %' = DIVIDE(CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\"), SUM('Loads'[revenue]), 0)\n\t\tformatString: \"0.0%\"\n\t\tlineageTag: d15eab55-18f2-558a-b3d8-3f6bde57dfa6\n\n\tmeasure 'Revenue per Mile' = DIVIDE(SUM('Loads'[revenue]), SUM('Trips'[actual_distance_miles]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 6a7f8c9d-ae59-5350-b000-d2098e25e5dd\n\n\tmeasure 'Revenue per Trip' = DIVIDE(SUM('Loads'[revenue]), COUNT('Trips'[trip_id]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: be478467-bb36-5135-92b2-1280a432b523\n\n\tmeasure 'Average Revenue per Driver' = AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: b48816ec-1244-5c22-ae05-174fd572bc6d\n\n\tmeasure 'High Value Loads' = CALCULATE(DISTINCTCOUNT('Trips'[load_id]), 'Loads'[RevenueBand] = \"High Value\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 941ed71d-c9cd-5bf8-9c14-71585bf98f31\n\n\tmeasure 'Revenue %' = DIVIDE(SUM('Loads'[revenue]), CALCULATE(SUM('Loads'[revenue]), ALLSELECTED()), 0)\n\t\tformatString: \"0.0%\"\n\t\tlineageTag: f72e061a-527b-5da5-a953-892acb27092f\n\n\tmeasure 'Total Loads' = COUNT('Trips'[load_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: dc568f16-f764-5701-bf95-6f1a21fe4d5b\n\n\tcolumn customer_id\n\t\tdataType: string\n\t\tlineageTag: f9aee854-a44e-583e-911e-b0a3c8d6d728\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn route_id\n\t\tdataType: string\n\t\tlineageTag: fac49772-56f1-52a7-8521-e03aecf65481\n\t\tsummarizeBy: none\n\t\tsourceColumn: route_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_id\n\t\tdataType: string\n\t\tlineageTag: d5e9dbe9-70ec-549f-93d4-88c964aeb994\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_date\n\t\tdataType: dateTime\n\t\tlineageTag: d015f215-d74d-5b4c-b75a-6f60e9adb897\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_type\n\t\tdataType: string\n\t\tlineageTag: cec011a4-0571-5301-8667-00e470144aa6\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn weight_lbs\n\t\tdataType: double\n\t\tlineageTag: d4d0b472-c8a2-5abf-973c-08da760a4765\n\t\tsummarizeBy: sum\n\t\tsourceColumn: weight_lbs\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn pieces\n\t\tdataType: double\n\t\tlineageTag: 115c40fc-1695-5395-b1b3-cdcc5666e45a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: pieces\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn revenue\n\t\tdataType: double\n\t\tlineageTag: 1a41650e-0a8c-5cf9-af7f-beec7d3c1c04\n\t\tsummarizeBy: sum\n\t\tsourceColumn: revenue\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_surcharge\n\t\tdataType: double\n\t\tlineageTag: e2f4d3bd-bea8-5a0e-a66d-66cd37ffbacc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_surcharge\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn accessorial_charges\n\t\tdataType: double\n\t\tlineageTag: e3933416-af83-51f9-b7e5-298adeabebbe\n\t\tsummarizeBy: sum\n\t\tsourceColumn: accessorial_charges\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_status\n\t\tdataType: string\n\t\tlineageTag: 53352867-8cc2-5877-a19e-b8709cc9ca7a\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn booking_type\n\t\tdataType: string\n\t\tlineageTag: d9ae0f6b-f9f8-5906-9d00-94110a53d571\n\t\tsummarizeBy: none\n\t\tsourceColumn: booking_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn RevenueBand = SWITCH(TRUE(), 'Loads'[revenue] >= 6000, \"High Value\", 'Loads'[revenue] >= 3000, \"Medium Value\", \"Low Value\")\n\t\tdataType: string\n\t\tlineageTag: 543f6047-0955-5329-ac40-4210c3bc9133\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Loads = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"customer_id\", \"route_id\", \"load_id\", \"load_date\", \"load_type\", \"weight_lbs\", \"pieces\", \"revenue\", \"fuel_surcharge\", \"accessorial_charges\", \"load_status\", \"booking_type\", \"RevenueBand\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/Maintenance.tmdl": "table Maintenance\n\tlineageTag: c75bd5d7-e55c-54a1-989f-8feb4433992f\n\n\tmeasure 'Total Maintainane Cost' = SUM('Maintenance'[maintenance_total_cost])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 77f41ac7-0c8c-5611-814a-bcf9899d6369\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 32ec1da0-6836-5507-b254-e5039c74718e\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_id\n\t\tdataType: string\n\t\tlineageTag: ce9ec557-f02e-54e9-bfaf-1e2f665df756\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_date\n\t\tdataType: dateTime\n\t\tlineageTag: 6a4d1d20-7f1f-5992-a2a9-c9769c0a942a\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_type\n\t\tdataType: string\n\t\tlineageTag: 847e0af4-af79-5c6f-9e03-017e18101046\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn odometer_reading\n\t\tdataType: double\n\t\tlineageTag: 038241d8-57a1-5fe4-8963-c17fba582206\n\t\tsummarizeBy: sum\n\t\tsourceColumn: odometer_reading\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn labor_hours\n\t\tdataType: double\n\t\tlineageTag: 962b58e9-c61c-5310-ab3f-312ac4120d0d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: labor_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn labor_cost\n\t\tdataType: double\n\t\tlineageTag: fc70b322-2558-511b-a173-73a365cdf9c6\n\t\tsummarizeBy: sum\n\t\tsourceColumn: labor_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn parts_cost\n\t\tdataType: double\n\t\tlineageTag: b6fdd733-557f-56d7-b740-904ce21870a2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: parts_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_total_cost\n\t\tdataType: double\n\t\tlineageTag: 924a75f8-0942-59ef-8e8f-782e29a6ab05\n\t\tsummarizeBy: sum\n\t\tsourceColumn: maintenance_total_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_location\n\t\tdataType: string\n\t\tlineageTag: 645ee12b-a4ff-5335-bb8d-6e5e0efb828e\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_location\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn downtime_hours\n\t\tdataType: double\n\t\tlineageTag: a62f3bf5-3362-592f-998e-62deeb89abe1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: downtime_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn service_description\n\t\tdataType: string\n\t\tlineageTag: 8dd9cbf6-f21f-51c4-a5bf-899956e18384\n\t\tsummarizeBy: none\n\t\tsourceColumn: service_description\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Maintenance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    maintenance_id,\n\t\t\t\t    truck_id,\n\t\t\t\t    maintenance_date,\n\t\t\t\t    maintenance_type,\n\t\t\t\t    odometer_reading,\n\t\t\t\t    labor_hours,\n\t\t\t\t    labor_cost,\n\t\t\t\t    parts_cost,\n\t\t\t\t    total_cost        AS maintenance_total_cost,\n\t\t\t\t    facility_location,\n\t\t\t\t    downtime_hours,\n\t\t\t\t    service_description\n\t\t\t\t    FROM fleetvision.maintenance_records\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/MaintenanceByTruck.tmdl": "table MaintenanceByTruck\n\tlineageTag: b25cf30f-944f-5acb-867f-2865adb4cad0\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 10c23d76-c733-59e6-8256-977e303922c3\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MaintenanceEvents\n\t\tdataType: double\n\t\tlineageTag: 777b6bbb-c10c-5996-bca2-26c6b54ac5a8\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MaintenanceEvents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalMaintenanceCost\n\t\tdataType: double\n\t\tlineageTag: abd1a5e4-802f-5767-8c38-e97a37b62b1c\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalMaintenanceCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalDowntimeHours\n\t\tdataType: dateTime\n\t\tlineageTag: c5e3d8d6-68a4-55da-896d-bf5411232e9a\n\t\tsummarizeBy: none\n\t\tsourceColumn: TotalDowntimeHours\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgDowntimeHours\n\t\tdataType: double\n\t\tlineageTag: c2847ac1-7ea9-5e8d-bf20-574fac218614\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgDowntimeHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalLaborCost\n\t\tdataType: double\n\t\tlineageTag: c3c4b815-fafb-550f-9320-6d6239736fbe\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalLaborCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalPartsCost\n\t\tdataType: double\n\t\tlineageTag: 11c3f4d4-e75c-5175-8e97-28332ad62a7e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalPartsCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgLaborHours\n\t\tdataType: double\n\t\tlineageTag: 19e11044-a6f7-51b4-8034-5d6237d7da7d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgLaborHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition MaintenanceByTruck = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Maintenance\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Parameters.tmdl": "table Parameters\n\tlineageTag: 0fe49ea5-fe5c-5a45-9ff7-e50b75dc067a\n\n\tcolumn Parameter\n\t\tdataType: string\n\t\tlineageTag: 22a0bd0b-9463-5b42-9a2d-5cfbd1cf63df\n\t\tsummarizeBy: none\n\t\tsourceColumn: Parameter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Value\n\t\tdataType: string\n\t\tlineageTag: 70b4627b-915e-51c1-9f8a-945f135294b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: Value\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Label\n\t\tdataType: string\n\t\tlineageTag: 5946bfca-d13d-5640-80d8-f86e9e9334a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: Label\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Order\n\t\tdataType: int64\n\t\tlineageTag: 3a397789-8015-5220-bf8f-5696fa2e68c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: Order\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Parameters = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table(\n\t\t\t\t        type table [Parameter = text, Value = text, Label = text, #\"Order\" = Int64.Type],\n\t\t\t\t        {\n\t\t\t            {\"MoneyThousandSep\", \",\", \"MoneyThousandSep\", 1},\n\t\t\t            {\"ThousandSep\", \",\", \"ThousandSep\", 2},\n\t\t\t            {\"MoneyFormat\", \"$ ###0.00;-$ ###0.00\", \"MoneyFormat\", 3},\n\t\t\t            {\"TimeFormat\", \"h:mm:ss TT\", \"TimeFormat\", 4},\n\t\t\t            {\"BrokenWeeks\", \"1\", \"BrokenWeeks\", 5},\n\t\t\t            {\"CreateSearchIndexOnReload\", \"1\", \"CreateSearchIndexOnReload\", 6},\n\t\t\t            {\"MonthNames\", \"Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec\", \"MonthNames\", 7},\n\t\t\t            {\"LongDayNames\", \"Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday\", \"LongDayNames\", 8},\n\t\t\t            {\"ScriptErrorCount\", \"0\", \"ScriptErrorCount\", 9},\n\t\t\t            {\"DateFormat\", \"M/D/YYYY\", \"DateFormat\", 10},\n\t\t\t            {\"ReferenceDay\", \"0\", \"ReferenceDay\", 11},\n\t\t\t            {\"FirstMonthOfYear\", \"1\", \"FirstMonthOfYear\", 12},\n\t\t\t            {\"ErrorMode\", \"1\", \"ErrorMode\", 13},\n\t\t\t            {\"StripComments\", \"1\", \"StripComments\", 14},\n\t\t\t            {\"OpenUrlTimeout\", \"86400\", \"OpenUrlTimeout\", 15},\n\t\t\t            {\"DecimalSep\", \".\", \"DecimalSep\", 16},\n\t\t\t            {\"TimestampFormat\", \"M/D/YYYY h:mm:ss[.fff] TT\", \"TimestampFormat\", 17},\n\t\t\t            {\"FirstWeekDay\", \"6\", \"FirstWeekDay\", 18},\n\t\t\t            {\"CollationLocale\", \"en-US\", \"CollationLocale\", 19},\n\t\t\t            {\"LongMonthNames\", \"January;February;March;April;May;June;July;August;September;October;November;December\", \"LongMonthNames\", 20},\n\t\t\t            {\"DayNames\", \"Mon;Tue;Wed;Thu;Fri;Sat;Sun\", \"DayNames\", 21},\n\t\t\t            {\"NumericalAbbreviation\", \"3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y\", \"NumericalAbbreviation\", 22},\n\t\t\t            {\"MoneyDecimalSep\", \".\", \"MoneyDecimalSep\", 23},\n\t\t\t            {\"vMinDate\", \"44562\", \"vMinDate\", 24},\n\t\t\t            {\"vMaxDate\", \"45657\", \"vMaxDate\", 25},\n\t\t\t            {\"vTopN\", \"10\", \"Number of top customers to display\", 26},\n\t\t\t            {\"vMeasure\", \"1\", \"Dynamic measure for chart analysis\", 27}\n\t\t\t\t        }\n\t\t\t\t    )\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Routes.tmdl": "table Routes\n\tlineageTag: 93f37141-d3c2-56bb-b0a2-4b0103dc7a39\n\n\tcolumn route_id\n\t\tdataType: string\n\t\tlineageTag: 9253f750-0daf-541e-a41e-f3a85786e891\n\t\tsummarizeBy: none\n\t\tsourceColumn: route_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn origin_city\n\t\tdataType: string\n\t\tlineageTag: b0a4338f-646b-5168-9396-8c7ab6e1e4c9\n\t\tsummarizeBy: none\n\t\tsourceColumn: origin_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn origin_state\n\t\tdataType: string\n\t\tlineageTag: ec33afe8-f83d-5f0b-a89a-5a019ac8a7e0\n\t\tsummarizeBy: none\n\t\tsourceColumn: origin_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn destination_city\n\t\tdataType: string\n\t\tlineageTag: 3d111ce7-9772-5c85-8695-e1eee9b231f3\n\t\tsummarizeBy: none\n\t\tsourceColumn: destination_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn destination_state\n\t\tdataType: string\n\t\tlineageTag: ba882fe1-8ab5-56df-862a-196b0c49407c\n\t\tsummarizeBy: none\n\t\tsourceColumn: destination_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn typical_distance_miles\n\t\tdataType: double\n\t\tlineageTag: dabf4cb2-3268-5938-a8c0-ab380f252996\n\t\tsummarizeBy: sum\n\t\tsourceColumn: typical_distance_miles\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn base_rate_per_mile\n\t\tdataType: double\n\t\tlineageTag: 605fcf2e-c734-5400-bd98-d45148bd7781\n\t\tsummarizeBy: sum\n\t\tsourceColumn: base_rate_per_mile\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_surcharge_rate\n\t\tdataType: double\n\t\tlineageTag: 033fed09-6dd1-535b-b5e9-606d0a9fed9f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_surcharge_rate\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn typical_transit_days\n\t\tdataType: double\n\t\tlineageTag: 6f23b6f1-12ca-5959-810f-624b91b019cf\n\t\tsummarizeBy: sum\n\t\tsourceColumn: typical_transit_days\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Routes = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.routes\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/SafetyByTrip.tmdl": "table SafetyByTrip\n\tlineageTag: aa58eacf-4c38-56da-b2a4-32a0492f9137\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: e5ef2bce-9187-5407-8570-b00e059eb4e0\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn SafetyIncidents\n\t\tdataType: double\n\t\tlineageTag: d731dbe6-39d5-555d-8038-75043b044cf6\n\t\tsummarizeBy: sum\n\t\tsourceColumn: SafetyIncidents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn PreventableIncidents\n\t\tdataType: double\n\t\tlineageTag: c3fc69af-3b1c-5ac5-880b-89e3b917e39e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: PreventableIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn InjuryIncidents\n\t\tdataType: double\n\t\tlineageTag: 4635d220-b341-5fc2-901a-9e8f9bac6e42\n\t\tsummarizeBy: sum\n\t\tsourceColumn: InjuryIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AtFaultIncidents\n\t\tdataType: double\n\t\tlineageTag: c02b0008-05aa-556f-996c-5bb0de59ed13\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AtFaultIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn VehicleDamageCost\n\t\tdataType: double\n\t\tlineageTag: dceec3bc-c146-5c4e-9ced-aa6bc728f9be\n\t\tsummarizeBy: sum\n\t\tsourceColumn: VehicleDamageCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CargoDamageCost\n\t\tdataType: double\n\t\tlineageTag: bf16af75-143b-539f-977e-65d73e977b5a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CargoDamageCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn ClaimAmount\n\t\tdataType: double\n\t\tlineageTag: e49b00b3-7f3b-59f0-a985-84df8cc7bcf4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: ClaimAmount\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition SafetyByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = SafetyIncidents\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/SafetyIncidents.tmdl": "table SafetyIncidents\n\tlineageTag: 88a98507-fbbe-56a6-a39e-af2a849e26e2\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: a89c8ced-7a7d-5ae2-9f34-fb17d593789a\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_id\n\t\tdataType: string\n\t\tlineageTag: d05f6c85-8144-54a2-8913-785108e0b87f\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_date\n\t\tdataType: dateTime\n\t\tlineageTag: 3940a4eb-c4af-5d7d-b179-4dbbb54cce4e\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_type\n\t\tdataType: string\n\t\tlineageTag: 35cef020-ecb0-5ce9-97be-b6d0b67ce2ef\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_city\n\t\tdataType: string\n\t\tlineageTag: b89c2e58-5b6a-5878-af24-00365499082e\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_state\n\t\tdataType: string\n\t\tlineageTag: b506cee5-77d0-597d-bef5-e3fe1594bd05\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn at_fault_flag\n\t\tdataType: string\n\t\tlineageTag: 4a3bc60b-49f5-5d8f-a8d7-221422c729df\n\t\tsummarizeBy: none\n\t\tsourceColumn: at_fault_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn injury_flag\n\t\tdataType: string\n\t\tlineageTag: d33ab9b7-cede-542b-8b3c-05a9a7a6c83b\n\t\tsummarizeBy: none\n\t\tsourceColumn: injury_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn vehicle_damage_cost\n\t\tdataType: double\n\t\tlineageTag: 28fe3887-f05b-51b8-841f-d268204c9874\n\t\tsummarizeBy: sum\n\t\tsourceColumn: vehicle_damage_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn cargo_damage_cost\n\t\tdataType: double\n\t\tlineageTag: daa92f9c-c5b3-5115-8ce8-1a56cbe6aa6d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: cargo_damage_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn claim_amount\n\t\tdataType: double\n\t\tlineageTag: 3860c0c0-6df4-531d-a92b-da1716e1af52\n\t\tsummarizeBy: sum\n\t\tsourceColumn: claim_amount\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn preventable_flag\n\t\tdataType: string\n\t\tlineageTag: 3650567e-08b6-5b69-9d0d-1b9db866e48f\n\t\tsummarizeBy: none\n\t\tsourceColumn: preventable_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn description\n\t\tdataType: string\n\t\tlineageTag: 833a5045-e9b0-5c64-979f-ecec0033d570\n\t\tsummarizeBy: none\n\t\tsourceColumn: description\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition SafetyIncidents = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    incident_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    incident_date,\n\t\t\t\t    incident_type,\n\t\t\t\t    location_city         AS incident_city,\n\t\t\t\t    location_state        AS incident_state,\n\t\t\t\t    at_fault_flag,\n\t\t\t\t    injury_flag,\n\t\t\t\t    vehicle_damage_cost,\n\t\t\t\t    cargo_damage_cost,\n\t\t\t\t    claim_amount,\n\t\t\t\t    preventable_flag,\n\t\t\t\t    description\n\t\t\t\t    FROM fleetvision.safety_incidents\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/TempCalendar.tmdl": "table TempCalendar\n\tlineageTag: 5e0cd0f0-e0ba-57de-8846-e7ae4705b534\n\n\tcolumn MinDate\n\t\tdataType: double\n\t\tlineageTag: 684b2574-4b39-53f6-93bb-0271715bf31f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MinDate\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MaxDate\n\t\tdataType: double\n\t\tlineageTag: 22d091f3-9138-5e68-8cdf-d6b4c35c21f3\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MaxDate\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TempCalendar = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"MinDate\", \"MaxDate\"}, {{#date(2020, 1, 1), #date(2026, 12, 31)}})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Trailers.tmdl": "table Trailers\n\tlineageTag: 1b47d346-6321-5afa-aecf-d2d29ece3614\n\n\tmeasure 'Active Trailers' = CALCULATE(DISTINCTCOUNT('Trips'[trailer_id]), 'Trailers'[trailer_status] = \"Active\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: efd511ba-959e-5b93-8c68-f84eb5915b8d\n\n\tcolumn trailer_id\n\t\tdataType: string\n\t\tlineageTag: 0183f130-8708-55df-85c5-260e1c85c1fa\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_number\n\t\tdataType: double\n\t\tlineageTag: 414a5015-4ca9-5eef-8025-1b59c240838a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: trailer_number\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_type\n\t\tdataType: string\n\t\tlineageTag: 5004a82c-bd7b-53ca-a7a6-cc23f755e368\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn length_feet\n\t\tdataType: double\n\t\tlineageTag: aef9fab4-4d68-59fc-adee-ceb211777735\n\t\tsummarizeBy: sum\n\t\tsourceColumn: length_feet\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_model_year\n\t\tdataType: int64\n\t\tlineageTag: b919d6f3-e2c0-59e6-8c9c-a6ca2ecaed93\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_model_year\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_vin\n\t\tdataType: string\n\t\tlineageTag: b9a6765b-089e-5e6d-935d-1d7f02737803\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_vin\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_acquisition_date\n\t\tdataType: dateTime\n\t\tlineageTag: 1e9b71af-bd39-561d-84b4-767fcf183f17\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_acquisition_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_status\n\t\tdataType: string\n\t\tlineageTag: 68e0f56d-685b-585a-9d28-68836c73c1e6\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn current_location\n\t\tdataType: string\n\t\tlineageTag: f5953b51-85ea-5dcb-82d0-975122fd0da7\n\t\tsummarizeBy: none\n\t\tsourceColumn: current_location\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trailers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    trailer_id,\n\t\t\t\t    trailer_number,\n\t\t\t\t    trailer_type,\n\t\t\t\t    length_feet,\n\t\t\t\t    model_year            AS trailer_model_year,\n\t\t\t\t    vin                   AS trailer_vin,\n\t\t\t\t    acquisition_date      AS trailer_acquisition_date,\n\t\t\t\t    status                AS trailer_status,\n\t\t\t\t    current_location\n\t\t\t\t    FROM fleetvision.trailers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/Trips.tmdl": "table Trips\n\tlineageTag: 3b0e1031-f748-5307-97a6-2f8653b800cd\n\n\tmeasure 'Maximum Trips by Truck' = MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 8dbb9c27-3953-55a5-b794-ee73660ad1b0\n\n\tmeasure 'Average Trip Distance' = AVERAGE('Trips'[actual_distance_miles])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e35b7be9-e127-541f-ad6a-bc4af4bb08cc\n\n\tmeasure 'Average Trip Duration' = AVERAGE('Trips'[actual_duration_hours])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 02209d34-c0d5-5a0b-b601-dbd7d263f297\n\n\tmeasure 'Total Trips' = COUNT('Trips'[trip_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: ea0647f4-bb8e-5695-81ab-ea36102811b3\n\n\tmeasure 'Total Drivers' = DISTINCTCOUNT('Trips'[driver_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 68a17c3b-ad04-50fc-b2ce-020ad3d1aa60\n\n\tmeasure 'Completed Trips' = CALCULATE(COUNT('Trips'[trip_id]), 'Trips'[trip_status] = \"Completed\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: d2d76ee4-575e-578f-bce6-66873c2a5729\n\n\tmeasure 'Completed Trip Revenue' = CALCULATE(SUM('Loads'[revenue]), 'Trips'[trip_status] = \"Completed\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 86eaa52e-08bb-55ec-abcb-003200199e96\n\n\tmeasure 'Average Fuel Efficiency' = DIVIDE(SUM('Trips'[actual_distance_miles]), SUM('Trips'[fuel_gallons_used]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e65eef8f-660c-5c9d-a653-c6f0286b46d3\n\n\tmeasure 'Fleet Operations' = MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 2ef29338-e4c0-5eed-a44e-0f4e6a6cc9aa\n\n\tmeasure 'Fleet Size' = DISTINCTCOUNT('Trips'[truck_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 15746ebf-8cf3-5cb4-aa70-041d190332e4\n\n\tmeasure 'Total Revenue Trips' = SUM('Loads'[revenue])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: f7d01dcf-3507-5017-a4e6-e11c2c850871\n\n\tmeasure 'Avg(idle_time_hours)' = AVERAGE('Trips'[idle_time_hours])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 006dce75-05d3-57ff-9787-b106c34baf73\n\n\tmeasure 'Avg(actual_distance_miles)' = AVERAGE('Trips'[actual_distance_miles])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5a97047a-bc4b-53e2-a3ee-96e38586420e\n\n\tmeasure 'Avg(average_mpg)' = AVERAGE('Trips'[average_mpg])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 7441cc14-eea6-5581-9600-a9ba5b5c9101\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: 99962d85-9cae-523b-a19e-c09fadd976ba\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 1338433a-4a62-55b4-a344-674a5641b340\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_id\n\t\tdataType: string\n\t\tlineageTag: 801332f2-6eca-58b9-9ca0-d0c0dc2bc758\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_id\n\t\tdataType: string\n\t\tlineageTag: 5fab398c-09f6-5896-a42d-7668e98edc81\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 45cb32c6-db6c-5f44-85a6-3162428e74be\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_distance_miles\n\t\tdataType: double\n\t\tlineageTag: a004a973-4cc0-54a1-b1cc-93e53f3baebd\n\t\tsummarizeBy: sum\n\t\tsourceColumn: actual_distance_miles\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_duration_hours\n\t\tdataType: double\n\t\tlineageTag: adee4386-7c9e-537e-a68e-f34c676feeab\n\t\tsummarizeBy: sum\n\t\tsourceColumn: actual_duration_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_gallons_used\n\t\tdataType: double\n\t\tlineageTag: 9fd8b063-6828-516a-bf44-49ace097b0d7\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_gallons_used\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn average_mpg\n\t\tdataType: double\n\t\tlineageTag: f8b79f28-4d66-5115-a313-9a2d5db414a5\n\t\tsummarizeBy: sum\n\t\tsourceColumn: average_mpg\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn idle_time_hours\n\t\tdataType: double\n\t\tlineageTag: a86e4c62-3297-59ae-805f-073e8fd8c1c2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: idle_time_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_status\n\t\tdataType: string\n\t\tlineageTag: e04d3a7a-6952-55f9-8ce8-b847c9ce6302\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckNumber = RELATED('Trucks'[truck_id])\n\t\tdataType: double\n\t\tlineageTag: 39eaa460-d6dc-597f-bb14-fee3dbcee91b\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DispatchDate = 'Trips'[dispatch_date]\n\t\tdataType: dateTime\n\t\tlineageTag: 6d76169b-6ede-540e-b064-7644c8d1b3f2\n\t\tsummarizeBy: none\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripMonth = FORMAT('Trips'[dispatch_date], \"mmmm\")\n\t\tdataType: double\n\t\tlineageTag: 27aaefa0-1993-5137-a5e5-a282e2b14f17\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn LoadMonth = FORMAT('Trips'[dispatch_date], \"mmmm\")\n\t\tdataType: double\n\t\tlineageTag: 4e57d450-05ee-5b88-b844-952746d313a0\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthStartDate\n\t\tdataType: dateTime\n\t\tlineageTag: 1ca03fd6-490f-58a9-8c09-57d005442371\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthStartDate\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthYear\n\t\tdataType: int64\n\t\tlineageTag: 1fd18945-0767-5c21-b6bb-7ec4be1ca5a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthYear\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthSort\n\t\tdataType: dateTime\n\t\tlineageTag: 366fd966-946d-50e0-ba39-e6a81006f822\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthSort\n\t\tformatString: General Date\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripYear = YEAR('Trips'[dispatch_date])\n\t\tdataType: int64\n\t\tlineageTag: 218aba61-06ec-54fd-8602-cfb0bcd1554f\n\t\tsummarizeBy: none\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripWeek = WEEKNUM('Trips'[dispatch_date])\n\t\tdataType: double\n\t\tlineageTag: adcb080b-6fd7-5eb1-a8e4-e387c72d0b07\n\t\tsummarizeBy: sum\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthNo\n\t\tdataType: double\n\t\tlineageTag: 21d65fba-e797-59b4-a21a-449aacd3cbdb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MonthNo\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DistanceBand = SWITCH(TRUE(), 'Trips'[actual_distance_miles] >= 1000, \"Long Haul\", 'Trips'[actual_distance_miles] >= 500, \"Medium Haul\", \"Short Haul\")\n\t\tdataType: string\n\t\tlineageTag: b4374b2a-0eef-5fe1-817b-7637e170f0cc\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FuelEfficiencyBand = SWITCH(TRUE(), 'Trips'[average_mpg] >= 8, \"High MPG\", 'Trips'[average_mpg] >= 6, \"Medium MPG\", \"Low MPG\")\n\t\tdataType: string\n\t\tlineageTag: 18facad7-0e7d-5994-9189-03fa7f5fedf0\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn IdleTimeBand = SWITCH(TRUE(), 'Trips'[idle_time_hours] >= 5, \"High Idle\", 'Trips'[idle_time_hours] >= 2, \"Moderate Idle\", \"Low Idle\")\n\t\tdataType: string\n\t\tlineageTag: 29d2e21b-0ecb-5b30-aa0a-d32756f84cfd\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trips = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"driver_id\", \"truck_id\", \"trailer_id\", \"load_id\", \"trip_id\", \"actual_distance_miles\", \"actual_duration_hours\", \"fuel_gallons_used\", \"average_mpg\", \"idle_time_hours\", \"trip_status\", \"TruckNumber\", \"DispatchDate\", \"TripMonth\", \"LoadMonth\", \"MonthStartDate\", \"MonthYear\", \"MonthSort\", \"TripYear\", \"TripWeek\", \"MonthNo\", \"DistanceBand\", \"FuelEfficiencyBand\", \"IdleTimeBand\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table",
            "definition/tables/TruckMap.tmdl": "table TruckMap\n\tlineageTag: f849a69c-f307-572a-b709-bee9c68d7ce4\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 9fcbeac3-e3d6-51a6-90c4-3b78c43bc3c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn unit_number\n\t\tdataType: double\n\t\tlineageTag: 707814c6-679d-50f6-9025-05bb8a6a9b91\n\t\tsummarizeBy: sum\n\t\tsourceColumn: unit_number\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TruckMap = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trucks,\n\t\t\t\t    #\"Distinct Rows\" = Table.Distinct(Source)\n\t\t\t\tin\n\t\t\t\t    #\"Distinct Rows\"\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/TruckPerformance.tmdl": "table TruckPerformance\n\tlineageTag: 465a4b13-9cea-5d82-a904-b415d908d3d7\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 3cf0614d-07a3-5b0e-b752-263e9653ff41\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckTrips\n\t\tdataType: double\n\t\tlineageTag: a3c3519c-de0e-5eab-82e4-6aee90391607\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckTrips\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckMiles\n\t\tdataType: double\n\t\tlineageTag: 61cd7d72-c934-5d24-bcbd-4d4a7aa0a0ba\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckMiles\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckHours\n\t\tdataType: double\n\t\tlineageTag: 4d08bd4d-6d19-51ec-a8c0-7e9949ceb3d2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckFuelGallons\n\t\tdataType: double\n\t\tlineageTag: 8f25cb4f-f83a-56d4-a428-d3e85f6742ec\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckFuelGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckMPG\n\t\tdataType: double\n\t\tlineageTag: 384ea1ed-afcf-5f6b-8f67-7a55b4596283\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckMPG\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckAvgIdleHours\n\t\tdataType: double\n\t\tlineageTag: a8769a6e-9da8-5d92-8bff-1fa222209c07\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckAvgIdleHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckIdleHours\n\t\tdataType: double\n\t\tlineageTag: b5ec3feb-86f2-555c-8530-6f72d2c7a9fa\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckIdleHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TruckPerformance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trips\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
            "definition/tables/Trucks.tmdl": "table Trucks\n\tlineageTag: 73040672-c518-5b15-ba0c-643ceb78be53\n\n\tmeasure 'Active Trucks' = CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[truck_status] = \"Active\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c15447ed-173b-597c-9fbd-28e01a6288cc\n\n\tmeasure 'Diesel Trucks' = CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[fuel_type] = \"Diesel\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: f6f5cf4a-1ce0-556e-8a42-57c0aa05be76\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: b7013c61-049e-5aa8-ba0f-e722fd6b91a8\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn unit_number\n\t\tdataType: double\n\t\tlineageTag: 0e1ef306-99e3-50e5-a961-5ac3429de1ae\n\t\tsummarizeBy: sum\n\t\tsourceColumn: unit_number\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn make\n\t\tdataType: string\n\t\tlineageTag: dedc418c-722c-52e7-b7f7-d19d7d951059\n\t\tsummarizeBy: none\n\t\tsourceColumn: make\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_model_year\n\t\tdataType: int64\n\t\tlineageTag: 5a007012-c08e-5d30-8d3a-04b12852280b\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_model_year\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_vin\n\t\tdataType: string\n\t\tlineageTag: bd430b8b-5845-581e-ae1c-55b5040bd471\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_vin\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_acquisition_date\n\t\tdataType: dateTime\n\t\tlineageTag: 2e4c72cd-e481-55b7-867c-42ca2fc6fb24\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_acquisition_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn acquisition_mileage\n\t\tdataType: double\n\t\tlineageTag: 250cf308-dbe2-5b4f-8a59-47ce9e99fdf8\n\t\tsummarizeBy: sum\n\t\tsourceColumn: acquisition_mileage\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_type\n\t\tdataType: string\n\t\tlineageTag: 4cb86b0b-807b-5b29-bbd0-5187c33b2d9a\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn tank_capacity_gallons\n\t\tdataType: double\n\t\tlineageTag: 3bf65880-7cf0-55d9-a4be-fcb8a908112f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: tank_capacity_gallons\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_status\n\t\tdataType: string\n\t\tlineageTag: 3140ac2e-3bdc-58ac-a113-fa169e3d4934\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_home_terminal\n\t\tdataType: string\n\t\tlineageTag: bb3b2d4c-4c72-5a36-8a99-9af955ca22cf\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_home_terminal\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trucks = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    truck_id,\n\t\t\t\t    unit_number,\n\t\t\t\t    make,\n\t\t\t\t    model_year            AS truck_model_year,\n\t\t\t\t    vin                   AS truck_vin,\n\t\t\t\t    acquisition_date      AS truck_acquisition_date,\n\t\t\t\t    acquisition_mileage,\n\t\t\t\t    fuel_type,\n\t\t\t\t    tank_capacity_gallons,\n\t\t\t\t    status                AS truck_status,\n\t\t\t\t    home_terminal         AS truck_home_terminal\n\t\t\t\t    FROM fleetvision.trucks\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table"
        },
        "report": {
            ".pbi/localSettings.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/localSettings/1.0.0/schema.json"
            },
            ".platform": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
                "metadata": {
                    "type": "Report",
                    "displayName": "FleetVision KSA"
                },
                "config": {
                    "version": "2.0",
                    "logicalId": "c86a1869-774f-5eb5-ab09-cedc8cf2af56"
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
                        "path": "../FleetVision KSA.SemanticModel"
                    }
                }
            },
            "definition/bookmarks/Bookmark001.bookmark.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
                "name": "Bookmark001",
                "displayName": "Fuel Efficiency",
                "explorationState": {
                    "version": "1.0.0",
                    "activeSection": "executive-overview",
                    "sections": {
                        "executive-overview": {
                            "visualContainers": {}
                        }
                    }
                }
            },
            "definition/bookmarks/Bookmark002.bookmark.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
                "name": "Bookmark002",
                "displayName": "High Value Loads",
                "explorationState": {
                    "version": "1.0.0",
                    "activeSection": "executive-overview",
                    "sections": {
                        "executive-overview": {
                            "visualContainers": {}
                        }
                    }
                }
            },
            "definition/bookmarks/Bookmark003.bookmark.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
                "name": "Bookmark003",
                "displayName": "Overall Operations",
                "explorationState": {
                    "version": "1.0.0",
                    "activeSection": "executive-overview",
                    "sections": {
                        "executive-overview": {
                            "visualContainers": {}
                        }
                    }
                }
            },
            "definition/bookmarks/bookmarks.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmarksMetadata/1.0.0/schema.json",
                "items": [
                    {
                        "name": "Bookmark001"
                    },
                    {
                        "name": "Bookmark002"
                    },
                    {
                        "name": "Bookmark003"
                    }
                ]
            },
            "definition/pages/customer-revenue-analytics/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "customer-revenue-analytics",
                "displayName": "Customer & Revenue Analytics",
                "displayOption": "FitToWidth",
                "height": 1300,
                "width": 1280
            },
            "definition/pages/customer-revenue-analytics/visuals/02c7510c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "02c7510c",
                "position": {
                    "x": 0,
                    "y": 960,
                    "width": 640,
                    "height": 300,
                    "z": 13,
                    "tabOrder": 13
                },
                "visual": {
                    "visualType": "image",
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
                                                "Value": "'Customer Analytics'"
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
            "definition/pages/customer-revenue-analytics/visuals/051cada8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "051cada8",
                "position": {
                    "x": 480,
                    "y": 300,
                    "width": 427,
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Revenue by Booking Type'"
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
            "definition/pages/customer-revenue-analytics/visuals/103bf763/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "103bf763",
                "position": {
                    "x": 533,
                    "y": 0,
                    "width": 213,
                    "height": 120,
                    "z": 2,
                    "tabOrder": 2
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "High Value Loads"
                                            }
                                        },
                                        "queryRef": "Loads.High Value Loads",
                                        "nativeQueryRef": "High Value Loads"
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
                                                "Value": "'High Value Loads'"
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
            "definition/pages/customer-revenue-analytics/visuals/1c21c9d1/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "1c21c9d1",
                "position": {
                    "x": 907,
                    "y": 300,
                    "width": 373,
                    "height": 300,
                    "z": 11,
                    "tabOrder": 11
                },
                "visual": {
                    "visualType": "donutChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "RevenueBand"
                                            }
                                        },
                                        "queryRef": "Loads.RevenueBand",
                                        "nativeQueryRef": "RevenueBand",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Loads"
                                            }
                                        },
                                        "queryRef": "Loads.Total Loads",
                                        "nativeQueryRef": "Total Loads"
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
                                                "Value": "'Load Distribution by Revenue Band'"
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
            "definition/pages/customer-revenue-analytics/visuals/21cf3e64/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "21cf3e64",
                "position": {
                    "x": 320,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 8,
                    "tabOrder": 8
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "MonthYear"
                                            }
                                        },
                                        "queryRef": "Trips.MonthYear",
                                        "nativeQueryRef": "MonthYear",
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
                                                "Value": "'MonthYear'"
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
            "definition/pages/customer-revenue-analytics/visuals/2c01dd2c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "2c01dd2c",
                "position": {
                    "x": 0,
                    "y": 600,
                    "width": 1280,
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "MonthYear"
                                            }
                                        },
                                        "queryRef": "Trips.MonthYear",
                                        "nativeQueryRef": "MonthYear",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Monthly Customer Revenue Trend'"
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
            "definition/pages/customer-revenue-analytics/visuals/5ef147d0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "5ef147d0",
                "position": {
                    "x": 1013,
                    "y": 0,
                    "width": 267,
                    "height": 120,
                    "z": 1,
                    "tabOrder": 1
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "High Value Revenue %"
                                            }
                                        },
                                        "queryRef": "Loads.High Value Revenue %",
                                        "nativeQueryRef": "High Value Revenue %"
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
                                                "Value": "'High Value Revenue %'"
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
            "definition/pages/customer-revenue-analytics/visuals/7b210fc2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "7b210fc2",
                "position": {
                    "x": 640,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 7,
                    "tabOrder": 7
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "RevenueBand"
                                            }
                                        },
                                        "queryRef": "Loads.RevenueBand",
                                        "nativeQueryRef": "RevenueBand",
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
                                                "Value": "'RevenueBand'"
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
            "definition/pages/customer-revenue-analytics/visuals/881373ba/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "881373ba",
                "position": {
                    "x": 640,
                    "y": 960,
                    "width": 640,
                    "height": 300,
                    "z": 14,
                    "tabOrder": 14
                },
                "visual": {
                    "visualType": "image",
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
                                                "Value": "'Revenue Analytics'"
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
            "definition/pages/customer-revenue-analytics/visuals/a07fbaca/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a07fbaca",
                "position": {
                    "x": 960,
                    "y": 120,
                    "width": 320,
                    "height": 180,
                    "z": 6,
                    "tabOrder": 6
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
                                                        "Entity": "Routes"
                                                    }
                                                },
                                                "Property": "origin_city"
                                            }
                                        },
                                        "queryRef": "Routes.origin_city",
                                        "nativeQueryRef": "origin_city",
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
                                                "Value": "'Route'"
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
            "definition/pages/customer-revenue-analytics/visuals/c7e82bb2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c7e82bb2",
                "position": {
                    "x": 0,
                    "y": 300,
                    "width": 480,
                    "height": 300,
                    "z": 9,
                    "tabOrder": 9
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "customer_id"
                                            }
                                        },
                                        "queryRef": "Customers.customer_id",
                                        "nativeQueryRef": "customer_id",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Revenue Contribution by Customer'"
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
            "definition/pages/customer-revenue-analytics/visuals/c934b93e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c934b93e",
                "position": {
                    "x": 747,
                    "y": 0,
                    "width": 267,
                    "height": 120,
                    "z": 3,
                    "tabOrder": 3
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Average Revenue per Customer"
                                            }
                                        },
                                        "queryRef": "Loads.Average Revenue per Customer",
                                        "nativeQueryRef": "Average Revenue per Customer"
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
                                                "Value": "'Average Revenue per Customer'"
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
            "definition/pages/customer-revenue-analytics/visuals/d91b886b/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "d91b886b",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 267,
                    "height": 120,
                    "z": 0,
                    "tabOrder": 0
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Highest Revenue by Customer"
                                            }
                                        },
                                        "queryRef": "Loads.Highest Revenue by Customer",
                                        "nativeQueryRef": "Highest Revenue by Customer"
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
                                                "Value": "'Highest Revenue by Customer'"
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
            "definition/pages/customer-revenue-analytics/visuals/df6c0c52/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "df6c0c52",
                "position": {
                    "x": 267,
                    "y": 0,
                    "width": 267,
                    "height": 120,
                    "z": 4,
                    "tabOrder": 4
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Completed Trip Revenue"
                                            }
                                        },
                                        "queryRef": "Trips.Completed Trip Revenue",
                                        "nativeQueryRef": "Completed Trip Revenue"
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
                                                "Value": "'Completed Trip Revenue'"
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
            "definition/pages/customer-revenue-analytics/visuals/e3b735db/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e3b735db",
                "position": {
                    "x": 0,
                    "y": 120,
                    "width": 320,
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "customer_id"
                                            }
                                        },
                                        "queryRef": "Customers.customer_id",
                                        "nativeQueryRef": "customer_id",
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
                                                "Value": "'Customer'"
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
            "definition/pages/customer-revenue-analytics/visuals/nav00c936e5/visual.json": {
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
            "definition/pages/customer-revenue-analytics/visuals/nav01db0cd2/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav01db0cd2",
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
                                                "Value": "'Fleet Operations'"
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
                                                "Value": "'fleet-operations'"
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
                                                "Value": "'fleet-operations'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/customer-revenue-analytics/visuals/nav029abe44/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "nav029abe44",
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
                                                "Value": "'Customer & Revenue Analytics'"
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
                                                "Value": "'customer-revenue-analytics'"
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
                                                "Value": "'customer-revenue-analytics'"
                                            }
                                        }
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "definition/pages/executive-overview/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "executive-overview",
                "displayName": "Executive Overview",
                "displayOption": "FitToWidth",
                "height": 1840,
                "width": 1280
            },
            "definition/pages/executive-overview/visuals/001df091/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "001df091",
                "position": {
                    "x": 640,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 2,
                    "tabOrder": 2
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "Total Customers"
                                            }
                                        },
                                        "queryRef": "Customers.Total Customers",
                                        "nativeQueryRef": "Total Customers"
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
                                                "Value": "'Total Customers'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/0f31f174/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "0f31f174",
                "position": {
                    "x": 0,
                    "y": 600,
                    "width": 640,
                    "height": 120,
                    "z": 19,
                    "tabOrder": 19
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
                                                        "Entity": "Parameters"
                                                    }
                                                },
                                                "Property": "Label"
                                            }
                                        },
                                        "queryRef": "Parameters.Label",
                                        "nativeQueryRef": "Label",
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
                                                "Value": "'Metric'"
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
            "definition/pages/executive-overview/visuals/11a70f5c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "11a70f5c",
                "position": {
                    "x": 853,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 15,
                    "tabOrder": 15
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                "Value": "'Load Month'"
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
            "definition/pages/executive-overview/visuals/4c98e4a9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "4c98e4a9",
                "position": {
                    "x": 0,
                    "y": 1440,
                    "width": 1280,
                    "height": 360,
                    "z": 9,
                    "tabOrder": 9
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "customer_id"
                                            }
                                        },
                                        "queryRef": "Customers.customer_id",
                                        "nativeQueryRef": "customer_id",
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
                                                "Value": "'Top Customers'"
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
            "definition/pages/executive-overview/visuals/50087210/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "50087210",
                "position": {
                    "x": 0,
                    "y": 540,
                    "width": 640,
                    "height": 60,
                    "z": 20,
                    "tabOrder": 20
                },
                "visual": {
                    "visualType": "actionButton",
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
                                                "Value": "'Go to Fleet Opeations'"
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
                                                "Value": "'Source Sans Pro'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#0065B3'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e1dad5'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/6a4064d9/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "6a4064d9",
                "position": {
                    "x": 1067,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 12,
                    "tabOrder": 12
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                "Value": "'Load Type'"
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
            "definition/pages/executive-overview/visuals/79c10c67/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "79c10c67",
                "position": {
                    "x": 213,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 13,
                    "tabOrder": 13
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
                                                        "Entity": "Drivers"
                                                    }
                                                },
                                                "Property": "first_name"
                                            }
                                        },
                                        "queryRef": "Drivers.first_name",
                                        "nativeQueryRef": "first_name",
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
                                                "Value": "'Driver'"
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
            "definition/pages/executive-overview/visuals/864fc125/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "864fc125",
                "position": {
                    "x": 427,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 16,
                    "tabOrder": 16
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
                                                        "Entity": "Trucks"
                                                    }
                                                },
                                                "Property": "truck_model_year"
                                            }
                                        },
                                        "queryRef": "Trucks.truck_model_year",
                                        "nativeQueryRef": "truck_model_year",
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
                                                "Value": "'Truck'"
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
            "definition/pages/executive-overview/visuals/90ee1b00/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "90ee1b00",
                "position": {
                    "x": 640,
                    "y": 720,
                    "width": 640,
                    "height": 360,
                    "z": 6,
                    "tabOrder": 6
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "customer_id"
                                            }
                                        },
                                        "queryRef": "Customers.customer_id",
                                        "nativeQueryRef": "customer_id",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Top 10 Customers by Revenue'"
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
            "definition/pages/executive-overview/visuals/9c586391/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9c586391",
                "position": {
                    "x": 0,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 0,
                    "tabOrder": 0
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Total Revenue'"
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
                                                "Value": "20.0D"
                                            }
                                        }
                                    },
                                    "fontFamily": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'Abril Fatface'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/9ec80dd5/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "9ec80dd5",
                "position": {
                    "x": 427,
                    "y": 1080,
                    "width": 427,
                    "height": 360,
                    "z": 7,
                    "tabOrder": 7
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
                                                        "Entity": "Routes"
                                                    }
                                                },
                                                "Property": "origin_city"
                                            }
                                        },
                                        "queryRef": "Routes.origin_city",
                                        "nativeQueryRef": "origin_city",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Top 10 Routes by Revenue'"
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
            "definition/pages/executive-overview/visuals/a8a70822/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "a8a70822",
                "position": {
                    "x": 0,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 10,
                    "tabOrder": 10
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
                                                        "Entity": "Customers"
                                                    }
                                                },
                                                "Property": "customer_id"
                                            }
                                        },
                                        "queryRef": "Customers.customer_id",
                                        "nativeQueryRef": "customer_id",
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
                                                "Value": "'Customer'"
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
                                    "fontColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#c25dab'"
                                                    }
                                                }
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
            "definition/pages/executive-overview/visuals/aef55492/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "aef55492",
                "position": {
                    "x": 1067,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 4,
                    "tabOrder": 4
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Fleet Size"
                                            }
                                        },
                                        "queryRef": "Trips.Fleet Size",
                                        "nativeQueryRef": "Fleet Size"
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
                                                "Value": "'Fleet Size'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/bc1c0d2c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "bc1c0d2c",
                "position": {
                    "x": 853,
                    "y": 1080,
                    "width": 427,
                    "height": 360,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "donutChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Loads"
                                            }
                                        },
                                        "queryRef": "Loads.Total Loads",
                                        "nativeQueryRef": "Total Loads"
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
                                                "Value": "'Loads by Type'"
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
            "definition/pages/executive-overview/visuals/c0bb57e8/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c0bb57e8",
                "position": {
                    "x": 640,
                    "y": 180,
                    "width": 213,
                    "height": 300,
                    "z": 11,
                    "tabOrder": 11
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
                                                        "Entity": "Routes"
                                                    }
                                                },
                                                "Property": "origin_city"
                                            }
                                        },
                                        "queryRef": "Routes.origin_city",
                                        "nativeQueryRef": "origin_city",
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
                                                "Value": "'Route'"
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
            "definition/pages/executive-overview/visuals/d39556f0/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "d39556f0",
                "position": {
                    "x": 640,
                    "y": 540,
                    "width": 640,
                    "height": 60,
                    "z": 21,
                    "tabOrder": 21
                },
                "visual": {
                    "visualType": "actionButton",
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
                                                "Value": "'Go to Customer & Revenue Analytics'"
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
                        "action": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#0065B3'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e1dad5'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/e09d4e3a/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e09d4e3a",
                "position": {
                    "x": 213,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 17,
                    "tabOrder": 17
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Average Revenue per Load"
                                            }
                                        },
                                        "queryRef": "Loads.Average Revenue per Load",
                                        "nativeQueryRef": "Average Revenue per Load"
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
                                                "Value": "'Average Revenue per Load'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/e4c6985c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e4c6985c",
                "position": {
                    "x": 0,
                    "y": 720,
                    "width": 640,
                    "height": 360,
                    "z": 5,
                    "tabOrder": 5
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                        "Entity": "_Measures"
                                                    }
                                                },
                                                "Property": "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                                            }
                                        },
                                        "queryRef": "_Measures.='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )",
                                        "nativeQueryRef": "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
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
                                                "Value": "'='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend''"
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
            "definition/pages/executive-overview/visuals/e84c2667/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "e84c2667",
                "position": {
                    "x": 0,
                    "y": 1080,
                    "width": 427,
                    "height": 360,
                    "z": 14,
                    "tabOrder": 14
                },
                "visual": {
                    "visualType": "donutChart",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "route_id"
                                            }
                                        },
                                        "queryRef": "Loads.route_id",
                                        "nativeQueryRef": "route_id",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Loads"
                                            }
                                        },
                                        "queryRef": "Loads.Total Loads",
                                        "nativeQueryRef": "Total Loads"
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
                                                "Value": "'Loads by Booking Type'"
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
            "definition/pages/executive-overview/visuals/f274700f/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "f274700f",
                "position": {
                    "x": 427,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 1,
                    "tabOrder": 1
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Total Trips"
                                            }
                                        },
                                        "queryRef": "Trips.Total Trips",
                                        "nativeQueryRef": "Total Trips"
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
                                                "Value": "'Total Trips'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/ff30b3dd/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "ff30b3dd",
                "position": {
                    "x": 853,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 3,
                    "tabOrder": 3
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Total Drivers"
                                            }
                                        },
                                        "queryRef": "Trips.Total Drivers",
                                        "nativeQueryRef": "Total Drivers"
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
                                                "Value": "'Total Drivers'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#99cfcd'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/executive-overview/visuals/ffa08fac/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "ffa08fac",
                "position": {
                    "x": 640,
                    "y": 600,
                    "width": 640,
                    "height": 120,
                    "z": 18,
                    "tabOrder": 18
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
                                                        "Entity": "Parameters"
                                                    }
                                                },
                                                "Property": "Label"
                                            }
                                        },
                                        "queryRef": "Parameters.Label",
                                        "nativeQueryRef": "Label",
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
                                                "Value": "'Top N Customers'"
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
            "definition/pages/fleet-operations/page.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
                "name": "fleet-operations",
                "displayName": "Fleet Operations",
                "displayOption": "FitToWidth",
                "height": 820,
                "width": 1280
            },
            "definition/pages/fleet-operations/visuals/15b12c08/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "15b12c08",
                "position": {
                    "x": 0,
                    "y": 720,
                    "width": 640,
                    "height": 60,
                    "z": 10,
                    "tabOrder": 10
                },
                "visual": {
                    "visualType": "actionButton",
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
                                                "Value": "'Go to Executive overview'"
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
                                                "Value": "'Source Sans Pro'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#0065B3'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e1dad5'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/25d111c4/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "25d111c4",
                "position": {
                    "x": 640,
                    "y": 720,
                    "width": 640,
                    "height": 60,
                    "z": 11,
                    "tabOrder": 11
                },
                "visual": {
                    "visualType": "actionButton",
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
                                                "Value": "'Go to Customer & Revenue Analytics'"
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
                                                "Value": "'Source Sans Pro'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "action": [
                            {
                                "properties": {
                                    "type": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "'PageNavigation'"
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "fill": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "fillColor": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#0065B3'"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e1dad5'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/2e5b83ff/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "2e5b83ff",
                "position": {
                    "x": 853,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 1,
                    "tabOrder": 1
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Average Trip Duration"
                                            }
                                        },
                                        "queryRef": "Trips.Average Trip Duration",
                                        "nativeQueryRef": "Average Trip Duration"
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
                                                "Value": "'Average Trip Duration'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/5336c41a/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "5336c41a",
                "position": {
                    "x": 427,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 2,
                    "tabOrder": 2
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Average Trip Distance"
                                            }
                                        },
                                        "queryRef": "Trips.Average Trip Distance",
                                        "nativeQueryRef": "Average Trip Distance"
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
                                                "Value": "'Average Trip Distance'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/5815d4bb/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "5815d4bb",
                "position": {
                    "x": 0,
                    "y": 180,
                    "width": 907,
                    "height": 240,
                    "z": 5,
                    "tabOrder": 5
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "DistanceBand"
                                            }
                                        },
                                        "queryRef": "Trips.DistanceBand",
                                        "nativeQueryRef": "DistanceBand",
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Total Trips"
                                            }
                                        },
                                        "queryRef": "Trips.Total Trips",
                                        "nativeQueryRef": "Total Trips"
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
                                                "Value": "'Distance Band Distribution'"
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
            "definition/pages/fleet-operations/visuals/65fe3a5c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "65fe3a5c",
                "position": {
                    "x": 0,
                    "y": 420,
                    "width": 640,
                    "height": 300,
                    "z": 7,
                    "tabOrder": 7
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
                                                        "Entity": "TruckMap"
                                                    }
                                                },
                                                "Property": "unit_number"
                                            }
                                        },
                                        "queryRef": "TruckMap.unit_number",
                                        "nativeQueryRef": "unit_number",
                                        "active": true
                                    },
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "TruckMap"
                                                    }
                                                },
                                                "Property": "unit_number"
                                            }
                                        },
                                        "queryRef": "TruckMap.unit_number",
                                        "nativeQueryRef": "unit_number",
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Avg(actual_distance_miles)"
                                            }
                                        },
                                        "queryRef": "Trips.Avg(actual_distance_miles)",
                                        "nativeQueryRef": "Avg(actual_distance_miles)"
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Avg(average_mpg)"
                                            }
                                        },
                                        "queryRef": "Trips.Avg(average_mpg)",
                                        "nativeQueryRef": "Avg(average_mpg)"
                                    }
                                ]
                            },
                            "Size": {
                                "projections": [
                                    {
                                        "field": {
                                            "Measure": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Revenue"
                                            }
                                        },
                                        "queryRef": "Loads.Total Revenue",
                                        "nativeQueryRef": "Total Revenue"
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
                                                "Value": "'Truck Performance'"
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
            "definition/pages/fleet-operations/visuals/69cacc6e/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "69cacc6e",
                "position": {
                    "x": 907,
                    "y": 180,
                    "width": 373,
                    "height": 240,
                    "z": 6,
                    "tabOrder": 6
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "IdleTimeBand"
                                            }
                                        },
                                        "queryRef": "Trips.IdleTimeBand",
                                        "nativeQueryRef": "IdleTimeBand",
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Avg(idle_time_hours)"
                                            }
                                        },
                                        "queryRef": "Trips.Avg(idle_time_hours)",
                                        "nativeQueryRef": "Avg(idle_time_hours)"
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
                                                "Value": "'Idle Time Analysis'"
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
            "definition/pages/fleet-operations/visuals/b105a5be/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "b105a5be",
                "position": {
                    "x": 640,
                    "y": 0,
                    "width": 213,
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Fleet Operations"
                                            }
                                        },
                                        "queryRef": "Trips.Fleet Operations",
                                        "nativeQueryRef": "Fleet Operations"
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
                                                "Value": "'Fleet Operations'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/c47b0476/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "c47b0476",
                "position": {
                    "x": 213,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 0,
                    "tabOrder": 0
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
                                                        "Entity": "Trips"
                                                    }
                                                },
                                                "Property": "Average Fuel Efficiency"
                                            }
                                        },
                                        "queryRef": "Trips.Average Fuel Efficiency",
                                        "nativeQueryRef": "Average Fuel Efficiency"
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
                                                "Value": "'Average Fuel Efficiency'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/d8e3104c/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "d8e3104c",
                "position": {
                    "x": 640,
                    "y": 420,
                    "width": 640,
                    "height": 300,
                    "z": 8,
                    "tabOrder": 8
                },
                "visual": {
                    "visualType": "funnel",
                    "query": {
                        "queryState": {
                            "Category": {
                                "projections": [
                                    {
                                        "field": {
                                            "Column": {
                                                "Expression": {
                                                    "SourceRef": {
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "RevenueBand"
                                            }
                                        },
                                        "queryRef": "Loads.RevenueBand",
                                        "nativeQueryRef": "RevenueBand",
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Total Loads"
                                            }
                                        },
                                        "queryRef": "Loads.Total Loads",
                                        "nativeQueryRef": "Total Loads"
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
                                                "Value": "'High Value Loads'"
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
            "definition/pages/fleet-operations/visuals/dbe9586d/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "dbe9586d",
                "position": {
                    "x": 1067,
                    "y": 0,
                    "width": 213,
                    "height": 180,
                    "z": 4,
                    "tabOrder": 4
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
                                                        "Entity": "Loads"
                                                    }
                                                },
                                                "Property": "Revenue per Mile"
                                            }
                                        },
                                        "queryRef": "Loads.Revenue per Mile",
                                        "nativeQueryRef": "Revenue per Mile"
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
                                                "Value": "'Revenue per Mile'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/fleet-operations/visuals/f7d0a73a/visual.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
                "name": "f7d0a73a",
                "position": {
                    "x": 320,
                    "y": 240,
                    "width": 213,
                    "height": 180,
                    "z": 3,
                    "tabOrder": 3
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
                                                        "Entity": "Trucks"
                                                    }
                                                },
                                                "Property": "Active Trucks"
                                            }
                                        },
                                        "queryRef": "Trucks.Active Trucks",
                                        "nativeQueryRef": "Active Trucks"
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
                                                "Value": "'Active Trucks'"
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
                        "background": [
                            {
                                "properties": {
                                    "show": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "true"
                                            }
                                        }
                                    },
                                    "color": {
                                        "solid": {
                                            "color": {
                                                "expr": {
                                                    "Literal": {
                                                        "Value": "'#e0bd8d'"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "transparency": {
                                        "expr": {
                                            "Literal": {
                                                "Value": "0D"
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
            "definition/pages/pages.json": {
                "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
                "pageOrder": [
                    "executive-overview",
                    "fleet-operations",
                    "customer-revenue-analytics"
                ],
                "activePageName": "executive-overview"
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
                "displayName": "FleetVision KSA"
            },
            "config": {
                "version": "2.0",
                "logicalId": "ed16d0fb-208d-5b8f-97d5-5c2393c51ccb"
            }
        },
        "definition.pbism": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
            "version": "4.0",
            "settings": {}
        },
        "definition/cultures/en-US.tmdl": "cultureInfo en-US\n\tlinguisticMetadata =\n\t\t\t{\n\t\t\t  \"Version\": \"1.0.0\",\n\t\t\t  \"Language\": \"en-US\"\n\t\t\t}\n\t\tcontentType: json\n",
        "definition/database.tmdl": "database\n\tcompatibilityLevel: 1567\n",
        "definition/expressions.tmdl": "expression FleetVisionRedshift =\n\t\tlet\n\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")\n\t\tin\n\t\t    Source\n\tlineageTag: a127a1ae-58df-5e94-8b3c-f5853b9e3f44\n\n\tannotation PBI_NavigationStepName = Navigation\n\n\tannotation PBI_ResultType = Table\n",
        "definition/model.tmdl": "model Model\n\tculture: en-US\n\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\tdiscourageImplicitMeasures\n\tsourceQueryCulture: en-US\n\n\tannotation PBI_QueryOrder = [\"Trips\", \"Drivers\", \"DriverPerformance\", \"Trucks\", \"Maintenance\", \"TruckPerformance\", \"MaintenanceByTruck\", \"Trailers\", \"Customers\", \"Loads\", \"Facilities\", \"DeliveryEvents\", \"Routes\", \"FuelPurchases\", \"SafetyIncidents\", \"FuelByTrip\", \"DeliveryByTrip\", \"SafetyByTrip\", \"Calendar\", \"TruckMap\", \"TempCalendar\", \"Parameters\"]\n\tannotation PBI_ProTooling = [\"DevMode\"]\n\nref table Trips\nref table Drivers\nref table DriverPerformance\nref table Trucks\nref table Maintenance\nref table TruckPerformance\nref table MaintenanceByTruck\nref table Trailers\nref table Customers\nref table Loads\nref table Facilities\nref table DeliveryEvents\nref table Routes\nref table FuelPurchases\nref table SafetyIncidents\nref table FuelByTrip\nref table DeliveryByTrip\nref table SafetyByTrip\nref table Calendar\nref table TruckMap\nref table TempCalendar\nref table Parameters\n\nref cultureInfo en-US\n",
        "definition/relationships.tmdl": "relationship e4431242-a315-54fb-8d0f-4ca40ea1d8ac\n\tfromColumn: Trips.driver_id\n\ttoColumn: Drivers.driver_id\n\nrelationship e94bd60a-ba44-5e9d-9d9d-54e8e7fc72b8\n\tfromColumn: DriverPerformance.driver_id\n\ttoColumn: Drivers.driver_id\n\nrelationship c966bdbd-33b5-5391-8722-ab301da110ec\n\tfromColumn: Trips.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 3382a17c-41ec-58c0-9dc6-268e467b37ec\n\tfromColumn: Maintenance.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 090fed02-c19b-52dc-9a2f-9e7bb6424ff5\n\tfromColumn: TruckPerformance.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 00760774-0afa-5dc5-a227-3bec5e31b530\n\tfromColumn: MaintenanceByTruck.truck_id\n\ttoColumn: Trucks.truck_id\n\nrelationship 5af54763-ad58-5311-a102-731b876e0079\n\tfromColumn: Trips.trailer_id\n\ttoColumn: Trailers.trailer_id\n\nrelationship 758ef9e8-e22c-5c9a-a54b-f70629f369e3\n\tfromColumn: Trips.load_id\n\ttoColumn: Loads.load_id\n\nrelationship 008548d9-a777-5478-b6d2-ccc87322420a\n\tfromColumn: FuelPurchases.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship e2834fc3-650f-5d8b-b9b1-f3f8d0db0e41\n\tfromColumn: DeliveryEvents.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 95107944-0045-5bb1-920d-6c5a4a130564\n\tfromColumn: SafetyIncidents.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 3aba2506-7628-5e52-849b-53b3d55d34b7\n\tfromColumn: FuelByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship e6821b6d-3dab-5538-8c33-f599f6ccb3be\n\tfromColumn: DeliveryByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship a00d5fe6-2cc6-50c3-910e-8561f1cfaabc\n\tfromColumn: SafetyByTrip.trip_id\n\ttoColumn: Trips.trip_id\n\nrelationship 2e86c837-0b84-5365-b1a1-921439cab523\n\tfromColumn: Loads.customer_id\n\ttoColumn: Customers.customer_id\n\nrelationship 866b89a5-0870-5faa-99c7-883cccfb3e58\n\tfromColumn: Loads.route_id\n\ttoColumn: Routes.route_id\n\nrelationship 9686f357-f377-5b44-a1b0-7499c90273e8\n\tfromColumn: DeliveryEvents.facility_id\n\ttoColumn: Facilities.facility_id\n",
        "definition/tables/Calendar.tmdl": "table Calendar\n\tlineageTag: 3e8768d4-2c5d-519b-a88b-9a72ddeafd79\n\n\tcolumn DispatchDate\n\t\tdataType: dateTime\n\t\tlineageTag: 384a1023-b3ac-5475-83c0-2919eaba147c\n\t\tsummarizeBy: none\n\t\tsourceColumn: DispatchDate\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarYear\n\t\tdataType: int64\n\t\tlineageTag: d6ee7cf6-bb79-55e2-83a1-4d5300e381b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarYear\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarQuarter\n\t\tdataType: string\n\t\tlineageTag: e7b59f15-82da-5553-b2f6-cc80d8adcba1\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarQuarter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonth\n\t\tdataType: double\n\t\tlineageTag: 35c59a6b-12fe-5d37-ae03-8cedef6fcd9f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarMonth\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonthYear\n\t\tdataType: int64\n\t\tlineageTag: c0e70147-64b5-5bfe-88b2-ec25cc1e77cd\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarMonthYear\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarMonthStart\n\t\tdataType: dateTime\n\t\tlineageTag: 8a16538b-80e4-5cb1-b3bb-6694129064f0\n\t\tsummarizeBy: none\n\t\tsourceColumn: CalendarMonthStart\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarWeek\n\t\tdataType: double\n\t\tlineageTag: 36aeaadc-3b48-53be-82c6-e7c49d844dbc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarWeek\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarWeekDay\n\t\tdataType: double\n\t\tlineageTag: 3bd941a2-d151-5d89-a65e-b934854a9f33\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarWeekDay\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CalendarDay\n\t\tdataType: double\n\t\tlineageTag: f4dfdae1-326c-5b35-930f-9fbf11c50547\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CalendarDay\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Calendar = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    StartDate = #date(2020, 1, 1),\n\t\t\t\t    EndDate = #date(2026, 12, 31),\n\t\t\t\t    NumberOfDays = Duration.Days(EndDate - StartDate) + 1,\n\t\t\t\t    DateList = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0)),\n\t\t\t\t    #\"Converted to Table\" = Table.FromList(DateList, Splitter.SplitByNothing(), {\"DispatchDate\"}, null, ExtraValues.Error),\n\t\t\t\t    #\"Changed Type\" = Table.TransformColumnTypes(#\"Converted to Table\", {{\"DispatchDate\", type date}}),\n\t\t\t\t    #\"Added CalendarYear\" = Table.AddColumn(#\"Changed Type\", \"CalendarYear\", each Date.Year([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarQuarter\" = Table.AddColumn(#\"Added CalendarYear\", \"CalendarQuarter\", each \"Q\" & Text.From(Date.QuarterOfYear([DispatchDate])), type text),\n\t\t\t\t    #\"Added CalendarMonth\" = Table.AddColumn(#\"Added CalendarQuarter\", \"CalendarMonth\", each Date.Month([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarMonthYear\" = Table.AddColumn(#\"Added CalendarMonth\", \"CalendarMonthYear\", each Date.ToText([DispatchDate], \"MMM yyyy\"), type text),\n\t\t\t\t    #\"Added CalendarMonthStart\" = Table.AddColumn(#\"Added CalendarMonthYear\", \"CalendarMonthStart\", each Date.StartOfMonth([DispatchDate]), type date),\n\t\t\t\t    #\"Added CalendarWeek\" = Table.AddColumn(#\"Added CalendarMonthStart\", \"CalendarWeek\", each Date.WeekOfYear([DispatchDate]), Int64.Type),\n\t\t\t\t    #\"Added CalendarWeekDay\" = Table.AddColumn(#\"Added CalendarWeek\", \"CalendarWeekDay\", each Date.DayOfWeekName([DispatchDate]), type text),\n\t\t\t\t    #\"Added CalendarDay\" = Table.AddColumn(#\"Added CalendarWeekDay\", \"CalendarDay\", each Date.Day([DispatchDate]), Int64.Type)\n\t\t\t\tin\n\t\t\t\t    #\"Added CalendarDay\"\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Customers.tmdl": "table Customers\n\tlineageTag: 38a9d5ed-6ca7-5ecb-8256-fc65bb46a03e\n\n\tmeasure 'Total Customers' = DISTINCTCOUNT('Customers'[customer_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 0902181d-1af0-50ef-8642-3b06b993e9f3\n\n\tcolumn customer_id\n\t\tdataType: string\n\t\tlineageTag: 3fb9a87c-1881-581d-a4ca-aa8d50ffbc83\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn customer_name\n\t\tdataType: string\n\t\tlineageTag: 710a38c7-6aa4-56b8-962c-c9b538f8b4a8\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn customer_type\n\t\tdataType: string\n\t\tlineageTag: e3f78ab5-00b6-5059-91c8-bcd16616c466\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn credit_terms_days\n\t\tdataType: double\n\t\tlineageTag: 6539a2f5-9455-5a2d-ae3f-1371438ee7af\n\t\tsummarizeBy: sum\n\t\tsourceColumn: credit_terms_days\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn primary_freight_type\n\t\tdataType: string\n\t\tlineageTag: 50ec5661-1be8-5744-8901-5e6496adca60\n\t\tsummarizeBy: none\n\t\tsourceColumn: primary_freight_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn account_status\n\t\tdataType: string\n\t\tlineageTag: 6c0a054a-3b09-59a4-bbb5-67aa33132010\n\t\tsummarizeBy: none\n\t\tsourceColumn: account_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn contract_start_date\n\t\tdataType: dateTime\n\t\tlineageTag: 6339cc9c-bb4e-5d95-9051-8df23c70e46a\n\t\tsummarizeBy: none\n\t\tsourceColumn: contract_start_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn annual_revenue_potential\n\t\tdataType: double\n\t\tlineageTag: 3c2ae234-c1c7-5e20-b644-1e03f1081517\n\t\tsummarizeBy: sum\n\t\tsourceColumn: annual_revenue_potential\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Customers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.customers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/DeliveryByTrip.tmdl": "table DeliveryByTrip\n\tlineageTag: 8467d34e-5c38-5c04-9b84-ada65dd67f05\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 1e9201d6-2ceb-5873-a19b-afc1d95b073c\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DeliveryEvents\n\t\tdataType: double\n\t\tlineageTag: 4ebf74f8-5423-54d5-9f39-cf91934e2320\n\t\tsummarizeBy: sum\n\t\tsourceColumn: DeliveryEvents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn OnTimeEvents = SWITCH(TRUE(), 'DeliveryByTrip'[on_time_flag], 1, 0)\n\t\tdataType: dateTime\n\t\tlineageTag: 16d2e960-c7b1-52e4-8527-0f11324b83c8\n\t\tsummarizeBy: none\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn LateEvents = SWITCH(TRUE(), 'DeliveryByTrip'[on_time_flag] = 0, 1, 0)\n\t\tdataType: double\n\t\tlineageTag: 5937a09b-82a4-54a7-b867-3512f025af6c\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn OnTimeRate = SWITCH(TRUE(), Count(DISTINCT 'DeliveryByTrip'[event_id]) > 0, Sum( If('DeliveryByTrip'[on_time_flag], 1, 0) ) / Count(DISTINCT event_id), 0)\n\t\tdataType: dateTime\n\t\tlineageTag: 8d7d28f8-bd6a-5b80-8e42-f59315501f58\n\t\tsummarizeBy: none\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalDetentionMinutes\n\t\tdataType: double\n\t\tlineageTag: 1b4d5f37-0adc-57cb-9131-bb3ebc44bf13\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalDetentionMinutes\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgDetentionMinutes\n\t\tdataType: double\n\t\tlineageTag: 3d3520f3-6ef4-5a73-9da7-884aa1bf0766\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgDetentionMinutes\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DeliveryByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = DeliveryEvents\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/DeliveryEvents.tmdl": "table DeliveryEvents\n\tlineageTag: a31b3de9-e3b3-5759-a0dd-2e97dd0eea8d\n\n\tmeasure 'On-Time Delivery %' = AVERAGE('DeliveryEvents'[on_time_flag])*100\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: fae51d1f-d8f9-5b55-99bd-a56967d5ec3d\n\n\tcolumn facility_id\n\t\tdataType: string\n\t\tlineageTag: 1d72730f-a012-591b-8eb9-423a7a53ec20\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: d01822dc-9b8a-5903-8c08-2e3235029ac6\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn event_id\n\t\tdataType: string\n\t\tlineageTag: 4bdc4e52-91af-552c-b08b-32bc059e3ad9\n\t\tsummarizeBy: none\n\t\tsourceColumn: event_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn event_type\n\t\tdataType: string\n\t\tlineageTag: 13085807-aaca-5f23-81cc-04f6447e7fe9\n\t\tsummarizeBy: none\n\t\tsourceColumn: event_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn scheduled_datetime\n\t\tdataType: dateTime\n\t\tlineageTag: 482c832f-a235-54f9-ac1b-009a261720a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: scheduled_datetime\n\t\tformatString: M/D/YYYY h:mm:ss[.fff] TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_datetime\n\t\tdataType: dateTime\n\t\tlineageTag: 03590705-13b4-5dc6-885d-a1f5ae637966\n\t\tsummarizeBy: none\n\t\tsourceColumn: actual_datetime\n\t\tformatString: M/D/YYYY h:mm:ss[.fff] TT\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn detention_minutes\n\t\tdataType: double\n\t\tlineageTag: e0ae6536-e685-504f-a3f5-6e7ae6717b9c\n\t\tsummarizeBy: sum\n\t\tsourceColumn: detention_minutes\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn on_time_flag\n\t\tdataType: string\n\t\tlineageTag: d3ca52eb-7d52-53f4-ad16-70b945ca2e19\n\t\tsummarizeBy: none\n\t\tsourceColumn: on_time_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn delivery_city\n\t\tdataType: string\n\t\tlineageTag: 4389c613-2b52-5490-81af-c783dd41d716\n\t\tsummarizeBy: none\n\t\tsourceColumn: delivery_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn delivery_state\n\t\tdataType: string\n\t\tlineageTag: ced951d9-a000-5e41-b483-647362840126\n\t\tsummarizeBy: none\n\t\tsourceColumn: delivery_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DeliveryEvents = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    event_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    event_type,\n\t\t\t\t    facility_id,\n\t\t\t\t    scheduled_datetime,\n\t\t\t\t    actual_datetime,\n\t\t\t\t    detention_minutes,\n\t\t\t\t    on_time_flag,\n\t\t\t\t    location_city     AS delivery_city,\n\t\t\t\t    location_state    AS delivery_state\n\t\t\t\t    FROM fleetvision.delivery_events\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/DriverPerformance.tmdl": "table DriverPerformance\n\tlineageTag: 45e4a570-977d-56a3-ba43-7e841ee0690b\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: 423ac404-8093-56ae-a1ae-3fd51b27ce71\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalTrips\n\t\tdataType: double\n\t\tlineageTag: 71074d0a-12be-5155-a402-d5c8f7494d29\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalTrips\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalMiles\n\t\tdataType: double\n\t\tlineageTag: ee2aca6e-5705-5d9f-b343-dfaec87438e1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalMiles\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalTripHours\n\t\tdataType: double\n\t\tlineageTag: d02e9eb5-9a8d-5eb1-9a1f-a41656414bda\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalTripHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalFuelGallons\n\t\tdataType: double\n\t\tlineageTag: 98b2f4a1-e0d8-5320-a2f7-3c5b586a27fc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalFuelGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FleetMPG\n\t\tdataType: double\n\t\tlineageTag: 4f766b95-c033-58ce-8574-cc99405efda3\n\t\tsummarizeBy: sum\n\t\tsourceColumn: FleetMPG\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgMPG\n\t\tdataType: double\n\t\tlineageTag: ca74523b-4db1-58fe-b4d1-6b4c09a65ad2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgMPG\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgIdleHours\n\t\tdataType: double\n\t\tlineageTag: dcdc5388-82cd-5894-9609-a100115039eb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgIdleHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalIdleHours\n\t\tdataType: double\n\t\tlineageTag: 1f7a1ac1-fdd6-5452-8b8f-1910ce867802\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalIdleHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition DriverPerformance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trips\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Drivers.tmdl": "table Drivers\n\tlineageTag: b5a283ed-c128-51a0-8b2d-9cee846a3a5d\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: ff7ba233-3d4c-5538-ad67-86e8724f0ce9\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn first_name\n\t\tdataType: string\n\t\tlineageTag: 59e4ef1d-b004-59f4-8272-6058164eab60\n\t\tsummarizeBy: none\n\t\tsourceColumn: first_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn last_name\n\t\tdataType: string\n\t\tlineageTag: e9e84dd3-793c-52e1-8f4b-467e8774d911\n\t\tsummarizeBy: none\n\t\tsourceColumn: last_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn hire_date\n\t\tdataType: dateTime\n\t\tlineageTag: d3648a12-76b2-52f7-8a41-36102663f4b3\n\t\tsummarizeBy: none\n\t\tsourceColumn: hire_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn termination_date\n\t\tdataType: dateTime\n\t\tlineageTag: 1e242dce-d9ef-5a26-b670-d45337a4331d\n\t\tsummarizeBy: none\n\t\tsourceColumn: termination_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn license_number\n\t\tdataType: string\n\t\tlineageTag: c766caed-61a2-5537-aad0-3324fc8fc2d9\n\t\tsummarizeBy: none\n\t\tsourceColumn: license_number\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn license_state\n\t\tdataType: string\n\t\tlineageTag: a7311415-3759-506e-bdb6-f06a089ca0a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: license_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn date_of_birth\n\t\tdataType: dateTime\n\t\tlineageTag: 993f311d-1e16-576c-b412-e72821e2feda\n\t\tsummarizeBy: none\n\t\tsourceColumn: date_of_birth\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn home_terminal\n\t\tdataType: string\n\t\tlineageTag: 68634f9f-e5ae-586b-b168-1bb3cc4a147a\n\t\tsummarizeBy: none\n\t\tsourceColumn: home_terminal\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn employment_status\n\t\tdataType: string\n\t\tlineageTag: 87c433b3-8796-59a7-9447-09400ef28c74\n\t\tsummarizeBy: none\n\t\tsourceColumn: employment_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn cdl_class\n\t\tdataType: string\n\t\tlineageTag: 7afe4b3f-44b7-57e5-80a0-c67edc7827f2\n\t\tsummarizeBy: none\n\t\tsourceColumn: cdl_class\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn years_experience\n\t\tdataType: double\n\t\tlineageTag: 85797267-21b3-574a-a017-c3c943dbf581\n\t\tsummarizeBy: sum\n\t\tsourceColumn: years_experience\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Drivers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    driver_id,\n\t\t\t\t    first_name,\n\t\t\t\t    last_name,\n\t\t\t\t    hire_date,\n\t\t\t\t    termination_date,\n\t\t\t\t    license_number,\n\t\t\t\t    license_state,\n\t\t\t\t    date_of_birth,\n\t\t\t\t    home_terminal,\n\t\t\t\t    employment_status,\n\t\t\t\t    cdl_class,\n\t\t\t\t    years_experience\n\t\t\t\t    FROM fleetvision.drivers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Facilities.tmdl": "table Facilities\n\tlineageTag: eca24c6c-83b3-5419-a289-29e6960295aa\n\n\tcolumn facility_id\n\t\tdataType: string\n\t\tlineageTag: c700d0aa-3c5c-5b30-8f4e-c99a9a385da1\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_name\n\t\tdataType: string\n\t\tlineageTag: 356ad5c7-1cd3-5977-b34e-824fd53af81f\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_name\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_type\n\t\tdataType: string\n\t\tlineageTag: 3eca9b5c-5eac-58f4-9f2c-d16582ab3dd7\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn city\n\t\tdataType: string\n\t\tlineageTag: d71be1f5-b0f6-51f2-8f7b-a549cc2ab774\n\t\tsummarizeBy: none\n\t\tsourceColumn: city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn state\n\t\tdataType: string\n\t\tlineageTag: c0842320-6428-5c14-ae71-462eb7b1b698\n\t\tsummarizeBy: none\n\t\tsourceColumn: state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn latitude\n\t\tdataType: double\n\t\tlineageTag: 10ba13ce-58c1-5dd0-ad5a-863e782c5f21\n\t\tsummarizeBy: sum\n\t\tsourceColumn: latitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn longitude\n\t\tdataType: double\n\t\tlineageTag: 6f624232-1bfb-57e6-bb68-5688203ca06f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: longitude\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn dock_doors\n\t\tdataType: double\n\t\tlineageTag: cb2ce4bf-cdd3-5827-a116-649c76c6b9e7\n\t\tsummarizeBy: sum\n\t\tsourceColumn: dock_doors\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn operating_hours\n\t\tdataType: string\n\t\tlineageTag: 085355eb-63c6-56ba-a29d-e0bcf0dcdf27\n\t\tsummarizeBy: none\n\t\tsourceColumn: operating_hours\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn longitude_latitude\n\t\tdataType: string\n\t\tlineageTag: 3168d3a5-b189-536e-b479-e1c824a26724\n\t\tsummarizeBy: none\n\t\tsourceColumn: longitude_latitude\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Facilities = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.facilities\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/FuelByTrip.tmdl": "table FuelByTrip\n\tlineageTag: 92a3a65c-e644-527c-9742-7e68c00ed86a\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 727e8482-c80b-53b1-8673-26c365074440\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn PurchasedGallons\n\t\tdataType: double\n\t\tlineageTag: 1324fdf1-26e7-5e3c-a8f4-ca515e388028\n\t\tsummarizeBy: sum\n\t\tsourceColumn: PurchasedGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalFuelCost\n\t\tdataType: double\n\t\tlineageTag: 8125f77c-fd8f-5fd0-b14b-192a0bd182e4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalFuelCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgFuelPricePerGallon\n\t\tdataType: double\n\t\tlineageTag: 19375e2e-a18e-5c24-9538-f5e5a73f7c1e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgFuelPricePerGallon\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FuelTransactions\n\t\tdataType: double\n\t\tlineageTag: 67fec475-d41c-5346-8f5a-70764ccfc656\n\t\tsummarizeBy: sum\n\t\tsourceColumn: FuelTransactions\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition FuelByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = FuelPurchases\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/FuelPurchases.tmdl": "table FuelPurchases\n\tlineageTag: 6c3a21d2-b0ad-5e6a-94f0-aac32a8bf75c\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 3597cd69-ad08-56e1-a904-b02ab6b9f14a\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_purchase_id\n\t\tdataType: string\n\t\tlineageTag: 8c848f98-012f-55a8-a40f-669e3a6eddf8\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_purchase_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn purchase_date\n\t\tdataType: dateTime\n\t\tlineageTag: 86b98a74-c808-58e0-b7b2-ea8b715eac1b\n\t\tsummarizeBy: none\n\t\tsourceColumn: purchase_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_city\n\t\tdataType: string\n\t\tlineageTag: 5062cd58-fc08-5929-96f4-5d507e73d51d\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_state\n\t\tdataType: string\n\t\tlineageTag: 1ee79352-50e2-5aa3-81d0-26ae2b94df18\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn gallons\n\t\tdataType: double\n\t\tlineageTag: 093543c3-cc92-5ed8-9c34-51b52ceb0367\n\t\tsummarizeBy: sum\n\t\tsourceColumn: gallons\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn price_per_gallon\n\t\tdataType: double\n\t\tlineageTag: 44016af0-05fd-56a4-b01b-e9526d6ad4fb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: price_per_gallon\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_total_cost\n\t\tdataType: double\n\t\tlineageTag: b42d4880-553f-5dd1-9ba8-6876d0b1730e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_total_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_card_number\n\t\tdataType: string\n\t\tlineageTag: 2fb4b2c9-14b3-50b7-acd0-84a39588d6ea\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_card_number\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition FuelPurchases = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    fuel_purchase_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    purchase_date,\n\t\t\t\t    location_city     AS fuel_city,\n\t\t\t\t    location_state    AS fuel_state,\n\t\t\t\t    gallons,\n\t\t\t\t    price_per_gallon,\n\t\t\t\t    total_cost        AS fuel_total_cost,\n\t\t\t\t    fuel_card_number\n\t\t\t\t    FROM fleetvision.fuel_purchases\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Loads.tmdl": "table Loads\n\tlineageTag: 13e30a87-fa1f-5fb1-a4d4-f18fb28b9558\n\n\tmeasure 'Total Revenue' = DIVIDE(SUM('Loads'[revenue]), 1000000, 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 91098b09-6315-5012-8cb4-76e719439999\n\n\tmeasure 'Customer Analytics' = MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5a444008-2977-58aa-8afd-9a301f70d1f2\n\n\tmeasure 'Highest Revenue by Customer' = MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 1b63a406-2922-5cb0-9dcf-d471af1453d0\n\n\tmeasure 'Average Revenue per Load' = AVERAGE('Loads'[revenue])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: ec7cf70c-2291-5cbb-9d68-2b9728cb6e1a\n\n\tmeasure 'High Value Revenue' = CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 9e0aa5db-e86e-5f58-b721-d6dbdd9858ce\n\n\tmeasure 'Average Revenue per Customer' = DIVIDE(SUM('Loads'[revenue]), DISTINCTCOUNT('Customers'[customer_id]), 0)\n\t\tformatString: \"$#,##0\"\n\t\tlineageTag: 290c931b-09a5-5f54-b1d3-6d67170e6f7f\n\n\tmeasure 'Driver Analytics' = AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e05a035d-85ce-5856-a036-1afbc7f0beb3\n\n\tmeasure 'High Value Revenue %' = DIVIDE(CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\"), SUM('Loads'[revenue]), 0)\n\t\tformatString: \"0.0%\"\n\t\tlineageTag: d15eab55-18f2-558a-b3d8-3f6bde57dfa6\n\n\tmeasure 'Revenue per Mile' = DIVIDE(SUM('Loads'[revenue]), SUM('Trips'[actual_distance_miles]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 6a7f8c9d-ae59-5350-b000-d2098e25e5dd\n\n\tmeasure 'Revenue per Trip' = DIVIDE(SUM('Loads'[revenue]), COUNT('Trips'[trip_id]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: be478467-bb36-5135-92b2-1280a432b523\n\n\tmeasure 'Average Revenue per Driver' = AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: b48816ec-1244-5c22-ae05-174fd572bc6d\n\n\tmeasure 'High Value Loads' = CALCULATE(DISTINCTCOUNT('Trips'[load_id]), 'Loads'[RevenueBand] = \"High Value\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 941ed71d-c9cd-5bf8-9c14-71585bf98f31\n\n\tmeasure 'Revenue %' = DIVIDE(SUM('Loads'[revenue]), CALCULATE(SUM('Loads'[revenue]), ALLSELECTED()), 0)\n\t\tformatString: \"0.0%\"\n\t\tlineageTag: f72e061a-527b-5da5-a953-892acb27092f\n\n\tmeasure 'Total Loads' = COUNT('Trips'[load_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: dc568f16-f764-5701-bf95-6f1a21fe4d5b\n\n\tcolumn customer_id\n\t\tdataType: string\n\t\tlineageTag: f9aee854-a44e-583e-911e-b0a3c8d6d728\n\t\tsummarizeBy: none\n\t\tsourceColumn: customer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn route_id\n\t\tdataType: string\n\t\tlineageTag: fac49772-56f1-52a7-8521-e03aecf65481\n\t\tsummarizeBy: none\n\t\tsourceColumn: route_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_id\n\t\tdataType: string\n\t\tlineageTag: d5e9dbe9-70ec-549f-93d4-88c964aeb994\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_date\n\t\tdataType: dateTime\n\t\tlineageTag: d015f215-d74d-5b4c-b75a-6f60e9adb897\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_type\n\t\tdataType: string\n\t\tlineageTag: cec011a4-0571-5301-8667-00e470144aa6\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn weight_lbs\n\t\tdataType: double\n\t\tlineageTag: d4d0b472-c8a2-5abf-973c-08da760a4765\n\t\tsummarizeBy: sum\n\t\tsourceColumn: weight_lbs\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn pieces\n\t\tdataType: double\n\t\tlineageTag: 115c40fc-1695-5395-b1b3-cdcc5666e45a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: pieces\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn revenue\n\t\tdataType: double\n\t\tlineageTag: 1a41650e-0a8c-5cf9-af7f-beec7d3c1c04\n\t\tsummarizeBy: sum\n\t\tsourceColumn: revenue\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_surcharge\n\t\tdataType: double\n\t\tlineageTag: e2f4d3bd-bea8-5a0e-a66d-66cd37ffbacc\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_surcharge\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn accessorial_charges\n\t\tdataType: double\n\t\tlineageTag: e3933416-af83-51f9-b7e5-298adeabebbe\n\t\tsummarizeBy: sum\n\t\tsourceColumn: accessorial_charges\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_status\n\t\tdataType: string\n\t\tlineageTag: 53352867-8cc2-5877-a19e-b8709cc9ca7a\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn booking_type\n\t\tdataType: string\n\t\tlineageTag: d9ae0f6b-f9f8-5906-9d00-94110a53d571\n\t\tsummarizeBy: none\n\t\tsourceColumn: booking_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn RevenueBand = SWITCH(TRUE(), 'Loads'[revenue] >= 6000, \"High Value\", 'Loads'[revenue] >= 3000, \"Medium Value\", \"Low Value\")\n\t\tdataType: string\n\t\tlineageTag: 543f6047-0955-5329-ac40-4210c3bc9133\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Loads = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"customer_id\", \"route_id\", \"load_id\", \"load_date\", \"load_type\", \"weight_lbs\", \"pieces\", \"revenue\", \"fuel_surcharge\", \"accessorial_charges\", \"load_status\", \"booking_type\", \"RevenueBand\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/Maintenance.tmdl": "table Maintenance\n\tlineageTag: c75bd5d7-e55c-54a1-989f-8feb4433992f\n\n\tmeasure 'Total Maintainane Cost' = SUM('Maintenance'[maintenance_total_cost])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 77f41ac7-0c8c-5611-814a-bcf9899d6369\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 32ec1da0-6836-5507-b254-e5039c74718e\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_id\n\t\tdataType: string\n\t\tlineageTag: ce9ec557-f02e-54e9-bfaf-1e2f665df756\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_date\n\t\tdataType: dateTime\n\t\tlineageTag: 6a4d1d20-7f1f-5992-a2a9-c9769c0a942a\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_type\n\t\tdataType: string\n\t\tlineageTag: 847e0af4-af79-5c6f-9e03-017e18101046\n\t\tsummarizeBy: none\n\t\tsourceColumn: maintenance_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn odometer_reading\n\t\tdataType: double\n\t\tlineageTag: 038241d8-57a1-5fe4-8963-c17fba582206\n\t\tsummarizeBy: sum\n\t\tsourceColumn: odometer_reading\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn labor_hours\n\t\tdataType: double\n\t\tlineageTag: 962b58e9-c61c-5310-ab3f-312ac4120d0d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: labor_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn labor_cost\n\t\tdataType: double\n\t\tlineageTag: fc70b322-2558-511b-a173-73a365cdf9c6\n\t\tsummarizeBy: sum\n\t\tsourceColumn: labor_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn parts_cost\n\t\tdataType: double\n\t\tlineageTag: b6fdd733-557f-56d7-b740-904ce21870a2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: parts_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn maintenance_total_cost\n\t\tdataType: double\n\t\tlineageTag: 924a75f8-0942-59ef-8e8f-782e29a6ab05\n\t\tsummarizeBy: sum\n\t\tsourceColumn: maintenance_total_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn facility_location\n\t\tdataType: string\n\t\tlineageTag: 645ee12b-a4ff-5335-bb8d-6e5e0efb828e\n\t\tsummarizeBy: none\n\t\tsourceColumn: facility_location\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn downtime_hours\n\t\tdataType: double\n\t\tlineageTag: a62f3bf5-3362-592f-998e-62deeb89abe1\n\t\tsummarizeBy: sum\n\t\tsourceColumn: downtime_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn service_description\n\t\tdataType: string\n\t\tlineageTag: 8dd9cbf6-f21f-51c4-a5bf-899956e18384\n\t\tsummarizeBy: none\n\t\tsourceColumn: service_description\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Maintenance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    maintenance_id,\n\t\t\t\t    truck_id,\n\t\t\t\t    maintenance_date,\n\t\t\t\t    maintenance_type,\n\t\t\t\t    odometer_reading,\n\t\t\t\t    labor_hours,\n\t\t\t\t    labor_cost,\n\t\t\t\t    parts_cost,\n\t\t\t\t    total_cost        AS maintenance_total_cost,\n\t\t\t\t    facility_location,\n\t\t\t\t    downtime_hours,\n\t\t\t\t    service_description\n\t\t\t\t    FROM fleetvision.maintenance_records\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/MaintenanceByTruck.tmdl": "table MaintenanceByTruck\n\tlineageTag: b25cf30f-944f-5acb-867f-2865adb4cad0\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 10c23d76-c733-59e6-8256-977e303922c3\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MaintenanceEvents\n\t\tdataType: double\n\t\tlineageTag: 777b6bbb-c10c-5996-bca2-26c6b54ac5a8\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MaintenanceEvents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalMaintenanceCost\n\t\tdataType: double\n\t\tlineageTag: abd1a5e4-802f-5767-8c38-e97a37b62b1c\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalMaintenanceCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalDowntimeHours\n\t\tdataType: dateTime\n\t\tlineageTag: c5e3d8d6-68a4-55da-896d-bf5411232e9a\n\t\tsummarizeBy: none\n\t\tsourceColumn: TotalDowntimeHours\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgDowntimeHours\n\t\tdataType: double\n\t\tlineageTag: c2847ac1-7ea9-5e8d-bf20-574fac218614\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgDowntimeHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalLaborCost\n\t\tdataType: double\n\t\tlineageTag: c3c4b815-fafb-550f-9320-6d6239736fbe\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalLaborCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TotalPartsCost\n\t\tdataType: double\n\t\tlineageTag: 11c3f4d4-e75c-5175-8e97-28332ad62a7e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TotalPartsCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AvgLaborHours\n\t\tdataType: double\n\t\tlineageTag: 19e11044-a6f7-51b4-8034-5d6237d7da7d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AvgLaborHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition MaintenanceByTruck = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Maintenance\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Parameters.tmdl": "table Parameters\n\tlineageTag: 0fe49ea5-fe5c-5a45-9ff7-e50b75dc067a\n\n\tcolumn Parameter\n\t\tdataType: string\n\t\tlineageTag: 22a0bd0b-9463-5b42-9a2d-5cfbd1cf63df\n\t\tsummarizeBy: none\n\t\tsourceColumn: Parameter\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Value\n\t\tdataType: string\n\t\tlineageTag: 70b4627b-915e-51c1-9f8a-945f135294b6\n\t\tsummarizeBy: none\n\t\tsourceColumn: Value\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Label\n\t\tdataType: string\n\t\tlineageTag: 5946bfca-d13d-5640-80d8-f86e9e9334a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: Label\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn Order\n\t\tdataType: int64\n\t\tlineageTag: 3a397789-8015-5220-bf8f-5696fa2e68c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: Order\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Parameters = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table(\n\t\t\t\t        type table [Parameter = text, Value = text, Label = text, #\"Order\" = Int64.Type],\n\t\t\t\t        {\n\t\t\t            {\"MoneyThousandSep\", \",\", \"MoneyThousandSep\", 1},\n\t\t\t            {\"ThousandSep\", \",\", \"ThousandSep\", 2},\n\t\t\t            {\"MoneyFormat\", \"$ ###0.00;-$ ###0.00\", \"MoneyFormat\", 3},\n\t\t\t            {\"TimeFormat\", \"h:mm:ss TT\", \"TimeFormat\", 4},\n\t\t\t            {\"BrokenWeeks\", \"1\", \"BrokenWeeks\", 5},\n\t\t\t            {\"CreateSearchIndexOnReload\", \"1\", \"CreateSearchIndexOnReload\", 6},\n\t\t\t            {\"MonthNames\", \"Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec\", \"MonthNames\", 7},\n\t\t\t            {\"LongDayNames\", \"Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday\", \"LongDayNames\", 8},\n\t\t\t            {\"ScriptErrorCount\", \"0\", \"ScriptErrorCount\", 9},\n\t\t\t            {\"DateFormat\", \"M/D/YYYY\", \"DateFormat\", 10},\n\t\t\t            {\"ReferenceDay\", \"0\", \"ReferenceDay\", 11},\n\t\t\t            {\"FirstMonthOfYear\", \"1\", \"FirstMonthOfYear\", 12},\n\t\t\t            {\"ErrorMode\", \"1\", \"ErrorMode\", 13},\n\t\t\t            {\"StripComments\", \"1\", \"StripComments\", 14},\n\t\t\t            {\"OpenUrlTimeout\", \"86400\", \"OpenUrlTimeout\", 15},\n\t\t\t            {\"DecimalSep\", \".\", \"DecimalSep\", 16},\n\t\t\t            {\"TimestampFormat\", \"M/D/YYYY h:mm:ss[.fff] TT\", \"TimestampFormat\", 17},\n\t\t\t            {\"FirstWeekDay\", \"6\", \"FirstWeekDay\", 18},\n\t\t\t            {\"CollationLocale\", \"en-US\", \"CollationLocale\", 19},\n\t\t\t            {\"LongMonthNames\", \"January;February;March;April;May;June;July;August;September;October;November;December\", \"LongMonthNames\", 20},\n\t\t\t            {\"DayNames\", \"Mon;Tue;Wed;Thu;Fri;Sat;Sun\", \"DayNames\", 21},\n\t\t\t            {\"NumericalAbbreviation\", \"3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y\", \"NumericalAbbreviation\", 22},\n\t\t\t            {\"MoneyDecimalSep\", \".\", \"MoneyDecimalSep\", 23},\n\t\t\t            {\"vMinDate\", \"44562\", \"vMinDate\", 24},\n\t\t\t            {\"vMaxDate\", \"45657\", \"vMaxDate\", 25},\n\t\t\t            {\"vTopN\", \"10\", \"Number of top customers to display\", 26},\n\t\t\t            {\"vMeasure\", \"1\", \"Dynamic measure for chart analysis\", 27}\n\t\t\t\t        }\n\t\t\t\t    )\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Routes.tmdl": "table Routes\n\tlineageTag: 93f37141-d3c2-56bb-b0a2-4b0103dc7a39\n\n\tcolumn route_id\n\t\tdataType: string\n\t\tlineageTag: 9253f750-0daf-541e-a41e-f3a85786e891\n\t\tsummarizeBy: none\n\t\tsourceColumn: route_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn origin_city\n\t\tdataType: string\n\t\tlineageTag: b0a4338f-646b-5168-9396-8c7ab6e1e4c9\n\t\tsummarizeBy: none\n\t\tsourceColumn: origin_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn origin_state\n\t\tdataType: string\n\t\tlineageTag: ec33afe8-f83d-5f0b-a89a-5a019ac8a7e0\n\t\tsummarizeBy: none\n\t\tsourceColumn: origin_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn destination_city\n\t\tdataType: string\n\t\tlineageTag: 3d111ce7-9772-5c85-8695-e1eee9b231f3\n\t\tsummarizeBy: none\n\t\tsourceColumn: destination_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn destination_state\n\t\tdataType: string\n\t\tlineageTag: ba882fe1-8ab5-56df-862a-196b0c49407c\n\t\tsummarizeBy: none\n\t\tsourceColumn: destination_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn typical_distance_miles\n\t\tdataType: double\n\t\tlineageTag: dabf4cb2-3268-5938-a8c0-ab380f252996\n\t\tsummarizeBy: sum\n\t\tsourceColumn: typical_distance_miles\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn base_rate_per_mile\n\t\tdataType: double\n\t\tlineageTag: 605fcf2e-c734-5400-bd98-d45148bd7781\n\t\tsummarizeBy: sum\n\t\tsourceColumn: base_rate_per_mile\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_surcharge_rate\n\t\tdataType: double\n\t\tlineageTag: 033fed09-6dd1-535b-b5e9-606d0a9fed9f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_surcharge_rate\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn typical_transit_days\n\t\tdataType: double\n\t\tlineageTag: 6f23b6f1-12ca-5959-810f-624b91b019cf\n\t\tsummarizeBy: sum\n\t\tsourceColumn: typical_transit_days\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Routes = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT *\n\t\t\t\t    FROM fleetvision.routes\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/SafetyByTrip.tmdl": "table SafetyByTrip\n\tlineageTag: aa58eacf-4c38-56da-b2a4-32a0492f9137\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: e5ef2bce-9187-5407-8570-b00e059eb4e0\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn SafetyIncidents\n\t\tdataType: double\n\t\tlineageTag: d731dbe6-39d5-555d-8038-75043b044cf6\n\t\tsummarizeBy: sum\n\t\tsourceColumn: SafetyIncidents\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn PreventableIncidents\n\t\tdataType: double\n\t\tlineageTag: c3fc69af-3b1c-5ac5-880b-89e3b917e39e\n\t\tsummarizeBy: sum\n\t\tsourceColumn: PreventableIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn InjuryIncidents\n\t\tdataType: double\n\t\tlineageTag: 4635d220-b341-5fc2-901a-9e8f9bac6e42\n\t\tsummarizeBy: sum\n\t\tsourceColumn: InjuryIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn AtFaultIncidents\n\t\tdataType: double\n\t\tlineageTag: c02b0008-05aa-556f-996c-5bb0de59ed13\n\t\tsummarizeBy: sum\n\t\tsourceColumn: AtFaultIncidents\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn VehicleDamageCost\n\t\tdataType: double\n\t\tlineageTag: dceec3bc-c146-5c4e-9ced-aa6bc728f9be\n\t\tsummarizeBy: sum\n\t\tsourceColumn: VehicleDamageCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn CargoDamageCost\n\t\tdataType: double\n\t\tlineageTag: bf16af75-143b-539f-977e-65d73e977b5a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: CargoDamageCost\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn ClaimAmount\n\t\tdataType: double\n\t\tlineageTag: e49b00b3-7f3b-59f0-a985-84df8cc7bcf4\n\t\tsummarizeBy: sum\n\t\tsourceColumn: ClaimAmount\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition SafetyByTrip = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = SafetyIncidents\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/SafetyIncidents.tmdl": "table SafetyIncidents\n\tlineageTag: 88a98507-fbbe-56a6-a39e-af2a849e26e2\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: a89c8ced-7a7d-5ae2-9f34-fb17d593789a\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_id\n\t\tdataType: string\n\t\tlineageTag: d05f6c85-8144-54a2-8913-785108e0b87f\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_date\n\t\tdataType: dateTime\n\t\tlineageTag: 3940a4eb-c4af-5d7d-b179-4dbbb54cce4e\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_type\n\t\tdataType: string\n\t\tlineageTag: 35cef020-ecb0-5ce9-97be-b6d0b67ce2ef\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_city\n\t\tdataType: string\n\t\tlineageTag: b89c2e58-5b6a-5878-af24-00365499082e\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_city\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn incident_state\n\t\tdataType: string\n\t\tlineageTag: b506cee5-77d0-597d-bef5-e3fe1594bd05\n\t\tsummarizeBy: none\n\t\tsourceColumn: incident_state\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn at_fault_flag\n\t\tdataType: string\n\t\tlineageTag: 4a3bc60b-49f5-5d8f-a8d7-221422c729df\n\t\tsummarizeBy: none\n\t\tsourceColumn: at_fault_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn injury_flag\n\t\tdataType: string\n\t\tlineageTag: d33ab9b7-cede-542b-8b3c-05a9a7a6c83b\n\t\tsummarizeBy: none\n\t\tsourceColumn: injury_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn vehicle_damage_cost\n\t\tdataType: double\n\t\tlineageTag: 28fe3887-f05b-51b8-841f-d268204c9874\n\t\tsummarizeBy: sum\n\t\tsourceColumn: vehicle_damage_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn cargo_damage_cost\n\t\tdataType: double\n\t\tlineageTag: daa92f9c-c5b3-5115-8ce8-1a56cbe6aa6d\n\t\tsummarizeBy: sum\n\t\tsourceColumn: cargo_damage_cost\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn claim_amount\n\t\tdataType: double\n\t\tlineageTag: 3860c0c0-6df4-531d-a92b-da1716e1af52\n\t\tsummarizeBy: sum\n\t\tsourceColumn: claim_amount\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn preventable_flag\n\t\tdataType: string\n\t\tlineageTag: 3650567e-08b6-5b69-9d0d-1b9db866e48f\n\t\tsummarizeBy: none\n\t\tsourceColumn: preventable_flag\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn description\n\t\tdataType: string\n\t\tlineageTag: 833a5045-e9b0-5c64-979f-ecec0033d570\n\t\tsummarizeBy: none\n\t\tsourceColumn: description\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition SafetyIncidents = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    incident_id,\n\t\t\t\t    trip_id,\n\t\t\t\t    incident_date,\n\t\t\t\t    incident_type,\n\t\t\t\t    location_city         AS incident_city,\n\t\t\t\t    location_state        AS incident_state,\n\t\t\t\t    at_fault_flag,\n\t\t\t\t    injury_flag,\n\t\t\t\t    vehicle_damage_cost,\n\t\t\t\t    cargo_damage_cost,\n\t\t\t\t    claim_amount,\n\t\t\t\t    preventable_flag,\n\t\t\t\t    description\n\t\t\t\t    FROM fleetvision.safety_incidents\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/TempCalendar.tmdl": "table TempCalendar\n\tlineageTag: 5e0cd0f0-e0ba-57de-8846-e7ae4705b534\n\n\tcolumn MinDate\n\t\tdataType: double\n\t\tlineageTag: 684b2574-4b39-53f6-93bb-0271715bf31f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MinDate\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MaxDate\n\t\tdataType: double\n\t\tlineageTag: 22d091f3-9138-5e68-8cdf-d6b4c35c21f3\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MaxDate\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TempCalendar = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"MinDate\", \"MaxDate\"}, {{#date(2020, 1, 1), #date(2026, 12, 31)}})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Trailers.tmdl": "table Trailers\n\tlineageTag: 1b47d346-6321-5afa-aecf-d2d29ece3614\n\n\tmeasure 'Active Trailers' = CALCULATE(DISTINCTCOUNT('Trips'[trailer_id]), 'Trailers'[trailer_status] = \"Active\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: efd511ba-959e-5b93-8c68-f84eb5915b8d\n\n\tcolumn trailer_id\n\t\tdataType: string\n\t\tlineageTag: 0183f130-8708-55df-85c5-260e1c85c1fa\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_number\n\t\tdataType: double\n\t\tlineageTag: 414a5015-4ca9-5eef-8025-1b59c240838a\n\t\tsummarizeBy: sum\n\t\tsourceColumn: trailer_number\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_type\n\t\tdataType: string\n\t\tlineageTag: 5004a82c-bd7b-53ca-a7a6-cc23f755e368\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn length_feet\n\t\tdataType: double\n\t\tlineageTag: aef9fab4-4d68-59fc-adee-ceb211777735\n\t\tsummarizeBy: sum\n\t\tsourceColumn: length_feet\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_model_year\n\t\tdataType: int64\n\t\tlineageTag: b919d6f3-e2c0-59e6-8c9c-a6ca2ecaed93\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_model_year\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_vin\n\t\tdataType: string\n\t\tlineageTag: b9a6765b-089e-5e6d-935d-1d7f02737803\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_vin\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_acquisition_date\n\t\tdataType: dateTime\n\t\tlineageTag: 1e9b71af-bd39-561d-84b4-767fcf183f17\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_acquisition_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_status\n\t\tdataType: string\n\t\tlineageTag: 68e0f56d-685b-585a-9d28-68836c73c1e6\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn current_location\n\t\tdataType: string\n\t\tlineageTag: f5953b51-85ea-5dcb-82d0-975122fd0da7\n\t\tsummarizeBy: none\n\t\tsourceColumn: current_location\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trailers = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    trailer_id,\n\t\t\t\t    trailer_number,\n\t\t\t\t    trailer_type,\n\t\t\t\t    length_feet,\n\t\t\t\t    model_year            AS trailer_model_year,\n\t\t\t\t    vin                   AS trailer_vin,\n\t\t\t\t    acquisition_date      AS trailer_acquisition_date,\n\t\t\t\t    status                AS trailer_status,\n\t\t\t\t    current_location\n\t\t\t\t    FROM fleetvision.trailers\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/Trips.tmdl": "table Trips\n\tlineageTag: 3b0e1031-f748-5307-97a6-2f8653b800cd\n\n\tmeasure 'Maximum Trips by Truck' = MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 8dbb9c27-3953-55a5-b794-ee73660ad1b0\n\n\tmeasure 'Average Trip Distance' = AVERAGE('Trips'[actual_distance_miles])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e35b7be9-e127-541f-ad6a-bc4af4bb08cc\n\n\tmeasure 'Average Trip Duration' = AVERAGE('Trips'[actual_duration_hours])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 02209d34-c0d5-5a0b-b601-dbd7d263f297\n\n\tmeasure 'Total Trips' = COUNT('Trips'[trip_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: ea0647f4-bb8e-5695-81ab-ea36102811b3\n\n\tmeasure 'Total Drivers' = DISTINCTCOUNT('Trips'[driver_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 68a17c3b-ad04-50fc-b2ce-020ad3d1aa60\n\n\tmeasure 'Completed Trips' = CALCULATE(COUNT('Trips'[trip_id]), 'Trips'[trip_status] = \"Completed\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: d2d76ee4-575e-578f-bce6-66873c2a5729\n\n\tmeasure 'Completed Trip Revenue' = CALCULATE(SUM('Loads'[revenue]), 'Trips'[trip_status] = \"Completed\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 86eaa52e-08bb-55ec-abcb-003200199e96\n\n\tmeasure 'Average Fuel Efficiency' = DIVIDE(SUM('Trips'[actual_distance_miles]), SUM('Trips'[fuel_gallons_used]), 0)\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: e65eef8f-660c-5c9d-a653-c6f0286b46d3\n\n\tmeasure 'Fleet Operations' = MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 2ef29338-e4c0-5eed-a44e-0f4e6a6cc9aa\n\n\tmeasure 'Fleet Size' = DISTINCTCOUNT('Trips'[truck_id])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 15746ebf-8cf3-5cb4-aa70-041d190332e4\n\n\tmeasure 'Total Revenue Trips' = SUM('Loads'[revenue])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: f7d01dcf-3507-5017-a4e6-e11c2c850871\n\n\tmeasure 'Avg(idle_time_hours)' = AVERAGE('Trips'[idle_time_hours])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 006dce75-05d3-57ff-9787-b106c34baf73\n\n\tmeasure 'Avg(actual_distance_miles)' = AVERAGE('Trips'[actual_distance_miles])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 5a97047a-bc4b-53e2-a3ee-96e38586420e\n\n\tmeasure 'Avg(average_mpg)' = AVERAGE('Trips'[average_mpg])\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: 7441cc14-eea6-5581-9600-a9ba5b5c9101\n\n\tcolumn driver_id\n\t\tdataType: string\n\t\tlineageTag: 99962d85-9cae-523b-a19e-c09fadd976ba\n\t\tsummarizeBy: none\n\t\tsourceColumn: driver_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 1338433a-4a62-55b4-a344-674a5641b340\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trailer_id\n\t\tdataType: string\n\t\tlineageTag: 801332f2-6eca-58b9-9ca0-d0c0dc2bc758\n\t\tsummarizeBy: none\n\t\tsourceColumn: trailer_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn load_id\n\t\tdataType: string\n\t\tlineageTag: 5fab398c-09f6-5896-a42d-7668e98edc81\n\t\tsummarizeBy: none\n\t\tsourceColumn: load_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_id\n\t\tdataType: string\n\t\tlineageTag: 45cb32c6-db6c-5f44-85a6-3162428e74be\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_distance_miles\n\t\tdataType: double\n\t\tlineageTag: a004a973-4cc0-54a1-b1cc-93e53f3baebd\n\t\tsummarizeBy: sum\n\t\tsourceColumn: actual_distance_miles\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn actual_duration_hours\n\t\tdataType: double\n\t\tlineageTag: adee4386-7c9e-537e-a68e-f34c676feeab\n\t\tsummarizeBy: sum\n\t\tsourceColumn: actual_duration_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_gallons_used\n\t\tdataType: double\n\t\tlineageTag: 9fd8b063-6828-516a-bf44-49ace097b0d7\n\t\tsummarizeBy: sum\n\t\tsourceColumn: fuel_gallons_used\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn average_mpg\n\t\tdataType: double\n\t\tlineageTag: f8b79f28-4d66-5115-a313-9a2d5db414a5\n\t\tsummarizeBy: sum\n\t\tsourceColumn: average_mpg\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn idle_time_hours\n\t\tdataType: double\n\t\tlineageTag: a86e4c62-3297-59ae-805f-073e8fd8c1c2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: idle_time_hours\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn trip_status\n\t\tdataType: string\n\t\tlineageTag: e04d3a7a-6952-55f9-8ce8-b847c9ce6302\n\t\tsummarizeBy: none\n\t\tsourceColumn: trip_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckNumber = RELATED('Trucks'[truck_id])\n\t\tdataType: double\n\t\tlineageTag: 39eaa460-d6dc-597f-bb14-fee3dbcee91b\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DispatchDate = 'Trips'[dispatch_date]\n\t\tdataType: dateTime\n\t\tlineageTag: 6d76169b-6ede-540e-b064-7644c8d1b3f2\n\t\tsummarizeBy: none\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripMonth = FORMAT('Trips'[dispatch_date], \"mmmm\")\n\t\tdataType: double\n\t\tlineageTag: 27aaefa0-1993-5137-a5e5-a282e2b14f17\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn LoadMonth = FORMAT('Trips'[dispatch_date], \"mmmm\")\n\t\tdataType: double\n\t\tlineageTag: 4e57d450-05ee-5b88-b844-952746d313a0\n\t\tsummarizeBy: sum\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthStartDate\n\t\tdataType: dateTime\n\t\tlineageTag: 1ca03fd6-490f-58a9-8c09-57d005442371\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthStartDate\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthYear\n\t\tdataType: int64\n\t\tlineageTag: 1fd18945-0767-5c21-b6bb-7ec4be1ca5a9\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthYear\n\t\tformatString: YYYY-MM-DD\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthSort\n\t\tdataType: dateTime\n\t\tlineageTag: 366fd966-946d-50e0-ba39-e6a81006f822\n\t\tsummarizeBy: none\n\t\tsourceColumn: MonthSort\n\t\tformatString: General Date\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripYear = YEAR('Trips'[dispatch_date])\n\t\tdataType: int64\n\t\tlineageTag: 218aba61-06ec-54fd-8602-cfb0bcd1554f\n\t\tsummarizeBy: none\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TripWeek = WEEKNUM('Trips'[dispatch_date])\n\t\tdataType: double\n\t\tlineageTag: adcb080b-6fd7-5eb1-a8e4-e387c72d0b07\n\t\tsummarizeBy: sum\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn MonthNo\n\t\tdataType: double\n\t\tlineageTag: 21d65fba-e797-59b4-a21a-449aacd3cbdb\n\t\tsummarizeBy: sum\n\t\tsourceColumn: MonthNo\n\t\tformatString: ##############\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn DistanceBand = SWITCH(TRUE(), 'Trips'[actual_distance_miles] >= 1000, \"Long Haul\", 'Trips'[actual_distance_miles] >= 500, \"Medium Haul\", \"Short Haul\")\n\t\tdataType: string\n\t\tlineageTag: b4374b2a-0eef-5fe1-817b-7637e170f0cc\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn FuelEfficiencyBand = SWITCH(TRUE(), 'Trips'[average_mpg] >= 8, \"High MPG\", 'Trips'[average_mpg] >= 6, \"Medium MPG\", \"Low MPG\")\n\t\tdataType: string\n\t\tlineageTag: 18facad7-0e7d-5994-9189-03fa7f5fedf0\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn IdleTimeBand = SWITCH(TRUE(), 'Trips'[idle_time_hours] >= 5, \"High Idle\", 'Trips'[idle_time_hours] >= 2, \"Moderate Idle\", \"Low Idle\")\n\t\tdataType: string\n\t\tlineageTag: 29d2e21b-0ecb-5b30-aa0a-d32756f84cfd\n\t\tsummarizeBy: none\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trips = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = #table({\"driver_id\", \"truck_id\", \"trailer_id\", \"load_id\", \"trip_id\", \"actual_distance_miles\", \"actual_duration_hours\", \"fuel_gallons_used\", \"average_mpg\", \"idle_time_hours\", \"trip_status\", \"TruckNumber\", \"DispatchDate\", \"TripMonth\", \"LoadMonth\", \"MonthStartDate\", \"MonthYear\", \"MonthSort\", \"TripYear\", \"TripWeek\", \"MonthNo\", \"DistanceBand\", \"FuelEfficiencyBand\", \"IdleTimeBand\"}, {})\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table",
        "definition/tables/TruckMap.tmdl": "table TruckMap\n\tlineageTag: f849a69c-f307-572a-b709-bee9c68d7ce4\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 9fcbeac3-e3d6-51a6-90c4-3b78c43bc3c5\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn unit_number\n\t\tdataType: double\n\t\tlineageTag: 707814c6-679d-50f6-9025-05bb8a6a9b91\n\t\tsummarizeBy: sum\n\t\tsourceColumn: unit_number\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TruckMap = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trucks,\n\t\t\t\t    #\"Distinct Rows\" = Table.Distinct(Source)\n\t\t\t\tin\n\t\t\t\t    #\"Distinct Rows\"\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/TruckPerformance.tmdl": "table TruckPerformance\n\tlineageTag: 465a4b13-9cea-5d82-a904-b415d908d3d7\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: 3cf0614d-07a3-5b0e-b752-263e9653ff41\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckTrips\n\t\tdataType: double\n\t\tlineageTag: a3c3519c-de0e-5eab-82e4-6aee90391607\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckTrips\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckMiles\n\t\tdataType: double\n\t\tlineageTag: 61cd7d72-c934-5d24-bcbd-4d4a7aa0a0ba\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckMiles\n\t\tformatString: #,##0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckHours\n\t\tdataType: double\n\t\tlineageTag: 4d08bd4d-6d19-51ec-a8c0-7e9949ceb3d2\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckFuelGallons\n\t\tdataType: double\n\t\tlineageTag: 8f25cb4f-f83a-56d4-a428-d3e85f6742ec\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckFuelGallons\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckMPG\n\t\tdataType: double\n\t\tlineageTag: 384ea1ed-afcf-5f6b-8f67-7a55b4596283\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckMPG\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckAvgIdleHours\n\t\tdataType: double\n\t\tlineageTag: a8769a6e-9da8-5d92-8bff-1fa222209c07\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckAvgIdleHours\n\t\tformatString: ########\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn TruckIdleHours\n\t\tdataType: double\n\t\tlineageTag: b5ec3feb-86f2-555c-8530-6f72d2c7a9fa\n\t\tsummarizeBy: sum\n\t\tsourceColumn: TruckIdleHours\n\t\tformatString: #,##0.00\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition TruckPerformance = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = Trips\n\t\t\t\tin\n\t\t\t\t    Source\n\n\tannotation PBI_ResultType = Table\n",
        "definition/tables/Trucks.tmdl": "table Trucks\n\tlineageTag: 73040672-c518-5b15-ba0c-643ceb78be53\n\n\tmeasure 'Active Trucks' = CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[truck_status] = \"Active\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: c15447ed-173b-597c-9fbd-28e01a6288cc\n\n\tmeasure 'Diesel Trucks' = CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[fuel_type] = \"Diesel\")\n\t\tformatString: \"#,##0.00\"\n\t\tlineageTag: f6f5cf4a-1ce0-556e-8a42-57c0aa05be76\n\n\tcolumn truck_id\n\t\tdataType: string\n\t\tlineageTag: b7013c61-049e-5aa8-ba0f-e722fd6b91a8\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_id\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn unit_number\n\t\tdataType: double\n\t\tlineageTag: 0e1ef306-99e3-50e5-a961-5ac3429de1ae\n\t\tsummarizeBy: sum\n\t\tsourceColumn: unit_number\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn make\n\t\tdataType: string\n\t\tlineageTag: dedc418c-722c-52e7-b7f7-d19d7d951059\n\t\tsummarizeBy: none\n\t\tsourceColumn: make\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_model_year\n\t\tdataType: int64\n\t\tlineageTag: 5a007012-c08e-5d30-8d3a-04b12852280b\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_model_year\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_vin\n\t\tdataType: string\n\t\tlineageTag: bd430b8b-5845-581e-ae1c-55b5040bd471\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_vin\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_acquisition_date\n\t\tdataType: dateTime\n\t\tlineageTag: 2e4c72cd-e481-55b7-867c-42ca2fc6fb24\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_acquisition_date\n\t\tformatString: M/D/YYYY\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn acquisition_mileage\n\t\tdataType: double\n\t\tlineageTag: 250cf308-dbe2-5b4f-8a59-47ce9e99fdf8\n\t\tsummarizeBy: sum\n\t\tsourceColumn: acquisition_mileage\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn fuel_type\n\t\tdataType: string\n\t\tlineageTag: 4cb86b0b-807b-5b29-bbd0-5187c33b2d9a\n\t\tsummarizeBy: none\n\t\tsourceColumn: fuel_type\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn tank_capacity_gallons\n\t\tdataType: double\n\t\tlineageTag: 3bf65880-7cf0-55d9-a4be-fcb8a908112f\n\t\tsummarizeBy: sum\n\t\tsourceColumn: tank_capacity_gallons\n\t\tformatString: ###0\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_status\n\t\tdataType: string\n\t\tlineageTag: 3140ac2e-3bdc-58ac-a113-fa169e3d4934\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_status\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tcolumn truck_home_terminal\n\t\tdataType: string\n\t\tlineageTag: bb3b2d4c-4c72-5a36-8a99-9af955ca22cf\n\t\tsummarizeBy: none\n\t\tsourceColumn: truck_home_terminal\n\n\t\tannotation SummarizationSetBy = Automatic\n\n\tpartition Trucks = m\n\t\tmode: import\n\t\tsource =\n\t\t\t\tlet\n\t\t\t\t    Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\"),\n\t\t\t\t    Result = Value.NativeQuery(Source, \"SELECT\n\t\t\t\t    truck_id,\n\t\t\t\t    unit_number,\n\t\t\t\t    make,\n\t\t\t\t    model_year            AS truck_model_year,\n\t\t\t\t    vin                   AS truck_vin,\n\t\t\t\t    acquisition_date      AS truck_acquisition_date,\n\t\t\t\t    acquisition_mileage,\n\t\t\t\t    fuel_type,\n\t\t\t\t    tank_capacity_gallons,\n\t\t\t\t    status                AS truck_status,\n\t\t\t\t    home_terminal         AS truck_home_terminal\n\t\t\t\t    FROM fleetvision.trucks\", null, [EnableFolding=false])\n\t\t\t\tin\n\t\t\t\t    Result\n\n\tannotation PBI_ResultType = Table"
    },
    "report": {
        ".pbi/localSettings.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/localSettings/1.0.0/schema.json"
        },
        ".platform": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
            "metadata": {
                "type": "Report",
                "displayName": "FleetVision KSA"
            },
            "config": {
                "version": "2.0",
                "logicalId": "c86a1869-774f-5eb5-ab09-cedc8cf2af56"
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
                    "path": "../FleetVision KSA.SemanticModel"
                }
            }
        },
        "definition/bookmarks/Bookmark001.bookmark.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
            "name": "Bookmark001",
            "displayName": "Fuel Efficiency",
            "explorationState": {
                "version": "1.0.0",
                "activeSection": "executive-overview",
                "sections": {
                    "executive-overview": {
                        "visualContainers": {}
                    }
                }
            }
        },
        "definition/bookmarks/Bookmark002.bookmark.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
            "name": "Bookmark002",
            "displayName": "High Value Loads",
            "explorationState": {
                "version": "1.0.0",
                "activeSection": "executive-overview",
                "sections": {
                    "executive-overview": {
                        "visualContainers": {}
                    }
                }
            }
        },
        "definition/bookmarks/Bookmark003.bookmark.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmark/1.0.0/schema.json",
            "name": "Bookmark003",
            "displayName": "Overall Operations",
            "explorationState": {
                "version": "1.0.0",
                "activeSection": "executive-overview",
                "sections": {
                    "executive-overview": {
                        "visualContainers": {}
                    }
                }
            }
        },
        "definition/bookmarks/bookmarks.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/bookmarksMetadata/1.0.0/schema.json",
            "items": [
                {
                    "name": "Bookmark001"
                },
                {
                    "name": "Bookmark002"
                },
                {
                    "name": "Bookmark003"
                }
            ]
        },
        "definition/pages/customer-revenue-analytics/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "customer-revenue-analytics",
            "displayName": "Customer & Revenue Analytics",
            "displayOption": "FitToWidth",
            "height": 1300,
            "width": 1280
        },
        "definition/pages/customer-revenue-analytics/visuals/02c7510c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "02c7510c",
            "position": {
                "x": 0,
                "y": 960,
                "width": 640,
                "height": 300,
                "z": 13,
                "tabOrder": 13
            },
            "visual": {
                "visualType": "image",
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
                                            "Value": "'Customer Analytics'"
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
        "definition/pages/customer-revenue-analytics/visuals/051cada8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "051cada8",
            "position": {
                "x": 480,
                "y": 300,
                "width": 427,
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Revenue by Booking Type'"
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
        "definition/pages/customer-revenue-analytics/visuals/103bf763/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "103bf763",
            "position": {
                "x": 533,
                "y": 0,
                "width": 213,
                "height": 120,
                "z": 2,
                "tabOrder": 2
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "High Value Loads"
                                        }
                                    },
                                    "queryRef": "Loads.High Value Loads",
                                    "nativeQueryRef": "High Value Loads"
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
                                            "Value": "'High Value Loads'"
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
        "definition/pages/customer-revenue-analytics/visuals/1c21c9d1/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "1c21c9d1",
            "position": {
                "x": 907,
                "y": 300,
                "width": 373,
                "height": 300,
                "z": 11,
                "tabOrder": 11
            },
            "visual": {
                "visualType": "donutChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "RevenueBand"
                                        }
                                    },
                                    "queryRef": "Loads.RevenueBand",
                                    "nativeQueryRef": "RevenueBand",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Loads"
                                        }
                                    },
                                    "queryRef": "Loads.Total Loads",
                                    "nativeQueryRef": "Total Loads"
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
                                            "Value": "'Load Distribution by Revenue Band'"
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
        "definition/pages/customer-revenue-analytics/visuals/21cf3e64/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "21cf3e64",
            "position": {
                "x": 320,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 8,
                "tabOrder": 8
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "MonthYear"
                                        }
                                    },
                                    "queryRef": "Trips.MonthYear",
                                    "nativeQueryRef": "MonthYear",
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
                                            "Value": "'MonthYear'"
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
        "definition/pages/customer-revenue-analytics/visuals/2c01dd2c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "2c01dd2c",
            "position": {
                "x": 0,
                "y": 600,
                "width": 1280,
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "MonthYear"
                                        }
                                    },
                                    "queryRef": "Trips.MonthYear",
                                    "nativeQueryRef": "MonthYear",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Monthly Customer Revenue Trend'"
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
        "definition/pages/customer-revenue-analytics/visuals/5ef147d0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "5ef147d0",
            "position": {
                "x": 1013,
                "y": 0,
                "width": 267,
                "height": 120,
                "z": 1,
                "tabOrder": 1
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "High Value Revenue %"
                                        }
                                    },
                                    "queryRef": "Loads.High Value Revenue %",
                                    "nativeQueryRef": "High Value Revenue %"
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
                                            "Value": "'High Value Revenue %'"
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
        "definition/pages/customer-revenue-analytics/visuals/7b210fc2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "7b210fc2",
            "position": {
                "x": 640,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 7,
                "tabOrder": 7
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "RevenueBand"
                                        }
                                    },
                                    "queryRef": "Loads.RevenueBand",
                                    "nativeQueryRef": "RevenueBand",
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
                                            "Value": "'RevenueBand'"
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
        "definition/pages/customer-revenue-analytics/visuals/881373ba/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "881373ba",
            "position": {
                "x": 640,
                "y": 960,
                "width": 640,
                "height": 300,
                "z": 14,
                "tabOrder": 14
            },
            "visual": {
                "visualType": "image",
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
                                            "Value": "'Revenue Analytics'"
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
        "definition/pages/customer-revenue-analytics/visuals/a07fbaca/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a07fbaca",
            "position": {
                "x": 960,
                "y": 120,
                "width": 320,
                "height": 180,
                "z": 6,
                "tabOrder": 6
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
                                                    "Entity": "Routes"
                                                }
                                            },
                                            "Property": "origin_city"
                                        }
                                    },
                                    "queryRef": "Routes.origin_city",
                                    "nativeQueryRef": "origin_city",
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
                                            "Value": "'Route'"
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
        "definition/pages/customer-revenue-analytics/visuals/c7e82bb2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c7e82bb2",
            "position": {
                "x": 0,
                "y": 300,
                "width": 480,
                "height": 300,
                "z": 9,
                "tabOrder": 9
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "customer_id"
                                        }
                                    },
                                    "queryRef": "Customers.customer_id",
                                    "nativeQueryRef": "customer_id",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Revenue Contribution by Customer'"
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
        "definition/pages/customer-revenue-analytics/visuals/c934b93e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c934b93e",
            "position": {
                "x": 747,
                "y": 0,
                "width": 267,
                "height": 120,
                "z": 3,
                "tabOrder": 3
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Average Revenue per Customer"
                                        }
                                    },
                                    "queryRef": "Loads.Average Revenue per Customer",
                                    "nativeQueryRef": "Average Revenue per Customer"
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
                                            "Value": "'Average Revenue per Customer'"
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
        "definition/pages/customer-revenue-analytics/visuals/d91b886b/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "d91b886b",
            "position": {
                "x": 0,
                "y": 0,
                "width": 267,
                "height": 120,
                "z": 0,
                "tabOrder": 0
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Highest Revenue by Customer"
                                        }
                                    },
                                    "queryRef": "Loads.Highest Revenue by Customer",
                                    "nativeQueryRef": "Highest Revenue by Customer"
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
                                            "Value": "'Highest Revenue by Customer'"
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
        "definition/pages/customer-revenue-analytics/visuals/df6c0c52/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "df6c0c52",
            "position": {
                "x": 267,
                "y": 0,
                "width": 267,
                "height": 120,
                "z": 4,
                "tabOrder": 4
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Completed Trip Revenue"
                                        }
                                    },
                                    "queryRef": "Trips.Completed Trip Revenue",
                                    "nativeQueryRef": "Completed Trip Revenue"
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
                                            "Value": "'Completed Trip Revenue'"
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
        "definition/pages/customer-revenue-analytics/visuals/e3b735db/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e3b735db",
            "position": {
                "x": 0,
                "y": 120,
                "width": 320,
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "customer_id"
                                        }
                                    },
                                    "queryRef": "Customers.customer_id",
                                    "nativeQueryRef": "customer_id",
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
                                            "Value": "'Customer'"
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
        "definition/pages/customer-revenue-analytics/visuals/nav00c936e5/visual.json": {
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
        "definition/pages/customer-revenue-analytics/visuals/nav01db0cd2/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav01db0cd2",
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
                                            "Value": "'Fleet Operations'"
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
                                            "Value": "'fleet-operations'"
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
                                            "Value": "'fleet-operations'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/customer-revenue-analytics/visuals/nav029abe44/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "nav029abe44",
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
                                            "Value": "'Customer & Revenue Analytics'"
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
                                            "Value": "'customer-revenue-analytics'"
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
                                            "Value": "'customer-revenue-analytics'"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "definition/pages/executive-overview/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "executive-overview",
            "displayName": "Executive Overview",
            "displayOption": "FitToWidth",
            "height": 1840,
            "width": 1280
        },
        "definition/pages/executive-overview/visuals/001df091/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "001df091",
            "position": {
                "x": 640,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 2,
                "tabOrder": 2
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "Total Customers"
                                        }
                                    },
                                    "queryRef": "Customers.Total Customers",
                                    "nativeQueryRef": "Total Customers"
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
                                            "Value": "'Total Customers'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/0f31f174/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "0f31f174",
            "position": {
                "x": 0,
                "y": 600,
                "width": 640,
                "height": 120,
                "z": 19,
                "tabOrder": 19
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
                                                    "Entity": "Parameters"
                                                }
                                            },
                                            "Property": "Label"
                                        }
                                    },
                                    "queryRef": "Parameters.Label",
                                    "nativeQueryRef": "Label",
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
                                            "Value": "'Metric'"
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
        "definition/pages/executive-overview/visuals/11a70f5c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "11a70f5c",
            "position": {
                "x": 853,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 15,
                "tabOrder": 15
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                            "Value": "'Load Month'"
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
        "definition/pages/executive-overview/visuals/4c98e4a9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "4c98e4a9",
            "position": {
                "x": 0,
                "y": 1440,
                "width": 1280,
                "height": 360,
                "z": 9,
                "tabOrder": 9
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "customer_id"
                                        }
                                    },
                                    "queryRef": "Customers.customer_id",
                                    "nativeQueryRef": "customer_id",
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
                                            "Value": "'Top Customers'"
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
        "definition/pages/executive-overview/visuals/50087210/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "50087210",
            "position": {
                "x": 0,
                "y": 540,
                "width": 640,
                "height": 60,
                "z": 20,
                "tabOrder": 20
            },
            "visual": {
                "visualType": "actionButton",
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
                                            "Value": "'Go to Fleet Opeations'"
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
                                            "Value": "'Source Sans Pro'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#0065B3'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e1dad5'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/6a4064d9/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "6a4064d9",
            "position": {
                "x": 1067,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 12,
                "tabOrder": 12
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                            "Value": "'Load Type'"
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
        "definition/pages/executive-overview/visuals/79c10c67/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "79c10c67",
            "position": {
                "x": 213,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 13,
                "tabOrder": 13
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
                                                    "Entity": "Drivers"
                                                }
                                            },
                                            "Property": "first_name"
                                        }
                                    },
                                    "queryRef": "Drivers.first_name",
                                    "nativeQueryRef": "first_name",
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
                                            "Value": "'Driver'"
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
        "definition/pages/executive-overview/visuals/864fc125/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "864fc125",
            "position": {
                "x": 427,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 16,
                "tabOrder": 16
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
                                                    "Entity": "Trucks"
                                                }
                                            },
                                            "Property": "truck_model_year"
                                        }
                                    },
                                    "queryRef": "Trucks.truck_model_year",
                                    "nativeQueryRef": "truck_model_year",
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
                                            "Value": "'Truck'"
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
        "definition/pages/executive-overview/visuals/90ee1b00/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "90ee1b00",
            "position": {
                "x": 640,
                "y": 720,
                "width": 640,
                "height": 360,
                "z": 6,
                "tabOrder": 6
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "customer_id"
                                        }
                                    },
                                    "queryRef": "Customers.customer_id",
                                    "nativeQueryRef": "customer_id",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Top 10 Customers by Revenue'"
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
        "definition/pages/executive-overview/visuals/9c586391/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9c586391",
            "position": {
                "x": 0,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 0,
                "tabOrder": 0
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Total Revenue'"
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
                                            "Value": "20.0D"
                                        }
                                    }
                                },
                                "fontFamily": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'Abril Fatface'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/9ec80dd5/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "9ec80dd5",
            "position": {
                "x": 427,
                "y": 1080,
                "width": 427,
                "height": 360,
                "z": 7,
                "tabOrder": 7
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
                                                    "Entity": "Routes"
                                                }
                                            },
                                            "Property": "origin_city"
                                        }
                                    },
                                    "queryRef": "Routes.origin_city",
                                    "nativeQueryRef": "origin_city",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Top 10 Routes by Revenue'"
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
        "definition/pages/executive-overview/visuals/a8a70822/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "a8a70822",
            "position": {
                "x": 0,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 10,
                "tabOrder": 10
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
                                                    "Entity": "Customers"
                                                }
                                            },
                                            "Property": "customer_id"
                                        }
                                    },
                                    "queryRef": "Customers.customer_id",
                                    "nativeQueryRef": "customer_id",
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
                                            "Value": "'Customer'"
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
                                "fontColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#c25dab'"
                                                }
                                            }
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
        "definition/pages/executive-overview/visuals/aef55492/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "aef55492",
            "position": {
                "x": 1067,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 4,
                "tabOrder": 4
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Fleet Size"
                                        }
                                    },
                                    "queryRef": "Trips.Fleet Size",
                                    "nativeQueryRef": "Fleet Size"
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
                                            "Value": "'Fleet Size'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/bc1c0d2c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "bc1c0d2c",
            "position": {
                "x": 853,
                "y": 1080,
                "width": 427,
                "height": 360,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "donutChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Loads"
                                        }
                                    },
                                    "queryRef": "Loads.Total Loads",
                                    "nativeQueryRef": "Total Loads"
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
                                            "Value": "'Loads by Type'"
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
        "definition/pages/executive-overview/visuals/c0bb57e8/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c0bb57e8",
            "position": {
                "x": 640,
                "y": 180,
                "width": 213,
                "height": 300,
                "z": 11,
                "tabOrder": 11
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
                                                    "Entity": "Routes"
                                                }
                                            },
                                            "Property": "origin_city"
                                        }
                                    },
                                    "queryRef": "Routes.origin_city",
                                    "nativeQueryRef": "origin_city",
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
                                            "Value": "'Route'"
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
        "definition/pages/executive-overview/visuals/d39556f0/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "d39556f0",
            "position": {
                "x": 640,
                "y": 540,
                "width": 640,
                "height": 60,
                "z": 21,
                "tabOrder": 21
            },
            "visual": {
                "visualType": "actionButton",
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
                                            "Value": "'Go to Customer & Revenue Analytics'"
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
                    "action": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#0065B3'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e1dad5'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/e09d4e3a/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e09d4e3a",
            "position": {
                "x": 213,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 17,
                "tabOrder": 17
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Average Revenue per Load"
                                        }
                                    },
                                    "queryRef": "Loads.Average Revenue per Load",
                                    "nativeQueryRef": "Average Revenue per Load"
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
                                            "Value": "'Average Revenue per Load'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/e4c6985c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e4c6985c",
            "position": {
                "x": 0,
                "y": 720,
                "width": 640,
                "height": 360,
                "z": 5,
                "tabOrder": 5
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                                    "Entity": "_Measures"
                                                }
                                            },
                                            "Property": "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                                        }
                                    },
                                    "queryRef": "_Measures.='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )",
                                    "nativeQueryRef": "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
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
                                            "Value": "'='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend''"
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
        "definition/pages/executive-overview/visuals/e84c2667/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "e84c2667",
            "position": {
                "x": 0,
                "y": 1080,
                "width": 427,
                "height": 360,
                "z": 14,
                "tabOrder": 14
            },
            "visual": {
                "visualType": "donutChart",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "route_id"
                                        }
                                    },
                                    "queryRef": "Loads.route_id",
                                    "nativeQueryRef": "route_id",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Loads"
                                        }
                                    },
                                    "queryRef": "Loads.Total Loads",
                                    "nativeQueryRef": "Total Loads"
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
                                            "Value": "'Loads by Booking Type'"
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
        "definition/pages/executive-overview/visuals/f274700f/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "f274700f",
            "position": {
                "x": 427,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 1,
                "tabOrder": 1
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Total Trips"
                                        }
                                    },
                                    "queryRef": "Trips.Total Trips",
                                    "nativeQueryRef": "Total Trips"
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
                                            "Value": "'Total Trips'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/ff30b3dd/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "ff30b3dd",
            "position": {
                "x": 853,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 3,
                "tabOrder": 3
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Total Drivers"
                                        }
                                    },
                                    "queryRef": "Trips.Total Drivers",
                                    "nativeQueryRef": "Total Drivers"
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
                                            "Value": "'Total Drivers'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#99cfcd'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/executive-overview/visuals/ffa08fac/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "ffa08fac",
            "position": {
                "x": 640,
                "y": 600,
                "width": 640,
                "height": 120,
                "z": 18,
                "tabOrder": 18
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
                                                    "Entity": "Parameters"
                                                }
                                            },
                                            "Property": "Label"
                                        }
                                    },
                                    "queryRef": "Parameters.Label",
                                    "nativeQueryRef": "Label",
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
                                            "Value": "'Top N Customers'"
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
        "definition/pages/fleet-operations/page.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
            "name": "fleet-operations",
            "displayName": "Fleet Operations",
            "displayOption": "FitToWidth",
            "height": 820,
            "width": 1280
        },
        "definition/pages/fleet-operations/visuals/15b12c08/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "15b12c08",
            "position": {
                "x": 0,
                "y": 720,
                "width": 640,
                "height": 60,
                "z": 10,
                "tabOrder": 10
            },
            "visual": {
                "visualType": "actionButton",
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
                                            "Value": "'Go to Executive overview'"
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
                                            "Value": "'Source Sans Pro'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#0065B3'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e1dad5'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/25d111c4/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "25d111c4",
            "position": {
                "x": 640,
                "y": 720,
                "width": 640,
                "height": 60,
                "z": 11,
                "tabOrder": 11
            },
            "visual": {
                "visualType": "actionButton",
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
                                            "Value": "'Go to Customer & Revenue Analytics'"
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
                                            "Value": "'Source Sans Pro'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "action": [
                        {
                            "properties": {
                                "type": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "'PageNavigation'"
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "fill": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "fillColor": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#0065B3'"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ],
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e1dad5'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/2e5b83ff/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "2e5b83ff",
            "position": {
                "x": 853,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 1,
                "tabOrder": 1
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Average Trip Duration"
                                        }
                                    },
                                    "queryRef": "Trips.Average Trip Duration",
                                    "nativeQueryRef": "Average Trip Duration"
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
                                            "Value": "'Average Trip Duration'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/5336c41a/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "5336c41a",
            "position": {
                "x": 427,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 2,
                "tabOrder": 2
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Average Trip Distance"
                                        }
                                    },
                                    "queryRef": "Trips.Average Trip Distance",
                                    "nativeQueryRef": "Average Trip Distance"
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
                                            "Value": "'Average Trip Distance'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/5815d4bb/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "5815d4bb",
            "position": {
                "x": 0,
                "y": 180,
                "width": 907,
                "height": 240,
                "z": 5,
                "tabOrder": 5
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "DistanceBand"
                                        }
                                    },
                                    "queryRef": "Trips.DistanceBand",
                                    "nativeQueryRef": "DistanceBand",
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Total Trips"
                                        }
                                    },
                                    "queryRef": "Trips.Total Trips",
                                    "nativeQueryRef": "Total Trips"
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
                                            "Value": "'Distance Band Distribution'"
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
        "definition/pages/fleet-operations/visuals/65fe3a5c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "65fe3a5c",
            "position": {
                "x": 0,
                "y": 420,
                "width": 640,
                "height": 300,
                "z": 7,
                "tabOrder": 7
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
                                                    "Entity": "TruckMap"
                                                }
                                            },
                                            "Property": "unit_number"
                                        }
                                    },
                                    "queryRef": "TruckMap.unit_number",
                                    "nativeQueryRef": "unit_number",
                                    "active": true
                                },
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "TruckMap"
                                                }
                                            },
                                            "Property": "unit_number"
                                        }
                                    },
                                    "queryRef": "TruckMap.unit_number",
                                    "nativeQueryRef": "unit_number",
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Avg(actual_distance_miles)"
                                        }
                                    },
                                    "queryRef": "Trips.Avg(actual_distance_miles)",
                                    "nativeQueryRef": "Avg(actual_distance_miles)"
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Avg(average_mpg)"
                                        }
                                    },
                                    "queryRef": "Trips.Avg(average_mpg)",
                                    "nativeQueryRef": "Avg(average_mpg)"
                                }
                            ]
                        },
                        "Size": {
                            "projections": [
                                {
                                    "field": {
                                        "Measure": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Revenue"
                                        }
                                    },
                                    "queryRef": "Loads.Total Revenue",
                                    "nativeQueryRef": "Total Revenue"
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
                                            "Value": "'Truck Performance'"
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
        "definition/pages/fleet-operations/visuals/69cacc6e/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "69cacc6e",
            "position": {
                "x": 907,
                "y": 180,
                "width": 373,
                "height": 240,
                "z": 6,
                "tabOrder": 6
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "IdleTimeBand"
                                        }
                                    },
                                    "queryRef": "Trips.IdleTimeBand",
                                    "nativeQueryRef": "IdleTimeBand",
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Avg(idle_time_hours)"
                                        }
                                    },
                                    "queryRef": "Trips.Avg(idle_time_hours)",
                                    "nativeQueryRef": "Avg(idle_time_hours)"
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
                                            "Value": "'Idle Time Analysis'"
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
        "definition/pages/fleet-operations/visuals/b105a5be/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "b105a5be",
            "position": {
                "x": 640,
                "y": 0,
                "width": 213,
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Fleet Operations"
                                        }
                                    },
                                    "queryRef": "Trips.Fleet Operations",
                                    "nativeQueryRef": "Fleet Operations"
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
                                            "Value": "'Fleet Operations'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/c47b0476/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "c47b0476",
            "position": {
                "x": 213,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 0,
                "tabOrder": 0
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
                                                    "Entity": "Trips"
                                                }
                                            },
                                            "Property": "Average Fuel Efficiency"
                                        }
                                    },
                                    "queryRef": "Trips.Average Fuel Efficiency",
                                    "nativeQueryRef": "Average Fuel Efficiency"
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
                                            "Value": "'Average Fuel Efficiency'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/d8e3104c/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "d8e3104c",
            "position": {
                "x": 640,
                "y": 420,
                "width": 640,
                "height": 300,
                "z": 8,
                "tabOrder": 8
            },
            "visual": {
                "visualType": "funnel",
                "query": {
                    "queryState": {
                        "Category": {
                            "projections": [
                                {
                                    "field": {
                                        "Column": {
                                            "Expression": {
                                                "SourceRef": {
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "RevenueBand"
                                        }
                                    },
                                    "queryRef": "Loads.RevenueBand",
                                    "nativeQueryRef": "RevenueBand",
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Total Loads"
                                        }
                                    },
                                    "queryRef": "Loads.Total Loads",
                                    "nativeQueryRef": "Total Loads"
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
                                            "Value": "'High Value Loads'"
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
        "definition/pages/fleet-operations/visuals/dbe9586d/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "dbe9586d",
            "position": {
                "x": 1067,
                "y": 0,
                "width": 213,
                "height": 180,
                "z": 4,
                "tabOrder": 4
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
                                                    "Entity": "Loads"
                                                }
                                            },
                                            "Property": "Revenue per Mile"
                                        }
                                    },
                                    "queryRef": "Loads.Revenue per Mile",
                                    "nativeQueryRef": "Revenue per Mile"
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
                                            "Value": "'Revenue per Mile'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/fleet-operations/visuals/f7d0a73a/visual.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.9.0/schema.json",
            "name": "f7d0a73a",
            "position": {
                "x": 320,
                "y": 240,
                "width": 213,
                "height": 180,
                "z": 3,
                "tabOrder": 3
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
                                                    "Entity": "Trucks"
                                                }
                                            },
                                            "Property": "Active Trucks"
                                        }
                                    },
                                    "queryRef": "Trucks.Active Trucks",
                                    "nativeQueryRef": "Active Trucks"
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
                                            "Value": "'Active Trucks'"
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
                    "background": [
                        {
                            "properties": {
                                "show": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "true"
                                        }
                                    }
                                },
                                "color": {
                                    "solid": {
                                        "color": {
                                            "expr": {
                                                "Literal": {
                                                    "Value": "'#e0bd8d'"
                                                }
                                            }
                                        }
                                    }
                                },
                                "transparency": {
                                    "expr": {
                                        "Literal": {
                                            "Value": "0D"
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
        "definition/pages/pages.json": {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
            "pageOrder": [
                "executive-overview",
                "fleet-operations",
                "customer-revenue-analytics"
            ],
            "activePageName": "executive-overview"
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