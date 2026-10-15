# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataFilterRulesResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'rules': 'list[DataFilterRuleResp]',
        'status': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'rules': 'rules',
        'status': 'status'
    }

    def __init__(self, total_count=None, rules=None, status=None):
        r"""ShowDataFilterRulesResultResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param rules: 数据过滤规则列表。
        :type rules: list[:class:`huaweicloudsdkdrs.v5.DataFilterRuleResp`]
        :param status: 查询过滤规则进度。
        :type status: str
        """
        
        super().__init__()

        self._total_count = None
        self._rules = None
        self._status = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if rules is not None:
            self.rules = rules
        if status is not None:
            self.status = status

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowDataFilterRulesResultResponse.

        总数。

        :return: The total_count of this ShowDataFilterRulesResultResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowDataFilterRulesResultResponse.

        总数。

        :param total_count: The total_count of this ShowDataFilterRulesResultResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def rules(self):
        r"""Gets the rules of this ShowDataFilterRulesResultResponse.

        数据过滤规则列表。

        :return: The rules of this ShowDataFilterRulesResultResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataFilterRuleResp`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ShowDataFilterRulesResultResponse.

        数据过滤规则列表。

        :param rules: The rules of this ShowDataFilterRulesResultResponse.
        :type rules: list[:class:`huaweicloudsdkdrs.v5.DataFilterRuleResp`]
        """
        self._rules = rules

    @property
    def status(self):
        r"""Gets the status of this ShowDataFilterRulesResultResponse.

        查询过滤规则进度。

        :return: The status of this ShowDataFilterRulesResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDataFilterRulesResultResponse.

        查询过滤规则进度。

        :param status: The status of this ShowDataFilterRulesResultResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("ShowDataFilterRulesResultResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDataFilterRulesResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
