# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateExternalEntityReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'connection_type': 'str',
        'mqtt_connection_info': 'MqttConnectionInfo'
    }

    attribute_map = {
        'protocol': 'protocol',
        'connection_type': 'connection_type',
        'mqtt_connection_info': 'mqtt_connection_info'
    }

    def __init__(self, protocol=None, connection_type=None, mqtt_connection_info=None):
        r"""UpdateExternalEntityReqDTO

        The model defined in huaweicloud sdk

        :param protocol: 连接外部实体的协议类型
        :type protocol: str
        :param connection_type: 连接类型
        :type connection_type: str
        :param mqtt_connection_info: 
        :type mqtt_connection_info: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        """
        
        

        self._protocol = None
        self._connection_type = None
        self._mqtt_connection_info = None
        self.discriminator = None

        self.protocol = protocol
        self.connection_type = connection_type
        if mqtt_connection_info is not None:
            self.mqtt_connection_info = mqtt_connection_info

    @property
    def protocol(self):
        r"""Gets the protocol of this UpdateExternalEntityReqDTO.

        连接外部实体的协议类型

        :return: The protocol of this UpdateExternalEntityReqDTO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this UpdateExternalEntityReqDTO.

        连接外部实体的协议类型

        :param protocol: The protocol of this UpdateExternalEntityReqDTO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def connection_type(self):
        r"""Gets the connection_type of this UpdateExternalEntityReqDTO.

        连接类型

        :return: The connection_type of this UpdateExternalEntityReqDTO.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this UpdateExternalEntityReqDTO.

        连接类型

        :param connection_type: The connection_type of this UpdateExternalEntityReqDTO.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def mqtt_connection_info(self):
        r"""Gets the mqtt_connection_info of this UpdateExternalEntityReqDTO.

        :return: The mqtt_connection_info of this UpdateExternalEntityReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        """
        return self._mqtt_connection_info

    @mqtt_connection_info.setter
    def mqtt_connection_info(self, mqtt_connection_info):
        r"""Sets the mqtt_connection_info of this UpdateExternalEntityReqDTO.

        :param mqtt_connection_info: The mqtt_connection_info of this UpdateExternalEntityReqDTO.
        :type mqtt_connection_info: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        """
        self._mqtt_connection_info = mqtt_connection_info

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
        if not isinstance(other, UpdateExternalEntityReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
