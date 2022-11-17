# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAndExecuteJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templated': 'bool',
        'created_at': 'int',
        'updated_at': 'int',
        'id': 'str',
        'tenant_id': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'input_id': 'str',
        'output_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'cluster_id': 'str',
        'engine_job_id': 'str',
        'return_code': 'str',
        'is_public': 'bool',
        'is_protected': 'bool',
        'group_id': 'str',
        'jar_path': 'str',
        'input': 'str',
        'output': 'str',
        'job_log': 'str',
        'job_type': 'int',
        'file_action': 'str',
        'arguments': 'str',
        'hql': 'str',
        'job_state': 'int',
        'job_final_status': 'int',
        'hive_script_path': 'str',
        'create_by': 'str',
        'finished_step': 'int',
        'job_main_id': 'str',
        'job_step_id': 'str',
        'postpone_at': 'int',
        'step_name': 'str',
        'step_num': 'int',
        'task_num': 'int',
        'update_by': 'str',
        'credentials': 'str',
        'user_id': 'str',
        'job_configs': 'dict(str, object)',
        'extra': 'dict(str, object)',
        'data_source_urls': 'dict(str, object)',
        'info': 'dict(str, object)'
    }

    attribute_map = {
        'templated': 'templated',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'id': 'id',
        'tenant_id': 'tenant_id',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'input_id': 'input_id',
        'output_id': 'output_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cluster_id': 'cluster_id',
        'engine_job_id': 'engine_job_id',
        'return_code': 'return_code',
        'is_public': 'is_public',
        'is_protected': 'is_protected',
        'group_id': 'group_id',
        'jar_path': 'jar_path',
        'input': 'input',
        'output': 'output',
        'job_log': 'job_log',
        'job_type': 'job_type',
        'file_action': 'file_action',
        'arguments': 'arguments',
        'hql': 'hql',
        'job_state': 'job_state',
        'job_final_status': 'job_final_status',
        'hive_script_path': 'hive_script_path',
        'create_by': 'create_by',
        'finished_step': 'finished_step',
        'job_main_id': 'job_main_id',
        'job_step_id': 'job_step_id',
        'postpone_at': 'postpone_at',
        'step_name': 'step_name',
        'step_num': 'step_num',
        'task_num': 'task_num',
        'update_by': 'update_by',
        'credentials': 'credentials',
        'user_id': 'user_id',
        'job_configs': 'job_configs',
        'extra': 'extra',
        'data_source_urls': 'data_source_urls',
        'info': 'info'
    }

    def __init__(self, templated=None, created_at=None, updated_at=None, id=None, tenant_id=None, job_id=None, job_name=None, input_id=None, output_id=None, start_time=None, end_time=None, cluster_id=None, engine_job_id=None, return_code=None, is_public=None, is_protected=None, group_id=None, jar_path=None, input=None, output=None, job_log=None, job_type=None, file_action=None, arguments=None, hql=None, job_state=None, job_final_status=None, hive_script_path=None, create_by=None, finished_step=None, job_main_id=None, job_step_id=None, postpone_at=None, step_name=None, step_num=None, task_num=None, update_by=None, credentials=None, user_id=None, job_configs=None, extra=None, data_source_urls=None, info=None):
        """CreateAndExecuteJobResponse

        The model defined in huaweicloud sdk

        :param templated: 作业执行对象是否由作业模板生成。
        :type templated: bool
        :param created_at: 作业创建时间，十位时间戳。
        :type created_at: int
        :param updated_at: 作业更新时间，十位时间戳。
        :type updated_at: int
        :param id: 作业ID。
        :type id: str
        :param tenant_id: 项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。
        :type tenant_id: str
        :param job_id: 作业应用ID。
        :type job_id: str
        :param job_name: 作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。
        :type job_name: str
        :param input_id: 数据输入ID。
        :type input_id: str
        :param output_id: 数据输出ID。
        :type output_id: str
        :param start_time: 作业执行开始时间，十位时间戳。
        :type start_time: int
        :param end_time: 作业执行结束时间，十位时间戳。
        :type end_time: int
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param engine_job_id: Oozie工作流ID。
        :type engine_job_id: str
        :param return_code: 运行结果返回码。
        :type return_code: str
        :param is_public: 是否公开。 当前版本不支持该功能。
        :type is_public: bool
        :param is_protected: 是否受保护。 当前版本不支持该功能。
        :type is_protected: bool
        :param group_id: 作业执行组ID。
        :type group_id: str
        :param jar_path: 执行程序Jar包或sql文件地址，需要满足如下要求：  - 最多为1023字符，不能包含;|&amp;&gt;&lt;&#39;$特殊字符，且不可为空或全空格。  - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。  - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。
        :type jar_path: str
        :param input: 数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type input: str
        :param output: 数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type output: str
        :param job_log: 作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&amp;&gt;&#39;&lt;$特殊字符，可为空。
        :type job_log: str
        :param job_type: 作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（该接口当前不支持）  说明： 只有包含Spark和Hive组件的集群才能新增Spark和Hive类型的作业。
        :type job_type: int
        :param file_action: 文件操作类型，包括：  - export：从HDFS导出数据至OBS  - import：从OBS导入数据至HDFS
        :type file_action: str
        :param arguments: 程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&amp;&gt;&#39;&lt;$!\\\&quot;\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username&#x3D;admin @password&#x3D;admin_123
        :type arguments: str
        :param hql: Hive&amp;Spark Sql语句
        :type hql: str
        :param job_state: 作业状态码。  - 1：Terminated - 2：Starting - 3：Running - 4：Completed - 5：Abnormal - 6：Error
        :type job_state: int
        :param job_final_status: 作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消
        :type job_final_status: int
        :param hive_script_path: sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&amp;&gt;&lt;&#39;$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。
        :type hive_script_path: str
        :param create_by: 创建作业的用户ID。  为兼容历史版本，保留此参数。
        :type create_by: str
        :param finished_step: 当前已完成的步骤数。  为兼容历史版本，保留此参数。
        :type finished_step: int
        :param job_main_id: 作业主ID。  为兼容历史版本，保留此参数。
        :type job_main_id: str
        :param job_step_id: 作业步骤ID。  为兼容历史版本，保留此参数。
        :type job_step_id: str
        :param postpone_at: 延迟时间，十位时间戳。  为兼容历史版本，保留此参数。
        :type postpone_at: int
        :param step_name: 作业步骤名。  为兼容历史版本，保留此参数。
        :type step_name: str
        :param step_num: 步骤数量  为兼容历史版本，保留此参数。
        :type step_num: int
        :param task_num: 任务数量。为兼容历史版本，保留此参数。
        :type task_num: int
        :param update_by: 更新作业的用户ID。
        :type update_by: str
        :param credentials: 令牌，当前版本不支持。
        :type credentials: str
        :param user_id: 创建作业的用户ID。  历史版本兼容，不再使用。
        :type user_id: str
        :param job_configs: 键值对集合，用于保存作业运行配置。
        :type job_configs: dict(str, object)
        :param extra: 认证信息，当前版本不支持。
        :type extra: dict(str, object)
        :param data_source_urls: 数据源URL。
        :type data_source_urls: dict(str, object)
        :param info: 键值对集合，包含oozie返回的作业运行信息。
        :type info: dict(str, object)
        """
        
        super(CreateAndExecuteJobResponse, self).__init__()

        self._templated = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._tenant_id = None
        self._job_id = None
        self._job_name = None
        self._input_id = None
        self._output_id = None
        self._start_time = None
        self._end_time = None
        self._cluster_id = None
        self._engine_job_id = None
        self._return_code = None
        self._is_public = None
        self._is_protected = None
        self._group_id = None
        self._jar_path = None
        self._input = None
        self._output = None
        self._job_log = None
        self._job_type = None
        self._file_action = None
        self._arguments = None
        self._hql = None
        self._job_state = None
        self._job_final_status = None
        self._hive_script_path = None
        self._create_by = None
        self._finished_step = None
        self._job_main_id = None
        self._job_step_id = None
        self._postpone_at = None
        self._step_name = None
        self._step_num = None
        self._task_num = None
        self._update_by = None
        self._credentials = None
        self._user_id = None
        self._job_configs = None
        self._extra = None
        self._data_source_urls = None
        self._info = None
        self.discriminator = None

        if templated is not None:
            self.templated = templated
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if input_id is not None:
            self.input_id = input_id
        if output_id is not None:
            self.output_id = output_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if engine_job_id is not None:
            self.engine_job_id = engine_job_id
        if return_code is not None:
            self.return_code = return_code
        if is_public is not None:
            self.is_public = is_public
        if is_protected is not None:
            self.is_protected = is_protected
        if group_id is not None:
            self.group_id = group_id
        if jar_path is not None:
            self.jar_path = jar_path
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if job_log is not None:
            self.job_log = job_log
        if job_type is not None:
            self.job_type = job_type
        if file_action is not None:
            self.file_action = file_action
        if arguments is not None:
            self.arguments = arguments
        if hql is not None:
            self.hql = hql
        if job_state is not None:
            self.job_state = job_state
        if job_final_status is not None:
            self.job_final_status = job_final_status
        if hive_script_path is not None:
            self.hive_script_path = hive_script_path
        if create_by is not None:
            self.create_by = create_by
        if finished_step is not None:
            self.finished_step = finished_step
        if job_main_id is not None:
            self.job_main_id = job_main_id
        if job_step_id is not None:
            self.job_step_id = job_step_id
        if postpone_at is not None:
            self.postpone_at = postpone_at
        if step_name is not None:
            self.step_name = step_name
        if step_num is not None:
            self.step_num = step_num
        if task_num is not None:
            self.task_num = task_num
        if update_by is not None:
            self.update_by = update_by
        if credentials is not None:
            self.credentials = credentials
        if user_id is not None:
            self.user_id = user_id
        if job_configs is not None:
            self.job_configs = job_configs
        if extra is not None:
            self.extra = extra
        if data_source_urls is not None:
            self.data_source_urls = data_source_urls
        if info is not None:
            self.info = info

    @property
    def templated(self):
        """Gets the templated of this CreateAndExecuteJobResponse.

        作业执行对象是否由作业模板生成。

        :return: The templated of this CreateAndExecuteJobResponse.
        :rtype: bool
        """
        return self._templated

    @templated.setter
    def templated(self, templated):
        """Sets the templated of this CreateAndExecuteJobResponse.

        作业执行对象是否由作业模板生成。

        :param templated: The templated of this CreateAndExecuteJobResponse.
        :type templated: bool
        """
        self._templated = templated

    @property
    def created_at(self):
        """Gets the created_at of this CreateAndExecuteJobResponse.

        作业创建时间，十位时间戳。

        :return: The created_at of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateAndExecuteJobResponse.

        作业创建时间，十位时间戳。

        :param created_at: The created_at of this CreateAndExecuteJobResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateAndExecuteJobResponse.

        作业更新时间，十位时间戳。

        :return: The updated_at of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateAndExecuteJobResponse.

        作业更新时间，十位时间戳。

        :param updated_at: The updated_at of this CreateAndExecuteJobResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CreateAndExecuteJobResponse.

        作业ID。

        :return: The id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAndExecuteJobResponse.

        作业ID。

        :param id: The id of this CreateAndExecuteJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateAndExecuteJobResponse.

        项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。

        :return: The tenant_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateAndExecuteJobResponse.

        项目编号。获取方法，请参见[获取项目ID](https://support.huaweicloud.com/api-mrs/mrs_02_0011.html)。

        :param tenant_id: The tenant_id of this CreateAndExecuteJobResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def job_id(self):
        """Gets the job_id of this CreateAndExecuteJobResponse.

        作业应用ID。

        :return: The job_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateAndExecuteJobResponse.

        作业应用ID。

        :param job_id: The job_id of this CreateAndExecuteJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this CreateAndExecuteJobResponse.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。

        :return: The job_name of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CreateAndExecuteJobResponse.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  说明： 不同作业的名称允许相同，但不建议设置相同。

        :param job_name: The job_name of this CreateAndExecuteJobResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def input_id(self):
        """Gets the input_id of this CreateAndExecuteJobResponse.

        数据输入ID。

        :return: The input_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this CreateAndExecuteJobResponse.

        数据输入ID。

        :param input_id: The input_id of this CreateAndExecuteJobResponse.
        :type input_id: str
        """
        self._input_id = input_id

    @property
    def output_id(self):
        """Gets the output_id of this CreateAndExecuteJobResponse.

        数据输出ID。

        :return: The output_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        """Sets the output_id of this CreateAndExecuteJobResponse.

        数据输出ID。

        :param output_id: The output_id of this CreateAndExecuteJobResponse.
        :type output_id: str
        """
        self._output_id = output_id

    @property
    def start_time(self):
        """Gets the start_time of this CreateAndExecuteJobResponse.

        作业执行开始时间，十位时间戳。

        :return: The start_time of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateAndExecuteJobResponse.

        作业执行开始时间，十位时间戳。

        :param start_time: The start_time of this CreateAndExecuteJobResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CreateAndExecuteJobResponse.

        作业执行结束时间，十位时间戳。

        :return: The end_time of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateAndExecuteJobResponse.

        作业执行结束时间，十位时间戳。

        :param end_time: The end_time of this CreateAndExecuteJobResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateAndExecuteJobResponse.

        集群ID。

        :return: The cluster_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateAndExecuteJobResponse.

        集群ID。

        :param cluster_id: The cluster_id of this CreateAndExecuteJobResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def engine_job_id(self):
        """Gets the engine_job_id of this CreateAndExecuteJobResponse.

        Oozie工作流ID。

        :return: The engine_job_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._engine_job_id

    @engine_job_id.setter
    def engine_job_id(self, engine_job_id):
        """Sets the engine_job_id of this CreateAndExecuteJobResponse.

        Oozie工作流ID。

        :param engine_job_id: The engine_job_id of this CreateAndExecuteJobResponse.
        :type engine_job_id: str
        """
        self._engine_job_id = engine_job_id

    @property
    def return_code(self):
        """Gets the return_code of this CreateAndExecuteJobResponse.

        运行结果返回码。

        :return: The return_code of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this CreateAndExecuteJobResponse.

        运行结果返回码。

        :param return_code: The return_code of this CreateAndExecuteJobResponse.
        :type return_code: str
        """
        self._return_code = return_code

    @property
    def is_public(self):
        """Gets the is_public of this CreateAndExecuteJobResponse.

        是否公开。 当前版本不支持该功能。

        :return: The is_public of this CreateAndExecuteJobResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this CreateAndExecuteJobResponse.

        是否公开。 当前版本不支持该功能。

        :param is_public: The is_public of this CreateAndExecuteJobResponse.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def is_protected(self):
        """Gets the is_protected of this CreateAndExecuteJobResponse.

        是否受保护。 当前版本不支持该功能。

        :return: The is_protected of this CreateAndExecuteJobResponse.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """Sets the is_protected of this CreateAndExecuteJobResponse.

        是否受保护。 当前版本不支持该功能。

        :param is_protected: The is_protected of this CreateAndExecuteJobResponse.
        :type is_protected: bool
        """
        self._is_protected = is_protected

    @property
    def group_id(self):
        """Gets the group_id of this CreateAndExecuteJobResponse.

        作业执行组ID。

        :return: The group_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateAndExecuteJobResponse.

        作业执行组ID。

        :param group_id: The group_id of this CreateAndExecuteJobResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def jar_path(self):
        """Gets the jar_path of this CreateAndExecuteJobResponse.

        执行程序Jar包或sql文件地址，需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。  - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。  - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。

        :return: The jar_path of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._jar_path

    @jar_path.setter
    def jar_path(self, jar_path):
        """Sets the jar_path of this CreateAndExecuteJobResponse.

        执行程序Jar包或sql文件地址，需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。  - 需要以“/”或“s3a://”开头。OBS路径不支持KMS加密的文件或程序。  - Spark Script需要以“.sql”结尾，MapReduce和Spark Jar需要以“.jar”结尾，sql和jar不区分大小写。

        :param jar_path: The jar_path of this CreateAndExecuteJobResponse.
        :type jar_path: str
        """
        self._jar_path = jar_path

    @property
    def input(self):
        """Gets the input of this CreateAndExecuteJobResponse.

        数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The input of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateAndExecuteJobResponse.

        数据输入地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，OBS路径不支持KMS加密的文件或程序。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param input: The input of this CreateAndExecuteJobResponse.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateAndExecuteJobResponse.

        数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The output of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateAndExecuteJobResponse.

        数据输出地址，必须以“/”或“s3a://”开头。请配置为正确的OBS路径，如果该路径不存在，系统会自动创建。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param output: The output of this CreateAndExecuteJobResponse.
        :type output: str
        """
        self._output = output

    @property
    def job_log(self):
        """Gets the job_log of this CreateAndExecuteJobResponse.

        作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :return: The job_log of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._job_log

    @job_log.setter
    def job_log(self, job_log):
        """Sets the job_log of this CreateAndExecuteJobResponse.

        作业日志存储地址，该日志信息记录作业运行状态。必须以“/”或“s3a://”开头，请配置为正确的OBS路径。  最多为1023字符，不能包含;|&>'<$特殊字符，可为空。

        :param job_log: The job_log of this CreateAndExecuteJobResponse.
        :type job_log: str
        """
        self._job_log = job_log

    @property
    def job_type(self):
        """Gets the job_type of this CreateAndExecuteJobResponse.

        作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（该接口当前不支持）  说明： 只有包含Spark和Hive组件的集群才能新增Spark和Hive类型的作业。

        :return: The job_type of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this CreateAndExecuteJobResponse.

        作业类型码。 - 1：MapReduce - 2：Spark - 3：Hive Script - 4：HiveSQL（当前不支持） - 5：DistCp，导入、导出数据。 - 6：Spark Script - 7：Spark SQL，提交SQL语句，（该接口当前不支持）  说明： 只有包含Spark和Hive组件的集群才能新增Spark和Hive类型的作业。

        :param job_type: The job_type of this CreateAndExecuteJobResponse.
        :type job_type: int
        """
        self._job_type = job_type

    @property
    def file_action(self):
        """Gets the file_action of this CreateAndExecuteJobResponse.

        文件操作类型，包括：  - export：从HDFS导出数据至OBS  - import：从OBS导入数据至HDFS

        :return: The file_action of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._file_action

    @file_action.setter
    def file_action(self, file_action):
        """Sets the file_action of this CreateAndExecuteJobResponse.

        文件操作类型，包括：  - export：从HDFS导出数据至OBS  - import：从OBS导入数据至HDFS

        :param file_action: The file_action of this CreateAndExecuteJobResponse.
        :type file_action: str
        """
        self._file_action = file_action

    @property
    def arguments(self):
        """Gets the arguments of this CreateAndExecuteJobResponse.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username=admin @password=admin_123

        :return: The arguments of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this CreateAndExecuteJobResponse.

        程序执行的关键参数，该参数由用户程序内的函数指定，MRS只负责参数的传入。 最多为150000字符，不能包含;|&>'<$!\\\"\\特殊字符，可为空。 说明： 用户输入带有敏感信息（如登录密码）的参数时，可通过在参数名前添加“@”的方式，为该参数值加密，以防止敏感信息被明文形式持久化。在查看作业信息时，敏感信息显示为“*”。 例如：username=admin @password=admin_123

        :param arguments: The arguments of this CreateAndExecuteJobResponse.
        :type arguments: str
        """
        self._arguments = arguments

    @property
    def hql(self):
        """Gets the hql of this CreateAndExecuteJobResponse.

        Hive&Spark Sql语句

        :return: The hql of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._hql

    @hql.setter
    def hql(self, hql):
        """Sets the hql of this CreateAndExecuteJobResponse.

        Hive&Spark Sql语句

        :param hql: The hql of this CreateAndExecuteJobResponse.
        :type hql: str
        """
        self._hql = hql

    @property
    def job_state(self):
        """Gets the job_state of this CreateAndExecuteJobResponse.

        作业状态码。  - 1：Terminated - 2：Starting - 3：Running - 4：Completed - 5：Abnormal - 6：Error

        :return: The job_state of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this CreateAndExecuteJobResponse.

        作业状态码。  - 1：Terminated - 2：Starting - 3：Running - 4：Completed - 5：Abnormal - 6：Error

        :param job_state: The job_state of this CreateAndExecuteJobResponse.
        :type job_state: int
        """
        self._job_state = job_state

    @property
    def job_final_status(self):
        """Gets the job_final_status of this CreateAndExecuteJobResponse.

        作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消

        :return: The job_final_status of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._job_final_status

    @job_final_status.setter
    def job_final_status(self, job_final_status):
        """Sets the job_final_status of this CreateAndExecuteJobResponse.

        作业最终状态码。  - 0：未完成 - 1：执行错误，终止执行 - 2：执行完成并且成功 - 3：已取消

        :param job_final_status: The job_final_status of this CreateAndExecuteJobResponse.
        :type job_final_status: int
        """
        self._job_final_status = job_final_status

    @property
    def hive_script_path(self):
        """Gets the hive_script_path of this CreateAndExecuteJobResponse.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。

        :return: The hive_script_path of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._hive_script_path

    @hive_script_path.setter
    def hive_script_path(self, hive_script_path):
        """Sets the hive_script_path of this CreateAndExecuteJobResponse.

        sql程序路径，仅Spark Script和Hive Script作业需要使用此参数。需要满足如下要求：  - 最多为1023字符，不能包含;|&><'$特殊字符，且不可为空或全空格。 - 需要以“/”或“s3a://”开头，OBS路径不支持KMS加密的文件或程序。 - 需要以“.sql”结尾，sql不区分大小写。

        :param hive_script_path: The hive_script_path of this CreateAndExecuteJobResponse.
        :type hive_script_path: str
        """
        self._hive_script_path = hive_script_path

    @property
    def create_by(self):
        """Gets the create_by of this CreateAndExecuteJobResponse.

        创建作业的用户ID。  为兼容历史版本，保留此参数。

        :return: The create_by of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CreateAndExecuteJobResponse.

        创建作业的用户ID。  为兼容历史版本，保留此参数。

        :param create_by: The create_by of this CreateAndExecuteJobResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def finished_step(self):
        """Gets the finished_step of this CreateAndExecuteJobResponse.

        当前已完成的步骤数。  为兼容历史版本，保留此参数。

        :return: The finished_step of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._finished_step

    @finished_step.setter
    def finished_step(self, finished_step):
        """Sets the finished_step of this CreateAndExecuteJobResponse.

        当前已完成的步骤数。  为兼容历史版本，保留此参数。

        :param finished_step: The finished_step of this CreateAndExecuteJobResponse.
        :type finished_step: int
        """
        self._finished_step = finished_step

    @property
    def job_main_id(self):
        """Gets the job_main_id of this CreateAndExecuteJobResponse.

        作业主ID。  为兼容历史版本，保留此参数。

        :return: The job_main_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._job_main_id

    @job_main_id.setter
    def job_main_id(self, job_main_id):
        """Sets the job_main_id of this CreateAndExecuteJobResponse.

        作业主ID。  为兼容历史版本，保留此参数。

        :param job_main_id: The job_main_id of this CreateAndExecuteJobResponse.
        :type job_main_id: str
        """
        self._job_main_id = job_main_id

    @property
    def job_step_id(self):
        """Gets the job_step_id of this CreateAndExecuteJobResponse.

        作业步骤ID。  为兼容历史版本，保留此参数。

        :return: The job_step_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._job_step_id

    @job_step_id.setter
    def job_step_id(self, job_step_id):
        """Sets the job_step_id of this CreateAndExecuteJobResponse.

        作业步骤ID。  为兼容历史版本，保留此参数。

        :param job_step_id: The job_step_id of this CreateAndExecuteJobResponse.
        :type job_step_id: str
        """
        self._job_step_id = job_step_id

    @property
    def postpone_at(self):
        """Gets the postpone_at of this CreateAndExecuteJobResponse.

        延迟时间，十位时间戳。  为兼容历史版本，保留此参数。

        :return: The postpone_at of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._postpone_at

    @postpone_at.setter
    def postpone_at(self, postpone_at):
        """Sets the postpone_at of this CreateAndExecuteJobResponse.

        延迟时间，十位时间戳。  为兼容历史版本，保留此参数。

        :param postpone_at: The postpone_at of this CreateAndExecuteJobResponse.
        :type postpone_at: int
        """
        self._postpone_at = postpone_at

    @property
    def step_name(self):
        """Gets the step_name of this CreateAndExecuteJobResponse.

        作业步骤名。  为兼容历史版本，保留此参数。

        :return: The step_name of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this CreateAndExecuteJobResponse.

        作业步骤名。  为兼容历史版本，保留此参数。

        :param step_name: The step_name of this CreateAndExecuteJobResponse.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def step_num(self):
        """Gets the step_num of this CreateAndExecuteJobResponse.

        步骤数量  为兼容历史版本，保留此参数。

        :return: The step_num of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._step_num

    @step_num.setter
    def step_num(self, step_num):
        """Sets the step_num of this CreateAndExecuteJobResponse.

        步骤数量  为兼容历史版本，保留此参数。

        :param step_num: The step_num of this CreateAndExecuteJobResponse.
        :type step_num: int
        """
        self._step_num = step_num

    @property
    def task_num(self):
        """Gets the task_num of this CreateAndExecuteJobResponse.

        任务数量。为兼容历史版本，保留此参数。

        :return: The task_num of this CreateAndExecuteJobResponse.
        :rtype: int
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        """Sets the task_num of this CreateAndExecuteJobResponse.

        任务数量。为兼容历史版本，保留此参数。

        :param task_num: The task_num of this CreateAndExecuteJobResponse.
        :type task_num: int
        """
        self._task_num = task_num

    @property
    def update_by(self):
        """Gets the update_by of this CreateAndExecuteJobResponse.

        更新作业的用户ID。

        :return: The update_by of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CreateAndExecuteJobResponse.

        更新作业的用户ID。

        :param update_by: The update_by of this CreateAndExecuteJobResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def credentials(self):
        """Gets the credentials of this CreateAndExecuteJobResponse.

        令牌，当前版本不支持。

        :return: The credentials of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreateAndExecuteJobResponse.

        令牌，当前版本不支持。

        :param credentials: The credentials of this CreateAndExecuteJobResponse.
        :type credentials: str
        """
        self._credentials = credentials

    @property
    def user_id(self):
        """Gets the user_id of this CreateAndExecuteJobResponse.

        创建作业的用户ID。  历史版本兼容，不再使用。

        :return: The user_id of this CreateAndExecuteJobResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateAndExecuteJobResponse.

        创建作业的用户ID。  历史版本兼容，不再使用。

        :param user_id: The user_id of this CreateAndExecuteJobResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def job_configs(self):
        """Gets the job_configs of this CreateAndExecuteJobResponse.

        键值对集合，用于保存作业运行配置。

        :return: The job_configs of this CreateAndExecuteJobResponse.
        :rtype: dict(str, object)
        """
        return self._job_configs

    @job_configs.setter
    def job_configs(self, job_configs):
        """Sets the job_configs of this CreateAndExecuteJobResponse.

        键值对集合，用于保存作业运行配置。

        :param job_configs: The job_configs of this CreateAndExecuteJobResponse.
        :type job_configs: dict(str, object)
        """
        self._job_configs = job_configs

    @property
    def extra(self):
        """Gets the extra of this CreateAndExecuteJobResponse.

        认证信息，当前版本不支持。

        :return: The extra of this CreateAndExecuteJobResponse.
        :rtype: dict(str, object)
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this CreateAndExecuteJobResponse.

        认证信息，当前版本不支持。

        :param extra: The extra of this CreateAndExecuteJobResponse.
        :type extra: dict(str, object)
        """
        self._extra = extra

    @property
    def data_source_urls(self):
        """Gets the data_source_urls of this CreateAndExecuteJobResponse.

        数据源URL。

        :return: The data_source_urls of this CreateAndExecuteJobResponse.
        :rtype: dict(str, object)
        """
        return self._data_source_urls

    @data_source_urls.setter
    def data_source_urls(self, data_source_urls):
        """Sets the data_source_urls of this CreateAndExecuteJobResponse.

        数据源URL。

        :param data_source_urls: The data_source_urls of this CreateAndExecuteJobResponse.
        :type data_source_urls: dict(str, object)
        """
        self._data_source_urls = data_source_urls

    @property
    def info(self):
        """Gets the info of this CreateAndExecuteJobResponse.

        键值对集合，包含oozie返回的作业运行信息。

        :return: The info of this CreateAndExecuteJobResponse.
        :rtype: dict(str, object)
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this CreateAndExecuteJobResponse.

        键值对集合，包含oozie返回的作业运行信息。

        :param info: The info of this CreateAndExecuteJobResponse.
        :type info: dict(str, object)
        """
        self._info = info

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
        if not isinstance(other, CreateAndExecuteJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
