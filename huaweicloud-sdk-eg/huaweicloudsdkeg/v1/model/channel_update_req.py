# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelUpdateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'enterprise_project_id': 'str',
        'cross_account': 'bool',
        'policy': 'dict(str, ChannelCreateReqPolicy)'
    }

    attribute_map = {
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'cross_account': 'cross_account',
        'policy': 'policy'
    }

    def __init__(self, description=None, enterprise_project_id=None, cross_account=None, policy=None):
        r"""ChannelUpdateReq

        The model defined in huaweicloud sdk

        :param description: 通道描述
        :type description: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param cross_account: 跨账号开关
        :type cross_account: bool
        :param policy: 策略
        :type policy: dict(str, ChannelCreateReqPolicy)
        """
        
        

        self._description = None
        self._enterprise_project_id = None
        self._cross_account = None
        self._policy = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if cross_account is not None:
            self.cross_account = cross_account
        if policy is not None:
            self.policy = policy

    @property
    def description(self):
        r"""Gets the description of this ChannelUpdateReq.

        通道描述

        :return: The description of this ChannelUpdateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChannelUpdateReq.

        通道描述

        :param description: The description of this ChannelUpdateReq.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChannelUpdateReq.

        企业项目id

        :return: The enterprise_project_id of this ChannelUpdateReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChannelUpdateReq.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ChannelUpdateReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def cross_account(self):
        r"""Gets the cross_account of this ChannelUpdateReq.

        跨账号开关

        :return: The cross_account of this ChannelUpdateReq.
        :rtype: bool
        """
        return self._cross_account

    @cross_account.setter
    def cross_account(self, cross_account):
        r"""Sets the cross_account of this ChannelUpdateReq.

        跨账号开关

        :param cross_account: The cross_account of this ChannelUpdateReq.
        :type cross_account: bool
        """
        self._cross_account = cross_account

    @property
    def policy(self):
        r"""Gets the policy of this ChannelUpdateReq.

        策略

        :return: The policy of this ChannelUpdateReq.
        :rtype: dict(str, ChannelCreateReqPolicy)
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ChannelUpdateReq.

        策略

        :param policy: The policy of this ChannelUpdateReq.
        :type policy: dict(str, ChannelCreateReqPolicy)
        """
        self._policy = policy

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
        if not isinstance(other, ChannelUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
