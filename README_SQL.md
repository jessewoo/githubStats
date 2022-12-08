-- select * from jos_tooldownloadcount

/* INSERT INTO 'jos_tooldownloadcount' (id, tool_name, date_download, ip_address, ip_lat, ip_long, country, region, city, zip, source, coord_updated) VALUES (1, 'test_tool', '2022-12-05', '93.127.206.80', 0.0, 0.0, 'none', 'none', 'none', 'none', 'test_source', 0); */
	
INSERT INTO `jos_tooldownloadcount` (`id`, `tool_name`, `date_download`, `ip_address`, `ip_lat`, `ip_long`, `country`, `region`, `city`, `zip`, `source`, `coord_updated`)
VALUES
	(NULL, 'test_tool_3', '2022-12-04 00:00:00', '154.160.153.87', 0, 0, '0', '0', '0', '0', 'test_source_3', 0);

-- UPDATE `jos_tooldownloadcount` SET `ip_lat` = 100.1, `ip_long` = 200.1 WHERE `ip_address` = '88.232.8.204'

INSERT INTO `jos_tooldownloadcount` (`id`, `tool_name`, `tool_id`, `date_download`, `ip_address`, `ip_lat`, `ip_long`, `country`, `region`, `city`, `zip`, `source`, `coord_updated`)
VALUES
	(NULL, 'test_tool_3', 3, '2022-12-04 00:00:00', '125.94.124.1', 0, 0, '0', '0', '0', '0', 'test_source_3', 0),
	(NULL, 'test_tool_3', 3, '2022-12-03 00:00:00', '140.23.100.245', 0, 0, '0', '0', '0', '0', 'test_source_3', 0),
	(NULL, 'test_tool_3', 3, '2022-12-01 00:00:00', '149.148.193.120', 0, 0, '0', '0', '0', '0', 'test_source_3', 0),
	(NULL, 'test_tool_2', 2, '2022-12-05 00:00:00', '97.203.159.142', 0, 0, '0', '0', '0', '0', 'test_source_2', 0),
	(NULL, 'test_tool', 1, '2022-12-02 00:00:00', '104.233.18.78', 0, 0, '0', '0', '0', '0', 'test_source', 0),
	(NULL, 'test_tool', 1, '2022-12-03 00:00:00', '87.120.113.144', 0, 0, '0', '0', '0', '0', 'test_source', 0),
	(NULL, 'test_tool', 1, '2022-12-01 00:00:00', '109.76.94.90', 0, 0, '0', '0', '0', '0', 'test_source', 0),
	(NULL, 'test_tool', 1, '2022-12-05 00:00:00', '86.191.233.52', 0, 0, '0', '0', '0', '0', 'test_source', 0),
	(NULL, 'test_tool', 1, '2022-12-04 00:00:00', '62.175.199.197', 0, 0, '0', '0', '0', '0', 'test_source', 0),
	(NULL, 'test_tool_2', 2, '2022-12-02 00:00:00', '79.240.98.139', 0, 0, '0', '0', '0', '0', 'test_source_2', 0),
	(NULL, 'test_tool_2', 2, '2022-12-03 00:00:00', '4.167.209.239', 0, 0, '0', '0', '0', '0', 'test_source_2', 0),
	(NULL, 'test_tool_2', 2, '2022-12-05 00:00:00', '153.50.187.62', 0, 0, '0', '0', '0', '0', 'test_source_2', 0),
	(NULL, 'test_tool_3', 3, '2022-12-04 00:00:00', '14.132.116.178', 0, 0, '0', '0', '0', '0', 'test_source_3', 0);