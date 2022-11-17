# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespHostType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_type': 'str',
        'host_type_name': 'str'
    }

    attribute_map = {
        'host_type': 'host_type',
        'host_type_name': 'host_type_name'
    }

    def __init__(self, host_type=None, host_type_name=None):
        """RespHostType

        The model defined in huaweicloud sdk

        :param host_type: 专属主机类型。
        :type host_type: str
        :param host_type_name: 专属主机类型名字。
        :type host_type_name: str
        """
        
        

        self._host_type = None
        self._host_type_name = None
        self.discriminator = None

        self.host_type = host_type
        self.host_type_name = host_type_name

    @property
    def host_type(self):
        """Gets the host_type of this RespHostType.

        专属主机类型。

        :return: The host_type of this RespHostType.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this RespHostType.

        专属主机类型。

        :param host_type: The host_type of this RespHostType.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def host_type_name(self):
        """Gets the host_type_name of this RespHostType.

        专属主机类型名字。

        :return: The host_type_name of this RespHostType.
        :rtype: str
        """
        return self._host_type_name

    @host_type_name.setter
    def host_type_name(self, host_type_name):
        """Sets the host_type_name of this RespHostType.

        专属主机类型名字。

        :param host_type_name: The host_type_name of this RespHostType.
        :type host_type_name: str
        """
        self._host_type_name = host_type_name

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
        if not isinstance(other, RespHostType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
