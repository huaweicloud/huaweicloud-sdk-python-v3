# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportInfoResponse(SdkResponse):

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
        'report_name': 'str',
        'report_period': 'str',
        'report_range': 'CreateReportRequestBodyReportRange',
        'language': 'str',
        'notification_task': 'str',
        'layout_id': 'str',
        'status': 'str',
        'is_generated': 'bool',
        'report_rule_infos': 'list[ReportRuleInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'report_name': 'report_name',
        'report_period': 'report_period',
        'report_range': 'report_range',
        'language': 'language',
        'notification_task': 'notification_task',
        'layout_id': 'layout_id',
        'status': 'status',
        'is_generated': 'is_generated',
        'report_rule_infos': 'report_rule_infos',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, report_name=None, report_period=None, report_range=None, language=None, notification_task=None, layout_id=None, status=None, is_generated=None, report_rule_infos=None, x_request_id=None):
        r"""ShowReportInfoResponse

        The model defined in huaweicloud sdk

        :param id: 报告id
        :type id: str
        :param report_name: 报告名称
        :type report_name: str
        :param report_period: 报告周期 weekly, daily, annual, monthly
        :type report_period: str
        :param report_range: 
        :type report_range: :class:`huaweicloudsdksecmaster.v1.CreateReportRequestBodyReportRange`
        :param language: 语言
        :type language: str
        :param notification_task: 通知任务id
        :type notification_task: str
        :param layout_id: 布局id
        :type layout_id: str
        :param status: 报告状态 enable, disable
        :type status: str
        :param is_generated: 报告是否已生成
        :type is_generated: bool
        :param report_rule_infos: 报告发送规则
        :type report_rule_infos: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._id = None
        self._report_name = None
        self._report_period = None
        self._report_range = None
        self._language = None
        self._notification_task = None
        self._layout_id = None
        self._status = None
        self._is_generated = None
        self._report_rule_infos = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if report_name is not None:
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
        if status is not None:
            self.status = status
        if is_generated is not None:
            self.is_generated = is_generated
        if report_rule_infos is not None:
            self.report_rule_infos = report_rule_infos
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this ShowReportInfoResponse.

        报告id

        :return: The id of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowReportInfoResponse.

        报告id

        :param id: The id of this ShowReportInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def report_name(self):
        r"""Gets the report_name of this ShowReportInfoResponse.

        报告名称

        :return: The report_name of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ShowReportInfoResponse.

        报告名称

        :param report_name: The report_name of this ShowReportInfoResponse.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_period(self):
        r"""Gets the report_period of this ShowReportInfoResponse.

        报告周期 weekly, daily, annual, monthly

        :return: The report_period of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._report_period

    @report_period.setter
    def report_period(self, report_period):
        r"""Sets the report_period of this ShowReportInfoResponse.

        报告周期 weekly, daily, annual, monthly

        :param report_period: The report_period of this ShowReportInfoResponse.
        :type report_period: str
        """
        self._report_period = report_period

    @property
    def report_range(self):
        r"""Gets the report_range of this ShowReportInfoResponse.

        :return: The report_range of this ShowReportInfoResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.CreateReportRequestBodyReportRange`
        """
        return self._report_range

    @report_range.setter
    def report_range(self, report_range):
        r"""Sets the report_range of this ShowReportInfoResponse.

        :param report_range: The report_range of this ShowReportInfoResponse.
        :type report_range: :class:`huaweicloudsdksecmaster.v1.CreateReportRequestBodyReportRange`
        """
        self._report_range = report_range

    @property
    def language(self):
        r"""Gets the language of this ShowReportInfoResponse.

        语言

        :return: The language of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ShowReportInfoResponse.

        语言

        :param language: The language of this ShowReportInfoResponse.
        :type language: str
        """
        self._language = language

    @property
    def notification_task(self):
        r"""Gets the notification_task of this ShowReportInfoResponse.

        通知任务id

        :return: The notification_task of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._notification_task

    @notification_task.setter
    def notification_task(self, notification_task):
        r"""Sets the notification_task of this ShowReportInfoResponse.

        通知任务id

        :param notification_task: The notification_task of this ShowReportInfoResponse.
        :type notification_task: str
        """
        self._notification_task = notification_task

    @property
    def layout_id(self):
        r"""Gets the layout_id of this ShowReportInfoResponse.

        布局id

        :return: The layout_id of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this ShowReportInfoResponse.

        布局id

        :param layout_id: The layout_id of this ShowReportInfoResponse.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def status(self):
        r"""Gets the status of this ShowReportInfoResponse.

        报告状态 enable, disable

        :return: The status of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowReportInfoResponse.

        报告状态 enable, disable

        :param status: The status of this ShowReportInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def is_generated(self):
        r"""Gets the is_generated of this ShowReportInfoResponse.

        报告是否已生成

        :return: The is_generated of this ShowReportInfoResponse.
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        r"""Sets the is_generated of this ShowReportInfoResponse.

        报告是否已生成

        :param is_generated: The is_generated of this ShowReportInfoResponse.
        :type is_generated: bool
        """
        self._is_generated = is_generated

    @property
    def report_rule_infos(self):
        r"""Gets the report_rule_infos of this ShowReportInfoResponse.

        报告发送规则

        :return: The report_rule_infos of this ShowReportInfoResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleInfo`]
        """
        return self._report_rule_infos

    @report_rule_infos.setter
    def report_rule_infos(self, report_rule_infos):
        r"""Sets the report_rule_infos of this ShowReportInfoResponse.

        报告发送规则

        :param report_rule_infos: The report_rule_infos of this ShowReportInfoResponse.
        :type report_rule_infos: list[:class:`huaweicloudsdksecmaster.v1.ReportRuleInfo`]
        """
        self._report_rule_infos = report_rule_infos

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowReportInfoResponse.

        :return: The x_request_id of this ShowReportInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowReportInfoResponse.

        :param x_request_id: The x_request_id of this ShowReportInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowReportInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowReportInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
