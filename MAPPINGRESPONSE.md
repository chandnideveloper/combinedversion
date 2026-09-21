{
    "status": "success",
    "message": "Mapping completed successfully",
    "error_message": null,
    "contract_version": "2.0",
    "workbook_metadata": {
        "project_id": "afdeddc7-4dca-470b-bd3d-cdc279a1c408",
        "app_id": "afdeddc7-4dca-470b-bd3d-cdc279a1c408",
        "space_id": "personal",
        "name": "FleetVision KSA",
        "app_name": "FleetVision KSA",
        "run_id": "c-oihjb",
        "created_at": "2026-09-01T03:23:42.561520",
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
        "last_modified": "2026-08-30T07:02:31.151Z"
    },
    "connections": [
        {
            "name": "FleetVisionRedshift",
            "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2",
            "lib_name": "FleetVisionRedshift",
            "driver": "redshift",
            "source_connector": "redshift",
            "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
            "port": "5439",
            "database": "dev",
            "schema": "public",
            "warehouse": null,
            "role": null,
            "project": null,
            "dataset": null,
            "http_path": null,
            "path": null,
            "username": null,
            "fabric": {
                "m_expression": "AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")",
                "m_source_function": "AmazonRedshift.Database",
                "gateway_required": true,
                "privacy_level": "Organizational"
            },
            "confidence": {
                "score": 0.97,
                "band": "high",
                "llm_score": 0.97,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Driver 'redshift' maps to AmazonRedshift.Database by lookup."
            }
        },
        {
            "name": "DataFiles",
            "connection_id": "6f93cda1-15c4-4321-94e7-ac3cdcab5e4c",
            "lib_name": "DataFiles",
            "driver": "qix-datafiles.exe",
            "source_connector": "qix-datafiles.exe",
            "server": null,
            "port": "5439",
            "database": "dev",
            "schema": null,
            "warehouse": null,
            "role": null,
            "project": null,
            "dataset": null,
            "http_path": null,
            "path": "datafiles",
            "username": null,
            "fabric": {
                "m_expression": "Folder.Files(\"datafiles\")",
                "m_source_function": "Folder.Files",
                "gateway_required": true,
                "privacy_level": "Organizational"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "The connection references a folder path ('datafiles') and uses a Qlik datafiles connector. M equivalent is Folder.Files."
            }
        }
    ],
    "tables": [
        {
            "name": "Trips",
            "table_name": "Trips",
            "load_type": "source",
            "source_type": "resident",
            "connection": null,
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nTrips:\r\nNoConcatenate\r\nLOAD\r\n    trip_id,\r\n    load_id,\r\n    driver_id,\r\n    truck_id,\r\n    ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber,\r\n    trailer_id,\r\n\r\n    Date(dispatch_date) as DispatchDate,\r\n    Month(dispatch_date) as TripMonth,\r\n    Month(dispatch_date) as LoadMonth,\r\n    MonthStart(dispatch_date) as MonthStartDate,\r\n\tMonthName(dispatch_date) as MonthYear,\r\n\tNum(MonthStart(dispatch_date)) as MonthSort,\r\n    Year(dispatch_date) as TripYear,\r\n    Week(dispatch_date) as TripWeek,\r\n    Num(Month(dispatch_date)) as MonthNo,\r\n\r\n    actual_distance_miles,\r\n    actual_duration_hours,\r\n    fuel_gallons_used,\r\n    average_mpg,\r\n    idle_time_hours,\r\n    trip_status,\r\n    \r\n    If(\r\n        actual_distance_miles >= 1000,\r\n        'Long Haul',\r\n        If(actual_distance_miles >= 500,\r\n            'Medium Haul',\r\n            'Short Haul'\r\n        )\r\n    ) as DistanceBand,\r\n    \r\n    If(\r\n    average_mpg >= 8,\r\n    'High MPG',\r\n    If(\r\n        average_mpg >= 6,\r\n        'Medium MPG',\r\n        'Low MPG'\r\n    )\r\n) as FuelEfficiencyBand,\r\n\r\nIf(\r\n    idle_time_hours >= 5,\r\n    'High Idle',\r\n    If(\r\n        idle_time_hours >= 2,\r\n        'Moderate Idle',\r\n        'Low Idle'\r\n    )\r\n) as IdleTimeBand\r\n\r\nResident Trips_Raw",
            "custom_sql": "SQL SELECT\r\n    trip_id,\r\n    load_id,\r\n    driver_id,\r\n    truck_id,\r\n    trailer_id,\r\n    dispatch_date,\r\n    actual_distance_miles,\r\n    actual_duration_hours,\r\n    fuel_gallons_used,\r\n    average_mpg,\r\n    idle_time_hours,\r\n    trip_status\r\nFROM fleetvision.v_trips",
            "columns": [
                {
                    "qlik_column_name": "driver_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "driver_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "trailer_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trailer_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "load_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "load_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "actual_distance_miles",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "actual_distance_miles",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "actual_duration_hours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "actual_duration_hours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "fuel_gallons_used",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "fuel_gallons_used",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "average_mpg",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "average_mpg",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "idle_time_hours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "idle_time_hours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "trip_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "TruckNumber",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckNumber",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "DispatchDate",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "DispatchDate",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "TripMonth",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TripMonth",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "LoadMonth",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "LoadMonth",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "MonthStartDate",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "MonthStartDate",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "MonthYear",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "MonthYear",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "YYYY-MM-DD"
                },
                {
                    "qlik_column_name": "MonthSort",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "MonthSort",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "TripYear",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TripYear",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "TripWeek",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TripWeek",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "MonthNo",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "MonthNo",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "DistanceBand",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "DistanceBand",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "FuelEfficiencyBand",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "FuelEfficiencyBand",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "IdleTimeBand",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "IdleTimeBand",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
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
                "rationale": "All Qlik date and conditional functions mapped directly. However, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber, ApplyMap('TruckMap', truck_id, 'Unknown') as TruckNumber cannot be resolved, so field is set to null."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Trips in Source"
                }
            ]
        },
        {
            "name": "Drivers",
            "table_name": "Drivers",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nDrivers:\r\nLOAD\r\n    driver_id,\r\n    first_name,\r\n    last_name,\r\n\r\n    Trim(first_name & ' ' & last_name) AS DriverName,\r\n\r\n    hire_date,\r\n    termination_date,\r\n    license_number,\r\n    license_state,\r\n    date_of_birth,\r\n\r\n    home_terminal,\r\n\r\n    Upper(Trim(home_terminal)) AS HOME_TERMINAL,\r\n\r\n    employment_status,\r\n    cdl_class,\r\n    years_experience;\nSQL SELECT\r\n    driver_id,\r\n    first_name,\r\n    last_name,\r\n    hire_date,\r\n    termination_date,\r\n    license_number,\r\n    license_state,\r\n    date_of_birth,\r\n    home_terminal,\r\n    employment_status,\r\n    cdl_class,\r\n    years_experience\r\nFROM fleetvision.drivers",
            "custom_sql": "SQL SELECT\r\n    driver_id,\r\n    first_name,\r\n    last_name,\r\n    hire_date,\r\n    termination_date,\r\n    license_number,\r\n    license_state,\r\n    date_of_birth,\r\n    home_terminal,\r\n    employment_status,\r\n    cdl_class,\r\n    years_experience\r\nFROM fleetvision.drivers",
            "columns": [
                {
                    "qlik_column_name": "driver_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "driver_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "first_name",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "first_name",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "last_name",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "last_name",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "hire_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "hire_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "termination_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "termination_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "license_number",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "license_number",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "license_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "license_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "date_of_birth",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "date_of_birth",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "home_terminal",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "home_terminal",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "employment_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "employment_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "cdl_class",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "cdl_class",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "years_experience",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "years_experience",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\n    driver_id,\r\n    first_name,\r\n    last_name,\r\n    hire_date,\r\n    termination_date,\r\n    license_number,\r\n    license_state,\r\n    date_of_birth,\r\n    home_terminal,\r\n    employment_status,\r\n    cdl_class,\r\n    years_experience\r\nFROM fleetvision.drivers\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "DriverPerformance",
            "table_name": "DriverPerformance",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "Trips",
            "qlik_query": "\n\n// --- Source Part ---\nDriverPerformance:\r\nLOAD\r\n    driver_id,\r\n    Count(DISTINCT trip_id) AS TotalTrips,\r\n    Sum(actual_distance_miles) AS TotalMiles,\r\n    Sum(actual_duration_hours) AS TotalTripHours,\r\n    Sum(fuel_gallons_used) AS TotalFuelGallons,\r\n    If(\r\n        Sum(fuel_gallons_used) > 0,\r\n        Sum(actual_distance_miles) / Sum(fuel_gallons_used),\r\n        0\r\n    ) AS FleetMPG,\r\n    Avg(average_mpg) AS AvgMPG,\r\n    Avg(idle_time_hours) AS AvgIdleHours,\r\n    Sum(idle_time_hours) AS TotalIdleHours\r\nResident Trips\r\nGROUP BY driver_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "driver_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "driver_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "TotalTrips",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalTrips",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "TotalMiles",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalMiles",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "TotalTripHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalTripHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TotalFuelGallons",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalFuelGallons",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "FleetMPG",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "FleetMPG",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "AvgMPG",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgMPG",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                },
                {
                    "qlik_column_name": "AvgIdleHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgIdleHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                },
                {
                    "qlik_column_name": "TotalIdleHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalIdleHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Trips in Source"
                }
            ]
        },
        {
            "name": "Trucks",
            "table_name": "Trucks",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nTrucks:\r\nSQL SELECT\r\ntruck_id,\r\nunit_number,\r\nmake,\r\nmodel_year            AS truck_model_year,\r\nvin                   AS truck_vin,\r\nacquisition_date      AS truck_acquisition_date,\r\nacquisition_mileage,\r\nfuel_type,\r\ntank_capacity_gallons,\r\nstatus                AS truck_status,\r\nhome_terminal         AS truck_home_terminal\r\nFROM fleetvision.trucks",
            "custom_sql": "SQL SELECT\r\ntruck_id,\r\nunit_number,\r\nmake,\r\nmodel_year            AS truck_model_year,\r\nvin                   AS truck_vin,\r\nacquisition_date      AS truck_acquisition_date,\r\nacquisition_mileage,\r\nfuel_type,\r\ntank_capacity_gallons,\r\nstatus                AS truck_status,\r\nhome_terminal         AS truck_home_terminal\r\nFROM fleetvision.trucks",
            "columns": [
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "unit_number",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "unit_number",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "make",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "make",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "truck_model_year",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "truck_model_year",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "truck_vin",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_vin",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "truck_acquisition_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "truck_acquisition_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "acquisition_mileage",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "acquisition_mileage",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "fuel_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "fuel_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "tank_capacity_gallons",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "tank_capacity_gallons",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "truck_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "truck_home_terminal",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_home_terminal",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\ntruck_id,\r\nunit_number,\r\nmake,\r\nmodel_year            AS truck_model_year,\r\nvin                   AS truck_vin,\r\nacquisition_date      AS truck_acquisition_date,\r\nacquisition_mileage,\r\nfuel_type,\r\ntank_capacity_gallons,\r\nstatus                AS truck_status,\r\nhome_terminal         AS truck_home_terminal\r\nFROM fleetvision.trucks\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "Maintenance",
            "table_name": "Maintenance",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nMaintenance:\r\nSQL SELECT\r\nmaintenance_id,\r\ntruck_id,\r\nmaintenance_date,\r\nmaintenance_type,\r\nodometer_reading,\r\nlabor_hours,\r\nlabor_cost,\r\nparts_cost,\r\ntotal_cost        AS maintenance_total_cost,\r\nfacility_location,\r\ndowntime_hours,\r\nservice_description\r\nFROM fleetvision.maintenance_records",
            "custom_sql": "SQL SELECT\r\nmaintenance_id,\r\ntruck_id,\r\nmaintenance_date,\r\nmaintenance_type,\r\nodometer_reading,\r\nlabor_hours,\r\nlabor_cost,\r\nparts_cost,\r\ntotal_cost        AS maintenance_total_cost,\r\nfacility_location,\r\ndowntime_hours,\r\nservice_description\r\nFROM fleetvision.maintenance_records",
            "columns": [
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "maintenance_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "maintenance_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "maintenance_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "maintenance_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "maintenance_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "maintenance_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "odometer_reading",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "odometer_reading",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "labor_hours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "labor_hours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "labor_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "labor_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "parts_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "parts_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "maintenance_total_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "maintenance_total_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "facility_location",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "facility_location",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "downtime_hours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "downtime_hours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "service_description",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "service_description",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\nmaintenance_id,\r\ntruck_id,\r\nmaintenance_date,\r\nmaintenance_type,\r\nodometer_reading,\r\nlabor_hours,\r\nlabor_cost,\r\nparts_cost,\r\ntotal_cost        AS maintenance_total_cost,\r\nfacility_location,\r\ndowntime_hours,\r\nservice_description\r\nFROM fleetvision.maintenance_records\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "TruckPerformance",
            "table_name": "TruckPerformance",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "Trips",
            "qlik_query": "\n\n// --- Source Part ---\nTruckPerformance:\r\nLOAD\r\n    truck_id,\r\n    Count(DISTINCT trip_id) AS TruckTrips,\r\n    Sum(actual_distance_miles) AS TruckMiles,\r\n    Sum(actual_duration_hours) AS TruckHours,\r\n    Sum(fuel_gallons_used) AS TruckFuelGallons,\r\n    If(\r\n        Sum(fuel_gallons_used) > 0,\r\n        Sum(actual_distance_miles) / Sum(fuel_gallons_used),\r\n        0\r\n    ) AS TruckMPG,\r\n    Avg(idle_time_hours) AS TruckAvgIdleHours,\r\n    Sum(idle_time_hours) AS TruckIdleHours\r\nResident Trips\r\nGROUP BY truck_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "TruckTrips",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckTrips",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "TruckMiles",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckMiles",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "TruckHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TruckFuelGallons",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckFuelGallons",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TruckMPG",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckMPG",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TruckAvgIdleHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckAvgIdleHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                },
                {
                    "qlik_column_name": "TruckIdleHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TruckIdleHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Trips in Source"
                }
            ]
        },
        {
            "name": "MaintenanceByTruck",
            "table_name": "MaintenanceByTruck",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "Maintenance",
            "qlik_query": "\n\n// --- Source Part ---\nMaintenanceByTruck:\r\nLOAD\r\n    truck_id,\r\n\r\n    Count(DISTINCT maintenance_id) AS MaintenanceEvents,\r\n\r\n    Sum(maintenance_total_cost) AS TotalMaintenanceCost,\r\n\r\n    Sum(downtime_hours) AS TotalDowntimeHours,\r\n\r\n    Avg(downtime_hours) AS AvgDowntimeHours,\r\n\r\n    Sum(labor_cost) AS TotalLaborCost,\r\n\r\n    Sum(parts_cost) AS TotalPartsCost,\r\n\r\n    Avg(labor_hours) AS AvgLaborHours\r\n\r\nResident Maintenance\r\n\r\nGROUP BY truck_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "MaintenanceEvents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "MaintenanceEvents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "TotalMaintenanceCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalMaintenanceCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TotalDowntimeHours",
                    "qlik_datatype": "TIME",
                    "fabric_column_name": "TotalDowntimeHours",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "YYYY-MM-DD"
                },
                {
                    "qlik_column_name": "AvgDowntimeHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgDowntimeHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                },
                {
                    "qlik_column_name": "TotalLaborCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalLaborCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TotalPartsCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalPartsCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "AvgLaborHours",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgLaborHours",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Maintenance in Source"
                }
            ]
        },
        {
            "name": "Trailers",
            "table_name": "Trailers",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nTrailers:\r\nSQL SELECT\r\ntrailer_id,\r\ntrailer_number,\r\ntrailer_type,\r\nlength_feet,\r\nmodel_year            AS trailer_model_year,\r\nvin                   AS trailer_vin,\r\nacquisition_date      AS trailer_acquisition_date,\r\nstatus                AS trailer_status,\r\ncurrent_location\r\nFROM fleetvision.trailers",
            "custom_sql": "SQL SELECT\r\ntrailer_id,\r\ntrailer_number,\r\ntrailer_type,\r\nlength_feet,\r\nmodel_year            AS trailer_model_year,\r\nvin                   AS trailer_vin,\r\nacquisition_date      AS trailer_acquisition_date,\r\nstatus                AS trailer_status,\r\ncurrent_location\r\nFROM fleetvision.trailers",
            "columns": [
                {
                    "qlik_column_name": "trailer_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trailer_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "trailer_number",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "trailer_number",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "trailer_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trailer_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "length_feet",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "length_feet",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "trailer_model_year",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "trailer_model_year",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "trailer_vin",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trailer_vin",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "trailer_acquisition_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "trailer_acquisition_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "trailer_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trailer_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "current_location",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "current_location",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\ntrailer_id,\r\ntrailer_number,\r\ntrailer_type,\r\nlength_feet,\r\nmodel_year            AS trailer_model_year,\r\nvin                   AS trailer_vin,\r\nacquisition_date      AS trailer_acquisition_date,\r\nstatus                AS trailer_status,\r\ncurrent_location\r\nFROM fleetvision.trailers\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "Customers",
            "table_name": "Customers",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nCustomers:\r\nSQL SELECT *\r\nFROM fleetvision.customers",
            "custom_sql": "SQL SELECT *\r\nFROM fleetvision.customers",
            "columns": [
                {
                    "qlik_column_name": "customer_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "customer_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "customer_name",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "customer_name",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "customer_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "customer_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "credit_terms_days",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "credit_terms_days",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "primary_freight_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "primary_freight_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "account_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "account_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "contract_start_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "contract_start_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "annual_revenue_potential",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "annual_revenue_potential",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT *\r\nFROM fleetvision.customers\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "Loads",
            "table_name": "Loads",
            "load_type": "source",
            "source_type": "resident",
            "connection": null,
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nLoads:\r\nNoConcatenate\r\nLOAD\r\n    *,\r\n\r\n    If(\r\n    revenue >= 6000,\r\n    'High Value',\r\n    If(\r\n        revenue >= 3000,\r\n        'Medium Value',\r\n        'Low Value'\r\n    )\r\n) as RevenueBand\r\n\r\nResident Loads_Raw",
            "custom_sql": "SQL SELECT *\r\nFROM fleetvision.loads",
            "columns": [
                {
                    "qlik_column_name": "customer_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "customer_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "route_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "route_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "load_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "load_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "load_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "load_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "load_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "load_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "weight_lbs",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "weight_lbs",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "pieces",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "pieces",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "revenue",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "revenue",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "fuel_surcharge",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "fuel_surcharge",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "accessorial_charges",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "accessorial_charges",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "load_status",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "load_status",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "booking_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "booking_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "RevenueBand",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "RevenueBand",
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
                    "content": "let Source = Loads in Source"
                }
            ]
        },
        {
            "name": "Facilities",
            "table_name": "Facilities",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nFacilities:\r\nSQL SELECT *\r\nFROM fleetvision.facilities",
            "custom_sql": "SQL SELECT *\r\nFROM fleetvision.facilities",
            "columns": [
                {
                    "qlik_column_name": "facility_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "facility_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "facility_name",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "facility_name",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "facility_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "facility_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "latitude",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "latitude",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "longitude",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "longitude",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "dock_doors",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "dock_doors",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "operating_hours",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "operating_hours",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "longitude_latitude",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "longitude_latitude",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT *\r\nFROM fleetvision.facilities\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "DeliveryEvents",
            "table_name": "DeliveryEvents",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nDeliveryEvents:\r\nSQL SELECT\r\nevent_id,\r\ntrip_id,\r\nevent_type,\r\nfacility_id,\r\nscheduled_datetime,\r\nactual_datetime,\r\ndetention_minutes,\r\non_time_flag,\r\nlocation_city     AS delivery_city,\r\nlocation_state    AS delivery_state\r\nFROM fleetvision.delivery_events",
            "custom_sql": "SQL SELECT\r\nevent_id,\r\ntrip_id,\r\nevent_type,\r\nfacility_id,\r\nscheduled_datetime,\r\nactual_datetime,\r\ndetention_minutes,\r\non_time_flag,\r\nlocation_city     AS delivery_city,\r\nlocation_state    AS delivery_state\r\nFROM fleetvision.delivery_events",
            "columns": [
                {
                    "qlik_column_name": "facility_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "facility_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "event_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "event_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "event_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "event_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "scheduled_datetime",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "scheduled_datetime",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY h:mm:ss[.fff] TT"
                },
                {
                    "qlik_column_name": "actual_datetime",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "actual_datetime",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY h:mm:ss[.fff] TT"
                },
                {
                    "qlik_column_name": "detention_minutes",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "detention_minutes",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "on_time_flag",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "on_time_flag",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "delivery_city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "delivery_city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "delivery_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "delivery_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\nevent_id,\r\ntrip_id,\r\nevent_type,\r\nfacility_id,\r\nscheduled_datetime,\r\nactual_datetime,\r\ndetention_minutes,\r\non_time_flag,\r\nlocation_city     AS delivery_city,\r\nlocation_state    AS delivery_state\r\nFROM fleetvision.delivery_events\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "Routes",
            "table_name": "Routes",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nRoutes:\r\nSQL SELECT *\r\nFROM fleetvision.routes",
            "custom_sql": "SQL SELECT *\r\nFROM fleetvision.routes",
            "columns": [
                {
                    "qlik_column_name": "route_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "route_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "origin_city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "origin_city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "origin_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "origin_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "destination_city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "destination_city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "destination_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "destination_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "typical_distance_miles",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "typical_distance_miles",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "base_rate_per_mile",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "base_rate_per_mile",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "fuel_surcharge_rate",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "fuel_surcharge_rate",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "typical_transit_days",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "typical_transit_days",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT *\r\nFROM fleetvision.routes\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "FuelPurchases",
            "table_name": "FuelPurchases",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nFuelPurchases:\r\nSQL SELECT\r\nfuel_purchase_id,\r\ntrip_id,\r\npurchase_date,\r\nlocation_city     AS fuel_city,\r\nlocation_state    AS fuel_state,\r\ngallons,\r\nprice_per_gallon,\r\ntotal_cost        AS fuel_total_cost,\r\nfuel_card_number\r\nFROM fleetvision.fuel_purchases",
            "custom_sql": "SQL SELECT\r\nfuel_purchase_id,\r\ntrip_id,\r\npurchase_date,\r\nlocation_city     AS fuel_city,\r\nlocation_state    AS fuel_state,\r\ngallons,\r\nprice_per_gallon,\r\ntotal_cost        AS fuel_total_cost,\r\nfuel_card_number\r\nFROM fleetvision.fuel_purchases",
            "columns": [
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "fuel_purchase_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "fuel_purchase_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "purchase_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "purchase_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "fuel_city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "fuel_city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "fuel_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "fuel_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "gallons",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "gallons",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "price_per_gallon",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "price_per_gallon",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "fuel_total_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "fuel_total_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "fuel_card_number",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "fuel_card_number",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\nfuel_purchase_id,\r\ntrip_id,\r\npurchase_date,\r\nlocation_city     AS fuel_city,\r\nlocation_state    AS fuel_state,\r\ngallons,\r\nprice_per_gallon,\r\ntotal_cost        AS fuel_total_cost,\r\nfuel_card_number\r\nFROM fleetvision.fuel_purchases\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "SafetyIncidents",
            "table_name": "SafetyIncidents",
            "load_type": "source",
            "source_type": "database",
            "connection": {
                "datasource_id": "ds_1",
                "engine_datasource_id": "redshift",
                "name": "FleetVisionRedshift",
                "connector_type": "redshift",
                "driver": "redshift",
                "source_connector": "redshift",
                "server": "fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com",
                "database": "dev",
                "connection_id": "766fedfe-250e-4cea-b491-7b05671132d2"
            },
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nSafetyIncidents:\r\nSQL SELECT\r\nincident_id,\r\ntrip_id,\r\nincident_date,\r\nincident_type,\r\nlocation_city         AS incident_city,\r\nlocation_state        AS incident_state,\r\nat_fault_flag,\r\ninjury_flag,\r\nvehicle_damage_cost,\r\ncargo_damage_cost,\r\nclaim_amount,\r\npreventable_flag,\r\ndescription\r\nFROM fleetvision.safety_incidents",
            "custom_sql": "SQL SELECT\r\nincident_id,\r\ntrip_id,\r\nincident_date,\r\nincident_type,\r\nlocation_city         AS incident_city,\r\nlocation_state        AS incident_state,\r\nat_fault_flag,\r\ninjury_flag,\r\nvehicle_damage_cost,\r\ncargo_damage_cost,\r\nclaim_amount,\r\npreventable_flag,\r\ndescription\r\nFROM fleetvision.safety_incidents",
            "columns": [
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "incident_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "incident_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "incident_date",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "incident_date",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "incident_type",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "incident_type",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "incident_city",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "incident_city",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "incident_state",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "incident_state",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "at_fault_flag",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "at_fault_flag",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "injury_flag",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "injury_flag",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "vehicle_damage_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "vehicle_damage_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "cargo_damage_cost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "cargo_damage_cost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "claim_amount",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "claim_amount",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "##############"
                },
                {
                    "qlik_column_name": "preventable_flag",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "preventable_flag",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "description",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "description",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
                "checks": [
                    {
                        "id": "m_let_in_balanced",
                        "status": "pass"
                    },
                    {
                        "id": "m_source_matches_driver",
                        "status": "pass"
                    },
                    {
                        "id": "m_identifiers_escaped",
                        "status": "pass"
                    },
                    {
                        "id": "m_no_placeholder_fallback",
                        "status": "pass"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = AmazonRedshift.Database(\"fleetvision-wg.881226714470.ap-southeast-2.redshift-serverless.amazonaws.com:5439\", \"dev\")"
                },
                {
                    "step": 2,
                    "content": "Result = Value.NativeQuery(Source, \"SELECT\r\nincident_id,\r\ntrip_id,\r\nincident_date,\r\nincident_type,\r\nlocation_city         AS incident_city,\r\nlocation_state        AS incident_state,\r\nat_fault_flag,\r\ninjury_flag,\r\nvehicle_damage_cost,\r\ncargo_damage_cost,\r\nclaim_amount,\r\npreventable_flag,\r\ndescription\r\nFROM fleetvision.safety_incidents\", null, [EnableFolding=false]) in Result"
                }
            ]
        },
        {
            "name": "FuelByTrip",
            "table_name": "FuelByTrip",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "FuelPurchases",
            "qlik_query": "\n\n// --- Source Part ---\nFuelByTrip:\r\nLOAD\r\n    trip_id,\r\n\r\n    Sum(gallons) AS PurchasedGallons,\r\n\r\n    Sum(fuel_total_cost) AS TotalFuelCost,\r\n\r\n    If(\r\n        Sum(gallons) > 0,\r\n        Sum(fuel_total_cost) / Sum(gallons),\r\n        0\r\n    ) AS AvgFuelPricePerGallon,\r\n\r\n    Count(DISTINCT fuel_purchase_id) AS FuelTransactions\r\n\r\nResident FuelPurchases\r\n\r\nGROUP BY trip_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "PurchasedGallons",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "PurchasedGallons",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "TotalFuelCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalFuelCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "AvgFuelPricePerGallon",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgFuelPricePerGallon",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "FuelTransactions",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "FuelTransactions",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = FuelPurchases in Source"
                }
            ]
        },
        {
            "name": "DeliveryByTrip",
            "table_name": "DeliveryByTrip",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "DeliveryEvents",
            "qlik_query": "\n\n// --- Source Part ---\nDeliveryByTrip:\r\nLOAD\r\n    trip_id,\r\n\r\n    Count(DISTINCT event_id) AS DeliveryEvents,\r\n\r\n    Sum(\r\n        If(on_time_flag, 1, 0)\r\n    ) AS OnTimeEvents,\r\n\r\n    Sum(\r\n        If(on_time_flag = 0, 1, 0)\r\n    ) AS LateEvents,\r\n\r\n    If(\r\n        Count(DISTINCT event_id) > 0,\r\n        Sum(\r\n            If(on_time_flag, 1, 0)\r\n        )\r\n        /\r\n        Count(DISTINCT event_id),\r\n        0\r\n    ) AS OnTimeRate,\r\n\r\n    Sum(detention_minutes) AS TotalDetentionMinutes,\r\n\r\n    Avg(detention_minutes) AS AvgDetentionMinutes\r\n\r\nResident DeliveryEvents\r\n\r\nGROUP BY trip_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "DeliveryEvents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "DeliveryEvents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "OnTimeEvents",
                    "qlik_datatype": "TIME",
                    "fabric_column_name": "OnTimeEvents",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "YYYY-MM-DD"
                },
                {
                    "qlik_column_name": "LateEvents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "LateEvents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "OnTimeRate",
                    "qlik_datatype": "TIME",
                    "fabric_column_name": "OnTimeRate",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "YYYY-MM-DD"
                },
                {
                    "qlik_column_name": "TotalDetentionMinutes",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "TotalDetentionMinutes",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "AvgDetentionMinutes",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AvgDetentionMinutes",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "########"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = DeliveryEvents in Source"
                }
            ]
        },
        {
            "name": "SafetyByTrip",
            "table_name": "SafetyByTrip",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "SafetyIncidents",
            "qlik_query": "\n\n// --- Source Part ---\nSafetyByTrip:\r\nLOAD\r\n    trip_id,\r\n\r\n    Count(DISTINCT incident_id) AS SafetyIncidents,\r\n\r\n    Sum(\r\n        If(preventable_flag =  1, 0)\r\n    ) AS PreventableIncidents,\r\n\r\n    Sum(\r\n        If(injury_flag = 1, 0)\r\n    ) AS InjuryIncidents,\r\n\r\n    Sum(\r\n        If(at_fault_flag = 1, 0)\r\n    ) AS AtFaultIncidents,\r\n\r\n    Sum(vehicle_damage_cost) AS VehicleDamageCost,\r\n\r\n    Sum(cargo_damage_cost) AS CargoDamageCost,\r\n\r\n    Sum(claim_amount) AS ClaimAmount\r\n\r\nResident SafetyIncidents\r\n\r\nGROUP BY trip_id",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "trip_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "trip_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "SafetyIncidents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "SafetyIncidents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "PreventableIncidents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "PreventableIncidents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "InjuryIncidents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "InjuryIncidents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "AtFaultIncidents",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "AtFaultIncidents",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "VehicleDamageCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "VehicleDamageCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "CargoDamageCost",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CargoDamageCost",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "ClaimAmount",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "ClaimAmount",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = SafetyIncidents in Source"
                }
            ]
        },
        {
            "name": "Calendar",
            "table_name": "Calendar",
            "load_type": "autogenerate",
            "source_type": "generated",
            "connection": null,
            "upstream_table": null,
            "qlik_query": "\n\n// --- Source Part ---\nCalendar:\r\nLOAD\r\n    Date($(vMinDate) + IterNo() - 1) AS DispatchDate,\r\n\r\n    Year($(vMinDate) + IterNo() - 1) AS CalendarYear,\r\n\r\n    'Q' & Ceil(\r\n        Month($(vMinDate) + IterNo() - 1) / 3\r\n    ) AS CalendarQuarter,\r\n\r\n    Month(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarMonth,\r\n\r\n    MonthName(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarMonthYear,\r\n\r\n    MonthStart(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarMonthStart,\r\n\r\n    Week(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarWeek,\r\n\r\n    WeekDay(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarWeekDay,\r\n\r\n    Day(\r\n        $(vMinDate) + IterNo() - 1\r\n    ) AS CalendarDay\r\n\r\nAUTOGENERATE 1\r\n\r\nWHILE $(vMinDate) + IterNo() - 1 <= $(vMaxDate)",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "DispatchDate",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "DispatchDate",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "CalendarYear",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CalendarYear",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "CalendarQuarter",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "CalendarQuarter",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "General Text"
                },
                {
                    "qlik_column_name": "CalendarMonth",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CalendarMonth",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "CalendarMonthYear",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "CalendarMonthYear",
                    "fabric_datatype": "int64",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "YYYY-MM-DD"
                },
                {
                    "qlik_column_name": "CalendarMonthStart",
                    "qlik_datatype": "DATE",
                    "fabric_column_name": "CalendarMonthStart",
                    "fabric_datatype": "dateTime",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "M/D/YYYY"
                },
                {
                    "qlik_column_name": "CalendarWeek",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CalendarWeek",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
                },
                {
                    "qlik_column_name": "CalendarWeekDay",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CalendarWeekDay",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0"
                },
                {
                    "qlik_column_name": "CalendarDay",
                    "qlik_datatype": "NUMBER",
                    "fabric_column_name": "CalendarDay",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "###0"
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
                    "content": "let StartDate = #date(2020, 1, 1)"
                },
                {
                    "step": 2,
                    "content": "EndDate = #date(2026, 12, 31)"
                },
                {
                    "step": 3,
                    "content": "NumberOfDays = Duration.Days(EndDate - StartDate) + 1"
                },
                {
                    "step": 4,
                    "content": "DateList = List.Dates(StartDate, NumberOfDays, #duration(1, 0, 0, 0))"
                },
                {
                    "step": 5,
                    "content": "#\"Converted to Table\" = Table.FromList(DateList, Splitter.SplitByNothing(), {\"DispatchDate\"}, null, ExtraValues.Error)"
                },
                {
                    "step": 6,
                    "content": "#\"Changed Type\" = Table.TransformColumnTypes(#\"Converted to Table\", {{\"DispatchDate\", type date}})"
                },
                {
                    "step": 7,
                    "content": "#\"Added CalendarYear\" = Table.AddColumn(#\"Changed Type\", \"CalendarYear\", each Date.Year([DispatchDate]), Int64.Type)"
                },
                {
                    "step": 8,
                    "content": "#\"Added CalendarQuarter\" = Table.AddColumn(#\"Added CalendarYear\", \"CalendarQuarter\", each \"Q\" & Text.From(Date.QuarterOfYear([DispatchDate])), type text)"
                },
                {
                    "step": 9,
                    "content": "#\"Added CalendarMonth\" = Table.AddColumn(#\"Added CalendarQuarter\", \"CalendarMonth\", each Date.Month([DispatchDate]), Int64.Type)"
                },
                {
                    "step": 10,
                    "content": "#\"Added CalendarMonthYear\" = Table.AddColumn(#\"Added CalendarMonth\", \"CalendarMonthYear\", each Date.ToText([DispatchDate], \"MMM yyyy\"), type text)"
                },
                {
                    "step": 11,
                    "content": "#\"Added CalendarMonthStart\" = Table.AddColumn(#\"Added CalendarMonthYear\", \"CalendarMonthStart\", each Date.StartOfMonth([DispatchDate]), type date)"
                },
                {
                    "step": 12,
                    "content": "#\"Added CalendarWeek\" = Table.AddColumn(#\"Added CalendarMonthStart\", \"CalendarWeek\", each Date.WeekOfYear([DispatchDate]), Int64.Type)"
                },
                {
                    "step": 13,
                    "content": "#\"Added CalendarWeekDay\" = Table.AddColumn(#\"Added CalendarWeek\", \"CalendarWeekDay\", each Date.DayOfWeekName([DispatchDate]), type text)"
                },
                {
                    "step": 14,
                    "content": "#\"Added CalendarDay\" = Table.AddColumn(#\"Added CalendarWeekDay\", \"CalendarDay\", each Date.Day([DispatchDate]), Int64.Type) in #\"Added CalendarDay\""
                }
            ]
        },
        {
            "name": "TruckMap",
            "table_name": "TruckMap",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "Trucks",
            "qlik_query": "\n\n// --- Source Part ---\nTruckMap:\r\nMAPPING LOAD\r\n    truck_id,\r\n    unit_number\r\nResident Trucks",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "truck_id",
                    "qlik_datatype": "STRING",
                    "fabric_column_name": "truck_id",
                    "fabric_datatype": "string",
                    "summarize_by": "none",
                    "is_hidden": false,
                    "format_string": "@"
                },
                {
                    "qlik_column_name": "unit_number",
                    "qlik_datatype": "NUMERIC",
                    "fabric_column_name": "unit_number",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = Trucks"
                },
                {
                    "step": 2,
                    "content": "#\"Distinct Rows\" = Table.Distinct(Source) in #\"Distinct Rows\""
                }
            ]
        },
        {
            "name": "TempCalendar",
            "table_name": "TempCalendar",
            "load_type": "resident",
            "source_type": "resident",
            "connection": null,
            "upstream_table": "Trips",
            "qlik_query": "\n\n// --- Source Part ---\nTempCalendar:\r\nLOAD\r\n    Min(DispatchDate) AS MinDate,\r\n    Max(DispatchDate) AS MaxDate\r\nResident Trips",
            "custom_sql": null,
            "columns": [
                {
                    "qlik_column_name": "MinDate",
                    "qlik_datatype": "NUMERIC",
                    "fabric_column_name": "MinDate",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                },
                {
                    "qlik_column_name": "MaxDate",
                    "qlik_datatype": "NUMERIC",
                    "fabric_column_name": "MaxDate",
                    "fabric_datatype": "double",
                    "summarize_by": "sum",
                    "is_hidden": false,
                    "format_string": "#,##0.00"
                }
            ],
            "confidence": {
                "score": 0.98,
                "score_out_of_100": 98,
                "percentage": "98%",
                "band": "high",
                "llm_score": 0.98,
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
                        "status": "skip"
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
                "penalties": [],
                "requires_review": false,
                "rationale": "Table structure, columns, and Power Query M expressions mapped with all checks passing."
            },
            "m_query": [
                {
                    "step": 1,
                    "content": "let Source = #table({\"MinDate\", \"MaxDate\"}, {{#date(2020, 1, 1), #date(2026, 12, 31)}}) in Source"
                }
            ]
        }
    ],
    "relationships": [
        {
            "name": "Trips.driver_id -> Drivers.driver_id",
            "qlik_key_field": "driver_id",
            "source_table": "Trips",
            "source_column": "driver_id",
            "target_table": "Drivers",
            "target_column": "driver_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "driver_id",
                "to_table": "Drivers",
                "to_column": "driver_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "e4431242-a315-54fb-8d0f-4ca40ea1d8ac"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'Drivers' mapped successfully."
            }
        },
        {
            "name": "Trips.driver_id -> DriverPerformance.driver_id",
            "qlik_key_field": "driver_id",
            "source_table": "Trips",
            "source_column": "driver_id",
            "target_table": "DriverPerformance",
            "target_column": "driver_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "driver_id",
                "to_table": "DriverPerformance",
                "to_column": "driver_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "1b543f3c-bed2-5116-816c-df875bf5a6a4"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'DriverPerformance' mapped successfully."
            }
        },
        {
            "name": "Drivers.driver_id -> DriverPerformance.driver_id",
            "qlik_key_field": "driver_id",
            "source_table": "Drivers",
            "source_column": "driver_id",
            "target_table": "DriverPerformance",
            "target_column": "driver_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Drivers",
                "from_column": "driver_id",
                "to_table": "DriverPerformance",
                "to_column": "driver_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "7f14b912-af2b-57b4-803f-5f43ddbf9b60"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Drivers' and 'DriverPerformance' mapped successfully."
            }
        },
        {
            "name": "Trips.truck_id -> Trucks.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trips",
            "source_column": "truck_id",
            "target_table": "Trucks",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "truck_id",
                "to_table": "Trucks",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "c966bdbd-33b5-5391-8722-ab301da110ec"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'Trucks' mapped successfully."
            }
        },
        {
            "name": "Trips.truck_id -> Maintenance.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trips",
            "source_column": "truck_id",
            "target_table": "Maintenance",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "truck_id",
                "to_table": "Maintenance",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "0358e3c2-cc8d-5416-a9e2-ed366bc39ace"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'Maintenance' mapped successfully."
            }
        },
        {
            "name": "Trips.truck_id -> TruckPerformance.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trips",
            "source_column": "truck_id",
            "target_table": "TruckPerformance",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "truck_id",
                "to_table": "TruckPerformance",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "c19934e5-8daf-5170-b6f6-21bd79cc38c5"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'TruckPerformance' mapped successfully."
            }
        },
        {
            "name": "Trips.truck_id -> MaintenanceByTruck.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trips",
            "source_column": "truck_id",
            "target_table": "MaintenanceByTruck",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "truck_id",
                "to_table": "MaintenanceByTruck",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "dfe70750-b91d-59e1-9ef7-859f9c869c23"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'MaintenanceByTruck' mapped successfully."
            }
        },
        {
            "name": "Trucks.truck_id -> Maintenance.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trucks",
            "source_column": "truck_id",
            "target_table": "Maintenance",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trucks",
                "from_column": "truck_id",
                "to_table": "Maintenance",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "71830c1c-ab34-5f0f-a447-7df2ea4ab209"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trucks' and 'Maintenance' mapped successfully."
            }
        },
        {
            "name": "Trucks.truck_id -> TruckPerformance.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trucks",
            "source_column": "truck_id",
            "target_table": "TruckPerformance",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trucks",
                "from_column": "truck_id",
                "to_table": "TruckPerformance",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "e3f3aada-b7ab-5428-a2c7-f3e237602379"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trucks' and 'TruckPerformance' mapped successfully."
            }
        },
        {
            "name": "Trucks.truck_id -> MaintenanceByTruck.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Trucks",
            "source_column": "truck_id",
            "target_table": "MaintenanceByTruck",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trucks",
                "from_column": "truck_id",
                "to_table": "MaintenanceByTruck",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "893dab63-2fcd-5974-a65d-caf85e07c548"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trucks' and 'MaintenanceByTruck' mapped successfully."
            }
        },
        {
            "name": "Maintenance.truck_id -> TruckPerformance.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Maintenance",
            "source_column": "truck_id",
            "target_table": "TruckPerformance",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Maintenance",
                "from_column": "truck_id",
                "to_table": "TruckPerformance",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "9eac0853-caa7-5c55-8534-1df5f44e62ed"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Maintenance' and 'TruckPerformance' mapped successfully."
            }
        },
        {
            "name": "Maintenance.truck_id -> MaintenanceByTruck.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "Maintenance",
            "source_column": "truck_id",
            "target_table": "MaintenanceByTruck",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Maintenance",
                "from_column": "truck_id",
                "to_table": "MaintenanceByTruck",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "ecdba711-d2c6-51bc-8965-e4cd5c951550"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Maintenance' and 'MaintenanceByTruck' mapped successfully."
            }
        },
        {
            "name": "TruckPerformance.truck_id -> MaintenanceByTruck.truck_id",
            "qlik_key_field": "truck_id",
            "source_table": "TruckPerformance",
            "source_column": "truck_id",
            "target_table": "MaintenanceByTruck",
            "target_column": "truck_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "TruckPerformance",
                "from_column": "truck_id",
                "to_table": "MaintenanceByTruck",
                "to_column": "truck_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "53977c54-7642-567b-b6e2-9afe8611d9ef"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'TruckPerformance' and 'MaintenanceByTruck' mapped successfully."
            }
        },
        {
            "name": "Trips.trailer_id -> Trailers.trailer_id",
            "qlik_key_field": "trailer_id",
            "source_table": "Trips",
            "source_column": "trailer_id",
            "target_table": "Trailers",
            "target_column": "trailer_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trailer_id",
                "to_table": "Trailers",
                "to_column": "trailer_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "5af54763-ad58-5311-a102-731b876e0079"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'Trailers' mapped successfully."
            }
        },
        {
            "name": "Loads.load_id -> Trips.load_id",
            "qlik_key_field": "load_id",
            "source_table": "Loads",
            "source_column": "load_id",
            "target_table": "Trips",
            "target_column": "load_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Loads",
                "from_column": "load_id",
                "to_table": "Trips",
                "to_column": "load_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "04cd68d9-950b-5a6f-a9e6-64bbe5cab47a"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Loads' and 'Trips' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> FuelPurchases.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "FuelPurchases",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "FuelPurchases",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "343fb011-99b6-502c-97dd-2200363827b3"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'FuelPurchases' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> DeliveryEvents.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "DeliveryEvents",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "DeliveryEvents",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "05d4c764-8dba-5a0b-b53d-32911274a238"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'DeliveryEvents' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> SafetyIncidents.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "SafetyIncidents",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "SafetyIncidents",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "15358fed-3cb0-586f-a092-52fc90674081"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'SafetyIncidents' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> FuelByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "FuelByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "FuelByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "61d748d1-6539-51e9-bd93-d4fd536e3f8d"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'FuelByTrip' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> DeliveryByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "DeliveryByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "DeliveryByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "761052f4-f26b-5db7-964b-a2ba29f94dd7"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'DeliveryByTrip' mapped successfully."
            }
        },
        {
            "name": "Trips.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "Trips",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "b7d36cad-9353-5f92-85fb-2af7ab623430"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "FuelPurchases.trip_id -> DeliveryEvents.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelPurchases",
            "source_column": "trip_id",
            "target_table": "DeliveryEvents",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelPurchases",
                "from_column": "trip_id",
                "to_table": "DeliveryEvents",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "3e9190ce-e974-5935-b02e-d42769b7d8c7"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelPurchases' and 'DeliveryEvents' mapped successfully."
            }
        },
        {
            "name": "FuelPurchases.trip_id -> SafetyIncidents.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelPurchases",
            "source_column": "trip_id",
            "target_table": "SafetyIncidents",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelPurchases",
                "from_column": "trip_id",
                "to_table": "SafetyIncidents",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "11366535-01cf-5543-8313-4f53ef735113"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelPurchases' and 'SafetyIncidents' mapped successfully."
            }
        },
        {
            "name": "FuelPurchases.trip_id -> FuelByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelPurchases",
            "source_column": "trip_id",
            "target_table": "FuelByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelPurchases",
                "from_column": "trip_id",
                "to_table": "FuelByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "ef00d1f1-3564-59b9-bab0-bdc270ea1ee2"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelPurchases' and 'FuelByTrip' mapped successfully."
            }
        },
        {
            "name": "FuelPurchases.trip_id -> DeliveryByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelPurchases",
            "source_column": "trip_id",
            "target_table": "DeliveryByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelPurchases",
                "from_column": "trip_id",
                "to_table": "DeliveryByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "483af162-4343-5d67-b9fa-be200900636d"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelPurchases' and 'DeliveryByTrip' mapped successfully."
            }
        },
        {
            "name": "FuelPurchases.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelPurchases",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelPurchases",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "53540ba3-f8fa-5387-b0fa-9a970126058f"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelPurchases' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "DeliveryEvents.trip_id -> SafetyIncidents.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "DeliveryEvents",
            "source_column": "trip_id",
            "target_table": "SafetyIncidents",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "DeliveryEvents",
                "from_column": "trip_id",
                "to_table": "SafetyIncidents",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "80842d54-9456-537e-9122-9354cd0dcc52"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'DeliveryEvents' and 'SafetyIncidents' mapped successfully."
            }
        },
        {
            "name": "DeliveryEvents.trip_id -> FuelByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "DeliveryEvents",
            "source_column": "trip_id",
            "target_table": "FuelByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "DeliveryEvents",
                "from_column": "trip_id",
                "to_table": "FuelByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "63c66be4-0850-5111-acb0-8e54bfc13b79"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'DeliveryEvents' and 'FuelByTrip' mapped successfully."
            }
        },
        {
            "name": "DeliveryEvents.trip_id -> DeliveryByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "DeliveryEvents",
            "source_column": "trip_id",
            "target_table": "DeliveryByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "DeliveryEvents",
                "from_column": "trip_id",
                "to_table": "DeliveryByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "8e89da38-e65f-5839-b733-e5bad3bd6c83"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'DeliveryEvents' and 'DeliveryByTrip' mapped successfully."
            }
        },
        {
            "name": "DeliveryEvents.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "DeliveryEvents",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "DeliveryEvents",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "aad26084-883e-5ff7-8052-7bf3f1f07132"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'DeliveryEvents' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "SafetyIncidents.trip_id -> FuelByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "SafetyIncidents",
            "source_column": "trip_id",
            "target_table": "FuelByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "SafetyIncidents",
                "from_column": "trip_id",
                "to_table": "FuelByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "bee799fd-e030-5905-9649-4658b391b48e"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'SafetyIncidents' and 'FuelByTrip' mapped successfully."
            }
        },
        {
            "name": "SafetyIncidents.trip_id -> DeliveryByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "SafetyIncidents",
            "source_column": "trip_id",
            "target_table": "DeliveryByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "SafetyIncidents",
                "from_column": "trip_id",
                "to_table": "DeliveryByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "6b3b6273-a93b-59f4-bbcb-e4ff9053bb49"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'SafetyIncidents' and 'DeliveryByTrip' mapped successfully."
            }
        },
        {
            "name": "SafetyIncidents.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "SafetyIncidents",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "SafetyIncidents",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "8702cace-167e-55a3-96f0-326684b14881"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'SafetyIncidents' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "FuelByTrip.trip_id -> DeliveryByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelByTrip",
            "source_column": "trip_id",
            "target_table": "DeliveryByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelByTrip",
                "from_column": "trip_id",
                "to_table": "DeliveryByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "27c3fa49-fa19-5b15-94cf-a622c0015e41"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelByTrip' and 'DeliveryByTrip' mapped successfully."
            }
        },
        {
            "name": "FuelByTrip.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "FuelByTrip",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "FuelByTrip",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "306f97c9-6bd1-5b12-bbfc-633e8f88d91b"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'FuelByTrip' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "DeliveryByTrip.trip_id -> SafetyByTrip.trip_id",
            "qlik_key_field": "trip_id",
            "source_table": "DeliveryByTrip",
            "source_column": "trip_id",
            "target_table": "SafetyByTrip",
            "target_column": "trip_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "DeliveryByTrip",
                "from_column": "trip_id",
                "to_table": "SafetyByTrip",
                "to_column": "trip_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "8db61516-174e-5fcc-b26d-c048d332fd1d"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'DeliveryByTrip' and 'SafetyByTrip' mapped successfully."
            }
        },
        {
            "name": "Trips.DispatchDate -> Calendar.DispatchDate",
            "qlik_key_field": "DispatchDate",
            "source_table": "Trips",
            "source_column": "DispatchDate",
            "target_table": "Calendar",
            "target_column": "DispatchDate",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Trips",
                "from_column": "DispatchDate",
                "to_table": "Calendar",
                "to_column": "DispatchDate",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "8284e7c8-4b0a-59a7-adf0-091163498844"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Trips' and 'Calendar' mapped successfully."
            }
        },
        {
            "name": "Customers.customer_id -> Loads.customer_id",
            "qlik_key_field": "customer_id",
            "source_table": "Customers",
            "source_column": "customer_id",
            "target_table": "Loads",
            "target_column": "customer_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Customers",
                "from_column": "customer_id",
                "to_table": "Loads",
                "to_column": "customer_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "a4ed51b2-0ea7-557a-b91c-294afb4d090a"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Customers' and 'Loads' mapped successfully."
            }
        },
        {
            "name": "Loads.route_id -> Routes.route_id",
            "qlik_key_field": "route_id",
            "source_table": "Loads",
            "source_column": "route_id",
            "target_table": "Routes",
            "target_column": "route_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Loads",
                "from_column": "route_id",
                "to_table": "Routes",
                "to_column": "route_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "866b89a5-0870-5faa-99c7-883cccfb3e58"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Loads' and 'Routes' mapped successfully."
            }
        },
        {
            "name": "Facilities.facility_id -> DeliveryEvents.facility_id",
            "qlik_key_field": "facility_id",
            "source_table": "Facilities",
            "source_column": "facility_id",
            "target_table": "DeliveryEvents",
            "target_column": "facility_id",
            "qlik_relationship_type": "many-to-one",
            "note": null,
            "fabric": {
                "from_table": "Facilities",
                "from_column": "facility_id",
                "to_table": "DeliveryEvents",
                "to_column": "facility_id",
                "cardinality": "manyToOne",
                "cross_filter_direction": "singleDirection",
                "is_active": true,
                "lineage_tag": "60a01a9c-92d7-5ee4-984c-f015c8adb102"
            },
            "confidence": {
                "score": 0.95,
                "score_out_of_100": 95,
                "percentage": "95%",
                "band": "high",
                "llm_score": 0.95,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Relationship between 'Facilities' and 'DeliveryEvents' mapped successfully."
            }
        }
    ],
    "measures": [
        {
            "name": "Total Revenue",
            "qlik_expression": "Sum(revenue)/1000000",
            "qlik_number_format": {},
            "tables": [
                "Loads"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Loads'[revenue]), 1000000, 0)",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "91098b09-6315-5012-8cb4-76e719439999"
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
                "rationale": "The Qlik expression 'Sum(revenue)/1000000' was converted to DAX 'DIVIDE(SUM('Loads'[revenue]), 1000000, 0)' with all syntax checks passing."
            }
        },
        {
            "name": "Customer Analytics",
            "qlik_expression": "Max( Aggr( Sum(revenue), customer_name ))",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Customers"
            ],
            "fabric": {
                "dax_expression": "MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "5a444008-2977-58aa-8afd-9a301f70d1f2"
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
                "rationale": "The Qlik expression 'Max( Aggr( Sum(revenue), customer_name ))' was converted to DAX 'MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "Maximum Trips by Truck",
            "qlik_expression": "Max( Aggr( Count(trip_id), truck_id ) )",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "FuelPurchases",
                "DeliveryEvents",
                "SafetyIncidents",
                "FuelByTrip",
                "DeliveryByTrip",
                "SafetyByTrip",
                "Trucks",
                "Maintenance",
                "TruckPerformance",
                "MaintenanceByTruck"
            ],
            "fabric": {
                "dax_expression": "MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "8dbb9c27-3953-55a5-b794-ee73660ad1b0"
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
                "rationale": "The Qlik expression 'Max( Aggr( Count(trip_id), truck_id ) )' was converted to DAX 'MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "Highest Revenue by Customer",
            "qlik_expression": "Max( Aggr( Sum(revenue), customer_name ) )",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Customers"
            ],
            "fabric": {
                "dax_expression": "MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "1b63a406-2922-5cb0-9dcf-d471af1453d0"
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
                "rationale": "The Qlik expression 'Max( Aggr( Sum(revenue), customer_name ) )' was converted to DAX 'MAXX(SUMMARIZE('Customers', 'Customers'[customer_name], \"@value\", SUM('Loads'[revenue])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "Average Trip Distance",
            "qlik_expression": "Avg(actual_distance_miles)",
            "qlik_number_format": {},
            "tables": [
                "Trips"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('Trips'[actual_distance_miles])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "e35b7be9-e127-541f-ad6a-bc4af4bb08cc"
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
                "rationale": "The Qlik expression 'Avg(actual_distance_miles)' was converted to DAX 'AVERAGE('Trips'[actual_distance_miles])' with all syntax checks passing."
            }
        },
        {
            "name": "Active Trailers",
            "qlik_expression": "Count({<trailer_status={'Active'}>} DISTINCT trailer_id)",
            "qlik_number_format": {},
            "tables": [
                "Trailers",
                "Trips"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(DISTINCTCOUNT('Trips'[trailer_id]), 'Trailers'[trailer_status] = \"Active\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "efd511ba-959e-5b93-8c68-f84eb5915b8d"
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
                "rationale": "The Qlik expression 'Count({<trailer_status={'Active'}>} DISTINCT trailer_id)' was converted to DAX 'CALCULATE(DISTINCTCOUNT('Trips'[trailer_id]), 'Trailers'[trailer_status] = \"Active\")' with all syntax checks passing."
            }
        },
        {
            "name": "Average Revenue per Load",
            "qlik_expression": "Avg(revenue)",
            "qlik_number_format": {},
            "tables": [
                "Loads"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('Loads'[revenue])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "ec7cf70c-2291-5cbb-9d68-2b9728cb6e1a"
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
                "rationale": "The Qlik expression 'Avg(revenue)' was converted to DAX 'AVERAGE('Loads'[revenue])' with all syntax checks passing."
            }
        },
        {
            "name": "High Value Revenue",
            "qlik_expression": "Sum({<RevenueBand={'High Value'}>} revenue)",
            "qlik_number_format": {},
            "tables": [
                "Loads"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\")",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "9e0aa5db-e86e-5f58-b721-d6dbdd9858ce"
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
                "rationale": "The Qlik expression 'Sum({<RevenueBand={'High Value'}>} revenue)' was converted to DAX 'CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\")' with all syntax checks passing."
            }
        },
        {
            "name": "Average Trip Duration",
            "qlik_expression": "Avg(actual_duration_hours)",
            "qlik_number_format": {},
            "tables": [
                "Trips"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('Trips'[actual_duration_hours])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "02209d34-c0d5-5a0b-b601-dbd7d263f297"
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
                "rationale": "The Qlik expression 'Avg(actual_duration_hours)' was converted to DAX 'AVERAGE('Trips'[actual_duration_hours])' with all syntax checks passing."
            }
        },
        {
            "name": "Total Trips",
            "qlik_expression": "Count(trip_id)",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "FuelPurchases",
                "DeliveryEvents",
                "SafetyIncidents",
                "FuelByTrip",
                "DeliveryByTrip",
                "SafetyByTrip"
            ],
            "fabric": {
                "dax_expression": "COUNT('Trips'[trip_id])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "ea0647f4-bb8e-5695-81ab-ea36102811b3"
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
                "rationale": "The Qlik expression 'Count(trip_id)' was converted to DAX 'COUNT('Trips'[trip_id])' with all syntax checks passing."
            }
        },
        {
            "name": "Average Revenue per Customer",
            "qlik_expression": "Num(     Sum(revenue) /     Count(DISTINCT customer_id),     '$#,##0' )",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Customers"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Loads'[revenue]), DISTINCTCOUNT('Customers'[customer_id]), 0)",
                "data_type": "decimal",
                "format_string": "$#,##0",
                "lineage_tag": "290c931b-09a5-5f54-b1d3-6d67170e6f7f"
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
                "rationale": "The Qlik expression 'Num(     Sum(revenue) /     Count(DISTINCT customer_id),     '$#,##0' )' was converted to DAX 'DIVIDE(SUM('Loads'[revenue]), DISTINCTCOUNT('Customers'[customer_id]), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "Total Drivers",
            "qlik_expression": "Count(DISTINCT driver_id)",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "Drivers",
                "DriverPerformance"
            ],
            "fabric": {
                "dax_expression": "DISTINCTCOUNT('Trips'[driver_id])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "68a17c3b-ad04-50fc-b2ce-020ad3d1aa60"
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
                "rationale": "The Qlik expression 'Count(DISTINCT driver_id)' was converted to DAX 'DISTINCTCOUNT('Trips'[driver_id])' with all syntax checks passing."
            }
        },
        {
            "name": "Driver Analytics",
            "qlik_expression": "Avg( Aggr( Sum(revenue), driver_id ))",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips",
                "Drivers",
                "DriverPerformance"
            ],
            "fabric": {
                "dax_expression": "AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "e05a035d-85ce-5856-a036-1afbc7f0beb3"
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
                "rationale": "The Qlik expression 'Avg( Aggr( Sum(revenue), driver_id ))' was converted to DAX 'AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "High Value Revenue %",
            "qlik_expression": "Num(     Sum({<RevenueBand={'High Value'}>} revenue)     /     Sum(revenue),     '0.0%' )",
            "qlik_number_format": {},
            "tables": [
                "Loads"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\"), SUM('Loads'[revenue]), 0)",
                "data_type": "decimal",
                "format_string": "0.0%",
                "lineage_tag": "d15eab55-18f2-558a-b3d8-3f6bde57dfa6"
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
                "rationale": "The Qlik expression 'Num(     Sum({<RevenueBand={'High Value'}>} revenue)     /     Sum(revenue),     '0.0%' )' was converted to DAX 'DIVIDE(CALCULATE(SUM('Loads'[revenue]), 'Loads'[RevenueBand] = \"High Value\"), SUM('Loads'[revenue]), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "Revenue per Mile",
            "qlik_expression": "Sum(revenue) / Sum(actual_distance_miles)",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Loads'[revenue]), SUM('Trips'[actual_distance_miles]), 0)",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "6a7f8c9d-ae59-5350-b000-d2098e25e5dd"
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
                "rationale": "The Qlik expression 'Sum(revenue) / Sum(actual_distance_miles)' was converted to DAX 'DIVIDE(SUM('Loads'[revenue]), SUM('Trips'[actual_distance_miles]), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "Revenue per Trip",
            "qlik_expression": "Sum(revenue) / Count(trip_id)",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips",
                "FuelPurchases",
                "DeliveryEvents",
                "SafetyIncidents",
                "FuelByTrip",
                "DeliveryByTrip",
                "SafetyByTrip"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Loads'[revenue]), COUNT('Trips'[trip_id]), 0)",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "be478467-bb36-5135-92b2-1280a432b523"
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
                "rationale": "The Qlik expression 'Sum(revenue) / Count(trip_id)' was converted to DAX 'DIVIDE(SUM('Loads'[revenue]), COUNT('Trips'[trip_id]), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "Completed Trips",
            "qlik_expression": "Count({<trip_status={'Completed'}>} trip_id)",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "FuelPurchases",
                "DeliveryEvents",
                "SafetyIncidents",
                "FuelByTrip",
                "DeliveryByTrip",
                "SafetyByTrip"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(COUNT('Trips'[trip_id]), 'Trips'[trip_status] = \"Completed\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "d2d76ee4-575e-578f-bce6-66873c2a5729"
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
                "rationale": "The Qlik expression 'Count({<trip_status={'Completed'}>} trip_id)' was converted to DAX 'CALCULATE(COUNT('Trips'[trip_id]), 'Trips'[trip_status] = \"Completed\")' with all syntax checks passing."
            }
        },
        {
            "name": "Average Revenue per Driver",
            "qlik_expression": "Avg( Aggr( Sum(revenue), driver_id ) )",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips",
                "Drivers",
                "DriverPerformance"
            ],
            "fabric": {
                "dax_expression": "AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "b48816ec-1244-5c22-ae05-174fd572bc6d"
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
                "rationale": "The Qlik expression 'Avg( Aggr( Sum(revenue), driver_id ) )' was converted to DAX 'AVERAGEX(SUMMARIZE('Trips', 'Trips'[driver_id], \"@value\", SUM('Loads'[revenue])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "Completed Trip Revenue",
            "qlik_expression": "Sum({<trip_status={'Completed'}>} revenue)",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "Loads"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(SUM('Loads'[revenue]), 'Trips'[trip_status] = \"Completed\")",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "86eaa52e-08bb-55ec-abcb-003200199e96"
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
                "rationale": "The Qlik expression 'Sum({<trip_status={'Completed'}>} revenue)' was converted to DAX 'CALCULATE(SUM('Loads'[revenue]), 'Trips'[trip_status] = \"Completed\")' with all syntax checks passing."
            }
        },
        {
            "name": "Active Trucks",
            "qlik_expression": "Count({<truck_status={'Active'}>} DISTINCT truck_id)",
            "qlik_number_format": {},
            "tables": [
                "Trucks",
                "Trips",
                "Maintenance",
                "TruckPerformance",
                "MaintenanceByTruck"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[truck_status] = \"Active\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "c15447ed-173b-597c-9fbd-28e01a6288cc"
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
                "rationale": "The Qlik expression 'Count({<truck_status={'Active'}>} DISTINCT truck_id)' was converted to DAX 'CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[truck_status] = \"Active\")' with all syntax checks passing."
            }
        },
        {
            "name": "Average Fuel Efficiency",
            "qlik_expression": "Sum(actual_distance_miles) / Sum(fuel_gallons_used)",
            "qlik_number_format": {},
            "tables": [
                "Trips"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Trips'[actual_distance_miles]), SUM('Trips'[fuel_gallons_used]), 0)",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "e65eef8f-660c-5c9d-a653-c6f0286b46d3"
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
                "rationale": "The Qlik expression 'Sum(actual_distance_miles) / Sum(fuel_gallons_used)' was converted to DAX 'DIVIDE(SUM('Trips'[actual_distance_miles]), SUM('Trips'[fuel_gallons_used]), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "High Value Loads",
            "qlik_expression": "Count({<RevenueBand={'High Value'}>} DISTINCT load_id)",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(DISTINCTCOUNT('Trips'[load_id]), 'Loads'[RevenueBand] = \"High Value\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "941ed71d-c9cd-5bf8-9c14-71585bf98f31"
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
                "rationale": "The Qlik expression 'Count({<RevenueBand={'High Value'}>} DISTINCT load_id)' was converted to DAX 'CALCULATE(DISTINCTCOUNT('Trips'[load_id]), 'Loads'[RevenueBand] = \"High Value\")' with all syntax checks passing."
            }
        },
        {
            "name": "Fleet Operations",
            "qlik_expression": "Max( Aggr( Count(trip_id), truck_id ))",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "FuelPurchases",
                "DeliveryEvents",
                "SafetyIncidents",
                "FuelByTrip",
                "DeliveryByTrip",
                "SafetyByTrip",
                "Trucks",
                "Maintenance",
                "TruckPerformance",
                "MaintenanceByTruck"
            ],
            "fabric": {
                "dax_expression": "MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "2ef29338-e4c0-5eed-a44e-0f4e6a6cc9aa"
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
                "rationale": "The Qlik expression 'Max( Aggr( Count(trip_id), truck_id ))' was converted to DAX 'MAXX(SUMMARIZE('Trips', 'Trips'[truck_id], \"@value\", COUNT('Trips'[trip_id])), [@value])' with all syntax checks passing."
            }
        },
        {
            "name": "Revenue %",
            "qlik_expression": "Num(Sum(revenue)/Sum(TOTAL revenue),'0.0%')",
            "qlik_number_format": {},
            "tables": [
                "Loads"
            ],
            "fabric": {
                "dax_expression": "DIVIDE(SUM('Loads'[revenue]), CALCULATE(SUM('Loads'[revenue]), ALLSELECTED()), 0)",
                "data_type": "decimal",
                "format_string": "0.0%",
                "lineage_tag": "f72e061a-527b-5da5-a953-892acb27092f"
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
                "rationale": "The Qlik expression 'Num(Sum(revenue)/Sum(TOTAL revenue),'0.0%')' was converted to DAX 'DIVIDE(SUM('Loads'[revenue]), CALCULATE(SUM('Loads'[revenue]), ALLSELECTED()), 0)' with all syntax checks passing."
            }
        },
        {
            "name": "On-Time Delivery %",
            "qlik_expression": "Avg(on_time_flag)*100",
            "qlik_number_format": {},
            "tables": [
                "DeliveryEvents"
            ],
            "fabric": {
                "dax_expression": "AVERAGE('DeliveryEvents'[on_time_flag])*100",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "fae51d1f-d8f9-5b55-99bd-a56967d5ec3d"
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
                "rationale": "The Qlik expression 'Avg(on_time_flag)*100' was converted to DAX 'AVERAGE('DeliveryEvents'[on_time_flag])*100' with all syntax checks passing."
            }
        },
        {
            "name": "Total Loads",
            "qlik_expression": "Count(load_id)",
            "qlik_number_format": {},
            "tables": [
                "Loads",
                "Trips"
            ],
            "fabric": {
                "dax_expression": "COUNT('Trips'[load_id])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "dc568f16-f764-5701-bf95-6f1a21fe4d5b"
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
                "rationale": "The Qlik expression 'Count(load_id)' was converted to DAX 'COUNT('Trips'[load_id])' with all syntax checks passing."
            }
        },
        {
            "name": "Total Customers",
            "qlik_expression": "Count(DISTINCT customer_id)",
            "qlik_number_format": {},
            "tables": [
                "Customers",
                "Loads"
            ],
            "fabric": {
                "dax_expression": "DISTINCTCOUNT('Customers'[customer_id])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "0902181d-1af0-50ef-8642-3b06b993e9f3"
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
                "rationale": "The Qlik expression 'Count(DISTINCT customer_id)' was converted to DAX 'DISTINCTCOUNT('Customers'[customer_id])' with all syntax checks passing."
            }
        },
        {
            "name": "Total Maintainane Cost",
            "qlik_expression": "Sum(maintenance_total_cost)",
            "qlik_number_format": {},
            "tables": [
                "Maintenance"
            ],
            "fabric": {
                "dax_expression": "SUM('Maintenance'[maintenance_total_cost])",
                "data_type": "decimal",
                "format_string": "#,##0.00",
                "lineage_tag": "77f41ac7-0c8c-5611-814a-bcf9899d6369"
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
                "rationale": "The Qlik expression 'Sum(maintenance_total_cost)' was converted to DAX 'SUM('Maintenance'[maintenance_total_cost])' with all syntax checks passing."
            }
        },
        {
            "name": "Diesel Trucks",
            "qlik_expression": "Count({<fuel_type={'Diesel'}>} DISTINCT truck_id)",
            "qlik_number_format": {},
            "tables": [
                "Trucks",
                "Trips",
                "Maintenance",
                "TruckPerformance",
                "MaintenanceByTruck"
            ],
            "fabric": {
                "dax_expression": "CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[fuel_type] = \"Diesel\")",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "f6f5cf4a-1ce0-556e-8a42-57c0aa05be76"
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
                "rationale": "The Qlik expression 'Count({<fuel_type={'Diesel'}>} DISTINCT truck_id)' was converted to DAX 'CALCULATE(DISTINCTCOUNT('Trips'[truck_id]), 'Trucks'[fuel_type] = \"Diesel\")' with all syntax checks passing."
            }
        },
        {
            "name": "Fleet Size",
            "qlik_expression": "Count(DISTINCT truck_id)",
            "qlik_number_format": {},
            "tables": [
                "Trips",
                "Trucks",
                "Maintenance",
                "TruckPerformance",
                "MaintenanceByTruck"
            ],
            "fabric": {
                "dax_expression": "DISTINCTCOUNT('Trips'[truck_id])",
                "data_type": "string",
                "format_string": "#,##0.00",
                "lineage_tag": "15746ebf-8cf3-5cb4-aa70-041d190332e4"
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
                "rationale": "The Qlik expression 'Count(DISTINCT truck_id)' was converted to DAX 'DISTINCTCOUNT('Trips'[truck_id])' with all syntax checks passing."
            }
        },
        {
            "name": "Total Revenue Trips",
            "qlik_expression": "Pick(     $(vMeasure),     Sum(revenue)/1000000,     Count(trip_id),     Count(DISTINCT customer_id),     Count(DISTINCT driver_id) )",
            "dax_expression": "SUM('Loads'[revenue])",
            "tables": [
                "Trips"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Trips",
                "dax_expression": "SUM('Loads'[revenue])",
                "format_string": "#,##0.00",
                "tmdl": "measure 'Total Revenue Trips' = SUM('Loads'[revenue])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Total Revenue Trips'."
            }
        },
        {
            "name": "Avg(idle_time_hours)",
            "qlik_expression": "Avg(idle_time_hours)",
            "dax_expression": "AVERAGE('Trips'[idle_time_hours])",
            "tables": [
                "Trips"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Trips",
                "dax_expression": "AVERAGE('Trips'[idle_time_hours])",
                "format_string": "#,##0.00",
                "tmdl": "measure 'Avg(idle_time_hours)' = AVERAGE('Trips'[idle_time_hours])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Avg(idle_time_hours)'."
            }
        },
        {
            "name": "Avg(actual_distance_miles)",
            "qlik_expression": "Avg(actual_distance_miles)",
            "dax_expression": "AVERAGE('Trips'[actual_distance_miles])",
            "tables": [
                "Trips"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Trips",
                "dax_expression": "AVERAGE('Trips'[actual_distance_miles])",
                "format_string": "#,##0.00",
                "tmdl": "measure 'Avg(actual_distance_miles)' = AVERAGE('Trips'[actual_distance_miles])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Avg(actual_distance_miles)'."
            }
        },
        {
            "name": "Avg(average_mpg)",
            "qlik_expression": "Avg(average_mpg)",
            "dax_expression": "AVERAGE('Trips'[average_mpg])",
            "tables": [
                "Trips"
            ],
            "is_stub": true,
            "fabric": {
                "table": "Trips",
                "dax_expression": "AVERAGE('Trips'[average_mpg])",
                "format_string": "#,##0.00",
                "tmdl": "measure 'Avg(average_mpg)' = AVERAGE('Trips'[average_mpg])"
            },
            "confidence": {
                "score": 0.9,
                "band": "high",
                "llm_score": 0.9,
                "checks": [],
                "penalties": [],
                "requires_review": false,
                "rationale": "Derived DAX measure for visual field 'Avg(average_mpg)'."
            }
        }
    ],
    "dimensions": [
        {
            "name": "Driver",
            "qlik_expression": "",
            "qlik_datatype": "STRING (CALCULATED)",
            "nature": "TEXT",
            "tables": [
                "Drivers"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Drivers",
                "lineage_tag": "947645c7-0d61-4165-b8a9-187c1930d383"
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
            "name": "YearMonth",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER",
            "nature": "INTEGER",
            "tables": [
                "DeliveryEvents"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "DeliveryEvents",
                "lineage_tag": "441c9bad-bdfa-4146-a927-ed58d4cad078"
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
            "name": "Trip Status",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Trips"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Trips",
                "lineage_tag": "37d55f14-6912-47f1-b104-047f8d5b7ad3"
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
            "name": "Load Month",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER (CALCULATED)",
            "nature": "INTEGER",
            "tables": [
                "Loads"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "Loads",
                "lineage_tag": "f1ab5cc8-c022-49cb-9faf-b22805655daf"
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
            "name": "Customer",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Customers"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Customers",
                "lineage_tag": "ad44b473-85ae-441c-828a-b2ae1513b590"
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
            "name": "Route",
            "qlik_expression": "",
            "qlik_datatype": "STRING (CALCULATED)",
            "nature": "TEXT",
            "tables": [
                "Routes"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Routes",
                "lineage_tag": "ec060a65-33fb-4fae-9232-2c254d0c1ae3"
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
                "DeliveryEvents"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "DeliveryEvents",
                "lineage_tag": "11d16be9-4b60-48a5-8c27-34f989810e09"
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
            "name": "Load Type",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Loads"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Loads",
                "lineage_tag": "a256c203-461f-4b35-b21c-87f3643f1414"
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
            "name": "Booking Type",
            "qlik_expression": "",
            "qlik_datatype": "STRING",
            "nature": "TEXT",
            "tables": [
                "Loads"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "string",
                "table": "Loads",
                "lineage_tag": "79611639-2856-4fe8-ba23-ac5126dfb329"
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
            "name": "Truck",
            "qlik_expression": "",
            "qlik_datatype": "NUMBER (CALCULATED)",
            "nature": "INTEGER",
            "tables": [
                "Trucks"
            ],
            "limitations": [],
            "fabric": {
                "dax_expression": "",
                "is_calculated": false,
                "data_type": "number",
                "table": "Trucks",
                "lineage_tag": "b96395ef-7baa-40a9-a0a1-15b6500a09b4"
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
                    "title": "RcsrXpD",
                    "visual_name": "RcsrXpD",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Revenue",
                        "title_font_size": "20px",
                        "title_font_family": "Abril Fatface, serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                    "title": "Total Revenue",
                    "name": "Total Revenue",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 0,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Revenue",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Revenue",
                        "title_font_size": "20px",
                        "title_font_family": "Abril Fatface, serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                            "font_size": "20px",
                            "font_family": "Abril Fatface, serif",
                            "show": false
                        },
                        "subtitle": {
                            "color": "#8b8b8b"
                        },
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "title": {
                                    "subTitle": {
                                        "color": {
                                            "index": -1,
                                            "color": "#8b8b8b",
                                            "alpha": 1
                                        }
                                    },
                                    "main": {
                                        "fontSize": "20px",
                                        "fontFamily": "Abril Fatface, serif"
                                    }
                                },
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 0.63
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
                            },
                            {
                                "key": "useAdvancedMode",
                                "useAdvancedMode": true
                            },
                            {
                                "key": "simpleSettings",
                                "simpleFontSize": 0.6
                            },
                            {
                                "key": "firstMeasureTitle",
                                "label": {
                                    "name": {
                                        "fontSize": {
                                            "fluid": 0.6
                                        },
                                        "fontStyle": [
                                            "bold"
                                        ]
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                                "qFmt": "$#,##0.0M",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "text_align": "center",
                        "backgroundColor": "#99cfcd",
                        "fontSize": "20px"
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
                    "title": "pReKpR",
                    "visual_name": "pReKpR",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 8,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Trips"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Trips",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                    "title": "Total Trips",
                    "name": "Total Trips",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 8,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 427,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Trips",
                            "visible": true
                        },
                        "general": {
                            "x": 427,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Trips"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Trips",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 1
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
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
                                            "fluid": 0.6
                                        },
                                        "fontStyle": [
                                            "bold"
                                        ]
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                        "backgroundColor": "#99cfcd",
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
                    "title": "sWRr",
                    "visual_name": "sWRr",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Customers"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Customers",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                    "title": "Total Customers",
                    "name": "Total Customers",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 640,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Customers",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Customers"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Customers",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 1
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
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
                                            "fluid": 0.6
                                        },
                                        "fontStyle": [
                                            "bold"
                                        ]
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                        "backgroundColor": "#99cfcd",
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
                    "title": "cRfsjp",
                    "visual_name": "cRfsjp",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 16,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Drivers"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Drivers",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                    "title": "Total Drivers",
                    "name": "Total Drivers",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 16,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 853,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Total Drivers",
                            "visible": true
                        },
                        "general": {
                            "x": 853,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Total Drivers"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Total Drivers",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 1
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
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
                                            "fluid": 0.6
                                        },
                                        "fontStyle": [
                                            "bold"
                                        ]
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                        "backgroundColor": "#99cfcd",
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
                    "title": "FEPPP",
                    "visual_name": "FEPPP",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 20,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Fleet Size"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Fleet Size",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "20px",
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
                    "title": "Fleet Size",
                    "name": "Fleet Size",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 20,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 1067,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Fleet Size",
                            "visible": true
                        },
                        "general": {
                            "x": 1067,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Fleet Size"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Fleet Size",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "20px",
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
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "20px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "20px",
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 1
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
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
                                        "fontStyle": [
                                            "bold"
                                        ],
                                        "fontSize": {
                                            "fluid": 0.6
                                        }
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                        "backgroundColor": "#99cfcd",
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
                    "title": "xbTxPjC",
                    "visual_name": "xbTxPjC",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 12,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                    ],
                    "x_axis": [
                        "Load Month"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                    "name": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 12,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 0,
                        "y": 206,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 206,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                    ],
                    "x_axis_fields": [
                        "Load Month"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "auto": false,
                        "mode": "primary",
                        "single_color": "#002833",
                        "raw_single_color": "#002833",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": -1,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "on"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            },
                            {
                                "key": "line",
                                "style": {
                                    "lineThickness": 2
                                }
                            },
                            {
                                "key": "axis"
                            },
                            {
                                "key": "label"
                            },
                            {
                                "key": "legend"
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
                                "color": "#002833",
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
                        "data_colors": {
                            "primary": "#002833",
                            "mode": "primary",
                            "auto": false
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
                                "qFmt": "$#,##0.0M",
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
                    "title": "hqpgX",
                    "visual_name": "hqpgX",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 12,
                    "colspan": 12,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top 10 Customers by Revenue",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "16px",
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
                    "title": "Top 10 Customers by Revenue",
                    "name": "Top 10 Customers by Revenue",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 12,
                        "colspan": 12,
                        "rowspan": 6,
                        "x": 640,
                        "y": 206,
                        "width": 640,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Top 10 Customers by Revenue",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 206,
                            "width": 640,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top 10 Customers by Revenue",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "16px",
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
                        "auto": false,
                        "mode": "primary",
                        "single_color": "#b83e51",
                        "raw_single_color": "#b83e51",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": -1,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "on"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "borderRadius": "16px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "16px"
                            }
                        ],
                        "colorScheme": {
                            "auto": false,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true,
                                "quarantine": {
                                    "isCustomFormatted": false
                                }
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": -1,
                                "color": "#b83e51",
                                "alpha": 1
                            },
                            "useDimColVal": true,
                            "useMeasureGradient": false,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "12",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10,
                            "altLabel": "AjfgE",
                            "byMeasureDef": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
                            },
                            "byDimDef": {
                                "label": "SJWVwe",
                                "key": "SJWVwe",
                                "type": "libraryItem"
                            }
                        },
                        "data_colors": {
                            "primary": "#b83e51",
                            "mode": "primary",
                            "auto": false,
                            "by_measure": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
                            },
                            "by_dimension": {
                                "label": "SJWVwe",
                                "key": "SJWVwe",
                                "type": "libraryItem"
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
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "$#,##0.0M",
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
                    "title": "JQqMHER",
                    "visual_name": "JQqMHER",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 8,
                    "row": 18,
                    "colspan": 8,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top 10 Routes by Revenue",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Top 10 Routes by Revenue",
                    "name": "Top 10 Routes by Revenue",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 8,
                        "row": 18,
                        "colspan": 8,
                        "rowspan": 6,
                        "x": 427,
                        "y": 309,
                        "width": 427,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Top 10 Routes by Revenue",
                            "visible": true
                        },
                        "general": {
                            "x": 427,
                            "y": 309,
                            "width": 427,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top 10 Routes by Revenue",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "auto": false,
                        "mode": "byMeasure",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
                        "colorScheme": {
                            "auto": false,
                            "mode": "byMeasure",
                            "formatting": {
                                "numFormatFromTemplate": true,
                                "quarantine": {
                                    "isCustomFormatted": false
                                }
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
                            "measureMax": 10,
                            "altLabel": "AjfgE",
                            "byMeasureDef": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
                            }
                        },
                        "data_colors": {
                            "mode": "byMeasure",
                            "auto": false,
                            "by_measure": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
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
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "$#,##0.0M",
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
                    "title": "RJhBz",
                    "visual_name": "RJhBz",
                    "object_category": "other",
                    "chart_type": "piechart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 16,
                    "row": 18,
                    "colspan": 8,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Loads"
                    ],
                    "x_axis": [
                        "Load Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Loads by Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "donutChart",
                    "bi_type": "donutChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Loads by Type",
                    "name": "Loads by Type",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 16,
                        "row": 18,
                        "colspan": 8,
                        "rowspan": 6,
                        "x": 853,
                        "y": 309,
                        "width": 427,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "donutChart",
                        "title": {
                            "text": "Loads by Type",
                            "visible": true
                        },
                        "general": {
                            "x": 853,
                            "y": 309,
                            "width": 427,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                    "y_axis_fields": [
                        "Total Loads"
                    ],
                    "x_axis_fields": [
                        "Load Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Loads by Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
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
                        "auto": false,
                        "mode": "byDimension",
                        "dimension_scheme": "100",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "100",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "borderRadius": "15px",
                        "innerRadius": 0.55,
                        "strokeColor": "#FFFFFF",
                        "components": [
                            {
                                "key": "slices",
                                "style": {
                                    "strokeWidth": "none",
                                    "strokeColor": {
                                        "index": -1,
                                        "color": "#FFFFFF"
                                    },
                                    "cornerRadius": 0,
                                    "innerRadius": 0.55
                                }
                            },
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
                        "colorScheme": {
                            "auto": false,
                            "mode": "byDimension",
                            "formatting": {
                                "numFormatFromTemplate": true,
                                "quarantine": {
                                    "isCustomFormatted": false
                                }
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": false,
                            "useMeasureGradient": false,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "100",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10,
                            "altLabel": "gXFAXcp",
                            "byDimDef": {
                                "label": "gXFAXcp",
                                "key": "gXFAXcp",
                                "type": "libraryItem"
                            },
                            "byMeasureDef": {
                                "label": "pSzSnUp",
                                "key": "pSzSnUp",
                                "type": "libraryItem"
                            }
                        },
                        "data_colors": {
                            "mode": "byDimension",
                            "auto": false,
                            "by_measure": {
                                "label": "pSzSnUp",
                                "key": "pSzSnUp",
                                "type": "libraryItem"
                            },
                            "by_dimension": {
                                "label": "gXFAXcp",
                                "key": "gXFAXcp",
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
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "DmejKEM",
                    "visual_name": "DmejKEM",
                    "object_category": "other",
                    "chart_type": "sn-table",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 24,
                    "colspan": 24,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue",
                        "Total Loads",
                        "Average Revenue per Load",
                        "Revenue %"
                    ],
                    "x_axis": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top Customers",
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
                    "title": "Top Customers",
                    "name": "Top Customers",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
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
                        "visualType": "tableEx",
                        "title": {
                            "text": "Top Customers",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 411,
                            "width": 1280,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                    "y_axis_fields": [
                        "Total Revenue",
                        "Total Loads",
                        "Average Revenue per Load",
                        "Revenue %"
                    ],
                    "x_axis_fields": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top Customers",
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
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "$#,##0.0M",
                                "qDec": ".",
                                "qThou": ","
                            },
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
                                "qType": "U",
                                "qnDec": 10,
                                "qUseThou": 0
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
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "mpV",
                    "visual_name": "mpV",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Customer",
                        "title_color": "#c25dab",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Customer",
                    "name": "Customer",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 0,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Customer",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Customer",
                        "title_color": "#c25dab",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                            "color": "#c25dab",
                            "show": false
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "title": {
                                    "main": {
                                        "color": {
                                            "index": -1,
                                            "color": "#c25dab",
                                            "alpha": 1
                                        }
                                    }
                                }
                            }
                        ],
                        "legend": {
                            "show": false
                        },
                        "titleColor": "#c25dab"
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
                    "title": "JxhYr",
                    "visual_name": "JxhYr",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Route",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Route",
                    "name": "Route",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 640,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Route",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Route",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
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
                    "title": "JVqkaP",
                    "visual_name": "JVqkaP",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 20,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Load Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Load Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Load Type",
                    "name": "Load Type",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 20,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 1067,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Load Type",
                            "visible": true
                        },
                        "general": {
                            "x": 1067,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Load Type"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Load Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
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
                    "title": "FanfT",
                    "visual_name": "FanfT",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 4,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Driver"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Driver",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Driver",
                    "name": "Driver",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 4,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 213,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Driver",
                            "visible": true
                        },
                        "general": {
                            "x": 213,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Driver"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Driver",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
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
                    "title": "yuQxa",
                    "visual_name": "yuQxa",
                    "object_category": "other",
                    "chart_type": "piechart",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 18,
                    "colspan": 8,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Loads"
                    ],
                    "x_axis": [
                        "Booking Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Loads by Booking Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "donutChart",
                    "bi_type": "donutChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Loads by Booking Type",
                    "name": "Loads by Booking Type",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 18,
                        "colspan": 8,
                        "rowspan": 6,
                        "x": 0,
                        "y": 309,
                        "width": 427,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "donutChart",
                        "title": {
                            "text": "Loads by Booking Type",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 309,
                            "width": 427,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                    "y_axis_fields": [
                        "Total Loads"
                    ],
                    "x_axis_fields": [
                        "Booking Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Loads by Booking Type",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
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
                        "auto": false,
                        "mode": "byDimension",
                        "dimension_scheme": "100",
                        "measure_scheme": "sg",
                        "palette_index": 6,
                        "palette_scheme": "100",
                        "is_multicolor": true,
                        "use_base_colors": "off"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "borderRadius": "15px",
                        "innerRadius": 0.55,
                        "strokeColor": "#FFFFFF",
                        "components": [
                            {
                                "key": "slices",
                                "style": {
                                    "strokeWidth": "none",
                                    "strokeColor": {
                                        "index": -1,
                                        "color": "#FFFFFF"
                                    },
                                    "cornerRadius": 0,
                                    "innerRadius": 0.55
                                }
                            },
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
                        "colorScheme": {
                            "auto": false,
                            "mode": "byDimension",
                            "formatting": {
                                "numFormatFromTemplate": true,
                                "quarantine": {
                                    "isCustomFormatted": false
                                }
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 6
                            },
                            "useDimColVal": false,
                            "useMeasureGradient": true,
                            "persistent": false,
                            "expressionIsColor": true,
                            "measureScheme": "sg",
                            "reverseScheme": false,
                            "dimensionScheme": "100",
                            "autoMinMax": true,
                            "measureMin": 0,
                            "measureMax": 10,
                            "altLabel": "mZVtGZ",
                            "byMeasureDef": {
                                "label": "pSzSnUp",
                                "key": "pSzSnUp",
                                "type": "libraryItem"
                            },
                            "byDimDef": {
                                "label": "mZVtGZ",
                                "key": "mZVtGZ",
                                "type": "libraryItem"
                            }
                        },
                        "data_colors": {
                            "mode": "byDimension",
                            "auto": false,
                            "by_measure": {
                                "label": "pSzSnUp",
                                "key": "pSzSnUp",
                                "type": "libraryItem"
                            },
                            "by_dimension": {
                                "label": "mZVtGZ",
                                "key": "mZVtGZ",
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
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "kqbVa",
                    "visual_name": "kqbVa",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 16,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Load Month"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Load Month",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Load Month",
                    "name": "Load Month",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 16,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 853,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Load Month",
                            "visible": true
                        },
                        "general": {
                            "x": 853,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Load Month"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Load Month",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
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
                    "title": "pkmKCqm",
                    "visual_name": "pkmKCqm",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 8,
                    "row": 3,
                    "colspan": 4,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Truck"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Truck",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                    "title": "Truck",
                    "name": "Truck",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 8,
                        "row": 3,
                        "colspan": 4,
                        "rowspan": 5,
                        "x": 427,
                        "y": 51,
                        "width": 213,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Truck",
                            "visible": true
                        },
                        "general": {
                            "x": 427,
                            "y": 51,
                            "width": 213,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [
                        "Truck"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Truck",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border_radius": "15px",
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
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px"
                            }
                        ],
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
                    "title": "grbmmG",
                    "visual_name": "grbmmG",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 4,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Revenue per Load"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Revenue per Load",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                    "title": "Average Revenue per Load",
                    "name": "Average Revenue per Load",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 4,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 213,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Revenue per Load",
                            "visible": true
                        },
                        "general": {
                            "x": 213,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Revenue per Load"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Revenue per Load",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#99cfcd",
                        "border_radius": "15px",
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
                        "background": {
                            "color": "#99cfcd"
                        },
                        "borderRadius": "15px",
                        "components": [
                            {
                                "key": "general",
                                "borderRadius": "15px",
                                "bgColor": {
                                    "color": {
                                        "index": 2,
                                        "color": "#99cfcd",
                                        "alpha": 1
                                    }
                                }
                            },
                            {
                                "key": "textAlignment"
                            },
                            {
                                "key": "textBehavior",
                                "textBehavior": "relative"
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
                                            "fluid": 0.6
                                        },
                                        "fontStyle": [
                                            "bold"
                                        ]
                                    }
                                }
                            },
                            {
                                "key": "firstMeasureValue"
                            },
                            {
                                "key": "secondMeasureTitle"
                            },
                            {
                                "key": "secondMeasureValue"
                            }
                        ],
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
                        "backgroundColor": "#99cfcd",
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
                    "title": "hSFqB",
                    "visual_name": "hSFqB",
                    "object_category": "other",
                    "chart_type": "qlik-variable-input",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 10,
                    "colspan": 12,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top N Customers",
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
                    "supported": false,
                    "status": "unmapped",
                    "title": "Top N Customers",
                    "name": "Top N Customers",
                    "object_category": "other",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": "Re-create using a single-value slicer bound to a parameter table.",
                    "layout": {
                        "col": 12,
                        "row": 10,
                        "colspan": 12,
                        "rowspan": 2,
                        "x": 640,
                        "y": 171,
                        "width": 640,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Top N Customers",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 171,
                            "width": 640,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct Power BI visual equivalent. It can be approximated with a textbox for documentation or replaced by a Power BI parameter input (e.g., using a slicer or Power Query parameter). Re-create using a single-value slicer bound to a parameter table.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Top N Customers",
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
                    "score": 0.6,
                    "score_out_of_100": 60,
                    "percentage": "60%",
                    "band": "medium",
                    "llm_score": 0.6,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "fail"
                        }
                    ],
                    "penalties": [],
                    "requires_review": true,
                    "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct Power BI visual equivalent. It can be approximated with a textbox for documentation or replaced by a Power BI parameter input (e.g., using a slicer or Power Query parameter). Re-create using a single-value slicer bound to a parameter table."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "dgEzRMq",
                    "visual_name": "dgEzRMq",
                    "object_category": "other",
                    "chart_type": "qlik-variable-input",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 10,
                    "colspan": 12,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Metric",
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
                    "supported": false,
                    "status": "unmapped",
                    "title": "Metric",
                    "name": "Metric",
                    "object_category": "other",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": "Re-create using a single-value slicer bound to a parameter table.",
                    "layout": {
                        "col": 0,
                        "row": 10,
                        "colspan": 12,
                        "rowspan": 2,
                        "x": 0,
                        "y": 171,
                        "width": 640,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "slicer",
                        "title": {
                            "text": "Metric",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 171,
                            "width": 640,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct equivalent in Power BI/Fabric. The closest approximation would be a textbox or custom visual, but native support is unavailable. Marked as unsupported with an unmapped status and a recommendation to implement a custom Power Apps visual or use a parameter input via Power BI's query parameters. Re-create using a single-value slicer bound to a parameter table.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Metric",
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
                    "score": 0.6,
                    "score_out_of_100": 60,
                    "percentage": "60%",
                    "band": "medium",
                    "llm_score": 0.6,
                    "checks": [
                        {
                            "id": "visual_type_recognized",
                            "status": "fail"
                        }
                    ],
                    "penalties": [],
                    "requires_review": true,
                    "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct equivalent in Power BI/Fabric. The closest approximation would be a textbox or custom visual, but native support is unavailable. Marked as unsupported with an unmapped status and a recommendation to implement a custom Power Apps visual or use a parameter input via Power BI's query parameters. Re-create using a single-value slicer bound to a parameter table."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "AWSzx",
                    "visual_name": "AWSzx",
                    "object_category": "other",
                    "chart_type": "action-button",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 0,
                    "row": 9,
                    "colspan": 12,
                    "rowspan": 1,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Fleet Opeations",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "actionButton",
                    "bi_type": "actionButton",
                    "supported": true,
                    "status": "mapped",
                    "title": "Go to Fleet Opeations",
                    "name": "Go to Fleet Opeations",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 9,
                        "colspan": 12,
                        "rowspan": 1,
                        "x": 0,
                        "y": 154,
                        "width": 640,
                        "height": 20
                    },
                    "power_bi_visual_type": {
                        "visualType": "actionButton",
                        "title": {
                            "text": "Go to Fleet Opeations",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 154,
                            "width": 640,
                            "height": 20
                        }
                    },
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Fleet Opeations",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
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
                            "font_family": "Source Sans Pro, sans-serif",
                            "show": true
                        },
                        "background": {
                            "color": "#e1dad5"
                        },
                        "components": [
                            {
                                "key": "general",
                                "title": {
                                    "main": {
                                        "fontFamily": "Source Sans Pro, sans-serif"
                                    }
                                },
                                "bgColor": {
                                    "color": {
                                        "index": 12,
                                        "color": "#e1dad5",
                                        "alpha": 1
                                    }
                                },
                                "borderColor": {
                                    "index": 15,
                                    "color": "#000000",
                                    "alpha": 1
                                }
                            }
                        ],
                        "legend": {
                            "show": false
                        },
                        "backgroundColor": "#e1dad5"
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
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "JjhAvt",
                    "visual_name": "JjhAvt",
                    "object_category": "other",
                    "chart_type": "action-button",
                    "sheet_name": "Executive Overview",
                    "layout": {},
                    "col": 12,
                    "row": 9,
                    "colspan": 12,
                    "rowspan": 1,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Customer & Revenue Analytics",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e1dad5",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "actionButton",
                    "bi_type": "actionButton",
                    "supported": true,
                    "status": "mapped",
                    "title": "Go to Customer & Revenue Analytics",
                    "name": "Go to Customer & Revenue Analytics",
                    "object_category": "standard",
                    "sheet_name": "Executive Overview",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 9,
                        "colspan": 12,
                        "rowspan": 1,
                        "x": 640,
                        "y": 154,
                        "width": 640,
                        "height": 20
                    },
                    "power_bi_visual_type": {
                        "visualType": "actionButton",
                        "title": {
                            "text": "Go to Customer & Revenue Analytics",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 154,
                            "width": 640,
                            "height": 20
                        }
                    },
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Customer & Revenue Analytics",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e1dad5",
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
                        "background": {
                            "color": "#e1dad5"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 12,
                                        "color": "#e1dad5",
                                        "alpha": 1
                                    }
                                },
                                "borderColor": {
                                    "index": 15,
                                    "color": "#000000",
                                    "alpha": 1
                                }
                            }
                        ],
                        "legend": {
                            "show": false
                        },
                        "backgroundColor": "#e1dad5"
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
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "rmuRw",
                    "visual_name": "rmuRw",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 4,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Fuel Efficiency"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Fuel Efficiency",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Average Fuel Efficiency",
                    "name": "Average Fuel Efficiency",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 4,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 213,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Fuel Efficiency",
                            "visible": true
                        },
                        "general": {
                            "x": 213,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Fuel Efficiency"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Fuel Efficiency",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "eypGTT",
                    "visual_name": "eypGTT",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 16,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Trip Duration"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Trip Duration",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Average Trip Duration",
                    "name": "Average Trip Duration",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 16,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 853,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Trip Duration",
                            "visible": true
                        },
                        "general": {
                            "x": 853,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Trip Duration"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Trip Duration",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "eEhJRgX",
                    "visual_name": "eEhJRgX",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 8,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Trip Distance"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Trip Distance",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Average Trip Distance",
                    "name": "Average Trip Distance",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 8,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 427,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Trip Distance",
                            "visible": true
                        },
                        "general": {
                            "x": 427,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Trip Distance"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Trip Distance",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "cPjKK",
                    "visual_name": "cPjKK",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 6,
                    "row": 4,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Active Trucks"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Active Trucks",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Active Trucks",
                    "name": "Active Trucks",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 6,
                        "row": 4,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 320,
                        "y": 69,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Active Trucks",
                            "visible": true
                        },
                        "general": {
                            "x": 320,
                            "y": 69,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Active Trucks"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Active Trucks",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "xFpPDH",
                    "visual_name": "xFpPDH",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 20,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Revenue per Mile"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Revenue per Mile",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Revenue per Mile",
                    "name": "Revenue per Mile",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 20,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 1067,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Revenue per Mile",
                            "visible": true
                        },
                        "general": {
                            "x": 1067,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Revenue per Mile"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Revenue per Mile",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "HYxBPK",
                    "visual_name": "HYxBPK",
                    "object_category": "other",
                    "chart_type": "treemap",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 0,
                    "row": 3,
                    "colspan": 17,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Trips"
                    ],
                    "x_axis": [
                        "DistanceBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Distance Band Distribution",
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
                    "title": "Distance Band Distribution",
                    "name": "Distance Band Distribution",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 3,
                        "colspan": 17,
                        "rowspan": 4,
                        "x": 0,
                        "y": 51,
                        "width": 907,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "treemap",
                        "title": {
                            "text": "Distance Band Distribution",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 51,
                            "width": 907,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                    "y_axis_fields": [
                        "Total Trips"
                    ],
                    "x_axis_fields": [
                        "DistanceBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Distance Band Distribution",
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
                    "title": "mpcAKWU",
                    "visual_name": "mpcAKWU",
                    "object_category": "other",
                    "chart_type": "boxplot",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 17,
                    "row": 3,
                    "colspan": 7,
                    "rowspan": 4,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Avg(idle_time_hours)"
                    ],
                    "x_axis": [
                        "IdleTimeBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Idle Time Analysis",
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
                    "title": "Idle Time Analysis",
                    "name": "Idle Time Analysis",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 17,
                        "row": 3,
                        "colspan": 7,
                        "rowspan": 4,
                        "x": 907,
                        "y": 51,
                        "width": 373,
                        "height": 69
                    },
                    "power_bi_visual_type": {
                        "visualType": "boxPlot",
                        "title": {
                            "text": "Idle Time Analysis",
                            "visible": true
                        },
                        "general": {
                            "x": 907,
                            "y": 51,
                            "width": 373,
                            "height": 69
                        }
                    },
                    "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual.",
                    "y_axis_fields": [
                        "Avg(idle_time_hours)"
                    ],
                    "x_axis_fields": [
                        "IdleTimeBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Idle Time Analysis",
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
                    "title": "PJWEW",
                    "visual_name": "PJWEW",
                    "object_category": "other",
                    "chart_type": "scatterplot",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 0,
                    "row": 7,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Avg(actual_distance_miles)",
                        "Avg(average_mpg)",
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "unit_number"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Truck Performance",
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
                    "title": "Truck Performance",
                    "name": "Truck Performance",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 7,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 120,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "scatterChart",
                        "title": {
                            "text": "Truck Performance",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 120,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual.",
                    "y_axis_fields": [
                        "Avg(actual_distance_miles)",
                        "Avg(average_mpg)",
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "unit_number"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Truck Performance",
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
                            },
                            {
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "$#,##0.0M",
                                "qDec": ".",
                                "qThou": ","
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
                    "title": "jbgKqE",
                    "visual_name": "jbgKqE",
                    "object_category": "chart",
                    "chart_type": "funnel",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 12,
                    "row": 7,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Loads"
                    ],
                    "x_axis": [
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "High Value Loads",
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
                    "visual_type": "funnel",
                    "bi_type": "funnel",
                    "supported": true,
                    "status": "mapped",
                    "title": "High Value Loads",
                    "name": "High Value Loads",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 7,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 120,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "funnel",
                        "title": {
                            "text": "High Value Loads",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 120,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'funnel' visual maps directly to Fabric 'funnel' visual.",
                    "y_axis_fields": [
                        "Total Loads"
                    ],
                    "x_axis_fields": [
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "High Value Loads",
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
                    "rationale": "The Qlik Sense 'funnel' visual maps directly to Fabric 'funnel' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "KKFj",
                    "visual_name": "KKFj",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 12,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Fleet Operations"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Fleet Operations",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                    "title": "Fleet Operations",
                    "name": "Fleet Operations",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 3,
                        "x": 640,
                        "y": 0,
                        "width": 213,
                        "height": 51
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Fleet Operations",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 0,
                            "width": 213,
                            "height": 51
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Fleet Operations"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Fleet Operations",
                        "title_font_size": "M",
                        "title_font_family": "Segoe UI, sans-serif",
                        "background_color": "#e0bd8d",
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
                        "background": {
                            "color": "#e0bd8d"
                        },
                        "components": [
                            {
                                "key": "general",
                                "bgColor": {
                                    "color": {
                                        "index": 11,
                                        "color": "#e0bd8d",
                                        "alpha": 1
                                    }
                                }
                            }
                        ],
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
                        "backgroundColor": "#e0bd8d",
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
                    "title": "ffTSNj",
                    "visual_name": "ffTSNj",
                    "object_category": "other",
                    "chart_type": "action-button",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 0,
                    "row": 12,
                    "colspan": 12,
                    "rowspan": 1,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Executive overview",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "actionButton",
                    "bi_type": "actionButton",
                    "supported": true,
                    "status": "mapped",
                    "title": "Go to Executive overview",
                    "name": "Go to Executive overview",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 12,
                        "colspan": 12,
                        "rowspan": 1,
                        "x": 0,
                        "y": 206,
                        "width": 640,
                        "height": 20
                    },
                    "power_bi_visual_type": {
                        "visualType": "actionButton",
                        "title": {
                            "text": "Go to Executive overview",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 206,
                            "width": 640,
                            "height": 20
                        }
                    },
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Executive overview",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
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
                            "font_family": "Source Sans Pro, sans-serif",
                            "show": true
                        },
                        "background": {
                            "color": "#e1dad5"
                        },
                        "components": [
                            {
                                "key": "general",
                                "title": {
                                    "main": {
                                        "fontFamily": "Source Sans Pro, sans-serif"
                                    }
                                },
                                "bgColor": {
                                    "color": {
                                        "index": 12,
                                        "color": "#e1dad5",
                                        "alpha": 1
                                    }
                                },
                                "borderColor": {
                                    "index": 15,
                                    "color": "#000000",
                                    "alpha": 1
                                }
                            }
                        ],
                        "legend": {
                            "show": false
                        },
                        "backgroundColor": "#e1dad5"
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
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "EVktj",
                    "visual_name": "EVktj",
                    "object_category": "other",
                    "chart_type": "action-button",
                    "sheet_name": "Fleet Operations",
                    "layout": {},
                    "col": 12,
                    "row": 12,
                    "colspan": 12,
                    "rowspan": 1,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Customer & Revenue Analytics",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
                        "border": {
                            "show": false
                        },
                        "legend": {
                            "show": false
                        }
                    }
                },
                "fabric": {
                    "visual_type": "actionButton",
                    "bi_type": "actionButton",
                    "supported": true,
                    "status": "mapped",
                    "title": "Go to Customer & Revenue Analytics",
                    "name": "Go to Customer & Revenue Analytics",
                    "object_category": "standard",
                    "sheet_name": "Fleet Operations",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 12,
                        "colspan": 12,
                        "rowspan": 1,
                        "x": 640,
                        "y": 206,
                        "width": 640,
                        "height": 20
                    },
                    "power_bi_visual_type": {
                        "visualType": "actionButton",
                        "title": {
                            "text": "Go to Customer & Revenue Analytics",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 206,
                            "width": 640,
                            "height": 20
                        }
                    },
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Go to Customer & Revenue Analytics",
                        "title_font_family": "Source Sans Pro, sans-serif",
                        "background_color": "#e1dad5",
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
                            "font_family": "Source Sans Pro, sans-serif",
                            "show": true
                        },
                        "background": {
                            "color": "#e1dad5"
                        },
                        "components": [
                            {
                                "key": "general",
                                "title": {
                                    "main": {
                                        "fontFamily": "Source Sans Pro, sans-serif"
                                    }
                                },
                                "bgColor": {
                                    "color": {
                                        "index": 12,
                                        "color": "#e1dad5",
                                        "alpha": 1
                                    }
                                },
                                "borderColor": {
                                    "index": 15,
                                    "color": "#000000",
                                    "alpha": 1
                                }
                            }
                        ],
                        "legend": {
                            "show": false
                        },
                        "backgroundColor": "#e1dad5"
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
                    "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "NgkPzp",
                    "visual_name": "NgkPzp",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 0,
                    "row": 0,
                    "colspan": 5,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Highest Revenue by Customer"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Highest Revenue by Customer",
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
                    "title": "Highest Revenue by Customer",
                    "name": "Highest Revenue by Customer",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 0,
                        "colspan": 5,
                        "rowspan": 2,
                        "x": 0,
                        "y": 0,
                        "width": 267,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Highest Revenue by Customer",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 0,
                            "width": 267,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Highest Revenue by Customer"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Highest Revenue by Customer",
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
                    "title": "bWNPnp",
                    "visual_name": "bWNPnp",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 19,
                    "row": 0,
                    "colspan": 5,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "High Value Revenue %"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "High Value Revenue %",
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
                    "title": "High Value Revenue %",
                    "name": "High Value Revenue %",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 19,
                        "row": 0,
                        "colspan": 5,
                        "rowspan": 2,
                        "x": 1013,
                        "y": 0,
                        "width": 267,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "High Value Revenue %",
                            "visible": true
                        },
                        "general": {
                            "x": 1013,
                            "y": 0,
                            "width": 267,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "High Value Revenue %"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "High Value Revenue %",
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
                    "title": "zxPNm",
                    "visual_name": "zxPNm",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 10,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "High Value Loads"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "High Value Loads",
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
                    "title": "High Value Loads",
                    "name": "High Value Loads",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 10,
                        "row": 0,
                        "colspan": 4,
                        "rowspan": 2,
                        "x": 533,
                        "y": 0,
                        "width": 213,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "High Value Loads",
                            "visible": true
                        },
                        "general": {
                            "x": 533,
                            "y": 0,
                            "width": 213,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "High Value Loads"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "High Value Loads",
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
                    "title": "TYnajA",
                    "visual_name": "TYnajA",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 14,
                    "row": 0,
                    "colspan": 5,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Average Revenue per Customer"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Revenue per Customer",
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
                    "title": "Average Revenue per Customer",
                    "name": "Average Revenue per Customer",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 14,
                        "row": 0,
                        "colspan": 5,
                        "rowspan": 2,
                        "x": 747,
                        "y": 0,
                        "width": 267,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Average Revenue per Customer",
                            "visible": true
                        },
                        "general": {
                            "x": 747,
                            "y": 0,
                            "width": 267,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Average Revenue per Customer"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Average Revenue per Customer",
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
                    "title": "mubYNVd",
                    "visual_name": "mubYNVd",
                    "object_category": "other",
                    "chart_type": "kpi",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 5,
                    "row": 0,
                    "colspan": 5,
                    "rowspan": 2,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Completed Trip Revenue"
                    ],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Completed Trip Revenue",
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
                    "title": "Completed Trip Revenue",
                    "name": "Completed Trip Revenue",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 5,
                        "row": 0,
                        "colspan": 5,
                        "rowspan": 2,
                        "x": 267,
                        "y": 0,
                        "width": 267,
                        "height": 34
                    },
                    "power_bi_visual_type": {
                        "visualType": "card",
                        "title": {
                            "text": "Completed Trip Revenue",
                            "visible": true
                        },
                        "general": {
                            "x": 267,
                            "y": 0,
                            "width": 267,
                            "height": 34
                        }
                    },
                    "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                    "y_axis_fields": [
                        "Completed Trip Revenue"
                    ],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": false,
                        "title": "Completed Trip Revenue",
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
                    "title": "cTfPhEj",
                    "visual_name": "cTfPhEj",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 0,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Customer",
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
                    "title": "Customer",
                    "name": "Customer",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
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
                            "text": "Customer",
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
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Customer",
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
                    "title": "JxjPRPg",
                    "visual_name": "JxjPRPg",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 18,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Route",
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
                    "title": "Route",
                    "name": "Route",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
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
                            "text": "Route",
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
                        "Route"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "Route",
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
                    "title": "rprpnyy",
                    "visual_name": "rprpnyy",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 12,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "RevenueBand",
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
                    "title": "RevenueBand",
                    "name": "RevenueBand",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
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
                            "text": "RevenueBand",
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
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": false,
                        "title": "RevenueBand",
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
                    "title": "DsKZpQW",
                    "visual_name": "DsKZpQW",
                    "object_category": "other",
                    "chart_type": "filterpane",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 6,
                    "row": 2,
                    "colspan": 6,
                    "rowspan": 3,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [
                        "MonthYear"
                    ],
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
                    }
                },
                "fabric": {
                    "visual_type": "slicer",
                    "bi_type": "slicer",
                    "supported": true,
                    "status": "mapped",
                    "title": "MonthYear",
                    "name": "MonthYear",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
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
                            "text": "MonthYear",
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
                        "MonthYear"
                    ],
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
                    "title": "cPBNNjB",
                    "visual_name": "cPBNNjB",
                    "object_category": "other",
                    "chart_type": "treemap",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 0,
                    "row": 5,
                    "colspan": 9,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue Contribution by Customer",
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
                    "title": "Revenue Contribution by Customer",
                    "name": "Revenue Contribution by Customer",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 5,
                        "colspan": 9,
                        "rowspan": 5,
                        "x": 0,
                        "y": 86,
                        "width": 480,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "treemap",
                        "title": {
                            "text": "Revenue Contribution by Customer",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 86,
                            "width": 480,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "Customer"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue Contribution by Customer",
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
                                "qType": "R",
                                "qnDec": 2,
                                "qUseThou": 0,
                                "qFmt": "$#,##0.0M",
                                "qDec": ".",
                                "qThou": ","
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
                    "title": "tGaxu",
                    "visual_name": "tGaxu",
                    "object_category": "chart",
                    "chart_type": "linechart",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 0,
                    "row": 10,
                    "colspan": 24,
                    "rowspan": 6,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "MonthYear"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Monthly Customer Revenue Trend",
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
                    "title": "Monthly Customer Revenue Trend",
                    "name": "Monthly Customer Revenue Trend",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 10,
                        "colspan": 24,
                        "rowspan": 6,
                        "x": 0,
                        "y": 171,
                        "width": 1280,
                        "height": 103
                    },
                    "power_bi_visual_type": {
                        "visualType": "lineChart",
                        "title": {
                            "text": "Monthly Customer Revenue Trend",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 171,
                            "width": 1280,
                            "height": 103
                        }
                    },
                    "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "MonthYear"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Monthly Customer Revenue Trend",
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
                            "persistent": true,
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
                                "continuousAuto": false,
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
                                "qFmt": "$#,##0.0M",
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
                    "title": "jQXpenC",
                    "visual_name": "jQXpenC",
                    "object_category": "other",
                    "chart_type": "piechart",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 17,
                    "row": 5,
                    "colspan": 7,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Loads"
                    ],
                    "x_axis": [
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Load Distribution by Revenue Band",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
                        },
                        "legend": {
                            "show": true,
                            "dock": "auto"
                        }
                    }
                },
                "fabric": {
                    "visual_type": "donutChart",
                    "bi_type": "donutChart",
                    "supported": true,
                    "status": "mapped",
                    "title": "Load Distribution by Revenue Band",
                    "name": "Load Distribution by Revenue Band",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 17,
                        "row": 5,
                        "colspan": 7,
                        "rowspan": 5,
                        "x": 907,
                        "y": 86,
                        "width": 373,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "donutChart",
                        "title": {
                            "text": "Load Distribution by Revenue Band",
                            "visible": true
                        },
                        "general": {
                            "x": 907,
                            "y": 86,
                            "width": 373,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                    "y_axis_fields": [
                        "Total Loads"
                    ],
                    "x_axis_fields": [
                        "RevenueBand"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Load Distribution by Revenue Band",
                        "title_font_family": "Segoe UI, sans-serif",
                        "border": {
                            "show": false
                        },
                        "inner_radius": 0.55,
                        "stroke_color": {
                            "index": -1,
                            "color": "#FFFFFF"
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
                        "innerRadius": 0.55,
                        "strokeColor": "#FFFFFF",
                        "components": [
                            {
                                "key": "slices",
                                "style": {
                                    "strokeWidth": "none",
                                    "strokeColor": {
                                        "index": -1,
                                        "color": "#FFFFFF"
                                    },
                                    "cornerRadius": 0,
                                    "innerRadius": 0.55
                                }
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
                    "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "hPBvpkk",
                    "visual_name": "hPBvpkk",
                    "object_category": "chart",
                    "chart_type": "barchart",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 9,
                    "row": 5,
                    "colspan": 8,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [
                        "Total Revenue"
                    ],
                    "x_axis": [
                        "Booking Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue by Booking Type",
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
                    "title": "Revenue by Booking Type",
                    "name": "Revenue by Booking Type",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 9,
                        "row": 5,
                        "colspan": 8,
                        "rowspan": 5,
                        "x": 480,
                        "y": 86,
                        "width": 427,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "barChart",
                        "title": {
                            "text": "Revenue by Booking Type",
                            "visible": true
                        },
                        "general": {
                            "x": 480,
                            "y": 86,
                            "width": 427,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                    "y_axis_fields": [
                        "Total Revenue"
                    ],
                    "x_axis_fields": [
                        "Booking Type"
                    ],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue by Booking Type",
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
                        "auto": false,
                        "mode": "primary",
                        "single_color": "#ac4d58",
                        "raw_single_color": "#ac4d58",
                        "dimension_scheme": "12",
                        "measure_scheme": "sg",
                        "palette_index": 10,
                        "palette_scheme": "12",
                        "is_multicolor": true,
                        "use_base_colors": "on"
                    },
                    "style_and_formatting": {
                        "title": {
                            "show": true
                        },
                        "colorScheme": {
                            "auto": false,
                            "mode": "primary",
                            "formatting": {
                                "numFormatFromTemplate": true,
                                "quarantine": {
                                    "isCustomFormatted": false
                                }
                            },
                            "useBaseColors": "off",
                            "paletteColor": {
                                "index": 10,
                                "color": "#ac4d58",
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
                            "altLabel": "AjfgE",
                            "byMeasureDef": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
                            },
                            "byDimDef": {
                                "label": "mZVtGZ",
                                "key": "mZVtGZ",
                                "type": "libraryItem"
                            }
                        },
                        "data_colors": {
                            "primary": "#ac4d58",
                            "mode": "primary",
                            "auto": false,
                            "by_measure": {
                                "label": "AjfgE",
                                "key": "AjfgE",
                                "type": "libraryItem"
                            },
                            "by_dimension": {
                                "label": "mZVtGZ",
                                "key": "mZVtGZ",
                                "type": "libraryItem"
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
                                "qFmt": "$#,##0.0M",
                                "qDec": ".",
                                "qThou": ","
                            }
                        ],
                        "orientation": "horizontal",
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
                    "title": "UtkCby",
                    "visual_name": "UtkCby",
                    "object_category": "other",
                    "chart_type": "sn-image",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 0,
                    "row": 16,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Customer Analytics",
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
                    "visual_type": "image",
                    "bi_type": "image",
                    "supported": true,
                    "status": "mapped",
                    "title": "Customer Analytics",
                    "name": "Customer Analytics",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 0,
                        "row": 16,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 0,
                        "y": 274,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "image",
                        "title": {
                            "text": "Customer Analytics",
                            "visible": true
                        },
                        "general": {
                            "x": 0,
                            "y": 274,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Customer Analytics",
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
                    "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual."
                }
            },
            {
                "name": "DashboardObject",
                "qlik_source": {
                    "title": "BJpSGS",
                    "visual_name": "BJpSGS",
                    "object_category": "other",
                    "chart_type": "sn-image",
                    "sheet_name": "Customer & Revenue Analytics",
                    "layout": {},
                    "col": 12,
                    "row": 16,
                    "colspan": 12,
                    "rowspan": 5,
                    "header_styling": {},
                    "card_styling": {},
                    "y_axis": [],
                    "x_axis": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue Analytics",
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
                    "visual_type": "image",
                    "bi_type": "image",
                    "supported": true,
                    "status": "mapped",
                    "title": "Revenue Analytics",
                    "name": "Revenue Analytics",
                    "object_category": "standard",
                    "sheet_name": "Customer & Revenue Analytics",
                    "replacement_strategy": null,
                    "layout": {
                        "col": 12,
                        "row": 16,
                        "colspan": 12,
                        "rowspan": 5,
                        "x": 640,
                        "y": 274,
                        "width": 640,
                        "height": 86
                    },
                    "power_bi_visual_type": {
                        "visualType": "image",
                        "title": {
                            "text": "Revenue Analytics",
                            "visible": true
                        },
                        "general": {
                            "x": 640,
                            "y": 274,
                            "width": 640,
                            "height": 86
                        }
                    },
                    "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual.",
                    "y_axis_fields": [],
                    "x_axis_fields": [],
                    "formatting": {
                        "show_titles": true,
                        "title": "Revenue Analytics",
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
                    "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual."
                }
            }
        ],
        "sheets": [
            {
                "sheet_id": "CqUTPj",
                "title": "Executive Overview",
                "visualization_count": 22,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "RcsrXpD",
                            "visual_name": "RcsrXpD",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Revenue",
                                "title_font_size": "20px",
                                "title_font_family": "Abril Fatface, serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                            "title": "Total Revenue",
                            "name": "Total Revenue",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 0,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Revenue",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Revenue",
                                "title_font_size": "20px",
                                "title_font_family": "Abril Fatface, serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                                    "font_size": "20px",
                                    "font_family": "Abril Fatface, serif",
                                    "show": false
                                },
                                "subtitle": {
                                    "color": "#8b8b8b"
                                },
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "title": {
                                            "subTitle": {
                                                "color": {
                                                    "index": -1,
                                                    "color": "#8b8b8b",
                                                    "alpha": 1
                                                }
                                            },
                                            "main": {
                                                "fontSize": "20px",
                                                "fontFamily": "Abril Fatface, serif"
                                            }
                                        },
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 0.63
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
                                    },
                                    {
                                        "key": "useAdvancedMode",
                                        "useAdvancedMode": true
                                    },
                                    {
                                        "key": "simpleSettings",
                                        "simpleFontSize": 0.6
                                    },
                                    {
                                        "key": "firstMeasureTitle",
                                        "label": {
                                            "name": {
                                                "fontSize": {
                                                    "fluid": 0.6
                                                },
                                                "fontStyle": [
                                                    "bold"
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                        "qFmt": "$#,##0.0M",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "text_align": "center",
                                "backgroundColor": "#99cfcd",
                                "fontSize": "20px"
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
                            "title": "pReKpR",
                            "visual_name": "pReKpR",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 8,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Trips"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Trips",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                            "title": "Total Trips",
                            "name": "Total Trips",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 8,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 427,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Trips",
                                    "visible": true
                                },
                                "general": {
                                    "x": 427,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Trips"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Trips",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 1
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
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
                                                    "fluid": 0.6
                                                },
                                                "fontStyle": [
                                                    "bold"
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                "backgroundColor": "#99cfcd",
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
                            "title": "sWRr",
                            "visual_name": "sWRr",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Customers"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Customers",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                            "title": "Total Customers",
                            "name": "Total Customers",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 640,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Customers",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Customers"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Customers",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 1
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
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
                                                    "fluid": 0.6
                                                },
                                                "fontStyle": [
                                                    "bold"
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                "backgroundColor": "#99cfcd",
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
                            "title": "cRfsjp",
                            "visual_name": "cRfsjp",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 16,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Drivers"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Drivers",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                            "title": "Total Drivers",
                            "name": "Total Drivers",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 16,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 853,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Total Drivers",
                                    "visible": true
                                },
                                "general": {
                                    "x": 853,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Total Drivers"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Total Drivers",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 1
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
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
                                                    "fluid": 0.6
                                                },
                                                "fontStyle": [
                                                    "bold"
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                "backgroundColor": "#99cfcd",
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
                            "title": "FEPPP",
                            "visual_name": "FEPPP",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 20,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Fleet Size"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Fleet Size",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "20px",
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
                            "title": "Fleet Size",
                            "name": "Fleet Size",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 20,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 1067,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Fleet Size",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1067,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Fleet Size"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Fleet Size",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "20px",
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
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "20px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "20px",
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 1
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
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
                                                "fontStyle": [
                                                    "bold"
                                                ],
                                                "fontSize": {
                                                    "fluid": 0.6
                                                }
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                "backgroundColor": "#99cfcd",
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
                            "title": "xbTxPjC",
                            "visual_name": "xbTxPjC",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 12,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                            ],
                            "x_axis": [
                                "Load Month"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                            "name": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 12,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 0,
                                "y": 206,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 206,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "='Total ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' )"
                            ],
                            "x_axis_fields": [
                                "Load Month"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "auto": false,
                                "mode": "primary",
                                "single_color": "#002833",
                                "raw_single_color": "#002833",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": -1,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "on"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    },
                                    {
                                        "key": "line",
                                        "style": {
                                            "lineThickness": 2
                                        }
                                    },
                                    {
                                        "key": "axis"
                                    },
                                    {
                                        "key": "label"
                                    },
                                    {
                                        "key": "legend"
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
                                        "color": "#002833",
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
                                "data_colors": {
                                    "primary": "#002833",
                                    "mode": "primary",
                                    "auto": false
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
                                        "qFmt": "$#,##0.0M",
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
                            "title": "hqpgX",
                            "visual_name": "hqpgX",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 12,
                            "colspan": 12,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top 10 Customers by Revenue",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "16px",
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
                            "title": "Top 10 Customers by Revenue",
                            "name": "Top 10 Customers by Revenue",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 12,
                                "colspan": 12,
                                "rowspan": 6,
                                "x": 640,
                                "y": 206,
                                "width": 640,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Top 10 Customers by Revenue",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 206,
                                    "width": 640,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top 10 Customers by Revenue",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "16px",
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
                                "auto": false,
                                "mode": "primary",
                                "single_color": "#b83e51",
                                "raw_single_color": "#b83e51",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": -1,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "on"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "borderRadius": "16px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "16px"
                                    }
                                ],
                                "colorScheme": {
                                    "auto": false,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true,
                                        "quarantine": {
                                            "isCustomFormatted": false
                                        }
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": -1,
                                        "color": "#b83e51",
                                        "alpha": 1
                                    },
                                    "useDimColVal": true,
                                    "useMeasureGradient": false,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "12",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10,
                                    "altLabel": "AjfgE",
                                    "byMeasureDef": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
                                    },
                                    "byDimDef": {
                                        "label": "SJWVwe",
                                        "key": "SJWVwe",
                                        "type": "libraryItem"
                                    }
                                },
                                "data_colors": {
                                    "primary": "#b83e51",
                                    "mode": "primary",
                                    "auto": false,
                                    "by_measure": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
                                    },
                                    "by_dimension": {
                                        "label": "SJWVwe",
                                        "key": "SJWVwe",
                                        "type": "libraryItem"
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
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "$#,##0.0M",
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
                            "title": "JQqMHER",
                            "visual_name": "JQqMHER",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 8,
                            "row": 18,
                            "colspan": 8,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top 10 Routes by Revenue",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Top 10 Routes by Revenue",
                            "name": "Top 10 Routes by Revenue",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 8,
                                "row": 18,
                                "colspan": 8,
                                "rowspan": 6,
                                "x": 427,
                                "y": 309,
                                "width": 427,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Top 10 Routes by Revenue",
                                    "visible": true
                                },
                                "general": {
                                    "x": 427,
                                    "y": 309,
                                    "width": 427,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top 10 Routes by Revenue",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "auto": false,
                                "mode": "byMeasure",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
                                "colorScheme": {
                                    "auto": false,
                                    "mode": "byMeasure",
                                    "formatting": {
                                        "numFormatFromTemplate": true,
                                        "quarantine": {
                                            "isCustomFormatted": false
                                        }
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
                                    "measureMax": 10,
                                    "altLabel": "AjfgE",
                                    "byMeasureDef": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
                                    }
                                },
                                "data_colors": {
                                    "mode": "byMeasure",
                                    "auto": false,
                                    "by_measure": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
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
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "$#,##0.0M",
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
                            "title": "RJhBz",
                            "visual_name": "RJhBz",
                            "object_category": "other",
                            "chart_type": "piechart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 16,
                            "row": 18,
                            "colspan": 8,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Loads"
                            ],
                            "x_axis": [
                                "Load Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Loads by Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "donutChart",
                            "bi_type": "donutChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Loads by Type",
                            "name": "Loads by Type",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 16,
                                "row": 18,
                                "colspan": 8,
                                "rowspan": 6,
                                "x": 853,
                                "y": 309,
                                "width": 427,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "donutChart",
                                "title": {
                                    "text": "Loads by Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 853,
                                    "y": 309,
                                    "width": 427,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                            "y_axis_fields": [
                                "Total Loads"
                            ],
                            "x_axis_fields": [
                                "Load Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Loads by Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
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
                                "auto": false,
                                "mode": "byDimension",
                                "dimension_scheme": "100",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "100",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "borderRadius": "15px",
                                "innerRadius": 0.55,
                                "strokeColor": "#FFFFFF",
                                "components": [
                                    {
                                        "key": "slices",
                                        "style": {
                                            "strokeWidth": "none",
                                            "strokeColor": {
                                                "index": -1,
                                                "color": "#FFFFFF"
                                            },
                                            "cornerRadius": 0,
                                            "innerRadius": 0.55
                                        }
                                    },
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
                                "colorScheme": {
                                    "auto": false,
                                    "mode": "byDimension",
                                    "formatting": {
                                        "numFormatFromTemplate": true,
                                        "quarantine": {
                                            "isCustomFormatted": false
                                        }
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": false,
                                    "useMeasureGradient": false,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "100",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10,
                                    "altLabel": "gXFAXcp",
                                    "byDimDef": {
                                        "label": "gXFAXcp",
                                        "key": "gXFAXcp",
                                        "type": "libraryItem"
                                    },
                                    "byMeasureDef": {
                                        "label": "pSzSnUp",
                                        "key": "pSzSnUp",
                                        "type": "libraryItem"
                                    }
                                },
                                "data_colors": {
                                    "mode": "byDimension",
                                    "auto": false,
                                    "by_measure": {
                                        "label": "pSzSnUp",
                                        "key": "pSzSnUp",
                                        "type": "libraryItem"
                                    },
                                    "by_dimension": {
                                        "label": "gXFAXcp",
                                        "key": "gXFAXcp",
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
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "DmejKEM",
                            "visual_name": "DmejKEM",
                            "object_category": "other",
                            "chart_type": "sn-table",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 24,
                            "colspan": 24,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue",
                                "Total Loads",
                                "Average Revenue per Load",
                                "Revenue %"
                            ],
                            "x_axis": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top Customers",
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
                            "title": "Top Customers",
                            "name": "Top Customers",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
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
                                "visualType": "tableEx",
                                "title": {
                                    "text": "Top Customers",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 411,
                                    "width": 1280,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'sn-table' visual maps directly to Fabric 'tableEx' visual.",
                            "y_axis_fields": [
                                "Total Revenue",
                                "Total Loads",
                                "Average Revenue per Load",
                                "Revenue %"
                            ],
                            "x_axis_fields": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top Customers",
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
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "$#,##0.0M",
                                        "qDec": ".",
                                        "qThou": ","
                                    },
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
                                        "qType": "U",
                                        "qnDec": 10,
                                        "qUseThou": 0
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
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "mpV",
                            "visual_name": "mpV",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Customer",
                                "title_color": "#c25dab",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Customer",
                            "name": "Customer",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 0,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Customer",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Customer",
                                "title_color": "#c25dab",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                    "color": "#c25dab",
                                    "show": false
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "title": {
                                            "main": {
                                                "color": {
                                                    "index": -1,
                                                    "color": "#c25dab",
                                                    "alpha": 1
                                                }
                                            }
                                        }
                                    }
                                ],
                                "legend": {
                                    "show": false
                                },
                                "titleColor": "#c25dab"
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
                            "title": "JxhYr",
                            "visual_name": "JxhYr",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Route",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Route",
                            "name": "Route",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 640,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Route",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Route",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
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
                            "title": "JVqkaP",
                            "visual_name": "JVqkaP",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 20,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Load Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Load Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Load Type",
                            "name": "Load Type",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 20,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 1067,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Load Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1067,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Load Type"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Load Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
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
                            "title": "FanfT",
                            "visual_name": "FanfT",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 4,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Driver"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Driver",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Driver",
                            "name": "Driver",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 4,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 213,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Driver",
                                    "visible": true
                                },
                                "general": {
                                    "x": 213,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Driver"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Driver",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
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
                            "title": "yuQxa",
                            "visual_name": "yuQxa",
                            "object_category": "other",
                            "chart_type": "piechart",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 18,
                            "colspan": 8,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Loads"
                            ],
                            "x_axis": [
                                "Booking Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Loads by Booking Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "donutChart",
                            "bi_type": "donutChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Loads by Booking Type",
                            "name": "Loads by Booking Type",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 18,
                                "colspan": 8,
                                "rowspan": 6,
                                "x": 0,
                                "y": 309,
                                "width": 427,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "donutChart",
                                "title": {
                                    "text": "Loads by Booking Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 309,
                                    "width": 427,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                            "y_axis_fields": [
                                "Total Loads"
                            ],
                            "x_axis_fields": [
                                "Booking Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Loads by Booking Type",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
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
                                "auto": false,
                                "mode": "byDimension",
                                "dimension_scheme": "100",
                                "measure_scheme": "sg",
                                "palette_index": 6,
                                "palette_scheme": "100",
                                "is_multicolor": true,
                                "use_base_colors": "off"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "borderRadius": "15px",
                                "innerRadius": 0.55,
                                "strokeColor": "#FFFFFF",
                                "components": [
                                    {
                                        "key": "slices",
                                        "style": {
                                            "strokeWidth": "none",
                                            "strokeColor": {
                                                "index": -1,
                                                "color": "#FFFFFF"
                                            },
                                            "cornerRadius": 0,
                                            "innerRadius": 0.55
                                        }
                                    },
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
                                "colorScheme": {
                                    "auto": false,
                                    "mode": "byDimension",
                                    "formatting": {
                                        "numFormatFromTemplate": true,
                                        "quarantine": {
                                            "isCustomFormatted": false
                                        }
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 6
                                    },
                                    "useDimColVal": false,
                                    "useMeasureGradient": true,
                                    "persistent": false,
                                    "expressionIsColor": true,
                                    "measureScheme": "sg",
                                    "reverseScheme": false,
                                    "dimensionScheme": "100",
                                    "autoMinMax": true,
                                    "measureMin": 0,
                                    "measureMax": 10,
                                    "altLabel": "mZVtGZ",
                                    "byMeasureDef": {
                                        "label": "pSzSnUp",
                                        "key": "pSzSnUp",
                                        "type": "libraryItem"
                                    },
                                    "byDimDef": {
                                        "label": "mZVtGZ",
                                        "key": "mZVtGZ",
                                        "type": "libraryItem"
                                    }
                                },
                                "data_colors": {
                                    "mode": "byDimension",
                                    "auto": false,
                                    "by_measure": {
                                        "label": "pSzSnUp",
                                        "key": "pSzSnUp",
                                        "type": "libraryItem"
                                    },
                                    "by_dimension": {
                                        "label": "mZVtGZ",
                                        "key": "mZVtGZ",
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
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "kqbVa",
                            "visual_name": "kqbVa",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 16,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Load Month"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Load Month",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Load Month",
                            "name": "Load Month",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 16,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 853,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Load Month",
                                    "visible": true
                                },
                                "general": {
                                    "x": 853,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Load Month"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Load Month",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
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
                            "title": "pkmKCqm",
                            "visual_name": "pkmKCqm",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 8,
                            "row": 3,
                            "colspan": 4,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Truck"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Truck",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                            "title": "Truck",
                            "name": "Truck",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 8,
                                "row": 3,
                                "colspan": 4,
                                "rowspan": 5,
                                "x": 427,
                                "y": 51,
                                "width": 213,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Truck",
                                    "visible": true
                                },
                                "general": {
                                    "x": 427,
                                    "y": 51,
                                    "width": 213,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'filterpane' visual maps directly to Fabric 'slicer' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [
                                "Truck"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Truck",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border_radius": "15px",
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
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px"
                                    }
                                ],
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
                            "title": "grbmmG",
                            "visual_name": "grbmmG",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 4,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Revenue per Load"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Revenue per Load",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                            "title": "Average Revenue per Load",
                            "name": "Average Revenue per Load",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 4,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 213,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Revenue per Load",
                                    "visible": true
                                },
                                "general": {
                                    "x": 213,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Revenue per Load"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Revenue per Load",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#99cfcd",
                                "border_radius": "15px",
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
                                "background": {
                                    "color": "#99cfcd"
                                },
                                "borderRadius": "15px",
                                "components": [
                                    {
                                        "key": "general",
                                        "borderRadius": "15px",
                                        "bgColor": {
                                            "color": {
                                                "index": 2,
                                                "color": "#99cfcd",
                                                "alpha": 1
                                            }
                                        }
                                    },
                                    {
                                        "key": "textAlignment"
                                    },
                                    {
                                        "key": "textBehavior",
                                        "textBehavior": "relative"
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
                                                    "fluid": 0.6
                                                },
                                                "fontStyle": [
                                                    "bold"
                                                ]
                                            }
                                        }
                                    },
                                    {
                                        "key": "firstMeasureValue"
                                    },
                                    {
                                        "key": "secondMeasureTitle"
                                    },
                                    {
                                        "key": "secondMeasureValue"
                                    }
                                ],
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
                                "backgroundColor": "#99cfcd",
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
                            "title": "hSFqB",
                            "visual_name": "hSFqB",
                            "object_category": "other",
                            "chart_type": "qlik-variable-input",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 10,
                            "colspan": 12,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top N Customers",
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
                            "supported": false,
                            "status": "unmapped",
                            "title": "Top N Customers",
                            "name": "Top N Customers",
                            "object_category": "other",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": "Re-create using a single-value slicer bound to a parameter table.",
                            "layout": {
                                "col": 12,
                                "row": 10,
                                "colspan": 12,
                                "rowspan": 2,
                                "x": 640,
                                "y": 171,
                                "width": 640,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Top N Customers",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 171,
                                    "width": 640,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct Power BI visual equivalent. It can be approximated with a textbox for documentation or replaced by a Power BI parameter input (e.g., using a slicer or Power Query parameter). Re-create using a single-value slicer bound to a parameter table.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Top N Customers",
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
                            "score": 0.6,
                            "score_out_of_100": 60,
                            "percentage": "60%",
                            "band": "medium",
                            "llm_score": 0.6,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "fail"
                                }
                            ],
                            "penalties": [],
                            "requires_review": true,
                            "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct Power BI visual equivalent. It can be approximated with a textbox for documentation or replaced by a Power BI parameter input (e.g., using a slicer or Power Query parameter). Re-create using a single-value slicer bound to a parameter table."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "dgEzRMq",
                            "visual_name": "dgEzRMq",
                            "object_category": "other",
                            "chart_type": "qlik-variable-input",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 10,
                            "colspan": 12,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Metric",
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
                            "supported": false,
                            "status": "unmapped",
                            "title": "Metric",
                            "name": "Metric",
                            "object_category": "other",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": "Re-create using a single-value slicer bound to a parameter table.",
                            "layout": {
                                "col": 0,
                                "row": 10,
                                "colspan": 12,
                                "rowspan": 2,
                                "x": 0,
                                "y": 171,
                                "width": 640,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "slicer",
                                "title": {
                                    "text": "Metric",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 171,
                                    "width": 640,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct equivalent in Power BI/Fabric. The closest approximation would be a textbox or custom visual, but native support is unavailable. Marked as unsupported with an unmapped status and a recommendation to implement a custom Power Apps visual or use a parameter input via Power BI's query parameters. Re-create using a single-value slicer bound to a parameter table.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Metric",
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
                            "score": 0.6,
                            "score_out_of_100": 60,
                            "percentage": "60%",
                            "band": "medium",
                            "llm_score": 0.6,
                            "checks": [
                                {
                                    "id": "visual_type_recognized",
                                    "status": "fail"
                                }
                            ],
                            "penalties": [],
                            "requires_review": true,
                            "rationale": "The Qlik Sense chart_type 'qlik-variable-input' has no direct equivalent in Power BI/Fabric. The closest approximation would be a textbox or custom visual, but native support is unavailable. Marked as unsupported with an unmapped status and a recommendation to implement a custom Power Apps visual or use a parameter input via Power BI's query parameters. Re-create using a single-value slicer bound to a parameter table."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "AWSzx",
                            "visual_name": "AWSzx",
                            "object_category": "other",
                            "chart_type": "action-button",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 0,
                            "row": 9,
                            "colspan": 12,
                            "rowspan": 1,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Fleet Opeations",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "actionButton",
                            "bi_type": "actionButton",
                            "supported": true,
                            "status": "mapped",
                            "title": "Go to Fleet Opeations",
                            "name": "Go to Fleet Opeations",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 9,
                                "colspan": 12,
                                "rowspan": 1,
                                "x": 0,
                                "y": 154,
                                "width": 640,
                                "height": 20
                            },
                            "power_bi_visual_type": {
                                "visualType": "actionButton",
                                "title": {
                                    "text": "Go to Fleet Opeations",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 154,
                                    "width": 640,
                                    "height": 20
                                }
                            },
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Fleet Opeations",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
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
                                    "font_family": "Source Sans Pro, sans-serif",
                                    "show": true
                                },
                                "background": {
                                    "color": "#e1dad5"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "title": {
                                            "main": {
                                                "fontFamily": "Source Sans Pro, sans-serif"
                                            }
                                        },
                                        "bgColor": {
                                            "color": {
                                                "index": 12,
                                                "color": "#e1dad5",
                                                "alpha": 1
                                            }
                                        },
                                        "borderColor": {
                                            "index": 15,
                                            "color": "#000000",
                                            "alpha": 1
                                        }
                                    }
                                ],
                                "legend": {
                                    "show": false
                                },
                                "backgroundColor": "#e1dad5"
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
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "JjhAvt",
                            "visual_name": "JjhAvt",
                            "object_category": "other",
                            "chart_type": "action-button",
                            "sheet_name": "Executive Overview",
                            "layout": {},
                            "col": 12,
                            "row": 9,
                            "colspan": 12,
                            "rowspan": 1,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Customer & Revenue Analytics",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e1dad5",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "actionButton",
                            "bi_type": "actionButton",
                            "supported": true,
                            "status": "mapped",
                            "title": "Go to Customer & Revenue Analytics",
                            "name": "Go to Customer & Revenue Analytics",
                            "object_category": "standard",
                            "sheet_name": "Executive Overview",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 9,
                                "colspan": 12,
                                "rowspan": 1,
                                "x": 640,
                                "y": 154,
                                "width": 640,
                                "height": 20
                            },
                            "power_bi_visual_type": {
                                "visualType": "actionButton",
                                "title": {
                                    "text": "Go to Customer & Revenue Analytics",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 154,
                                    "width": 640,
                                    "height": 20
                                }
                            },
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Customer & Revenue Analytics",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e1dad5",
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
                                "background": {
                                    "color": "#e1dad5"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 12,
                                                "color": "#e1dad5",
                                                "alpha": 1
                                            }
                                        },
                                        "borderColor": {
                                            "index": 15,
                                            "color": "#000000",
                                            "alpha": 1
                                        }
                                    }
                                ],
                                "legend": {
                                    "show": false
                                },
                                "backgroundColor": "#e1dad5"
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
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                        }
                    }
                ]
            },
            {
                "sheet_id": "HjfJrj",
                "title": "Fleet Operations",
                "visualization_count": 12,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "rmuRw",
                            "visual_name": "rmuRw",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 4,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Fuel Efficiency"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Fuel Efficiency",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Average Fuel Efficiency",
                            "name": "Average Fuel Efficiency",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 4,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 213,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Fuel Efficiency",
                                    "visible": true
                                },
                                "general": {
                                    "x": 213,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Fuel Efficiency"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Fuel Efficiency",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "eypGTT",
                            "visual_name": "eypGTT",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 16,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Trip Duration"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Trip Duration",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Average Trip Duration",
                            "name": "Average Trip Duration",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 16,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 853,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Trip Duration",
                                    "visible": true
                                },
                                "general": {
                                    "x": 853,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Trip Duration"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Trip Duration",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "eEhJRgX",
                            "visual_name": "eEhJRgX",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 8,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Trip Distance"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Trip Distance",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Average Trip Distance",
                            "name": "Average Trip Distance",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 8,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 427,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Trip Distance",
                                    "visible": true
                                },
                                "general": {
                                    "x": 427,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Trip Distance"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Trip Distance",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "cPjKK",
                            "visual_name": "cPjKK",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 6,
                            "row": 4,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Active Trucks"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Active Trucks",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Active Trucks",
                            "name": "Active Trucks",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 6,
                                "row": 4,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 320,
                                "y": 69,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Active Trucks",
                                    "visible": true
                                },
                                "general": {
                                    "x": 320,
                                    "y": 69,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Active Trucks"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Active Trucks",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "xFpPDH",
                            "visual_name": "xFpPDH",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 20,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Revenue per Mile"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Revenue per Mile",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Revenue per Mile",
                            "name": "Revenue per Mile",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 20,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 1067,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Revenue per Mile",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1067,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Revenue per Mile"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Revenue per Mile",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "HYxBPK",
                            "visual_name": "HYxBPK",
                            "object_category": "other",
                            "chart_type": "treemap",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 0,
                            "row": 3,
                            "colspan": 17,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Trips"
                            ],
                            "x_axis": [
                                "DistanceBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Distance Band Distribution",
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
                            "title": "Distance Band Distribution",
                            "name": "Distance Band Distribution",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 3,
                                "colspan": 17,
                                "rowspan": 4,
                                "x": 0,
                                "y": 51,
                                "width": 907,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "treemap",
                                "title": {
                                    "text": "Distance Band Distribution",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 51,
                                    "width": 907,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                            "y_axis_fields": [
                                "Total Trips"
                            ],
                            "x_axis_fields": [
                                "DistanceBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Distance Band Distribution",
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
                            "title": "mpcAKWU",
                            "visual_name": "mpcAKWU",
                            "object_category": "other",
                            "chart_type": "boxplot",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 17,
                            "row": 3,
                            "colspan": 7,
                            "rowspan": 4,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Avg(idle_time_hours)"
                            ],
                            "x_axis": [
                                "IdleTimeBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Idle Time Analysis",
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
                            "title": "Idle Time Analysis",
                            "name": "Idle Time Analysis",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 17,
                                "row": 3,
                                "colspan": 7,
                                "rowspan": 4,
                                "x": 907,
                                "y": 51,
                                "width": 373,
                                "height": 69
                            },
                            "power_bi_visual_type": {
                                "visualType": "boxPlot",
                                "title": {
                                    "text": "Idle Time Analysis",
                                    "visible": true
                                },
                                "general": {
                                    "x": 907,
                                    "y": 51,
                                    "width": 373,
                                    "height": 69
                                }
                            },
                            "rationale": "The Qlik Sense 'boxplot' visual maps directly to Fabric 'boxPlot' visual.",
                            "y_axis_fields": [
                                "Avg(idle_time_hours)"
                            ],
                            "x_axis_fields": [
                                "IdleTimeBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Idle Time Analysis",
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
                            "title": "PJWEW",
                            "visual_name": "PJWEW",
                            "object_category": "other",
                            "chart_type": "scatterplot",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 0,
                            "row": 7,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Avg(actual_distance_miles)",
                                "Avg(average_mpg)",
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "unit_number"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Truck Performance",
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
                            "title": "Truck Performance",
                            "name": "Truck Performance",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 7,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 120,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "scatterChart",
                                "title": {
                                    "text": "Truck Performance",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 120,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'scatterplot' visual maps directly to Fabric 'scatterChart' visual.",
                            "y_axis_fields": [
                                "Avg(actual_distance_miles)",
                                "Avg(average_mpg)",
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "unit_number"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Truck Performance",
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
                                    },
                                    {
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "$#,##0.0M",
                                        "qDec": ".",
                                        "qThou": ","
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
                            "title": "jbgKqE",
                            "visual_name": "jbgKqE",
                            "object_category": "chart",
                            "chart_type": "funnel",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 12,
                            "row": 7,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Loads"
                            ],
                            "x_axis": [
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "High Value Loads",
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
                            "visual_type": "funnel",
                            "bi_type": "funnel",
                            "supported": true,
                            "status": "mapped",
                            "title": "High Value Loads",
                            "name": "High Value Loads",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 7,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 120,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "funnel",
                                "title": {
                                    "text": "High Value Loads",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 120,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'funnel' visual maps directly to Fabric 'funnel' visual.",
                            "y_axis_fields": [
                                "Total Loads"
                            ],
                            "x_axis_fields": [
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "High Value Loads",
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
                            "rationale": "The Qlik Sense 'funnel' visual maps directly to Fabric 'funnel' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "KKFj",
                            "visual_name": "KKFj",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 12,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Fleet Operations"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Fleet Operations",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                            "title": "Fleet Operations",
                            "name": "Fleet Operations",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 3,
                                "x": 640,
                                "y": 0,
                                "width": 213,
                                "height": 51
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Fleet Operations",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 0,
                                    "width": 213,
                                    "height": 51
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Fleet Operations"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Fleet Operations",
                                "title_font_size": "M",
                                "title_font_family": "Segoe UI, sans-serif",
                                "background_color": "#e0bd8d",
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
                                "background": {
                                    "color": "#e0bd8d"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "bgColor": {
                                            "color": {
                                                "index": 11,
                                                "color": "#e0bd8d",
                                                "alpha": 1
                                            }
                                        }
                                    }
                                ],
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
                                "backgroundColor": "#e0bd8d",
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
                            "title": "ffTSNj",
                            "visual_name": "ffTSNj",
                            "object_category": "other",
                            "chart_type": "action-button",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 0,
                            "row": 12,
                            "colspan": 12,
                            "rowspan": 1,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Executive overview",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "actionButton",
                            "bi_type": "actionButton",
                            "supported": true,
                            "status": "mapped",
                            "title": "Go to Executive overview",
                            "name": "Go to Executive overview",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 12,
                                "colspan": 12,
                                "rowspan": 1,
                                "x": 0,
                                "y": 206,
                                "width": 640,
                                "height": 20
                            },
                            "power_bi_visual_type": {
                                "visualType": "actionButton",
                                "title": {
                                    "text": "Go to Executive overview",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 206,
                                    "width": 640,
                                    "height": 20
                                }
                            },
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Executive overview",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
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
                                    "font_family": "Source Sans Pro, sans-serif",
                                    "show": true
                                },
                                "background": {
                                    "color": "#e1dad5"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "title": {
                                            "main": {
                                                "fontFamily": "Source Sans Pro, sans-serif"
                                            }
                                        },
                                        "bgColor": {
                                            "color": {
                                                "index": 12,
                                                "color": "#e1dad5",
                                                "alpha": 1
                                            }
                                        },
                                        "borderColor": {
                                            "index": 15,
                                            "color": "#000000",
                                            "alpha": 1
                                        }
                                    }
                                ],
                                "legend": {
                                    "show": false
                                },
                                "backgroundColor": "#e1dad5"
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
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "EVktj",
                            "visual_name": "EVktj",
                            "object_category": "other",
                            "chart_type": "action-button",
                            "sheet_name": "Fleet Operations",
                            "layout": {},
                            "col": 12,
                            "row": 12,
                            "colspan": 12,
                            "rowspan": 1,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Customer & Revenue Analytics",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
                                "border": {
                                    "show": false
                                },
                                "legend": {
                                    "show": false
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "actionButton",
                            "bi_type": "actionButton",
                            "supported": true,
                            "status": "mapped",
                            "title": "Go to Customer & Revenue Analytics",
                            "name": "Go to Customer & Revenue Analytics",
                            "object_category": "standard",
                            "sheet_name": "Fleet Operations",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 12,
                                "colspan": 12,
                                "rowspan": 1,
                                "x": 640,
                                "y": 206,
                                "width": 640,
                                "height": 20
                            },
                            "power_bi_visual_type": {
                                "visualType": "actionButton",
                                "title": {
                                    "text": "Go to Customer & Revenue Analytics",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 206,
                                    "width": 640,
                                    "height": 20
                                }
                            },
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Go to Customer & Revenue Analytics",
                                "title_font_family": "Source Sans Pro, sans-serif",
                                "background_color": "#e1dad5",
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
                                    "font_family": "Source Sans Pro, sans-serif",
                                    "show": true
                                },
                                "background": {
                                    "color": "#e1dad5"
                                },
                                "components": [
                                    {
                                        "key": "general",
                                        "title": {
                                            "main": {
                                                "fontFamily": "Source Sans Pro, sans-serif"
                                            }
                                        },
                                        "bgColor": {
                                            "color": {
                                                "index": 12,
                                                "color": "#e1dad5",
                                                "alpha": 1
                                            }
                                        },
                                        "borderColor": {
                                            "index": 15,
                                            "color": "#000000",
                                            "alpha": 1
                                        }
                                    }
                                ],
                                "legend": {
                                    "show": false
                                },
                                "backgroundColor": "#e1dad5"
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
                            "rationale": "The Qlik Sense 'action-button' visual maps directly to Fabric 'actionButton' visual."
                        }
                    }
                ]
            },
            {
                "sheet_id": "xpNQLL",
                "title": "Customer & Revenue Analytics",
                "visualization_count": 15,
                "visualizations": [
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "NgkPzp",
                            "visual_name": "NgkPzp",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 0,
                            "row": 0,
                            "colspan": 5,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Highest Revenue by Customer"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Highest Revenue by Customer",
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
                            "title": "Highest Revenue by Customer",
                            "name": "Highest Revenue by Customer",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 0,
                                "colspan": 5,
                                "rowspan": 2,
                                "x": 0,
                                "y": 0,
                                "width": 267,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Highest Revenue by Customer",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 267,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Highest Revenue by Customer"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Highest Revenue by Customer",
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
                            "title": "bWNPnp",
                            "visual_name": "bWNPnp",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 19,
                            "row": 0,
                            "colspan": 5,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "High Value Revenue %"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "High Value Revenue %",
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
                            "title": "High Value Revenue %",
                            "name": "High Value Revenue %",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 19,
                                "row": 0,
                                "colspan": 5,
                                "rowspan": 2,
                                "x": 1013,
                                "y": 0,
                                "width": 267,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "High Value Revenue %",
                                    "visible": true
                                },
                                "general": {
                                    "x": 1013,
                                    "y": 0,
                                    "width": 267,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "High Value Revenue %"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "High Value Revenue %",
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
                            "title": "zxPNm",
                            "visual_name": "zxPNm",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 10,
                            "row": 0,
                            "colspan": 4,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "High Value Loads"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "High Value Loads",
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
                            "title": "High Value Loads",
                            "name": "High Value Loads",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 10,
                                "row": 0,
                                "colspan": 4,
                                "rowspan": 2,
                                "x": 533,
                                "y": 0,
                                "width": 213,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "High Value Loads",
                                    "visible": true
                                },
                                "general": {
                                    "x": 533,
                                    "y": 0,
                                    "width": 213,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "High Value Loads"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "High Value Loads",
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
                            "title": "TYnajA",
                            "visual_name": "TYnajA",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 14,
                            "row": 0,
                            "colspan": 5,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Average Revenue per Customer"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Revenue per Customer",
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
                            "title": "Average Revenue per Customer",
                            "name": "Average Revenue per Customer",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 14,
                                "row": 0,
                                "colspan": 5,
                                "rowspan": 2,
                                "x": 747,
                                "y": 0,
                                "width": 267,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Average Revenue per Customer",
                                    "visible": true
                                },
                                "general": {
                                    "x": 747,
                                    "y": 0,
                                    "width": 267,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Average Revenue per Customer"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Average Revenue per Customer",
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
                            "title": "mubYNVd",
                            "visual_name": "mubYNVd",
                            "object_category": "other",
                            "chart_type": "kpi",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 5,
                            "row": 0,
                            "colspan": 5,
                            "rowspan": 2,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Completed Trip Revenue"
                            ],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Completed Trip Revenue",
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
                            "title": "Completed Trip Revenue",
                            "name": "Completed Trip Revenue",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 5,
                                "row": 0,
                                "colspan": 5,
                                "rowspan": 2,
                                "x": 267,
                                "y": 0,
                                "width": 267,
                                "height": 34
                            },
                            "power_bi_visual_type": {
                                "visualType": "card",
                                "title": {
                                    "text": "Completed Trip Revenue",
                                    "visible": true
                                },
                                "general": {
                                    "x": 267,
                                    "y": 0,
                                    "width": 267,
                                    "height": 34
                                }
                            },
                            "rationale": "The Qlik Sense 'kpi' visual maps directly to Fabric 'card' visual.",
                            "y_axis_fields": [
                                "Completed Trip Revenue"
                            ],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": false,
                                "title": "Completed Trip Revenue",
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
                            "title": "cTfPhEj",
                            "visual_name": "cTfPhEj",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 0,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Customer",
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
                            "title": "Customer",
                            "name": "Customer",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
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
                                    "text": "Customer",
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
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Customer",
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
                            "title": "JxjPRPg",
                            "visual_name": "JxjPRPg",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 18,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Route",
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
                            "title": "Route",
                            "name": "Route",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
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
                                    "text": "Route",
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
                                "Route"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "Route",
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
                            "title": "rprpnyy",
                            "visual_name": "rprpnyy",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 12,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "RevenueBand",
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
                            "title": "RevenueBand",
                            "name": "RevenueBand",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
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
                                    "text": "RevenueBand",
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
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": false,
                                "title": "RevenueBand",
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
                            "title": "DsKZpQW",
                            "visual_name": "DsKZpQW",
                            "object_category": "other",
                            "chart_type": "filterpane",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 6,
                            "row": 2,
                            "colspan": 6,
                            "rowspan": 3,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [
                                "MonthYear"
                            ],
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
                            }
                        },
                        "fabric": {
                            "visual_type": "slicer",
                            "bi_type": "slicer",
                            "supported": true,
                            "status": "mapped",
                            "title": "MonthYear",
                            "name": "MonthYear",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
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
                                    "text": "MonthYear",
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
                                "MonthYear"
                            ],
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
                            "title": "cPBNNjB",
                            "visual_name": "cPBNNjB",
                            "object_category": "other",
                            "chart_type": "treemap",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 0,
                            "row": 5,
                            "colspan": 9,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue Contribution by Customer",
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
                            "title": "Revenue Contribution by Customer",
                            "name": "Revenue Contribution by Customer",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 5,
                                "colspan": 9,
                                "rowspan": 5,
                                "x": 0,
                                "y": 86,
                                "width": 480,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "treemap",
                                "title": {
                                    "text": "Revenue Contribution by Customer",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 86,
                                    "width": 480,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'treemap' visual maps directly to Fabric 'treemap' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "Customer"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue Contribution by Customer",
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
                                        "qType": "R",
                                        "qnDec": 2,
                                        "qUseThou": 0,
                                        "qFmt": "$#,##0.0M",
                                        "qDec": ".",
                                        "qThou": ","
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
                            "title": "tGaxu",
                            "visual_name": "tGaxu",
                            "object_category": "chart",
                            "chart_type": "linechart",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 0,
                            "row": 10,
                            "colspan": 24,
                            "rowspan": 6,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "MonthYear"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Monthly Customer Revenue Trend",
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
                            "title": "Monthly Customer Revenue Trend",
                            "name": "Monthly Customer Revenue Trend",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 10,
                                "colspan": 24,
                                "rowspan": 6,
                                "x": 0,
                                "y": 171,
                                "width": 1280,
                                "height": 103
                            },
                            "power_bi_visual_type": {
                                "visualType": "lineChart",
                                "title": {
                                    "text": "Monthly Customer Revenue Trend",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 171,
                                    "width": 1280,
                                    "height": 103
                                }
                            },
                            "rationale": "The Qlik Sense 'linechart' visual maps directly to Fabric 'lineChart' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "MonthYear"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Monthly Customer Revenue Trend",
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
                                    "persistent": true,
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
                                        "continuousAuto": false,
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
                                        "qFmt": "$#,##0.0M",
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
                            "title": "jQXpenC",
                            "visual_name": "jQXpenC",
                            "object_category": "other",
                            "chart_type": "piechart",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 17,
                            "row": 5,
                            "colspan": 7,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Loads"
                            ],
                            "x_axis": [
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Load Distribution by Revenue Band",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
                                },
                                "legend": {
                                    "show": true,
                                    "dock": "auto"
                                }
                            }
                        },
                        "fabric": {
                            "visual_type": "donutChart",
                            "bi_type": "donutChart",
                            "supported": true,
                            "status": "mapped",
                            "title": "Load Distribution by Revenue Band",
                            "name": "Load Distribution by Revenue Band",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 17,
                                "row": 5,
                                "colspan": 7,
                                "rowspan": 5,
                                "x": 907,
                                "y": 86,
                                "width": 373,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "donutChart",
                                "title": {
                                    "text": "Load Distribution by Revenue Band",
                                    "visible": true
                                },
                                "general": {
                                    "x": 907,
                                    "y": 86,
                                    "width": 373,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual.",
                            "y_axis_fields": [
                                "Total Loads"
                            ],
                            "x_axis_fields": [
                                "RevenueBand"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Load Distribution by Revenue Band",
                                "title_font_family": "Segoe UI, sans-serif",
                                "border": {
                                    "show": false
                                },
                                "inner_radius": 0.55,
                                "stroke_color": {
                                    "index": -1,
                                    "color": "#FFFFFF"
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
                                "innerRadius": 0.55,
                                "strokeColor": "#FFFFFF",
                                "components": [
                                    {
                                        "key": "slices",
                                        "style": {
                                            "strokeWidth": "none",
                                            "strokeColor": {
                                                "index": -1,
                                                "color": "#FFFFFF"
                                            },
                                            "cornerRadius": 0,
                                            "innerRadius": 0.55
                                        }
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
                            "rationale": "The Qlik Sense 'piechart' visual maps directly to Fabric 'donutChart' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "hPBvpkk",
                            "visual_name": "hPBvpkk",
                            "object_category": "chart",
                            "chart_type": "barchart",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 9,
                            "row": 5,
                            "colspan": 8,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [
                                "Total Revenue"
                            ],
                            "x_axis": [
                                "Booking Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue by Booking Type",
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
                            "title": "Revenue by Booking Type",
                            "name": "Revenue by Booking Type",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 9,
                                "row": 5,
                                "colspan": 8,
                                "rowspan": 5,
                                "x": 480,
                                "y": 86,
                                "width": 427,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "barChart",
                                "title": {
                                    "text": "Revenue by Booking Type",
                                    "visible": true
                                },
                                "general": {
                                    "x": 480,
                                    "y": 86,
                                    "width": 427,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'barchart' visual maps directly to Fabric 'barChart' visual.",
                            "y_axis_fields": [
                                "Total Revenue"
                            ],
                            "x_axis_fields": [
                                "Booking Type"
                            ],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue by Booking Type",
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
                                "auto": false,
                                "mode": "primary",
                                "single_color": "#ac4d58",
                                "raw_single_color": "#ac4d58",
                                "dimension_scheme": "12",
                                "measure_scheme": "sg",
                                "palette_index": 10,
                                "palette_scheme": "12",
                                "is_multicolor": true,
                                "use_base_colors": "on"
                            },
                            "style_and_formatting": {
                                "title": {
                                    "show": true
                                },
                                "colorScheme": {
                                    "auto": false,
                                    "mode": "primary",
                                    "formatting": {
                                        "numFormatFromTemplate": true,
                                        "quarantine": {
                                            "isCustomFormatted": false
                                        }
                                    },
                                    "useBaseColors": "off",
                                    "paletteColor": {
                                        "index": 10,
                                        "color": "#ac4d58",
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
                                    "altLabel": "AjfgE",
                                    "byMeasureDef": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
                                    },
                                    "byDimDef": {
                                        "label": "mZVtGZ",
                                        "key": "mZVtGZ",
                                        "type": "libraryItem"
                                    }
                                },
                                "data_colors": {
                                    "primary": "#ac4d58",
                                    "mode": "primary",
                                    "auto": false,
                                    "by_measure": {
                                        "label": "AjfgE",
                                        "key": "AjfgE",
                                        "type": "libraryItem"
                                    },
                                    "by_dimension": {
                                        "label": "mZVtGZ",
                                        "key": "mZVtGZ",
                                        "type": "libraryItem"
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
                                        "qFmt": "$#,##0.0M",
                                        "qDec": ".",
                                        "qThou": ","
                                    }
                                ],
                                "orientation": "horizontal",
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
                            "title": "UtkCby",
                            "visual_name": "UtkCby",
                            "object_category": "other",
                            "chart_type": "sn-image",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 0,
                            "row": 16,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Customer Analytics",
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
                            "visual_type": "image",
                            "bi_type": "image",
                            "supported": true,
                            "status": "mapped",
                            "title": "Customer Analytics",
                            "name": "Customer Analytics",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 0,
                                "row": 16,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 0,
                                "y": 274,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "image",
                                "title": {
                                    "text": "Customer Analytics",
                                    "visible": true
                                },
                                "general": {
                                    "x": 0,
                                    "y": 274,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Customer Analytics",
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
                            "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual."
                        }
                    },
                    {
                        "name": "DashboardObject",
                        "qlik_source": {
                            "title": "BJpSGS",
                            "visual_name": "BJpSGS",
                            "object_category": "other",
                            "chart_type": "sn-image",
                            "sheet_name": "Customer & Revenue Analytics",
                            "layout": {},
                            "col": 12,
                            "row": 16,
                            "colspan": 12,
                            "rowspan": 5,
                            "header_styling": {},
                            "card_styling": {},
                            "y_axis": [],
                            "x_axis": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue Analytics",
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
                            "visual_type": "image",
                            "bi_type": "image",
                            "supported": true,
                            "status": "mapped",
                            "title": "Revenue Analytics",
                            "name": "Revenue Analytics",
                            "object_category": "standard",
                            "sheet_name": "Customer & Revenue Analytics",
                            "replacement_strategy": null,
                            "layout": {
                                "col": 12,
                                "row": 16,
                                "colspan": 12,
                                "rowspan": 5,
                                "x": 640,
                                "y": 274,
                                "width": 640,
                                "height": 86
                            },
                            "power_bi_visual_type": {
                                "visualType": "image",
                                "title": {
                                    "text": "Revenue Analytics",
                                    "visible": true
                                },
                                "general": {
                                    "x": 640,
                                    "y": 274,
                                    "width": 640,
                                    "height": 86
                                }
                            },
                            "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual.",
                            "y_axis_fields": [],
                            "x_axis_fields": [],
                            "formatting": {
                                "show_titles": true,
                                "title": "Revenue Analytics",
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
                            "rationale": "The Qlik Sense 'sn-image' visual maps directly to Fabric 'image' visual."
                        }
                    }
                ]
            }
        ]
    },
    "filters": [
        {
            "name": "customer_name",
            "qlik_source": {
                "name": "customer_name",
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
            "name": "=origin_city & ' → ' & destination_city",
            "qlik_source": {
                "name": "=origin_city & ' → ' & destination_city",
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
            "name": "load_type",
            "qlik_source": {
                "name": "load_type",
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
            "name": "=first_name & ' ' & last_name",
            "qlik_source": {
                "name": "=first_name & ' ' & last_name",
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
            "name": "=Month(load_date)",
            "qlik_source": {
                "name": "=Month(load_date)",
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
            "name": "=unit_number",
            "qlik_source": {
                "name": "=unit_number",
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
            "name": "customer_name",
            "qlik_source": {
                "name": "customer_name",
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
            "name": "=origin_city & ' → ' & destination_city",
            "qlik_source": {
                "name": "=origin_city & ' → ' & destination_city",
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
            "name": "RevenueBand",
            "qlik_source": {
                "name": "RevenueBand",
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
            "name": "MonthYear",
            "qlik_source": {
                "name": "MonthYear",
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
                "id": "48549b8f-d230-4cb3-897d-7f14ba2a66ad",
                "name": "MoneyThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "48549b8f-d230-4cb3-897d-7f14ba2a66ad",
                    "qType": "variable"
                }
            },
            {
                "id": "f9397b21-2acf-498c-914d-3e029e7467ae",
                "name": "ThousandSep",
                "definition": ",",
                "value": ",",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET ThousandSep=',';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "f9397b21-2acf-498c-914d-3e029e7467ae",
                    "qType": "variable"
                }
            },
            {
                "id": "b7b8fceb-e946-4272-bb2b-86f68bd21000",
                "name": "MoneyFormat",
                "definition": "$ ###0.00;-$ ###0.00",
                "value": "$ ###0.00;-$ ###0.00",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyFormat='$ ###0.00;-$ ###0.00';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "b7b8fceb-e946-4272-bb2b-86f68bd21000",
                    "qType": "variable"
                }
            },
            {
                "id": "ae9899dd-dc97-4fa4-9a48-84fabfcab05a",
                "name": "TimeFormat",
                "definition": "h:mm:ss TT",
                "value": "h:mm:ss TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimeFormat='h:mm:ss TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "ae9899dd-dc97-4fa4-9a48-84fabfcab05a",
                    "qType": "variable"
                }
            },
            {
                "id": "a91e768f-4bd9-4f02-a021-33a2527e75e2",
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
                    "qId": "a91e768f-4bd9-4f02-a021-33a2527e75e2",
                    "qType": "variable"
                }
            },
            {
                "id": "6595bbf1-ef18-47f1-a465-e4c81cc8031b",
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
                    "qId": "6595bbf1-ef18-47f1-a465-e4c81cc8031b",
                    "qType": "variable"
                }
            },
            {
                "id": "3924ba5f-34c9-479e-9460-4d071b0ea7e8",
                "name": "MonthNames",
                "definition": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "value": "Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MonthNames='Jan;Feb;Mar;Apr;May;Jun;Jul;Aug;Sep;Oct;Nov;Dec';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "3924ba5f-34c9-479e-9460-4d071b0ea7e8",
                    "qType": "variable"
                }
            },
            {
                "id": "89a3357d-f2ac-496b-aee7-d42440cfa919",
                "name": "LongDayNames",
                "definition": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "value": "Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongDayNames='Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "89a3357d-f2ac-496b-aee7-d42440cfa919",
                    "qType": "variable"
                }
            },
            {
                "id": "68cc4889-f9e2-40f5-ad7a-899c0c45b07e",
                "name": "ScriptError",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "68cc4889-f9e2-40f5-ad7a-899c0c45b07e",
                    "qType": "variable"
                }
            },
            {
                "id": "5530e8f8-f9d8-4fd6-9066-de1cc00dcd3c",
                "name": "ScriptErrorCount",
                "definition": "0",
                "value": "0",
                "num_value": 0,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "5530e8f8-f9d8-4fd6-9066-de1cc00dcd3c",
                    "qType": "variable"
                }
            },
            {
                "id": "a63f18f1-6f22-44a9-8e10-2e47019a0ed9",
                "name": "ScriptErrorList",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "a63f18f1-6f22-44a9-8e10-2e47019a0ed9",
                    "qType": "variable"
                }
            },
            {
                "id": "b89e235b-54ad-4a3a-be5c-d0c41f83762d",
                "name": "DateFormat",
                "definition": "M/D/YYYY",
                "value": "M/D/YYYY",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DateFormat='M/D/YYYY';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "b89e235b-54ad-4a3a-be5c-d0c41f83762d",
                    "qType": "variable"
                }
            },
            {
                "id": "48482be6-6bfa-44de-bbac-86cdc00a09a6",
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
                    "qId": "48482be6-6bfa-44de-bbac-86cdc00a09a6",
                    "qType": "variable"
                }
            },
            {
                "id": "960fab41-061b-43ac-8650-b61f916b4162",
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
                    "qId": "960fab41-061b-43ac-8650-b61f916b4162",
                    "qType": "variable"
                }
            },
            {
                "id": "3e33be3b-4943-4e11-814c-58129e58c579",
                "name": "ErrorMode",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "3e33be3b-4943-4e11-814c-58129e58c579",
                    "qType": "variable"
                }
            },
            {
                "id": "c2899323-edd3-4e30-96ea-9ba637a1bfa9",
                "name": "StripComments",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "c2899323-edd3-4e30-96ea-9ba637a1bfa9",
                    "qType": "variable"
                }
            },
            {
                "id": "17df9275-e060-4d88-b5a1-e40367d2ce47",
                "name": "OpenUrlTimeout",
                "definition": "86400",
                "value": "86400",
                "num_value": 86400,
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "usage_count": 0,
                "qInfo": {
                    "qId": "17df9275-e060-4d88-b5a1-e40367d2ce47",
                    "qType": "variable"
                }
            },
            {
                "id": "b56abf1d-009a-4686-8672-55316145b243",
                "name": "DecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "b56abf1d-009a-4686-8672-55316145b243",
                    "qType": "variable"
                }
            },
            {
                "id": "bb7262bf-9a21-4f0f-8617-f461c9dc9185",
                "name": "TimestampFormat",
                "definition": "M/D/YYYY h:mm:ss[.fff] TT",
                "value": "M/D/YYYY h:mm:ss[.fff] TT",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET TimestampFormat='M/D/YYYY h:mm:ss[.fff] TT';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "bb7262bf-9a21-4f0f-8617-f461c9dc9185",
                    "qType": "variable"
                }
            },
            {
                "id": "2b31c79f-1803-4ee2-bc93-5f72affa3c2a",
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
                    "qId": "2b31c79f-1803-4ee2-bc93-5f72affa3c2a",
                    "qType": "variable"
                }
            },
            {
                "id": "c809e855-322f-447b-aa36-e8fea6ef5894",
                "name": "CollationLocale",
                "definition": "en-US",
                "value": "en-US",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET CollationLocale='en-US';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "c809e855-322f-447b-aa36-e8fea6ef5894",
                    "qType": "variable"
                }
            },
            {
                "id": "65685e68-b625-4c2b-9d38-6519eaf9c253",
                "name": "LongMonthNames",
                "definition": "January;February;March;April;May;June;July;August;September;October;November;December",
                "value": "January;February;March;April;May;June;July;August;September;October;November;December",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET LongMonthNames='January;February;March;April;May;June;July;August;September;October;November;December';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "65685e68-b625-4c2b-9d38-6519eaf9c253",
                    "qType": "variable"
                }
            },
            {
                "id": "3fdbaf36-9d7e-4a52-94cb-db55a4b38a13",
                "name": "DayNames",
                "definition": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "value": "Mon;Tue;Wed;Thu;Fri;Sat;Sun",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET DayNames='Mon;Tue;Wed;Thu;Fri;Sat;Sun';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "3fdbaf36-9d7e-4a52-94cb-db55a4b38a13",
                    "qType": "variable"
                }
            },
            {
                "id": "f6c200bb-49d7-4502-97c6-ee11ed4b9ddb",
                "name": "NumericalAbbreviation",
                "definition": "3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y",
                "value": "3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET NumericalAbbreviation='3:k;6:M;9:G;12:T;15:P;18:E;21:Z;24:Y;-3:m;-6:μ;-9:n;-12:p;-15:f;-18:a;-21:z;-24:y';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "f6c200bb-49d7-4502-97c6-ee11ed4b9ddb",
                    "qType": "variable"
                }
            },
            {
                "id": "a706d462-2c77-475c-9ec4-cfcdea2d2f93",
                "name": "MoneyDecimalSep",
                "definition": ".",
                "value": ".",
                "is_script_created": true,
                "is_reserved": true,
                "is_config": false,
                "script_line": "SET MoneyDecimalSep='.';",
                "usage_count": 0,
                "qInfo": {
                    "qId": "a706d462-2c77-475c-9ec4-cfcdea2d2f93",
                    "qType": "variable"
                }
            },
            {
                "id": "4fb218e3-b4ec-48da-b2db-4811ea107e6a",
                "name": "vMinDate",
                "definition": "44562",
                "value": "44562",
                "num_value": 44562,
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "script_line": "LET vMinDate = Num(Peek('MinDate', 0, 'TempCalendar'));",
                "usage_count": 0,
                "qInfo": {
                    "qId": "4fb218e3-b4ec-48da-b2db-4811ea107e6a",
                    "qType": "variable"
                }
            },
            {
                "id": "6df450bf-ca1e-4c64-83a1-63f89f2af87d",
                "name": "vMaxDate",
                "definition": "45657",
                "value": "45657",
                "num_value": 45657,
                "is_script_created": true,
                "is_reserved": false,
                "is_config": false,
                "script_line": "LET vMaxDate = Num(Peek('MaxDate', 0, 'TempCalendar'));",
                "usage_count": 0,
                "qInfo": {
                    "qId": "6df450bf-ca1e-4c64-83a1-63f89f2af87d",
                    "qType": "variable"
                }
            },
            {
                "id": "381c9234-e685-4fac-816d-e3fdd0396ba5",
                "name": "vTopN",
                "definition": "10",
                "value": "10",
                "num_value": 10,
                "description": "Number of top customers to display",
                "comment": "Number of top customers to display",
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "used_in_sheets": [
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview"
                    }
                ],
                "used_in_visualizations": [
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "hqpgX",
                        "visualization_title": "Top 10 Customers by Revenue",
                        "visualization_type": "barchart"
                    },
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "hSFqB",
                        "visualization_title": "Top N Customers",
                        "visualization_type": "qlik-variable-input"
                    }
                ],
                "usage_count": 3,
                "qInfo": {
                    "qId": "381c9234-e685-4fac-816d-e3fdd0396ba5",
                    "qType": "variable"
                }
            },
            {
                "id": "006717ea-e706-4d79-b21e-a951e1424ce5",
                "name": "vMeasure",
                "definition": "1",
                "value": "1",
                "num_value": 1,
                "description": "Dynamic measure for chart analysis",
                "comment": "Dynamic measure for chart analysis",
                "is_script_created": false,
                "is_reserved": false,
                "is_config": false,
                "used_in_sheets": [
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview"
                    }
                ],
                "used_in_visualizations": [
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "xbTxPjC",
                        "visualization_title": "='Monthly ' & Pick(     $(vMeasure),     'Revenue',     'Trips',     'Customers',     'Drivers' ) & ' Trend'",
                        "visualization_type": "linechart"
                    },
                    {
                        "sheet_id": "CqUTPj",
                        "sheet_title": "Executive Overview",
                        "visualization_id": "dgEzRMq",
                        "visualization_title": "Metric",
                        "visualization_type": "qlik-variable-input"
                    }
                ],
                "usage_count": 3,
                "qInfo": {
                    "qId": "006717ea-e706-4d79-b21e-a951e1424ce5",
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
        "count": 1,
        "converted_items": [
            {
                "qProperty": {
                    "qInfo": {
                        "qId": "btbwk",
                        "qType": "story"
                    },
                    "qMetaDef": {
                        "title": "My new story"
                    },
                    "creationDate": "2026-08-10T04:32:41.963Z",
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
                                "qId": "ZKPXKf",
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
                "id": "btbwk",
                "title": "My new story",
                "slides": [
                    {
                        "index": 0,
                        "id": "ZKPXKf",
                        "type": "slide",
                        "rank": -1,
                        "item_count": 0
                    }
                ],
                "slide_count": 1
            }
        ],
        "not_found_msg": null
    },
    "bookmarks": {
        "count": 3,
        "converted_items": [
            {
                "qInfo": {
                    "qId": "1e935e8e-3090-41cb-a92b-0118cfbc67c9",
                    "qType": "bookmark"
                },
                "qMeta": {
                    "_resourcetype": "app.object",
                    "_objecttype": "bookmark",
                    "id": "1e935e8e-3090-41cb-a92b-0118cfbc67c9",
                    "approved": false,
                    "published": false,
                    "owner": "auth0|8a1e70903ef66d05b2b4eb57d0907f6a85989721a16e4351c5a7be507387b9aa",
                    "ownerId": "6a8d0f4b51a463e48fce8198",
                    "createdDate": "2026-08-30T06:37:20.271Z",
                    "modifiedDate": "2026-08-30T06:37:20.271Z",
                    "encrypted": true,
                    "privileges": [
                        "read",
                        "update",
                        "delete",
                        "publish",
                        "change_owner"
                    ],
                    "title": "Fuel Efficiency",
                    "description": "Fleet operations focused on fuel efficiency",
                    "isExtended": false
                },
                "qData": {
                    "qBookmark": {
                        "qStateData": [
                            {
                                "qStateName": "$"
                            }
                        ],
                        "qUtcModifyTime": 46247.133150752314
                    },
                    "title": "Fuel Efficiency",
                    "description": "Fleet operations focused on fuel efficiency",
                    "sheetId": "HjfJrj",
                    "creationDate": "2026-08-13T03:11:43.871Z"
                },
                "id": "1e935e8e-3090-41cb-a92b-0118cfbc67c9",
                "title": "Fuel Efficiency",
                "description": "Fleet operations focused on fuel efficiency",
                "sheet_id": "HjfJrj",
                "creation_date": "2026-08-13T03:11:43.871Z",
                "owner_id": "6a8d0f4b51a463e48fce8198",
                "published": false,
                "approved": false,
                "qProperty": {
                    "qInfo": {
                        "qId": "1e935e8e-3090-41cb-a92b-0118cfbc67c9",
                        "qType": "bookmark"
                    },
                    "qMetaDef": {
                        "title": "Fuel Efficiency",
                        "description": "Fleet operations focused on fuel efficiency",
                        "isExtended": false
                    },
                    "creationDate": "2026-08-13T03:11:43.871Z",
                    "sheetId": "HjfJrj"
                }
            },
            {
                "qInfo": {
                    "qId": "379133ad-1814-4daa-aa3c-0fd6ed5d63dc",
                    "qType": "bookmark"
                },
                "qMeta": {
                    "_resourcetype": "app.object",
                    "_objecttype": "bookmark",
                    "id": "379133ad-1814-4daa-aa3c-0fd6ed5d63dc",
                    "approved": false,
                    "published": false,
                    "owner": "auth0|8a1e70903ef66d05b2b4eb57d0907f6a85989721a16e4351c5a7be507387b9aa",
                    "ownerId": "6a8d0f4b51a463e48fce8198",
                    "createdDate": "2026-08-30T06:37:20.278Z",
                    "modifiedDate": "2026-08-30T06:37:20.278Z",
                    "encrypted": true,
                    "privileges": [
                        "read",
                        "update",
                        "delete",
                        "publish",
                        "change_owner"
                    ],
                    "title": "High Value Loads",
                    "description": "Fleet operations view focused on high value loads",
                    "isExtended": false
                },
                "qData": {
                    "qBookmark": {
                        "qStateData": [
                            {
                                "qStateName": "$"
                            }
                        ],
                        "qUtcModifyTime": 46247.132808090275
                    },
                    "title": "High Value Loads",
                    "description": "Fleet operations view focused on high value loads",
                    "sheetId": "HjfJrj",
                    "creationDate": "2026-08-13T03:11:14.175Z"
                },
                "id": "379133ad-1814-4daa-aa3c-0fd6ed5d63dc",
                "title": "High Value Loads",
                "description": "Fleet operations view focused on high value loads",
                "sheet_id": "HjfJrj",
                "creation_date": "2026-08-13T03:11:14.175Z",
                "owner_id": "6a8d0f4b51a463e48fce8198",
                "published": false,
                "approved": false,
                "qProperty": {
                    "qInfo": {
                        "qId": "379133ad-1814-4daa-aa3c-0fd6ed5d63dc",
                        "qType": "bookmark"
                    },
                    "qMetaDef": {
                        "title": "High Value Loads",
                        "description": "Fleet operations view focused on high value loads",
                        "isExtended": false
                    },
                    "creationDate": "2026-08-13T03:11:14.175Z",
                    "sheetId": "HjfJrj"
                }
            },
            {
                "qInfo": {
                    "qId": "a3db9a77-2436-4642-9a43-6f056ba3d4ec",
                    "qType": "bookmark"
                },
                "qMeta": {
                    "_resourcetype": "app.object",
                    "_objecttype": "bookmark",
                    "id": "a3db9a77-2436-4642-9a43-6f056ba3d4ec",
                    "approved": false,
                    "published": false,
                    "owner": "auth0|8a1e70903ef66d05b2b4eb57d0907f6a85989721a16e4351c5a7be507387b9aa",
                    "ownerId": "6a8d0f4b51a463e48fce8198",
                    "createdDate": "2026-08-30T06:37:20.314Z",
                    "modifiedDate": "2026-08-30T06:37:20.314Z",
                    "encrypted": true,
                    "privileges": [
                        "read",
                        "update",
                        "delete",
                        "publish",
                        "change_owner"
                    ],
                    "title": "Overall Operations",
                    "description": "Overall fleet operations performance",
                    "isExtended": false
                },
                "qData": {
                    "qBookmark": {
                        "qStateData": [
                            {
                                "qStateName": "$"
                            }
                        ],
                        "qUtcModifyTime": 46247.132460891204
                    },
                    "title": "Overall Operations",
                    "description": "Overall fleet operations performance",
                    "sheetId": "HjfJrj",
                    "creationDate": "2026-08-13T03:10:44.257Z"
                },
                "id": "a3db9a77-2436-4642-9a43-6f056ba3d4ec",
                "title": "Overall Operations",
                "description": "Overall fleet operations performance",
                "sheet_id": "HjfJrj",
                "creation_date": "2026-08-13T03:10:44.257Z",
                "owner_id": "6a8d0f4b51a463e48fce8198",
                "published": false,
                "approved": false,
                "qProperty": {
                    "qInfo": {
                        "qId": "a3db9a77-2436-4642-9a43-6f056ba3d4ec",
                        "qType": "bookmark"
                    },
                    "qMetaDef": {
                        "title": "Overall Operations",
                        "description": "Overall fleet operations performance",
                        "isExtended": false
                    },
                    "creationDate": "2026-08-13T03:10:44.257Z",
                    "sheetId": "HjfJrj"
                }
            }
        ],
        "not_found_msg": null
    },
    "themes": {
        "count": 0,
        "converted_items": [],
        "not_found_msg": "No themes found"
    },
    "extensions": {
        "count": 3,
        "converted_items": [
            {
                "name": "qlik-variable-input",
                "type": "qlik-variable-input",
                "visualization": "qlik-variable-input",
                "used_by": [
                    {
                        "object_id": "hSFqB"
                    },
                    {
                        "object_id": "dgEzRMq"
                    }
                ]
            },
            {
                "name": "qlik-funnel-chart-ext",
                "type": "qlik-funnel-chart-ext",
                "visualization": "qlik-funnel-chart-ext",
                "used_by": [
                    {
                        "object_id": "jbgKqE"
                    }
                ]
            },
            {
                "name": "sn-image",
                "type": "sn-image",
                "visualization": "sn-image",
                "used_by": [
                    {
                        "object_id": "UtkCby"
                    },
                    {
                        "object_id": "BJpSGS"
                    }
                ]
            }
        ],
        "not_found_msg": null
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
        "media_files": [
            {
                "name": "/api/v1/apps/afdeddc7-4dca-470b-bd3d-cdc279a1c408/media/files/images.jpg",
                "url": "/api/v1/apps/afdeddc7-4dca-470b-bd3d-cdc279a1c408/media/files/images.jpg"
            },
            {
                "name": "/api/v1/apps/afdeddc7-4dca-470b-bd3d-cdc279a1c408/media/files/images.png",
                "url": "/api/v1/apps/afdeddc7-4dca-470b-bd3d-cdc279a1c408/media/files/images.png"
            }
        ],
        "content_libraries": [
            {
                "name": "appcontent",
                "app_specific": true
            }
        ]
    },
    "snapshots": [],
    "data_files": [
        {
            "id": "6c0a3afd-2624-4f25-9240-7da08db55b08",
            "name": "cityAliases.qvd",
            "baseName": "cityAliases.qvd",
            "isFolder": false,
            "size": 5138372,
            "createdDate": "2026-08-30T06:45:51.65Z",
            "modifiedDate": "2026-08-30T06:45:51.794Z",
            "ownerId": "6a8d0f4b51a463e48fce8198"
        },
        {
            "id": "de5ee464-9251-45a6-97b7-38c591ef4ac0",
            "name": "cityGeo.qvd",
            "baseName": "cityGeo.qvd",
            "isFolder": false,
            "size": 1700641,
            "createdDate": "2026-08-30T06:45:51.63Z",
            "modifiedDate": "2026-08-30T06:45:51.746Z",
            "ownerId": "6a8d0f4b51a463e48fce8198"
        }
    ],
    "conversion_summary": {
        "total_items": 97,
        "converted": 95,
        "failed": 2,
        "confidence": 0.93,
        "confidence_score": 93,
        "confidence_percentage": "93%",
        "score_out_of_100": 93,
        "requires_review": true,
        "by_section": {
            "tables": {
                "total": 23,
                "converted": 21,
                "failed": 2
            },
            "measures": {
                "total": 34,
                "converted": 34,
                "failed": 0
            },
            "relationships": {
                "total": 40,
                "converted": 40,
                "failed": 0
            }
        },
        "dax_confidence_scores": [
            0.98,
            0.98,
            0.98,
            0.98,
            0.8,
            0.8,
            0.8,
            0.98,
            0.8,
            0.8,
            0.98,
            0.8,
            0.98,
            0.98,
            0.98,
            0.98,
            0.8,
            0.98,
            0.98,
            0.8,
            0.98,
            0.8,
            0.98,
            0.98,
            0.8,
            0.8,
            0.8,
            0.98,
            0.8,
            0.8,
            0.9,
            0.9,
            0.9,
            0.9
        ],
        "dax_count": 34
    },
    "llm_status": {
        "converted": true,
        "model": "groq:openai/gpt-oss-120b",
        "prompt_version": "2.0",
        "reason": "Mapping and conversion completed successfully with full Contract 2.0 formatting."
    },
    "source": "fresh"
}