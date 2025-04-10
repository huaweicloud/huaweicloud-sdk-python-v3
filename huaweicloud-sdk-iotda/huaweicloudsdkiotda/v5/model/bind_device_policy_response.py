# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindDevicePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'target_type': 'str',
        'success_targets': 'list[str]',
        'failure_targets': 'list[DevicePolicyBindOrUnbindFailureDetail]'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'target_type': 'target_type',
        'success_targets': 'success_targets',
        'failure_targets': 'failure_targets'
    }

    def __init__(self, policy_id=None, target_type=None, success_targets=None, failure_targets=None):
        r"""BindDevicePolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID。
        :type policy_id: str
        :param target_type: **参数说明**：策略的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。
        :type target_type: str
        :param success_targets: 成功的目标id列表。
        :type success_targets: list[str]
        :param failure_targets: 失败的目标id列表 
        :type failure_targets: list[:class:`huaweicloudsdkiotda.v5.DevicePolicyBindOrUnbindFailureDetail`]
        """
        
        super(BindDevicePolicyResponse, self).__init__()

        self._policy_id = None
        self._target_type = None
        self._success_targets = None
        self._failure_targets = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if target_type is not None:
            self.target_type = target_type
        if success_targets is not None:
            self.success_targets = success_targets
        if failure_targets is not None:
            self.failure_targets = failure_targets

    @property
    def policy_id(self):
        r"""Gets the policy_id of this BindDevicePolicyResponse.

        策略ID。

        :return: The policy_id of this BindDevicePolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this BindDevicePolicyResponse.

        策略ID。

        :param policy_id: The policy_id of this BindDevicePolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def target_type(self):
        r"""Gets the target_type of this BindDevicePolicyResponse.

        **参数说明**：策略的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。

        :return: The target_type of this BindDevicePolicyResponse.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this BindDevicePolicyResponse.

        **参数说明**：策略的目标类型。 **取值范围**：device|product|app，device表示设备，product表示产品，app表示整个资源空间。

        :param target_type: The target_type of this BindDevicePolicyResponse.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def success_targets(self):
        r"""Gets the success_targets of this BindDevicePolicyResponse.

        成功的目标id列表。

        :return: The success_targets of this BindDevicePolicyResponse.
        :rtype: list[str]
        """
        return self._success_targets

    @success_targets.setter
    def success_targets(self, success_targets):
        r"""Sets the success_targets of this BindDevicePolicyResponse.

        成功的目标id列表。

        :param success_targets: The success_targets of this BindDevicePolicyResponse.
        :type success_targets: list[str]
        """
        self._success_targets = success_targets

    @property
    def failure_targets(self):
        r"""Gets the failure_targets of this BindDevicePolicyResponse.

        失败的目标id列表 

        :return: The failure_targets of this BindDevicePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.DevicePolicyBindOrUnbindFailureDetail`]
        """
        return self._failure_targets

    @failure_targets.setter
    def failure_targets(self, failure_targets):
        r"""Sets the failure_targets of this BindDevicePolicyResponse.

        失败的目标id列表 

        :param failure_targets: The failure_targets of this BindDevicePolicyResponse.
        :type failure_targets: list[:class:`huaweicloudsdkiotda.v5.DevicePolicyBindOrUnbindFailureDetail`]
        """
        self._failure_targets = failure_targets

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
        if not isinstance(other, BindDevicePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
