# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportRuleSecrecyLevelDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'builtin_rule_id': 'str',
        'secrecy_level': 'str'
    }

    attribute_map = {
        'builtin_rule_id': 'builtin_rule_id',
        'secrecy_level': 'secrecy_level'
    }

    def __init__(self, builtin_rule_id=None, secrecy_level=None):
        r"""ImportRuleSecrecyLevelDto

        The model defined in huaweicloud sdk

        :param builtin_rule_id: 内置规则模板id。
        :type builtin_rule_id: str
        :param secrecy_level: 密级id，获取方法请参见[获取数据密级](ListSecuritySecrecyLevels.xml)。
        :type secrecy_level: str
        """
        
        

        self._builtin_rule_id = None
        self._secrecy_level = None
        self.discriminator = None

        if builtin_rule_id is not None:
            self.builtin_rule_id = builtin_rule_id
        if secrecy_level is not None:
            self.secrecy_level = secrecy_level

    @property
    def builtin_rule_id(self):
        r"""Gets the builtin_rule_id of this ImportRuleSecrecyLevelDto.

        内置规则模板id。

        :return: The builtin_rule_id of this ImportRuleSecrecyLevelDto.
        :rtype: str
        """
        return self._builtin_rule_id

    @builtin_rule_id.setter
    def builtin_rule_id(self, builtin_rule_id):
        r"""Sets the builtin_rule_id of this ImportRuleSecrecyLevelDto.

        内置规则模板id。

        :param builtin_rule_id: The builtin_rule_id of this ImportRuleSecrecyLevelDto.
        :type builtin_rule_id: str
        """
        self._builtin_rule_id = builtin_rule_id

    @property
    def secrecy_level(self):
        r"""Gets the secrecy_level of this ImportRuleSecrecyLevelDto.

        密级id，获取方法请参见[获取数据密级](ListSecuritySecrecyLevels.xml)。

        :return: The secrecy_level of this ImportRuleSecrecyLevelDto.
        :rtype: str
        """
        return self._secrecy_level

    @secrecy_level.setter
    def secrecy_level(self, secrecy_level):
        r"""Sets the secrecy_level of this ImportRuleSecrecyLevelDto.

        密级id，获取方法请参见[获取数据密级](ListSecuritySecrecyLevels.xml)。

        :param secrecy_level: The secrecy_level of this ImportRuleSecrecyLevelDto.
        :type secrecy_level: str
        """
        self._secrecy_level = secrecy_level

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
        if not isinstance(other, ImportRuleSecrecyLevelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
