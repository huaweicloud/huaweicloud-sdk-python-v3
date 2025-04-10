# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityResourcePermissionPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'policy_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'policy_id': 'policy_id'
    }

    def __init__(self, workspace=None, policy_id=None):
        r"""ShowSecurityResourcePermissionPolicyRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param policy_id: 空间资源权限策略id。
        :type policy_id: str
        """
        
        

        self._workspace = None
        self._policy_id = None
        self.discriminator = None

        self.workspace = workspace
        self.policy_id = policy_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowSecurityResourcePermissionPolicyRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowSecurityResourcePermissionPolicyRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowSecurityResourcePermissionPolicyRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowSecurityResourcePermissionPolicyRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowSecurityResourcePermissionPolicyRequest.

        空间资源权限策略id。

        :return: The policy_id of this ShowSecurityResourcePermissionPolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowSecurityResourcePermissionPolicyRequest.

        空间资源权限策略id。

        :param policy_id: The policy_id of this ShowSecurityResourcePermissionPolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, ShowSecurityResourcePermissionPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
