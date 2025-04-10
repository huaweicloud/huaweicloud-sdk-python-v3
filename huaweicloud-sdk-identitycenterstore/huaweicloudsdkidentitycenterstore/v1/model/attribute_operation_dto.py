# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributeOperationDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('attribute_value')

    openapi_types = {
        'attribute_path': 'str',
        'attribute_value': 'str'
    }

    attribute_map = {
        'attribute_path': 'attribute_path',
        'attribute_value': 'attribute_value'
    }

    def __init__(self, attribute_path=None, attribute_value=None):
        r"""AttributeOperationDto

        The model defined in huaweicloud sdk

        :param attribute_path: 要更新的属性的字符串表示
        :type attribute_path: str
        :param attribute_value: 要更新的属性值。当属性为对象类型时，此处填写对象的JSON字符串。为null时表示删除对应属性
        :type attribute_value: str
        """
        
        

        self._attribute_path = None
        self._attribute_value = None
        self.discriminator = None

        self.attribute_path = attribute_path
        if attribute_value is not None:
            self.attribute_value = attribute_value

    @property
    def attribute_path(self):
        r"""Gets the attribute_path of this AttributeOperationDto.

        要更新的属性的字符串表示

        :return: The attribute_path of this AttributeOperationDto.
        :rtype: str
        """
        return self._attribute_path

    @attribute_path.setter
    def attribute_path(self, attribute_path):
        r"""Sets the attribute_path of this AttributeOperationDto.

        要更新的属性的字符串表示

        :param attribute_path: The attribute_path of this AttributeOperationDto.
        :type attribute_path: str
        """
        self._attribute_path = attribute_path

    @property
    def attribute_value(self):
        r"""Gets the attribute_value of this AttributeOperationDto.

        要更新的属性值。当属性为对象类型时，此处填写对象的JSON字符串。为null时表示删除对应属性

        :return: The attribute_value of this AttributeOperationDto.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        r"""Sets the attribute_value of this AttributeOperationDto.

        要更新的属性值。当属性为对象类型时，此处填写对象的JSON字符串。为null时表示删除对应属性

        :param attribute_value: The attribute_value of this AttributeOperationDto.
        :type attribute_value: str
        """
        self._attribute_value = attribute_value

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
        if not isinstance(other, AttributeOperationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
