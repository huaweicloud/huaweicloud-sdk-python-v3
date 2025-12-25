# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_rule_name': 'str',
        'description': 'str',
        'directory': 'str',
        'script': 'str',
        'status': 'str',
        'job_mode': 'str',
        'job_mode_setting': 'IsapJobModeSettingDto',
        'environment': 'str',
        'job_output_setting': 'IsapJobOutputSetting',
        'output_table_id': 'str',
        'output_table_name': 'str',
        'cu_quota_amount': 'float',
        'output_table_ids': 'list[str]',
        'output_table_names': 'list[str]'
    }

    attribute_map = {
        'alert_rule_name': 'alert_rule_name',
        'description': 'description',
        'directory': 'directory',
        'script': 'script',
        'status': 'status',
        'job_mode': 'job_mode',
        'job_mode_setting': 'job_mode_setting',
        'environment': 'environment',
        'job_output_setting': 'job_output_setting',
        'output_table_id': 'output_table_id',
        'output_table_name': 'output_table_name',
        'cu_quota_amount': 'cu_quota_amount',
        'output_table_ids': 'output_table_ids',
        'output_table_names': 'output_table_names'
    }

    def __init__(self, alert_rule_name=None, description=None, directory=None, script=None, status=None, job_mode=None, job_mode_setting=None, environment=None, job_output_setting=None, output_table_id=None, output_table_name=None, cu_quota_amount=None, output_table_ids=None, output_table_names=None):
        r"""CreateAlertRuleRequestBody

        The model defined in huaweicloud sdk

        :param alert_rule_name: Alert rule name 告警规则名称
        :type alert_rule_name: str
        :param description: Alert rule description 告警规则描述
        :type description: str
        :param directory: directory 目录分组
        :type directory: str
        :param script: Job Script 作业脚本
        :type script: str
        :param status: **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    
        :type status: str
        :param job_mode: **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  
        :type job_mode: str
        :param job_mode_setting: 
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        :param environment: **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     
        :type environment: str
        :param job_output_setting: 
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        :param output_table_id: UUID
        :type output_table_id: str
        :param output_table_name: 表名
        :type output_table_name: str
        :param cu_quota_amount: 数量
        :type cu_quota_amount: float
        :param output_table_ids: 输出表id列表
        :type output_table_ids: list[str]
        :param output_table_names: 输出表名称列表
        :type output_table_names: list[str]
        """
        
        

        self._alert_rule_name = None
        self._description = None
        self._directory = None
        self._script = None
        self._status = None
        self._job_mode = None
        self._job_mode_setting = None
        self._environment = None
        self._job_output_setting = None
        self._output_table_id = None
        self._output_table_name = None
        self._cu_quota_amount = None
        self._output_table_ids = None
        self._output_table_names = None
        self.discriminator = None

        self.alert_rule_name = alert_rule_name
        self.description = description
        if directory is not None:
            self.directory = directory
        if script is not None:
            self.script = script
        self.status = status
        self.job_mode = job_mode
        if job_mode_setting is not None:
            self.job_mode_setting = job_mode_setting
        self.environment = environment
        if job_output_setting is not None:
            self.job_output_setting = job_output_setting
        self.output_table_id = output_table_id
        if output_table_name is not None:
            self.output_table_name = output_table_name
        self.cu_quota_amount = cu_quota_amount
        self.output_table_ids = output_table_ids
        self.output_table_names = output_table_names

    @property
    def alert_rule_name(self):
        r"""Gets the alert_rule_name of this CreateAlertRuleRequestBody.

        Alert rule name 告警规则名称

        :return: The alert_rule_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._alert_rule_name

    @alert_rule_name.setter
    def alert_rule_name(self, alert_rule_name):
        r"""Sets the alert_rule_name of this CreateAlertRuleRequestBody.

        Alert rule name 告警规则名称

        :param alert_rule_name: The alert_rule_name of this CreateAlertRuleRequestBody.
        :type alert_rule_name: str
        """
        self._alert_rule_name = alert_rule_name

    @property
    def description(self):
        r"""Gets the description of this CreateAlertRuleRequestBody.

        Alert rule description 告警规则描述

        :return: The description of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertRuleRequestBody.

        Alert rule description 告警规则描述

        :param description: The description of this CreateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this CreateAlertRuleRequestBody.

        directory 目录分组

        :return: The directory of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this CreateAlertRuleRequestBody.

        directory 目录分组

        :param directory: The directory of this CreateAlertRuleRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def script(self):
        r"""Gets the script of this CreateAlertRuleRequestBody.

        Job Script 作业脚本

        :return: The script of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this CreateAlertRuleRequestBody.

        Job Script 作业脚本

        :param script: The script of this CreateAlertRuleRequestBody.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this CreateAlertRuleRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAlertRuleRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this CreateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def job_mode(self):
        r"""Gets the job_mode of this CreateAlertRuleRequestBody.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :return: The job_mode of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this CreateAlertRuleRequestBody.

        **参数解释**: 作业模式 - STREAMING 流式处理 - BATCH 批处理 - SEARCH 检索  **约束限制** 不涉及 **取值范围**: - STREAMING - BATCH - SEARCH  **默认值** 不涉及  

        :param job_mode: The job_mode of this CreateAlertRuleRequestBody.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_mode_setting(self):
        r"""Gets the job_mode_setting of this CreateAlertRuleRequestBody.

        :return: The job_mode_setting of this CreateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        return self._job_mode_setting

    @job_mode_setting.setter
    def job_mode_setting(self, job_mode_setting):
        r"""Sets the job_mode_setting of this CreateAlertRuleRequestBody.

        :param job_mode_setting: The job_mode_setting of this CreateAlertRuleRequestBody.
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        self._job_mode_setting = job_mode_setting

    @property
    def environment(self):
        r"""Gets the environment of this CreateAlertRuleRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :return: The environment of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this CreateAlertRuleRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :param environment: The environment of this CreateAlertRuleRequestBody.
        :type environment: str
        """
        self._environment = environment

    @property
    def job_output_setting(self):
        r"""Gets the job_output_setting of this CreateAlertRuleRequestBody.

        :return: The job_output_setting of this CreateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        return self._job_output_setting

    @job_output_setting.setter
    def job_output_setting(self, job_output_setting):
        r"""Sets the job_output_setting of this CreateAlertRuleRequestBody.

        :param job_output_setting: The job_output_setting of this CreateAlertRuleRequestBody.
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        self._job_output_setting = job_output_setting

    @property
    def output_table_id(self):
        r"""Gets the output_table_id of this CreateAlertRuleRequestBody.

        UUID

        :return: The output_table_id of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._output_table_id

    @output_table_id.setter
    def output_table_id(self, output_table_id):
        r"""Sets the output_table_id of this CreateAlertRuleRequestBody.

        UUID

        :param output_table_id: The output_table_id of this CreateAlertRuleRequestBody.
        :type output_table_id: str
        """
        self._output_table_id = output_table_id

    @property
    def output_table_name(self):
        r"""Gets the output_table_name of this CreateAlertRuleRequestBody.

        表名

        :return: The output_table_name of this CreateAlertRuleRequestBody.
        :rtype: str
        """
        return self._output_table_name

    @output_table_name.setter
    def output_table_name(self, output_table_name):
        r"""Sets the output_table_name of this CreateAlertRuleRequestBody.

        表名

        :param output_table_name: The output_table_name of this CreateAlertRuleRequestBody.
        :type output_table_name: str
        """
        self._output_table_name = output_table_name

    @property
    def cu_quota_amount(self):
        r"""Gets the cu_quota_amount of this CreateAlertRuleRequestBody.

        数量

        :return: The cu_quota_amount of this CreateAlertRuleRequestBody.
        :rtype: float
        """
        return self._cu_quota_amount

    @cu_quota_amount.setter
    def cu_quota_amount(self, cu_quota_amount):
        r"""Sets the cu_quota_amount of this CreateAlertRuleRequestBody.

        数量

        :param cu_quota_amount: The cu_quota_amount of this CreateAlertRuleRequestBody.
        :type cu_quota_amount: float
        """
        self._cu_quota_amount = cu_quota_amount

    @property
    def output_table_ids(self):
        r"""Gets the output_table_ids of this CreateAlertRuleRequestBody.

        输出表id列表

        :return: The output_table_ids of this CreateAlertRuleRequestBody.
        :rtype: list[str]
        """
        return self._output_table_ids

    @output_table_ids.setter
    def output_table_ids(self, output_table_ids):
        r"""Sets the output_table_ids of this CreateAlertRuleRequestBody.

        输出表id列表

        :param output_table_ids: The output_table_ids of this CreateAlertRuleRequestBody.
        :type output_table_ids: list[str]
        """
        self._output_table_ids = output_table_ids

    @property
    def output_table_names(self):
        r"""Gets the output_table_names of this CreateAlertRuleRequestBody.

        输出表名称列表

        :return: The output_table_names of this CreateAlertRuleRequestBody.
        :rtype: list[str]
        """
        return self._output_table_names

    @output_table_names.setter
    def output_table_names(self, output_table_names):
        r"""Sets the output_table_names of this CreateAlertRuleRequestBody.

        输出表名称列表

        :param output_table_names: The output_table_names of this CreateAlertRuleRequestBody.
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
        if not isinstance(other, CreateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
