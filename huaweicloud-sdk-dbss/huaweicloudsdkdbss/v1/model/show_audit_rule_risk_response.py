# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditRuleRiskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'rule_name': 'str',
        'status': 'str',
        'action': 'str',
        'schemas': 'list[RuleRiskInfoBeanSchemas]',
        'rank': 'int',
        'ignore_case': 'bool',
        'risk_level': 'str',
        'db_ids': 'str',
        'execution_symbol': 'str',
        'execution_time': 'int',
        'affect_symbol': 'str',
        'affect_rows': 'int',
        'client_ips': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'status': 'status',
        'action': 'action',
        'schemas': 'schemas',
        'rank': 'rank',
        'ignore_case': 'ignore_case',
        'risk_level': 'risk_level',
        'db_ids': 'db_ids',
        'execution_symbol': 'execution_symbol',
        'execution_time': 'execution_time',
        'affect_symbol': 'affect_symbol',
        'affect_rows': 'affect_rows',
        'client_ips': 'client_ips'
    }

    def __init__(self, rule_id=None, rule_name=None, status=None, action=None, schemas=None, rank=None, ignore_case=None, risk_level=None, db_ids=None, execution_symbol=None, execution_time=None, affect_symbol=None, affect_rows=None, client_ips=None):
        """ShowAuditRuleRiskResponse

        The model defined in huaweicloud sdk

        :param rule_id: 风险规则ID
        :type rule_id: str
        :param rule_name: 风险名称
        :type rule_name: str
        :param status: 风险规则状态 枚举值：  OFF  ON
        :type status: str
        :param action: 操作集合, 中间逗号分隔 LOGIN CREATE_TABLE CREATE_TABLESPACE DROP_TABLE DROP_TABLESPACE DELETE INSERT INSERT_SELECT SELECT SELECT_FOR_UPDATE UPDATE CREATE_USER DROP_USER GRANT OPERATE ALL
        :type action: str
        :param schemas: Schema列表
        :type schemas: list[:class:`huaweicloudsdkdbss.v1.RuleRiskInfoBeanSchemas`]
        :param rank: 风险规则优先级
        :type rank: int
        :param ignore_case: 是否忽略大小写
        :type ignore_case: bool
        :param risk_level: 风险级别 枚举值：  LOW  MEDIUM  HIGH  NO_RISK
        :type risk_level: str
        :param db_ids: 数据库id，中间逗号分隔（单个id 小于256位）
        :type db_ids: str
        :param execution_symbol: 执行时长对执行时长阈值的关系 枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH
        :type execution_symbol: str
        :param execution_time: 设定的执行时长阈值
        :type execution_time: int
        :param affect_symbol: 影响行数对行数阈值的关系：  枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH
        :type affect_symbol: str
        :param affect_rows: 设定的影响行数阈值
        :type affect_rows: int
        :param client_ips: 客户端IP段: IP-IP格式，或IP/XX 格式。 各个IP段使用逗号连接
        :type client_ips: str
        """
        
        super(ShowAuditRuleRiskResponse, self).__init__()

        self._rule_id = None
        self._rule_name = None
        self._status = None
        self._action = None
        self._schemas = None
        self._rank = None
        self._ignore_case = None
        self._risk_level = None
        self._db_ids = None
        self._execution_symbol = None
        self._execution_time = None
        self._affect_symbol = None
        self._affect_rows = None
        self._client_ips = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action
        if schemas is not None:
            self.schemas = schemas
        if rank is not None:
            self.rank = rank
        if ignore_case is not None:
            self.ignore_case = ignore_case
        if risk_level is not None:
            self.risk_level = risk_level
        if db_ids is not None:
            self.db_ids = db_ids
        if execution_symbol is not None:
            self.execution_symbol = execution_symbol
        if execution_time is not None:
            self.execution_time = execution_time
        if affect_symbol is not None:
            self.affect_symbol = affect_symbol
        if affect_rows is not None:
            self.affect_rows = affect_rows
        if client_ips is not None:
            self.client_ips = client_ips

    @property
    def rule_id(self):
        """Gets the rule_id of this ShowAuditRuleRiskResponse.

        风险规则ID

        :return: The rule_id of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ShowAuditRuleRiskResponse.

        风险规则ID

        :param rule_id: The rule_id of this ShowAuditRuleRiskResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ShowAuditRuleRiskResponse.

        风险名称

        :return: The rule_name of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ShowAuditRuleRiskResponse.

        风险名称

        :param rule_name: The rule_name of this ShowAuditRuleRiskResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def status(self):
        """Gets the status of this ShowAuditRuleRiskResponse.

        风险规则状态 枚举值：  OFF  ON

        :return: The status of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowAuditRuleRiskResponse.

        风险规则状态 枚举值：  OFF  ON

        :param status: The status of this ShowAuditRuleRiskResponse.
        :type status: str
        """
        self._status = status

    @property
    def action(self):
        """Gets the action of this ShowAuditRuleRiskResponse.

        操作集合, 中间逗号分隔 LOGIN CREATE_TABLE CREATE_TABLESPACE DROP_TABLE DROP_TABLESPACE DELETE INSERT INSERT_SELECT SELECT SELECT_FOR_UPDATE UPDATE CREATE_USER DROP_USER GRANT OPERATE ALL

        :return: The action of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowAuditRuleRiskResponse.

        操作集合, 中间逗号分隔 LOGIN CREATE_TABLE CREATE_TABLESPACE DROP_TABLE DROP_TABLESPACE DELETE INSERT INSERT_SELECT SELECT SELECT_FOR_UPDATE UPDATE CREATE_USER DROP_USER GRANT OPERATE ALL

        :param action: The action of this ShowAuditRuleRiskResponse.
        :type action: str
        """
        self._action = action

    @property
    def schemas(self):
        """Gets the schemas of this ShowAuditRuleRiskResponse.

        Schema列表

        :return: The schemas of this ShowAuditRuleRiskResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.RuleRiskInfoBeanSchemas`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this ShowAuditRuleRiskResponse.

        Schema列表

        :param schemas: The schemas of this ShowAuditRuleRiskResponse.
        :type schemas: list[:class:`huaweicloudsdkdbss.v1.RuleRiskInfoBeanSchemas`]
        """
        self._schemas = schemas

    @property
    def rank(self):
        """Gets the rank of this ShowAuditRuleRiskResponse.

        风险规则优先级

        :return: The rank of this ShowAuditRuleRiskResponse.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this ShowAuditRuleRiskResponse.

        风险规则优先级

        :param rank: The rank of this ShowAuditRuleRiskResponse.
        :type rank: int
        """
        self._rank = rank

    @property
    def ignore_case(self):
        """Gets the ignore_case of this ShowAuditRuleRiskResponse.

        是否忽略大小写

        :return: The ignore_case of this ShowAuditRuleRiskResponse.
        :rtype: bool
        """
        return self._ignore_case

    @ignore_case.setter
    def ignore_case(self, ignore_case):
        """Sets the ignore_case of this ShowAuditRuleRiskResponse.

        是否忽略大小写

        :param ignore_case: The ignore_case of this ShowAuditRuleRiskResponse.
        :type ignore_case: bool
        """
        self._ignore_case = ignore_case

    @property
    def risk_level(self):
        """Gets the risk_level of this ShowAuditRuleRiskResponse.

        风险级别 枚举值：  LOW  MEDIUM  HIGH  NO_RISK

        :return: The risk_level of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this ShowAuditRuleRiskResponse.

        风险级别 枚举值：  LOW  MEDIUM  HIGH  NO_RISK

        :param risk_level: The risk_level of this ShowAuditRuleRiskResponse.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def db_ids(self):
        """Gets the db_ids of this ShowAuditRuleRiskResponse.

        数据库id，中间逗号分隔（单个id 小于256位）

        :return: The db_ids of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        """Sets the db_ids of this ShowAuditRuleRiskResponse.

        数据库id，中间逗号分隔（单个id 小于256位）

        :param db_ids: The db_ids of this ShowAuditRuleRiskResponse.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def execution_symbol(self):
        """Gets the execution_symbol of this ShowAuditRuleRiskResponse.

        执行时长对执行时长阈值的关系 枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH

        :return: The execution_symbol of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._execution_symbol

    @execution_symbol.setter
    def execution_symbol(self, execution_symbol):
        """Sets the execution_symbol of this ShowAuditRuleRiskResponse.

        执行时长对执行时长阈值的关系 枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH

        :param execution_symbol: The execution_symbol of this ShowAuditRuleRiskResponse.
        :type execution_symbol: str
        """
        self._execution_symbol = execution_symbol

    @property
    def execution_time(self):
        """Gets the execution_time of this ShowAuditRuleRiskResponse.

        设定的执行时长阈值

        :return: The execution_time of this ShowAuditRuleRiskResponse.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this ShowAuditRuleRiskResponse.

        设定的执行时长阈值

        :param execution_time: The execution_time of this ShowAuditRuleRiskResponse.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def affect_symbol(self):
        """Gets the affect_symbol of this ShowAuditRuleRiskResponse.

        影响行数对行数阈值的关系：  枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH

        :return: The affect_symbol of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._affect_symbol

    @affect_symbol.setter
    def affect_symbol(self, affect_symbol):
        """Sets the affect_symbol of this ShowAuditRuleRiskResponse.

        影响行数对行数阈值的关系：  枚举值：  GREATER  EQUAL  LESS  GREATER_EQUAL  LESS_EQUAL  NO_MATCH

        :param affect_symbol: The affect_symbol of this ShowAuditRuleRiskResponse.
        :type affect_symbol: str
        """
        self._affect_symbol = affect_symbol

    @property
    def affect_rows(self):
        """Gets the affect_rows of this ShowAuditRuleRiskResponse.

        设定的影响行数阈值

        :return: The affect_rows of this ShowAuditRuleRiskResponse.
        :rtype: int
        """
        return self._affect_rows

    @affect_rows.setter
    def affect_rows(self, affect_rows):
        """Sets the affect_rows of this ShowAuditRuleRiskResponse.

        设定的影响行数阈值

        :param affect_rows: The affect_rows of this ShowAuditRuleRiskResponse.
        :type affect_rows: int
        """
        self._affect_rows = affect_rows

    @property
    def client_ips(self):
        """Gets the client_ips of this ShowAuditRuleRiskResponse.

        客户端IP段: IP-IP格式，或IP/XX 格式。 各个IP段使用逗号连接

        :return: The client_ips of this ShowAuditRuleRiskResponse.
        :rtype: str
        """
        return self._client_ips

    @client_ips.setter
    def client_ips(self, client_ips):
        """Sets the client_ips of this ShowAuditRuleRiskResponse.

        客户端IP段: IP-IP格式，或IP/XX 格式。 各个IP段使用逗号连接

        :param client_ips: The client_ips of this ShowAuditRuleRiskResponse.
        :type client_ips: str
        """
        self._client_ips = client_ips

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
        if not isinstance(other, ShowAuditRuleRiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
