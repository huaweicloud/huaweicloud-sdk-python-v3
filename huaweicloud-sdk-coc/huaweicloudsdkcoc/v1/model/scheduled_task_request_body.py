# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_infos': 'list[TicketInfo]',
        'name': 'str',
        'enterprise_project_id': 'str',
        'agency_name': 'str',
        'version_no': 'str',
        'trigger_time': 'TriggerTime',
        'task_type': 'str',
        'associated_task_id': 'str',
        'associated_task_type': 'str',
        'associated_task_name': 'str',
        'associated_task_name_en': 'str',
        'associated_task_enterprise_project_id': 'str',
        'runbook_instance_mode': 'str',
        'risk_level': 'str',
        'input_param': 'dict(str, str)',
        'target_instances': 'list[ScheduleInstance]',
        'enable_approve': 'bool',
        'reviewer_notification': 'MessageNotification',
        'reviewer_user_name': 'str',
        'enable_message_notification': 'bool',
        'message_notification': 'MessageNotification'
    }

    attribute_map = {
        'ticket_infos': 'ticket_infos',
        'name': 'name',
        'enterprise_project_id': 'enterprise_project_id',
        'agency_name': 'agency_name',
        'version_no': 'version_no',
        'trigger_time': 'trigger_time',
        'task_type': 'task_type',
        'associated_task_id': 'associated_task_id',
        'associated_task_type': 'associated_task_type',
        'associated_task_name': 'associated_task_name',
        'associated_task_name_en': 'associated_task_name_en',
        'associated_task_enterprise_project_id': 'associated_task_enterprise_project_id',
        'runbook_instance_mode': 'runbook_instance_mode',
        'risk_level': 'risk_level',
        'input_param': 'input_param',
        'target_instances': 'target_instances',
        'enable_approve': 'enable_approve',
        'reviewer_notification': 'reviewer_notification',
        'reviewer_user_name': 'reviewer_user_name',
        'enable_message_notification': 'enable_message_notification',
        'message_notification': 'message_notification'
    }

    def __init__(self, ticket_infos=None, name=None, enterprise_project_id=None, agency_name=None, version_no=None, trigger_time=None, task_type=None, associated_task_id=None, associated_task_type=None, associated_task_name=None, associated_task_name_en=None, associated_task_enterprise_project_id=None, runbook_instance_mode=None, risk_level=None, input_param=None, target_instances=None, enable_approve=None, reviewer_notification=None, reviewer_user_name=None, enable_message_notification=None, message_notification=None):
        r"""ScheduledTaskRequestBody

        The model defined in huaweicloud sdk

        :param ticket_infos: 选择的四号提权单信息
        :type ticket_infos: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        :param name: 任务名称
        :type name: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param version_no: 版本号
        :type version_no: str
        :param trigger_time: 
        :type trigger_time: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        :param task_type: 任务类型
        :type task_type: str
        :param associated_task_id: 关联任务ID（脚本ID/作业ID）
        :type associated_task_id: str
        :param associated_task_type: 关联任务的类型
        :type associated_task_type: str
        :param associated_task_name: 关联任务名称（脚本名称/作业名称）
        :type associated_task_name: str
        :param associated_task_name_en: 关联任务名称(英文)（脚本名称/作业名称）
        :type associated_task_name_en: str
        :param associated_task_enterprise_project_id: 关联任务的企业项目ID
        :type associated_task_enterprise_project_id: str
        :param runbook_instance_mode: 作业实例模式
        :type runbook_instance_mode: str
        :param risk_level: 风险等级
        :type risk_level: str
        :param input_param: 执行参数，值为json串
        :type input_param: dict(str, str)
        :param target_instances: 目标实例信息
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        :param enable_approve: 是否开启入库人工审核
        :type enable_approve: bool
        :param reviewer_notification: 
        :type reviewer_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        :param reviewer_user_name: 审核人昵称
        :type reviewer_user_name: str
        :param enable_message_notification: 是否启用消息通知
        :type enable_message_notification: bool
        :param message_notification: 
        :type message_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        
        

        self._ticket_infos = None
        self._name = None
        self._enterprise_project_id = None
        self._agency_name = None
        self._version_no = None
        self._trigger_time = None
        self._task_type = None
        self._associated_task_id = None
        self._associated_task_type = None
        self._associated_task_name = None
        self._associated_task_name_en = None
        self._associated_task_enterprise_project_id = None
        self._runbook_instance_mode = None
        self._risk_level = None
        self._input_param = None
        self._target_instances = None
        self._enable_approve = None
        self._reviewer_notification = None
        self._reviewer_user_name = None
        self._enable_message_notification = None
        self._message_notification = None
        self.discriminator = None

        if ticket_infos is not None:
            self.ticket_infos = ticket_infos
        self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if agency_name is not None:
            self.agency_name = agency_name
        self.version_no = version_no
        self.trigger_time = trigger_time
        self.task_type = task_type
        self.associated_task_id = associated_task_id
        self.associated_task_type = associated_task_type
        self.associated_task_name = associated_task_name
        if associated_task_name_en is not None:
            self.associated_task_name_en = associated_task_name_en
        if associated_task_enterprise_project_id is not None:
            self.associated_task_enterprise_project_id = associated_task_enterprise_project_id
        if runbook_instance_mode is not None:
            self.runbook_instance_mode = runbook_instance_mode
        self.risk_level = risk_level
        self.input_param = input_param
        self.target_instances = target_instances
        self.enable_approve = enable_approve
        if reviewer_notification is not None:
            self.reviewer_notification = reviewer_notification
        if reviewer_user_name is not None:
            self.reviewer_user_name = reviewer_user_name
        self.enable_message_notification = enable_message_notification
        if message_notification is not None:
            self.message_notification = message_notification

    @property
    def ticket_infos(self):
        r"""Gets the ticket_infos of this ScheduledTaskRequestBody.

        选择的四号提权单信息

        :return: The ticket_infos of this ScheduledTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        """
        return self._ticket_infos

    @ticket_infos.setter
    def ticket_infos(self, ticket_infos):
        r"""Sets the ticket_infos of this ScheduledTaskRequestBody.

        选择的四号提权单信息

        :param ticket_infos: The ticket_infos of this ScheduledTaskRequestBody.
        :type ticket_infos: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        """
        self._ticket_infos = ticket_infos

    @property
    def name(self):
        r"""Gets the name of this ScheduledTaskRequestBody.

        任务名称

        :return: The name of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduledTaskRequestBody.

        任务名称

        :param name: The name of this ScheduledTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ScheduledTaskRequestBody.

        企业项目id

        :return: The enterprise_project_id of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ScheduledTaskRequestBody.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ScheduledTaskRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ScheduledTaskRequestBody.

        委托名称

        :return: The agency_name of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ScheduledTaskRequestBody.

        委托名称

        :param agency_name: The agency_name of this ScheduledTaskRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def version_no(self):
        r"""Gets the version_no of this ScheduledTaskRequestBody.

        版本号

        :return: The version_no of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._version_no

    @version_no.setter
    def version_no(self, version_no):
        r"""Sets the version_no of this ScheduledTaskRequestBody.

        版本号

        :param version_no: The version_no of this ScheduledTaskRequestBody.
        :type version_no: str
        """
        self._version_no = version_no

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this ScheduledTaskRequestBody.

        :return: The trigger_time of this ScheduledTaskRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this ScheduledTaskRequestBody.

        :param trigger_time: The trigger_time of this ScheduledTaskRequestBody.
        :type trigger_time: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        """
        self._trigger_time = trigger_time

    @property
    def task_type(self):
        r"""Gets the task_type of this ScheduledTaskRequestBody.

        任务类型

        :return: The task_type of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ScheduledTaskRequestBody.

        任务类型

        :param task_type: The task_type of this ScheduledTaskRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def associated_task_id(self):
        r"""Gets the associated_task_id of this ScheduledTaskRequestBody.

        关联任务ID（脚本ID/作业ID）

        :return: The associated_task_id of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._associated_task_id

    @associated_task_id.setter
    def associated_task_id(self, associated_task_id):
        r"""Sets the associated_task_id of this ScheduledTaskRequestBody.

        关联任务ID（脚本ID/作业ID）

        :param associated_task_id: The associated_task_id of this ScheduledTaskRequestBody.
        :type associated_task_id: str
        """
        self._associated_task_id = associated_task_id

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this ScheduledTaskRequestBody.

        关联任务的类型

        :return: The associated_task_type of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this ScheduledTaskRequestBody.

        关联任务的类型

        :param associated_task_type: The associated_task_type of this ScheduledTaskRequestBody.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this ScheduledTaskRequestBody.

        关联任务名称（脚本名称/作业名称）

        :return: The associated_task_name of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this ScheduledTaskRequestBody.

        关联任务名称（脚本名称/作业名称）

        :param associated_task_name: The associated_task_name of this ScheduledTaskRequestBody.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def associated_task_name_en(self):
        r"""Gets the associated_task_name_en of this ScheduledTaskRequestBody.

        关联任务名称(英文)（脚本名称/作业名称）

        :return: The associated_task_name_en of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._associated_task_name_en

    @associated_task_name_en.setter
    def associated_task_name_en(self, associated_task_name_en):
        r"""Sets the associated_task_name_en of this ScheduledTaskRequestBody.

        关联任务名称(英文)（脚本名称/作业名称）

        :param associated_task_name_en: The associated_task_name_en of this ScheduledTaskRequestBody.
        :type associated_task_name_en: str
        """
        self._associated_task_name_en = associated_task_name_en

    @property
    def associated_task_enterprise_project_id(self):
        r"""Gets the associated_task_enterprise_project_id of this ScheduledTaskRequestBody.

        关联任务的企业项目ID

        :return: The associated_task_enterprise_project_id of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._associated_task_enterprise_project_id

    @associated_task_enterprise_project_id.setter
    def associated_task_enterprise_project_id(self, associated_task_enterprise_project_id):
        r"""Sets the associated_task_enterprise_project_id of this ScheduledTaskRequestBody.

        关联任务的企业项目ID

        :param associated_task_enterprise_project_id: The associated_task_enterprise_project_id of this ScheduledTaskRequestBody.
        :type associated_task_enterprise_project_id: str
        """
        self._associated_task_enterprise_project_id = associated_task_enterprise_project_id

    @property
    def runbook_instance_mode(self):
        r"""Gets the runbook_instance_mode of this ScheduledTaskRequestBody.

        作业实例模式

        :return: The runbook_instance_mode of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._runbook_instance_mode

    @runbook_instance_mode.setter
    def runbook_instance_mode(self, runbook_instance_mode):
        r"""Sets the runbook_instance_mode of this ScheduledTaskRequestBody.

        作业实例模式

        :param runbook_instance_mode: The runbook_instance_mode of this ScheduledTaskRequestBody.
        :type runbook_instance_mode: str
        """
        self._runbook_instance_mode = runbook_instance_mode

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ScheduledTaskRequestBody.

        风险等级

        :return: The risk_level of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ScheduledTaskRequestBody.

        风险等级

        :param risk_level: The risk_level of this ScheduledTaskRequestBody.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def input_param(self):
        r"""Gets the input_param of this ScheduledTaskRequestBody.

        执行参数，值为json串

        :return: The input_param of this ScheduledTaskRequestBody.
        :rtype: dict(str, str)
        """
        return self._input_param

    @input_param.setter
    def input_param(self, input_param):
        r"""Sets the input_param of this ScheduledTaskRequestBody.

        执行参数，值为json串

        :param input_param: The input_param of this ScheduledTaskRequestBody.
        :type input_param: dict(str, str)
        """
        self._input_param = input_param

    @property
    def target_instances(self):
        r"""Gets the target_instances of this ScheduledTaskRequestBody.

        目标实例信息

        :return: The target_instances of this ScheduledTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        r"""Sets the target_instances of this ScheduledTaskRequestBody.

        目标实例信息

        :param target_instances: The target_instances of this ScheduledTaskRequestBody.
        :type target_instances: list[:class:`huaweicloudsdkcoc.v1.ScheduleInstance`]
        """
        self._target_instances = target_instances

    @property
    def enable_approve(self):
        r"""Gets the enable_approve of this ScheduledTaskRequestBody.

        是否开启入库人工审核

        :return: The enable_approve of this ScheduledTaskRequestBody.
        :rtype: bool
        """
        return self._enable_approve

    @enable_approve.setter
    def enable_approve(self, enable_approve):
        r"""Sets the enable_approve of this ScheduledTaskRequestBody.

        是否开启入库人工审核

        :param enable_approve: The enable_approve of this ScheduledTaskRequestBody.
        :type enable_approve: bool
        """
        self._enable_approve = enable_approve

    @property
    def reviewer_notification(self):
        r"""Gets the reviewer_notification of this ScheduledTaskRequestBody.

        :return: The reviewer_notification of this ScheduledTaskRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        return self._reviewer_notification

    @reviewer_notification.setter
    def reviewer_notification(self, reviewer_notification):
        r"""Sets the reviewer_notification of this ScheduledTaskRequestBody.

        :param reviewer_notification: The reviewer_notification of this ScheduledTaskRequestBody.
        :type reviewer_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        self._reviewer_notification = reviewer_notification

    @property
    def reviewer_user_name(self):
        r"""Gets the reviewer_user_name of this ScheduledTaskRequestBody.

        审核人昵称

        :return: The reviewer_user_name of this ScheduledTaskRequestBody.
        :rtype: str
        """
        return self._reviewer_user_name

    @reviewer_user_name.setter
    def reviewer_user_name(self, reviewer_user_name):
        r"""Sets the reviewer_user_name of this ScheduledTaskRequestBody.

        审核人昵称

        :param reviewer_user_name: The reviewer_user_name of this ScheduledTaskRequestBody.
        :type reviewer_user_name: str
        """
        self._reviewer_user_name = reviewer_user_name

    @property
    def enable_message_notification(self):
        r"""Gets the enable_message_notification of this ScheduledTaskRequestBody.

        是否启用消息通知

        :return: The enable_message_notification of this ScheduledTaskRequestBody.
        :rtype: bool
        """
        return self._enable_message_notification

    @enable_message_notification.setter
    def enable_message_notification(self, enable_message_notification):
        r"""Sets the enable_message_notification of this ScheduledTaskRequestBody.

        是否启用消息通知

        :param enable_message_notification: The enable_message_notification of this ScheduledTaskRequestBody.
        :type enable_message_notification: bool
        """
        self._enable_message_notification = enable_message_notification

    @property
    def message_notification(self):
        r"""Gets the message_notification of this ScheduledTaskRequestBody.

        :return: The message_notification of this ScheduledTaskRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        return self._message_notification

    @message_notification.setter
    def message_notification(self, message_notification):
        r"""Sets the message_notification of this ScheduledTaskRequestBody.

        :param message_notification: The message_notification of this ScheduledTaskRequestBody.
        :type message_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        self._message_notification = message_notification

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
        if not isinstance(other, ScheduledTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
