# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleSetV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ruleset_id': 'str',
        'language': 'str'
    }

    attribute_map = {
        'ruleset_id': 'ruleset_id',
        'language': 'language'
    }

    def __init__(self, ruleset_id=None, language=None):
        r"""RuleSetV2

        The model defined in huaweicloud sdk

        :param ruleset_id: 规则集id，需要从web界面获取
        :type ruleset_id: str
        :param language: 检查语言，支持cpp,java,js,python,php,css,html,go,typescript
        :type language: str
        """
        
        

        self._ruleset_id = None
        self._language = None
        self.discriminator = None

        if ruleset_id is not None:
            self.ruleset_id = ruleset_id
        self.language = language

    @property
    def ruleset_id(self):
        r"""Gets the ruleset_id of this RuleSetV2.

        规则集id，需要从web界面获取

        :return: The ruleset_id of this RuleSetV2.
        :rtype: str
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        r"""Sets the ruleset_id of this RuleSetV2.

        规则集id，需要从web界面获取

        :param ruleset_id: The ruleset_id of this RuleSetV2.
        :type ruleset_id: str
        """
        self._ruleset_id = ruleset_id

    @property
    def language(self):
        r"""Gets the language of this RuleSetV2.

        检查语言，支持cpp,java,js,python,php,css,html,go,typescript

        :return: The language of this RuleSetV2.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RuleSetV2.

        检查语言，支持cpp,java,js,python,php,css,html,go,typescript

        :param language: The language of this RuleSetV2.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, RuleSetV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
