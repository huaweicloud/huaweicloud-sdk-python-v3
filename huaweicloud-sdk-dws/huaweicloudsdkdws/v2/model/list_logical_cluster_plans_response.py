# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogicalClusterPlansResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plans': 'list[LogicalClusterPlanVo]'
    }

    attribute_map = {
        'plans': 'plans'
    }

    def __init__(self, plans=None):
        r"""ListLogicalClusterPlansResponse

        The model defined in huaweicloud sdk

        :param plans: **参数解释**： 逻辑集群增删计划对象列表。列表最大返回一般不超过20条。 **取值范围**： 不涉及。
        :type plans: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanVo`]
        """
        
        super(ListLogicalClusterPlansResponse, self).__init__()

        self._plans = None
        self.discriminator = None

        if plans is not None:
            self.plans = plans

    @property
    def plans(self):
        r"""Gets the plans of this ListLogicalClusterPlansResponse.

        **参数解释**： 逻辑集群增删计划对象列表。列表最大返回一般不超过20条。 **取值范围**： 不涉及。

        :return: The plans of this ListLogicalClusterPlansResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanVo`]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        r"""Sets the plans of this ListLogicalClusterPlansResponse.

        **参数解释**： 逻辑集群增删计划对象列表。列表最大返回一般不超过20条。 **取值范围**： 不涉及。

        :param plans: The plans of this ListLogicalClusterPlansResponse.
        :type plans: list[:class:`huaweicloudsdkdws.v2.LogicalClusterPlanVo`]
        """
        self._plans = plans

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
        if not isinstance(other, ListLogicalClusterPlansResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
