# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyTypeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_types': 'list[str]'
    }

    attribute_map = {
        'policy_types': 'policy_types'
    }

    def __init__(self, policy_types=None):
        r"""AgencyTypeBody

        The model defined in huaweicloud sdk

        :param policy_types: 权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。
        :type policy_types: list[str]
        """
        
        

        self._policy_types = None
        self.discriminator = None

        if policy_types is not None:
            self.policy_types = policy_types

    @property
    def policy_types(self):
        r"""Gets the policy_types of this AgencyTypeBody.

        权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。

        :return: The policy_types of this AgencyTypeBody.
        :rtype: list[str]
        """
        return self._policy_types

    @policy_types.setter
    def policy_types(self, policy_types):
        r"""Sets the policy_types of this AgencyTypeBody.

        权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。

        :param policy_types: The policy_types of this AgencyTypeBody.
        :type policy_types: list[str]
        """
        self._policy_types = policy_types

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
        if not isinstance(other, AgencyTypeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
