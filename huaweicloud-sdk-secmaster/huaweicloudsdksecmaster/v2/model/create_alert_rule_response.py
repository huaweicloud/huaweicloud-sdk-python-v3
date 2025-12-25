# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_rule_id': 'str',
        'alert_rule_name': 'str',
        'script': 'str',
        'status': 'str',
        'directory': 'str',
        'description': 'str',
        'job_mode': 'str',
        'job_mode_setting': 'IsapJobModeSettingVo',
        'job_output_setting': 'AlertRuleJobSetting',
        'process_status': 'str',
        'process_error': 'str',
        'environment': 'str',
        'output_table_id': 'str',
        'output_table_name': 'str',
        'output_table_ids': 'list[str]',
        'output_table_names': 'list[str]',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int',
        'delete_time': 'int'
    }

    attribute_map = {
        'alert_rule_id': 'alert_rule_id',
        'alert_rule_name': 'alert_rule_name',
        'script': 'script',
        'status': 'status',
        'directory': 'directory',
        'description': 'description',
        'job_mode': 'job_mode',
        'job_mode_setting': 'job_mode_setting',
        'job_output_setting': 'job_output_setting',
        'process_status': 'process_status',
        'process_error': 'process_error',
        'environment': 'environment',
        'output_table_id': 'output_table_id',
        'output_table_name': 'output_table_name',
        'output_table_ids': 'output_table_ids',
        'output_table_names': 'output_table_names',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time',
        'delete_time': 'delete_time'
    }

    def __init__(self, alert_rule_id=None, alert_rule_name=None, script=None, status=None, directory=None, description=None, job_mode=None, job_mode_setting=None, job_output_setting=None, process_status=None, process_error=None, environment=None, output_table_id=None, output_table_name=None, output_table_ids=None, output_table_names=None, create_by=None, create_time=None, update_by=None, update_time=None, delete_time=None):
        r"""CreateAlertRuleResponse

        The model defined in huaweicloud sdk

        :param alert_rule_id: UUID
        :type alert_rule_id: str
        :param alert_rule_name: Alert rule name 告警规则名称
        :type alert_rule_name: str
        :param script: Job Script 作业脚本
        :type script: str
        :param status: **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param directory: directory 目录分组
        :type directory: str
        :param description: Alert rule description 告警规则描述
        :type description: str
        :param job_mode: **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  
        :type job_mode: str
        :param job_mode_setting: 
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        :param job_output_setting: 
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.AlertRuleJobSetting`
        :param process_status: **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   
        :type process_status: str
        :param process_error: **参数解释**: 告警规则处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及       
        :type process_error: str
        :param environment: **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     
        :type environment: str
        :param output_table_id: UUID
        :type output_table_id: str
        :param output_table_name: 表名称
        :type output_table_name: str
        :param output_table_ids: 输出表ID列表
        :type output_table_ids: list[str]
        :param output_table_names: 输出表名称列表
        :type output_table_names: list[str]
        :param create_by: 创建者
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param update_by: 更新者
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        super().__init__()

        self._alert_rule_id = None
        self._alert_rule_name = None
        self._script = None
        self._status = None
        self._directory = None
        self._description = None
        self._job_mode = None
        self._job_mode_setting = None
        self._job_output_setting = None
        self._process_status = None
        self._process_error = None
        self._environment = None
        self._output_table_id = None
        self._output_table_name = None
        self._output_table_ids = None
        self._output_table_names = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self._delete_time = None
        self.discriminator = None

        if alert_rule_id is not None:
            self.alert_rule_id = alert_rule_id
        if alert_rule_name is not None:
            self.alert_rule_name = alert_rule_name
        if script is not None:
            self.script = script
        if status is not None:
            self.status = status
        if directory is not None:
            self.directory = directory
        if description is not None:
            self.description = description
        if job_mode is not None:
            self.job_mode = job_mode
        if job_mode_setting is not None:
            self.job_mode_setting = job_mode_setting
        if job_output_setting is not None:
            self.job_output_setting = job_output_setting
        if process_status is not None:
            self.process_status = process_status
        if process_error is not None:
            self.process_error = process_error
        if environment is not None:
            self.environment = environment
        if output_table_id is not None:
            self.output_table_id = output_table_id
        if output_table_name is not None:
            self.output_table_name = output_table_name
        if output_table_ids is not None:
            self.output_table_ids = output_table_ids
        if output_table_names is not None:
            self.output_table_names = output_table_names
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def alert_rule_id(self):
        r"""Gets the alert_rule_id of this CreateAlertRuleResponse.

        UUID

        :return: The alert_rule_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._alert_rule_id

    @alert_rule_id.setter
    def alert_rule_id(self, alert_rule_id):
        r"""Sets the alert_rule_id of this CreateAlertRuleResponse.

        UUID

        :param alert_rule_id: The alert_rule_id of this CreateAlertRuleResponse.
        :type alert_rule_id: str
        """
        self._alert_rule_id = alert_rule_id

    @property
    def alert_rule_name(self):
        r"""Gets the alert_rule_name of this CreateAlertRuleResponse.

        Alert rule name 告警规则名称

        :return: The alert_rule_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._alert_rule_name

    @alert_rule_name.setter
    def alert_rule_name(self, alert_rule_name):
        r"""Sets the alert_rule_name of this CreateAlertRuleResponse.

        Alert rule name 告警规则名称

        :param alert_rule_name: The alert_rule_name of this CreateAlertRuleResponse.
        :type alert_rule_name: str
        """
        self._alert_rule_name = alert_rule_name

    @property
    def script(self):
        r"""Gets the script of this CreateAlertRuleResponse.

        Job Script 作业脚本

        :return: The script of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this CreateAlertRuleResponse.

        Job Script 作业脚本

        :param script: The script of this CreateAlertRuleResponse.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleResponse.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleResponse.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this CreateAlertRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def directory(self):
        r"""Gets the directory of this CreateAlertRuleResponse.

        directory 目录分组

        :return: The directory of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreateAlertRuleResponse.

        directory 目录分组

        :param directory: The directory of this CreateAlertRuleResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def description(self):
        r"""Gets the description of this CreateAlertRuleResponse.

        Alert rule description 告警规则描述

        :return: The description of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertRuleResponse.

        Alert rule description 告警规则描述

        :param description: The description of this CreateAlertRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def job_mode(self):
        r"""Gets the job_mode of this CreateAlertRuleResponse.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :return: The job_mode of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this CreateAlertRuleResponse.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :param job_mode: The job_mode of this CreateAlertRuleResponse.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_mode_setting(self):
        r"""Gets the job_mode_setting of this CreateAlertRuleResponse.

        :return: The job_mode_setting of this CreateAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        """
        return self._job_mode_setting

    @job_mode_setting.setter
    def job_mode_setting(self, job_mode_setting):
        r"""Sets the job_mode_setting of this CreateAlertRuleResponse.

        :param job_mode_setting: The job_mode_setting of this CreateAlertRuleResponse.
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        """
        self._job_mode_setting = job_mode_setting

    @property
    def job_output_setting(self):
        r"""Gets the job_output_setting of this CreateAlertRuleResponse.

        :return: The job_output_setting of this CreateAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.AlertRuleJobSetting`
        """
        return self._job_output_setting

    @job_output_setting.setter
    def job_output_setting(self, job_output_setting):
        r"""Sets the job_output_setting of this CreateAlertRuleResponse.

        :param job_output_setting: The job_output_setting of this CreateAlertRuleResponse.
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.AlertRuleJobSetting`
        """
        self._job_output_setting = job_output_setting

    @property
    def process_status(self):
        r"""Gets the process_status of this CreateAlertRuleResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   

        :return: The process_status of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this CreateAlertRuleResponse.

        **参数解释**: 作业处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及   

        :param process_status: The process_status of this CreateAlertRuleResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def process_error(self):
        r"""Gets the process_error of this CreateAlertRuleResponse.

        **参数解释**: 告警规则处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及       

        :return: The process_error of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this CreateAlertRuleResponse.

        **参数解释**: 告警规则处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及       

        :param process_error: The process_error of this CreateAlertRuleResponse.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def environment(self):
        r"""Gets the environment of this CreateAlertRuleResponse.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :return: The environment of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this CreateAlertRuleResponse.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :param environment: The environment of this CreateAlertRuleResponse.
        :type environment: str
        """
        self._environment = environment

    @property
    def output_table_id(self):
        r"""Gets the output_table_id of this CreateAlertRuleResponse.

        UUID

        :return: The output_table_id of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._output_table_id

    @output_table_id.setter
    def output_table_id(self, output_table_id):
        r"""Sets the output_table_id of this CreateAlertRuleResponse.

        UUID

        :param output_table_id: The output_table_id of this CreateAlertRuleResponse.
        :type output_table_id: str
        """
        self._output_table_id = output_table_id

    @property
    def output_table_name(self):
        r"""Gets the output_table_name of this CreateAlertRuleResponse.

        表名称

        :return: The output_table_name of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._output_table_name

    @output_table_name.setter
    def output_table_name(self, output_table_name):
        r"""Sets the output_table_name of this CreateAlertRuleResponse.

        表名称

        :param output_table_name: The output_table_name of this CreateAlertRuleResponse.
        :type output_table_name: str
        """
        self._output_table_name = output_table_name

    @property
    def output_table_ids(self):
        r"""Gets the output_table_ids of this CreateAlertRuleResponse.

        输出表ID列表

        :return: The output_table_ids of this CreateAlertRuleResponse.
        :rtype: list[str]
        """
        return self._output_table_ids

    @output_table_ids.setter
    def output_table_ids(self, output_table_ids):
        r"""Sets the output_table_ids of this CreateAlertRuleResponse.

        输出表ID列表

        :param output_table_ids: The output_table_ids of this CreateAlertRuleResponse.
        :type output_table_ids: list[str]
        """
        self._output_table_ids = output_table_ids

    @property
    def output_table_names(self):
        r"""Gets the output_table_names of this CreateAlertRuleResponse.

        输出表名称列表

        :return: The output_table_names of this CreateAlertRuleResponse.
        :rtype: list[str]
        """
        return self._output_table_names

    @output_table_names.setter
    def output_table_names(self, output_table_names):
        r"""Sets the output_table_names of this CreateAlertRuleResponse.

        输出表名称列表

        :param output_table_names: The output_table_names of this CreateAlertRuleResponse.
        :type output_table_names: list[str]
        """
        self._output_table_names = output_table_names

    @property
    def create_by(self):
        r"""Gets the create_by of this CreateAlertRuleResponse.

        创建者

        :return: The create_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CreateAlertRuleResponse.

        创建者

        :param create_by: The create_by of this CreateAlertRuleResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :return: The create_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :param create_time: The create_time of this CreateAlertRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this CreateAlertRuleResponse.

        更新者

        :return: The update_by of this CreateAlertRuleResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CreateAlertRuleResponse.

        更新者

        :param update_by: The update_by of this CreateAlertRuleResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :return: The update_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :param update_time: The update_time of this CreateAlertRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def delete_time(self):
        r"""Gets the delete_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :return: The delete_time of this CreateAlertRuleResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this CreateAlertRuleResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this CreateAlertRuleResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("CreateAlertRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
