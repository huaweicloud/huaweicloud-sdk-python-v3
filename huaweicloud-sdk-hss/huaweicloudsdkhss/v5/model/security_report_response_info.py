# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityReportResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'int',
        'report_sub_id': 'int',
        'default_report': 'bool',
        'latest_create_time': 'int',
        'report_name': 'str',
        'report_category': 'str',
        'report_status': 'str',
        'report_create_time': 'int',
        'sending_period': 'str'
    }

    attribute_map = {
        'report_id': 'report_id',
        'report_sub_id': 'report_sub_id',
        'default_report': 'default_report',
        'latest_create_time': 'latest_create_time',
        'report_name': 'report_name',
        'report_category': 'report_category',
        'report_status': 'report_status',
        'report_create_time': 'report_create_time',
        'sending_period': 'sending_period'
    }

    def __init__(self, report_id=None, report_sub_id=None, default_report=None, latest_create_time=None, report_name=None, report_category=None, report_status=None, report_create_time=None, sending_period=None):
        r"""SecurityReportResponseInfo

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 
        :type report_id: int
        :param report_sub_id: **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 
        :type report_sub_id: int
        :param default_report: **参数解释**: 是否是默认的，默认的不能删除 **取值范围**: - true ：是。 - false ：否。 
        :type default_report: bool
        :param latest_create_time: **参数解释**： 最近生成时间，毫秒(如果返回值为null，代表暂未生成) **取值范围**: 不涉及 
        :type latest_create_time: int
        :param report_name: **参数解释**: 报告名称 **取值范围**: 字符长度1-128位 
        :type report_name: str
        :param report_category: **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 
        :type report_category: str
        :param report_status: **参数解释**: 报告开启状态 **取值范围**:   - opened：开启   - closed：关闭 
        :type report_status: str
        :param report_create_time: **参数解释**： 报告创建时间 **取值范围**: 不涉及 
        :type report_create_time: int
        :param sending_period: **参数解释**: 报告发送的时间段 **取值范围**:   - morning：代表0点到6点   - noon：代表6点到12点   - afternoon：代表12点到18点   - evening：代表18点到24点 
        :type sending_period: str
        """
        
        

        self._report_id = None
        self._report_sub_id = None
        self._default_report = None
        self._latest_create_time = None
        self._report_name = None
        self._report_category = None
        self._report_status = None
        self._report_create_time = None
        self._sending_period = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if report_sub_id is not None:
            self.report_sub_id = report_sub_id
        if default_report is not None:
            self.default_report = default_report
        if latest_create_time is not None:
            self.latest_create_time = latest_create_time
        if report_name is not None:
            self.report_name = report_name
        if report_category is not None:
            self.report_category = report_category
        if report_status is not None:
            self.report_status = report_status
        if report_create_time is not None:
            self.report_create_time = report_create_time
        if sending_period is not None:
            self.sending_period = sending_period

    @property
    def report_id(self):
        r"""Gets the report_id of this SecurityReportResponseInfo.

        **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 

        :return: The report_id of this SecurityReportResponseInfo.
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this SecurityReportResponseInfo.

        **参数解释**: 报告ID **取值范围**: 字符长度10-2147483647位 

        :param report_id: The report_id of this SecurityReportResponseInfo.
        :type report_id: int
        """
        self._report_id = report_id

    @property
    def report_sub_id(self):
        r"""Gets the report_sub_id of this SecurityReportResponseInfo.

        **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 

        :return: The report_sub_id of this SecurityReportResponseInfo.
        :rtype: int
        """
        return self._report_sub_id

    @report_sub_id.setter
    def report_sub_id(self, report_sub_id):
        r"""Sets the report_sub_id of this SecurityReportResponseInfo.

        **参数解释**: 报告子ID **取值范围**: 字符长度10-2147483647位 

        :param report_sub_id: The report_sub_id of this SecurityReportResponseInfo.
        :type report_sub_id: int
        """
        self._report_sub_id = report_sub_id

    @property
    def default_report(self):
        r"""Gets the default_report of this SecurityReportResponseInfo.

        **参数解释**: 是否是默认的，默认的不能删除 **取值范围**: - true ：是。 - false ：否。 

        :return: The default_report of this SecurityReportResponseInfo.
        :rtype: bool
        """
        return self._default_report

    @default_report.setter
    def default_report(self, default_report):
        r"""Sets the default_report of this SecurityReportResponseInfo.

        **参数解释**: 是否是默认的，默认的不能删除 **取值范围**: - true ：是。 - false ：否。 

        :param default_report: The default_report of this SecurityReportResponseInfo.
        :type default_report: bool
        """
        self._default_report = default_report

    @property
    def latest_create_time(self):
        r"""Gets the latest_create_time of this SecurityReportResponseInfo.

        **参数解释**： 最近生成时间，毫秒(如果返回值为null，代表暂未生成) **取值范围**: 不涉及 

        :return: The latest_create_time of this SecurityReportResponseInfo.
        :rtype: int
        """
        return self._latest_create_time

    @latest_create_time.setter
    def latest_create_time(self, latest_create_time):
        r"""Sets the latest_create_time of this SecurityReportResponseInfo.

        **参数解释**： 最近生成时间，毫秒(如果返回值为null，代表暂未生成) **取值范围**: 不涉及 

        :param latest_create_time: The latest_create_time of this SecurityReportResponseInfo.
        :type latest_create_time: int
        """
        self._latest_create_time = latest_create_time

    @property
    def report_name(self):
        r"""Gets the report_name of this SecurityReportResponseInfo.

        **参数解释**: 报告名称 **取值范围**: 字符长度1-128位 

        :return: The report_name of this SecurityReportResponseInfo.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this SecurityReportResponseInfo.

        **参数解释**: 报告名称 **取值范围**: 字符长度1-128位 

        :param report_name: The report_name of this SecurityReportResponseInfo.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_category(self):
        r"""Gets the report_category of this SecurityReportResponseInfo.

        **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 

        :return: The report_category of this SecurityReportResponseInfo.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this SecurityReportResponseInfo.

        **参数解释**: 报告类别 **取值范围**: - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告 

        :param report_category: The report_category of this SecurityReportResponseInfo.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def report_status(self):
        r"""Gets the report_status of this SecurityReportResponseInfo.

        **参数解释**: 报告开启状态 **取值范围**:   - opened：开启   - closed：关闭 

        :return: The report_status of this SecurityReportResponseInfo.
        :rtype: str
        """
        return self._report_status

    @report_status.setter
    def report_status(self, report_status):
        r"""Sets the report_status of this SecurityReportResponseInfo.

        **参数解释**: 报告开启状态 **取值范围**:   - opened：开启   - closed：关闭 

        :param report_status: The report_status of this SecurityReportResponseInfo.
        :type report_status: str
        """
        self._report_status = report_status

    @property
    def report_create_time(self):
        r"""Gets the report_create_time of this SecurityReportResponseInfo.

        **参数解释**： 报告创建时间 **取值范围**: 不涉及 

        :return: The report_create_time of this SecurityReportResponseInfo.
        :rtype: int
        """
        return self._report_create_time

    @report_create_time.setter
    def report_create_time(self, report_create_time):
        r"""Sets the report_create_time of this SecurityReportResponseInfo.

        **参数解释**： 报告创建时间 **取值范围**: 不涉及 

        :param report_create_time: The report_create_time of this SecurityReportResponseInfo.
        :type report_create_time: int
        """
        self._report_create_time = report_create_time

    @property
    def sending_period(self):
        r"""Gets the sending_period of this SecurityReportResponseInfo.

        **参数解释**: 报告发送的时间段 **取值范围**:   - morning：代表0点到6点   - noon：代表6点到12点   - afternoon：代表12点到18点   - evening：代表18点到24点 

        :return: The sending_period of this SecurityReportResponseInfo.
        :rtype: str
        """
        return self._sending_period

    @sending_period.setter
    def sending_period(self, sending_period):
        r"""Sets the sending_period of this SecurityReportResponseInfo.

        **参数解释**: 报告发送的时间段 **取值范围**:   - morning：代表0点到6点   - noon：代表6点到12点   - afternoon：代表12点到18点   - evening：代表18点到24点 

        :param sending_period: The sending_period of this SecurityReportResponseInfo.
        :type sending_period: str
        """
        self._sending_period = sending_period

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
        if not isinstance(other, SecurityReportResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
