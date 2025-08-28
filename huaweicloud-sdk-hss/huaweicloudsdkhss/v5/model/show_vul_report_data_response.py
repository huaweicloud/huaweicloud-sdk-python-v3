# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulReportDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sumary': 'ShowVulReportDataResponseInfoSumary',
        'hosts': 'list[ShowVulReportDataResponseInfoHosts]',
        'vulnerabilities': 'list[ShowVulReportDataResponseInfoVulnerabilities]',
        'report_create_time': 'int',
        'vulnerability_total_count': 'int',
        'host_total_count': 'int'
    }

    attribute_map = {
        'sumary': 'sumary',
        'hosts': 'hosts',
        'vulnerabilities': 'vulnerabilities',
        'report_create_time': 'report_create_time',
        'vulnerability_total_count': 'vulnerability_total_count',
        'host_total_count': 'host_total_count'
    }

    def __init__(self, sumary=None, hosts=None, vulnerabilities=None, report_create_time=None, vulnerability_total_count=None, host_total_count=None):
        r"""ShowVulReportDataResponse

        The model defined in huaweicloud sdk

        :param sumary: 
        :type sumary: :class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoSumary`
        :param hosts: 主机列表
        :type hosts: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoHosts`]
        :param vulnerabilities: 漏洞列表
        :type vulnerabilities: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoVulnerabilities`]
        :param report_create_time: **参数解释**： 报告生成时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type report_create_time: int
        :param vulnerability_total_count: **参数解释**： 漏洞总数量 **取值范围**： 最小值0，最大值10000000 
        :type vulnerability_total_count: int
        :param host_total_count: **参数解释**： 主机总数量 **取值范围**： 最小值0，最大值20000 
        :type host_total_count: int
        """
        
        super(ShowVulReportDataResponse, self).__init__()

        self._sumary = None
        self._hosts = None
        self._vulnerabilities = None
        self._report_create_time = None
        self._vulnerability_total_count = None
        self._host_total_count = None
        self.discriminator = None

        if sumary is not None:
            self.sumary = sumary
        if hosts is not None:
            self.hosts = hosts
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities
        if report_create_time is not None:
            self.report_create_time = report_create_time
        if vulnerability_total_count is not None:
            self.vulnerability_total_count = vulnerability_total_count
        if host_total_count is not None:
            self.host_total_count = host_total_count

    @property
    def sumary(self):
        r"""Gets the sumary of this ShowVulReportDataResponse.

        :return: The sumary of this ShowVulReportDataResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoSumary`
        """
        return self._sumary

    @sumary.setter
    def sumary(self, sumary):
        r"""Sets the sumary of this ShowVulReportDataResponse.

        :param sumary: The sumary of this ShowVulReportDataResponse.
        :type sumary: :class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoSumary`
        """
        self._sumary = sumary

    @property
    def hosts(self):
        r"""Gets the hosts of this ShowVulReportDataResponse.

        主机列表

        :return: The hosts of this ShowVulReportDataResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoHosts`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ShowVulReportDataResponse.

        主机列表

        :param hosts: The hosts of this ShowVulReportDataResponse.
        :type hosts: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoHosts`]
        """
        self._hosts = hosts

    @property
    def vulnerabilities(self):
        r"""Gets the vulnerabilities of this ShowVulReportDataResponse.

        漏洞列表

        :return: The vulnerabilities of this ShowVulReportDataResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoVulnerabilities`]
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        r"""Sets the vulnerabilities of this ShowVulReportDataResponse.

        漏洞列表

        :param vulnerabilities: The vulnerabilities of this ShowVulReportDataResponse.
        :type vulnerabilities: list[:class:`huaweicloudsdkhss.v5.ShowVulReportDataResponseInfoVulnerabilities`]
        """
        self._vulnerabilities = vulnerabilities

    @property
    def report_create_time(self):
        r"""Gets the report_create_time of this ShowVulReportDataResponse.

        **参数解释**： 报告生成时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The report_create_time of this ShowVulReportDataResponse.
        :rtype: int
        """
        return self._report_create_time

    @report_create_time.setter
    def report_create_time(self, report_create_time):
        r"""Sets the report_create_time of this ShowVulReportDataResponse.

        **参数解释**： 报告生成时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param report_create_time: The report_create_time of this ShowVulReportDataResponse.
        :type report_create_time: int
        """
        self._report_create_time = report_create_time

    @property
    def vulnerability_total_count(self):
        r"""Gets the vulnerability_total_count of this ShowVulReportDataResponse.

        **参数解释**： 漏洞总数量 **取值范围**： 最小值0，最大值10000000 

        :return: The vulnerability_total_count of this ShowVulReportDataResponse.
        :rtype: int
        """
        return self._vulnerability_total_count

    @vulnerability_total_count.setter
    def vulnerability_total_count(self, vulnerability_total_count):
        r"""Sets the vulnerability_total_count of this ShowVulReportDataResponse.

        **参数解释**： 漏洞总数量 **取值范围**： 最小值0，最大值10000000 

        :param vulnerability_total_count: The vulnerability_total_count of this ShowVulReportDataResponse.
        :type vulnerability_total_count: int
        """
        self._vulnerability_total_count = vulnerability_total_count

    @property
    def host_total_count(self):
        r"""Gets the host_total_count of this ShowVulReportDataResponse.

        **参数解释**： 主机总数量 **取值范围**： 最小值0，最大值20000 

        :return: The host_total_count of this ShowVulReportDataResponse.
        :rtype: int
        """
        return self._host_total_count

    @host_total_count.setter
    def host_total_count(self, host_total_count):
        r"""Sets the host_total_count of this ShowVulReportDataResponse.

        **参数解释**： 主机总数量 **取值范围**： 最小值0，最大值20000 

        :param host_total_count: The host_total_count of this ShowVulReportDataResponse.
        :type host_total_count: int
        """
        self._host_total_count = host_total_count

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
        if not isinstance(other, ShowVulReportDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
