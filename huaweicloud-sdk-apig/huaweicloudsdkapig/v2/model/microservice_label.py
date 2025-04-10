# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroserviceLabel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_name': 'str',
        'label_value': 'str'
    }

    attribute_map = {
        'label_name': 'label_name',
        'label_value': 'label_value'
    }

    def __init__(self, label_name=None, label_value=None):
        r"""MicroserviceLabel

        The model defined in huaweicloud sdk

        :param label_name: 标签名称。  以字母或者数字开头和结尾，由字母、数字、连接符(&#39;-&#39;)、下划线(&#39;_&#39;)、点号(&#39;.&#39;)组成且63个字符之内。
        :type label_name: str
        :param label_value: 标签值。  以字母或者数字开头和结尾，由字母、数字、连接符(&#39;-&#39;)、下划线(&#39;_&#39;)、点号(&#39;.&#39;)组成且63个字符之内。
        :type label_value: str
        """
        
        

        self._label_name = None
        self._label_value = None
        self.discriminator = None

        self.label_name = label_name
        self.label_value = label_value

    @property
    def label_name(self):
        r"""Gets the label_name of this MicroserviceLabel.

        标签名称。  以字母或者数字开头和结尾，由字母、数字、连接符('-')、下划线('_')、点号('.')组成且63个字符之内。

        :return: The label_name of this MicroserviceLabel.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this MicroserviceLabel.

        标签名称。  以字母或者数字开头和结尾，由字母、数字、连接符('-')、下划线('_')、点号('.')组成且63个字符之内。

        :param label_name: The label_name of this MicroserviceLabel.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def label_value(self):
        r"""Gets the label_value of this MicroserviceLabel.

        标签值。  以字母或者数字开头和结尾，由字母、数字、连接符('-')、下划线('_')、点号('.')组成且63个字符之内。

        :return: The label_value of this MicroserviceLabel.
        :rtype: str
        """
        return self._label_value

    @label_value.setter
    def label_value(self, label_value):
        r"""Sets the label_value of this MicroserviceLabel.

        标签值。  以字母或者数字开头和结尾，由字母、数字、连接符('-')、下划线('_')、点号('.')组成且63个字符之内。

        :param label_value: The label_value of this MicroserviceLabel.
        :type label_value: str
        """
        self._label_value = label_value

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
        if not isinstance(other, MicroserviceLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
