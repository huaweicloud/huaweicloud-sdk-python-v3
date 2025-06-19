# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlJobSystemDefendRuleResponse(SdkResponse):

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
        'category': 'str',
        'actions': 'list[str]',
        'engines': 'list[str]',
        'no_limit': 'bool',
        'desc': 'str',
        'param': 'SysRuleParam'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'category': 'category',
        'actions': 'actions',
        'engines': 'engines',
        'no_limit': 'no_limit',
        'desc': 'desc',
        'param': 'param'
    }

    def __init__(self, rule_id=None, category=None, actions=None, engines=None, no_limit=None, desc=None, param=None):
        r"""ShowSqlJobSystemDefendRuleResponse

        The model defined in huaweicloud sdk

        :param rule_id: 规则类型
        :type rule_id: str
        :param category: 规则状态类型
        :type category: str
        :param actions: 可执行的动作
        :type actions: list[str]
        :param engines: 支持的引擎
        :type engines: list[str]
        :param no_limit: 规则是否有限制值
        :type no_limit: bool
        :param desc: 规则描述
        :type desc: str
        :param param: 
        :type param: :class:`huaweicloudsdkdli.v1.SysRuleParam`
        """
        
        super(ShowSqlJobSystemDefendRuleResponse, self).__init__()

        self._rule_id = None
        self._category = None
        self._actions = None
        self._engines = None
        self._no_limit = None
        self._desc = None
        self._param = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if category is not None:
            self.category = category
        if actions is not None:
            self.actions = actions
        if engines is not None:
            self.engines = engines
        if no_limit is not None:
            self.no_limit = no_limit
        if desc is not None:
            self.desc = desc
        if param is not None:
            self.param = param

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ShowSqlJobSystemDefendRuleResponse.

        规则类型

        :return: The rule_id of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ShowSqlJobSystemDefendRuleResponse.

        规则类型

        :param rule_id: The rule_id of this ShowSqlJobSystemDefendRuleResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def category(self):
        r"""Gets the category of this ShowSqlJobSystemDefendRuleResponse.

        规则状态类型

        :return: The category of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowSqlJobSystemDefendRuleResponse.

        规则状态类型

        :param category: The category of this ShowSqlJobSystemDefendRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def actions(self):
        r"""Gets the actions of this ShowSqlJobSystemDefendRuleResponse.

        可执行的动作

        :return: The actions of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ShowSqlJobSystemDefendRuleResponse.

        可执行的动作

        :param actions: The actions of this ShowSqlJobSystemDefendRuleResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def engines(self):
        r"""Gets the engines of this ShowSqlJobSystemDefendRuleResponse.

        支持的引擎

        :return: The engines of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: list[str]
        """
        return self._engines

    @engines.setter
    def engines(self, engines):
        r"""Sets the engines of this ShowSqlJobSystemDefendRuleResponse.

        支持的引擎

        :param engines: The engines of this ShowSqlJobSystemDefendRuleResponse.
        :type engines: list[str]
        """
        self._engines = engines

    @property
    def no_limit(self):
        r"""Gets the no_limit of this ShowSqlJobSystemDefendRuleResponse.

        规则是否有限制值

        :return: The no_limit of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: bool
        """
        return self._no_limit

    @no_limit.setter
    def no_limit(self, no_limit):
        r"""Sets the no_limit of this ShowSqlJobSystemDefendRuleResponse.

        规则是否有限制值

        :param no_limit: The no_limit of this ShowSqlJobSystemDefendRuleResponse.
        :type no_limit: bool
        """
        self._no_limit = no_limit

    @property
    def desc(self):
        r"""Gets the desc of this ShowSqlJobSystemDefendRuleResponse.

        规则描述

        :return: The desc of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ShowSqlJobSystemDefendRuleResponse.

        规则描述

        :param desc: The desc of this ShowSqlJobSystemDefendRuleResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def param(self):
        r"""Gets the param of this ShowSqlJobSystemDefendRuleResponse.

        :return: The param of this ShowSqlJobSystemDefendRuleResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.SysRuleParam`
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this ShowSqlJobSystemDefendRuleResponse.

        :param param: The param of this ShowSqlJobSystemDefendRuleResponse.
        :type param: :class:`huaweicloudsdkdli.v1.SysRuleParam`
        """
        self._param = param

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
        if not isinstance(other, ShowSqlJobSystemDefendRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
