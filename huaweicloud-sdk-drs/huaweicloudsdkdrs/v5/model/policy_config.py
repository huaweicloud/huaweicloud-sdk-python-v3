# coding: utf-8

import six

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
        'dml_types': 'str'
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
        'dml_types': 'dml_types'
    }

    def __init__(self, filter_ddl_policy=None, conflict_policy=None, index_trans=None, ddl_trans=None, data_sync_topology_type=None, support_ddl_info=None, sync_type_policy=None, increment_read_mode=None, dml_types=None):
        """PolicyConfig

        The model defined in huaweicloud sdk

        :param filter_ddl_policy: 过滤DDL策略。取值： - drop_database  场景区别： - 实时迁移场景：MySQL迁移可填\&quot;\&quot;，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填\&quot;drop_database\&quot;。
        :type filter_ddl_policy: str
        :param conflict_policy: 增量阶段冲突策略。该冲突策略特指增量同步中的冲突处理策略,全量阶段的冲突默认忽略。取值： - ignore：忽略。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），DRS将忽略源库的冲突数据，并保留目标库中的冲突数据，继续进行后续同步。  - stop：报错。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），同步任务将失败并立即中止。可在同步日志中查看详细信息。  - overwrite：覆盖。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），将覆盖原来的冲突数据。  场景区别： - 实时迁移场景：不支持。 - 实时同步场景：支持。
        :type conflict_policy: str
        :param index_trans: 对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。
        :type index_trans: bool
        :param ddl_trans: 对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。
        :type ddl_trans: bool
        :param data_sync_topology_type: 数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。
        :type data_sync_topology_type: str
        :param support_ddl_info: 增量支持的DDL。取值： - \&quot;CREATE_TABLE,ADD_COLUMN,MODIFY_COLUMN,CHANGE_COLUMN,DROP_INDEX,ADD_INDEX,CREATE_INDEX,RENAME_INDEX\&quot;。 - 含义解释： - CREATE_TABLE：创建表。 - ADD_COLUMN：加列。 - MODIFY_COLUMN：改列属性。 - CHANGE_COLUMN：改列属性。 - DROP_INDEX：删除索引。 - ADD_INDEX：加索引。 - CREATE_INDEX：创建索引。 - RENAME_INDEX：重命名索引。 - 使用提示： 1.一对一，一对多场景，如果业务上认为源和目标应该使用保持严格一致，那么高危类DDL也应该勾选并同步。 2.一对一，一对多场景，如果业务上确定某个高危DDL不应该发生，则可以不勾选同步高危类DDL，这样DRS将拦截过滤这个DDL，从而起到保护目标数据的作用，但需要知晓过滤DDL的附带问题是可能导致同步失败，例如过滤删列动作。 3.多对一数据聚合场景，最佳实践是推荐只选择同步加列DDL，其他大部分DDL同步都因目标表修改而导致其他任务失败/数据不一致的情况发生，常见情况有：a、同步truncate导致目标数据全部被清空； b、同步创建索引导致目标表被锁定； c、同步rename导致其他任务找不到目标表而失败；d、同步改列导致其他任务因数据类型不兼容而失败；
        :type support_ddl_info: str
        :param sync_type_policy: 同步数据类型。取值：supportAllType（同步所有类型），tableData（同步数据），tableStructure（同步表结构），constraintData（索引同步）。 说明：除supportAllType以外，其他类型可组合填写，例如：\&quot;tableData,tableStructure\&quot; 。
        :type sync_type_policy: str
        :param increment_read_mode: oracle-gausssdb增量读取方式：logminer，xstream
        :type increment_read_mode: str
        :param dml_types: DML同步类型。
        :type dml_types: str
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

    @property
    def filter_ddl_policy(self):
        """Gets the filter_ddl_policy of this PolicyConfig.

        过滤DDL策略。取值： - drop_database  场景区别： - 实时迁移场景：MySQL迁移可填\"\"，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填\"drop_database\"。

        :return: The filter_ddl_policy of this PolicyConfig.
        :rtype: str
        """
        return self._filter_ddl_policy

    @filter_ddl_policy.setter
    def filter_ddl_policy(self, filter_ddl_policy):
        """Sets the filter_ddl_policy of this PolicyConfig.

        过滤DDL策略。取值： - drop_database  场景区别： - 实时迁移场景：MySQL迁移可填\"\"，表示不过滤DROP DATABASE。 - 实时同步场景：MySQL同步只能填\"drop_database\"。

        :param filter_ddl_policy: The filter_ddl_policy of this PolicyConfig.
        :type filter_ddl_policy: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def conflict_policy(self):
        """Gets the conflict_policy of this PolicyConfig.

        增量阶段冲突策略。该冲突策略特指增量同步中的冲突处理策略,全量阶段的冲突默认忽略。取值： - ignore：忽略。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），DRS将忽略源库的冲突数据，并保留目标库中的冲突数据，继续进行后续同步。  - stop：报错。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），同步任务将失败并立即中止。可在同步日志中查看详细信息。  - overwrite：覆盖。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），将覆盖原来的冲突数据。  场景区别： - 实时迁移场景：不支持。 - 实时同步场景：支持。

        :return: The conflict_policy of this PolicyConfig.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        """Sets the conflict_policy of this PolicyConfig.

        增量阶段冲突策略。该冲突策略特指增量同步中的冲突处理策略,全量阶段的冲突默认忽略。取值： - ignore：忽略。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），DRS将忽略源库的冲突数据，并保留目标库中的冲突数据，继续进行后续同步。  - stop：报错。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），同步任务将失败并立即中止。可在同步日志中查看详细信息。  - overwrite：覆盖。当同步数据与目标库已有数据冲突时（主键/唯一键重复等），将覆盖原来的冲突数据。  场景区别： - 实时迁移场景：不支持。 - 实时同步场景：支持。

        :param conflict_policy: The conflict_policy of this PolicyConfig.
        :type conflict_policy: str
        """
        self._conflict_policy = conflict_policy

    @property
    def index_trans(self):
        """Gets the index_trans of this PolicyConfig.

        对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。

        :return: The index_trans of this PolicyConfig.
        :rtype: bool
        """
        return self._index_trans

    @index_trans.setter
    def index_trans(self, index_trans):
        """Sets the index_trans of this PolicyConfig.

        对象同步范围：是否同步普通索引。DRS将默认同步主键/唯一索引，普通索引是指除主键/唯一索引以外的其他类型索引。取值： - true：将会同步全部的索引。 - false：仅同步主键/唯一索引，普通索引不会同步。

        :param index_trans: The index_trans of this PolicyConfig.
        :type index_trans: bool
        """
        self._index_trans = index_trans

    @property
    def ddl_trans(self):
        """Gets the ddl_trans of this PolicyConfig.

        对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。

        :return: The ddl_trans of this PolicyConfig.
        :rtype: bool
        """
        return self._ddl_trans

    @ddl_trans.setter
    def ddl_trans(self, ddl_trans):
        """Sets the ddl_trans of this PolicyConfig.

        对象同步范围：同步增量阶段是否同步DDL。取值： - true：增量阶段同步DDL。 - false：增量阶段不同步DDL。

        :param ddl_trans: The ddl_trans of this PolicyConfig.
        :type ddl_trans: bool
        """
        self._ddl_trans = ddl_trans

    @property
    def data_sync_topology_type(self):
        """Gets the data_sync_topology_type of this PolicyConfig.

        数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。

        :return: The data_sync_topology_type of this PolicyConfig.
        :rtype: str
        """
        return self._data_sync_topology_type

    @data_sync_topology_type.setter
    def data_sync_topology_type(self, data_sync_topology_type):
        """Sets the data_sync_topology_type of this PolicyConfig.

        数据同步拓扑。数据同步功能支持多种同步拓扑，您可以根据业务需求规划您的同步实例。参考链接。取值： - one2one：一对一。 - one2many：一对多。 - many2one：多对一。

        :param data_sync_topology_type: The data_sync_topology_type of this PolicyConfig.
        :type data_sync_topology_type: str
        """
        self._data_sync_topology_type = data_sync_topology_type

    @property
    def support_ddl_info(self):
        """Gets the support_ddl_info of this PolicyConfig.

        增量支持的DDL。取值： - \"CREATE_TABLE,ADD_COLUMN,MODIFY_COLUMN,CHANGE_COLUMN,DROP_INDEX,ADD_INDEX,CREATE_INDEX,RENAME_INDEX\"。 - 含义解释： - CREATE_TABLE：创建表。 - ADD_COLUMN：加列。 - MODIFY_COLUMN：改列属性。 - CHANGE_COLUMN：改列属性。 - DROP_INDEX：删除索引。 - ADD_INDEX：加索引。 - CREATE_INDEX：创建索引。 - RENAME_INDEX：重命名索引。 - 使用提示： 1.一对一，一对多场景，如果业务上认为源和目标应该使用保持严格一致，那么高危类DDL也应该勾选并同步。 2.一对一，一对多场景，如果业务上确定某个高危DDL不应该发生，则可以不勾选同步高危类DDL，这样DRS将拦截过滤这个DDL，从而起到保护目标数据的作用，但需要知晓过滤DDL的附带问题是可能导致同步失败，例如过滤删列动作。 3.多对一数据聚合场景，最佳实践是推荐只选择同步加列DDL，其他大部分DDL同步都因目标表修改而导致其他任务失败/数据不一致的情况发生，常见情况有：a、同步truncate导致目标数据全部被清空； b、同步创建索引导致目标表被锁定； c、同步rename导致其他任务找不到目标表而失败；d、同步改列导致其他任务因数据类型不兼容而失败；

        :return: The support_ddl_info of this PolicyConfig.
        :rtype: str
        """
        return self._support_ddl_info

    @support_ddl_info.setter
    def support_ddl_info(self, support_ddl_info):
        """Sets the support_ddl_info of this PolicyConfig.

        增量支持的DDL。取值： - \"CREATE_TABLE,ADD_COLUMN,MODIFY_COLUMN,CHANGE_COLUMN,DROP_INDEX,ADD_INDEX,CREATE_INDEX,RENAME_INDEX\"。 - 含义解释： - CREATE_TABLE：创建表。 - ADD_COLUMN：加列。 - MODIFY_COLUMN：改列属性。 - CHANGE_COLUMN：改列属性。 - DROP_INDEX：删除索引。 - ADD_INDEX：加索引。 - CREATE_INDEX：创建索引。 - RENAME_INDEX：重命名索引。 - 使用提示： 1.一对一，一对多场景，如果业务上认为源和目标应该使用保持严格一致，那么高危类DDL也应该勾选并同步。 2.一对一，一对多场景，如果业务上确定某个高危DDL不应该发生，则可以不勾选同步高危类DDL，这样DRS将拦截过滤这个DDL，从而起到保护目标数据的作用，但需要知晓过滤DDL的附带问题是可能导致同步失败，例如过滤删列动作。 3.多对一数据聚合场景，最佳实践是推荐只选择同步加列DDL，其他大部分DDL同步都因目标表修改而导致其他任务失败/数据不一致的情况发生，常见情况有：a、同步truncate导致目标数据全部被清空； b、同步创建索引导致目标表被锁定； c、同步rename导致其他任务找不到目标表而失败；d、同步改列导致其他任务因数据类型不兼容而失败；

        :param support_ddl_info: The support_ddl_info of this PolicyConfig.
        :type support_ddl_info: str
        """
        self._support_ddl_info = support_ddl_info

    @property
    def sync_type_policy(self):
        """Gets the sync_type_policy of this PolicyConfig.

        同步数据类型。取值：supportAllType（同步所有类型），tableData（同步数据），tableStructure（同步表结构），constraintData（索引同步）。 说明：除supportAllType以外，其他类型可组合填写，例如：\"tableData,tableStructure\" 。

        :return: The sync_type_policy of this PolicyConfig.
        :rtype: str
        """
        return self._sync_type_policy

    @sync_type_policy.setter
    def sync_type_policy(self, sync_type_policy):
        """Sets the sync_type_policy of this PolicyConfig.

        同步数据类型。取值：supportAllType（同步所有类型），tableData（同步数据），tableStructure（同步表结构），constraintData（索引同步）。 说明：除supportAllType以外，其他类型可组合填写，例如：\"tableData,tableStructure\" 。

        :param sync_type_policy: The sync_type_policy of this PolicyConfig.
        :type sync_type_policy: str
        """
        self._sync_type_policy = sync_type_policy

    @property
    def increment_read_mode(self):
        """Gets the increment_read_mode of this PolicyConfig.

        oracle-gausssdb增量读取方式：logminer，xstream

        :return: The increment_read_mode of this PolicyConfig.
        :rtype: str
        """
        return self._increment_read_mode

    @increment_read_mode.setter
    def increment_read_mode(self, increment_read_mode):
        """Sets the increment_read_mode of this PolicyConfig.

        oracle-gausssdb增量读取方式：logminer，xstream

        :param increment_read_mode: The increment_read_mode of this PolicyConfig.
        :type increment_read_mode: str
        """
        self._increment_read_mode = increment_read_mode

    @property
    def dml_types(self):
        """Gets the dml_types of this PolicyConfig.

        DML同步类型。

        :return: The dml_types of this PolicyConfig.
        :rtype: str
        """
        return self._dml_types

    @dml_types.setter
    def dml_types(self, dml_types):
        """Sets the dml_types of this PolicyConfig.

        DML同步类型。

        :param dml_types: The dml_types of this PolicyConfig.
        :type dml_types: str
        """
        self._dml_types = dml_types

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
        if not isinstance(other, PolicyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
