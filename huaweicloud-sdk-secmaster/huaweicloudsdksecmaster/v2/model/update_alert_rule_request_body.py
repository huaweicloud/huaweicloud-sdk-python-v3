# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertRuleRequestBody:

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
        'job_mode_setting': 'IsapJobModeSettingDto',
        'job_output_setting': 'IsapJobOutputSetting',
        'environment': 'str',
        'output_table_id': 'str',
        'output_table_ids': 'list[str]',
        'output_table_names': 'list[str]',
        'publish_status': 'str'
    }

    attribute_map = {
        'alert_rule_name': 'alert_rule_name',
        'description': 'description',
        'directory': 'directory',
        'script': 'script',
        'status': 'status',
        'job_mode_setting': 'job_mode_setting',
        'job_output_setting': 'job_output_setting',
        'environment': 'environment',
        'output_table_id': 'output_table_id',
        'output_table_ids': 'output_table_ids',
        'output_table_names': 'output_table_names',
        'publish_status': 'publish_status'
    }

    def __init__(self, alert_rule_name=None, description=None, directory=None, script=None, status=None, job_mode_setting=None, job_output_setting=None, environment=None, output_table_id=None, output_table_ids=None, output_table_names=None, publish_status=None):
        r"""UpdateAlertRuleRequestBody

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
        :param job_mode_setting: 
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        :param job_output_setting: 
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        :param environment: **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     
        :type environment: str
        :param output_table_id: UUID
        :type output_table_id: str
        :param output_table_ids: 输出表ID列表
        :type output_table_ids: list[str]
        :param output_table_names: 输出表名称列表
        :type output_table_names: list[str]
        :param publish_status: 发布状态: 只适用行管租户，不对外暴露参数
        :type publish_status: str
        """
        
        

        self._alert_rule_name = None
        self._description = None
        self._directory = None
        self._script = None
        self._status = None
        self._job_mode_setting = None
        self._job_output_setting = None
        self._environment = None
        self._output_table_id = None
        self._output_table_ids = None
        self._output_table_names = None
        self._publish_status = None
        self.discriminator = None

        if alert_rule_name is not None:
            self.alert_rule_name = alert_rule_name
        if description is not None:
            self.description = description
        if directory is not None:
            self.directory = directory
        if script is not None:
            self.script = script
        if status is not None:
            self.status = status
        if job_mode_setting is not None:
            self.job_mode_setting = job_mode_setting
        if job_output_setting is not None:
            self.job_output_setting = job_output_setting
        if environment is not None:
            self.environment = environment
        if output_table_id is not None:
            self.output_table_id = output_table_id
        if output_table_ids is not None:
            self.output_table_ids = output_table_ids
        if output_table_names is not None:
            self.output_table_names = output_table_names
        if publish_status is not None:
            self.publish_status = publish_status

    @property
    def alert_rule_name(self):
        r"""Gets the alert_rule_name of this UpdateAlertRuleRequestBody.

        Alert rule name 告警规则名称

        :return: The alert_rule_name of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._alert_rule_name

    @alert_rule_name.setter
    def alert_rule_name(self, alert_rule_name):
        r"""Sets the alert_rule_name of this UpdateAlertRuleRequestBody.

        Alert rule name 告警规则名称

        :param alert_rule_name: The alert_rule_name of this UpdateAlertRuleRequestBody.
        :type alert_rule_name: str
        """
        self._alert_rule_name = alert_rule_name

    @property
    def description(self):
        r"""Gets the description of this UpdateAlertRuleRequestBody.

        Alert rule description 告警规则描述

        :return: The description of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAlertRuleRequestBody.

        Alert rule description 告警规则描述

        :param description: The description of this UpdateAlertRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def directory(self):
        r"""Gets the directory of this UpdateAlertRuleRequestBody.

        directory 目录分组

        :return: The directory of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this UpdateAlertRuleRequestBody.

        directory 目录分组

        :param directory: The directory of this UpdateAlertRuleRequestBody.
        :type directory: str
        """
        self._directory = directory

    @property
    def script(self):
        r"""Gets the script of this UpdateAlertRuleRequestBody.

        Job Script 作业脚本

        :return: The script of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        r"""Sets the script of this UpdateAlertRuleRequestBody.

        Job Script 作业脚本

        :param script: The script of this UpdateAlertRuleRequestBody.
        :type script: str
        """
        self._script = script

    @property
    def status(self):
        r"""Gets the status of this UpdateAlertRuleRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :return: The status of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAlertRuleRequestBody.

        **参数解释**: 作业状态 - ENABLED 启用 - DISABLED 禁用  **约束限制** 不涉及 **取值范围**: - ENABLED - DISABLED  **默认值** 不涉及    

        :param status: The status of this UpdateAlertRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def job_mode_setting(self):
        r"""Gets the job_mode_setting of this UpdateAlertRuleRequestBody.

        :return: The job_mode_setting of this UpdateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        return self._job_mode_setting

    @job_mode_setting.setter
    def job_mode_setting(self, job_mode_setting):
        r"""Sets the job_mode_setting of this UpdateAlertRuleRequestBody.

        :param job_mode_setting: The job_mode_setting of this UpdateAlertRuleRequestBody.
        :type job_mode_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobModeSettingDto`
        """
        self._job_mode_setting = job_mode_setting

    @property
    def job_output_setting(self):
        r"""Gets the job_output_setting of this UpdateAlertRuleRequestBody.

        :return: The job_output_setting of this UpdateAlertRuleRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        return self._job_output_setting

    @job_output_setting.setter
    def job_output_setting(self, job_output_setting):
        r"""Sets the job_output_setting of this UpdateAlertRuleRequestBody.

        :param job_output_setting: The job_output_setting of this UpdateAlertRuleRequestBody.
        :type job_output_setting: :class:`huaweicloudsdksecmaster.v2.IsapJobOutputSetting`
        """
        self._job_output_setting = job_output_setting

    @property
    def environment(self):
        r"""Gets the environment of this UpdateAlertRuleRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :return: The environment of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this UpdateAlertRuleRequestBody.

        **参数解释**: 环境类型 - PROD 生产环境 - TEST 测试环境  **约束限制** 不涉及 **取值范围**: - PROD - TEST  **默认值** 不涉及     

        :param environment: The environment of this UpdateAlertRuleRequestBody.
        :type environment: str
        """
        self._environment = environment

    @property
    def output_table_id(self):
        r"""Gets the output_table_id of this UpdateAlertRuleRequestBody.

        UUID

        :return: The output_table_id of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._output_table_id

    @output_table_id.setter
    def output_table_id(self, output_table_id):
        r"""Sets the output_table_id of this UpdateAlertRuleRequestBody.

        UUID

        :param output_table_id: The output_table_id of this UpdateAlertRuleRequestBody.
        :type output_table_id: str
        """
        self._output_table_id = output_table_id

    @property
    def output_table_ids(self):
        r"""Gets the output_table_ids of this UpdateAlertRuleRequestBody.

        输出表ID列表

        :return: The output_table_ids of this UpdateAlertRuleRequestBody.
        :rtype: list[str]
        """
        return self._output_table_ids

    @output_table_ids.setter
    def output_table_ids(self, output_table_ids):
        r"""Sets the output_table_ids of this UpdateAlertRuleRequestBody.

        输出表ID列表

        :param output_table_ids: The output_table_ids of this UpdateAlertRuleRequestBody.
        :type output_table_ids: list[str]
        """
        self._output_table_ids = output_table_ids

    @property
    def output_table_names(self):
        r"""Gets the output_table_names of this UpdateAlertRuleRequestBody.

        输出表名称列表

        :return: The output_table_names of this UpdateAlertRuleRequestBody.
        :rtype: list[str]
        """
        return self._output_table_names

    @output_table_names.setter
    def output_table_names(self, output_table_names):
        r"""Sets the output_table_names of this UpdateAlertRuleRequestBody.

        输出表名称列表

        :param output_table_names: The output_table_names of this UpdateAlertRuleRequestBody.
        :type output_table_names: list[str]
        """
        self._output_table_names = output_table_names

    @property
    def publish_status(self):
        r"""Gets the publish_status of this UpdateAlertRuleRequestBody.

        发布状态: 只适用行管租户，不对外暴露参数

        :return: The publish_status of this UpdateAlertRuleRequestBody.
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        r"""Sets the publish_status of this UpdateAlertRuleRequestBody.

        发布状态: 只适用行管租户，不对外暴露参数

        :param publish_status: The publish_status of this UpdateAlertRuleRequestBody.
        :type publish_status: str
        """
        self._publish_status = publish_status

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
        if not isinstance(other, UpdateAlertRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
