# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleAddRiskRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'affect_rows': 'int',
        'affect_symbol': 'str',
        'client_ips': 'str',
        'db_ids': 'str',
        'exception_ips': 'str',
        'execution_symbol': 'str',
        'execution_time': 'int',
        'ignore_case': 'bool',
        'risk_level': 'str',
        'rule_name': 'str',
        'schemas': 'list[SchemaBean]',
        'status': 'str'
    }

    attribute_map = {
        'action': 'action',
        'affect_rows': 'affect_rows',
        'affect_symbol': 'affect_symbol',
        'client_ips': 'client_ips',
        'db_ids': 'db_ids',
        'exception_ips': 'exception_ips',
        'execution_symbol': 'execution_symbol',
        'execution_time': 'execution_time',
        'ignore_case': 'ignore_case',
        'risk_level': 'risk_level',
        'rule_name': 'rule_name',
        'schemas': 'schemas',
        'status': 'status'
    }

    def __init__(self, action=None, affect_rows=None, affect_symbol=None, client_ips=None, db_ids=None, exception_ips=None, execution_symbol=None, execution_time=None, ignore_case=None, risk_level=None, rule_name=None, schemas=None, status=None):
        r"""RuleAddRiskRuleRequest

        The model defined in huaweicloud sdk

        :param action: 操作类型，多个用英文&#39;,&#39;分隔
        :type action: str
        :param affect_rows: 影响行数
        :type affect_rows: int
        :param affect_symbol: 影响行数操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于
        :type affect_symbol: str
        :param client_ips: 客户端IP，多个用英文&#39;,&#39;分隔
        :type client_ips: str
        :param db_ids: 数据库ID，多个用英文&#39;,&#39;分隔
        :type db_ids: str
        :param exception_ips: 例外IP，IP内不做匹配，多个用英文&#39;,&#39;分隔
        :type exception_ips: str
        :param execution_symbol: 执行时长操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于
        :type execution_symbol: str
        :param execution_time: 执行时长
        :type execution_time: int
        :param ignore_case: 是否忽略大小写
        :type ignore_case: bool
        :param risk_level: 风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无
        :type risk_level: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param schemas: 操作对象
        :type schemas: list[:class:`huaweicloudsdkdbss.v1.SchemaBean`]
        :param status: 状态  - OFF：已关闭  - ON：已开启
        :type status: str
        """
        
        

        self._action = None
        self._affect_rows = None
        self._affect_symbol = None
        self._client_ips = None
        self._db_ids = None
        self._exception_ips = None
        self._execution_symbol = None
        self._execution_time = None
        self._ignore_case = None
        self._risk_level = None
        self._rule_name = None
        self._schemas = None
        self._status = None
        self.discriminator = None

        if action is not None:
            self.action = action
        self.affect_rows = affect_rows
        self.affect_symbol = affect_symbol
        if client_ips is not None:
            self.client_ips = client_ips
        if db_ids is not None:
            self.db_ids = db_ids
        if exception_ips is not None:
            self.exception_ips = exception_ips
        self.execution_symbol = execution_symbol
        self.execution_time = execution_time
        if ignore_case is not None:
            self.ignore_case = ignore_case
        self.risk_level = risk_level
        self.rule_name = rule_name
        if schemas is not None:
            self.schemas = schemas
        self.status = status

    @property
    def action(self):
        r"""Gets the action of this RuleAddRiskRuleRequest.

        操作类型，多个用英文','分隔

        :return: The action of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RuleAddRiskRuleRequest.

        操作类型，多个用英文','分隔

        :param action: The action of this RuleAddRiskRuleRequest.
        :type action: str
        """
        self._action = action

    @property
    def affect_rows(self):
        r"""Gets the affect_rows of this RuleAddRiskRuleRequest.

        影响行数

        :return: The affect_rows of this RuleAddRiskRuleRequest.
        :rtype: int
        """
        return self._affect_rows

    @affect_rows.setter
    def affect_rows(self, affect_rows):
        r"""Sets the affect_rows of this RuleAddRiskRuleRequest.

        影响行数

        :param affect_rows: The affect_rows of this RuleAddRiskRuleRequest.
        :type affect_rows: int
        """
        self._affect_rows = affect_rows

    @property
    def affect_symbol(self):
        r"""Gets the affect_symbol of this RuleAddRiskRuleRequest.

        影响行数操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于

        :return: The affect_symbol of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._affect_symbol

    @affect_symbol.setter
    def affect_symbol(self, affect_symbol):
        r"""Sets the affect_symbol of this RuleAddRiskRuleRequest.

        影响行数操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于

        :param affect_symbol: The affect_symbol of this RuleAddRiskRuleRequest.
        :type affect_symbol: str
        """
        self._affect_symbol = affect_symbol

    @property
    def client_ips(self):
        r"""Gets the client_ips of this RuleAddRiskRuleRequest.

        客户端IP，多个用英文','分隔

        :return: The client_ips of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._client_ips

    @client_ips.setter
    def client_ips(self, client_ips):
        r"""Sets the client_ips of this RuleAddRiskRuleRequest.

        客户端IP，多个用英文','分隔

        :param client_ips: The client_ips of this RuleAddRiskRuleRequest.
        :type client_ips: str
        """
        self._client_ips = client_ips

    @property
    def db_ids(self):
        r"""Gets the db_ids of this RuleAddRiskRuleRequest.

        数据库ID，多个用英文','分隔

        :return: The db_ids of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this RuleAddRiskRuleRequest.

        数据库ID，多个用英文','分隔

        :param db_ids: The db_ids of this RuleAddRiskRuleRequest.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def exception_ips(self):
        r"""Gets the exception_ips of this RuleAddRiskRuleRequest.

        例外IP，IP内不做匹配，多个用英文','分隔

        :return: The exception_ips of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._exception_ips

    @exception_ips.setter
    def exception_ips(self, exception_ips):
        r"""Sets the exception_ips of this RuleAddRiskRuleRequest.

        例外IP，IP内不做匹配，多个用英文','分隔

        :param exception_ips: The exception_ips of this RuleAddRiskRuleRequest.
        :type exception_ips: str
        """
        self._exception_ips = exception_ips

    @property
    def execution_symbol(self):
        r"""Gets the execution_symbol of this RuleAddRiskRuleRequest.

        执行时长操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于

        :return: The execution_symbol of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._execution_symbol

    @execution_symbol.setter
    def execution_symbol(self, execution_symbol):
        r"""Sets the execution_symbol of this RuleAddRiskRuleRequest.

        执行时长操作符 - GREATER: 大于 - EQUAL: 等于 - LESS: 小于 - GREATER_EQUAL: 大于等于 - LESS_EQUAL: 小于等于 - NO_MATCH: 不等于

        :param execution_symbol: The execution_symbol of this RuleAddRiskRuleRequest.
        :type execution_symbol: str
        """
        self._execution_symbol = execution_symbol

    @property
    def execution_time(self):
        r"""Gets the execution_time of this RuleAddRiskRuleRequest.

        执行时长

        :return: The execution_time of this RuleAddRiskRuleRequest.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this RuleAddRiskRuleRequest.

        执行时长

        :param execution_time: The execution_time of this RuleAddRiskRuleRequest.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def ignore_case(self):
        r"""Gets the ignore_case of this RuleAddRiskRuleRequest.

        是否忽略大小写

        :return: The ignore_case of this RuleAddRiskRuleRequest.
        :rtype: bool
        """
        return self._ignore_case

    @ignore_case.setter
    def ignore_case(self, ignore_case):
        r"""Sets the ignore_case of this RuleAddRiskRuleRequest.

        是否忽略大小写

        :param ignore_case: The ignore_case of this RuleAddRiskRuleRequest.
        :type ignore_case: bool
        """
        self._ignore_case = ignore_case

    @property
    def risk_level(self):
        r"""Gets the risk_level of this RuleAddRiskRuleRequest.

        风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无

        :return: The risk_level of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this RuleAddRiskRuleRequest.

        风险等级   - LOW：低  - MEDIUM：中  - HIGH：高  - NO_RISK：无

        :param risk_level: The risk_level of this RuleAddRiskRuleRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleAddRiskRuleRequest.

        规则名称

        :return: The rule_name of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleAddRiskRuleRequest.

        规则名称

        :param rule_name: The rule_name of this RuleAddRiskRuleRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def schemas(self):
        r"""Gets the schemas of this RuleAddRiskRuleRequest.

        操作对象

        :return: The schemas of this RuleAddRiskRuleRequest.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SchemaBean`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this RuleAddRiskRuleRequest.

        操作对象

        :param schemas: The schemas of this RuleAddRiskRuleRequest.
        :type schemas: list[:class:`huaweicloudsdkdbss.v1.SchemaBean`]
        """
        self._schemas = schemas

    @property
    def status(self):
        r"""Gets the status of this RuleAddRiskRuleRequest.

        状态  - OFF：已关闭  - ON：已开启

        :return: The status of this RuleAddRiskRuleRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RuleAddRiskRuleRequest.

        状态  - OFF：已关闭  - ON：已开启

        :param status: The status of this RuleAddRiskRuleRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RuleAddRiskRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
