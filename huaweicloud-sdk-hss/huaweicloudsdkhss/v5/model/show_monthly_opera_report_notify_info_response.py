# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonthlyOperaReportNotifyInfoResponse(SdkResponse):

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
        'title': 'str',
        'report_id': 'str',
        'current_month': 'int'
    }

    attribute_map = {
        'status': 'status',
        'title': 'title',
        'report_id': 'report_id',
        'current_month': 'current_month'
    }

    def __init__(self, status=None, title=None, report_id=None, current_month=None):
        r"""ShowMonthlyOperaReportNotifyInfoResponse

        The model defined in huaweicloud sdk

        :param status: close:不显示弹框 open：显示弹框
        :type status: str
        :param title: 称号 -vul-fix-master: 补洞大师 -vul-fix-expert: 漏洞修复小能手 -baseline-fix: 风险配置修复高手 -malware-file: 防病毒先锋 -ransomware-event: 防勒索达人 -web-tamper-event: 网站守卫
        :type title: str
        :param report_id: 当前用户唯一标识，报告时间，返回字符串：2024-04
        :type report_id: str
        :param current_month: 当前月份，6
        :type current_month: int
        """
        
        super(ShowMonthlyOperaReportNotifyInfoResponse, self).__init__()

        self._status = None
        self._title = None
        self._report_id = None
        self._current_month = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if report_id is not None:
            self.report_id = report_id
        if current_month is not None:
            self.current_month = current_month

    @property
    def status(self):
        r"""Gets the status of this ShowMonthlyOperaReportNotifyInfoResponse.

        close:不显示弹框 open：显示弹框

        :return: The status of this ShowMonthlyOperaReportNotifyInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowMonthlyOperaReportNotifyInfoResponse.

        close:不显示弹框 open：显示弹框

        :param status: The status of this ShowMonthlyOperaReportNotifyInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def title(self):
        r"""Gets the title of this ShowMonthlyOperaReportNotifyInfoResponse.

        称号 -vul-fix-master: 补洞大师 -vul-fix-expert: 漏洞修复小能手 -baseline-fix: 风险配置修复高手 -malware-file: 防病毒先锋 -ransomware-event: 防勒索达人 -web-tamper-event: 网站守卫

        :return: The title of this ShowMonthlyOperaReportNotifyInfoResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowMonthlyOperaReportNotifyInfoResponse.

        称号 -vul-fix-master: 补洞大师 -vul-fix-expert: 漏洞修复小能手 -baseline-fix: 风险配置修复高手 -malware-file: 防病毒先锋 -ransomware-event: 防勒索达人 -web-tamper-event: 网站守卫

        :param title: The title of this ShowMonthlyOperaReportNotifyInfoResponse.
        :type title: str
        """
        self._title = title

    @property
    def report_id(self):
        r"""Gets the report_id of this ShowMonthlyOperaReportNotifyInfoResponse.

        当前用户唯一标识，报告时间，返回字符串：2024-04

        :return: The report_id of this ShowMonthlyOperaReportNotifyInfoResponse.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ShowMonthlyOperaReportNotifyInfoResponse.

        当前用户唯一标识，报告时间，返回字符串：2024-04

        :param report_id: The report_id of this ShowMonthlyOperaReportNotifyInfoResponse.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def current_month(self):
        r"""Gets the current_month of this ShowMonthlyOperaReportNotifyInfoResponse.

        当前月份，6

        :return: The current_month of this ShowMonthlyOperaReportNotifyInfoResponse.
        :rtype: int
        """
        return self._current_month

    @current_month.setter
    def current_month(self, current_month):
        r"""Sets the current_month of this ShowMonthlyOperaReportNotifyInfoResponse.

        当前月份，6

        :param current_month: The current_month of this ShowMonthlyOperaReportNotifyInfoResponse.
        :type current_month: int
        """
        self._current_month = current_month

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
        if not isinstance(other, ShowMonthlyOperaReportNotifyInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
