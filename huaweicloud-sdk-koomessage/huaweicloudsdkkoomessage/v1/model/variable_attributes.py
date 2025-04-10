# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableAttributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'variable_index': 'int',
        'variable_type': 'str',
        'variable_desc': 'str'
    }

    attribute_map = {
        'variable_index': 'variable_index',
        'variable_type': 'variable_type',
        'variable_desc': 'variable_desc'
    }

    def __init__(self, variable_index=None, variable_type=None, variable_desc=None):
        r"""VariableAttributes

        The model defined in huaweicloud sdk

        :param variable_index: 参数索引。
        :type variable_index: int
        :param variable_type: 参数类型。PHONE：电话号码，NEWTEXT：解析标识，CHARDIGIT：其他号码(如验证码、订单号、密码等)，DATETIME：日期时间，MONEY：金额，TEXT：其他。
        :type variable_type: str
        :param variable_desc: 参数描述。变量类型为TEXT（其他）时必填。
        :type variable_desc: str
        """
        
        

        self._variable_index = None
        self._variable_type = None
        self._variable_desc = None
        self.discriminator = None

        self.variable_index = variable_index
        self.variable_type = variable_type
        if variable_desc is not None:
            self.variable_desc = variable_desc

    @property
    def variable_index(self):
        r"""Gets the variable_index of this VariableAttributes.

        参数索引。

        :return: The variable_index of this VariableAttributes.
        :rtype: int
        """
        return self._variable_index

    @variable_index.setter
    def variable_index(self, variable_index):
        r"""Sets the variable_index of this VariableAttributes.

        参数索引。

        :param variable_index: The variable_index of this VariableAttributes.
        :type variable_index: int
        """
        self._variable_index = variable_index

    @property
    def variable_type(self):
        r"""Gets the variable_type of this VariableAttributes.

        参数类型。PHONE：电话号码，NEWTEXT：解析标识，CHARDIGIT：其他号码(如验证码、订单号、密码等)，DATETIME：日期时间，MONEY：金额，TEXT：其他。

        :return: The variable_type of this VariableAttributes.
        :rtype: str
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this VariableAttributes.

        参数类型。PHONE：电话号码，NEWTEXT：解析标识，CHARDIGIT：其他号码(如验证码、订单号、密码等)，DATETIME：日期时间，MONEY：金额，TEXT：其他。

        :param variable_type: The variable_type of this VariableAttributes.
        :type variable_type: str
        """
        self._variable_type = variable_type

    @property
    def variable_desc(self):
        r"""Gets the variable_desc of this VariableAttributes.

        参数描述。变量类型为TEXT（其他）时必填。

        :return: The variable_desc of this VariableAttributes.
        :rtype: str
        """
        return self._variable_desc

    @variable_desc.setter
    def variable_desc(self, variable_desc):
        r"""Sets the variable_desc of this VariableAttributes.

        参数描述。变量类型为TEXT（其他）时必填。

        :param variable_desc: The variable_desc of this VariableAttributes.
        :type variable_desc: str
        """
        self._variable_desc = variable_desc

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
        if not isinstance(other, VariableAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
