# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAutoSqlLimitingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_sql_limiting_rules': 'list[AutoSqlLimitingRule]'
    }

    attribute_map = {
        'auto_sql_limiting_rules': 'auto_sql_limiting_rules'
    }

    def __init__(self, auto_sql_limiting_rules=None):
        r"""SetAutoSqlLimitingReq

        The model defined in huaweicloud sdk

        :param auto_sql_limiting_rules: **参数解释**：  开启自治限流规则。  **约束限制**：  不涉及。
        :type auto_sql_limiting_rules: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingRule`]
        """
        
        

        self._auto_sql_limiting_rules = None
        self.discriminator = None

        self.auto_sql_limiting_rules = auto_sql_limiting_rules

    @property
    def auto_sql_limiting_rules(self):
        r"""Gets the auto_sql_limiting_rules of this SetAutoSqlLimitingReq.

        **参数解释**：  开启自治限流规则。  **约束限制**：  不涉及。

        :return: The auto_sql_limiting_rules of this SetAutoSqlLimitingReq.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingRule`]
        """
        return self._auto_sql_limiting_rules

    @auto_sql_limiting_rules.setter
    def auto_sql_limiting_rules(self, auto_sql_limiting_rules):
        r"""Sets the auto_sql_limiting_rules of this SetAutoSqlLimitingReq.

        **参数解释**：  开启自治限流规则。  **约束限制**：  不涉及。

        :param auto_sql_limiting_rules: The auto_sql_limiting_rules of this SetAutoSqlLimitingReq.
        :type auto_sql_limiting_rules: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingRule`]
        """
        self._auto_sql_limiting_rules = auto_sql_limiting_rules

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetAutoSqlLimitingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
