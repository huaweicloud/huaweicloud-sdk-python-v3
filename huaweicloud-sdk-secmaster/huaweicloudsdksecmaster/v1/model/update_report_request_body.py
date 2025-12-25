# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'report_name': 'str',
        'report_period': 'str',
        'report_range': 'UpdateReportRequestBodyReportRange',
        'language': 'str',
        'notification_task': 'str',
        'layout_id': 'str',
        'report_id': 'str',
        'report_rule_infos': 'list[ReportRuleRequest]',
        'title': 'str',
        'to': 'str',
        'cc': 'str',
        'subject': 'str',
        'content': 'str',
        'report_file_type': 'str',
        'frequency': 'str',
        'binding_wizard': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'status': 'status',
        'report_name': 'report_name',
        'report_period': 'report_period',
        'report_range': 'report_range',
        'language': 'language',
        'notification_task': 'notification_task',
        'layout_id': 'layout_id',
        'report_id': 'report_id',
        'report_rule_infos': 'report_rule_infos',
        'title': 'title',
        'to': 'to',
        'cc': 'cc',
        'subject': 'subject',
        'content': 'content',
        'report_file_type': 'report_file_type',
        'frequency': 'frequency',
        'binding_wizard': 'binding_wizard',
        'timezone': 'timezone'
    }

    def __init__(self, status=None, report_name=None, report_period=None, report_range=None, language=None, notification_task=None, layout_id=None, report_id=None, report_rule_infos=None, title=None, to=None, cc=None, subject=None, content=None, report_file_type=None, frequency=None, binding_wizard=None, timezone=None):
        r"""UpdateReportRequestBody

        The model defined in huaweicloud sdk

        :param status: 报告状态 enable, disable
        :type status: str
        :param report_name: 报告名称
        :type report_name: str
        :param report_period: 报告周期 weekly, daily, annual, monthly
        :type report_period: str
        :param report_range: 
        :type report_range: :class:`huaweicloudsdksecmaster.v1.UpdateReportRequestBodyReportRange`
        :param language: 语言
        :type language: str
        :param notification_task: 通知任务id
        :type notification_task: str
        :param layout_id: 布局id
        :type layout_id: str
        :param report_id: 报告Id
        :type report_id: str
        :param report_rule_infos: 报告发送规则
        :type report_rule_infos: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleRequest`]
        :param title: 邮件标题
        :type title: str
        :param to: 收件人
        :type to: str
        :param cc: 抄送人
        :type cc: str
        :param subject: 备注
        :type subject: str
        :param content: 邮件内容
        :type content: str
        :param report_file_type: 报告类型，支持图片、pdf、html
        :type report_file_type: str
        :param frequency: 报告发送频率，daily，monthly，weekly
        :type frequency: str
        :param binding_wizard: 报告页面内容
        :type binding_wizard: str
        :param timezone: 信息
        :type timezone: str
        """
        
        

        self._status = None
        self._report_name = None
        self._report_period = None
        self._report_range = None
        self._language = None
        self._notification_task = None
        self._layout_id = None
        self._report_id = None
        self._report_rule_infos = None
        self._title = None
        self._to = None
        self._cc = None
        self._subject = None
        self._content = None
        self._report_file_type = None
        self._frequency = None
        self._binding_wizard = None
        self._timezone = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.report_name = report_name
        if report_period is not None:
            self.report_period = report_period
        if report_range is not None:
            self.report_range = report_range
        if language is not None:
            self.language = language
        if notification_task is not None:
            self.notification_task = notification_task
        if layout_id is not None:
            self.layout_id = layout_id
        if report_id is not None:
            self.report_id = report_id
        if report_rule_infos is not None:
            self.report_rule_infos = report_rule_infos
        if title is not None:
            self.title = title
        if to is not None:
            self.to = to
        if cc is not None:
            self.cc = cc
        if subject is not None:
            self.subject = subject
        if content is not None:
            self.content = content
        if report_file_type is not None:
            self.report_file_type = report_file_type
        if frequency is not None:
            self.frequency = frequency
        self.binding_wizard = binding_wizard
        if timezone is not None:
            self.timezone = timezone

    @property
    def status(self):
        r"""Gets the status of this UpdateReportRequestBody.

        报告状态 enable, disable

        :return: The status of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateReportRequestBody.

        报告状态 enable, disable

        :param status: The status of this UpdateReportRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def report_name(self):
        r"""Gets the report_name of this UpdateReportRequestBody.

        报告名称

        :return: The report_name of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this UpdateReportRequestBody.

        报告名称

        :param report_name: The report_name of this UpdateReportRequestBody.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_period(self):
        r"""Gets the report_period of this UpdateReportRequestBody.

        报告周期 weekly, daily, annual, monthly

        :return: The report_period of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._report_period

    @report_period.setter
    def report_period(self, report_period):
        r"""Sets the report_period of this UpdateReportRequestBody.

        报告周期 weekly, daily, annual, monthly

        :param report_period: The report_period of this UpdateReportRequestBody.
        :type report_period: str
        """
        self._report_period = report_period

    @property
    def report_range(self):
        r"""Gets the report_range of this UpdateReportRequestBody.

        :return: The report_range of this UpdateReportRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateReportRequestBodyReportRange`
        """
        return self._report_range

    @report_range.setter
    def report_range(self, report_range):
        r"""Sets the report_range of this UpdateReportRequestBody.

        :param report_range: The report_range of this UpdateReportRequestBody.
        :type report_range: :class:`huaweicloudsdksecmaster.v1.UpdateReportRequestBodyReportRange`
        """
        self._report_range = report_range

    @property
    def language(self):
        r"""Gets the language of this UpdateReportRequestBody.

        语言

        :return: The language of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this UpdateReportRequestBody.

        语言

        :param language: The language of this UpdateReportRequestBody.
        :type language: str
        """
        self._language = language

    @property
    def notification_task(self):
        r"""Gets the notification_task of this UpdateReportRequestBody.

        通知任务id

        :return: The notification_task of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._notification_task

    @notification_task.setter
    def notification_task(self, notification_task):
        r"""Sets the notification_task of this UpdateReportRequestBody.

        通知任务id

        :param notification_task: The notification_task of this UpdateReportRequestBody.
        :type notification_task: str
        """
        self._notification_task = notification_task

    @property
    def layout_id(self):
        r"""Gets the layout_id of this UpdateReportRequestBody.

        布局id

        :return: The layout_id of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this UpdateReportRequestBody.

        布局id

        :param layout_id: The layout_id of this UpdateReportRequestBody.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def report_id(self):
        r"""Gets the report_id of this UpdateReportRequestBody.

        报告Id

        :return: The report_id of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this UpdateReportRequestBody.

        报告Id

        :param report_id: The report_id of this UpdateReportRequestBody.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def report_rule_infos(self):
        r"""Gets the report_rule_infos of this UpdateReportRequestBody.

        报告发送规则

        :return: The report_rule_infos of this UpdateReportRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleRequest`]
        """
        return self._report_rule_infos

    @report_rule_infos.setter
    def report_rule_infos(self, report_rule_infos):
        r"""Sets the report_rule_infos of this UpdateReportRequestBody.

        报告发送规则

        :param report_rule_infos: The report_rule_infos of this UpdateReportRequestBody.
        :type report_rule_infos: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleRequest`]
        """
        self._report_rule_infos = report_rule_infos

    @property
    def title(self):
        r"""Gets the title of this UpdateReportRequestBody.

        邮件标题

        :return: The title of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UpdateReportRequestBody.

        邮件标题

        :param title: The title of this UpdateReportRequestBody.
        :type title: str
        """
        self._title = title

    @property
    def to(self):
        r"""Gets the to of this UpdateReportRequestBody.

        收件人

        :return: The to of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this UpdateReportRequestBody.

        收件人

        :param to: The to of this UpdateReportRequestBody.
        :type to: str
        """
        self._to = to

    @property
    def cc(self):
        r"""Gets the cc of this UpdateReportRequestBody.

        抄送人

        :return: The cc of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this UpdateReportRequestBody.

        抄送人

        :param cc: The cc of this UpdateReportRequestBody.
        :type cc: str
        """
        self._cc = cc

    @property
    def subject(self):
        r"""Gets the subject of this UpdateReportRequestBody.

        备注

        :return: The subject of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this UpdateReportRequestBody.

        备注

        :param subject: The subject of this UpdateReportRequestBody.
        :type subject: str
        """
        self._subject = subject

    @property
    def content(self):
        r"""Gets the content of this UpdateReportRequestBody.

        邮件内容

        :return: The content of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this UpdateReportRequestBody.

        邮件内容

        :param content: The content of this UpdateReportRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def report_file_type(self):
        r"""Gets the report_file_type of this UpdateReportRequestBody.

        报告类型，支持图片、pdf、html

        :return: The report_file_type of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._report_file_type

    @report_file_type.setter
    def report_file_type(self, report_file_type):
        r"""Sets the report_file_type of this UpdateReportRequestBody.

        报告类型，支持图片、pdf、html

        :param report_file_type: The report_file_type of this UpdateReportRequestBody.
        :type report_file_type: str
        """
        self._report_file_type = report_file_type

    @property
    def frequency(self):
        r"""Gets the frequency of this UpdateReportRequestBody.

        报告发送频率，daily，monthly，weekly

        :return: The frequency of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this UpdateReportRequestBody.

        报告发送频率，daily，monthly，weekly

        :param frequency: The frequency of this UpdateReportRequestBody.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def binding_wizard(self):
        r"""Gets the binding_wizard of this UpdateReportRequestBody.

        报告页面内容

        :return: The binding_wizard of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._binding_wizard

    @binding_wizard.setter
    def binding_wizard(self, binding_wizard):
        r"""Sets the binding_wizard of this UpdateReportRequestBody.

        报告页面内容

        :param binding_wizard: The binding_wizard of this UpdateReportRequestBody.
        :type binding_wizard: str
        """
        self._binding_wizard = binding_wizard

    @property
    def timezone(self):
        r"""Gets the timezone of this UpdateReportRequestBody.

        信息

        :return: The timezone of this UpdateReportRequestBody.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this UpdateReportRequestBody.

        信息

        :param timezone: The timezone of this UpdateReportRequestBody.
        :type timezone: str
        """
        self._timezone = timezone

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
        if not isinstance(other, UpdateReportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
