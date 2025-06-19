# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlJobDefendRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[SqlJobDefendRule]',
        'total_count': 'int'
    }

    attribute_map = {
        'rules': 'rules',
        'total_count': 'total_count'
    }

    def __init__(self, rules=None, total_count=None):
        r"""ListSqlJobDefendRulesResponse

        The model defined in huaweicloud sdk

        :param rules: 用户自定义规则信息。
        :type rules: list[:class:`huaweicloudsdkdli.v1.SqlJobDefendRule`]
        :param total_count: 总个数。
        :type total_count: int
        """
        
        super(ListSqlJobDefendRulesResponse, self).__init__()

        self._rules = None
        self._total_count = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if total_count is not None:
            self.total_count = total_count

    @property
    def rules(self):
        r"""Gets the rules of this ListSqlJobDefendRulesResponse.

        用户自定义规则信息。

        :return: The rules of this ListSqlJobDefendRulesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.SqlJobDefendRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListSqlJobDefendRulesResponse.

        用户自定义规则信息。

        :param rules: The rules of this ListSqlJobDefendRulesResponse.
        :type rules: list[:class:`huaweicloudsdkdli.v1.SqlJobDefendRule`]
        """
        self._rules = rules

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSqlJobDefendRulesResponse.

        总个数。

        :return: The total_count of this ListSqlJobDefendRulesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSqlJobDefendRulesResponse.

        总个数。

        :param total_count: The total_count of this ListSqlJobDefendRulesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListSqlJobDefendRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
