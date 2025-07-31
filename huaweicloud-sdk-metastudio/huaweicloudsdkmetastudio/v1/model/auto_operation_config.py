# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoOperationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation': 'str',
        'operation_time': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'operation_time': 'operation_time'
    }

    def __init__(self, operation=None, operation_time=None):
        r"""AutoOperationConfig

        The model defined in huaweicloud sdk

        :param operation: BLOCK: 冻结 DELETE：删除
        :type operation: str
        :param operation_time: 资源过期时间，格式遵循：RFC 3339 如\&quot;2025-01-10T00:00:00Z\&quot;
        :type operation_time: str
        """
        
        

        self._operation = None
        self._operation_time = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if operation_time is not None:
            self.operation_time = operation_time

    @property
    def operation(self):
        r"""Gets the operation of this AutoOperationConfig.

        BLOCK: 冻结 DELETE：删除

        :return: The operation of this AutoOperationConfig.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this AutoOperationConfig.

        BLOCK: 冻结 DELETE：删除

        :param operation: The operation of this AutoOperationConfig.
        :type operation: str
        """
        self._operation = operation

    @property
    def operation_time(self):
        r"""Gets the operation_time of this AutoOperationConfig.

        资源过期时间，格式遵循：RFC 3339 如\"2025-01-10T00:00:00Z\"

        :return: The operation_time of this AutoOperationConfig.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this AutoOperationConfig.

        资源过期时间，格式遵循：RFC 3339 如\"2025-01-10T00:00:00Z\"

        :param operation_time: The operation_time of this AutoOperationConfig.
        :type operation_time: str
        """
        self._operation_time = operation_time

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
        if not isinstance(other, AutoOperationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
