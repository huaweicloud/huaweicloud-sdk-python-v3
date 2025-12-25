# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDataTransformationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_transformation_name': 'str',
        'description': 'str',
        'directory': 'str',
        'script': 'str',
        'status': 'str',
        'belong': 'str',
        'job_mode': 'str',
        'cu_quota_amount': 'float',
        'job_mode_setting': 'IsapJobModeSettingDto',
        'environment': 'str',
        'output_table_id': 'str',
        'output_table_ids': 'list[str]',
        'output_table_names': 'list[str]'
    }

    attribute_map = {
        'data_transformation_name': 'data_transformation_name',
        'description': 'description',
        'directory': 'directory',
        'script': 'script',
        'status': 'status',
        'belong': 'belong',
        'job_mode': 'job_mode',
        'cu_quota_amount': 'cu_quota_amount',
        'job_mode_setting': 'job_mode_setting',
        'environment': 'environment',
        'output_table_id': 'output_table_id',
        'output_table_ids': 'output_table_ids',
        'output_table_names': 'output_table_names'
    }

    def __init__(self, data_transformation_name=None, description=None, directory=None, script=None, status=None, belong=None, job_mode=None, cu_quota_amount=None, job_mode_setting=None, environment=None, output_table_id=None, output_table_ids=None, output_table_names=None):
        r"""UpdateDataTransformationRequestBody

        The model defined in huaweicloud sdk

        :param data_transformation_name: 数据转换名称
        :type data_transformation_name: str
        :param description: 数据转换描述
        :type description: str
        :param directory: directory 目录分组
        :type directory: str
        :param script: Job Script 作业脚本
        :type script: str
        :param status: **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param belong: 归属
        :type belong: str
        :param job_mode: **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  
        :type job_mode: str
        :param cu_quota_amount: cu总量
        :type cu_quota_amount: float
        :param job_mode_setting: 
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        :param environment: **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     
        :type environment: str
        :param output_table_id: UUID
        :type output_table_id: str
        :param output_table_ids: 输出表ID列表
        :type output_table_ids: list[str]
        :param output_table_names: 输出表名称列表
        :type output_table_names: list[str]
        """
        
        

        self._data_transformation_name = None
        self._description = None
        self._directory = None
        self._script = None
        self._status = None
        self._belong = None
        self._job_mode = None
        self._cu_quota_amount = None
        self._job_mode_setting = None
        self._environment = None
        self._output_table_id = None
        self._output_table_ids = None
        self._output_table_names = None
        self.discriminator = None

        if data_transformation_name is not None:
            self.data_transformation_name = data_transformation_name
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if script is not None:
            self.script = script
        if status is not None:
            self.status = status
        if belong is not None:
            self.belong = belong
        if job_mode is not None:
            self.job_mode = job_mode
        if cu_quota_amount is not None:
            self.cu_quota_amount = cu_quota_amount
        if job_mode_setting is not None:
            self.job_mode_setting = job_mode_setting
        if environment is not None:
            self.environment = environment
        if output_table_id is not None:
            self.output_table_id = output_table_id
        if output_table_ids is not None:
            self.output_table_ids = output_table_ids
        if output_table_names is not None:
            self.output_table_names = output_table_names

    @property
    def data_transformation_name(self):
        r"""Gets the data_transformation_name of this UpdateDataTransformationRequestBody.

        数据转换名称

        :return: The data_transformation_name of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._data_transformation_name

    @data_transformation_name.setter
    def data_transformation_name(self, data_transformation_name):
        r"""Sets the data_transformation_name of this UpdateDataTransformationRequestBody.

        数据转换名称

        :param data_transformation_name: The data_transformation_name of this UpdateDataTransformationRequestBody.
        :type data_transformation_name: str
        """
        self._data_transformation_name = data_transformation_name

    @property
    def description(self):
        r"""Gets the description of this UpdateDataTransformationRequestBody.

        数据转换描述

        :return: The description of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateDataTransformationRequestBody.

        数据转换描述

        :param description: The description of this UpdateDataTransformationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this UpdateDataTransformationRequestBody.

        directory 目录分组

        :return: The directory of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdateDataTransformationRequestBody.

        directory 目录分组

        :param directory: The directory of this UpdateDataTransformationRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def script(self):
        r"""Gets the script of this UpdateDataTransformationRequestBody.

        Job Script 作业脚本

        :return: The script of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this UpdateDataTransformationRequestBody.

        Job Script 作业脚本

        :param script: The script of this UpdateDataTransformationRequestBody.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this UpdateDataTransformationRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateDataTransformationRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this UpdateDataTransformationRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def belong(self):
        r"""Gets the belong of this UpdateDataTransformationRequestBody.

        归属

        :return: The belong of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._belong

    @belong.setter
    def belong(self, belong):
        r"""Sets the belong of this UpdateDataTransformationRequestBody.

        归属

        :param belong: The belong of this UpdateDataTransformationRequestBody.
        :type belong: str
        """
        self._belong = belong

    @property
    def job_mode(self):
        r"""Gets the job_mode of this UpdateDataTransformationRequestBody.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :return: The job_mode of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this UpdateDataTransformationRequestBody.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :param job_mode: The job_mode of this UpdateDataTransformationRequestBody.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def cu_quota_amount(self):
        r"""Gets the cu_quota_amount of this UpdateDataTransformationRequestBody.

        cu总量

        :return: The cu_quota_amount of this UpdateDataTransformationRequestBody.
        :rtype: float
        """
        return self._cu_quota_amount

    @cu_quota_amount.setter
    def cu_quota_amount(self, cu_quota_amount):
        r"""Sets the cu_quota_amount of this UpdateDataTransformationRequestBody.

        cu总量

        :param cu_quota_amount: The cu_quota_amount of this UpdateDataTransformationRequestBody.
        :type cu_quota_amount: float
        """
        self._cu_quota_amount = cu_quota_amount

    @property
    def job_mode_setting(self):
        r"""Gets the job_mode_setting of this UpdateDataTransformationRequestBody.

        :return: The job_mode_setting of this UpdateDataTransformationRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        return self._job_mode_setting

    @job_mode_setting.setter
    def job_mode_setting(self, job_mode_setting):
        r"""Sets the job_mode_setting of this UpdateDataTransformationRequestBody.

        :param job_mode_setting: The job_mode_setting of this UpdateDataTransformationRequestBody.
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        self._job_mode_setting = job_mode_setting

    @property
    def environment(self):
        r"""Gets the environment of this UpdateDataTransformationRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :return: The environment of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this UpdateDataTransformationRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :param environment: The environment of this UpdateDataTransformationRequestBody.
        :type environment: str
        """
        self._environment = environment

    @property
    def output_table_id(self):
        r"""Gets the output_table_id of this UpdateDataTransformationRequestBody.

        UUID

        :return: The output_table_id of this UpdateDataTransformationRequestBody.
        :rtype: str
        """
        return self._output_table_id

    @output_table_id.setter
    def output_table_id(self, output_table_id):
        r"""Sets the output_table_id of this UpdateDataTransformationRequestBody.

        UUID

        :param output_table_id: The output_table_id of this UpdateDataTransformationRequestBody.
        :type output_table_id: str
        """
        self._output_table_id = output_table_id

    @property
    def output_table_ids(self):
        r"""Gets the output_table_ids of this UpdateDataTransformationRequestBody.

        输出表ID列表

        :return: The output_table_ids of this UpdateDataTransformationRequestBody.
        :rtype: list[str]
        """
        return self._output_table_ids

    @output_table_ids.setter
    def output_table_ids(self, output_table_ids):
        r"""Sets the output_table_ids of this UpdateDataTransformationRequestBody.

        输出表ID列表

        :param output_table_ids: The output_table_ids of this UpdateDataTransformationRequestBody.
        :type output_table_ids: list[str]
        """
        self._output_table_ids = output_table_ids

    @property
    def output_table_names(self):
        r"""Gets the output_table_names of this UpdateDataTransformationRequestBody.

        输出表名称列表

        :return: The output_table_names of this UpdateDataTransformationRequestBody.
        :rtype: list[str]
        """
        return self._output_table_names

    @output_table_names.setter
    def output_table_names(self, output_table_names):
        r"""Sets the output_table_names of this UpdateDataTransformationRequestBody.

        输出表名称列表

        :param output_table_names: The output_table_names of this UpdateDataTransformationRequestBody.
        :type output_table_names: list[str]
        """
        self._output_table_names = output_table_names

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
        if not isinstance(other, UpdateDataTransformationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
