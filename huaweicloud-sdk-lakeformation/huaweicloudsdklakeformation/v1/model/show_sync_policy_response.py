# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSyncPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_version': 'int',
        'policy_update_time': 'str',
        'policies': 'list[Policy]',
        'policy_deltas': 'list[PolicyDelta]'
    }

    attribute_map = {
        'policy_version': 'policy_version',
        'policy_update_time': 'policy_updateTime',
        'policies': 'policies',
        'policy_deltas': 'policy_deltas'
    }

    def __init__(self, policy_version=None, policy_update_time=None, policies=None, policy_deltas=None):
        r"""ShowSyncPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_version: 策略版本
        :type policy_version: int
        :param policy_update_time: 策略更新时间
        :type policy_update_time: str
        :param policies: 权限策略信息
        :type policies: list[:class:`huaweicloudsdklakeformation.v1.Policy`]
        :param policy_deltas: 增量权限策略信息
        :type policy_deltas: list[:class:`huaweicloudsdklakeformation.v1.PolicyDelta`]
        """
        
        super(ShowSyncPolicyResponse, self).__init__()

        self._policy_version = None
        self._policy_update_time = None
        self._policies = None
        self._policy_deltas = None
        self.discriminator = None

        if policy_version is not None:
            self.policy_version = policy_version
        if policy_update_time is not None:
            self.policy_update_time = policy_update_time
        if policies is not None:
            self.policies = policies
        if policy_deltas is not None:
            self.policy_deltas = policy_deltas

    @property
    def policy_version(self):
        r"""Gets the policy_version of this ShowSyncPolicyResponse.

        策略版本

        :return: The policy_version of this ShowSyncPolicyResponse.
        :rtype: int
        """
        return self._policy_version

    @policy_version.setter
    def policy_version(self, policy_version):
        r"""Sets the policy_version of this ShowSyncPolicyResponse.

        策略版本

        :param policy_version: The policy_version of this ShowSyncPolicyResponse.
        :type policy_version: int
        """
        self._policy_version = policy_version

    @property
    def policy_update_time(self):
        r"""Gets the policy_update_time of this ShowSyncPolicyResponse.

        策略更新时间

        :return: The policy_update_time of this ShowSyncPolicyResponse.
        :rtype: str
        """
        return self._policy_update_time

    @policy_update_time.setter
    def policy_update_time(self, policy_update_time):
        r"""Sets the policy_update_time of this ShowSyncPolicyResponse.

        策略更新时间

        :param policy_update_time: The policy_update_time of this ShowSyncPolicyResponse.
        :type policy_update_time: str
        """
        self._policy_update_time = policy_update_time

    @property
    def policies(self):
        r"""Gets the policies of this ShowSyncPolicyResponse.

        权限策略信息

        :return: The policies of this ShowSyncPolicyResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ShowSyncPolicyResponse.

        权限策略信息

        :param policies: The policies of this ShowSyncPolicyResponse.
        :type policies: list[:class:`huaweicloudsdklakeformation.v1.Policy`]
        """
        self._policies = policies

    @property
    def policy_deltas(self):
        r"""Gets the policy_deltas of this ShowSyncPolicyResponse.

        增量权限策略信息

        :return: The policy_deltas of this ShowSyncPolicyResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyDelta`]
        """
        return self._policy_deltas

    @policy_deltas.setter
    def policy_deltas(self, policy_deltas):
        r"""Sets the policy_deltas of this ShowSyncPolicyResponse.

        增量权限策略信息

        :param policy_deltas: The policy_deltas of this ShowSyncPolicyResponse.
        :type policy_deltas: list[:class:`huaweicloudsdklakeformation.v1.PolicyDelta`]
        """
        self._policy_deltas = policy_deltas

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
        if not isinstance(other, ShowSyncPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
