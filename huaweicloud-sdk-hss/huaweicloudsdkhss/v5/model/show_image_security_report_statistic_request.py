# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageSecurityReportStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'security_report_type': 'str',
        'body': 'BatchExportSWRBaselineInfoRequestInfo'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'security_report_type': 'security_report_type',
        'body': 'body'
    }

    def __init__(self, region=None, enterprise_project_id=None, security_report_type=None, body=None):
        r"""ShowImageSecurityReportStatisticRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param security_report_type: 安全报告类型，包含如下:   - vulnerability: 漏洞信息   - risk-config: 基线配置信息   - malwares: 恶意文件信息   - apps: 软件信息   - files: 文件信息   - sensitive-info: 敏感信息   - non-compliant-app: 软件合规信息   - build-command-risks: 镜像构建指令风险
        :type security_report_type: str
        :param body: Body of the ShowImageSecurityReportStatisticRequest
        :type body: :class:`huaweicloudsdkhss.v5.BatchExportSWRBaselineInfoRequestInfo`
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._security_report_type = None
        self._body = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.security_report_type = security_report_type
        if body is not None:
            self.body = body

    @property
    def region(self):
        r"""Gets the region of this ShowImageSecurityReportStatisticRequest.

        Region ID

        :return: The region of this ShowImageSecurityReportStatisticRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowImageSecurityReportStatisticRequest.

        Region ID

        :param region: The region of this ShowImageSecurityReportStatisticRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowImageSecurityReportStatisticRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ShowImageSecurityReportStatisticRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowImageSecurityReportStatisticRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ShowImageSecurityReportStatisticRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_report_type(self):
        r"""Gets the security_report_type of this ShowImageSecurityReportStatisticRequest.

        安全报告类型，包含如下:   - vulnerability: 漏洞信息   - risk-config: 基线配置信息   - malwares: 恶意文件信息   - apps: 软件信息   - files: 文件信息   - sensitive-info: 敏感信息   - non-compliant-app: 软件合规信息   - build-command-risks: 镜像构建指令风险

        :return: The security_report_type of this ShowImageSecurityReportStatisticRequest.
        :rtype: str
        """
        return self._security_report_type

    @security_report_type.setter
    def security_report_type(self, security_report_type):
        r"""Sets the security_report_type of this ShowImageSecurityReportStatisticRequest.

        安全报告类型，包含如下:   - vulnerability: 漏洞信息   - risk-config: 基线配置信息   - malwares: 恶意文件信息   - apps: 软件信息   - files: 文件信息   - sensitive-info: 敏感信息   - non-compliant-app: 软件合规信息   - build-command-risks: 镜像构建指令风险

        :param security_report_type: The security_report_type of this ShowImageSecurityReportStatisticRequest.
        :type security_report_type: str
        """
        self._security_report_type = security_report_type

    @property
    def body(self):
        r"""Gets the body of this ShowImageSecurityReportStatisticRequest.

        :return: The body of this ShowImageSecurityReportStatisticRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.BatchExportSWRBaselineInfoRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowImageSecurityReportStatisticRequest.

        :param body: The body of this ShowImageSecurityReportStatisticRequest.
        :type body: :class:`huaweicloudsdkhss.v5.BatchExportSWRBaselineInfoRequestInfo`
        """
        self._body = body

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
        if not isinstance(other, ShowImageSecurityReportStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
