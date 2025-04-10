# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlRuleResponseRules:

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
        'name': 'str',
        'status': 'str',
        'risk_level': 'str',
        'type': 'str',
        'rank': 'int',
        'feature': 'str',
        'regex': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'risk_level': 'risk_level',
        'type': 'type',
        'rank': 'rank',
        'feature': 'feature',
        'regex': 'regex'
    }

    def __init__(self, id=None, name=None, status=None, risk_level=None, type=None, rank=None, feature=None, regex=None):
        r"""SqlRuleResponseRules

        The model defined in huaweicloud sdk

        :param id: SQL规则ID
        :type id: str
        :param name: SQL规则名称
        :type name: str
        :param status: 规则的状态： - ON - OFF
        :type status: str
        :param risk_level: 风险级别 - HIGH - MEDIUM - LOW
        :type risk_level: str
        :param type: 风险类型
        :type type: str
        :param rank: 优先级。数字越小优先级越高。
        :type rank: int
        :param feature: SQL命令特征
        :type feature: str
        :param regex: 正则表达式
        :type regex: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._risk_level = None
        self._type = None
        self._rank = None
        self._feature = None
        self._regex = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if risk_level is not None:
            self.risk_level = risk_level
        if type is not None:
            self.type = type
        if rank is not None:
            self.rank = rank
        if feature is not None:
            self.feature = feature
        if regex is not None:
            self.regex = regex

    @property
    def id(self):
        r"""Gets the id of this SqlRuleResponseRules.

        SQL规则ID

        :return: The id of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SqlRuleResponseRules.

        SQL规则ID

        :param id: The id of this SqlRuleResponseRules.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SqlRuleResponseRules.

        SQL规则名称

        :return: The name of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SqlRuleResponseRules.

        SQL规则名称

        :param name: The name of this SqlRuleResponseRules.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this SqlRuleResponseRules.

        规则的状态： - ON - OFF

        :return: The status of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlRuleResponseRules.

        规则的状态： - ON - OFF

        :param status: The status of this SqlRuleResponseRules.
        :type status: str
        """
        self._status = status

    @property
    def risk_level(self):
        r"""Gets the risk_level of this SqlRuleResponseRules.

        风险级别 - HIGH - MEDIUM - LOW

        :return: The risk_level of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this SqlRuleResponseRules.

        风险级别 - HIGH - MEDIUM - LOW

        :param risk_level: The risk_level of this SqlRuleResponseRules.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def type(self):
        r"""Gets the type of this SqlRuleResponseRules.

        风险类型

        :return: The type of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SqlRuleResponseRules.

        风险类型

        :param type: The type of this SqlRuleResponseRules.
        :type type: str
        """
        self._type = type

    @property
    def rank(self):
        r"""Gets the rank of this SqlRuleResponseRules.

        优先级。数字越小优先级越高。

        :return: The rank of this SqlRuleResponseRules.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        r"""Sets the rank of this SqlRuleResponseRules.

        优先级。数字越小优先级越高。

        :param rank: The rank of this SqlRuleResponseRules.
        :type rank: int
        """
        self._rank = rank

    @property
    def feature(self):
        r"""Gets the feature of this SqlRuleResponseRules.

        SQL命令特征

        :return: The feature of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this SqlRuleResponseRules.

        SQL命令特征

        :param feature: The feature of this SqlRuleResponseRules.
        :type feature: str
        """
        self._feature = feature

    @property
    def regex(self):
        r"""Gets the regex of this SqlRuleResponseRules.

        正则表达式

        :return: The regex of this SqlRuleResponseRules.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this SqlRuleResponseRules.

        正则表达式

        :param regex: The regex of this SqlRuleResponseRules.
        :type regex: str
        """
        self._regex = regex

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
        if not isinstance(other, SqlRuleResponseRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
