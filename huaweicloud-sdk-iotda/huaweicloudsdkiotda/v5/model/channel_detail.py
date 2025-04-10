# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'mysql_forwarding': 'MysqlForwarding',
        'influxdb_forwarding': 'InfluxDBForwarding',
        'functiongraph_forwarding': 'FunctionGraphForwarding',
        'mrs_kafka_forwarding': 'MrsKafkaForwarding',
        'dms_rocketmq_forwarding': 'DmsRocketMQForwarding'
    }

    attribute_map = {
        'http_forwarding': 'http_forwarding',
        'dis_forwarding': 'dis_forwarding',
        'obs_forwarding': 'obs_forwarding',
        'amqp_forwarding': 'amqp_forwarding',
        'dms_kafka_forwarding': 'dms_kafka_forwarding',
        'roma_forwarding': 'roma_forwarding',
        'mysql_forwarding': 'mysql_forwarding',
        'influxdb_forwarding': 'influxdb_forwarding',
        'functiongraph_forwarding': 'functiongraph_forwarding',
        'mrs_kafka_forwarding': 'mrs_kafka_forwarding',
        'dms_rocketmq_forwarding': 'dms_rocketmq_forwarding'
    }

    def __init__(self, http_forwarding=None, dis_forwarding=None, obs_forwarding=None, amqp_forwarding=None, dms_kafka_forwarding=None, roma_forwarding=None, mysql_forwarding=None, influxdb_forwarding=None, functiongraph_forwarding=None, mrs_kafka_forwarding=None, dms_rocketmq_forwarding=None):
        r"""ChannelDetail

        The model defined in huaweicloud sdk

        :param http_forwarding: 
        :type http_forwarding: :class:`huaweicloudsdkiotda.v5.HttpForwarding`
        :param dis_forwarding: 
        :type dis_forwarding: :class:`huaweicloudsdkiotda.v5.DisForwarding`
        :param obs_forwarding: 
        :type obs_forwarding: :class:`huaweicloudsdkiotda.v5.ObsForwarding`
        :param amqp_forwarding: 
        :type amqp_forwarding: :class:`huaweicloudsdkiotda.v5.AmqpForwarding`
        :param dms_kafka_forwarding: 
        :type dms_kafka_forwarding: :class:`huaweicloudsdkiotda.v5.DmsKafkaForwarding`
        :param roma_forwarding: 
        :type roma_forwarding: :class:`huaweicloudsdkiotda.v5.RomaForwarding`
        :param mysql_forwarding: 
        :type mysql_forwarding: :class:`huaweicloudsdkiotda.v5.MysqlForwarding`
        :param influxdb_forwarding: 
        :type influxdb_forwarding: :class:`huaweicloudsdkiotda.v5.InfluxDBForwarding`
        :param functiongraph_forwarding: 
        :type functiongraph_forwarding: :class:`huaweicloudsdkiotda.v5.FunctionGraphForwarding`
        :param mrs_kafka_forwarding: 
        :type mrs_kafka_forwarding: :class:`huaweicloudsdkiotda.v5.MrsKafkaForwarding`
        :param dms_rocketmq_forwarding: 
        :type dms_rocketmq_forwarding: :class:`huaweicloudsdkiotda.v5.DmsRocketMQForwarding`
        """
        
        

        self._http_forwarding = None
        self._dis_forwarding = None
        self._obs_forwarding = None
        self._amqp_forwarding = None
        self._dms_kafka_forwarding = None
        self._roma_forwarding = None
        self._mysql_forwarding = None
        self._influxdb_forwarding = None
        self._functiongraph_forwarding = None
        self._mrs_kafka_forwarding = None
        self._dms_rocketmq_forwarding = None
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
        if mysql_forwarding is not None:
            self.mysql_forwarding = mysql_forwarding
        if influxdb_forwarding is not None:
            self.influxdb_forwarding = influxdb_forwarding
        if functiongraph_forwarding is not None:
            self.functiongraph_forwarding = functiongraph_forwarding
        if mrs_kafka_forwarding is not None:
            self.mrs_kafka_forwarding = mrs_kafka_forwarding
        if dms_rocketmq_forwarding is not None:
            self.dms_rocketmq_forwarding = dms_rocketmq_forwarding

    @property
    def http_forwarding(self):
        r"""Gets the http_forwarding of this ChannelDetail.

        :return: The http_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.HttpForwarding`
        """
        return self._http_forwarding

    @http_forwarding.setter
    def http_forwarding(self, http_forwarding):
        r"""Sets the http_forwarding of this ChannelDetail.

        :param http_forwarding: The http_forwarding of this ChannelDetail.
        :type http_forwarding: :class:`huaweicloudsdkiotda.v5.HttpForwarding`
        """
        self._http_forwarding = http_forwarding

    @property
    def dis_forwarding(self):
        r"""Gets the dis_forwarding of this ChannelDetail.

        :return: The dis_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.DisForwarding`
        """
        return self._dis_forwarding

    @dis_forwarding.setter
    def dis_forwarding(self, dis_forwarding):
        r"""Sets the dis_forwarding of this ChannelDetail.

        :param dis_forwarding: The dis_forwarding of this ChannelDetail.
        :type dis_forwarding: :class:`huaweicloudsdkiotda.v5.DisForwarding`
        """
        self._dis_forwarding = dis_forwarding

    @property
    def obs_forwarding(self):
        r"""Gets the obs_forwarding of this ChannelDetail.

        :return: The obs_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.ObsForwarding`
        """
        return self._obs_forwarding

    @obs_forwarding.setter
    def obs_forwarding(self, obs_forwarding):
        r"""Sets the obs_forwarding of this ChannelDetail.

        :param obs_forwarding: The obs_forwarding of this ChannelDetail.
        :type obs_forwarding: :class:`huaweicloudsdkiotda.v5.ObsForwarding`
        """
        self._obs_forwarding = obs_forwarding

    @property
    def amqp_forwarding(self):
        r"""Gets the amqp_forwarding of this ChannelDetail.

        :return: The amqp_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.AmqpForwarding`
        """
        return self._amqp_forwarding

    @amqp_forwarding.setter
    def amqp_forwarding(self, amqp_forwarding):
        r"""Sets the amqp_forwarding of this ChannelDetail.

        :param amqp_forwarding: The amqp_forwarding of this ChannelDetail.
        :type amqp_forwarding: :class:`huaweicloudsdkiotda.v5.AmqpForwarding`
        """
        self._amqp_forwarding = amqp_forwarding

    @property
    def dms_kafka_forwarding(self):
        r"""Gets the dms_kafka_forwarding of this ChannelDetail.

        :return: The dms_kafka_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.DmsKafkaForwarding`
        """
        return self._dms_kafka_forwarding

    @dms_kafka_forwarding.setter
    def dms_kafka_forwarding(self, dms_kafka_forwarding):
        r"""Sets the dms_kafka_forwarding of this ChannelDetail.

        :param dms_kafka_forwarding: The dms_kafka_forwarding of this ChannelDetail.
        :type dms_kafka_forwarding: :class:`huaweicloudsdkiotda.v5.DmsKafkaForwarding`
        """
        self._dms_kafka_forwarding = dms_kafka_forwarding

    @property
    def roma_forwarding(self):
        r"""Gets the roma_forwarding of this ChannelDetail.

        :return: The roma_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.RomaForwarding`
        """
        return self._roma_forwarding

    @roma_forwarding.setter
    def roma_forwarding(self, roma_forwarding):
        r"""Sets the roma_forwarding of this ChannelDetail.

        :param roma_forwarding: The roma_forwarding of this ChannelDetail.
        :type roma_forwarding: :class:`huaweicloudsdkiotda.v5.RomaForwarding`
        """
        self._roma_forwarding = roma_forwarding

    @property
    def mysql_forwarding(self):
        r"""Gets the mysql_forwarding of this ChannelDetail.

        :return: The mysql_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.MysqlForwarding`
        """
        return self._mysql_forwarding

    @mysql_forwarding.setter
    def mysql_forwarding(self, mysql_forwarding):
        r"""Sets the mysql_forwarding of this ChannelDetail.

        :param mysql_forwarding: The mysql_forwarding of this ChannelDetail.
        :type mysql_forwarding: :class:`huaweicloudsdkiotda.v5.MysqlForwarding`
        """
        self._mysql_forwarding = mysql_forwarding

    @property
    def influxdb_forwarding(self):
        r"""Gets the influxdb_forwarding of this ChannelDetail.

        :return: The influxdb_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.InfluxDBForwarding`
        """
        return self._influxdb_forwarding

    @influxdb_forwarding.setter
    def influxdb_forwarding(self, influxdb_forwarding):
        r"""Sets the influxdb_forwarding of this ChannelDetail.

        :param influxdb_forwarding: The influxdb_forwarding of this ChannelDetail.
        :type influxdb_forwarding: :class:`huaweicloudsdkiotda.v5.InfluxDBForwarding`
        """
        self._influxdb_forwarding = influxdb_forwarding

    @property
    def functiongraph_forwarding(self):
        r"""Gets the functiongraph_forwarding of this ChannelDetail.

        :return: The functiongraph_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.FunctionGraphForwarding`
        """
        return self._functiongraph_forwarding

    @functiongraph_forwarding.setter
    def functiongraph_forwarding(self, functiongraph_forwarding):
        r"""Sets the functiongraph_forwarding of this ChannelDetail.

        :param functiongraph_forwarding: The functiongraph_forwarding of this ChannelDetail.
        :type functiongraph_forwarding: :class:`huaweicloudsdkiotda.v5.FunctionGraphForwarding`
        """
        self._functiongraph_forwarding = functiongraph_forwarding

    @property
    def mrs_kafka_forwarding(self):
        r"""Gets the mrs_kafka_forwarding of this ChannelDetail.

        :return: The mrs_kafka_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.MrsKafkaForwarding`
        """
        return self._mrs_kafka_forwarding

    @mrs_kafka_forwarding.setter
    def mrs_kafka_forwarding(self, mrs_kafka_forwarding):
        r"""Sets the mrs_kafka_forwarding of this ChannelDetail.

        :param mrs_kafka_forwarding: The mrs_kafka_forwarding of this ChannelDetail.
        :type mrs_kafka_forwarding: :class:`huaweicloudsdkiotda.v5.MrsKafkaForwarding`
        """
        self._mrs_kafka_forwarding = mrs_kafka_forwarding

    @property
    def dms_rocketmq_forwarding(self):
        r"""Gets the dms_rocketmq_forwarding of this ChannelDetail.

        :return: The dms_rocketmq_forwarding of this ChannelDetail.
        :rtype: :class:`huaweicloudsdkiotda.v5.DmsRocketMQForwarding`
        """
        return self._dms_rocketmq_forwarding

    @dms_rocketmq_forwarding.setter
    def dms_rocketmq_forwarding(self, dms_rocketmq_forwarding):
        r"""Sets the dms_rocketmq_forwarding of this ChannelDetail.

        :param dms_rocketmq_forwarding: The dms_rocketmq_forwarding of this ChannelDetail.
        :type dms_rocketmq_forwarding: :class:`huaweicloudsdkiotda.v5.DmsRocketMQForwarding`
        """
        self._dms_rocketmq_forwarding = dms_rocketmq_forwarding

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChannelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
