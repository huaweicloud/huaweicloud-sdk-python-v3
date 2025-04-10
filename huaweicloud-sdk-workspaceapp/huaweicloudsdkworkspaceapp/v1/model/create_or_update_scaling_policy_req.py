# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrUpdateScalingPolicyReq:

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
        'scaling_policy_by_session': 'ScalingPolicyBySession',
        'server_group_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'max_scaling_amount': 'max_scaling_amount',
        'single_expansion_count': 'single_expansion_count',
        'scaling_policy_by_session': 'scaling_policy_by_session',
        'server_group_id': 'server_group_id'
    }

    def __init__(self, enable=None, max_scaling_amount=None, single_expansion_count=None, scaling_policy_by_session=None, server_group_id=None):
        r"""CreateOrUpdateScalingPolicyReq

        The model defined in huaweicloud sdk

        :param enable: 是否启用策略,默认启用： &#39;true&#39;: 启用 &#39;false&#39;: 禁用
        :type enable: bool
        :param max_scaling_amount: 最大扩容数量。
        :type max_scaling_amount: int
        :param single_expansion_count: 单次扩容数量。
        :type single_expansion_count: int
        :param scaling_policy_by_session: 
        :type scaling_policy_by_session: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        :param server_group_id: 服务器组唯一标识(仅按需服务器组支持该操作)。
        :type server_group_id: str
        """
        
        

        self._enable = None
        self._max_scaling_amount = None
        self._single_expansion_count = None
        self._scaling_policy_by_session = None
        self._server_group_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        self.max_scaling_amount = max_scaling_amount
        self.single_expansion_count = single_expansion_count
        self.scaling_policy_by_session = scaling_policy_by_session
        self.server_group_id = server_group_id

    @property
    def enable(self):
        r"""Gets the enable of this CreateOrUpdateScalingPolicyReq.

        是否启用策略,默认启用： 'true': 启用 'false': 禁用

        :return: The enable of this CreateOrUpdateScalingPolicyReq.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this CreateOrUpdateScalingPolicyReq.

        是否启用策略,默认启用： 'true': 启用 'false': 禁用

        :param enable: The enable of this CreateOrUpdateScalingPolicyReq.
        :type enable: bool
        """
        self._enable = enable

    @property
    def max_scaling_amount(self):
        r"""Gets the max_scaling_amount of this CreateOrUpdateScalingPolicyReq.

        最大扩容数量。

        :return: The max_scaling_amount of this CreateOrUpdateScalingPolicyReq.
        :rtype: int
        """
        return self._max_scaling_amount

    @max_scaling_amount.setter
    def max_scaling_amount(self, max_scaling_amount):
        r"""Sets the max_scaling_amount of this CreateOrUpdateScalingPolicyReq.

        最大扩容数量。

        :param max_scaling_amount: The max_scaling_amount of this CreateOrUpdateScalingPolicyReq.
        :type max_scaling_amount: int
        """
        self._max_scaling_amount = max_scaling_amount

    @property
    def single_expansion_count(self):
        r"""Gets the single_expansion_count of this CreateOrUpdateScalingPolicyReq.

        单次扩容数量。

        :return: The single_expansion_count of this CreateOrUpdateScalingPolicyReq.
        :rtype: int
        """
        return self._single_expansion_count

    @single_expansion_count.setter
    def single_expansion_count(self, single_expansion_count):
        r"""Sets the single_expansion_count of this CreateOrUpdateScalingPolicyReq.

        单次扩容数量。

        :param single_expansion_count: The single_expansion_count of this CreateOrUpdateScalingPolicyReq.
        :type single_expansion_count: int
        """
        self._single_expansion_count = single_expansion_count

    @property
    def scaling_policy_by_session(self):
        r"""Gets the scaling_policy_by_session of this CreateOrUpdateScalingPolicyReq.

        :return: The scaling_policy_by_session of this CreateOrUpdateScalingPolicyReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        """
        return self._scaling_policy_by_session

    @scaling_policy_by_session.setter
    def scaling_policy_by_session(self, scaling_policy_by_session):
        r"""Sets the scaling_policy_by_session of this CreateOrUpdateScalingPolicyReq.

        :param scaling_policy_by_session: The scaling_policy_by_session of this CreateOrUpdateScalingPolicyReq.
        :type scaling_policy_by_session: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicyBySession`
        """
        self._scaling_policy_by_session = scaling_policy_by_session

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this CreateOrUpdateScalingPolicyReq.

        服务器组唯一标识(仅按需服务器组支持该操作)。

        :return: The server_group_id of this CreateOrUpdateScalingPolicyReq.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this CreateOrUpdateScalingPolicyReq.

        服务器组唯一标识(仅按需服务器组支持该操作)。

        :param server_group_id: The server_group_id of this CreateOrUpdateScalingPolicyReq.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

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
        if not isinstance(other, CreateOrUpdateScalingPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
