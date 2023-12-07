# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'eps_id': 'str',
        'cross_account': 'bool',
        'policy': 'dict(str, ChannelCreateReqPolicy)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'eps_id': 'eps_id',
        'cross_account': 'cross_account',
        'policy': 'policy'
    }

    def __init__(self, name=None, description=None, eps_id=None, cross_account=None, policy=None):
        """ChannelCreateReq

        The model defined in huaweicloud sdk

        :param name: 通道名称，租户下唯一，由字母，数字，点，下划线和中划线组成，必须字母或数字开头，不能是default
        :type name: str
        :param description: 通道描述
        :type description: str
        :param eps_id: 企业项目id
        :type eps_id: str
        :param cross_account: 跨账号开关
        :type cross_account: bool
        :param policy: 策略
        :type policy: dict(str, ChannelCreateReqPolicy)
        """
        
        

        self._name = None
        self._description = None
        self._eps_id = None
        self._cross_account = None
        self._policy = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if eps_id is not None:
            self.eps_id = eps_id
        if cross_account is not None:
            self.cross_account = cross_account
        if policy is not None:
            self.policy = policy

    @property
    def name(self):
        """Gets the name of this ChannelCreateReq.

        通道名称，租户下唯一，由字母，数字，点，下划线和中划线组成，必须字母或数字开头，不能是default

        :return: The name of this ChannelCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelCreateReq.

        通道名称，租户下唯一，由字母，数字，点，下划线和中划线组成，必须字母或数字开头，不能是default

        :param name: The name of this ChannelCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ChannelCreateReq.

        通道描述

        :return: The description of this ChannelCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChannelCreateReq.

        通道描述

        :param description: The description of this ChannelCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def eps_id(self):
        """Gets the eps_id of this ChannelCreateReq.

        企业项目id

        :return: The eps_id of this ChannelCreateReq.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this ChannelCreateReq.

        企业项目id

        :param eps_id: The eps_id of this ChannelCreateReq.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def cross_account(self):
        """Gets the cross_account of this ChannelCreateReq.

        跨账号开关

        :return: The cross_account of this ChannelCreateReq.
        :rtype: bool
        """
        return self._cross_account

    @cross_account.setter
    def cross_account(self, cross_account):
        """Sets the cross_account of this ChannelCreateReq.

        跨账号开关

        :param cross_account: The cross_account of this ChannelCreateReq.
        :type cross_account: bool
        """
        self._cross_account = cross_account

    @property
    def policy(self):
        """Gets the policy of this ChannelCreateReq.

        策略

        :return: The policy of this ChannelCreateReq.
        :rtype: dict(str, ChannelCreateReqPolicy)
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ChannelCreateReq.

        策略

        :param policy: The policy of this ChannelCreateReq.
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
        if not isinstance(other, ChannelCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
