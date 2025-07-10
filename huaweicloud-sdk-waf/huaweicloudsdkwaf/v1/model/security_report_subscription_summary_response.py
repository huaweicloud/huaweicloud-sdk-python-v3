# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportSubscriptionSummaryResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str',
        'report_id': 'str',
        'report_name': 'str',
        'sending_period': 'str',
        'report_category': 'str',
        'report_status': 'str',
        'is_all_enterprise_project': 'bool',
        'enterprise_project_id': 'str',
        'template_eps_id': 'str',
        'is_report_created': 'bool',
        'latest_create_time': 'int'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'report_id': 'report_id',
        'report_name': 'report_name',
        'sending_period': 'sending_period',
        'report_category': 'report_category',
        'report_status': 'report_status',
        'is_all_enterprise_project': 'is_all_enterprise_project',
        'enterprise_project_id': 'enterprise_project_id',
        'template_eps_id': 'template_eps_id',
        'is_report_created': 'is_report_created',
        'latest_create_time': 'latest_create_time'
    }

    def __init__(self, subscription_id=None, report_id=None, report_name=None, sending_period=None, report_category=None, report_status=None, is_all_enterprise_project=None, enterprise_project_id=None, template_eps_id=None, is_report_created=None, latest_create_time=None):
        r"""SecurityReportSubscriptionSummaryResponse

        The model defined in huaweicloud sdk

        :param subscription_id: **参数解释：** 订阅ID **取值范围：** 不涉及
        :type subscription_id: str
        :param report_id: **参数解释：** 报告ID **取值范围：** 不涉及
        :type report_id: str
        :param report_name: **参数解释：** 报告模板名称 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。
        :type report_name: str
        :param sending_period: **参数解释：** 发送时间段 **取值范围：** - morning：00:00~06:00 - noon：06:00~12:00 - afternoon：12:00~18:00 - evening：18:00~24:00
        :type sending_period: str
        :param report_category: **参数解释：** 报告类型 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告
        :type report_category: str
        :param report_status: **参数解释：** 开启状态 **取值范围：** - opened：已开启 - closed：已关闭
        :type report_status: str
        :param is_all_enterprise_project: **参数解释：** 是否是所有企业项目 **取值范围：** - true：是所有企业项目 - false：不是所有企业项目
        :type is_all_enterprise_project: bool
        :param enterprise_project_id: **参数解释：** 企业项目ID，当前报告统计的企业项目范围 **取值范围：** 不涉及
        :type enterprise_project_id: str
        :param template_eps_id: **参数解释：** 报告所属项目，生成的报告所归属的企业项目 **取值范围：** 不涉及
        :type template_eps_id: str
        :param is_report_created: **参数解释：** 报告生成状态 **取值范围：** - true：已生成 - false：暂未生成
        :type is_report_created: bool
        :param latest_create_time: **参数解释：** 报告生成时间 **取值范围：** 13位毫秒时间戳
        :type latest_create_time: int
        """
        
        

        self._subscription_id = None
        self._report_id = None
        self._report_name = None
        self._sending_period = None
        self._report_category = None
        self._report_status = None
        self._is_all_enterprise_project = None
        self._enterprise_project_id = None
        self._template_eps_id = None
        self._is_report_created = None
        self._latest_create_time = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if sending_period is not None:
            self.sending_period = sending_period
        if report_category is not None:
            self.report_category = report_category
        if report_status is not None:
            self.report_status = report_status
        if is_all_enterprise_project is not None:
            self.is_all_enterprise_project = is_all_enterprise_project
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if template_eps_id is not None:
            self.template_eps_id = template_eps_id
        if is_report_created is not None:
            self.is_report_created = is_report_created
        if latest_create_time is not None:
            self.latest_create_time = latest_create_time

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 订阅ID **取值范围：** 不涉及

        :return: The subscription_id of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 订阅ID **取值范围：** 不涉及

        :param subscription_id: The subscription_id of this SecurityReportSubscriptionSummaryResponse.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def report_id(self):
        r"""Gets the report_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告ID **取值范围：** 不涉及

        :return: The report_id of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告ID **取值范围：** 不涉及

        :param report_id: The report_id of this SecurityReportSubscriptionSummaryResponse.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def report_name(self):
        r"""Gets the report_name of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告模板名称 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。

        :return: The report_name of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告模板名称 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。

        :param report_name: The report_name of this SecurityReportSubscriptionSummaryResponse.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def sending_period(self):
        r"""Gets the sending_period of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 发送时间段 **取值范围：** - morning：00:00~06:00 - noon：06:00~12:00 - afternoon：12:00~18:00 - evening：18:00~24:00

        :return: The sending_period of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 发送时间段 **取值范围：** - morning：00:00~06:00 - noon：06:00~12:00 - afternoon：12:00~18:00 - evening：18:00~24:00

        :param sending_period: The sending_period of this SecurityReportSubscriptionSummaryResponse.
        :type sending_period: str
        """
        self._sending_period = sending_period

    @property
    def report_category(self):
        r"""Gets the report_category of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告类型 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告

        :return: The report_category of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告类型 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告

        :param report_category: The report_category of this SecurityReportSubscriptionSummaryResponse.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def report_status(self):
        r"""Gets the report_status of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 开启状态 **取值范围：** - opened：已开启 - closed：已关闭

        :return: The report_status of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._report_status

    @report_status.setter
    def report_status(self, report_status):
        r"""Sets the report_status of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 开启状态 **取值范围：** - opened：已开启 - closed：已关闭

        :param report_status: The report_status of this SecurityReportSubscriptionSummaryResponse.
        :type report_status: str
        """
        self._report_status = report_status

    @property
    def is_all_enterprise_project(self):
        r"""Gets the is_all_enterprise_project of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 是否是所有企业项目 **取值范围：** - true：是所有企业项目 - false：不是所有企业项目

        :return: The is_all_enterprise_project of this SecurityReportSubscriptionSummaryResponse.
        :rtype: bool
        """
        return self._is_all_enterprise_project

    @is_all_enterprise_project.setter
    def is_all_enterprise_project(self, is_all_enterprise_project):
        r"""Sets the is_all_enterprise_project of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 是否是所有企业项目 **取值范围：** - true：是所有企业项目 - false：不是所有企业项目

        :param is_all_enterprise_project: The is_all_enterprise_project of this SecurityReportSubscriptionSummaryResponse.
        :type is_all_enterprise_project: bool
        """
        self._is_all_enterprise_project = is_all_enterprise_project

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 企业项目ID，当前报告统计的企业项目范围 **取值范围：** 不涉及

        :return: The enterprise_project_id of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 企业项目ID，当前报告统计的企业项目范围 **取值范围：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this SecurityReportSubscriptionSummaryResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def template_eps_id(self):
        r"""Gets the template_eps_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告所属项目，生成的报告所归属的企业项目 **取值范围：** 不涉及

        :return: The template_eps_id of this SecurityReportSubscriptionSummaryResponse.
        :rtype: str
        """
        return self._template_eps_id

    @template_eps_id.setter
    def template_eps_id(self, template_eps_id):
        r"""Sets the template_eps_id of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告所属项目，生成的报告所归属的企业项目 **取值范围：** 不涉及

        :param template_eps_id: The template_eps_id of this SecurityReportSubscriptionSummaryResponse.
        :type template_eps_id: str
        """
        self._template_eps_id = template_eps_id

    @property
    def is_report_created(self):
        r"""Gets the is_report_created of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告生成状态 **取值范围：** - true：已生成 - false：暂未生成

        :return: The is_report_created of this SecurityReportSubscriptionSummaryResponse.
        :rtype: bool
        """
        return self._is_report_created

    @is_report_created.setter
    def is_report_created(self, is_report_created):
        r"""Sets the is_report_created of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告生成状态 **取值范围：** - true：已生成 - false：暂未生成

        :param is_report_created: The is_report_created of this SecurityReportSubscriptionSummaryResponse.
        :type is_report_created: bool
        """
        self._is_report_created = is_report_created

    @property
    def latest_create_time(self):
        r"""Gets the latest_create_time of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告生成时间 **取值范围：** 13位毫秒时间戳

        :return: The latest_create_time of this SecurityReportSubscriptionSummaryResponse.
        :rtype: int
        """
        return self._latest_create_time

    @latest_create_time.setter
    def latest_create_time(self, latest_create_time):
        r"""Sets the latest_create_time of this SecurityReportSubscriptionSummaryResponse.

        **参数解释：** 报告生成时间 **取值范围：** 13位毫秒时间戳

        :param latest_create_time: The latest_create_time of this SecurityReportSubscriptionSummaryResponse.
        :type latest_create_time: int
        """
        self._latest_create_time = latest_create_time

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
        if not isinstance(other, SecurityReportSubscriptionSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
