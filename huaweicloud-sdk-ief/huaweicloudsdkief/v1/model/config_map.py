# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigMap:

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
        'description': 'str',
        'configs': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'configs': 'configs'
    }

    def __init__(self, name=None, description=None, configs=None):
        r"""ConfigMap

        The model defined in huaweicloud sdk

        :param name: 配置项名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param description: 配置项描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param configs: configs是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value无其它限制。 注：configs字典的长度即字典转为标准的字符串后的长度，例如字典{\&quot;a\&quot;: \&quot;b\&quot;}转为标准字符串后为&#39;{\&quot;a\&quot;: \&quot;b\&quot;}&#39;，长度为10
        :type configs: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._configs = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if configs is not None:
            self.configs = configs

    @property
    def name(self):
        r"""Gets the name of this ConfigMap.

        配置项名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this ConfigMap.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigMap.

        配置项名称，以小写英文字母开头，4-64位，可以使用小写英文、数字、中划线（-），不能以中划线结尾只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this ConfigMap.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ConfigMap.

        配置项描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this ConfigMap.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigMap.

        配置项描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this ConfigMap.
        :type description: str
        """
        self._description = description

    @property
    def configs(self):
        r"""Gets the configs of this ConfigMap.

        configs是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value无其它限制。 注：configs字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :return: The configs of this ConfigMap.
        :rtype: dict(str, str)
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this ConfigMap.

        configs是一个字典，由多个键值对组成，json化后最大总长度为1048576，key和value均为字符串。键值对中key由大小写字母或中划线开头，由数字、大小写字母、点号（.）、中划线（-）、下划线（_）组成，最小长度为1，最大长度63个字符， 键值对中的value无其它限制。 注：configs字典的长度即字典转为标准的字符串后的长度，例如字典{\"a\": \"b\"}转为标准字符串后为'{\"a\": \"b\"}'，长度为10

        :param configs: The configs of this ConfigMap.
        :type configs: dict(str, str)
        """
        self._configs = configs

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
        if not isinstance(other, ConfigMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
