# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateScalingPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'max_scaling_amount': 'int',
        'single_expansion_count': 'int',
        'scaling_policy_by_session': 'ScalingPolicyBySession'
    }

    attribute_map = {
        'enable': 'enable',
        'max_scaling_amount': 'max_scaling_amount',
        'single_expansion_count': 'single_expansion_count',
        'scaling_policy_by_session': 'scaling_policy_by_session'
    }

    def __init__(self, enable=None, max_scaling_amount=None, single_expansion_count=None, scaling_policy_by_session=None):
        r"""CreateOrUpdateScalingPolicyResponse

        The model defined in huaweicloud sdk

        :param enable: 是否启用策略,默认启用： &#39;true&#39;: 启用 &#39;false&#39;: 禁用
        :type enable: bool
        :param max_scaling_amount: 最大扩容数量。
        :type max_scaling_amount: int
        :param single_expansion_count: 单次扩容数量。
        :type single_expansion_count: int
        :param scaling_policy_by_session: 
        :type scaling_policy_by_session: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        """
        
        super(CreateOrUpdateScalingPolicyResponse, self).__init__()

        self._enable = None
        self._max_scaling_amount = None
        self._single_expansion_count = None
        self._scaling_policy_by_session = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if max_scaling_amount is not None:
            self.max_scaling_amount = max_scaling_amount
        if single_expansion_count is not None:
            self.single_expansion_count = single_expansion_count
        if scaling_policy_by_session is not None:
            self.scaling_policy_by_session = scaling_policy_by_session

    @property
    def enable(self):
        r"""Gets the enable of this CreateOrUpdateScalingPolicyResponse.

        是否启用策略,默认启用： 'true': 启用 'false': 禁用

        :return: The enable of this CreateOrUpdateScalingPolicyResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateOrUpdateScalingPolicyResponse.

        是否启用策略,默认启用： 'true': 启用 'false': 禁用

        :param enable: The enable of this CreateOrUpdateScalingPolicyResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def max_scaling_amount(self):
        r"""Gets the max_scaling_amount of this CreateOrUpdateScalingPolicyResponse.

        最大扩容数量。

        :return: The max_scaling_amount of this CreateOrUpdateScalingPolicyResponse.
        :rtype: int
        """
        return self._max_scaling_amount

    @max_scaling_amount.setter
    def max_scaling_amount(self, max_scaling_amount):
        r"""Sets the max_scaling_amount of this CreateOrUpdateScalingPolicyResponse.

        最大扩容数量。

        :param max_scaling_amount: The max_scaling_amount of this CreateOrUpdateScalingPolicyResponse.
        :type max_scaling_amount: int
        """
        self._max_scaling_amount = max_scaling_amount

    @property
    def single_expansion_count(self):
        r"""Gets the single_expansion_count of this CreateOrUpdateScalingPolicyResponse.

        单次扩容数量。

        :return: The single_expansion_count of this CreateOrUpdateScalingPolicyResponse.
        :rtype: int
        """
        return self._single_expansion_count

    @single_expansion_count.setter
    def single_expansion_count(self, single_expansion_count):
        r"""Sets the single_expansion_count of this CreateOrUpdateScalingPolicyResponse.

        单次扩容数量。

        :param single_expansion_count: The single_expansion_count of this CreateOrUpdateScalingPolicyResponse.
        :type single_expansion_count: int
        """
        self._single_expansion_count = single_expansion_count

    @property
    def scaling_policy_by_session(self):
        r"""Gets the scaling_policy_by_session of this CreateOrUpdateScalingPolicyResponse.

        :return: The scaling_policy_by_session of this CreateOrUpdateScalingPolicyResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        """
        return self._scaling_policy_by_session

    @scaling_policy_by_session.setter
    def scaling_policy_by_session(self, scaling_policy_by_session):
        r"""Sets the scaling_policy_by_session of this CreateOrUpdateScalingPolicyResponse.

        :param scaling_policy_by_session: The scaling_policy_by_session of this CreateOrUpdateScalingPolicyResponse.
        :type scaling_policy_by_session: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        """
        self._scaling_policy_by_session = scaling_policy_by_session

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
        if not isinstance(other, CreateOrUpdateScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
