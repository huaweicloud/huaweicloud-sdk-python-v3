# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMySQLCompatibilityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str'
    }

    attribute_map = {
        'port': 'port'
    }

    def __init__(self, port=None):
        """UpdateMySQLCompatibilityRequestBody

        The model defined in huaweicloud sdk

        :param port: MySQL兼容端口，修改端口的时候必填，不填默认保持原有设定端口，可选范围为：0, 1024-39998。 - 取值为0，标识关闭MySQL兼容端口服务。 - 限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,6500,8000-8006,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。 - 与数据库对外端口互斥。
        :type port: str
        """
        
        

        self._port = None
        self.discriminator = None

        if port is not None:
            self.port = port

    @property
    def port(self):
        """Gets the port of this UpdateMySQLCompatibilityRequestBody.

        MySQL兼容端口，修改端口的时候必填，不填默认保持原有设定端口，可选范围为：0, 1024-39998。 - 取值为0，标识关闭MySQL兼容端口服务。 - 限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,6500,8000-8006,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。 - 与数据库对外端口互斥。

        :return: The port of this UpdateMySQLCompatibilityRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this UpdateMySQLCompatibilityRequestBody.

        MySQL兼容端口，修改端口的时候必填，不填默认保持原有设定端口，可选范围为：0, 1024-39998。 - 取值为0，标识关闭MySQL兼容端口服务。 - 限制端口： 2378,2379,2380,4999,5000,5999,6000,6001,6500,8000-8006,8097,8098,12016,12017,20049,20050,21731,21732,32122,32123,32124。 - 与数据库对外端口互斥。

        :param port: The port of this UpdateMySQLCompatibilityRequestBody.
        :type port: str
        """
        self._port = port

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
        if not isinstance(other, UpdateMySQLCompatibilityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
