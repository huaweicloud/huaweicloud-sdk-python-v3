# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRuleTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accumulated_times': 'int',
        'create_by': 'str',
        'create_time': 'int',
        'cu_quota_amount': 'float',
        'description': 'str',
        'environment': 'str',
        'job_mode': 'str',
        'job_mode_setting': 'IsapJobModeSettingVo',
        'job_output_setting': 'IsapJobOutputSetting',
        'process_error': 'str',
        'process_status': 'str',
        'query_type': 'str',
        'script': 'str',
        'status': 'str',
        'table_name': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'triggers': 'list[Trigger]',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'accumulated_times': 'accumulated_times',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'cu_quota_amount': 'cu_quota_amount',
        'description': 'description',
        'environment': 'environment',
        'job_mode': 'job_mode',
        'job_mode_setting': 'job_mode_setting',
        'job_output_setting': 'job_output_setting',
        'process_error': 'process_error',
        'process_status': 'process_status',
        'query_type': 'query_type',
        'script': 'script',
        'status': 'status',
        'table_name': 'table_name',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'triggers': 'triggers',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, accumulated_times=None, create_by=None, create_time=None, cu_quota_amount=None, description=None, environment=None, job_mode=None, job_mode_setting=None, job_output_setting=None, process_error=None, process_status=None, query_type=None, script=None, status=None, table_name=None, template_id=None, template_name=None, triggers=None, update_by=None, update_time=None):
        r"""ShowAlertRuleTemplateResponse

        The model defined in huaweicloud sdk

        :param accumulated_times: 累计次数
        :type accumulated_times: int
        :param create_by: UUID
        :type create_by: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param cu_quota_amount: 数量
        :type cu_quota_amount: float
        :param description: 告警规则模板描述
        :type description: str
        :param environment: **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     
        :type environment: str
        :param job_mode: **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  
        :type job_mode: str
        :param job_mode_setting: 
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        :param job_output_setting: 
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        :param process_error: **参数解释**: 处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及      
        :type process_error: str
        :param process_status: **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         
        :type process_status: str
        :param query_type: **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        
        :type query_type: str
        :param script: Script 脚本
        :type script: str
        :param status: **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param table_name: 表名称
        :type table_name: str
        :param template_id: UUID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param triggers: 触发器数组
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        :param update_by: UUID
        :type update_by: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        """
        
        super().__init__()

        self._accumulated_times = None
        self._create_by = None
        self._create_time = None
        self._cu_quota_amount = None
        self._description = None
        self._environment = None
        self._job_mode = None
        self._job_mode_setting = None
        self._job_output_setting = None
        self._process_error = None
        self._process_status = None
        self._query_type = None
        self._script = None
        self._status = None
        self._table_name = None
        self._template_id = None
        self._template_name = None
        self._triggers = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if accumulated_times is not None:
            self.accumulated_times = accumulated_times
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if cu_quota_amount is not None:
            self.cu_quota_amount = cu_quota_amount
        if description is not None:
            self.description = description
        if environment is not None:
            self.environment = environment
        if job_mode is not None:
            self.job_mode = job_mode
        if job_mode_setting is not None:
            self.job_mode_setting = job_mode_setting
        if job_output_setting is not None:
            self.job_output_setting = job_output_setting
        if process_error is not None:
            self.process_error = process_error
        if process_status is not None:
            self.process_status = process_status
        if query_type is not None:
            self.query_type = query_type
        if script is not None:
            self.script = script
        if status is not None:
            self.status = status
        if table_name is not None:
            self.table_name = table_name
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if triggers is not None:
            self.triggers = triggers
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def accumulated_times(self):
        r"""Gets the accumulated_times of this ShowAlertRuleTemplateResponse.

        累计次数

        :return: The accumulated_times of this ShowAlertRuleTemplateResponse.
        :rtype: int
        """
        return self._accumulated_times

    @accumulated_times.setter
    def accumulated_times(self, accumulated_times):
        r"""Sets the accumulated_times of this ShowAlertRuleTemplateResponse.

        累计次数

        :param accumulated_times: The accumulated_times of this ShowAlertRuleTemplateResponse.
        :type accumulated_times: int
        """
        self._accumulated_times = accumulated_times

    @property
    def create_by(self):
        r"""Gets the create_by of this ShowAlertRuleTemplateResponse.

        UUID

        :return: The create_by of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ShowAlertRuleTemplateResponse.

        UUID

        :param create_by: The create_by of this ShowAlertRuleTemplateResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowAlertRuleTemplateResponse.

        毫秒时间戳

        :return: The create_time of this ShowAlertRuleTemplateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowAlertRuleTemplateResponse.

        毫秒时间戳

        :param create_time: The create_time of this ShowAlertRuleTemplateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def cu_quota_amount(self):
        r"""Gets the cu_quota_amount of this ShowAlertRuleTemplateResponse.

        数量

        :return: The cu_quota_amount of this ShowAlertRuleTemplateResponse.
        :rtype: float
        """
        return self._cu_quota_amount

    @cu_quota_amount.setter
    def cu_quota_amount(self, cu_quota_amount):
        r"""Sets the cu_quota_amount of this ShowAlertRuleTemplateResponse.

        数量

        :param cu_quota_amount: The cu_quota_amount of this ShowAlertRuleTemplateResponse.
        :type cu_quota_amount: float
        """
        self._cu_quota_amount = cu_quota_amount

    @property
    def description(self):
        r"""Gets the description of this ShowAlertRuleTemplateResponse.

        告警规则模板描述

        :return: The description of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowAlertRuleTemplateResponse.

        告警规则模板描述

        :param description: The description of this ShowAlertRuleTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def environment(self):
        r"""Gets the environment of this ShowAlertRuleTemplateResponse.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :return: The environment of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this ShowAlertRuleTemplateResponse.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :param environment: The environment of this ShowAlertRuleTemplateResponse.
        :type environment: str
        """
        self._environment = environment

    @property
    def job_mode(self):
        r"""Gets the job_mode of this ShowAlertRuleTemplateResponse.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :return: The job_mode of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this ShowAlertRuleTemplateResponse.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :param job_mode: The job_mode of this ShowAlertRuleTemplateResponse.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_mode_setting(self):
        r"""Gets the job_mode_setting of this ShowAlertRuleTemplateResponse.

        :return: The job_mode_setting of this ShowAlertRuleTemplateResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        """
        return self._job_mode_setting

    @job_mode_setting.setter
    def job_mode_setting(self, job_mode_setting):
        r"""Sets the job_mode_setting of this ShowAlertRuleTemplateResponse.

        :param job_mode_setting: The job_mode_setting of this ShowAlertRuleTemplateResponse.
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingVo`
        """
        self._job_mode_setting = job_mode_setting

    @property
    def job_output_setting(self):
        r"""Gets the job_output_setting of this ShowAlertRuleTemplateResponse.

        :return: The job_output_setting of this ShowAlertRuleTemplateResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        return self._job_output_setting

    @job_output_setting.setter
    def job_output_setting(self, job_output_setting):
        r"""Sets the job_output_setting of this ShowAlertRuleTemplateResponse.

        :param job_output_setting: The job_output_setting of this ShowAlertRuleTemplateResponse.
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        self._job_output_setting = job_output_setting

    @property
    def process_error(self):
        r"""Gets the process_error of this ShowAlertRuleTemplateResponse.

        **参数解释**: 处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及      

        :return: The process_error of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._process_error

    @process_error.setter
    def process_error(self, process_error):
        r"""Sets the process_error of this ShowAlertRuleTemplateResponse.

        **参数解释**: 处理错误 - NONE 无  **约束限制** 不涉及 **取值范围**: - NONE  **默认值** 不涉及      

        :param process_error: The process_error of this ShowAlertRuleTemplateResponse.
        :type process_error: str
        """
        self._process_error = process_error

    @property
    def process_status(self):
        r"""Gets the process_status of this ShowAlertRuleTemplateResponse.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         

        :return: The process_status of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this ShowAlertRuleTemplateResponse.

        **参数解释**: 处理状态 - COMPLETED 已完成 - CREATING 创建中 - UPDATING 更新中 - ENABLING 启用中 - DISABLING 停用中 - DELETING 删除中 - CREATE_FAILED 创建失败 - UPDATE_FAILED 更新失败 - ENABLE_FAILED 启用失败 - DISABLE_FAILED 停用失败 - DELETE_FAILED 删除失败 - RECOVERING 恢复中  **约束限制** 不涉及 **取值范围**: - COMPLETED - CREATING - UPDATING - ENABLING - DISABLING - DELETING - CREATE_FAILED - UPDATE_FAILED - ENABLE_FAILED - DISABLE_FAILED - DELETE_FAILED - RECOVERING  **默认值** 不涉及         

        :param process_status: The process_status of this ShowAlertRuleTemplateResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def query_type(self):
        r"""Gets the query_type of this ShowAlertRuleTemplateResponse.

        **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        

        :return: The query_type of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ShowAlertRuleTemplateResponse.

        **参数解释**: 查询类型 - SQL SQL查询 - CBSL CBSL查询  **约束限制** 不涉及 **取值范围**: - SQL - CBSL  **默认值** 不涉及        

        :param query_type: The query_type of this ShowAlertRuleTemplateResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def script(self):
        r"""Gets the script of this ShowAlertRuleTemplateResponse.

        Script 脚本

        :return: The script of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this ShowAlertRuleTemplateResponse.

        Script 脚本

        :param script: The script of this ShowAlertRuleTemplateResponse.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this ShowAlertRuleTemplateResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAlertRuleTemplateResponse.

        **参数解释**: 状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this ShowAlertRuleTemplateResponse.
        :type status: str
        """
        self._status = status

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowAlertRuleTemplateResponse.

        表名称

        :return: The table_name of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowAlertRuleTemplateResponse.

        表名称

        :param table_name: The table_name of this ShowAlertRuleTemplateResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowAlertRuleTemplateResponse.

        UUID

        :return: The template_id of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowAlertRuleTemplateResponse.

        UUID

        :param template_id: The template_id of this ShowAlertRuleTemplateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowAlertRuleTemplateResponse.

        模板名称

        :return: The template_name of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowAlertRuleTemplateResponse.

        模板名称

        :param template_name: The template_name of this ShowAlertRuleTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def triggers(self):
        r"""Gets the triggers of this ShowAlertRuleTemplateResponse.

        触发器数组

        :return: The triggers of this ShowAlertRuleTemplateResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this ShowAlertRuleTemplateResponse.

        触发器数组

        :param triggers: The triggers of this ShowAlertRuleTemplateResponse.
        :type triggers: list[:class:`huaweicloudsdksecmaster.v2.Trigger`]
        """
        self._triggers = triggers

    @property
    def update_by(self):
        r"""Gets the update_by of this ShowAlertRuleTemplateResponse.

        UUID

        :return: The update_by of this ShowAlertRuleTemplateResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this ShowAlertRuleTemplateResponse.

        UUID

        :param update_by: The update_by of this ShowAlertRuleTemplateResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAlertRuleTemplateResponse.

        毫秒时间戳

        :return: The update_time of this ShowAlertRuleTemplateResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAlertRuleTemplateResponse.

        毫秒时间戳

        :param update_time: The update_time of this ShowAlertRuleTemplateResponse.
        :type update_time: int
        """
        self._update_time = update_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowAlertRuleTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAlertRuleTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
