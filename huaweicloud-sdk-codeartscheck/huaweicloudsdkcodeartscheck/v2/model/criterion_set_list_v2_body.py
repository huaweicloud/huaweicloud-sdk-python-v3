# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CriterionSetListV2Body:

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
        'comments': 'str',
        'type': 'str',
        'creator': 'str',
        'create_time': 'str',
        'last_reviser': 'str',
        'last_update_time': 'str',
        'language': 'str',
        'parent_id': 'str',
        'num_criterion': 'int',
        'can_edit': 'bool',
        'can_delete': 'bool',
        'managers': 'str',
        'parent_set_names': 'str',
        'domain_id': 'str',
        'inherit_mode': 'str',
        'creator_id': 'str',
        'is_system_default': 'str',
        'is_project_default': 'str',
        'is_system_set': 'str',
        'rule_ids': 'str',
        'region': 'str',
        'can_set_default': 'bool',
        'is_used': 'bool',
        'child_sets': 'list[str]',
        'is_reliable': 'bool',
        'is_recommand': 'str',
        'is_default': 'bool',
        'default_set': 'str',
        'dept_id': 'str',
        'dept_name': 'str',
        'reliable_tag': 'str',
        'recommand_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'comments': 'comments',
        'type': 'type',
        'creator': 'creator',
        'create_time': 'createTime',
        'last_reviser': 'lastReviser',
        'last_update_time': 'lastUpdateTime',
        'language': 'language',
        'parent_id': 'parentId',
        'num_criterion': 'numCriterion',
        'can_edit': 'canEdit',
        'can_delete': 'canDelete',
        'managers': 'managers',
        'parent_set_names': 'parentSetNames',
        'domain_id': 'domainId',
        'inherit_mode': 'inheritMode',
        'creator_id': 'creatorId',
        'is_system_default': 'isSystemDefault',
        'is_project_default': 'isProjectDefault',
        'is_system_set': 'isSystemSet',
        'rule_ids': 'ruleIds',
        'region': 'region',
        'can_set_default': 'canSetDefault',
        'is_used': 'isUsed',
        'child_sets': 'childSets',
        'is_reliable': 'isReliable',
        'is_recommand': 'isRecommand',
        'is_default': 'isDefault',
        'default_set': 'defaultSet',
        'dept_id': 'deptId',
        'dept_name': 'deptName',
        'reliable_tag': 'reliableTag',
        'recommand_type': 'recommandType'
    }

    def __init__(self, id=None, name=None, comments=None, type=None, creator=None, create_time=None, last_reviser=None, last_update_time=None, language=None, parent_id=None, num_criterion=None, can_edit=None, can_delete=None, managers=None, parent_set_names=None, domain_id=None, inherit_mode=None, creator_id=None, is_system_default=None, is_project_default=None, is_system_set=None, rule_ids=None, region=None, can_set_default=None, is_used=None, child_sets=None, is_reliable=None, is_recommand=None, is_default=None, default_set=None, dept_id=None, dept_name=None, reliable_tag=None, recommand_type=None):
        r"""CriterionSetListV2Body

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则集ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 规则集中文名称。 **取值范围：** 任意中英文字符，数字，点，连字符和下划线组成的字符串，长度为[1~128]个字符。
        :type name: str
        :param comments: **参数解释：** 规则集中文描述。 **取值范围：** 不涉及。
        :type comments: str
        :param type: **参数解释：** 规则集类型。 **取值范围：** - system：系统规则集。 - custom：自定义规则集。
        :type type: str
        :param creator: **参数解释：** 规则集创建者。 **取值范围：** 用户名。
        :type creator: str
        :param create_time: **参数解释：** 规则集创建时间。 **取值范围：** 0时区标准时间。
        :type create_time: str
        :param last_reviser: **参数解释：** 规则集最近一次更新的操作人。 **取值范围：** 用户名。
        :type last_reviser: str
        :param last_update_time: **参数解释：** 规则集最近一次更新的时间。 **取值范围：** 0时区标准时间。
        :type last_update_time: str
        :param language: **参数解释：** 规则集语言。 **取值范围：** - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES
        :type language: str
        :param parent_id: **参数解释：** 父规则集ID。 **取值范围：** 32位UUID组成的字符串。多个ID之间用逗号分隔。
        :type parent_id: str
        :param num_criterion: **参数解释：** 规则集中已启用的规则数量。 **取值范围：** ≥0
        :type num_criterion: int
        :param can_edit: **参数解释：** 当前用户是否具有修改该规则集的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。
        :type can_edit: bool
        :param can_delete: **参数解释：** 当前用户是否具有删除该规则集的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。
        :type can_delete: bool
        :param managers: **参数解释：** 规则集管理员。 **取值范围：** 用户ID。多个ID用逗号分隔。
        :type managers: str
        :param parent_set_names: **参数解释：** 父规则集的名称。 **取值范围：** 多个规则集名称之间用逗号分隔。
        :type parent_set_names: str
        :param domain_id: **参数解释：** 租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 32位UUID。
        :type domain_id: str
        :param inherit_mode: **参数解释：** 规则集创建时候的继承类型。 **取值范围：** - strong：规则集创建的时候来源于继承。 - null：规则集创建的时候来源于非继承。
        :type inherit_mode: str
        :param creator_id: **参数解释：** 创建者用户ID。 **取值范围：** 32位UUID。
        :type creator_id: str
        :param is_system_default: **参数解释：** 是否为系统默认规则集。 **取值范围：** - 0：否。 - 1：是。
        :type is_system_default: str
        :param is_project_default: **参数解释：** 是否为项目默认规则集。 **取值范围：** - 0：否。 - 1：是。
        :type is_project_default: str
        :param is_system_set: **参数解释：** 是否为系统规则集。 **取值范围：** - 0：否。 - 1：是。
        :type is_system_set: str
        :param rule_ids: **参数解释：** 规则集中已启用的能力规则unique_id。 **取值范围：** unique_id为32位UUID。多个unique_id之间用逗号分隔。
        :type rule_ids: str
        :param region: **参数解释：** 规则集所在局点。 **取值范围：** 不涉及。
        :type region: str
        :param can_set_default: **参数解释：** 是否具有设置默认规则集的权限。 **取值范围：** - true：有权限。 - false：没有权限。
        :type can_set_default: bool
        :param is_used: **参数解释：** 规则集是否被使用。 **取值范围：** - true：规则集被使用。 - false：规则集未被使用。
        :type is_used: bool
        :param child_sets: **参数解释：** 子规则集。 **取值范围：** 不涉及。
        :type child_sets: list[str]
        :param is_reliable: **参数解释：** 是否为可信规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。
        :type is_reliable: bool
        :param is_recommand: **参数解释：** 是否为推荐规则集。该字段已弃用。 **取值范围：** - 1：是。 - 0：否。
        :type is_recommand: str
        :param is_default: **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。
        :type is_default: bool
        :param default_set: **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - \&quot;true\&quot;：是。 - \&quot;false\&quot;：否。
        :type default_set: str
        :param dept_id: **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。
        :type dept_id: str
        :param dept_name: **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。
        :type dept_name: str
        :param reliable_tag: **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。
        :type reliable_tag: str
        :param recommand_type: **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。
        :type recommand_type: str
        """
        
        

        self._id = None
        self._name = None
        self._comments = None
        self._type = None
        self._creator = None
        self._create_time = None
        self._last_reviser = None
        self._last_update_time = None
        self._language = None
        self._parent_id = None
        self._num_criterion = None
        self._can_edit = None
        self._can_delete = None
        self._managers = None
        self._parent_set_names = None
        self._domain_id = None
        self._inherit_mode = None
        self._creator_id = None
        self._is_system_default = None
        self._is_project_default = None
        self._is_system_set = None
        self._rule_ids = None
        self._region = None
        self._can_set_default = None
        self._is_used = None
        self._child_sets = None
        self._is_reliable = None
        self._is_recommand = None
        self._is_default = None
        self._default_set = None
        self._dept_id = None
        self._dept_name = None
        self._reliable_tag = None
        self._recommand_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if comments is not None:
            self.comments = comments
        if type is not None:
            self.type = type
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if last_reviser is not None:
            self.last_reviser = last_reviser
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if language is not None:
            self.language = language
        if parent_id is not None:
            self.parent_id = parent_id
        if num_criterion is not None:
            self.num_criterion = num_criterion
        if can_edit is not None:
            self.can_edit = can_edit
        if can_delete is not None:
            self.can_delete = can_delete
        if managers is not None:
            self.managers = managers
        if parent_set_names is not None:
            self.parent_set_names = parent_set_names
        if domain_id is not None:
            self.domain_id = domain_id
        if inherit_mode is not None:
            self.inherit_mode = inherit_mode
        if creator_id is not None:
            self.creator_id = creator_id
        if is_system_default is not None:
            self.is_system_default = is_system_default
        if is_project_default is not None:
            self.is_project_default = is_project_default
        if is_system_set is not None:
            self.is_system_set = is_system_set
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if region is not None:
            self.region = region
        if can_set_default is not None:
            self.can_set_default = can_set_default
        if is_used is not None:
            self.is_used = is_used
        if child_sets is not None:
            self.child_sets = child_sets
        if is_reliable is not None:
            self.is_reliable = is_reliable
        if is_recommand is not None:
            self.is_recommand = is_recommand
        if is_default is not None:
            self.is_default = is_default
        if default_set is not None:
            self.default_set = default_set
        if dept_id is not None:
            self.dept_id = dept_id
        if dept_name is not None:
            self.dept_name = dept_name
        if reliable_tag is not None:
            self.reliable_tag = reliable_tag
        if recommand_type is not None:
            self.recommand_type = recommand_type

    @property
    def id(self):
        r"""Gets the id of this CriterionSetListV2Body.

        **参数解释：** 规则集ID。 **取值范围：** 不涉及。

        :return: The id of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CriterionSetListV2Body.

        **参数解释：** 规则集ID。 **取值范围：** 不涉及。

        :param id: The id of this CriterionSetListV2Body.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CriterionSetListV2Body.

        **参数解释：** 规则集中文名称。 **取值范围：** 任意中英文字符，数字，点，连字符和下划线组成的字符串，长度为[1~128]个字符。

        :return: The name of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CriterionSetListV2Body.

        **参数解释：** 规则集中文名称。 **取值范围：** 任意中英文字符，数字，点，连字符和下划线组成的字符串，长度为[1~128]个字符。

        :param name: The name of this CriterionSetListV2Body.
        :type name: str
        """
        self._name = name

    @property
    def comments(self):
        r"""Gets the comments of this CriterionSetListV2Body.

        **参数解释：** 规则集中文描述。 **取值范围：** 不涉及。

        :return: The comments of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this CriterionSetListV2Body.

        **参数解释：** 规则集中文描述。 **取值范围：** 不涉及。

        :param comments: The comments of this CriterionSetListV2Body.
        :type comments: str
        """
        self._comments = comments

    @property
    def type(self):
        r"""Gets the type of this CriterionSetListV2Body.

        **参数解释：** 规则集类型。 **取值范围：** - system：系统规则集。 - custom：自定义规则集。

        :return: The type of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CriterionSetListV2Body.

        **参数解释：** 规则集类型。 **取值范围：** - system：系统规则集。 - custom：自定义规则集。

        :param type: The type of this CriterionSetListV2Body.
        :type type: str
        """
        self._type = type

    @property
    def creator(self):
        r"""Gets the creator of this CriterionSetListV2Body.

        **参数解释：** 规则集创建者。 **取值范围：** 用户名。

        :return: The creator of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CriterionSetListV2Body.

        **参数解释：** 规则集创建者。 **取值范围：** 用户名。

        :param creator: The creator of this CriterionSetListV2Body.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this CriterionSetListV2Body.

        **参数解释：** 规则集创建时间。 **取值范围：** 0时区标准时间。

        :return: The create_time of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CriterionSetListV2Body.

        **参数解释：** 规则集创建时间。 **取值范围：** 0时区标准时间。

        :param create_time: The create_time of this CriterionSetListV2Body.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_reviser(self):
        r"""Gets the last_reviser of this CriterionSetListV2Body.

        **参数解释：** 规则集最近一次更新的操作人。 **取值范围：** 用户名。

        :return: The last_reviser of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._last_reviser

    @last_reviser.setter
    def last_reviser(self, last_reviser):
        r"""Sets the last_reviser of this CriterionSetListV2Body.

        **参数解释：** 规则集最近一次更新的操作人。 **取值范围：** 用户名。

        :param last_reviser: The last_reviser of this CriterionSetListV2Body.
        :type last_reviser: str
        """
        self._last_reviser = last_reviser

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this CriterionSetListV2Body.

        **参数解释：** 规则集最近一次更新的时间。 **取值范围：** 0时区标准时间。

        :return: The last_update_time of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this CriterionSetListV2Body.

        **参数解释：** 规则集最近一次更新的时间。 **取值范围：** 0时区标准时间。

        :param last_update_time: The last_update_time of this CriterionSetListV2Body.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def language(self):
        r"""Gets the language of this CriterionSetListV2Body.

        **参数解释：** 规则集语言。 **取值范围：** - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :return: The language of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CriterionSetListV2Body.

        **参数解释：** 规则集语言。 **取值范围：** - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :param language: The language of this CriterionSetListV2Body.
        :type language: str
        """
        self._language = language

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CriterionSetListV2Body.

        **参数解释：** 父规则集ID。 **取值范围：** 32位UUID组成的字符串。多个ID之间用逗号分隔。

        :return: The parent_id of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CriterionSetListV2Body.

        **参数解释：** 父规则集ID。 **取值范围：** 32位UUID组成的字符串。多个ID之间用逗号分隔。

        :param parent_id: The parent_id of this CriterionSetListV2Body.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def num_criterion(self):
        r"""Gets the num_criterion of this CriterionSetListV2Body.

        **参数解释：** 规则集中已启用的规则数量。 **取值范围：** ≥0

        :return: The num_criterion of this CriterionSetListV2Body.
        :rtype: int
        """
        return self._num_criterion

    @num_criterion.setter
    def num_criterion(self, num_criterion):
        r"""Sets the num_criterion of this CriterionSetListV2Body.

        **参数解释：** 规则集中已启用的规则数量。 **取值范围：** ≥0

        :param num_criterion: The num_criterion of this CriterionSetListV2Body.
        :type num_criterion: int
        """
        self._num_criterion = num_criterion

    @property
    def can_edit(self):
        r"""Gets the can_edit of this CriterionSetListV2Body.

        **参数解释：** 当前用户是否具有修改该规则集的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :return: The can_edit of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this CriterionSetListV2Body.

        **参数解释：** 当前用户是否具有修改该规则集的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :param can_edit: The can_edit of this CriterionSetListV2Body.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_delete(self):
        r"""Gets the can_delete of this CriterionSetListV2Body.

        **参数解释：** 当前用户是否具有删除该规则集的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :return: The can_delete of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this CriterionSetListV2Body.

        **参数解释：** 当前用户是否具有删除该规则集的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :param can_delete: The can_delete of this CriterionSetListV2Body.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def managers(self):
        r"""Gets the managers of this CriterionSetListV2Body.

        **参数解释：** 规则集管理员。 **取值范围：** 用户ID。多个ID用逗号分隔。

        :return: The managers of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._managers

    @managers.setter
    def managers(self, managers):
        r"""Sets the managers of this CriterionSetListV2Body.

        **参数解释：** 规则集管理员。 **取值范围：** 用户ID。多个ID用逗号分隔。

        :param managers: The managers of this CriterionSetListV2Body.
        :type managers: str
        """
        self._managers = managers

    @property
    def parent_set_names(self):
        r"""Gets the parent_set_names of this CriterionSetListV2Body.

        **参数解释：** 父规则集的名称。 **取值范围：** 多个规则集名称之间用逗号分隔。

        :return: The parent_set_names of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._parent_set_names

    @parent_set_names.setter
    def parent_set_names(self, parent_set_names):
        r"""Sets the parent_set_names of this CriterionSetListV2Body.

        **参数解释：** 父规则集的名称。 **取值范围：** 多个规则集名称之间用逗号分隔。

        :param parent_set_names: The parent_set_names of this CriterionSetListV2Body.
        :type parent_set_names: str
        """
        self._parent_set_names = parent_set_names

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CriterionSetListV2Body.

        **参数解释：** 租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 32位UUID。

        :return: The domain_id of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CriterionSetListV2Body.

        **参数解释：** 租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 32位UUID。

        :param domain_id: The domain_id of this CriterionSetListV2Body.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def inherit_mode(self):
        r"""Gets the inherit_mode of this CriterionSetListV2Body.

        **参数解释：** 规则集创建时候的继承类型。 **取值范围：** - strong：规则集创建的时候来源于继承。 - null：规则集创建的时候来源于非继承。

        :return: The inherit_mode of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._inherit_mode

    @inherit_mode.setter
    def inherit_mode(self, inherit_mode):
        r"""Sets the inherit_mode of this CriterionSetListV2Body.

        **参数解释：** 规则集创建时候的继承类型。 **取值范围：** - strong：规则集创建的时候来源于继承。 - null：规则集创建的时候来源于非继承。

        :param inherit_mode: The inherit_mode of this CriterionSetListV2Body.
        :type inherit_mode: str
        """
        self._inherit_mode = inherit_mode

    @property
    def creator_id(self):
        r"""Gets the creator_id of this CriterionSetListV2Body.

        **参数解释：** 创建者用户ID。 **取值范围：** 32位UUID。

        :return: The creator_id of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this CriterionSetListV2Body.

        **参数解释：** 创建者用户ID。 **取值范围：** 32位UUID。

        :param creator_id: The creator_id of this CriterionSetListV2Body.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def is_system_default(self):
        r"""Gets the is_system_default of this CriterionSetListV2Body.

        **参数解释：** 是否为系统默认规则集。 **取值范围：** - 0：否。 - 1：是。

        :return: The is_system_default of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._is_system_default

    @is_system_default.setter
    def is_system_default(self, is_system_default):
        r"""Sets the is_system_default of this CriterionSetListV2Body.

        **参数解释：** 是否为系统默认规则集。 **取值范围：** - 0：否。 - 1：是。

        :param is_system_default: The is_system_default of this CriterionSetListV2Body.
        :type is_system_default: str
        """
        self._is_system_default = is_system_default

    @property
    def is_project_default(self):
        r"""Gets the is_project_default of this CriterionSetListV2Body.

        **参数解释：** 是否为项目默认规则集。 **取值范围：** - 0：否。 - 1：是。

        :return: The is_project_default of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._is_project_default

    @is_project_default.setter
    def is_project_default(self, is_project_default):
        r"""Sets the is_project_default of this CriterionSetListV2Body.

        **参数解释：** 是否为项目默认规则集。 **取值范围：** - 0：否。 - 1：是。

        :param is_project_default: The is_project_default of this CriterionSetListV2Body.
        :type is_project_default: str
        """
        self._is_project_default = is_project_default

    @property
    def is_system_set(self):
        r"""Gets the is_system_set of this CriterionSetListV2Body.

        **参数解释：** 是否为系统规则集。 **取值范围：** - 0：否。 - 1：是。

        :return: The is_system_set of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._is_system_set

    @is_system_set.setter
    def is_system_set(self, is_system_set):
        r"""Sets the is_system_set of this CriterionSetListV2Body.

        **参数解释：** 是否为系统规则集。 **取值范围：** - 0：否。 - 1：是。

        :param is_system_set: The is_system_set of this CriterionSetListV2Body.
        :type is_system_set: str
        """
        self._is_system_set = is_system_set

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this CriterionSetListV2Body.

        **参数解释：** 规则集中已启用的能力规则unique_id。 **取值范围：** unique_id为32位UUID。多个unique_id之间用逗号分隔。

        :return: The rule_ids of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this CriterionSetListV2Body.

        **参数解释：** 规则集中已启用的能力规则unique_id。 **取值范围：** unique_id为32位UUID。多个unique_id之间用逗号分隔。

        :param rule_ids: The rule_ids of this CriterionSetListV2Body.
        :type rule_ids: str
        """
        self._rule_ids = rule_ids

    @property
    def region(self):
        r"""Gets the region of this CriterionSetListV2Body.

        **参数解释：** 规则集所在局点。 **取值范围：** 不涉及。

        :return: The region of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CriterionSetListV2Body.

        **参数解释：** 规则集所在局点。 **取值范围：** 不涉及。

        :param region: The region of this CriterionSetListV2Body.
        :type region: str
        """
        self._region = region

    @property
    def can_set_default(self):
        r"""Gets the can_set_default of this CriterionSetListV2Body.

        **参数解释：** 是否具有设置默认规则集的权限。 **取值范围：** - true：有权限。 - false：没有权限。

        :return: The can_set_default of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._can_set_default

    @can_set_default.setter
    def can_set_default(self, can_set_default):
        r"""Sets the can_set_default of this CriterionSetListV2Body.

        **参数解释：** 是否具有设置默认规则集的权限。 **取值范围：** - true：有权限。 - false：没有权限。

        :param can_set_default: The can_set_default of this CriterionSetListV2Body.
        :type can_set_default: bool
        """
        self._can_set_default = can_set_default

    @property
    def is_used(self):
        r"""Gets the is_used of this CriterionSetListV2Body.

        **参数解释：** 规则集是否被使用。 **取值范围：** - true：规则集被使用。 - false：规则集未被使用。

        :return: The is_used of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        r"""Sets the is_used of this CriterionSetListV2Body.

        **参数解释：** 规则集是否被使用。 **取值范围：** - true：规则集被使用。 - false：规则集未被使用。

        :param is_used: The is_used of this CriterionSetListV2Body.
        :type is_used: bool
        """
        self._is_used = is_used

    @property
    def child_sets(self):
        r"""Gets the child_sets of this CriterionSetListV2Body.

        **参数解释：** 子规则集。 **取值范围：** 不涉及。

        :return: The child_sets of this CriterionSetListV2Body.
        :rtype: list[str]
        """
        return self._child_sets

    @child_sets.setter
    def child_sets(self, child_sets):
        r"""Sets the child_sets of this CriterionSetListV2Body.

        **参数解释：** 子规则集。 **取值范围：** 不涉及。

        :param child_sets: The child_sets of this CriterionSetListV2Body.
        :type child_sets: list[str]
        """
        self._child_sets = child_sets

    @property
    def is_reliable(self):
        r"""Gets the is_reliable of this CriterionSetListV2Body.

        **参数解释：** 是否为可信规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。

        :return: The is_reliable of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._is_reliable

    @is_reliable.setter
    def is_reliable(self, is_reliable):
        r"""Sets the is_reliable of this CriterionSetListV2Body.

        **参数解释：** 是否为可信规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。

        :param is_reliable: The is_reliable of this CriterionSetListV2Body.
        :type is_reliable: bool
        """
        self._is_reliable = is_reliable

    @property
    def is_recommand(self):
        r"""Gets the is_recommand of this CriterionSetListV2Body.

        **参数解释：** 是否为推荐规则集。该字段已弃用。 **取值范围：** - 1：是。 - 0：否。

        :return: The is_recommand of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._is_recommand

    @is_recommand.setter
    def is_recommand(self, is_recommand):
        r"""Sets the is_recommand of this CriterionSetListV2Body.

        **参数解释：** 是否为推荐规则集。该字段已弃用。 **取值范围：** - 1：是。 - 0：否。

        :param is_recommand: The is_recommand of this CriterionSetListV2Body.
        :type is_recommand: str
        """
        self._is_recommand = is_recommand

    @property
    def is_default(self):
        r"""Gets the is_default of this CriterionSetListV2Body.

        **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。

        :return: The is_default of this CriterionSetListV2Body.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this CriterionSetListV2Body.

        **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - true：是。 - false：否。

        :param is_default: The is_default of this CriterionSetListV2Body.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def default_set(self):
        r"""Gets the default_set of this CriterionSetListV2Body.

        **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - \"true\"：是。 - \"false\"：否。

        :return: The default_set of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._default_set

    @default_set.setter
    def default_set(self, default_set):
        r"""Sets the default_set of this CriterionSetListV2Body.

        **参数解释：** 是否为默认规则集。该字段已弃用。 **取值范围：** - \"true\"：是。 - \"false\"：否。

        :param default_set: The default_set of this CriterionSetListV2Body.
        :type default_set: str
        """
        self._default_set = default_set

    @property
    def dept_id(self):
        r"""Gets the dept_id of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :return: The dept_id of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._dept_id

    @dept_id.setter
    def dept_id(self, dept_id):
        r"""Sets the dept_id of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :param dept_id: The dept_id of this CriterionSetListV2Body.
        :type dept_id: str
        """
        self._dept_id = dept_id

    @property
    def dept_name(self):
        r"""Gets the dept_name of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :return: The dept_name of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        r"""Sets the dept_name of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :param dept_name: The dept_name of this CriterionSetListV2Body.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def reliable_tag(self):
        r"""Gets the reliable_tag of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :return: The reliable_tag of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._reliable_tag

    @reliable_tag.setter
    def reliable_tag(self, reliable_tag):
        r"""Sets the reliable_tag of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :param reliable_tag: The reliable_tag of this CriterionSetListV2Body.
        :type reliable_tag: str
        """
        self._reliable_tag = reliable_tag

    @property
    def recommand_type(self):
        r"""Gets the recommand_type of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :return: The recommand_type of this CriterionSetListV2Body.
        :rtype: str
        """
        return self._recommand_type

    @recommand_type.setter
    def recommand_type(self, recommand_type):
        r"""Sets the recommand_type of this CriterionSetListV2Body.

        **参数解释：** 该字段已弃用。 **取值范围：** 不涉及。

        :param recommand_type: The recommand_type of this CriterionSetListV2Body.
        :type recommand_type: str
        """
        self._recommand_type = recommand_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CriterionSetListV2Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
