# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionInfoFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'concurrency_type': 'str',
        'concurrency': 'int',
        'bandwidth_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'concurrency_type': 'concurrency_type',
        'concurrency': 'concurrency',
        'bandwidth_type': 'bandwidth_type'
    }

    def __init__(self, name=None, concurrency_type=None, concurrency=None, bandwidth_type=None):
        """ConnectionInfoFlavor

        The model defined in huaweicloud sdk

        :param name: 规格名称
        :type name: str
        :param concurrency_type: 并发规格类型
        :type concurrency_type: str
        :param concurrency: 并发数
        :type concurrency: int
        :param bandwidth_type: 带宽类型
        :type bandwidth_type: str
        """
        
        

        self._name = None
        self._concurrency_type = None
        self._concurrency = None
        self._bandwidth_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if concurrency_type is not None:
            self.concurrency_type = concurrency_type
        if concurrency is not None:
            self.concurrency = concurrency
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type

    @property
    def name(self):
        """Gets the name of this ConnectionInfoFlavor.

        规格名称

        :return: The name of this ConnectionInfoFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionInfoFlavor.

        规格名称

        :param name: The name of this ConnectionInfoFlavor.
        :type name: str
        """
        self._name = name

    @property
    def concurrency_type(self):
        """Gets the concurrency_type of this ConnectionInfoFlavor.

        并发规格类型

        :return: The concurrency_type of this ConnectionInfoFlavor.
        :rtype: str
        """
        return self._concurrency_type

    @concurrency_type.setter
    def concurrency_type(self, concurrency_type):
        """Sets the concurrency_type of this ConnectionInfoFlavor.

        并发规格类型

        :param concurrency_type: The concurrency_type of this ConnectionInfoFlavor.
        :type concurrency_type: str
        """
        self._concurrency_type = concurrency_type

    @property
    def concurrency(self):
        """Gets the concurrency of this ConnectionInfoFlavor.

        并发数

        :return: The concurrency of this ConnectionInfoFlavor.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this ConnectionInfoFlavor.

        并发数

        :param concurrency: The concurrency of this ConnectionInfoFlavor.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this ConnectionInfoFlavor.

        带宽类型

        :return: The bandwidth_type of this ConnectionInfoFlavor.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this ConnectionInfoFlavor.

        带宽类型

        :param bandwidth_type: The bandwidth_type of this ConnectionInfoFlavor.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

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
        if not isinstance(other, ConnectionInfoFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
