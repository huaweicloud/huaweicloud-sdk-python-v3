# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignScopeRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_selectors': 'list[SignRuleSelector]',
        'scope_selectors': 'dict(str, list[SignRuleSelector])',
        'repo_scope_mode': 'str'
    }

    attribute_map = {
        'tag_selectors': 'tag_selectors',
        'scope_selectors': 'scope_selectors',
        'repo_scope_mode': 'repo_scope_mode'
    }

    def __init__(self, tag_selectors=None, scope_selectors=None, repo_scope_mode=None):
        r"""SignScopeRule

        The model defined in huaweicloud sdk

        :param tag_selectors: 制品版本选择器，目前只支持长度为1
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.SignRuleSelector`]
        :param scope_selectors: 制品仓库选择器，目前只支持repository且长度为1
        :type scope_selectors: dict(str, list[SignRuleSelector])
        :param repo_scope_mode: repository选择方式。可选regular、selection，前端显示需要，api调用时可选regular
        :type repo_scope_mode: str
        """
        
        

        self._tag_selectors = None
        self._scope_selectors = None
        self._repo_scope_mode = None
        self.discriminator = None

        self.tag_selectors = tag_selectors
        self.scope_selectors = scope_selectors
        self.repo_scope_mode = repo_scope_mode

    @property
    def tag_selectors(self):
        r"""Gets the tag_selectors of this SignScopeRule.

        制品版本选择器，目前只支持长度为1

        :return: The tag_selectors of this SignScopeRule.
        :rtype: list[:class:`huaweicloudsdkswr.v2.SignRuleSelector`]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        r"""Sets the tag_selectors of this SignScopeRule.

        制品版本选择器，目前只支持长度为1

        :param tag_selectors: The tag_selectors of this SignScopeRule.
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.SignRuleSelector`]
        """
        self._tag_selectors = tag_selectors

    @property
    def scope_selectors(self):
        r"""Gets the scope_selectors of this SignScopeRule.

        制品仓库选择器，目前只支持repository且长度为1

        :return: The scope_selectors of this SignScopeRule.
        :rtype: dict(str, list[SignRuleSelector])
        """
        return self._scope_selectors

    @scope_selectors.setter
    def scope_selectors(self, scope_selectors):
        r"""Sets the scope_selectors of this SignScopeRule.

        制品仓库选择器，目前只支持repository且长度为1

        :param scope_selectors: The scope_selectors of this SignScopeRule.
        :type scope_selectors: dict(str, list[SignRuleSelector])
        """
        self._scope_selectors = scope_selectors

    @property
    def repo_scope_mode(self):
        r"""Gets the repo_scope_mode of this SignScopeRule.

        repository选择方式。可选regular、selection，前端显示需要，api调用时可选regular

        :return: The repo_scope_mode of this SignScopeRule.
        :rtype: str
        """
        return self._repo_scope_mode

    @repo_scope_mode.setter
    def repo_scope_mode(self, repo_scope_mode):
        r"""Sets the repo_scope_mode of this SignScopeRule.

        repository选择方式。可选regular、selection，前端显示需要，api调用时可选regular

        :param repo_scope_mode: The repo_scope_mode of this SignScopeRule.
        :type repo_scope_mode: str
        """
        self._repo_scope_mode = repo_scope_mode

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
        if not isinstance(other, SignScopeRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
