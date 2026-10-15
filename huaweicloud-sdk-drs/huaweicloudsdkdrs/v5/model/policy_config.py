# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter_ddl_policy': 'str',
        'conflict_policy': 'str',
        'index_trans': 'bool',
        'ddl_trans': 'bool',
        'data_sync_topology_type': 'str',
        'support_ddl_info': 'str',
        'sync_type_policy': 'str',
        'increment_read_mode': 'str',
        'dml_types': 'str',
        'is_create_table_with_index': 'bool'
    }

    attribute_map = {
        'filter_ddl_policy': 'filter_ddl_policy',
        'conflict_policy': 'conflict_policy',
        'index_trans': 'index_trans',
        'ddl_trans': 'ddl_trans',
        'data_sync_topology_type': 'data_sync_topology_type',
        'support_ddl_info': 'support_ddl_info',
        'sync_type_policy': 'sync_type_policy',
        'increment_read_mode': 'increment_read_mode',
        'dml_types': 'dml_types',
        'is_create_table_with_index': 'is_create_table_with_index'
    }

    def __init__(self, filter_ddl_policy=None, conflict_policy=None, index_trans=None, ddl_trans=None, data_sync_topology_type=None, support_ddl_info=None, sync_type_policy=None, increment_read_mode=None, dml_types=None, is_create_table_with_index=None):
        r"""PolicyConfig

        The model defined in huaweicloud sdk

        :param filter_ddl_policy: **参数解释**：  过滤DDL策略，指定增量同步阶段需要过滤的DDL操作类型。  **约束限制**：  - 实时迁移场景：MySQL迁移可填空，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填drop_database。  **取值范围**：  - drop_database：过滤DROP DATABASE操作  **默认取值**：  不涉及
        :type filter_ddl_policy: str
        :param conflict_policy: **参数解释**：  增量阶段冲突策略，指定当目标库已存在相同数据时的处理方式。该冲突策略特指增量同步中的冲突处理策略，全量阶段的冲突默认忽略。  **约束限制**：  - 实时迁移场景：不支持。 - 实时同步场景：支持。  **取值范围**：  - ignore：忽略，保留目标库中的冲突数据，继续进行后续同步 - stop：报错，同步任务将失败并立即中止 - overwrite：覆盖，用源库数据覆盖目标库已有数据  **默认取值**：  不涉及
        :type conflict_policy: str
        :param index_trans: 对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。
        :type index_trans: bool
        :param ddl_trans: 对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。
        :type ddl_trans: bool
        :param data_sync_topology_type: 数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。
        :type data_sync_topology_type: str
        :param support_ddl_info: **参数解释**：  增量支持的DDL，指定增量同步阶段允许同步的DDL操作类型。  **约束限制**：  不涉及。  **取值范围**：  - CREATE_TABLE：创建表 - ADD_COLUMN：加列 - MODIFY_COLUMN：改列属性 - CHANGE_COLUMN：改列属性 - DROP_INDEX：删除索引 - ADD_INDEX：加索引 - CREATE_INDEX：创建索引 - RENAME_INDEX：重命名索引  **默认取值**：  不涉及
        :type support_ddl_info: str
        :param sync_type_policy: **参数解释**：  同步数据类型，指定增量同步阶段需要同步的数据类型范围。  **约束限制**：  不涉及。  **取值范围**：  - supportAllType：同步所有类型 - tableData：同步数据 - tableStructure：同步表结构 - constraintData：索引同步  **默认取值**：  不涉及
        :type sync_type_policy: str
        :param increment_read_mode: **参数解释**：  Oracle-GaussDB增量读取方式，指定Oracle同步到GaussDB时增量数据的读取模式。  **约束限制**：  不涉及。  **取值范围**：  - logminer：Logminer方式 - xstream：Xstream方式  **默认取值**：  不涉及
        :type increment_read_mode: str
        :param dml_types: **参数解释**：  DML同步类型，指定增量同步阶段需要同步的数据操作类型，包括插入、更新和删除操作。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type dml_types: str
        :param is_create_table_with_index: **参数解释**：  索引与表结构是否同时建立，指定在同步过程中创建表时是否同时创建索引。  **约束限制**：  不涉及。  **取值范围**：  - true：索引与表结构同时建立 - false：索引与表结构不同时建立  **默认取值**：  不涉及
        :type is_create_table_with_index: bool
        """
        
        

        self._filter_ddl_policy = None
        self._conflict_policy = None
        self._index_trans = None
        self._ddl_trans = None
        self._data_sync_topology_type = None
        self._support_ddl_info = None
        self._sync_type_policy = None
        self._increment_read_mode = None
        self._dml_types = None
        self._is_create_table_with_index = None
        self.discriminator = None

        if filter_ddl_policy is not None:
            self.filter_ddl_policy = filter_ddl_policy
        if conflict_policy is not None:
            self.conflict_policy = conflict_policy
        if index_trans is not None:
            self.index_trans = index_trans
        if ddl_trans is not None:
            self.ddl_trans = ddl_trans
        if data_sync_topology_type is not None:
            self.data_sync_topology_type = data_sync_topology_type
        if support_ddl_info is not None:
            self.support_ddl_info = support_ddl_info
        if sync_type_policy is not None:
            self.sync_type_policy = sync_type_policy
        if increment_read_mode is not None:
            self.increment_read_mode = increment_read_mode
        if dml_types is not None:
            self.dml_types = dml_types
        if is_create_table_with_index is not None:
            self.is_create_table_with_index = is_create_table_with_index

    @property
    def filter_ddl_policy(self):
        r"""Gets the filter_ddl_policy of this PolicyConfig.

        **参数解释**：  过滤DDL策略，指定增量同步阶段需要过滤的DDL操作类型。  **约束限制**：  - 实时迁移场景：MySQL迁移可填空，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填drop_database。  **取值范围**：  - drop_database：过滤DROP DATABASE操作  **默认取值**：  不涉及

        :return: The filter_ddl_policy of this PolicyConfig.
        :rtype: str
        """
        return self._filter_ddl_policy

    @filter_ddl_policy.setter
    def filter_ddl_policy(self, filter_ddl_policy):
        r"""Sets the filter_ddl_policy of this PolicyConfig.

        **参数解释**：  过滤DDL策略，指定增量同步阶段需要过滤的DDL操作类型。  **约束限制**：  - 实时迁移场景：MySQL迁移可填空，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填drop_database。  **取值范围**：  - drop_database：过滤DROP DATABASE操作  **默认取值**：  不涉及

        :param filter_ddl_policy: The filter_ddl_policy of this PolicyConfig.
        :type filter_ddl_policy: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def conflict_policy(self):
        r"""Gets the conflict_policy of this PolicyConfig.

        **参数解释**：  增量阶段冲突策略，指定当目标库已存在相同数据时的处理方式。该冲突策略特指增量同步中的冲突处理策略，全量阶段的冲突默认忽略。  **约束限制**：  - 实时迁移场景：不支持。 - 实时同步场景：支持。  **取值范围**：  - ignore：忽略，保留目标库中的冲突数据，继续进行后续同步 - stop：报错，同步任务将失败并立即中止 - overwrite：覆盖，用源库数据覆盖目标库已有数据  **默认取值**：  不涉及

        :return: The conflict_policy of this PolicyConfig.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        r"""Sets the conflict_policy of this PolicyConfig.

        **参数解释**：  增量阶段冲突策略，指定当目标库已存在相同数据时的处理方式。该冲突策略特指增量同步中的冲突处理策略，全量阶段的冲突默认忽略。  **约束限制**：  - 实时迁移场景：不支持。 - 实时同步场景：支持。  **取值范围**：  - ignore：忽略，保留目标库中的冲突数据，继续进行后续同步 - stop：报错，同步任务将失败并立即中止 - overwrite：覆盖，用源库数据覆盖目标库已有数据  **默认取值**：  不涉及

        :param conflict_policy: The conflict_policy of this PolicyConfig.
        :type conflict_policy: str
        """
        self._conflict_policy = conflict_policy

    @property
    def index_trans(self):
        r"""Gets the index_trans of this PolicyConfig.

        对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。

        :return: The index_trans of this PolicyConfig.
        :rtype: bool
        """
        return self._index_trans

    @index_trans.setter
    def index_trans(self, index_trans):
        r"""Sets the index_trans of this PolicyConfig.

        对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。

        :param index_trans: The index_trans of this PolicyConfig.
        :type index_trans: bool
        """
        self._index_trans = index_trans

    @property
    def ddl_trans(self):
        r"""Gets the ddl_trans of this PolicyConfig.

        对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。

        :return: The ddl_trans of this PolicyConfig.
        :rtype: bool
        """
        return self._ddl_trans

    @ddl_trans.setter
    def ddl_trans(self, ddl_trans):
        r"""Sets the ddl_trans of this PolicyConfig.

        对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。

        :param ddl_trans: The ddl_trans of this PolicyConfig.
        :type ddl_trans: bool
        """
        self._ddl_trans = ddl_trans

    @property
    def data_sync_topology_type(self):
        r"""Gets the data_sync_topology_type of this PolicyConfig.

        数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。

        :return: The data_sync_topology_type of this PolicyConfig.
        :rtype: str
        """
        return self._data_sync_topology_type

    @data_sync_topology_type.setter
    def data_sync_topology_type(self, data_sync_topology_type):
        r"""Sets the data_sync_topology_type of this PolicyConfig.

        数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。

        :param data_sync_topology_type: The data_sync_topology_type of this PolicyConfig.
        :type data_sync_topology_type: str
        """
        self._data_sync_topology_type = data_sync_topology_type

    @property
    def support_ddl_info(self):
        r"""Gets the support_ddl_info of this PolicyConfig.

        **参数解释**：  增量支持的DDL，指定增量同步阶段允许同步的DDL操作类型。  **约束限制**：  不涉及。  **取值范围**：  - CREATE_TABLE：创建表 - ADD_COLUMN：加列 - MODIFY_COLUMN：改列属性 - CHANGE_COLUMN：改列属性 - DROP_INDEX：删除索引 - ADD_INDEX：加索引 - CREATE_INDEX：创建索引 - RENAME_INDEX：重命名索引  **默认取值**：  不涉及

        :return: The support_ddl_info of this PolicyConfig.
        :rtype: str
        """
        return self._support_ddl_info

    @support_ddl_info.setter
    def support_ddl_info(self, support_ddl_info):
        r"""Sets the support_ddl_info of this PolicyConfig.

        **参数解释**：  增量支持的DDL，指定增量同步阶段允许同步的DDL操作类型。  **约束限制**：  不涉及。  **取值范围**：  - CREATE_TABLE：创建表 - ADD_COLUMN：加列 - MODIFY_COLUMN：改列属性 - CHANGE_COLUMN：改列属性 - DROP_INDEX：删除索引 - ADD_INDEX：加索引 - CREATE_INDEX：创建索引 - RENAME_INDEX：重命名索引  **默认取值**：  不涉及

        :param support_ddl_info: The support_ddl_info of this PolicyConfig.
        :type support_ddl_info: str
        """
        self._support_ddl_info = support_ddl_info

    @property
    def sync_type_policy(self):
        r"""Gets the sync_type_policy of this PolicyConfig.

        **参数解释**：  同步数据类型，指定增量同步阶段需要同步的数据类型范围。  **约束限制**：  不涉及。  **取值范围**：  - supportAllType：同步所有类型 - tableData：同步数据 - tableStructure：同步表结构 - constraintData：索引同步  **默认取值**：  不涉及

        :return: The sync_type_policy of this PolicyConfig.
        :rtype: str
        """
        return self._sync_type_policy

    @sync_type_policy.setter
    def sync_type_policy(self, sync_type_policy):
        r"""Sets the sync_type_policy of this PolicyConfig.

        **参数解释**：  同步数据类型，指定增量同步阶段需要同步的数据类型范围。  **约束限制**：  不涉及。  **取值范围**：  - supportAllType：同步所有类型 - tableData：同步数据 - tableStructure：同步表结构 - constraintData：索引同步  **默认取值**：  不涉及

        :param sync_type_policy: The sync_type_policy of this PolicyConfig.
        :type sync_type_policy: str
        """
        self._sync_type_policy = sync_type_policy

    @property
    def increment_read_mode(self):
        r"""Gets the increment_read_mode of this PolicyConfig.

        **参数解释**：  Oracle-GaussDB增量读取方式，指定Oracle同步到GaussDB时增量数据的读取模式。  **约束限制**：  不涉及。  **取值范围**：  - logminer：Logminer方式 - xstream：Xstream方式  **默认取值**：  不涉及

        :return: The increment_read_mode of this PolicyConfig.
        :rtype: str
        """
        return self._increment_read_mode

    @increment_read_mode.setter
    def increment_read_mode(self, increment_read_mode):
        r"""Sets the increment_read_mode of this PolicyConfig.

        **参数解释**：  Oracle-GaussDB增量读取方式，指定Oracle同步到GaussDB时增量数据的读取模式。  **约束限制**：  不涉及。  **取值范围**：  - logminer：Logminer方式 - xstream：Xstream方式  **默认取值**：  不涉及

        :param increment_read_mode: The increment_read_mode of this PolicyConfig.
        :type increment_read_mode: str
        """
        self._increment_read_mode = increment_read_mode

    @property
    def dml_types(self):
        r"""Gets the dml_types of this PolicyConfig.

        **参数解释**：  DML同步类型，指定增量同步阶段需要同步的数据操作类型，包括插入、更新和删除操作。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The dml_types of this PolicyConfig.
        :rtype: str
        """
        return self._dml_types

    @dml_types.setter
    def dml_types(self, dml_types):
        r"""Sets the dml_types of this PolicyConfig.

        **参数解释**：  DML同步类型，指定增量同步阶段需要同步的数据操作类型，包括插入、更新和删除操作。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param dml_types: The dml_types of this PolicyConfig.
        :type dml_types: str
        """
        self._dml_types = dml_types

    @property
    def is_create_table_with_index(self):
        r"""Gets the is_create_table_with_index of this PolicyConfig.

        **参数解释**：  索引与表结构是否同时建立，指定在同步过程中创建表时是否同时创建索引。  **约束限制**：  不涉及。  **取值范围**：  - true：索引与表结构同时建立 - false：索引与表结构不同时建立  **默认取值**：  不涉及

        :return: The is_create_table_with_index of this PolicyConfig.
        :rtype: bool
        """
        return self._is_create_table_with_index

    @is_create_table_with_index.setter
    def is_create_table_with_index(self, is_create_table_with_index):
        r"""Sets the is_create_table_with_index of this PolicyConfig.

        **参数解释**：  索引与表结构是否同时建立，指定在同步过程中创建表时是否同时创建索引。  **约束限制**：  不涉及。  **取值范围**：  - true：索引与表结构同时建立 - false：索引与表结构不同时建立  **默认取值**：  不涉及

        :param is_create_table_with_index: The is_create_table_with_index of this PolicyConfig.
        :type is_create_table_with_index: bool
        """
        self._is_create_table_with_index = is_create_table_with_index

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
        if not isinstance(other, PolicyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
