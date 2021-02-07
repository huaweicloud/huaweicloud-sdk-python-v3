# coding: utf-8

import pprint
import re

import six





class ChannelDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'http_forwarding': 'HttpForwarding',
        'dis_forwarding': 'DisForwarding',
        'obs_forwarding': 'ObsForwarding',
        'amqp_forwarding': 'AmqpForwarding',
        'dms_kafka_forwarding': 'DmsKafkaForwarding',
        'roma_forwarding': 'RomaForwarding',
        'iota_forwarding': 'IoTAForwarding',
        'mqs_forwarding': 'MqsForwarding',
        'mysql_forwarding': 'MysqlForwarding',
        'mqtt_forwarding': 'MqttForwarding',
        'lts_forwarding': 'LtsForwarding',
        'influxdb_forwarding': 'InfluxDBForwarding',
        'functiongraph_forwarding': 'FunctionGraphForwarding',
        'mrs_kafka_forwarding': 'MrsKafkaForwarding'
    }

    attribute_map = {
        'http_forwarding': 'http_forwarding',
        'dis_forwarding': 'dis_forwarding',
        'obs_forwarding': 'obs_forwarding',
        'amqp_forwarding': 'amqp_forwarding',
        'dms_kafka_forwarding': 'dms_kafka_forwarding',
        'roma_forwarding': 'roma_forwarding',
        'iota_forwarding': 'iota_forwarding',
        'mqs_forwarding': 'mqs_forwarding',
        'mysql_forwarding': 'mysql_forwarding',
        'mqtt_forwarding': 'mqtt_forwarding',
        'lts_forwarding': 'lts_forwarding',
        'influxdb_forwarding': 'influxdb_forwarding',
        'functiongraph_forwarding': 'functiongraph_forwarding',
        'mrs_kafka_forwarding': 'mrs_kafka_forwarding'
    }

    def __init__(self, http_forwarding=None, dis_forwarding=None, obs_forwarding=None, amqp_forwarding=None, dms_kafka_forwarding=None, roma_forwarding=None, iota_forwarding=None, mqs_forwarding=None, mysql_forwarding=None, mqtt_forwarding=None, lts_forwarding=None, influxdb_forwarding=None, functiongraph_forwarding=None, mrs_kafka_forwarding=None):
        """ChannelDetail - a model defined in huaweicloud sdk"""
        
        

        self._http_forwarding = None
        self._dis_forwarding = None
        self._obs_forwarding = None
        self._amqp_forwarding = None
        self._dms_kafka_forwarding = None
        self._roma_forwarding = None
        self._iota_forwarding = None
        self._mqs_forwarding = None
        self._mysql_forwarding = None
        self._mqtt_forwarding = None
        self._lts_forwarding = None
        self._influxdb_forwarding = None
        self._functiongraph_forwarding = None
        self._mrs_kafka_forwarding = None
        self.discriminator = None

        if http_forwarding is not None:
            self.http_forwarding = http_forwarding
        if dis_forwarding is not None:
            self.dis_forwarding = dis_forwarding
        if obs_forwarding is not None:
            self.obs_forwarding = obs_forwarding
        if amqp_forwarding is not None:
            self.amqp_forwarding = amqp_forwarding
        if dms_kafka_forwarding is not None:
            self.dms_kafka_forwarding = dms_kafka_forwarding
        if roma_forwarding is not None:
            self.roma_forwarding = roma_forwarding
        if iota_forwarding is not None:
            self.iota_forwarding = iota_forwarding
        if mqs_forwarding is not None:
            self.mqs_forwarding = mqs_forwarding
        if mysql_forwarding is not None:
            self.mysql_forwarding = mysql_forwarding
        if mqtt_forwarding is not None:
            self.mqtt_forwarding = mqtt_forwarding
        if lts_forwarding is not None:
            self.lts_forwarding = lts_forwarding
        if influxdb_forwarding is not None:
            self.influxdb_forwarding = influxdb_forwarding
        if functiongraph_forwarding is not None:
            self.functiongraph_forwarding = functiongraph_forwarding
        if mrs_kafka_forwarding is not None:
            self.mrs_kafka_forwarding = mrs_kafka_forwarding

    @property
    def http_forwarding(self):
        """Gets the http_forwarding of this ChannelDetail.


        :return: The http_forwarding of this ChannelDetail.
        :rtype: HttpForwarding
        """
        return self._http_forwarding

    @http_forwarding.setter
    def http_forwarding(self, http_forwarding):
        """Sets the http_forwarding of this ChannelDetail.


        :param http_forwarding: The http_forwarding of this ChannelDetail.
        :type: HttpForwarding
        """
        self._http_forwarding = http_forwarding

    @property
    def dis_forwarding(self):
        """Gets the dis_forwarding of this ChannelDetail.


        :return: The dis_forwarding of this ChannelDetail.
        :rtype: DisForwarding
        """
        return self._dis_forwarding

    @dis_forwarding.setter
    def dis_forwarding(self, dis_forwarding):
        """Sets the dis_forwarding of this ChannelDetail.


        :param dis_forwarding: The dis_forwarding of this ChannelDetail.
        :type: DisForwarding
        """
        self._dis_forwarding = dis_forwarding

    @property
    def obs_forwarding(self):
        """Gets the obs_forwarding of this ChannelDetail.


        :return: The obs_forwarding of this ChannelDetail.
        :rtype: ObsForwarding
        """
        return self._obs_forwarding

    @obs_forwarding.setter
    def obs_forwarding(self, obs_forwarding):
        """Sets the obs_forwarding of this ChannelDetail.


        :param obs_forwarding: The obs_forwarding of this ChannelDetail.
        :type: ObsForwarding
        """
        self._obs_forwarding = obs_forwarding

    @property
    def amqp_forwarding(self):
        """Gets the amqp_forwarding of this ChannelDetail.


        :return: The amqp_forwarding of this ChannelDetail.
        :rtype: AmqpForwarding
        """
        return self._amqp_forwarding

    @amqp_forwarding.setter
    def amqp_forwarding(self, amqp_forwarding):
        """Sets the amqp_forwarding of this ChannelDetail.


        :param amqp_forwarding: The amqp_forwarding of this ChannelDetail.
        :type: AmqpForwarding
        """
        self._amqp_forwarding = amqp_forwarding

    @property
    def dms_kafka_forwarding(self):
        """Gets the dms_kafka_forwarding of this ChannelDetail.


        :return: The dms_kafka_forwarding of this ChannelDetail.
        :rtype: DmsKafkaForwarding
        """
        return self._dms_kafka_forwarding

    @dms_kafka_forwarding.setter
    def dms_kafka_forwarding(self, dms_kafka_forwarding):
        """Sets the dms_kafka_forwarding of this ChannelDetail.


        :param dms_kafka_forwarding: The dms_kafka_forwarding of this ChannelDetail.
        :type: DmsKafkaForwarding
        """
        self._dms_kafka_forwarding = dms_kafka_forwarding

    @property
    def roma_forwarding(self):
        """Gets the roma_forwarding of this ChannelDetail.


        :return: The roma_forwarding of this ChannelDetail.
        :rtype: RomaForwarding
        """
        return self._roma_forwarding

    @roma_forwarding.setter
    def roma_forwarding(self, roma_forwarding):
        """Sets the roma_forwarding of this ChannelDetail.


        :param roma_forwarding: The roma_forwarding of this ChannelDetail.
        :type: RomaForwarding
        """
        self._roma_forwarding = roma_forwarding

    @property
    def iota_forwarding(self):
        """Gets the iota_forwarding of this ChannelDetail.


        :return: The iota_forwarding of this ChannelDetail.
        :rtype: IoTAForwarding
        """
        return self._iota_forwarding

    @iota_forwarding.setter
    def iota_forwarding(self, iota_forwarding):
        """Sets the iota_forwarding of this ChannelDetail.


        :param iota_forwarding: The iota_forwarding of this ChannelDetail.
        :type: IoTAForwarding
        """
        self._iota_forwarding = iota_forwarding

    @property
    def mqs_forwarding(self):
        """Gets the mqs_forwarding of this ChannelDetail.


        :return: The mqs_forwarding of this ChannelDetail.
        :rtype: MqsForwarding
        """
        return self._mqs_forwarding

    @mqs_forwarding.setter
    def mqs_forwarding(self, mqs_forwarding):
        """Sets the mqs_forwarding of this ChannelDetail.


        :param mqs_forwarding: The mqs_forwarding of this ChannelDetail.
        :type: MqsForwarding
        """
        self._mqs_forwarding = mqs_forwarding

    @property
    def mysql_forwarding(self):
        """Gets the mysql_forwarding of this ChannelDetail.


        :return: The mysql_forwarding of this ChannelDetail.
        :rtype: MysqlForwarding
        """
        return self._mysql_forwarding

    @mysql_forwarding.setter
    def mysql_forwarding(self, mysql_forwarding):
        """Sets the mysql_forwarding of this ChannelDetail.


        :param mysql_forwarding: The mysql_forwarding of this ChannelDetail.
        :type: MysqlForwarding
        """
        self._mysql_forwarding = mysql_forwarding

    @property
    def mqtt_forwarding(self):
        """Gets the mqtt_forwarding of this ChannelDetail.


        :return: The mqtt_forwarding of this ChannelDetail.
        :rtype: MqttForwarding
        """
        return self._mqtt_forwarding

    @mqtt_forwarding.setter
    def mqtt_forwarding(self, mqtt_forwarding):
        """Sets the mqtt_forwarding of this ChannelDetail.


        :param mqtt_forwarding: The mqtt_forwarding of this ChannelDetail.
        :type: MqttForwarding
        """
        self._mqtt_forwarding = mqtt_forwarding

    @property
    def lts_forwarding(self):
        """Gets the lts_forwarding of this ChannelDetail.


        :return: The lts_forwarding of this ChannelDetail.
        :rtype: LtsForwarding
        """
        return self._lts_forwarding

    @lts_forwarding.setter
    def lts_forwarding(self, lts_forwarding):
        """Sets the lts_forwarding of this ChannelDetail.


        :param lts_forwarding: The lts_forwarding of this ChannelDetail.
        :type: LtsForwarding
        """
        self._lts_forwarding = lts_forwarding

    @property
    def influxdb_forwarding(self):
        """Gets the influxdb_forwarding of this ChannelDetail.


        :return: The influxdb_forwarding of this ChannelDetail.
        :rtype: InfluxDBForwarding
        """
        return self._influxdb_forwarding

    @influxdb_forwarding.setter
    def influxdb_forwarding(self, influxdb_forwarding):
        """Sets the influxdb_forwarding of this ChannelDetail.


        :param influxdb_forwarding: The influxdb_forwarding of this ChannelDetail.
        :type: InfluxDBForwarding
        """
        self._influxdb_forwarding = influxdb_forwarding

    @property
    def functiongraph_forwarding(self):
        """Gets the functiongraph_forwarding of this ChannelDetail.


        :return: The functiongraph_forwarding of this ChannelDetail.
        :rtype: FunctionGraphForwarding
        """
        return self._functiongraph_forwarding

    @functiongraph_forwarding.setter
    def functiongraph_forwarding(self, functiongraph_forwarding):
        """Sets the functiongraph_forwarding of this ChannelDetail.


        :param functiongraph_forwarding: The functiongraph_forwarding of this ChannelDetail.
        :type: FunctionGraphForwarding
        """
        self._functiongraph_forwarding = functiongraph_forwarding

    @property
    def mrs_kafka_forwarding(self):
        """Gets the mrs_kafka_forwarding of this ChannelDetail.


        :return: The mrs_kafka_forwarding of this ChannelDetail.
        :rtype: MrsKafkaForwarding
        """
        return self._mrs_kafka_forwarding

    @mrs_kafka_forwarding.setter
    def mrs_kafka_forwarding(self, mrs_kafka_forwarding):
        """Sets the mrs_kafka_forwarding of this ChannelDetail.


        :param mrs_kafka_forwarding: The mrs_kafka_forwarding of this ChannelDetail.
        :type: MrsKafkaForwarding
        """
        self._mrs_kafka_forwarding = mrs_kafka_forwarding

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChannelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
