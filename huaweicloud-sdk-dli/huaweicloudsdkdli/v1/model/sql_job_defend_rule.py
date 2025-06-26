# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJobDefendRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_uuid': 'str',
        'project_id': 'str',
        'rule_name': 'str',
        'rule_id': 'str',
        'category': 'str',
        'engine_rules': 'object',
        'queue_names': 'list[str]',
        'desc': 'str',
        'sys_desc': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'rule_uuid': 'rule_uuid',
        'project_id': 'project_id',
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'category': 'category',
        'engine_rules': 'engine_rules',
        'queue_names': 'queue_names',
        'desc': 'desc',
        'sys_desc': 'sys_desc',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, rule_uuid=None, project_id=None, rule_name=None, rule_id=None, category=None, engine_rules=None, queue_names=None, desc=None, sys_desc=None, create_time=None, update_time=None):
        r"""SqlJobDefendRule

        The model defined in huaweicloud sdk

        :param rule_uuid: 规则唯一标识
        :type rule_uuid: str
        :param project_id: 项目编号
        :type project_id: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_id: 规则类型
        :type rule_id: str
        :param category: 规则状态类型
        :type category: str
        :param engine_rules: 规则详情
        :type engine_rules: object
        :param queue_names: 队列名称
        :type queue_names: list[str]
        :param desc: 用户规则描述
        :type desc: str
        :param sys_desc: 系统规则描述
        :type sys_desc: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._rule_uuid = None
        self._project_id = None
        self._rule_name = None
        self._rule_id = None
        self._category = None
        self._engine_rules = None
        self._queue_names = None
        self._desc = None
        self._sys_desc = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if rule_uuid is not None:
            self.rule_uuid = rule_uuid
        if project_id is not None:
            self.project_id = project_id
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_id is not None:
            self.rule_id = rule_id
        if category is not None:
            self.category = category
        if engine_rules is not None:
            self.engine_rules = engine_rules
        if queue_names is not None:
            self.queue_names = queue_names
        if desc is not None:
            self.desc = desc
        if sys_desc is not None:
            self.sys_desc = sys_desc
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def rule_uuid(self):
        r"""Gets the rule_uuid of this SqlJobDefendRule.

        规则唯一标识

        :return: The rule_uuid of this SqlJobDefendRule.
        :rtype: str
        """
        return self._rule_uuid

    @rule_uuid.setter
    def rule_uuid(self, rule_uuid):
        r"""Sets the rule_uuid of this SqlJobDefendRule.

        规则唯一标识

        :param rule_uuid: The rule_uuid of this SqlJobDefendRule.
        :type rule_uuid: str
        """
        self._rule_uuid = rule_uuid

    @property
    def project_id(self):
        r"""Gets the project_id of this SqlJobDefendRule.

        项目编号

        :return: The project_id of this SqlJobDefendRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SqlJobDefendRule.

        项目编号

        :param project_id: The project_id of this SqlJobDefendRule.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this SqlJobDefendRule.

        规则名称

        :return: The rule_name of this SqlJobDefendRule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this SqlJobDefendRule.

        规则名称

        :param rule_name: The rule_name of this SqlJobDefendRule.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this SqlJobDefendRule.

        规则类型

        :return: The rule_id of this SqlJobDefendRule.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this SqlJobDefendRule.

        规则类型

        :param rule_id: The rule_id of this SqlJobDefendRule.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def category(self):
        r"""Gets the category of this SqlJobDefendRule.

        规则状态类型

        :return: The category of this SqlJobDefendRule.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SqlJobDefendRule.

        规则状态类型

        :param category: The category of this SqlJobDefendRule.
        :type category: str
        """
        self._category = category

    @property
    def engine_rules(self):
        r"""Gets the engine_rules of this SqlJobDefendRule.

        规则详情

        :return: The engine_rules of this SqlJobDefendRule.
        :rtype: object
        """
        return self._engine_rules

    @engine_rules.setter
    def engine_rules(self, engine_rules):
        r"""Sets the engine_rules of this SqlJobDefendRule.

        规则详情

        :param engine_rules: The engine_rules of this SqlJobDefendRule.
        :type engine_rules: object
        """
        self._engine_rules = engine_rules

    @property
    def queue_names(self):
        r"""Gets the queue_names of this SqlJobDefendRule.

        队列名称

        :return: The queue_names of this SqlJobDefendRule.
        :rtype: list[str]
        """
        return self._queue_names

    @queue_names.setter
    def queue_names(self, queue_names):
        r"""Sets the queue_names of this SqlJobDefendRule.

        队列名称

        :param queue_names: The queue_names of this SqlJobDefendRule.
        :type queue_names: list[str]
        """
        self._queue_names = queue_names

    @property
    def desc(self):
        r"""Gets the desc of this SqlJobDefendRule.

        用户规则描述

        :return: The desc of this SqlJobDefendRule.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this SqlJobDefendRule.

        用户规则描述

        :param desc: The desc of this SqlJobDefendRule.
        :type desc: str
        """
        self._desc = desc

    @property
    def sys_desc(self):
        r"""Gets the sys_desc of this SqlJobDefendRule.

        系统规则描述

        :return: The sys_desc of this SqlJobDefendRule.
        :rtype: str
        """
        return self._sys_desc

    @sys_desc.setter
    def sys_desc(self, sys_desc):
        r"""Sets the sys_desc of this SqlJobDefendRule.

        系统规则描述

        :param sys_desc: The sys_desc of this SqlJobDefendRule.
        :type sys_desc: str
        """
        self._sys_desc = sys_desc

    @property
    def create_time(self):
        r"""Gets the create_time of this SqlJobDefendRule.

        创建时间

        :return: The create_time of this SqlJobDefendRule.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SqlJobDefendRule.

        创建时间

        :param create_time: The create_time of this SqlJobDefendRule.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SqlJobDefendRule.

        更新时间

        :return: The update_time of this SqlJobDefendRule.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SqlJobDefendRule.

        更新时间

        :param update_time: The update_time of this SqlJobDefendRule.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, SqlJobDefendRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
