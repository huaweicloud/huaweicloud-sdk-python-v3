# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmRulesItemsDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'int',
        'node_id': 'int',
        'remind_type': 'int',
        'topic_name': 'str',
        'urn': 'str',
        'notify_type': 'int',
        'display_number': 'str',
        'callee_number': 'str',
        'complete_time': 'str',
        'create_time': 'int',
        'use_flag': 'int',
        'create_user': 'str',
        'rule_name': 'str',
        'alarm_periods': 'list[AlarmPeriod]',
        'job_directory': 'list[DirectoryDTO]',
        'node_id_list': 'list[int]',
        'node_name_list': 'list[str]',
        'add_mode': 'str',
        'subject_type': 'str',
        'notify_method': 'str',
        'protocol': 'str',
        'other_persons': 'str',
        'max_send_times': 'int',
        'send_interval': 'int',
        'duty_schedule_id': 'int',
        'smn_config_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'node_id': 'node_id',
        'remind_type': 'remind_type',
        'topic_name': 'topic_name',
        'urn': 'urn',
        'notify_type': 'notify_type',
        'display_number': 'display_number',
        'callee_number': 'callee_number',
        'complete_time': 'complete_time',
        'create_time': 'create_time',
        'use_flag': 'use_flag',
        'create_user': 'create_user',
        'rule_name': 'rule_name',
        'alarm_periods': 'alarm_periods',
        'job_directory': 'job_directory',
        'node_id_list': 'node_id_list',
        'node_name_list': 'node_name_list',
        'add_mode': 'add_mode',
        'subject_type': 'subject_type',
        'notify_method': 'notify_method',
        'protocol': 'protocol',
        'other_persons': 'other_persons',
        'max_send_times': 'max_send_times',
        'send_interval': 'send_interval',
        'duty_schedule_id': 'duty_schedule_id',
        'smn_config_id': 'smn_config_id'
    }

    def __init__(self, name=None, id=None, node_id=None, remind_type=None, topic_name=None, urn=None, notify_type=None, display_number=None, callee_number=None, complete_time=None, create_time=None, use_flag=None, create_user=None, rule_name=None, alarm_periods=None, job_directory=None, node_id_list=None, node_name_list=None, add_mode=None, subject_type=None, notify_method=None, protocol=None, other_persons=None, max_send_times=None, send_interval=None, duty_schedule_id=None, smn_config_id=None):
        r"""AlarmRulesItemsDetails

        The model defined in huaweicloud sdk

        :param name: 作业名称。
        :type name: str
        :param id: ID，与业务无关。
        :type id: int
        :param node_id: 作业ID/节点任务ID。
        :type node_id: int
        :param remind_type: 通知类型，0:完成;1:运行异常;3:未完成; 4:资源繁忙; 5-11基线相关的告警。
        :type remind_type: int
        :param topic_name: 租户创建的smn服务的topic名称。
        :type topic_name: str
        :param urn: topic对应URN。
        :type urn: str
        :param notify_type: 节点类型，1:作业; 2: 节点任务; 3: 基线任务。
        :type notify_type: int
        :param display_number: 责任人电话。
        :type display_number: str
        :param callee_number: 被叫方的电话。
        :type callee_number: str
        :param complete_time: 完成时间。
        :type complete_time: str
        :param create_time: 创建时间。
        :type create_time: int
        :param use_flag: 开关。
        :type use_flag: int
        :param create_user: 创建人。
        :type create_user: str
        :param rule_name: 规则名称。
        :type rule_name: str
        :param alarm_periods: 任务告警信息。
        :type alarm_periods: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmPeriod`]
        :param job_directory: 作业目录信息。
        :type job_directory: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryDTO`]
        :param node_id_list: 作业ID/节点任务ID。
        :type node_id_list: list[int]
        :param node_name_list: 作业名称/作业名称.节点任务名称。
        :type node_name_list: list[str]
        :param add_mode: 添加类型。
        :type add_mode: str
        :param subject_type: 告警对象类型。
        :type subject_type: str
        :param notify_method: 告警方式。
        :type notify_method: str
        :param protocol: 终端协议。
        :type protocol: str
        :param other_persons: 抄送人。
        :type other_persons: str
        :param max_send_times: 最大通知次数。
        :type max_send_times: int
        :param send_interval: 最小通知间隔，单位分钟。
        :type send_interval: int
        :param duty_schedule_id: 值班表id。
        :type duty_schedule_id: int
        :param smn_config_id: smn配置id。
        :type smn_config_id: str
        """
        
        

        self._name = None
        self._id = None
        self._node_id = None
        self._remind_type = None
        self._topic_name = None
        self._urn = None
        self._notify_type = None
        self._display_number = None
        self._callee_number = None
        self._complete_time = None
        self._create_time = None
        self._use_flag = None
        self._create_user = None
        self._rule_name = None
        self._alarm_periods = None
        self._job_directory = None
        self._node_id_list = None
        self._node_name_list = None
        self._add_mode = None
        self._subject_type = None
        self._notify_method = None
        self._protocol = None
        self._other_persons = None
        self._max_send_times = None
        self._send_interval = None
        self._duty_schedule_id = None
        self._smn_config_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if node_id is not None:
            self.node_id = node_id
        if remind_type is not None:
            self.remind_type = remind_type
        if topic_name is not None:
            self.topic_name = topic_name
        if urn is not None:
            self.urn = urn
        if notify_type is not None:
            self.notify_type = notify_type
        if display_number is not None:
            self.display_number = display_number
        if callee_number is not None:
            self.callee_number = callee_number
        if complete_time is not None:
            self.complete_time = complete_time
        if create_time is not None:
            self.create_time = create_time
        if use_flag is not None:
            self.use_flag = use_flag
        if create_user is not None:
            self.create_user = create_user
        if rule_name is not None:
            self.rule_name = rule_name
        if alarm_periods is not None:
            self.alarm_periods = alarm_periods
        if job_directory is not None:
            self.job_directory = job_directory
        if node_id_list is not None:
            self.node_id_list = node_id_list
        if node_name_list is not None:
            self.node_name_list = node_name_list
        if add_mode is not None:
            self.add_mode = add_mode
        if subject_type is not None:
            self.subject_type = subject_type
        if notify_method is not None:
            self.notify_method = notify_method
        if protocol is not None:
            self.protocol = protocol
        if other_persons is not None:
            self.other_persons = other_persons
        if max_send_times is not None:
            self.max_send_times = max_send_times
        if send_interval is not None:
            self.send_interval = send_interval
        if duty_schedule_id is not None:
            self.duty_schedule_id = duty_schedule_id
        if smn_config_id is not None:
            self.smn_config_id = smn_config_id

    @property
    def name(self):
        r"""Gets the name of this AlarmRulesItemsDetails.

        作业名称。

        :return: The name of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmRulesItemsDetails.

        作业名称。

        :param name: The name of this AlarmRulesItemsDetails.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this AlarmRulesItemsDetails.

        ID，与业务无关。

        :return: The id of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlarmRulesItemsDetails.

        ID，与业务无关。

        :param id: The id of this AlarmRulesItemsDetails.
        :type id: int
        """
        self._id = id

    @property
    def node_id(self):
        r"""Gets the node_id of this AlarmRulesItemsDetails.

        作业ID/节点任务ID。

        :return: The node_id of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this AlarmRulesItemsDetails.

        作业ID/节点任务ID。

        :param node_id: The node_id of this AlarmRulesItemsDetails.
        :type node_id: int
        """
        self._node_id = node_id

    @property
    def remind_type(self):
        r"""Gets the remind_type of this AlarmRulesItemsDetails.

        通知类型，0:完成;1:运行异常;3:未完成; 4:资源繁忙; 5-11基线相关的告警。

        :return: The remind_type of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._remind_type

    @remind_type.setter
    def remind_type(self, remind_type):
        r"""Sets the remind_type of this AlarmRulesItemsDetails.

        通知类型，0:完成;1:运行异常;3:未完成; 4:资源繁忙; 5-11基线相关的告警。

        :param remind_type: The remind_type of this AlarmRulesItemsDetails.
        :type remind_type: int
        """
        self._remind_type = remind_type

    @property
    def topic_name(self):
        r"""Gets the topic_name of this AlarmRulesItemsDetails.

        租户创建的smn服务的topic名称。

        :return: The topic_name of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        r"""Sets the topic_name of this AlarmRulesItemsDetails.

        租户创建的smn服务的topic名称。

        :param topic_name: The topic_name of this AlarmRulesItemsDetails.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def urn(self):
        r"""Gets the urn of this AlarmRulesItemsDetails.

        topic对应URN。

        :return: The urn of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this AlarmRulesItemsDetails.

        topic对应URN。

        :param urn: The urn of this AlarmRulesItemsDetails.
        :type urn: str
        """
        self._urn = urn

    @property
    def notify_type(self):
        r"""Gets the notify_type of this AlarmRulesItemsDetails.

        节点类型，1:作业; 2: 节点任务; 3: 基线任务。

        :return: The notify_type of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._notify_type

    @notify_type.setter
    def notify_type(self, notify_type):
        r"""Sets the notify_type of this AlarmRulesItemsDetails.

        节点类型，1:作业; 2: 节点任务; 3: 基线任务。

        :param notify_type: The notify_type of this AlarmRulesItemsDetails.
        :type notify_type: int
        """
        self._notify_type = notify_type

    @property
    def display_number(self):
        r"""Gets the display_number of this AlarmRulesItemsDetails.

        责任人电话。

        :return: The display_number of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._display_number

    @display_number.setter
    def display_number(self, display_number):
        r"""Sets the display_number of this AlarmRulesItemsDetails.

        责任人电话。

        :param display_number: The display_number of this AlarmRulesItemsDetails.
        :type display_number: str
        """
        self._display_number = display_number

    @property
    def callee_number(self):
        r"""Gets the callee_number of this AlarmRulesItemsDetails.

        被叫方的电话。

        :return: The callee_number of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._callee_number

    @callee_number.setter
    def callee_number(self, callee_number):
        r"""Sets the callee_number of this AlarmRulesItemsDetails.

        被叫方的电话。

        :param callee_number: The callee_number of this AlarmRulesItemsDetails.
        :type callee_number: str
        """
        self._callee_number = callee_number

    @property
    def complete_time(self):
        r"""Gets the complete_time of this AlarmRulesItemsDetails.

        完成时间。

        :return: The complete_time of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._complete_time

    @complete_time.setter
    def complete_time(self, complete_time):
        r"""Sets the complete_time of this AlarmRulesItemsDetails.

        完成时间。

        :param complete_time: The complete_time of this AlarmRulesItemsDetails.
        :type complete_time: str
        """
        self._complete_time = complete_time

    @property
    def create_time(self):
        r"""Gets the create_time of this AlarmRulesItemsDetails.

        创建时间。

        :return: The create_time of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AlarmRulesItemsDetails.

        创建时间。

        :param create_time: The create_time of this AlarmRulesItemsDetails.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def use_flag(self):
        r"""Gets the use_flag of this AlarmRulesItemsDetails.

        开关。

        :return: The use_flag of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._use_flag

    @use_flag.setter
    def use_flag(self, use_flag):
        r"""Sets the use_flag of this AlarmRulesItemsDetails.

        开关。

        :param use_flag: The use_flag of this AlarmRulesItemsDetails.
        :type use_flag: int
        """
        self._use_flag = use_flag

    @property
    def create_user(self):
        r"""Gets the create_user of this AlarmRulesItemsDetails.

        创建人。

        :return: The create_user of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this AlarmRulesItemsDetails.

        创建人。

        :param create_user: The create_user of this AlarmRulesItemsDetails.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def rule_name(self):
        r"""Gets the rule_name of this AlarmRulesItemsDetails.

        规则名称。

        :return: The rule_name of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this AlarmRulesItemsDetails.

        规则名称。

        :param rule_name: The rule_name of this AlarmRulesItemsDetails.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def alarm_periods(self):
        r"""Gets the alarm_periods of this AlarmRulesItemsDetails.

        任务告警信息。

        :return: The alarm_periods of this AlarmRulesItemsDetails.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmPeriod`]
        """
        return self._alarm_periods

    @alarm_periods.setter
    def alarm_periods(self, alarm_periods):
        r"""Sets the alarm_periods of this AlarmRulesItemsDetails.

        任务告警信息。

        :param alarm_periods: The alarm_periods of this AlarmRulesItemsDetails.
        :type alarm_periods: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmPeriod`]
        """
        self._alarm_periods = alarm_periods

    @property
    def job_directory(self):
        r"""Gets the job_directory of this AlarmRulesItemsDetails.

        作业目录信息。

        :return: The job_directory of this AlarmRulesItemsDetails.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryDTO`]
        """
        return self._job_directory

    @job_directory.setter
    def job_directory(self, job_directory):
        r"""Sets the job_directory of this AlarmRulesItemsDetails.

        作业目录信息。

        :param job_directory: The job_directory of this AlarmRulesItemsDetails.
        :type job_directory: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryDTO`]
        """
        self._job_directory = job_directory

    @property
    def node_id_list(self):
        r"""Gets the node_id_list of this AlarmRulesItemsDetails.

        作业ID/节点任务ID。

        :return: The node_id_list of this AlarmRulesItemsDetails.
        :rtype: list[int]
        """
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, node_id_list):
        r"""Sets the node_id_list of this AlarmRulesItemsDetails.

        作业ID/节点任务ID。

        :param node_id_list: The node_id_list of this AlarmRulesItemsDetails.
        :type node_id_list: list[int]
        """
        self._node_id_list = node_id_list

    @property
    def node_name_list(self):
        r"""Gets the node_name_list of this AlarmRulesItemsDetails.

        作业名称/作业名称.节点任务名称。

        :return: The node_name_list of this AlarmRulesItemsDetails.
        :rtype: list[str]
        """
        return self._node_name_list

    @node_name_list.setter
    def node_name_list(self, node_name_list):
        r"""Sets the node_name_list of this AlarmRulesItemsDetails.

        作业名称/作业名称.节点任务名称。

        :param node_name_list: The node_name_list of this AlarmRulesItemsDetails.
        :type node_name_list: list[str]
        """
        self._node_name_list = node_name_list

    @property
    def add_mode(self):
        r"""Gets the add_mode of this AlarmRulesItemsDetails.

        添加类型。

        :return: The add_mode of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._add_mode

    @add_mode.setter
    def add_mode(self, add_mode):
        r"""Sets the add_mode of this AlarmRulesItemsDetails.

        添加类型。

        :param add_mode: The add_mode of this AlarmRulesItemsDetails.
        :type add_mode: str
        """
        self._add_mode = add_mode

    @property
    def subject_type(self):
        r"""Gets the subject_type of this AlarmRulesItemsDetails.

        告警对象类型。

        :return: The subject_type of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        r"""Sets the subject_type of this AlarmRulesItemsDetails.

        告警对象类型。

        :param subject_type: The subject_type of this AlarmRulesItemsDetails.
        :type subject_type: str
        """
        self._subject_type = subject_type

    @property
    def notify_method(self):
        r"""Gets the notify_method of this AlarmRulesItemsDetails.

        告警方式。

        :return: The notify_method of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._notify_method

    @notify_method.setter
    def notify_method(self, notify_method):
        r"""Sets the notify_method of this AlarmRulesItemsDetails.

        告警方式。

        :param notify_method: The notify_method of this AlarmRulesItemsDetails.
        :type notify_method: str
        """
        self._notify_method = notify_method

    @property
    def protocol(self):
        r"""Gets the protocol of this AlarmRulesItemsDetails.

        终端协议。

        :return: The protocol of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AlarmRulesItemsDetails.

        终端协议。

        :param protocol: The protocol of this AlarmRulesItemsDetails.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def other_persons(self):
        r"""Gets the other_persons of this AlarmRulesItemsDetails.

        抄送人。

        :return: The other_persons of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._other_persons

    @other_persons.setter
    def other_persons(self, other_persons):
        r"""Sets the other_persons of this AlarmRulesItemsDetails.

        抄送人。

        :param other_persons: The other_persons of this AlarmRulesItemsDetails.
        :type other_persons: str
        """
        self._other_persons = other_persons

    @property
    def max_send_times(self):
        r"""Gets the max_send_times of this AlarmRulesItemsDetails.

        最大通知次数。

        :return: The max_send_times of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._max_send_times

    @max_send_times.setter
    def max_send_times(self, max_send_times):
        r"""Sets the max_send_times of this AlarmRulesItemsDetails.

        最大通知次数。

        :param max_send_times: The max_send_times of this AlarmRulesItemsDetails.
        :type max_send_times: int
        """
        self._max_send_times = max_send_times

    @property
    def send_interval(self):
        r"""Gets the send_interval of this AlarmRulesItemsDetails.

        最小通知间隔，单位分钟。

        :return: The send_interval of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._send_interval

    @send_interval.setter
    def send_interval(self, send_interval):
        r"""Sets the send_interval of this AlarmRulesItemsDetails.

        最小通知间隔，单位分钟。

        :param send_interval: The send_interval of this AlarmRulesItemsDetails.
        :type send_interval: int
        """
        self._send_interval = send_interval

    @property
    def duty_schedule_id(self):
        r"""Gets the duty_schedule_id of this AlarmRulesItemsDetails.

        值班表id。

        :return: The duty_schedule_id of this AlarmRulesItemsDetails.
        :rtype: int
        """
        return self._duty_schedule_id

    @duty_schedule_id.setter
    def duty_schedule_id(self, duty_schedule_id):
        r"""Sets the duty_schedule_id of this AlarmRulesItemsDetails.

        值班表id。

        :param duty_schedule_id: The duty_schedule_id of this AlarmRulesItemsDetails.
        :type duty_schedule_id: int
        """
        self._duty_schedule_id = duty_schedule_id

    @property
    def smn_config_id(self):
        r"""Gets the smn_config_id of this AlarmRulesItemsDetails.

        smn配置id。

        :return: The smn_config_id of this AlarmRulesItemsDetails.
        :rtype: str
        """
        return self._smn_config_id

    @smn_config_id.setter
    def smn_config_id(self, smn_config_id):
        r"""Sets the smn_config_id of this AlarmRulesItemsDetails.

        smn配置id。

        :param smn_config_id: The smn_config_id of this AlarmRulesItemsDetails.
        :type smn_config_id: str
        """
        self._smn_config_id = smn_config_id

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
        if not isinstance(other, AlarmRulesItemsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
