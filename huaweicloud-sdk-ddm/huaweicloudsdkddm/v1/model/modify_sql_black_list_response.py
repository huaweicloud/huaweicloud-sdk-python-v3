# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifySqlBlackListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_black_list_full_check': 'str',
        'sql_black_list_prefix_check': 'str',
        'sql_black_list_regex_check': 'str'
    }

    attribute_map = {
        'sql_black_list_full_check': 'sql_black_list_full_check',
        'sql_black_list_prefix_check': 'sql_black_list_prefix_check',
        'sql_black_list_regex_check': 'sql_black_list_regex_check'
    }

    def __init__(self, sql_black_list_full_check=None, sql_black_list_prefix_check=None, sql_black_list_regex_check=None):
        r"""ModifySqlBlackListResponse

        The model defined in huaweicloud sdk

        :param sql_black_list_full_check: **参数解释**：  全量匹配sql黑名单。  **参数范围**：  不涉及。
        :type sql_black_list_full_check: str
        :param sql_black_list_prefix_check: **参数解释**：  前缀匹配sql黑名单。  **参数范围**：  不涉及。
        :type sql_black_list_prefix_check: str
        :param sql_black_list_regex_check: **参数解释**：  正则匹配sql黑名单。  **参数范围**：  不涉及。
        :type sql_black_list_regex_check: str
        """
        
        super().__init__()

        self._sql_black_list_full_check = None
        self._sql_black_list_prefix_check = None
        self._sql_black_list_regex_check = None
        self.discriminator = None

        if sql_black_list_full_check is not None:
            self.sql_black_list_full_check = sql_black_list_full_check
        if sql_black_list_prefix_check is not None:
            self.sql_black_list_prefix_check = sql_black_list_prefix_check
        if sql_black_list_regex_check is not None:
            self.sql_black_list_regex_check = sql_black_list_regex_check

    @property
    def sql_black_list_full_check(self):
        r"""Gets the sql_black_list_full_check of this ModifySqlBlackListResponse.

        **参数解释**：  全量匹配sql黑名单。  **参数范围**：  不涉及。

        :return: The sql_black_list_full_check of this ModifySqlBlackListResponse.
        :rtype: str
        """
        return self._sql_black_list_full_check

    @sql_black_list_full_check.setter
    def sql_black_list_full_check(self, sql_black_list_full_check):
        r"""Sets the sql_black_list_full_check of this ModifySqlBlackListResponse.

        **参数解释**：  全量匹配sql黑名单。  **参数范围**：  不涉及。

        :param sql_black_list_full_check: The sql_black_list_full_check of this ModifySqlBlackListResponse.
        :type sql_black_list_full_check: str
        """
        self._sql_black_list_full_check = sql_black_list_full_check

    @property
    def sql_black_list_prefix_check(self):
        r"""Gets the sql_black_list_prefix_check of this ModifySqlBlackListResponse.

        **参数解释**：  前缀匹配sql黑名单。  **参数范围**：  不涉及。

        :return: The sql_black_list_prefix_check of this ModifySqlBlackListResponse.
        :rtype: str
        """
        return self._sql_black_list_prefix_check

    @sql_black_list_prefix_check.setter
    def sql_black_list_prefix_check(self, sql_black_list_prefix_check):
        r"""Sets the sql_black_list_prefix_check of this ModifySqlBlackListResponse.

        **参数解释**：  前缀匹配sql黑名单。  **参数范围**：  不涉及。

        :param sql_black_list_prefix_check: The sql_black_list_prefix_check of this ModifySqlBlackListResponse.
        :type sql_black_list_prefix_check: str
        """
        self._sql_black_list_prefix_check = sql_black_list_prefix_check

    @property
    def sql_black_list_regex_check(self):
        r"""Gets the sql_black_list_regex_check of this ModifySqlBlackListResponse.

        **参数解释**：  正则匹配sql黑名单。  **参数范围**：  不涉及。

        :return: The sql_black_list_regex_check of this ModifySqlBlackListResponse.
        :rtype: str
        """
        return self._sql_black_list_regex_check

    @sql_black_list_regex_check.setter
    def sql_black_list_regex_check(self, sql_black_list_regex_check):
        r"""Sets the sql_black_list_regex_check of this ModifySqlBlackListResponse.

        **参数解释**：  正则匹配sql黑名单。  **参数范围**：  不涉及。

        :param sql_black_list_regex_check: The sql_black_list_regex_check of this ModifySqlBlackListResponse.
        :type sql_black_list_regex_check: str
        """
        self._sql_black_list_regex_check = sql_black_list_regex_check

    def to_dict(self):
        import warnings
        warnings.warn("ModifySqlBlackListResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ModifySqlBlackListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
