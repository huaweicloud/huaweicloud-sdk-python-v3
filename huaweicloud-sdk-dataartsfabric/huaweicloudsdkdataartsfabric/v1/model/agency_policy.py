# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_type': 'str',
        'is_required': 'bool',
        'is_enable': 'bool',
        'actions': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'policy_type': 'policy_type',
        'is_required': 'is_required',
        'is_enable': 'is_enable',
        'actions': 'actions',
        'description': 'description'
    }

    def __init__(self, policy_type=None, is_required=None, is_enable=None, actions=None, description=None):
        r"""AgencyPolicy

        The model defined in huaweicloud sdk

        :param policy_type: 权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务相关权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。
        :type policy_type: str
        :param is_required: 是否是必需的。
        :type is_required: bool
        :param is_enable: 是否已开启。
        :type is_enable: bool
        :param actions: 权限列表
        :type actions: list[str]
        :param description: 策略描述
        :type description: str
        """
        
        

        self._policy_type = None
        self._is_required = None
        self._is_enable = None
        self._actions = None
        self._description = None
        self.discriminator = None

        self.policy_type = policy_type
        self.is_required = is_required
        self.is_enable = is_enable
        self.actions = actions
        self.description = description

    @property
    def policy_type(self):
        r"""Gets the policy_type of this AgencyPolicy.

        权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务相关权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。

        :return: The policy_type of this AgencyPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this AgencyPolicy.

        权限类型列表，使用Fabric的功能，可能需要授权一些权限策略，可以在policy_types中加入策略类型来授权权限。FABRIC_COMMON_POLICY：基础通用服务相关权限策略，是委托必需的权限策略；FABRIC_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN；FABRIC_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略；FABRIC_AOM_POLICY：AOM功能相关权限策略。

        :param policy_type: The policy_type of this AgencyPolicy.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def is_required(self):
        r"""Gets the is_required of this AgencyPolicy.

        是否是必需的。

        :return: The is_required of this AgencyPolicy.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this AgencyPolicy.

        是否是必需的。

        :param is_required: The is_required of this AgencyPolicy.
        :type is_required: bool
        """
        self._is_required = is_required

    @property
    def is_enable(self):
        r"""Gets the is_enable of this AgencyPolicy.

        是否已开启。

        :return: The is_enable of this AgencyPolicy.
        :rtype: bool
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this AgencyPolicy.

        是否已开启。

        :param is_enable: The is_enable of this AgencyPolicy.
        :type is_enable: bool
        """
        self._is_enable = is_enable

    @property
    def actions(self):
        r"""Gets the actions of this AgencyPolicy.

        权限列表

        :return: The actions of this AgencyPolicy.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this AgencyPolicy.

        权限列表

        :param actions: The actions of this AgencyPolicy.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def description(self):
        r"""Gets the description of this AgencyPolicy.

        策略描述

        :return: The description of this AgencyPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AgencyPolicy.

        策略描述

        :param description: The description of this AgencyPolicy.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AgencyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
