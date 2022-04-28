# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIgnoreRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'rule': 'str',
        'mode': 'int',
        'conditions': 'list[Condition]',
        'domain': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'rule': 'rule',
        'mode': 'mode',
        'conditions': 'conditions',
        'domain': 'domain'
    }

    def __init__(self, id=None, policyid=None, timestamp=None, description=None, status=None, rule=None, mode=None, conditions=None, domain=None):
        """CreateIgnoreRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param timestamp: 创建规则的时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param rule: 屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护-&gt;防护规则中查询，也可以从防护事件的事件详情中查询内置规则id）
        :type rule: str
        :param mode: 版本号固定值为1,代表v2版本误报屏蔽规则，v1版本仅支持兼容旧版本，不支持创建
        :type mode: int
        :param conditions: 条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        :param domain: 防护域名或防护网站
        :type domain: list[str]
        """
        
        super(CreateIgnoreRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._rule = None
        self._mode = None
        self._conditions = None
        self._domain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if rule is not None:
            self.rule = rule
        if mode is not None:
            self.mode = mode
        if conditions is not None:
            self.conditions = conditions
        if domain is not None:
            self.domain = domain

    @property
    def id(self):
        """Gets the id of this CreateIgnoreRuleResponse.

        规则id

        :return: The id of this CreateIgnoreRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateIgnoreRuleResponse.

        规则id

        :param id: The id of this CreateIgnoreRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CreateIgnoreRuleResponse.

        策略id

        :return: The policyid of this CreateIgnoreRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateIgnoreRuleResponse.

        策略id

        :param policyid: The policyid of this CreateIgnoreRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateIgnoreRuleResponse.

        创建规则的时间戳

        :return: The timestamp of this CreateIgnoreRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateIgnoreRuleResponse.

        创建规则的时间戳

        :param timestamp: The timestamp of this CreateIgnoreRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this CreateIgnoreRuleResponse.

        规则描述

        :return: The description of this CreateIgnoreRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIgnoreRuleResponse.

        规则描述

        :param description: The description of this CreateIgnoreRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateIgnoreRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this CreateIgnoreRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateIgnoreRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this CreateIgnoreRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def rule(self):
        """Gets the rule of this CreateIgnoreRuleResponse.

        屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护->防护规则中查询，也可以从防护事件的事件详情中查询内置规则id）

        :return: The rule of this CreateIgnoreRuleResponse.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this CreateIgnoreRuleResponse.

        屏蔽的内置规则id（内置规则id通常可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护->防护规则中查询，也可以从防护事件的事件详情中查询内置规则id）

        :param rule: The rule of this CreateIgnoreRuleResponse.
        :type rule: str
        """
        self._rule = rule

    @property
    def mode(self):
        """Gets the mode of this CreateIgnoreRuleResponse.

        版本号固定值为1,代表v2版本误报屏蔽规则，v1版本仅支持兼容旧版本，不支持创建

        :return: The mode of this CreateIgnoreRuleResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateIgnoreRuleResponse.

        版本号固定值为1,代表v2版本误报屏蔽规则，v1版本仅支持兼容旧版本，不支持创建

        :param mode: The mode of this CreateIgnoreRuleResponse.
        :type mode: int
        """
        self._mode = mode

    @property
    def conditions(self):
        """Gets the conditions of this CreateIgnoreRuleResponse.

        条件列表

        :return: The conditions of this CreateIgnoreRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateIgnoreRuleResponse.

        条件列表

        :param conditions: The conditions of this CreateIgnoreRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        """
        self._conditions = conditions

    @property
    def domain(self):
        """Gets the domain of this CreateIgnoreRuleResponse.

        防护域名或防护网站

        :return: The domain of this CreateIgnoreRuleResponse.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateIgnoreRuleResponse.

        防护域名或防护网站

        :param domain: The domain of this CreateIgnoreRuleResponse.
        :type domain: list[str]
        """
        self._domain = domain

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
        if not isinstance(other, CreateIgnoreRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
