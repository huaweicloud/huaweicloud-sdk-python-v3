# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoliciesOfPolicyGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_id': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'policy_type': 'policy_type'
    }

    def __init__(self, policy_group_id=None, policy_type=None):
        r"""ListPoliciesOfPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组id。
        :type policy_group_id: str
        :param policy_type: 根据策略类型过滤结果，不传则查询所有策略。 可选类型: - 外设：Peripherals; - 音频：Audio; - 客户端：Client; - 显示：Display; - 文件与剪切板：FileAndClip; - 接入控制：ClientAccessControl; - 会话：SessionAutoDisconnect; - 虚拟通道：VirtualChannel - 水印：Watermark; - 键盘鼠标：KeyboardAndMouse; - 通用音视频旁路：Seamless。 - 录屏审计：RecordAudit。
        :type policy_type: str
        """
        
        

        self._policy_group_id = None
        self._policy_type = None
        self.discriminator = None

        self.policy_group_id = policy_group_id
        if policy_type is not None:
            self.policy_type = policy_type

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListPoliciesOfPolicyGroupRequest.

        策略组id。

        :return: The policy_group_id of this ListPoliciesOfPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListPoliciesOfPolicyGroupRequest.

        策略组id。

        :param policy_group_id: The policy_group_id of this ListPoliciesOfPolicyGroupRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ListPoliciesOfPolicyGroupRequest.

        根据策略类型过滤结果，不传则查询所有策略。 可选类型: - 外设：Peripherals; - 音频：Audio; - 客户端：Client; - 显示：Display; - 文件与剪切板：FileAndClip; - 接入控制：ClientAccessControl; - 会话：SessionAutoDisconnect; - 虚拟通道：VirtualChannel - 水印：Watermark; - 键盘鼠标：KeyboardAndMouse; - 通用音视频旁路：Seamless。 - 录屏审计：RecordAudit。

        :return: The policy_type of this ListPoliciesOfPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ListPoliciesOfPolicyGroupRequest.

        根据策略类型过滤结果，不传则查询所有策略。 可选类型: - 外设：Peripherals; - 音频：Audio; - 客户端：Client; - 显示：Display; - 文件与剪切板：FileAndClip; - 接入控制：ClientAccessControl; - 会话：SessionAutoDisconnect; - 虚拟通道：VirtualChannel - 水印：Watermark; - 键盘鼠标：KeyboardAndMouse; - 通用音视频旁路：Seamless。 - 录屏审计：RecordAudit。

        :param policy_type: The policy_type of this ListPoliciesOfPolicyGroupRequest.
        :type policy_type: str
        """
        self._policy_type = policy_type

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
        if not isinstance(other, ListPoliciesOfPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
