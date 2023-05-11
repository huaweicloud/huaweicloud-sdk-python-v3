# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAnticrawlerRuleRequestbody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conditions': 'list[AnticrawlerCondition]',
        'name': 'str',
        'type': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'name': 'name',
        'type': 'type',
        'priority': 'priority'
    }

    def __init__(self, conditions=None, name=None, type=None, priority=None):
        """CreateAnticrawlerRuleRequestbody

        The model defined in huaweicloud sdk

        :param conditions: 匹配条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        :param name: 规则名称
        :type name: str
        :param type: JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url
        :type type: str
        :param priority: 执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。
        :type priority: int
        """
        
        

        self._conditions = None
        self._name = None
        self._type = None
        self._priority = None
        self.discriminator = None

        self.conditions = conditions
        self.name = name
        self.type = type
        self.priority = priority

    @property
    def conditions(self):
        """Gets the conditions of this CreateAnticrawlerRuleRequestbody.

        匹配条件列表

        :return: The conditions of this CreateAnticrawlerRuleRequestbody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateAnticrawlerRuleRequestbody.

        匹配条件列表

        :param conditions: The conditions of this CreateAnticrawlerRuleRequestbody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.AnticrawlerCondition`]
        """
        self._conditions = conditions

    @property
    def name(self):
        """Gets the name of this CreateAnticrawlerRuleRequestbody.

        规则名称

        :return: The name of this CreateAnticrawlerRuleRequestbody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAnticrawlerRuleRequestbody.

        规则名称

        :param name: The name of this CreateAnticrawlerRuleRequestbody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateAnticrawlerRuleRequestbody.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :return: The type of this CreateAnticrawlerRuleRequestbody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAnticrawlerRuleRequestbody.

        JS脚本反爬虫规则类型，指定防护路径：anticrawler_specific_url 排除防护路径：anticrawler_except_url

        :param type: The type of this CreateAnticrawlerRuleRequestbody.
        :type type: str
        """
        self._type = type

    @property
    def priority(self):
        """Gets the priority of this CreateAnticrawlerRuleRequestbody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :return: The priority of this CreateAnticrawlerRuleRequestbody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateAnticrawlerRuleRequestbody.

        执行该规则的优先级，值越小，优先级越高，值相同时，规则创建时间早，优先级越高。取值范围：0到1000。

        :param priority: The priority of this CreateAnticrawlerRuleRequestbody.
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
        if not isinstance(other, CreateAnticrawlerRuleRequestbody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
