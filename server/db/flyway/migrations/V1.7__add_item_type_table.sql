CREATE TABLE item_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    display_name VARCHAR(255) NOT NULL
);

INSERT INTO item_type (name, display_name) VALUES ('green_rupees', 'Green Rupees');
INSERT INTO item_type (name, display_name) VALUES ('blue_rupees', 'Blue Rupees');
INSERT INTO item_type (name, display_name) VALUES ('red_rupees', 'Red Rupees');
INSERT INTO item_type (name, display_name) VALUES ('purple_rupees', 'Purple Rupees');
INSERT INTO item_type (name, display_name) VALUES ('silver_rupees', 'Silver Rupees');
INSERT INTO item_type (name, display_name) VALUES ('gold_rupees', 'Gold Rupees');
INSERT INTO item_type (name, display_name) VALUES ('royal_wallet', 'Royal Wallet');
INSERT INTO item_type (name, display_name) VALUES ('navigation', 'Navigation');
INSERT INTO item_type (name, display_name) VALUES ('magic_powers', 'Magic Powers');
INSERT INTO item_type (name, display_name) VALUES ('magic_jars', 'Magic Jars');
INSERT INTO item_type (name, display_name) VALUES ('green_potions', 'Green Potions');
INSERT INTO item_type (name, display_name) VALUES ('blue_potions', 'Blue Potions');
INSERT INTO item_type (name, display_name) VALUES ('red_potions', 'Red Potions');
INSERT INTO item_type (name, display_name) VALUES ('stray_fairies', 'Stray Fairies');
INSERT INTO item_type (name, display_name) VALUES ('fairy', 'Fairy');
INSERT INTO item_type (name, display_name) VALUES ('time_travel', 'Time Travel');
INSERT INTO item_type (name, display_name) VALUES ('masks', 'Masks');
INSERT INTO item_type (name, display_name) VALUES ('deku_sticks', 'Deku Sticks');
INSERT INTO item_type (name, display_name) VALUES ('deku_nuts', 'Deku Nuts');
INSERT INTO item_type (name, display_name) VALUES ('milk', 'Milk');
INSERT INTO item_type (name, display_name) VALUES ('songs', 'Songs');
INSERT INTO item_type (name, display_name) VALUES ('fake', 'Fake');
INSERT INTO item_type (name, display_name) VALUES ('chateau', 'Chateau');
INSERT INTO item_type (name, display_name) VALUES ('scooped_items', 'Scooped Items');
INSERT INTO item_type (name, display_name) VALUES ('boss_remains', 'Boss Remains');
INSERT INTO item_type (name, display_name) VALUES ('trade_items', 'Trade Items');
INSERT INTO item_type (name, display_name) VALUES ('frogs', 'Frogs');
INSERT INTO item_type (name, display_name) VALUES ('arrows', 'Arrows');
INSERT INTO item_type (name, display_name) VALUES ('bombchu', 'Bombchu');
INSERT INTO item_type (name, display_name) VALUES ('notebook_entries', 'Notebook Entries');
INSERT INTO item_type (name, display_name) VALUES ('dungeon_keys', 'Dungeon Keys');
INSERT INTO item_type (name, display_name) VALUES ('bombs', 'Bombs');
INSERT INTO item_type (name, display_name) VALUES ('seahorse', 'Seahorse');
INSERT INTO item_type (name, display_name) VALUES ('recovery_hearts', 'Recovery Hearts');
INSERT INTO item_type (name, display_name) VALUES ('skulltula_tokens', 'Skulltula Tokens');
INSERT INTO item_type (name, display_name) VALUES ('shields', 'Shields');
INSERT INTO item_type (name, display_name) VALUES ('heart_containers', 'Heart Containers');
INSERT INTO item_type (name, display_name) VALUES ('main_inventory', 'Main Inventory');
INSERT INTO item_type (name, display_name) VALUES ('pieces_of_heart', 'Pieces of Heart');

ALTER TABLE items
ADD COLUMN item_type_id INTEGER REFERENCES item_type(id);

