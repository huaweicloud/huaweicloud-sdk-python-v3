# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAnticrawlerRuleResponse(SdkResponse):

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
        r"""DeleteAnticrawlerRuleResponse

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
        
        super(DeleteAnticrawlerRuleResponse, self).__init__()

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
        r"""Gets the id of this DeleteAnticrawlerRuleResponse.

        规则id

        :return: The id of this DeleteAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteAnticrawlerRuleResponse.

        规则id

        :param id: The id of this DeleteAnticrawlerRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this DeleteAnticrawlerRuleResponse.

        策略id

        :return: The policyid of this DeleteAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this DeleteAnticrawlerRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteAnticrawlerRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def conditions(self):
        r"""Gets the conditions of this DeleteAnticrawlerRuleResponse.

        匹配条件列表

        :return: The conditions of this DeleteAnticrawlerRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this DeleteAnticrawlerRuleResponse.

        匹配条件列表

        :param conditions: The conditions of this DeleteAnticrawlerRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        self._conditions = conditions

    @property
    def name(self):
        r"""Gets the name of this DeleteAnticrawlerRuleResponse.

        规则名称

        :return: The name of this DeleteAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteAnticrawlerRuleResponse.

        规则名称

        :param name: The name of this DeleteAnticrawlerRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DeleteAnticrawlerRuleResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :return: The type of this DeleteAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteAnticrawlerRuleResponse.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :param type: The type of this DeleteAnticrawlerRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def timestamp(self):
        r"""Gets the timestamp of this DeleteAnticrawlerRuleResponse.

        创建规则时间戳

        :return: The timestamp of this DeleteAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this DeleteAnticrawlerRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this DeleteAnticrawlerRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def status(self):
        r"""Gets the status of this DeleteAnticrawlerRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this DeleteAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteAnticrawlerRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this DeleteAnticrawlerRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def priority(self):
        r"""Gets the priority of this DeleteAnticrawlerRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this DeleteAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this DeleteAnticrawlerRuleResponse.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this DeleteAnticrawlerRuleResponse.
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
        if not isinstance(other, DeleteAnticrawlerRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
