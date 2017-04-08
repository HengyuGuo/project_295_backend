DROP DATABASE project_295;
CREATE DATABASE project_295;
USE project_295;

-- DROP TABLE backend_clusters;
-- DROP TABLE backend_sensors;
-- SELECT * FROM backend_clusters;
-- SELECT * FROM backend_sensors;


CREATE TABLE backend_clusters (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
operation BOOLEAN NOT NULL DEFAULT 1,
health VARCHAR(50) DEFAULT 'unavailable',
message VARCHAR(100) DEFAULT 'pending to be deployed'
);

INSERT INTO backend_clusters (
operation,
health,
message
) VALUES (
1,
'ok',
''
);

INSERT INTO backend_clusters (
operation,
health,
message
) VALUES (
1,
'ok',
''
);

INSERT INTO backend_clusters (
operation,
health,
message
) VALUES (
1,
'ok',
''
);

CREATE TABLE backend_sensors (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
cluster_id_id INT NOT NULL,
FOREIGN KEY (cluster_id_id) REFERENCES backend_clusters(id) ON DELETE RESTRICT,
latitude FLOAT,
longitude FLOAT,
sensor_type VARCHAR(100),
manufacture VARCHAR(100),
operation BOOLEAN NOT NULL DEFAULT 1,
health VARCHAR(50) DEFAULT 'unavailable',
message VARCHAR(100) DEFAULT 'pending to be deployed'
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
1,
'37.773972', 
'-122.431297',
'temperature',
'Capgo',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
1,
'37.789251', 
'-122.469174',
'temperature',
'Omega',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
1,
'37.720766', 
'-122.459906',
'temperature',
'Rtd',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
1,
'37.741034', 
'-122.456816',
'temperature',
'Amphenol',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
1,
'37.732074', 
'-122.435530',
'temperature',
'Murata',
1,
'ok',
''
);





INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
2,
'37.699466', 
'-122.469233',
'pressure',
'ThomasNet',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
2,
'37.695697', 
'-122.462152',
'pressure',
'Mouser',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
2,
'37.693762', 
'-122.461851',
'pressure',
'CST',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
2,
'37.689924', 
'-122.461422',
'pressure',
'PSL',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
2,
'37.688366', 
'-122.424561',
'pressure',
'SSI',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
3,
'37.829216', 
'-122.480059',
'motion',
'InvenSense',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
3,
'37.832878', 
'-122.482811',
'motion',
'MSSedco',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
3,
'37.828988', 
'-122.480639',
'motion',
'mCube',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
3,
'37.829502', 
'-122.484622',
'motion',
'SimpliSafe',
1,
'ok',
''
);

INSERT INTO backend_sensors (
cluster_id_id,
latitude,
longitude,
sensor_type,
manufacture,
operation,
health,
message
) VALUES (
3,
'37.834422', 
'-122.474337',
'motion',
'HKTDC',
1,
'ok',
''
);
