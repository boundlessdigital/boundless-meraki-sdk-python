class Sensor(object):
    def __init__(self, session):
        super(Sensor, self).__init__()
        self._session = session
        


    def getDeviceSensorRelationships(self, serial: str):
        """
        **List the sensor roles for a given device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-relationships

        - serial (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'getDeviceSensorRelationships'
        }
        resource = f'/devices/{serial}/sensor/relationships'

        return self._session.get(metadata, resource)
        


    def updateDeviceSensorRelationships(self, serial: str, **kwargs):
        """
        **Assign one or more sensor roles to a given device.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

        - serial (string): (required)
        - livestream (object): The camera assigned to a given sensor. Also supports the inverse when scoped to a given camera.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'updateDeviceSensorRelationships'
        }
        resource = f'/devices/{serial}/sensor/relationships'

        body_params = ['livestream', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSensorAlertsProfiles(self, networkId: str):
        """
        **Lists all sensor alert profiles for a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profiles

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'getNetworkSensorAlertsProfiles'
        }
        resource = f'/networks/{networkId}/sensor/alerts/profiles'

        return self._session.get(metadata, resource)
        


    def createNetworkSensorAlertsProfile(self, networkId: str, **kwargs):
        """
        **Creates a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

        - networkId (string): (required)
        - name (string): Name of the sensor alert profiles.
        - scheduleId (string): Id of the schedule to attach to the alert profile.
        - conditions (array): List of alert conditions.
        - recipients (object): List of recipients that will recieve the alert.
        - serials (array): List of device serials assigned to this sensor alert profile.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'createNetworkSensorAlertsProfile'
        }
        resource = f'/networks/{networkId}/sensor/alerts/profiles'

        body_params = ['name', 'scheduleId', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSensorAlertsProfile(self, networkId: str, id: str):
        """
        **Show details of a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'getNetworkSensorAlertsProfile'
        }
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSensorAlertsProfile(self, networkId: str, id: str, **kwargs):
        """
        **Updates a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        - name (string): Name of the sensor alert profiles.
        - scheduleId (string): Id of the schedule to attach to the alert profile.
        - conditions (array): List of alert conditions.
        - recipients (object): List of alert conditions.
        - serials (array): List of device serials assigned to this sensor alert profile.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'updateNetworkSensorAlertsProfile'
        }
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        body_params = ['name', 'scheduleId', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSensorAlertsProfile(self, networkId: str, id: str):
        """
        **Deletes a sensor alert profile from a network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'deleteNetworkSensorAlertsProfile'
        }
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSensorRelationships(self, networkId: str):
        """
        **List the sensor roles for devices in a given network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-relationships

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'getNetworkSensorRelationships'
        }
        resource = f'/networks/{networkId}/sensor/relationships'

        return self._session.get(metadata, resource)
        


    def getNetworkSensorSchedules(self, networkId: str):
        """
        **Returns a list of all sensor schedules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-schedules

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'schedules'],
            'operation': 'getNetworkSensorSchedules'
        }
        resource = f'/networks/{networkId}/sensor/schedules'

        return self._session.get(metadata, resource)
        


    def getNetworkSensorStatsAggregateBySensor(self, networkId: str, metric: str, **kwargs):
        """
        **Provides aggregated data about a set of sensors.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-stats-aggregate-by-sensor

        - networkId (string): (required)
        - metric (string): Type of metric we want the data for. This depends on the type of sensors you are requesting data, for example, "temperature" would be used for gathering temperature readings.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 730 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 730 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 730 days. The default is 2 hours.
        - serials (array): List of sensor serials for which we are generating statistics for.
        - agg (string): The aggregation algorithm to apply to the data. By default we will aggregate all of the readings in the resolution bucket using average but maximum and minimum values are also supported.
        """

        kwargs.update(locals())

        if 'agg' in kwargs:
            options = ['avg', 'max', 'min']
            assert kwargs['agg'] in options, f'''"agg" cannot be "{kwargs['agg']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['sensor', 'monitor', 'stats', 'aggregateBySensor'],
            'operation': 'getNetworkSensorStatsAggregateBySensor'
        }
        resource = f'/networks/{networkId}/sensor/stats/aggregateBySensor'

        query_params = ['t0', 't1', 'timespan', 'serials', 'metric', 'agg', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getNetworkSensorStatsHistoricalBySensor(self, networkId: str, metric: str, **kwargs):
        """
        **Return time series sensor statistics for a list of sensors**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-stats-historical-by-sensor

        - networkId (string): (required)
        - metric (string): Type of metric we want the data for. This depends on the type of sensors you are requesting data, for example, "temperature" would be used for gathering temperature readings.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 730 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 730 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 730 days. The default is 2 hours.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 1, 120, 3600, 14400, 86400. The default is 120.
        - serials (array): List of sensor serials for which we are generating statistics for.
        - agg (string): The aggregation algorithm to apply to the data. By default we will aggregate all of the readings in the resolution bucket using average but maximum and minimum values are also supported. Supported values are "avg", "max", "min"
        """

        kwargs.update(locals())

        if 'agg' in kwargs:
            options = ['avg', 'max', 'min']
            assert kwargs['agg'] in options, f'''"agg" cannot be "{kwargs['agg']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['sensor', 'monitor', 'stats', 'historicalBySensor'],
            'operation': 'getNetworkSensorStatsHistoricalBySensor'
        }
        resource = f'/networks/{networkId}/sensor/stats/historicalBySensor'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'serials', 'metric', 'agg', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getNetworkSensorStatsLatestBySensor(self, networkId: str, metric: str, **kwargs):
        """
        **Provides the latest reading for a set of sensors.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-stats-latest-by-sensor

        - networkId (string): (required)
        - metric (string): Type of metric we want the data for. This depends on the type of sensors you are requesting data, for example, "temperature" would be used for gathering temperature readings.
        - serials (array): List of sensor serials for which we are generating statistics for.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'stats', 'latestBySensor'],
            'operation': 'getNetworkSensorStatsLatestBySensor'
        }
        resource = f'/networks/{networkId}/sensor/stats/latestBySensor'

        query_params = ['serials', 'metric', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSensorReadingsHistory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return all reported readings from sensors in a given timespan, sorted by timestamp**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are temperature, humidity, water, and door.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'history'],
            'operation': 'getOrganizationSensorReadingsHistory'
        }
        resource = f'/organizations/{organizationId}/sensor/readings/history'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationSensorReadingsHistoryByInterval(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return all reported readings from sensors in a given timespan, summarized as a series of intervals, sorted by interval start time in descending order**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history-by-interval

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 86400. The default is 86400.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are temperature, humidity, water, and door.
        - models (array): Optional parameter to filter readings by one or more models. Allowed values are MT10, MT11, MT12, and MT20.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'history', 'byInterval'],
            'operation': 'getOrganizationSensorReadingsHistoryByInterval'
        }
        resource = f'/organizations/{organizationId}/sensor/readings/history/byInterval'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval', 'networkIds', 'serials', 'metrics', 'models', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', 'models', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationSensorReadingsLatest(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the latest available reading for each metric from each sensor, sorted by sensor serial**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are temperature, humidity, water, and door.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'latest'],
            'operation': 'getOrganizationSensorReadingsLatest'
        }
        resource = f'/organizations/{organizationId}/sensor/readings/latest'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
