-- select * from jos_tooldownloadcount

/* INSERT INTO 'jos_tooldownloadcount' (id, tool_name, date_download, ip_address, ip_lat, ip_long, country, region, city, zip, source, coord_updated) VALUES (1, 'test_tool', '2022-12-05', '93.127.206.80', 0.0, 0.0, 'none', 'none', 'none', 'none', 'test_source', 0); */
	
INSERT INTO `jos_tooldownloadcount` (`id`, `tool_name`, `date_download`, `ip_address`, `ip_lat`, `ip_long`, `country`, `region`, `city`, `zip`, `source`, `coord_updated`)
VALUES
	(NULL, 'test_tool_3', '2022-12-04 00:00:00', '154.160.153.87', 0, 0, '0', '0', '0', '0', 'test_source_3', 0);

-- UPDATE `jos_tooldownloadcount` SET `ip_lat` = 100.1, `ip_long` = 200.1 WHERE `ip_address` = '88.232.8.204'