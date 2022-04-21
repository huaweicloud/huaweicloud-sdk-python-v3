# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchPauseScalingPoliciesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_policy_id': 'list[str]',
        'force_delete': 'str',
        'action': 'str',
        'delete_alarm': 'str'
    }

    attribute_map = {
        'scaling_policy_id': 'scaling_policy_id',
        'force_delete': 'force_delete',
        'action': 'action',
        'delete_alarm': 'delete_alarm'
    }

    def __init__(self, scaling_policy_id=None, force_delete=None, action=None, delete_alarm=None):
        """BatchPauseScalingPoliciesOption

        The model defined in huaweicloud sdk

        :param scaling_policy_id: 伸缩策略ID。
        :type scaling_policy_id: list[str]
        :param force_delete: 是否强制删除伸缩策略。默认为no，可选值为yes或no。只有action为delete时，该字段才生效。
        :type force_delete: str
        :param action: 批量操作伸缩策略action标识：删除：delete。启用：resume。停止：pause。
        :type action: str
        :param delete_alarm: 是否删除告警策略使用的告警规则。可选值为yes或no，默认为no。  只有action为delete时，该字段才生效。
        :type delete_alarm: str
        """
        
        

        self._scaling_policy_id = None
        self._force_delete = None
        self._action = None
        self._delete_alarm = None
        self.discriminator = None

        self.scaling_policy_id = scaling_policy_id
        if force_delete is not None:
            self.force_delete = force_delete
        self.action = action
        if delete_alarm is not None:
            self.delete_alarm = delete_alarm

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this BatchPauseScalingPoliciesOption.

        伸缩策略ID。

        :return: The scaling_policy_id of this BatchPauseScalingPoliciesOption.
        :rtype: list[str]
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this BatchPauseScalingPoliciesOption.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this BatchPauseScalingPoliciesOption.
        :type scaling_policy_id: list[str]
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def force_delete(self):
        """Gets the force_delete of this BatchPauseScalingPoliciesOption.

        是否强制删除伸缩策略。默认为no，可选值为yes或no。只有action为delete时，该字段才生效。

        :return: The force_delete of this BatchPauseScalingPoliciesOption.
        :rtype: str
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this BatchPauseScalingPoliciesOption.

        是否强制删除伸缩策略。默认为no，可选值为yes或no。只有action为delete时，该字段才生效。

        :param force_delete: The force_delete of this BatchPauseScalingPoliciesOption.
        :type force_delete: str
        """
        self._force_delete = force_delete

    @property
    def action(self):
        """Gets the action of this BatchPauseScalingPoliciesOption.

        批量操作伸缩策略action标识：删除：delete。启用：resume。停止：pause。

        :return: The action of this BatchPauseScalingPoliciesOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchPauseScalingPoliciesOption.

        批量操作伸缩策略action标识：删除：delete。启用：resume。停止：pause。

        :param action: The action of this BatchPauseScalingPoliciesOption.
        :type action: str
        """
        self._action = action

    @property
    def delete_alarm(self):
        """Gets the delete_alarm of this BatchPauseScalingPoliciesOption.

        是否删除告警策略使用的告警规则。可选值为yes或no，默认为no。  只有action为delete时，该字段才生效。

        :return: The delete_alarm of this BatchPauseScalingPoliciesOption.
        :rtype: str
        """
        return self._delete_alarm

    @delete_alarm.setter
    def delete_alarm(self, delete_alarm):
        """Sets the delete_alarm of this BatchPauseScalingPoliciesOption.

        是否删除告警策略使用的告警规则。可选值为yes或no，默认为no。  只有action为delete时，该字段才生效。

        :param delete_alarm: The delete_alarm of this BatchPauseScalingPoliciesOption.
        :type delete_alarm: str
        """
        self._delete_alarm = delete_alarm

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
        if not isinstance(other, BatchPauseScalingPoliciesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
