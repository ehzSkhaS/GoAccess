I must fix this reamdme later, for now only external requirements:
    PostgreSQL 12.9
    
    PostGIS 3.0
    (use this only inside the database you are going to use it)
        -- Enable PostGIS (as of 3.0 contains just geometry/geography)
        CREATE EXTENSION postgis;
        -- enable raster support (for 3+)
        CREATE EXTENSION postgis_raster;
        -- Enable Topology
        CREATE EXTENSION postgis_topology;
        -- Enable PostGIS Advanced 3D
        -- and other geoprocessing algorithms
        -- sfcgal not available with all distributions
        CREATE EXTENSION postgis_sfcgal;
        -- fuzzy matching needed for Tiger
        CREATE EXTENSION fuzzystrmatch;
        -- rule based standardizer
        CREATE EXTENSION address_standardizer;
        -- example rule data set
        CREATE EXTENSION address_standardizer_data_us;
        -- Enable US Tiger Geocoder
        CREATE EXTENSION postgis_tiger_geocoder;

    Python 3.8