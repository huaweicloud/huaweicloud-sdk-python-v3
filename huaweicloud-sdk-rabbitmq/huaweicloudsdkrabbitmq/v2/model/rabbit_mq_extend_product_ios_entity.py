# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RabbitMQExtendProductIosEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'io_spec': 'str',
        'available_zones': 'list[str]',
        'type': 'str',
        'unavailable_zones': 'list[str]'
    }

    attribute_map = {
        'io_spec': 'io_spec',
        'available_zones': 'available_zones',
        'type': 'type',
        'unavailable_zones': 'unavailable_zones'
    }

    def __init__(self, io_spec=None, available_zones=None, type=None, unavailable_zones=None):
        """RabbitMQExtendProductIosEntity

        The model defined in huaweicloud sdk

        :param io_spec: 存储IO规格。
        :type io_spec: str
        :param available_zones: 有可用资源的可用区列表
        :type available_zones: list[str]
        :param type: IO类型。
        :type type: str
        :param unavailable_zones: 资源售罄的可用区列表。
        :type unavailable_zones: list[str]
        """
        
        

        self._io_spec = None
        self._available_zones = None
        self._type = None
        self._unavailable_zones = None
        self.discriminator = None

        if io_spec is not None:
            self.io_spec = io_spec
        if available_zones is not None:
            self.available_zones = available_zones
        if type is not None:
            self.type = type
        if unavailable_zones is not None:
            self.unavailable_zones = unavailable_zones

    @property
    def io_spec(self):
        """Gets the io_spec of this RabbitMQExtendProductIosEntity.

        存储IO规格。

        :return: The io_spec of this RabbitMQExtendProductIosEntity.
        :rtype: str
        """
        return self._io_spec

    @io_spec.setter
    def io_spec(self, io_spec):
        """Sets the io_spec of this RabbitMQExtendProductIosEntity.

        存储IO规格。

        :param io_spec: The io_spec of this RabbitMQExtendProductIosEntity.
        :type io_spec: str
        """
        self._io_spec = io_spec

    @property
    def available_zones(self):
        """Gets the available_zones of this RabbitMQExtendProductIosEntity.

        有可用资源的可用区列表

        :return: The available_zones of this RabbitMQExtendProductIosEntity.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this RabbitMQExtendProductIosEntity.

        有可用资源的可用区列表

        :param available_zones: The available_zones of this RabbitMQExtendProductIosEntity.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def type(self):
        """Gets the type of this RabbitMQExtendProductIosEntity.

        IO类型。

        :return: The type of this RabbitMQExtendProductIosEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RabbitMQExtendProductIosEntity.

        IO类型。

        :param type: The type of this RabbitMQExtendProductIosEntity.
        :type type: str
        """
        self._type = type

    @property
    def unavailable_zones(self):
        """Gets the unavailable_zones of this RabbitMQExtendProductIosEntity.

        资源售罄的可用区列表。

        :return: The unavailable_zones of this RabbitMQExtendProductIosEntity.
        :rtype: list[str]
        """
        return self._unavailable_zones

    @unavailable_zones.setter
    def unavailable_zones(self, unavailable_zones):
        """Sets the unavailable_zones of this RabbitMQExtendProductIosEntity.

        资源售罄的可用区列表。

        :param unavailable_zones: The unavailable_zones of this RabbitMQExtendProductIosEntity.
        :type unavailable_zones: list[str]
        """
        self._unavailable_zones = unavailable_zones

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
        if not isinstance(other, RabbitMQExtendProductIosEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
