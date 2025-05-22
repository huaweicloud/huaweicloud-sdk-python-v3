# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogicalClusterPlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'str'
    }

    attribute_map = {
        'plan_id': 'plan_id'
    }

    def __init__(self, plan_id=None):
        r"""CreateLogicalClusterPlanResponse

        The model defined in huaweicloud sdk

        :param plan_id: **参数解释**： 逻辑集群增删计划ID。 **取值范围**： 不涉及。
        :type plan_id: str
        """
        
        super(CreateLogicalClusterPlanResponse, self).__init__()

        self._plan_id = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this CreateLogicalClusterPlanResponse.

        **参数解释**： 逻辑集群增删计划ID。 **取值范围**： 不涉及。

        :return: The plan_id of this CreateLogicalClusterPlanResponse.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this CreateLogicalClusterPlanResponse.

        **参数解释**： 逻辑集群增删计划ID。 **取值范围**： 不涉及。

        :param plan_id: The plan_id of this CreateLogicalClusterPlanResponse.
        :type plan_id: str
        """
        self._plan_id = plan_id

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
        if not isinstance(other, CreateLogicalClusterPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
