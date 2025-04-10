# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScheduledTaskResponse(SdkResponse):

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
        'enterprise_project_id': 'str',
        'name': 'str',
        'agency_name': 'str',
        'trigger_time': 'TriggerTime',
        'version_no': 'str',
        'task_type': 'object',
        'associated_task_id': 'str',
        'associated_task_name': 'str',
        'associated_task_name_en': 'str',
        'associated_task_type': 'str',
        'runbook_instance_mode': 'str',
        'risk_level': 'str',
        'input_param': 'str',
        'enable_approve': 'bool',
        'reviewer_notification': 'MessageNotification',
        'created_user_name': 'str',
        'reviewer_user_name': 'str',
        'approve_status': 'object',
        'approve_comments': 'str',
        'target_instances': 'str',
        'enable_message_notification': 'bool',
        'message_notification': 'MessageNotification'
    }

    attribute_map = {
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'agency_name': 'agency_name',
        'trigger_time': 'trigger_time',
        'version_no': 'version_no',
        'task_type': 'task_type',
        'associated_task_id': 'associated_task_id',
        'associated_task_name': 'associated_task_name',
        'associated_task_name_en': 'associated_task_name_en',
        'associated_task_type': 'associated_task_type',
        'runbook_instance_mode': 'runbook_instance_mode',
        'risk_level': 'risk_level',
        'input_param': 'input_param',
        'enable_approve': 'enable_approve',
        'reviewer_notification': 'reviewer_notification',
        'created_user_name': 'created_user_name',
        'reviewer_user_name': 'reviewer_user_name',
        'approve_status': 'approve_status',
        'approve_comments': 'approve_comments',
        'target_instances': 'target_instances',
        'enable_message_notification': 'enable_message_notification',
        'message_notification': 'message_notification'
    }

    def __init__(self, id=None, enterprise_project_id=None, name=None, agency_name=None, trigger_time=None, version_no=None, task_type=None, associated_task_id=None, associated_task_name=None, associated_task_name_en=None, associated_task_type=None, runbook_instance_mode=None, risk_level=None, input_param=None, enable_approve=None, reviewer_notification=None, created_user_name=None, reviewer_user_name=None, approve_status=None, approve_comments=None, target_instances=None, enable_message_notification=None, message_notification=None):
        r"""ShowScheduledTaskResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param name: 任务名称
        :type name: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param trigger_time: 
        :type trigger_time: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        :param version_no: 版本号
        :type version_no: str
        :param task_type: 任务类型
        :type task_type: object
        :param associated_task_id: 关联任务ID（脚本ID/作业ID）
        :type associated_task_id: str
        :param associated_task_name: 关联任务名称（脚本名称/作业名称）
        :type associated_task_name: str
        :param associated_task_name_en: 关联任务名称(英文)（脚本名称/作业名称）
        :type associated_task_name_en: str
        :param associated_task_type: 关联任务的类型
        :type associated_task_type: str
        :param runbook_instance_mode: 作业实例模式
        :type runbook_instance_mode: str
        :param risk_level: 风险等级
        :type risk_level: str
        :param input_param: 执行参数，值为json串
        :type input_param: str
        :param enable_approve: 是否开启入库人工审核
        :type enable_approve: bool
        :param reviewer_notification: 
        :type reviewer_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        :param created_user_name: 创建人昵称
        :type created_user_name: str
        :param reviewer_user_name: 审核人昵称
        :type reviewer_user_name: str
        :param approve_status: 审批状态
        :type approve_status: object
        :param approve_comments: 审批意见
        :type approve_comments: str
        :param target_instances: 目标节点json串
        :type target_instances: str
        :param enable_message_notification: 是否启用消息通知
        :type enable_message_notification: bool
        :param message_notification: 
        :type message_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        
        super(ShowScheduledTaskResponse, self).__init__()

        self._id = None
        self._enterprise_project_id = None
        self._name = None
        self._agency_name = None
        self._trigger_time = None
        self._version_no = None
        self._task_type = None
        self._associated_task_id = None
        self._associated_task_name = None
        self._associated_task_name_en = None
        self._associated_task_type = None
        self._runbook_instance_mode = None
        self._risk_level = None
        self._input_param = None
        self._enable_approve = None
        self._reviewer_notification = None
        self._created_user_name = None
        self._reviewer_user_name = None
        self._approve_status = None
        self._approve_comments = None
        self._target_instances = None
        self._enable_message_notification = None
        self._message_notification = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if agency_name is not None:
            self.agency_name = agency_name
        if trigger_time is not None:
            self.trigger_time = trigger_time
        if version_no is not None:
            self.version_no = version_no
        if task_type is not None:
            self.task_type = task_type
        if associated_task_id is not None:
            self.associated_task_id = associated_task_id
        if associated_task_name is not None:
            self.associated_task_name = associated_task_name
        if associated_task_name_en is not None:
            self.associated_task_name_en = associated_task_name_en
        if associated_task_type is not None:
            self.associated_task_type = associated_task_type
        if runbook_instance_mode is not None:
            self.runbook_instance_mode = runbook_instance_mode
        if risk_level is not None:
            self.risk_level = risk_level
        if input_param is not None:
            self.input_param = input_param
        if enable_approve is not None:
            self.enable_approve = enable_approve
        if reviewer_notification is not None:
            self.reviewer_notification = reviewer_notification
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if reviewer_user_name is not None:
            self.reviewer_user_name = reviewer_user_name
        if approve_status is not None:
            self.approve_status = approve_status
        if approve_comments is not None:
            self.approve_comments = approve_comments
        if target_instances is not None:
            self.target_instances = target_instances
        if enable_message_notification is not None:
            self.enable_message_notification = enable_message_notification
        if message_notification is not None:
            self.message_notification = message_notification

    @property
    def id(self):
        r"""Gets the id of this ShowScheduledTaskResponse.

        任务ID

        :return: The id of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowScheduledTaskResponse.

        任务ID

        :param id: The id of this ShowScheduledTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowScheduledTaskResponse.

        企业项目id

        :return: The enterprise_project_id of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowScheduledTaskResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowScheduledTaskResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ShowScheduledTaskResponse.

        任务名称

        :return: The name of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowScheduledTaskResponse.

        任务名称

        :param name: The name of this ShowScheduledTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowScheduledTaskResponse.

        委托名称

        :return: The agency_name of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowScheduledTaskResponse.

        委托名称

        :param agency_name: The agency_name of this ShowScheduledTaskResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this ShowScheduledTaskResponse.

        :return: The trigger_time of this ShowScheduledTaskResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this ShowScheduledTaskResponse.

        :param trigger_time: The trigger_time of this ShowScheduledTaskResponse.
        :type trigger_time: :class:`huaweicloudsdkcoc.v1.TriggerTime`
        """
        self._trigger_time = trigger_time

    @property
    def version_no(self):
        r"""Gets the version_no of this ShowScheduledTaskResponse.

        版本号

        :return: The version_no of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._version_no

    @version_no.setter
    def version_no(self, version_no):
        r"""Sets the version_no of this ShowScheduledTaskResponse.

        版本号

        :param version_no: The version_no of this ShowScheduledTaskResponse.
        :type version_no: str
        """
        self._version_no = version_no

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowScheduledTaskResponse.

        任务类型

        :return: The task_type of this ShowScheduledTaskResponse.
        :rtype: object
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowScheduledTaskResponse.

        任务类型

        :param task_type: The task_type of this ShowScheduledTaskResponse.
        :type task_type: object
        """
        self._task_type = task_type

    @property
    def associated_task_id(self):
        r"""Gets the associated_task_id of this ShowScheduledTaskResponse.

        关联任务ID（脚本ID/作业ID）

        :return: The associated_task_id of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._associated_task_id

    @associated_task_id.setter
    def associated_task_id(self, associated_task_id):
        r"""Sets the associated_task_id of this ShowScheduledTaskResponse.

        关联任务ID（脚本ID/作业ID）

        :param associated_task_id: The associated_task_id of this ShowScheduledTaskResponse.
        :type associated_task_id: str
        """
        self._associated_task_id = associated_task_id

    @property
    def associated_task_name(self):
        r"""Gets the associated_task_name of this ShowScheduledTaskResponse.

        关联任务名称（脚本名称/作业名称）

        :return: The associated_task_name of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._associated_task_name

    @associated_task_name.setter
    def associated_task_name(self, associated_task_name):
        r"""Sets the associated_task_name of this ShowScheduledTaskResponse.

        关联任务名称（脚本名称/作业名称）

        :param associated_task_name: The associated_task_name of this ShowScheduledTaskResponse.
        :type associated_task_name: str
        """
        self._associated_task_name = associated_task_name

    @property
    def associated_task_name_en(self):
        r"""Gets the associated_task_name_en of this ShowScheduledTaskResponse.

        关联任务名称(英文)（脚本名称/作业名称）

        :return: The associated_task_name_en of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._associated_task_name_en

    @associated_task_name_en.setter
    def associated_task_name_en(self, associated_task_name_en):
        r"""Sets the associated_task_name_en of this ShowScheduledTaskResponse.

        关联任务名称(英文)（脚本名称/作业名称）

        :param associated_task_name_en: The associated_task_name_en of this ShowScheduledTaskResponse.
        :type associated_task_name_en: str
        """
        self._associated_task_name_en = associated_task_name_en

    @property
    def associated_task_type(self):
        r"""Gets the associated_task_type of this ShowScheduledTaskResponse.

        关联任务的类型

        :return: The associated_task_type of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._associated_task_type

    @associated_task_type.setter
    def associated_task_type(self, associated_task_type):
        r"""Sets the associated_task_type of this ShowScheduledTaskResponse.

        关联任务的类型

        :param associated_task_type: The associated_task_type of this ShowScheduledTaskResponse.
        :type associated_task_type: str
        """
        self._associated_task_type = associated_task_type

    @property
    def runbook_instance_mode(self):
        r"""Gets the runbook_instance_mode of this ShowScheduledTaskResponse.

        作业实例模式

        :return: The runbook_instance_mode of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._runbook_instance_mode

    @runbook_instance_mode.setter
    def runbook_instance_mode(self, runbook_instance_mode):
        r"""Sets the runbook_instance_mode of this ShowScheduledTaskResponse.

        作业实例模式

        :param runbook_instance_mode: The runbook_instance_mode of this ShowScheduledTaskResponse.
        :type runbook_instance_mode: str
        """
        self._runbook_instance_mode = runbook_instance_mode

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ShowScheduledTaskResponse.

        风险等级

        :return: The risk_level of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ShowScheduledTaskResponse.

        风险等级

        :param risk_level: The risk_level of this ShowScheduledTaskResponse.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def input_param(self):
        r"""Gets the input_param of this ShowScheduledTaskResponse.

        执行参数，值为json串

        :return: The input_param of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._input_param

    @input_param.setter
    def input_param(self, input_param):
        r"""Sets the input_param of this ShowScheduledTaskResponse.

        执行参数，值为json串

        :param input_param: The input_param of this ShowScheduledTaskResponse.
        :type input_param: str
        """
        self._input_param = input_param

    @property
    def enable_approve(self):
        r"""Gets the enable_approve of this ShowScheduledTaskResponse.

        是否开启入库人工审核

        :return: The enable_approve of this ShowScheduledTaskResponse.
        :rtype: bool
        """
        return self._enable_approve

    @enable_approve.setter
    def enable_approve(self, enable_approve):
        r"""Sets the enable_approve of this ShowScheduledTaskResponse.

        是否开启入库人工审核

        :param enable_approve: The enable_approve of this ShowScheduledTaskResponse.
        :type enable_approve: bool
        """
        self._enable_approve = enable_approve

    @property
    def reviewer_notification(self):
        r"""Gets the reviewer_notification of this ShowScheduledTaskResponse.

        :return: The reviewer_notification of this ShowScheduledTaskResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        return self._reviewer_notification

    @reviewer_notification.setter
    def reviewer_notification(self, reviewer_notification):
        r"""Sets the reviewer_notification of this ShowScheduledTaskResponse.

        :param reviewer_notification: The reviewer_notification of this ShowScheduledTaskResponse.
        :type reviewer_notification: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        self._reviewer_notification = reviewer_notification

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this ShowScheduledTaskResponse.

        创建人昵称

        :return: The created_user_name of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this ShowScheduledTaskResponse.

        创建人昵称

        :param created_user_name: The created_user_name of this ShowScheduledTaskResponse.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def reviewer_user_name(self):
        r"""Gets the reviewer_user_name of this ShowScheduledTaskResponse.

        审核人昵称

        :return: The reviewer_user_name of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._reviewer_user_name

    @reviewer_user_name.setter
    def reviewer_user_name(self, reviewer_user_name):
        r"""Sets the reviewer_user_name of this ShowScheduledTaskResponse.

        审核人昵称

        :param reviewer_user_name: The reviewer_user_name of this ShowScheduledTaskResponse.
        :type reviewer_user_name: str
        """
        self._reviewer_user_name = reviewer_user_name

    @property
    def approve_status(self):
        r"""Gets the approve_status of this ShowScheduledTaskResponse.

        审批状态

        :return: The approve_status of this ShowScheduledTaskResponse.
        :rtype: object
        """
        return self._approve_status

    @approve_status.setter
    def approve_status(self, approve_status):
        r"""Sets the approve_status of this ShowScheduledTaskResponse.

        审批状态

        :param approve_status: The approve_status of this ShowScheduledTaskResponse.
        :type approve_status: object
        """
        self._approve_status = approve_status

    @property
    def approve_comments(self):
        r"""Gets the approve_comments of this ShowScheduledTaskResponse.

        审批意见

        :return: The approve_comments of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._approve_comments

    @approve_comments.setter
    def approve_comments(self, approve_comments):
        r"""Sets the approve_comments of this ShowScheduledTaskResponse.

        审批意见

        :param approve_comments: The approve_comments of this ShowScheduledTaskResponse.
        :type approve_comments: str
        """
        self._approve_comments = approve_comments

    @property
    def target_instances(self):
        r"""Gets the target_instances of this ShowScheduledTaskResponse.

        目标节点json串

        :return: The target_instances of this ShowScheduledTaskResponse.
        :rtype: str
        """
        return self._target_instances

    @target_instances.setter
    def target_instances(self, target_instances):
        r"""Sets the target_instances of this ShowScheduledTaskResponse.

        目标节点json串

        :param target_instances: The target_instances of this ShowScheduledTaskResponse.
        :type target_instances: str
        """
        self._target_instances = target_instances

    @property
    def enable_message_notification(self):
        r"""Gets the enable_message_notification of this ShowScheduledTaskResponse.

        是否启用消息通知

        :return: The enable_message_notification of this ShowScheduledTaskResponse.
        :rtype: bool
        """
        return self._enable_message_notification

    @enable_message_notification.setter
    def enable_message_notification(self, enable_message_notification):
        r"""Sets the enable_message_notification of this ShowScheduledTaskResponse.

        是否启用消息通知

        :param enable_message_notification: The enable_message_notification of this ShowScheduledTaskResponse.
        :type enable_message_notification: bool
        """
        self._enable_message_notification = enable_message_notification

    @property
    def message_notification(self):
        r"""Gets the message_notification of this ShowScheduledTaskResponse.

        :return: The message_notification of this ShowScheduledTaskResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.MessageNotification`
        """
        return self._message_notification

    @message_notification.setter
    def message_notification(self, message_notification):
        r"""Sets the message_notification of this ShowScheduledTaskResponse.

        :param message_notification: The message_notification of this ShowScheduledTaskResponse.
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
        if not isinstance(other, ShowScheduledTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
