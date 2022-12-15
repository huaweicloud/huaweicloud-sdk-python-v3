# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedStorageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'host_num': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'host_num': 'host_num'
    }

    def __init__(self, spec_code=None, host_num=None):
        """DedicatedStorageInfo

        The model defined in huaweicloud sdk

        :param spec_code: 专属资源池存储资源规格码。
        :type spec_code: str
        :param host_num: 专属资源池存储主机数量。
        :type host_num: int
        """
        
        

        self._spec_code = None
        self._host_num = None
        self.discriminator = None

        self.spec_code = spec_code
        self.host_num = host_num

    @property
    def spec_code(self):
        """Gets the spec_code of this DedicatedStorageInfo.

        专属资源池存储资源规格码。

        :return: The spec_code of this DedicatedStorageInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this DedicatedStorageInfo.

        专属资源池存储资源规格码。

        :param spec_code: The spec_code of this DedicatedStorageInfo.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def host_num(self):
        """Gets the host_num of this DedicatedStorageInfo.

        专属资源池存储主机数量。

        :return: The host_num of this DedicatedStorageInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this DedicatedStorageInfo.

        专属资源池存储主机数量。

        :param host_num: The host_num of this DedicatedStorageInfo.
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
        if not isinstance(other, DedicatedStorageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
