# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportRuleInfo:

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
        'project_id': 'str',
        'workspace_id': 'str',
        'cycle': 'str',
        'rule': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'email_title': 'str',
        'email_to': 'str',
        'email_content': 'str',
        'report_file_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'cycle': 'cycle',
        'rule': 'rule',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'email_title': 'email_title',
        'email_to': 'email_to',
        'email_content': 'email_content',
        'report_file_type': 'report_file_type'
    }

    def __init__(self, id=None, project_id=None, workspace_id=None, cycle=None, rule=None, start_time=None, end_time=None, email_title=None, email_to=None, email_content=None, report_file_type=None):
        r"""ReportRuleInfo

        The model defined in huaweicloud sdk

        :param id: 报告发送规则id
        :type id: str
        :param project_id: 租户ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param cycle: 数据周期
        :type cycle: str
        :param rule: cron表达式
        :type rule: str
        :param start_time: 报告数据周期开始时间
        :type start_time: str
        :param end_time: 报告数据周期结束时间
        :type end_time: str
        :param email_title: 邮件标题
        :type email_title: str
        :param email_to: 收件人邮箱
        :type email_to: str
        :param email_content: 邮件内容
        :type email_content: str
        :param report_file_type: 报告类型，支持图片、pdf、html
        :type report_file_type: str
        """
        
        

        self._id = None
        self._project_id = None
        self._workspace_id = None
        self._cycle = None
        self._rule = None
        self._start_time = None
        self._end_time = None
        self._email_title = None
        self._email_to = None
        self._email_content = None
        self._report_file_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.cycle = cycle
        self.rule = rule
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if email_title is not None:
            self.email_title = email_title
        if email_to is not None:
            self.email_to = email_to
        if email_content is not None:
            self.email_content = email_content
        if report_file_type is not None:
            self.report_file_type = report_file_type

    @property
    def id(self):
        r"""Gets the id of this ReportRuleInfo.

        报告发送规则id

        :return: The id of this ReportRuleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReportRuleInfo.

        报告发送规则id

        :param id: The id of this ReportRuleInfo.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this ReportRuleInfo.

        租户ID

        :return: The project_id of this ReportRuleInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ReportRuleInfo.

        租户ID

        :param project_id: The project_id of this ReportRuleInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ReportRuleInfo.

        工作空间ID

        :return: The workspace_id of this ReportRuleInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ReportRuleInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this ReportRuleInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def cycle(self):
        r"""Gets the cycle of this ReportRuleInfo.

        数据周期

        :return: The cycle of this ReportRuleInfo.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this ReportRuleInfo.

        数据周期

        :param cycle: The cycle of this ReportRuleInfo.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def rule(self):
        r"""Gets the rule of this ReportRuleInfo.

        cron表达式

        :return: The rule of this ReportRuleInfo.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ReportRuleInfo.

        cron表达式

        :param rule: The rule of this ReportRuleInfo.
        :type rule: str
        """
        self._rule = rule

    @property
    def start_time(self):
        r"""Gets the start_time of this ReportRuleInfo.

        报告数据周期开始时间

        :return: The start_time of this ReportRuleInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ReportRuleInfo.

        报告数据周期开始时间

        :param start_time: The start_time of this ReportRuleInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ReportRuleInfo.

        报告数据周期结束时间

        :return: The end_time of this ReportRuleInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ReportRuleInfo.

        报告数据周期结束时间

        :param end_time: The end_time of this ReportRuleInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def email_title(self):
        r"""Gets the email_title of this ReportRuleInfo.

        邮件标题

        :return: The email_title of this ReportRuleInfo.
        :rtype: str
        """
        return self._email_title

    @email_title.setter
    def email_title(self, email_title):
        r"""Sets the email_title of this ReportRuleInfo.

        邮件标题

        :param email_title: The email_title of this ReportRuleInfo.
        :type email_title: str
        """
        self._email_title = email_title

    @property
    def email_to(self):
        r"""Gets the email_to of this ReportRuleInfo.

        收件人邮箱

        :return: The email_to of this ReportRuleInfo.
        :rtype: str
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        r"""Sets the email_to of this ReportRuleInfo.

        收件人邮箱

        :param email_to: The email_to of this ReportRuleInfo.
        :type email_to: str
        """
        self._email_to = email_to

    @property
    def email_content(self):
        r"""Gets the email_content of this ReportRuleInfo.

        邮件内容

        :return: The email_content of this ReportRuleInfo.
        :rtype: str
        """
        return self._email_content

    @email_content.setter
    def email_content(self, email_content):
        r"""Sets the email_content of this ReportRuleInfo.

        邮件内容

        :param email_content: The email_content of this ReportRuleInfo.
        :type email_content: str
        """
        self._email_content = email_content

    @property
    def report_file_type(self):
        r"""Gets the report_file_type of this ReportRuleInfo.

        报告类型，支持图片、pdf、html

        :return: The report_file_type of this ReportRuleInfo.
        :rtype: str
        """
        return self._report_file_type

    @report_file_type.setter
    def report_file_type(self, report_file_type):
        r"""Sets the report_file_type of this ReportRuleInfo.

        报告类型，支持图片、pdf、html

        :param report_file_type: The report_file_type of this ReportRuleInfo.
        :type report_file_type: str
        """
        self._report_file_type = report_file_type

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
        if not isinstance(other, ReportRuleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
