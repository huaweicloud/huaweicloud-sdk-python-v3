# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SingleKvExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func': 'str'
    }

    attribute_map = {
        'func': 'func'
    }

    def __init__(self, func=None):
        r"""SingleKvExpression

        The model defined in huaweicloud sdk

        :param func: 取值：\&quot;is_doc\&quot;, \&quot;is_blob\&quot;, \&quot;is_exist\&quot;, \&quot;not_exist\&quot;。
        :type func: str
        """
        
        

        self._func = None
        self.discriminator = None

        self.func = func

    @property
    def func(self):
        r"""Gets the func of this SingleKvExpression.

        取值：\"is_doc\", \"is_blob\", \"is_exist\", \"not_exist\"。

        :return: The func of this SingleKvExpression.
        :rtype: str
        """
        return self._func

    @func.setter
    def func(self, func):
        r"""Sets the func of this SingleKvExpression.

        取值：\"is_doc\", \"is_blob\", \"is_exist\", \"not_exist\"。

        :param func: The func of this SingleKvExpression.
        :type func: str
        """
        self._func = func

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
        if not isinstance(other, SingleKvExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
