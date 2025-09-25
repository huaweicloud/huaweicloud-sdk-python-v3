# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetValueHostNumInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value_type': 'str',
        'host_num': 'int'
    }

    attribute_map = {
        'value_type': 'value_type',
        'host_num': 'host_num'
    }

    def __init__(self, value_type=None, host_num=None):
        r"""AssetValueHostNumInfo

        The model defined in huaweicloud sdk

        :param value_type: 重要性类型
        :type value_type: str
        :param host_num: 主机数量
        :type host_num: int
        """
        
        

        self._value_type = None
        self._host_num = None
        self.discriminator = None

        if value_type is not None:
            self.value_type = value_type
        if host_num is not None:
            self.host_num = host_num

    @property
    def value_type(self):
        r"""Gets the value_type of this AssetValueHostNumInfo.

        重要性类型

        :return: The value_type of this AssetValueHostNumInfo.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this AssetValueHostNumInfo.

        重要性类型

        :param value_type: The value_type of this AssetValueHostNumInfo.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def host_num(self):
        r"""Gets the host_num of this AssetValueHostNumInfo.

        主机数量

        :return: The host_num of this AssetValueHostNumInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this AssetValueHostNumInfo.

        主机数量

        :param host_num: The host_num of this AssetValueHostNumInfo.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, AssetValueHostNumInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
