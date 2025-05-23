CREATE TABLE location_region_mapping (
    location_id INT NOT NULL,
    region_id INT NOT NULL,
    PRIMARY KEY (location_id, region_id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);