CREATE TABLE IF NOT EXISTS public.airlines_details
(
    id bigint,
    code bigint,
    day text COLLATE pg_catalog."default",
    airline text COLLATE pg_catalog."default",
    destination text COLLATE pg_catalog."default",
    dest_region text COLLATE pg_catalog."default",
    dest_size text COLLATE pg_catalog."default",
    boarding_area text COLLATE pg_catalog."default",
    dept_time text COLLATE pg_catalog."default",
    wait_min double precision,
    cleanliness text COLLATE pg_catalog."default",
    safety text COLLATE pg_catalog."default",
    satisfaction text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.airlines_details
    OWNER to postgres;