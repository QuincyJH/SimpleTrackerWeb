UPDATE items
SET item_type_id = item_type_table.id
FROM item_type AS item_type_table
WHERE items.item_type = item_type_table.name;

ALTER TABLE items DROP COLUMN item_type;

ALTER TABLE items
ADD CONSTRAINT fk_item_type
FOREIGN KEY (item_type_id)
REFERENCES item_type(id);