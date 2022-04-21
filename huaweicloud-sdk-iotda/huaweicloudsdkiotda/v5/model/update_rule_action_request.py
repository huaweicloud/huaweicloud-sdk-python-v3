# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRuleActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'action_id': 'str',
        'body': 'UpdateActionReq'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'action_id': 'action_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, action_id=None, body=None):
        """UpdateRuleActionRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param action_id: **参数说明**：规则动作ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type action_id: str
        :param body: Body of the UpdateRuleActionRequest
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateActionReq`
        """
        
        

        self._instance_id = None
        self._action_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.action_id = action_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateRuleActionRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this UpdateRuleActionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateRuleActionRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this UpdateRuleActionRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def action_id(self):
        """Gets the action_id of this UpdateRuleActionRequest.

        **参数说明**：规则动作ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The action_id of this UpdateRuleActionRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this UpdateRuleActionRequest.

        **参数说明**：规则动作ID。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param action_id: The action_id of this UpdateRuleActionRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def body(self):
        """Gets the body of this UpdateRuleActionRequest.


        :return: The body of this UpdateRuleActionRequest.
        :rtype: :class:`huaweicloudsdkiotda.v5.UpdateActionReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRuleActionRequest.


        :param body: The body of this UpdateRuleActionRequest.
        :type body: :class:`huaweicloudsdkiotda.v5.UpdateActionReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateRuleActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
