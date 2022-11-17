# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExternalEntityReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_id': 'str',
        'protocol': 'str',
        'connection_type': 'str',
        'mqtt_connection_info': 'MqttConnectionInfo',
        'space_id': 'str'
    }

    attribute_map = {
        'external_id': 'external_id',
        'protocol': 'protocol',
        'connection_type': 'connection_type',
        'mqtt_connection_info': 'mqtt_connection_info',
        'space_id': 'space_id'
    }

    def __init__(self, external_id=None, protocol=None, connection_type=None, mqtt_connection_info=None, space_id=None):
        """CreateExternalEntityReqDTO

        The model defined in huaweicloud sdk

        :param external_id: 外部实体Id，节点下唯一
        :type external_id: str
        :param protocol: 连接外部实体的协议类型
        :type protocol: str
        :param connection_type: 连接类型
        :type connection_type: str
        :param mqtt_connection_info: 
        :type mqtt_connection_info: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        :param space_id: 资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.
        :type space_id: str
        """
        
        

        self._external_id = None
        self._protocol = None
        self._connection_type = None
        self._mqtt_connection_info = None
        self._space_id = None
        self.discriminator = None

        self.external_id = external_id
        self.protocol = protocol
        self.connection_type = connection_type
        if mqtt_connection_info is not None:
            self.mqtt_connection_info = mqtt_connection_info
        if space_id is not None:
            self.space_id = space_id

    @property
    def external_id(self):
        """Gets the external_id of this CreateExternalEntityReqDTO.

        外部实体Id，节点下唯一

        :return: The external_id of this CreateExternalEntityReqDTO.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateExternalEntityReqDTO.

        外部实体Id，节点下唯一

        :param external_id: The external_id of this CreateExternalEntityReqDTO.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def protocol(self):
        """Gets the protocol of this CreateExternalEntityReqDTO.

        连接外部实体的协议类型

        :return: The protocol of this CreateExternalEntityReqDTO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateExternalEntityReqDTO.

        连接外部实体的协议类型

        :param protocol: The protocol of this CreateExternalEntityReqDTO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def connection_type(self):
        """Gets the connection_type of this CreateExternalEntityReqDTO.

        连接类型

        :return: The connection_type of this CreateExternalEntityReqDTO.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this CreateExternalEntityReqDTO.

        连接类型

        :param connection_type: The connection_type of this CreateExternalEntityReqDTO.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def mqtt_connection_info(self):
        """Gets the mqtt_connection_info of this CreateExternalEntityReqDTO.

        :return: The mqtt_connection_info of this CreateExternalEntityReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        """
        return self._mqtt_connection_info

    @mqtt_connection_info.setter
    def mqtt_connection_info(self, mqtt_connection_info):
        """Sets the mqtt_connection_info of this CreateExternalEntityReqDTO.

        :param mqtt_connection_info: The mqtt_connection_info of this CreateExternalEntityReqDTO.
        :type mqtt_connection_info: :class:`huaweicloudsdkiotedge.v2.MqttConnectionInfo`
        """
        self._mqtt_connection_info = mqtt_connection_info

    @property
    def space_id(self):
        """Gets the space_id of this CreateExternalEntityReqDTO.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.

        :return: The space_id of this CreateExternalEntityReqDTO.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this CreateExternalEntityReqDTO.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的外部实体归属到IoDA哪个资源空间下的边缘节点设备下，否则创建的外部实体将会归属到默认资源空间下对应的边缘节点下,对应于IoDA的app_id.

        :param space_id: The space_id of this CreateExternalEntityReqDTO.
        :type space_id: str
        """
        self._space_id = space_id

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
        if not isinstance(other, CreateExternalEntityReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
