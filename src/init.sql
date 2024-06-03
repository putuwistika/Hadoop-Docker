CREATE TABLE pokemon_effect(
   id SERIAL PRIMARY KEY,
   pokemon_ability_id INTEGER,
   effect VARCHAR,
   language VARCHAR,
   short_effect VARCHAR
);
