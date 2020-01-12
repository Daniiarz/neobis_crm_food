psql -U postgres -c "CREATE USER daniiar PASSWORD 'SSpass123'"

psql -U postgres -c "ALTER ROLE daniiar SET client_encoding TO 'utf8'";
psql -U postgres -c "ALTER ROLE daniiar SET default_transaction_isolation TO 'read committed'";
psql -U postgres -c "ALTER ROLE daniiar SET timezone TO 'Asia/Bishkek'";

psql -U postgres -c "CREATE DATABASE crmfood_db OWNER daniiar"