# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryFullTextRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'workspace_id': 'str',
        'search_text': 'str',
        'job_type': 'str',
        'script_type': 'str',
        'node_type': 'str',
        'new_save_or_commit': 'str',
        'owners': 'str',
        'doc_types': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'if_query_parameters': 'str',
        'match_type': 'int',
        'schedule_state': 'str',
        'is_exact': 'str',
        'exact_field': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'workspace_id': 'workspace_id',
        'search_text': 'search_text',
        'job_type': 'job_type',
        'script_type': 'script_type',
        'node_type': 'node_type',
        'new_save_or_commit': 'new_save_or_commit',
        'owners': 'owners',
        'doc_types': 'doc_types',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'if_query_parameters': 'if_query_parameters',
        'match_type': 'match_type',
        'schedule_state': 'schedule_state',
        'is_exact': 'is_exact',
        'exact_field': 'exact_field'
    }

    def __init__(self, workspace=None, workspace_id=None, search_text=None, job_type=None, script_type=None, node_type=None, new_save_or_commit=None, owners=None, doc_types=None, begin_time=None, end_time=None, limit=None, offset=None, if_query_parameters=None, match_type=None, schedule_state=None, is_exact=None, exact_field=None):
        r"""ShowFactoryFullTextRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param workspace_id: 搜索空间范围: 默认不传参，在全部空间内搜索。 - 当前工作空间ID: 当前工作空间的ID
        :type workspace_id: str
        :param search_text: 全局搜索关键字，输入至少两位字符。
        :type search_text: str
        :param job_type: 作业类型: （多选）样例: job_type&#x3D;BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业
        :type job_type: str
        :param script_type: 脚本类型: （多选）样例: script_type&#x3D;HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - SparkPython: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python
        :type script_type: str
        :param node_type: 节点类型: （多选）节点类型列表。样例: node_type&#x3D;com.cloud.datacraft.processactivity.ExecuteHiveJob 默认为全部。 - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL - com.cloud.datacraft.activity.DLISQL: DLI SQL - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL - com.cloud.datacraft.processactivity.ExecuteScript: Shell - com.cloud.datacraft.processactivity.ExecutePythonScript: Python - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine - com.cloud.datacraft.activity.DataMigration: DataMigration
        :type node_type: str
        :param new_save_or_commit: 最新修改: 样例: new_save_or_commit&#x3D;save 默认为save: 最新保存 - save: 最新保存 - commit: 最新提交
        :type new_save_or_commit: str
        :param owners: 责任人名称: （多选）人员列表或我的节点。样例: owners&#x3D;dayu_wm 默认不过滤责任人。
        :type owners: str
        :param doc_types: 搜索范围: （多选）样例: doc_types&#x3D;script 默认为全部。 - node: 开发作业 - script: 脚本
        :type doc_types: str
        :param begin_time: 开始时间，配合结束时间参数使用，默认没有时间范围。样例: begin_time&#x3D;1746633600000
        :type begin_time: int
        :param end_time: 结束时间，配合开始时间参数使用，默认没有时间范围。样例: endTime&#x3D;1746806399999
        :type end_time: int
        :param limit: 分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit&#x3D;10 默认值: 10。
        :type limit: int
        :param offset: 分页的起始页，取值范围大于等于0。样例: offset&#x3D;0 默认值: 0。
        :type offset: int
        :param if_query_parameters: 是否搜索配置参数部分的内容: 样例: if_query_parameters&#x3D;false 默认为false: 不搜索配置参数部分的内容 - true: 是 - false: 否
        :type if_query_parameters: str
        :param match_type: 匹配方式: 样例: match_type&#x3D;0 默认为0: 通用。 - 0: 通用 - 1: 模糊
        :type match_type: int
        :param schedule_state: 调度状态: 仅支持作业查找场景，需配置new_save_or_commit参数为commit 默认为全部。 - running: 已调度 - stop: 未调度
        :type schedule_state: str
        :param is_exact: 是否精确搜索: 开启后配合exact_field参数使用。 默认为false: 非精确搜索 - true: 精确搜索 - false: 非精确搜索
        :type is_exact: str
        :param exact_field: 精确查询的字段, 开启精确搜索时生效: - jobName: 作业名 - scriptName: 脚本名 - jobId: 作业ID - scriptId: 脚本ID
        :type exact_field: str
        """
        
        

        self._workspace = None
        self._workspace_id = None
        self._search_text = None
        self._job_type = None
        self._script_type = None
        self._node_type = None
        self._new_save_or_commit = None
        self._owners = None
        self._doc_types = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._if_query_parameters = None
        self._match_type = None
        self._schedule_state = None
        self._is_exact = None
        self._exact_field = None
        self.discriminator = None

        self.workspace = workspace
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.search_text = search_text
        if job_type is not None:
            self.job_type = job_type
        if script_type is not None:
            self.script_type = script_type
        if node_type is not None:
            self.node_type = node_type
        if new_save_or_commit is not None:
            self.new_save_or_commit = new_save_or_commit
        if owners is not None:
            self.owners = owners
        if doc_types is not None:
            self.doc_types = doc_types
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if if_query_parameters is not None:
            self.if_query_parameters = if_query_parameters
        if match_type is not None:
            self.match_type = match_type
        if schedule_state is not None:
            self.schedule_state = schedule_state
        if is_exact is not None:
            self.is_exact = is_exact
        if exact_field is not None:
            self.exact_field = exact_field

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowFactoryFullTextRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowFactoryFullTextRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowFactoryFullTextRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowFactoryFullTextRequest.

        搜索空间范围: 默认不传参，在全部空间内搜索。 - 当前工作空间ID: 当前工作空间的ID

        :return: The workspace_id of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowFactoryFullTextRequest.

        搜索空间范围: 默认不传参，在全部空间内搜索。 - 当前工作空间ID: 当前工作空间的ID

        :param workspace_id: The workspace_id of this ShowFactoryFullTextRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def search_text(self):
        r"""Gets the search_text of this ShowFactoryFullTextRequest.

        全局搜索关键字，输入至少两位字符。

        :return: The search_text of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        r"""Sets the search_text of this ShowFactoryFullTextRequest.

        全局搜索关键字，输入至少两位字符。

        :param search_text: The search_text of this ShowFactoryFullTextRequest.
        :type search_text: str
        """
        self._search_text = search_text

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowFactoryFullTextRequest.

        作业类型: （多选）样例: job_type=BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业

        :return: The job_type of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowFactoryFullTextRequest.

        作业类型: （多选）样例: job_type=BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业

        :param job_type: The job_type of this ShowFactoryFullTextRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def script_type(self):
        r"""Gets the script_type of this ShowFactoryFullTextRequest.

        脚本类型: （多选）样例: script_type=HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - SparkPython: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python

        :return: The script_type of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this ShowFactoryFullTextRequest.

        脚本类型: （多选）样例: script_type=HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - SparkPython: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python

        :param script_type: The script_type of this ShowFactoryFullTextRequest.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def node_type(self):
        r"""Gets the node_type of this ShowFactoryFullTextRequest.

        节点类型: （多选）节点类型列表。样例: node_type=com.cloud.datacraft.processactivity.ExecuteHiveJob 默认为全部。 - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL - com.cloud.datacraft.activity.DLISQL: DLI SQL - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL - com.cloud.datacraft.processactivity.ExecuteScript: Shell - com.cloud.datacraft.processactivity.ExecutePythonScript: Python - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine - com.cloud.datacraft.activity.DataMigration: DataMigration

        :return: The node_type of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ShowFactoryFullTextRequest.

        节点类型: （多选）节点类型列表。样例: node_type=com.cloud.datacraft.processactivity.ExecuteHiveJob 默认为全部。 - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL - com.cloud.datacraft.activity.DLISQL: DLI SQL - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL - com.cloud.datacraft.processactivity.ExecuteScript: Shell - com.cloud.datacraft.processactivity.ExecutePythonScript: Python - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine - com.cloud.datacraft.activity.DataMigration: DataMigration

        :param node_type: The node_type of this ShowFactoryFullTextRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def new_save_or_commit(self):
        r"""Gets the new_save_or_commit of this ShowFactoryFullTextRequest.

        最新修改: 样例: new_save_or_commit=save 默认为save: 最新保存 - save: 最新保存 - commit: 最新提交

        :return: The new_save_or_commit of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._new_save_or_commit

    @new_save_or_commit.setter
    def new_save_or_commit(self, new_save_or_commit):
        r"""Sets the new_save_or_commit of this ShowFactoryFullTextRequest.

        最新修改: 样例: new_save_or_commit=save 默认为save: 最新保存 - save: 最新保存 - commit: 最新提交

        :param new_save_or_commit: The new_save_or_commit of this ShowFactoryFullTextRequest.
        :type new_save_or_commit: str
        """
        self._new_save_or_commit = new_save_or_commit

    @property
    def owners(self):
        r"""Gets the owners of this ShowFactoryFullTextRequest.

        责任人名称: （多选）人员列表或我的节点。样例: owners=dayu_wm 默认不过滤责任人。

        :return: The owners of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        r"""Sets the owners of this ShowFactoryFullTextRequest.

        责任人名称: （多选）人员列表或我的节点。样例: owners=dayu_wm 默认不过滤责任人。

        :param owners: The owners of this ShowFactoryFullTextRequest.
        :type owners: str
        """
        self._owners = owners

    @property
    def doc_types(self):
        r"""Gets the doc_types of this ShowFactoryFullTextRequest.

        搜索范围: （多选）样例: doc_types=script 默认为全部。 - node: 开发作业 - script: 脚本

        :return: The doc_types of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._doc_types

    @doc_types.setter
    def doc_types(self, doc_types):
        r"""Sets the doc_types of this ShowFactoryFullTextRequest.

        搜索范围: （多选）样例: doc_types=script 默认为全部。 - node: 开发作业 - script: 脚本

        :param doc_types: The doc_types of this ShowFactoryFullTextRequest.
        :type doc_types: str
        """
        self._doc_types = doc_types

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowFactoryFullTextRequest.

        开始时间，配合结束时间参数使用，默认没有时间范围。样例: begin_time=1746633600000

        :return: The begin_time of this ShowFactoryFullTextRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowFactoryFullTextRequest.

        开始时间，配合结束时间参数使用，默认没有时间范围。样例: begin_time=1746633600000

        :param begin_time: The begin_time of this ShowFactoryFullTextRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowFactoryFullTextRequest.

        结束时间，配合开始时间参数使用，默认没有时间范围。样例: endTime=1746806399999

        :return: The end_time of this ShowFactoryFullTextRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowFactoryFullTextRequest.

        结束时间，配合开始时间参数使用，默认没有时间范围。样例: endTime=1746806399999

        :param end_time: The end_time of this ShowFactoryFullTextRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ShowFactoryFullTextRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit=10 默认值: 10。

        :return: The limit of this ShowFactoryFullTextRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowFactoryFullTextRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit=10 默认值: 10。

        :param limit: The limit of this ShowFactoryFullTextRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowFactoryFullTextRequest.

        分页的起始页，取值范围大于等于0。样例: offset=0 默认值: 0。

        :return: The offset of this ShowFactoryFullTextRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowFactoryFullTextRequest.

        分页的起始页，取值范围大于等于0。样例: offset=0 默认值: 0。

        :param offset: The offset of this ShowFactoryFullTextRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def if_query_parameters(self):
        r"""Gets the if_query_parameters of this ShowFactoryFullTextRequest.

        是否搜索配置参数部分的内容: 样例: if_query_parameters=false 默认为false: 不搜索配置参数部分的内容 - true: 是 - false: 否

        :return: The if_query_parameters of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._if_query_parameters

    @if_query_parameters.setter
    def if_query_parameters(self, if_query_parameters):
        r"""Sets the if_query_parameters of this ShowFactoryFullTextRequest.

        是否搜索配置参数部分的内容: 样例: if_query_parameters=false 默认为false: 不搜索配置参数部分的内容 - true: 是 - false: 否

        :param if_query_parameters: The if_query_parameters of this ShowFactoryFullTextRequest.
        :type if_query_parameters: str
        """
        self._if_query_parameters = if_query_parameters

    @property
    def match_type(self):
        r"""Gets the match_type of this ShowFactoryFullTextRequest.

        匹配方式: 样例: match_type=0 默认为0: 通用。 - 0: 通用 - 1: 模糊

        :return: The match_type of this ShowFactoryFullTextRequest.
        :rtype: int
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this ShowFactoryFullTextRequest.

        匹配方式: 样例: match_type=0 默认为0: 通用。 - 0: 通用 - 1: 模糊

        :param match_type: The match_type of this ShowFactoryFullTextRequest.
        :type match_type: int
        """
        self._match_type = match_type

    @property
    def schedule_state(self):
        r"""Gets the schedule_state of this ShowFactoryFullTextRequest.

        调度状态: 仅支持作业查找场景，需配置new_save_or_commit参数为commit 默认为全部。 - running: 已调度 - stop: 未调度

        :return: The schedule_state of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._schedule_state

    @schedule_state.setter
    def schedule_state(self, schedule_state):
        r"""Sets the schedule_state of this ShowFactoryFullTextRequest.

        调度状态: 仅支持作业查找场景，需配置new_save_or_commit参数为commit 默认为全部。 - running: 已调度 - stop: 未调度

        :param schedule_state: The schedule_state of this ShowFactoryFullTextRequest.
        :type schedule_state: str
        """
        self._schedule_state = schedule_state

    @property
    def is_exact(self):
        r"""Gets the is_exact of this ShowFactoryFullTextRequest.

        是否精确搜索: 开启后配合exact_field参数使用。 默认为false: 非精确搜索 - true: 精确搜索 - false: 非精确搜索

        :return: The is_exact of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._is_exact

    @is_exact.setter
    def is_exact(self, is_exact):
        r"""Sets the is_exact of this ShowFactoryFullTextRequest.

        是否精确搜索: 开启后配合exact_field参数使用。 默认为false: 非精确搜索 - true: 精确搜索 - false: 非精确搜索

        :param is_exact: The is_exact of this ShowFactoryFullTextRequest.
        :type is_exact: str
        """
        self._is_exact = is_exact

    @property
    def exact_field(self):
        r"""Gets the exact_field of this ShowFactoryFullTextRequest.

        精确查询的字段, 开启精确搜索时生效: - jobName: 作业名 - scriptName: 脚本名 - jobId: 作业ID - scriptId: 脚本ID

        :return: The exact_field of this ShowFactoryFullTextRequest.
        :rtype: str
        """
        return self._exact_field

    @exact_field.setter
    def exact_field(self, exact_field):
        r"""Sets the exact_field of this ShowFactoryFullTextRequest.

        精确查询的字段, 开启精确搜索时生效: - jobName: 作业名 - scriptName: 脚本名 - jobId: 作业ID - scriptId: 脚本ID

        :param exact_field: The exact_field of this ShowFactoryFullTextRequest.
        :type exact_field: str
        """
        self._exact_field = exact_field

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
        if not isinstance(other, ShowFactoryFullTextRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
