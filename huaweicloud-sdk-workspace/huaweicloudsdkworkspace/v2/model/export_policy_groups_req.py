# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportPolicyGroupsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_ids': 'list[str]'
    }

    attribute_map = {
        'policy_group_ids': 'policy_group_ids'
    }

    def __init__(self, policy_group_ids=None):
        r"""ExportPolicyGroupsReq

        The model defined in huaweicloud sdk

        :param policy_group_ids: 导出策略组的id列表。
        :type policy_group_ids: list[str]
        """
        
        

        self._policy_group_ids = None
        self.discriminator = None

        self.policy_group_ids = policy_group_ids

    @property
    def policy_group_ids(self):
        r"""Gets the policy_group_ids of this ExportPolicyGroupsReq.

        导出策略组的id列表。

        :return: The policy_group_ids of this ExportPolicyGroupsReq.
        :rtype: list[str]
        """
        return self._policy_group_ids

    @policy_group_ids.setter
    def policy_group_ids(self, policy_group_ids):
        r"""Sets the policy_group_ids of this ExportPolicyGroupsReq.

        导出策略组的id列表。

        :param policy_group_ids: The policy_group_ids of this ExportPolicyGroupsReq.
        :type policy_group_ids: list[str]
        """
        self._policy_group_ids = policy_group_ids

    def to_dict(self):
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
        if not isinstance(other, ExportPolicyGroupsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
