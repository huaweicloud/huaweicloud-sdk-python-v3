# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllConfigValueByTypeAndKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'key': 'key',
        'type': 'type'
    }

    def __init__(self, service_id=None, key=None, type=None):
        r"""ShowAllConfigValueByTypeAndKeyRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param key: 配置项key
        :type key: str
        :param type: 配置项类型
        :type type: str
        """
        
        

        self._service_id = None
        self._key = None
        self._type = None
        self.discriminator = None

        self.service_id = service_id
        self.key = key
        self.type = type

    @property
    def service_id(self):
        r"""Gets the service_id of this ShowAllConfigValueByTypeAndKeyRequest.

        服务id

        :return: The service_id of this ShowAllConfigValueByTypeAndKeyRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ShowAllConfigValueByTypeAndKeyRequest.

        服务id

        :param service_id: The service_id of this ShowAllConfigValueByTypeAndKeyRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def key(self):
        r"""Gets the key of this ShowAllConfigValueByTypeAndKeyRequest.

        配置项key

        :return: The key of this ShowAllConfigValueByTypeAndKeyRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ShowAllConfigValueByTypeAndKeyRequest.

        配置项key

        :param key: The key of this ShowAllConfigValueByTypeAndKeyRequest.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this ShowAllConfigValueByTypeAndKeyRequest.

        配置项类型

        :return: The type of this ShowAllConfigValueByTypeAndKeyRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAllConfigValueByTypeAndKeyRequest.

        配置项类型

        :param type: The type of this ShowAllConfigValueByTypeAndKeyRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowAllConfigValueByTypeAndKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
