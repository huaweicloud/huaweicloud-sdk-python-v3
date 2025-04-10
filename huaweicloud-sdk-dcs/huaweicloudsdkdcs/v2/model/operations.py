# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Operations:

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
        'is_support': 'bool',
        'cause_id': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'is_support': 'is_support',
        'cause_id': 'cause_id'
    }

    def __init__(self, operation=None, is_support=None, cause_id=None):
        r"""Operations

        The model defined in huaweicloud sdk

        :param operation: 操作信息
        :type operation: str
        :param is_support: 是否支持该操作
        :type is_support: bool
        :param cause_id: 不支持该操作的原因ID，仅在is_support为false时返回
        :type cause_id: str
        """
        
        

        self._operation = None
        self._is_support = None
        self._cause_id = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if is_support is not None:
            self.is_support = is_support
        if cause_id is not None:
            self.cause_id = cause_id

    @property
    def operation(self):
        r"""Gets the operation of this Operations.

        操作信息

        :return: The operation of this Operations.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this Operations.

        操作信息

        :param operation: The operation of this Operations.
        :type operation: str
        """
        self._operation = operation

    @property
    def is_support(self):
        r"""Gets the is_support of this Operations.

        是否支持该操作

        :return: The is_support of this Operations.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this Operations.

        是否支持该操作

        :param is_support: The is_support of this Operations.
        :type is_support: bool
        """
        self._is_support = is_support

    @property
    def cause_id(self):
        r"""Gets the cause_id of this Operations.

        不支持该操作的原因ID，仅在is_support为false时返回

        :return: The cause_id of this Operations.
        :rtype: str
        """
        return self._cause_id

    @cause_id.setter
    def cause_id(self, cause_id):
        r"""Sets the cause_id of this Operations.

        不支持该操作的原因ID，仅在is_support为false时返回

        :param cause_id: The cause_id of this Operations.
        :type cause_id: str
        """
        self._cause_id = cause_id

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
        if not isinstance(other, Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
