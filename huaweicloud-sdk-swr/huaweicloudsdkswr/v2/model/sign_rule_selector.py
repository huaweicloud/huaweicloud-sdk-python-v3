# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignRuleSelector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'decoration': 'str',
        'pattern': 'str',
        'extras': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'decoration': 'decoration',
        'pattern': 'pattern',
        'extras': 'extras'
    }

    def __init__(self, kind=None, decoration=None, pattern=None, extras=None):
        r"""SignRuleSelector

        The model defined in huaweicloud sdk

        :param kind: 匹配类型，目前只支持doublestar
        :type kind: str
        :param decoration: 选择器匹配类型,当前支持repoMatches
        :type decoration: str
        :param pattern: 选择器匹配样式，最大长度512。支持正则表达式，正则表达式规则可填写如 nginx-* ，{repo1，repo2} 等，其中： * ： 匹配不包含 &#39;/&#39; 的任何字段。 **：匹配包含 &#39;/&#39; 的任何字段。 ? ：匹配任何单个非 &#39;/&#39; 的字符。 {选项1,选项2,...}：同时匹配多个选项。
        :type pattern: str
        :param extras: 预留字段，镜像签名策略中，对无版本的制品进行签名则传入{\&quot;untagged\&quot;:true}
        :type extras: str
        """
        
        

        self._kind = None
        self._decoration = None
        self._pattern = None
        self._extras = None
        self.discriminator = None

        self.kind = kind
        self.decoration = decoration
        self.pattern = pattern
        if extras is not None:
            self.extras = extras

    @property
    def kind(self):
        r"""Gets the kind of this SignRuleSelector.

        匹配类型，目前只支持doublestar

        :return: The kind of this SignRuleSelector.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this SignRuleSelector.

        匹配类型，目前只支持doublestar

        :param kind: The kind of this SignRuleSelector.
        :type kind: str
        """
        self._kind = kind

    @property
    def decoration(self):
        r"""Gets the decoration of this SignRuleSelector.

        选择器匹配类型,当前支持repoMatches

        :return: The decoration of this SignRuleSelector.
        :rtype: str
        """
        return self._decoration

    @decoration.setter
    def decoration(self, decoration):
        r"""Sets the decoration of this SignRuleSelector.

        选择器匹配类型,当前支持repoMatches

        :param decoration: The decoration of this SignRuleSelector.
        :type decoration: str
        """
        self._decoration = decoration

    @property
    def pattern(self):
        r"""Gets the pattern of this SignRuleSelector.

        选择器匹配样式，最大长度512。支持正则表达式，正则表达式规则可填写如 nginx-* ，{repo1，repo2} 等，其中： * ： 匹配不包含 '/' 的任何字段。 **：匹配包含 '/' 的任何字段。 ? ：匹配任何单个非 '/' 的字符。 {选项1,选项2,...}：同时匹配多个选项。

        :return: The pattern of this SignRuleSelector.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this SignRuleSelector.

        选择器匹配样式，最大长度512。支持正则表达式，正则表达式规则可填写如 nginx-* ，{repo1，repo2} 等，其中： * ： 匹配不包含 '/' 的任何字段。 **：匹配包含 '/' 的任何字段。 ? ：匹配任何单个非 '/' 的字符。 {选项1,选项2,...}：同时匹配多个选项。

        :param pattern: The pattern of this SignRuleSelector.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def extras(self):
        r"""Gets the extras of this SignRuleSelector.

        预留字段，镜像签名策略中，对无版本的制品进行签名则传入{\"untagged\":true}

        :return: The extras of this SignRuleSelector.
        :rtype: str
        """
        return self._extras

    @extras.setter
    def extras(self, extras):
        r"""Sets the extras of this SignRuleSelector.

        预留字段，镜像签名策略中，对无版本的制品进行签名则传入{\"untagged\":true}

        :param extras: The extras of this SignRuleSelector.
        :type extras: str
        """
        self._extras = extras

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
        if not isinstance(other, SignRuleSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
