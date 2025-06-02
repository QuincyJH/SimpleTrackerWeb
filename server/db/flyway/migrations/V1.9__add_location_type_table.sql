CREATE TABLE location_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    display_name VARCHAR(255) NOT NULL
);

INSERT INTO location_type (name, display_name) VALUES ('rocks', 'Rocks');
INSERT INTO location_type (name, display_name) VALUES ('jars', 'Jars');
INSERT INTO location_type (name, display_name) VALUES ('starting_items', 'Starting Items');
INSERT INTO location_type (name, display_name) VALUES ('fairies', 'Fairies');
INSERT INTO location_type (name, display_name) VALUES ('fake', 'Fake');
INSERT INTO location_type (name, display_name) VALUES ('beehives', 'Beehives');
INSERT INTO location_type (name, display_name) VALUES ('crates', 'Crates');
INSERT INTO location_type (name, display_name) VALUES ('npc_rewards', 'NPC Rewards');
INSERT INTO location_type (name, display_name) VALUES ('freestanding', 'Freestanding Items');
INSERT INTO location_type (name, display_name) VALUES ('moon_items', 'Moon Items');
INSERT INTO location_type (name, display_name) VALUES ('glitches_required', 'Glitches Required');
INSERT INTO location_type (name, display_name) VALUES ('frogs', 'Frogs');
INSERT INTO location_type (name, display_name) VALUES ('hit_spots', 'Hit Spots');
INSERT INTO location_type (name, display_name) VALUES ('scoops', 'Scoops');
INSERT INTO location_type (name, display_name) VALUES ('barrels', 'Barrels');
INSERT INTO location_type (name, display_name) VALUES ('boss_fights', 'Boss Fights');
INSERT INTO location_type (name, display_name) VALUES ('grass', 'Grass');
INSERT INTO location_type (name, display_name) VALUES ('notebook_entries', 'Notebook Entries');
INSERT INTO location_type (name, display_name) VALUES ('enemy_spawn', 'Enemy Spawns');
INSERT INTO location_type (name, display_name) VALUES ('butterflies', 'Butterflies');
INSERT INTO location_type (name, display_name) VALUES ('small_snowballs', 'Small Snowballs');
INSERT INTO location_type (name, display_name) VALUES ('minigames', 'Minigames');
INSERT INTO location_type (name, display_name) VALUES ('chests', 'Chests');
INSERT INTO location_type (name, display_name) VALUES ('events', 'Events');
INSERT INTO location_type (name, display_name) VALUES ('large_snowballs', 'Large Snowballs');
INSERT INTO location_type (name, display_name) VALUES ('purchases', 'Purchases');
INSERT INTO location_type (name, display_name) VALUES ('invisible_items', 'Invisible Items');
INSERT INTO location_type (name, display_name) VALUES ('soft_soil', 'Soft Soil');

ALTER TABLE locations
ADD COLUMN location_type_id INTEGER REFERENCES location_type(id);

UPDATE locations
SET location_type_id = location_type_table.id
FROM location_type AS location_type_table
WHERE locations.location_type = location_type_table.name;

ALTER TABLE locations DROP COLUMN location_type;

ALTER TABLE locations
ADD CONSTRAINT fk_location_type
FOREIGN KEY (location_type_id)
REFERENCES location_type(id);
