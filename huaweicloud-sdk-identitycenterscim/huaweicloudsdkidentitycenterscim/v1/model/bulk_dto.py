# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BulkDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported': 'bool',
        'max_operations': 'int',
        'max_payload_size': 'int'
    }

    attribute_map = {
        'supported': 'supported',
        'max_operations': 'maxOperations',
        'max_payload_size': 'maxPayloadSize'
    }

    def __init__(self, supported=None, max_operations=None, max_payload_size=None):
        r"""BulkDto

        The model defined in huaweicloud sdk

        :param supported: 一个布尔值，表示服务提供商是否支持这种操作
        :type supported: bool
        :param max_operations: 一次可操作的最大个数
        :type max_operations: int
        :param max_payload_size: 最大有效载荷量
        :type max_payload_size: int
        """
        
        

        self._supported = None
        self._max_operations = None
        self._max_payload_size = None
        self.discriminator = None

        if supported is not None:
            self.supported = supported
        if max_operations is not None:
            self.max_operations = max_operations
        if max_payload_size is not None:
            self.max_payload_size = max_payload_size

    @property
    def supported(self):
        r"""Gets the supported of this BulkDto.

        一个布尔值，表示服务提供商是否支持这种操作

        :return: The supported of this BulkDto.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        r"""Sets the supported of this BulkDto.

        一个布尔值，表示服务提供商是否支持这种操作

        :param supported: The supported of this BulkDto.
        :type supported: bool
        """
        self._supported = supported

    @property
    def max_operations(self):
        r"""Gets the max_operations of this BulkDto.

        一次可操作的最大个数

        :return: The max_operations of this BulkDto.
        :rtype: int
        """
        return self._max_operations

    @max_operations.setter
    def max_operations(self, max_operations):
        r"""Sets the max_operations of this BulkDto.

        一次可操作的最大个数

        :param max_operations: The max_operations of this BulkDto.
        :type max_operations: int
        """
        self._max_operations = max_operations

    @property
    def max_payload_size(self):
        r"""Gets the max_payload_size of this BulkDto.

        最大有效载荷量

        :return: The max_payload_size of this BulkDto.
        :rtype: int
        """
        return self._max_payload_size

    @max_payload_size.setter
    def max_payload_size(self, max_payload_size):
        r"""Sets the max_payload_size of this BulkDto.

        最大有效载荷量

        :param max_payload_size: The max_payload_size of this BulkDto.
        :type max_payload_size: int
        """
        self._max_payload_size = max_payload_size

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
        if not isinstance(other, BulkDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
