# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDetailV2:

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
        'tenant_id': 'str',
        'project_id': 'str',
        'dgc_instance_id': 'str',
        'workspace': 'str',
        'doc_type': 'str',
        'owner': 'str',
        'new_save_or_commit': 'str',
        'version': 'int',
        'last_modified_time': 'int',
        'job_name': 'str',
        'job_type': 'str',
        'job_params': 'str',
        'node_name': 'str',
        'node_type': 'str',
        'script_name': 'str',
        'script_type': 'str',
        'script_params': 'str',
        'cdm_cluster_name': 'str',
        'cdm_job_name': 'str',
        'cdm_params': 'str',
        'workspace_name': 'str',
        'job_id': 'str',
        'script_id': 'str',
        'single_node_job_type': 'str',
        'schedule_state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'dgc_instance_id': 'dgc_instance_id',
        'workspace': 'workspace',
        'doc_type': 'doc_type',
        'owner': 'owner',
        'new_save_or_commit': 'new_save_or_commit',
        'version': 'version',
        'last_modified_time': 'last_modified_time',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'job_params': 'job_params',
        'node_name': 'node_name',
        'node_type': 'node_type',
        'script_name': 'script_name',
        'script_type': 'script_type',
        'script_params': 'script_params',
        'cdm_cluster_name': 'cdm_cluster_name',
        'cdm_job_name': 'cdm_job_name',
        'cdm_params': 'cdm_params',
        'workspace_name': 'workspace_name',
        'job_id': 'job_id',
        'script_id': 'script_id',
        'single_node_job_type': 'single_node_job_type',
        'schedule_state': 'schedule_state'
    }

    def __init__(self, id=None, tenant_id=None, project_id=None, dgc_instance_id=None, workspace=None, doc_type=None, owner=None, new_save_or_commit=None, version=None, last_modified_time=None, job_name=None, job_type=None, job_params=None, node_name=None, node_type=None, script_name=None, script_type=None, script_params=None, cdm_cluster_name=None, cdm_job_name=None, cdm_params=None, workspace_name=None, job_id=None, script_id=None, single_node_job_type=None, schedule_state=None):
        r"""SearchDetailV2

        The model defined in huaweicloud sdk

        :param id: 唯一标识符
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param dgc_instance_id: DGC实例ID
        :type dgc_instance_id: str
        :param workspace: 工作空间ID
        :type workspace: str
        :param doc_type: 搜索范围: （多选） 默认为全部。 - node: 开发作业 - script: 脚本
        :type doc_type: str
        :param owner: 负责人
        :type owner: str
        :param new_save_or_commit: 最新修改:  默认为save: 最新保存 - save: 最新保存 - commit: 最新提交
        :type new_save_or_commit: str
        :param version: 数字版本号或草稿标识
        :type version: int
        :param last_modified_time: 最后修改时间
        :type last_modified_time: int
        :param job_name: 作业名称
        :type job_name: str
        :param job_type: 作业类型: （多选）样例: job_type&#x3D;BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业
        :type job_type: str
        :param job_params: 作业参数
        :type job_params: str
        :param node_name: 节点名称
        :type node_name: str
        :param node_type: 节点类型: （多选）节点类型列表。 默认为全部。   - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL   - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL   - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python   - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL   - com.cloud.datacraft.activity.DLISQL: DLI SQL   - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job   - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL   - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL   - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL   - com.cloud.datacraft.processactivity.ExecuteScript: Shell   - com.cloud.datacraft.processactivity.ExecutePythonScript: Python   - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse   - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine   - com.cloud.datacraft.activity.DataMigration: DataMigration
        :type node_type: str
        :param script_name: 脚本名称
        :type script_name: str
        :param script_type: 脚本类型: （多选）样例: script_type&#x3D;HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - Spark Python: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python
        :type script_type: str
        :param script_params: 脚本参数
        :type script_params: str
        :param cdm_cluster_name: CDM集群名称
        :type cdm_cluster_name: str
        :param cdm_job_name: CDM作业名称
        :type cdm_job_name: str
        :param cdm_params: CDM参数
        :type cdm_params: str
        :param workspace_name: 工作空间名称
        :type workspace_name: str
        :param job_id: 作业ID
        :type job_id: str
        :param script_id: 脚本ID
        :type script_id: str
        :param single_node_job_type: 单节点作业类型
        :type single_node_job_type: str
        :param schedule_state: 调度状态:  默认为全部。 - running: 已调度 - stop: 未调度
        :type schedule_state: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._project_id = None
        self._dgc_instance_id = None
        self._workspace = None
        self._doc_type = None
        self._owner = None
        self._new_save_or_commit = None
        self._version = None
        self._last_modified_time = None
        self._job_name = None
        self._job_type = None
        self._job_params = None
        self._node_name = None
        self._node_type = None
        self._script_name = None
        self._script_type = None
        self._script_params = None
        self._cdm_cluster_name = None
        self._cdm_job_name = None
        self._cdm_params = None
        self._workspace_name = None
        self._job_id = None
        self._script_id = None
        self._single_node_job_type = None
        self._schedule_state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if dgc_instance_id is not None:
            self.dgc_instance_id = dgc_instance_id
        if workspace is not None:
            self.workspace = workspace
        if doc_type is not None:
            self.doc_type = doc_type
        if owner is not None:
            self.owner = owner
        if new_save_or_commit is not None:
            self.new_save_or_commit = new_save_or_commit
        if version is not None:
            self.version = version
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if job_params is not None:
            self.job_params = job_params
        if node_name is not None:
            self.node_name = node_name
        if node_type is not None:
            self.node_type = node_type
        if script_name is not None:
            self.script_name = script_name
        if script_type is not None:
            self.script_type = script_type
        if script_params is not None:
            self.script_params = script_params
        if cdm_cluster_name is not None:
            self.cdm_cluster_name = cdm_cluster_name
        if cdm_job_name is not None:
            self.cdm_job_name = cdm_job_name
        if cdm_params is not None:
            self.cdm_params = cdm_params
        if workspace_name is not None:
            self.workspace_name = workspace_name
        if job_id is not None:
            self.job_id = job_id
        if script_id is not None:
            self.script_id = script_id
        if single_node_job_type is not None:
            self.single_node_job_type = single_node_job_type
        if schedule_state is not None:
            self.schedule_state = schedule_state

    @property
    def id(self):
        r"""Gets the id of this SearchDetailV2.

        唯一标识符

        :return: The id of this SearchDetailV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SearchDetailV2.

        唯一标识符

        :param id: The id of this SearchDetailV2.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this SearchDetailV2.

        租户ID

        :return: The tenant_id of this SearchDetailV2.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this SearchDetailV2.

        租户ID

        :param tenant_id: The tenant_id of this SearchDetailV2.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this SearchDetailV2.

        项目ID

        :return: The project_id of this SearchDetailV2.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SearchDetailV2.

        项目ID

        :param project_id: The project_id of this SearchDetailV2.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dgc_instance_id(self):
        r"""Gets the dgc_instance_id of this SearchDetailV2.

        DGC实例ID

        :return: The dgc_instance_id of this SearchDetailV2.
        :rtype: str
        """
        return self._dgc_instance_id

    @dgc_instance_id.setter
    def dgc_instance_id(self, dgc_instance_id):
        r"""Sets the dgc_instance_id of this SearchDetailV2.

        DGC实例ID

        :param dgc_instance_id: The dgc_instance_id of this SearchDetailV2.
        :type dgc_instance_id: str
        """
        self._dgc_instance_id = dgc_instance_id

    @property
    def workspace(self):
        r"""Gets the workspace of this SearchDetailV2.

        工作空间ID

        :return: The workspace of this SearchDetailV2.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this SearchDetailV2.

        工作空间ID

        :param workspace: The workspace of this SearchDetailV2.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def doc_type(self):
        r"""Gets the doc_type of this SearchDetailV2.

        搜索范围: （多选） 默认为全部。 - node: 开发作业 - script: 脚本

        :return: The doc_type of this SearchDetailV2.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        r"""Sets the doc_type of this SearchDetailV2.

        搜索范围: （多选） 默认为全部。 - node: 开发作业 - script: 脚本

        :param doc_type: The doc_type of this SearchDetailV2.
        :type doc_type: str
        """
        self._doc_type = doc_type

    @property
    def owner(self):
        r"""Gets the owner of this SearchDetailV2.

        负责人

        :return: The owner of this SearchDetailV2.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SearchDetailV2.

        负责人

        :param owner: The owner of this SearchDetailV2.
        :type owner: str
        """
        self._owner = owner

    @property
    def new_save_or_commit(self):
        r"""Gets the new_save_or_commit of this SearchDetailV2.

        最新修改:  默认为save: 最新保存 - save: 最新保存 - commit: 最新提交

        :return: The new_save_or_commit of this SearchDetailV2.
        :rtype: str
        """
        return self._new_save_or_commit

    @new_save_or_commit.setter
    def new_save_or_commit(self, new_save_or_commit):
        r"""Sets the new_save_or_commit of this SearchDetailV2.

        最新修改:  默认为save: 最新保存 - save: 最新保存 - commit: 最新提交

        :param new_save_or_commit: The new_save_or_commit of this SearchDetailV2.
        :type new_save_or_commit: str
        """
        self._new_save_or_commit = new_save_or_commit

    @property
    def version(self):
        r"""Gets the version of this SearchDetailV2.

        数字版本号或草稿标识

        :return: The version of this SearchDetailV2.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SearchDetailV2.

        数字版本号或草稿标识

        :param version: The version of this SearchDetailV2.
        :type version: int
        """
        self._version = version

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this SearchDetailV2.

        最后修改时间

        :return: The last_modified_time of this SearchDetailV2.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this SearchDetailV2.

        最后修改时间

        :param last_modified_time: The last_modified_time of this SearchDetailV2.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def job_name(self):
        r"""Gets the job_name of this SearchDetailV2.

        作业名称

        :return: The job_name of this SearchDetailV2.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this SearchDetailV2.

        作业名称

        :param job_name: The job_name of this SearchDetailV2.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        r"""Gets the job_type of this SearchDetailV2.

        作业类型: （多选）样例: job_type=BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业

        :return: The job_type of this SearchDetailV2.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this SearchDetailV2.

        作业类型: （多选）样例: job_type=BATCH 默认为全部。 - BATCH: 批作业 - REAL_TIME: 流作业

        :param job_type: The job_type of this SearchDetailV2.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_params(self):
        r"""Gets the job_params of this SearchDetailV2.

        作业参数

        :return: The job_params of this SearchDetailV2.
        :rtype: str
        """
        return self._job_params

    @job_params.setter
    def job_params(self, job_params):
        r"""Sets the job_params of this SearchDetailV2.

        作业参数

        :param job_params: The job_params of this SearchDetailV2.
        :type job_params: str
        """
        self._job_params = job_params

    @property
    def node_name(self):
        r"""Gets the node_name of this SearchDetailV2.

        节点名称

        :return: The node_name of this SearchDetailV2.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SearchDetailV2.

        节点名称

        :param node_name: The node_name of this SearchDetailV2.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_type(self):
        r"""Gets the node_type of this SearchDetailV2.

        节点类型: （多选）节点类型列表。 默认为全部。   - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL   - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL   - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python   - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL   - com.cloud.datacraft.activity.DLISQL: DLI SQL   - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job   - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL   - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL   - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL   - com.cloud.datacraft.processactivity.ExecuteScript: Shell   - com.cloud.datacraft.processactivity.ExecutePythonScript: Python   - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse   - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine   - com.cloud.datacraft.activity.DataMigration: DataMigration

        :return: The node_type of this SearchDetailV2.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this SearchDetailV2.

        节点类型: （多选）节点类型列表。 默认为全部。   - com.cloud.datacraft.processactivity.ExecuteHiveJob: MRS Hive SQL   - com.cloud.datacraft.activity.ExecuteSparkSQL: MRS Spark SQL   - com.cloud.datacraft.activity.MRSSparkPython: MRS Spark Python   - com.cloud.datacraft.processactivity.ExecuteImpalaJob: MRS Impala SQL   - com.cloud.datacraft.activity.DLISQL: DLI SQL   - com.cloud.datacraft.activity.DliFlinkJob: DLI Flink Job   - com.cloud.datacraft.processactivity.ExecuteDWSJob: DWS SQL   - com.cloud.datacraft.activity.ExecuteQuery: RDS SQL   - com.cloud.datacraft.activity.MRSPrestoSQL: MRS Presto SQL   - com.cloud.datacraft.processactivity.ExecuteScript: Shell   - com.cloud.datacraft.processactivity.ExecutePythonScript: Python   - com.cloud.datacraft.processactivity.ExecuteClickHouseJob: ClickHouse   - com.cloud.datacraft.processactivity.ExecuteHetuEngineJob: HetuEngine   - com.cloud.datacraft.activity.DataMigration: DataMigration

        :param node_type: The node_type of this SearchDetailV2.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def script_name(self):
        r"""Gets the script_name of this SearchDetailV2.

        脚本名称

        :return: The script_name of this SearchDetailV2.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this SearchDetailV2.

        脚本名称

        :param script_name: The script_name of this SearchDetailV2.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_type(self):
        r"""Gets the script_type of this SearchDetailV2.

        脚本类型: （多选）样例: script_type=HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - Spark Python: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python

        :return: The script_type of this SearchDetailV2.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        r"""Sets the script_type of this SearchDetailV2.

        脚本类型: （多选）样例: script_type=HIVE,DLI。 默认为全部，不过滤任何类型脚本。 - HIVE: Hive SQL - DLI: DLI SQL - DWS: DWS SQL - SparkSQL: Spark SQL - Spark Python: Spark Python - FlinkSQL: Flink SQL - RDS: RDS SQL - PRESTO: Presto SQL - HETUENGINE: HeruEngine - ClickHouse: ClickHouse - IMPALA: Impala SQL - SHELL: Shell - PYTHON: Python

        :param script_type: The script_type of this SearchDetailV2.
        :type script_type: str
        """
        self._script_type = script_type

    @property
    def script_params(self):
        r"""Gets the script_params of this SearchDetailV2.

        脚本参数

        :return: The script_params of this SearchDetailV2.
        :rtype: str
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this SearchDetailV2.

        脚本参数

        :param script_params: The script_params of this SearchDetailV2.
        :type script_params: str
        """
        self._script_params = script_params

    @property
    def cdm_cluster_name(self):
        r"""Gets the cdm_cluster_name of this SearchDetailV2.

        CDM集群名称

        :return: The cdm_cluster_name of this SearchDetailV2.
        :rtype: str
        """
        return self._cdm_cluster_name

    @cdm_cluster_name.setter
    def cdm_cluster_name(self, cdm_cluster_name):
        r"""Sets the cdm_cluster_name of this SearchDetailV2.

        CDM集群名称

        :param cdm_cluster_name: The cdm_cluster_name of this SearchDetailV2.
        :type cdm_cluster_name: str
        """
        self._cdm_cluster_name = cdm_cluster_name

    @property
    def cdm_job_name(self):
        r"""Gets the cdm_job_name of this SearchDetailV2.

        CDM作业名称

        :return: The cdm_job_name of this SearchDetailV2.
        :rtype: str
        """
        return self._cdm_job_name

    @cdm_job_name.setter
    def cdm_job_name(self, cdm_job_name):
        r"""Sets the cdm_job_name of this SearchDetailV2.

        CDM作业名称

        :param cdm_job_name: The cdm_job_name of this SearchDetailV2.
        :type cdm_job_name: str
        """
        self._cdm_job_name = cdm_job_name

    @property
    def cdm_params(self):
        r"""Gets the cdm_params of this SearchDetailV2.

        CDM参数

        :return: The cdm_params of this SearchDetailV2.
        :rtype: str
        """
        return self._cdm_params

    @cdm_params.setter
    def cdm_params(self, cdm_params):
        r"""Sets the cdm_params of this SearchDetailV2.

        CDM参数

        :param cdm_params: The cdm_params of this SearchDetailV2.
        :type cdm_params: str
        """
        self._cdm_params = cdm_params

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this SearchDetailV2.

        工作空间名称

        :return: The workspace_name of this SearchDetailV2.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this SearchDetailV2.

        工作空间名称

        :param workspace_name: The workspace_name of this SearchDetailV2.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def job_id(self):
        r"""Gets the job_id of this SearchDetailV2.

        作业ID

        :return: The job_id of this SearchDetailV2.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SearchDetailV2.

        作业ID

        :param job_id: The job_id of this SearchDetailV2.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def script_id(self):
        r"""Gets the script_id of this SearchDetailV2.

        脚本ID

        :return: The script_id of this SearchDetailV2.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this SearchDetailV2.

        脚本ID

        :param script_id: The script_id of this SearchDetailV2.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def single_node_job_type(self):
        r"""Gets the single_node_job_type of this SearchDetailV2.

        单节点作业类型

        :return: The single_node_job_type of this SearchDetailV2.
        :rtype: str
        """
        return self._single_node_job_type

    @single_node_job_type.setter
    def single_node_job_type(self, single_node_job_type):
        r"""Sets the single_node_job_type of this SearchDetailV2.

        单节点作业类型

        :param single_node_job_type: The single_node_job_type of this SearchDetailV2.
        :type single_node_job_type: str
        """
        self._single_node_job_type = single_node_job_type

    @property
    def schedule_state(self):
        r"""Gets the schedule_state of this SearchDetailV2.

        调度状态:  默认为全部。 - running: 已调度 - stop: 未调度

        :return: The schedule_state of this SearchDetailV2.
        :rtype: str
        """
        return self._schedule_state

    @schedule_state.setter
    def schedule_state(self, schedule_state):
        r"""Sets the schedule_state of this SearchDetailV2.

        调度状态:  默认为全部。 - running: 已调度 - stop: 未调度

        :param schedule_state: The schedule_state of this SearchDetailV2.
        :type schedule_state: str
        """
        self._schedule_state = schedule_state

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
        if not isinstance(other, SearchDetailV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
