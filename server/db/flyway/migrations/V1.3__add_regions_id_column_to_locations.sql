ALTER TABLE locations
ADD COLUMN region_id INTEGER REFERENCES regions(id);

DROP TABLE IF EXISTS locations_regions_mapping;