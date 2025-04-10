# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAgencyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_type': 'str'
    }

    attribute_map = {
        'policy_type': 'policy_type'
    }

    def __init__(self, policy_type=None):
        r"""DeleteAgencyRequest

        The model defined in huaweicloud sdk

        :param policy_type: 权限策略类型。FABRIC_COMMON_POLICY：基础通用服务相关的权限策略；FABRIC_SMN_POLICY：消息通知功能相关的权限策略；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关的权限策略；FABRIC_AOM_POLICY：AOM功能相关的权限策略。
        :type policy_type: str
        """
        
        

        self._policy_type = None
        self.discriminator = None

        if policy_type is not None:
            self.policy_type = policy_type

    @property
    def policy_type(self):
        r"""Gets the policy_type of this DeleteAgencyRequest.

        权限策略类型。FABRIC_COMMON_POLICY：基础通用服务相关的权限策略；FABRIC_SMN_POLICY：消息通知功能相关的权限策略；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关的权限策略；FABRIC_AOM_POLICY：AOM功能相关的权限策略。

        :return: The policy_type of this DeleteAgencyRequest.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this DeleteAgencyRequest.

        权限策略类型。FABRIC_COMMON_POLICY：基础通用服务相关的权限策略；FABRIC_SMN_POLICY：消息通知功能相关的权限策略；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关的权限策略；FABRIC_AOM_POLICY：AOM功能相关的权限策略。

        :param policy_type: The policy_type of this DeleteAgencyRequest.
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
        if not isinstance(other, DeleteAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
