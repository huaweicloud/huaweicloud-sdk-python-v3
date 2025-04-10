# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransformationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transformation_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'transformation_type': 'transformation_type',
        'value': 'value'
    }

    def __init__(self, transformation_type=None, value=None):
        r"""TransformationInfo

        The model defined in huaweicloud sdk

        :param transformation_type: - 生成加工规则值为contentConditionalFilter - 生成配置规则值为configConditionalFilter
        :type transformation_type: str
        :param value: 过滤条件，生成加工规则值为sql条件语句，生成配置规则值为config。长度限制256。
        :type value: str
        """
        
        

        self._transformation_type = None
        self._value = None
        self.discriminator = None

        self.transformation_type = transformation_type
        self.value = value

    @property
    def transformation_type(self):
        r"""Gets the transformation_type of this TransformationInfo.

        - 生成加工规则值为contentConditionalFilter - 生成配置规则值为configConditionalFilter

        :return: The transformation_type of this TransformationInfo.
        :rtype: str
        """
        return self._transformation_type

    @transformation_type.setter
    def transformation_type(self, transformation_type):
        r"""Sets the transformation_type of this TransformationInfo.

        - 生成加工规则值为contentConditionalFilter - 生成配置规则值为configConditionalFilter

        :param transformation_type: The transformation_type of this TransformationInfo.
        :type transformation_type: str
        """
        self._transformation_type = transformation_type

    @property
    def value(self):
        r"""Gets the value of this TransformationInfo.

        过滤条件，生成加工规则值为sql条件语句，生成配置规则值为config。长度限制256。

        :return: The value of this TransformationInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TransformationInfo.

        过滤条件，生成加工规则值为sql条件语句，生成配置规则值为config。长度限制256。

        :param value: The value of this TransformationInfo.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, TransformationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
