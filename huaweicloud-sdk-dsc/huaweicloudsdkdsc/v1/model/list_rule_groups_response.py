# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleGroupsResponse(SdkResponse):

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
        'groups': 'list[ResponseGroup]'
    }

    attribute_map = {
        'total': 'total',
        'groups': 'groups'
    }

    def __init__(self, total=None, groups=None):
        r"""ListRuleGroupsResponse

        The model defined in huaweicloud sdk

        :param total: 规则组总数
        :type total: int
        :param groups: 规则组列表
        :type groups: list[:class:`huaweicloudsdkdsc.v1.ResponseGroup`]
        """
        
        super(ListRuleGroupsResponse, self).__init__()

        self._total = None
        self._groups = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if groups is not None:
            self.groups = groups

    @property
    def total(self):
        r"""Gets the total of this ListRuleGroupsResponse.

        规则组总数

        :return: The total of this ListRuleGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRuleGroupsResponse.

        规则组总数

        :param total: The total of this ListRuleGroupsResponse.
        :type total: int
        """
        self._total = total

    @property
    def groups(self):
        r"""Gets the groups of this ListRuleGroupsResponse.

        规则组列表

        :return: The groups of this ListRuleGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.ResponseGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ListRuleGroupsResponse.

        规则组列表

        :param groups: The groups of this ListRuleGroupsResponse.
        :type groups: list[:class:`huaweicloudsdkdsc.v1.ResponseGroup`]
        """
        self._groups = groups

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
        if not isinstance(other, ListRuleGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
