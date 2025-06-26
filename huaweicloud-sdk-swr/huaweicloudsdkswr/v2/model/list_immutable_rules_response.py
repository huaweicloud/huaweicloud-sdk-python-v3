# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImmutableRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'immutable_rules': 'list[ImmutableRule]',
        'total': 'int'
    }

    attribute_map = {
        'immutable_rules': 'immutable_rules',
        'total': 'total'
    }

    def __init__(self, immutable_rules=None, total=None):
        r"""ListImmutableRulesResponse

        The model defined in huaweicloud sdk

        :param immutable_rules: 策略列表
        :type immutable_rules: list[:class:`huaweicloudsdkswr.v2.ImmutableRule`]
        :param total: 策略总数
        :type total: int
        """
        
        super(ListImmutableRulesResponse, self).__init__()

        self._immutable_rules = None
        self._total = None
        self.discriminator = None

        if immutable_rules is not None:
            self.immutable_rules = immutable_rules
        if total is not None:
            self.total = total

    @property
    def immutable_rules(self):
        r"""Gets the immutable_rules of this ListImmutableRulesResponse.

        策略列表

        :return: The immutable_rules of this ListImmutableRulesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ImmutableRule`]
        """
        return self._immutable_rules

    @immutable_rules.setter
    def immutable_rules(self, immutable_rules):
        r"""Sets the immutable_rules of this ListImmutableRulesResponse.

        策略列表

        :param immutable_rules: The immutable_rules of this ListImmutableRulesResponse.
        :type immutable_rules: list[:class:`huaweicloudsdkswr.v2.ImmutableRule`]
        """
        self._immutable_rules = immutable_rules

    @property
    def total(self):
        r"""Gets the total of this ListImmutableRulesResponse.

        策略总数

        :return: The total of this ListImmutableRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListImmutableRulesResponse.

        策略总数

        :param total: The total of this ListImmutableRulesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListImmutableRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
