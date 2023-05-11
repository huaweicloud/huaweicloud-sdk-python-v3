# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAnticrawlerRuleResponse(SdkResponse):

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
        'conditions': 'list[AnticrawlerCondition]',
        'name': 'str',
        'type': 'str',
        'timestamp': 'int',
        'status': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'conditions': 'conditions',
        'name': 'name',
        'type': 'type',
        'timestamp': 'timestamp',
        'status': 'status',
        'priority': 'priority'
    }

    def __init__(self, id=None, policyid=None, conditions=None, name=None, type=None, timestamp=None, status=None, priority=None):
        """CreateAnticrawlerRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param conditions: 匹配条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        :param name: 规则名称
        :type name: str
        :param type: JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url
        :type type: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。
        :type priority: int
        """
        
        super(CreateAnticrawlerRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._conditions = None
        self._name = None
        self._type = None
        self._timestamp = None
        self._status = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if conditions is not None:
            self.conditions = conditions
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        """Gets the id of this CreateAnticrawlerRuleResponse.

        规则id

        :return: The id of this CreateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAnticrawlerRuleResponse.

        规则id

        :param id: The id of this CreateAnticrawlerRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this CreateAnticrawlerRuleResponse.

        策略id

        :return: The policyid of this CreateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this CreateAnticrawlerRuleResponse.

        策略id

        :param policyid: The policyid of this CreateAnticrawlerRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def conditions(self):
        """Gets the conditions of this CreateAnticrawlerRuleResponse.

        匹配条件列表

        :return: The conditions of this CreateAnticrawlerRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateAnticrawlerRuleResponse.

        匹配条件列表

        :param conditions: The conditions of this CreateAnticrawlerRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        self._conditions = conditions

    @property
    def name(self):
        """Gets the name of this CreateAnticrawlerRuleResponse.

        规则名称

        :return: The name of this CreateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAnticrawlerRuleResponse.

        规则名称

        :param name: The name of this CreateAnticrawlerRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateAnticrawlerRuleResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :return: The type of this CreateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAnticrawlerRuleResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :param type: The type of this CreateAnticrawlerRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateAnticrawlerRuleResponse.

        创建规则时间戳

        :return: The timestamp of this CreateAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateAnticrawlerRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreateAnticrawlerRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this CreateAnticrawlerRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this CreateAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateAnticrawlerRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this CreateAnticrawlerRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def priority(self):
        """Gets the priority of this CreateAnticrawlerRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this CreateAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateAnticrawlerRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this CreateAnticrawlerRuleResponse.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, CreateAnticrawlerRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
