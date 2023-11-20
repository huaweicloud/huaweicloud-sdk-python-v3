# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceIpRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'rules': 'list[TransferRuleInfo]'
    }

    attribute_map = {
        'total': 'total',
        'rules': 'rules'
    }

    def __init__(self, total=None, rules=None):
        """ListInstanceIpRuleResponse

        The model defined in huaweicloud sdk

        :param total: 转发规则总数
        :type total: int
        :param rules: 转发规则列表
        :type rules: list[:class:`huaweicloudsdkaad.v1.TransferRuleInfo`]
        """
        
        super(ListInstanceIpRuleResponse, self).__init__()

        self._total = None
        self._rules = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if rules is not None:
            self.rules = rules

    @property
    def total(self):
        """Gets the total of this ListInstanceIpRuleResponse.

        转发规则总数

        :return: The total of this ListInstanceIpRuleResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceIpRuleResponse.

        转发规则总数

        :param total: The total of this ListInstanceIpRuleResponse.
        :type total: int
        """
        self._total = total

    @property
    def rules(self):
        """Gets the rules of this ListInstanceIpRuleResponse.

        转发规则列表

        :return: The rules of this ListInstanceIpRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaad.v1.TransferRuleInfo`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ListInstanceIpRuleResponse.

        转发规则列表

        :param rules: The rules of this ListInstanceIpRuleResponse.
        :type rules: list[:class:`huaweicloudsdkaad.v1.TransferRuleInfo`]
        """
        self._rules = rules

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
        if not isinstance(other, ListInstanceIpRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other