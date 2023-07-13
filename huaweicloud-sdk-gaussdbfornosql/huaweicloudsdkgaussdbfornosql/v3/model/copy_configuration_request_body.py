# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyConfigurationRequestBody:

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
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, name=None, description=None):
        """CopyConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param name: 复制后的参数模板名称。最长64个字符，只允许大写字母、小写字母、数字、和“-_.”特殊字符。
        :type name: str
        :param description: 参数模板描述。最长256个字符，不支持&gt;!&lt;\&quot;&amp;&#39;&#x3D;特殊字符。默认为空。
        :type description: str
        """
        
        

        self._name = None
        self._description = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CopyConfigurationRequestBody.

        复制后的参数模板名称。最长64个字符，只允许大写字母、小写字母、数字、和“-_.”特殊字符。

        :return: The name of this CopyConfigurationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CopyConfigurationRequestBody.

        复制后的参数模板名称。最长64个字符，只允许大写字母、小写字母、数字、和“-_.”特殊字符。

        :param name: The name of this CopyConfigurationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CopyConfigurationRequestBody.

        参数模板描述。最长256个字符，不支持>!<\"&'=特殊字符。默认为空。

        :return: The description of this CopyConfigurationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CopyConfigurationRequestBody.

        参数模板描述。最长256个字符，不支持>!<\"&'=特殊字符。默认为空。

        :param description: The description of this CopyConfigurationRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CopyConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
