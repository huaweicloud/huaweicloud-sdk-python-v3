# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcepInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kafka_broker_ip': 'str',
        'vpcep_service_id': 'str',
        'vpcep_service_name': 'str',
        'vpcep_client_port': 'int'
    }

    attribute_map = {
        'kafka_broker_ip': 'kafka_broker_ip',
        'vpcep_service_id': 'vpcep_service_id',
        'vpcep_service_name': 'vpcep_service_name',
        'vpcep_client_port': 'vpcep_client_port'
    }

    def __init__(self, kafka_broker_ip=None, vpcep_service_id=None, vpcep_service_name=None, vpcep_client_port=None):
        """VpcepInfo

        The model defined in huaweicloud sdk

        :param kafka_broker_ip: Kafka的Broker ip
        :type kafka_broker_ip: str
        :param vpcep_service_id: Kafka的VPCEP的service id
        :type vpcep_service_id: str
        :param vpcep_service_name: Kafka的VPCEP的service name
        :type vpcep_service_name: str
        :param vpcep_client_port: Kafka的VPCEP的client port
        :type vpcep_client_port: int
        """
        
        

        self._kafka_broker_ip = None
        self._vpcep_service_id = None
        self._vpcep_service_name = None
        self._vpcep_client_port = None
        self.discriminator = None

        self.kafka_broker_ip = kafka_broker_ip
        self.vpcep_service_id = vpcep_service_id
        self.vpcep_service_name = vpcep_service_name
        self.vpcep_client_port = vpcep_client_port

    @property
    def kafka_broker_ip(self):
        """Gets the kafka_broker_ip of this VpcepInfo.

        Kafka的Broker ip

        :return: The kafka_broker_ip of this VpcepInfo.
        :rtype: str
        """
        return self._kafka_broker_ip

    @kafka_broker_ip.setter
    def kafka_broker_ip(self, kafka_broker_ip):
        """Sets the kafka_broker_ip of this VpcepInfo.

        Kafka的Broker ip

        :param kafka_broker_ip: The kafka_broker_ip of this VpcepInfo.
        :type kafka_broker_ip: str
        """
        self._kafka_broker_ip = kafka_broker_ip

    @property
    def vpcep_service_id(self):
        """Gets the vpcep_service_id of this VpcepInfo.

        Kafka的VPCEP的service id

        :return: The vpcep_service_id of this VpcepInfo.
        :rtype: str
        """
        return self._vpcep_service_id

    @vpcep_service_id.setter
    def vpcep_service_id(self, vpcep_service_id):
        """Sets the vpcep_service_id of this VpcepInfo.

        Kafka的VPCEP的service id

        :param vpcep_service_id: The vpcep_service_id of this VpcepInfo.
        :type vpcep_service_id: str
        """
        self._vpcep_service_id = vpcep_service_id

    @property
    def vpcep_service_name(self):
        """Gets the vpcep_service_name of this VpcepInfo.

        Kafka的VPCEP的service name

        :return: The vpcep_service_name of this VpcepInfo.
        :rtype: str
        """
        return self._vpcep_service_name

    @vpcep_service_name.setter
    def vpcep_service_name(self, vpcep_service_name):
        """Sets the vpcep_service_name of this VpcepInfo.

        Kafka的VPCEP的service name

        :param vpcep_service_name: The vpcep_service_name of this VpcepInfo.
        :type vpcep_service_name: str
        """
        self._vpcep_service_name = vpcep_service_name

    @property
    def vpcep_client_port(self):
        """Gets the vpcep_client_port of this VpcepInfo.

        Kafka的VPCEP的client port

        :return: The vpcep_client_port of this VpcepInfo.
        :rtype: int
        """
        return self._vpcep_client_port

    @vpcep_client_port.setter
    def vpcep_client_port(self, vpcep_client_port):
        """Sets the vpcep_client_port of this VpcepInfo.

        Kafka的VPCEP的client port

        :param vpcep_client_port: The vpcep_client_port of this VpcepInfo.
        :type vpcep_client_port: int
        """
        self._vpcep_client_port = vpcep_client_port

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
        if not isinstance(other, VpcepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
