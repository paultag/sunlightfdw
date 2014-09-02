CREATE EXTENSION mulicorn;

CREATE SERVER ocd FOREIGN DATA WRAPPER multicorn options (
    wrapper 'sunlightfdw.wrappers.ocd.OpenCivicDataFdw'
);

CREATE foreign table ocd_people (
    "name" text,
    "image" text,
    "id" text
) server ocd options (
    host 'http://localhost:8000',
    apikey 'foo'
);

SELECT * FROM ocd_people LIMIT 10;
