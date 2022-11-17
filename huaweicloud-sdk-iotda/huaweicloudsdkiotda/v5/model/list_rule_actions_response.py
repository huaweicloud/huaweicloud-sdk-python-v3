# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleActionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actions': 'list[RoutingRuleAction]',
        'count': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'count': 'count',
        'marker': 'marker'
    }

    def __init__(self, actions=None, count=None, marker=None):
        """ListRuleActionsResponse

        The model defined in huaweicloud sdk

        :param actions: 规则动作信息列表。
        :type actions: list[:class:`huaweicloudsdkiotda.v5.RoutingRuleAction`]
        :param count: 满足查询条件的记录总数。
        :type count: int
        :param marker: 本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。
        :type marker: str
        """
        
        super(ListRuleActionsResponse, self).__init__()

        self._actions = None
        self._count = None
        self._marker = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if count is not None:
            self.count = count
        if marker is not None:
            self.marker = marker

    @property
    def actions(self):
        """Gets the actions of this ListRuleActionsResponse.

        规则动作信息列表。

        :return: The actions of this ListRuleActionsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.RoutingRuleAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ListRuleActionsResponse.

        规则动作信息列表。

        :param actions: The actions of this ListRuleActionsResponse.
        :type actions: list[:class:`huaweicloudsdkiotda.v5.RoutingRuleAction`]
        """
        self._actions = actions

    @property
    def count(self):
        """Gets the count of this ListRuleActionsResponse.

        满足查询条件的记录总数。

        :return: The count of this ListRuleActionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRuleActionsResponse.

        满足查询条件的记录总数。

        :param count: The count of this ListRuleActionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def marker(self):
        """Gets the marker of this ListRuleActionsResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :return: The marker of this ListRuleActionsResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRuleActionsResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :param marker: The marker of this ListRuleActionsResponse.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListRuleActionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
