# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostRiskResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'agent_status': 'str',
        'install_result_code': 'str',
        'version': 'str',
        'protect_status': 'str',
        'detect_result': 'str',
        'asset': 'int',
        'vulnerability': 'int',
        'baseline': 'int',
        'intrusion': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'agent_status': 'agent_status',
        'install_result_code': 'install_result_code',
        'version': 'version',
        'protect_status': 'protect_status',
        'detect_result': 'detect_result',
        'asset': 'asset',
        'vulnerability': 'vulnerability',
        'baseline': 'baseline',
        'intrusion': 'intrusion'
    }

    def __init__(self, host_id=None, agent_status=None, install_result_code=None, version=None, protect_status=None, detect_result=None, asset=None, vulnerability=None, baseline=None, intrusion=None):
        r"""HostRiskResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param agent_status: Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。
        :type agent_status: str
        :param install_result_code: 安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。
        :type install_result_code: str
        :param version: 主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。
        :type protect_status: str
        :param detect_result: 云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。
        :type detect_result: str
        :param asset: 资产风险
        :type asset: int
        :param vulnerability: 漏洞风险
        :type vulnerability: int
        :param baseline: 基线风险
        :type baseline: int
        :param intrusion: 入侵风险
        :type intrusion: int
        """
        
        

        self._host_id = None
        self._agent_status = None
        self._install_result_code = None
        self._version = None
        self._protect_status = None
        self._detect_result = None
        self._asset = None
        self._vulnerability = None
        self._baseline = None
        self._intrusion = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if agent_status is not None:
            self.agent_status = agent_status
        if install_result_code is not None:
            self.install_result_code = install_result_code
        if version is not None:
            self.version = version
        if protect_status is not None:
            self.protect_status = protect_status
        if detect_result is not None:
            self.detect_result = detect_result
        if asset is not None:
            self.asset = asset
        if vulnerability is not None:
            self.vulnerability = vulnerability
        if baseline is not None:
            self.baseline = baseline
        if intrusion is not None:
            self.intrusion = intrusion

    @property
    def host_id(self):
        r"""Gets the host_id of this HostRiskResponseInfo.

        服务器ID

        :return: The host_id of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HostRiskResponseInfo.

        服务器ID

        :param host_id: The host_id of this HostRiskResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_status(self):
        r"""Gets the agent_status of this HostRiskResponseInfo.

        Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :return: The agent_status of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this HostRiskResponseInfo.

        Agent状态，包含如下5种。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。

        :param agent_status: The agent_status of this HostRiskResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def install_result_code(self):
        r"""Gets the install_result_code of this HostRiskResponseInfo.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :return: The install_result_code of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._install_result_code

    @install_result_code.setter
    def install_result_code(self, install_result_code):
        r"""Sets the install_result_code of this HostRiskResponseInfo.

        安装结果，包含如下12种。   - install_succeed ：安装成功。   - network_access_timeout ：网络不通，访问超时。   - invalid_port ：无效端口。   - auth_failed ：认证错误，口令不正确。   - permission_denied ：权限错误，被拒绝。   - no_available_vpc ：没有相同VPC的agent在线虚拟机。   - install_exception ：安装异常。   - invalid_param ：参数错误。   - install_failed ：安装失败。   - package_unavailable ：安装包失效。   - os_type_not_support ：系统类型错误。   - os_arch_not_support ：架构类型错误。

        :param install_result_code: The install_result_code of this HostRiskResponseInfo.
        :type install_result_code: str
        """
        self._install_result_code = install_result_code

    @property
    def version(self):
        r"""Gets the version of this HostRiskResponseInfo.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HostRiskResponseInfo.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version: The version of this HostRiskResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this HostRiskResponseInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :return: The protect_status of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this HostRiskResponseInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :param protect_status: The protect_status of this HostRiskResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this HostRiskResponseInfo.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :return: The detect_result of this HostRiskResponseInfo.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this HostRiskResponseInfo.

        云主机安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :param detect_result: The detect_result of this HostRiskResponseInfo.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def asset(self):
        r"""Gets the asset of this HostRiskResponseInfo.

        资产风险

        :return: The asset of this HostRiskResponseInfo.
        :rtype: int
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this HostRiskResponseInfo.

        资产风险

        :param asset: The asset of this HostRiskResponseInfo.
        :type asset: int
        """
        self._asset = asset

    @property
    def vulnerability(self):
        r"""Gets the vulnerability of this HostRiskResponseInfo.

        漏洞风险

        :return: The vulnerability of this HostRiskResponseInfo.
        :rtype: int
        """
        return self._vulnerability

    @vulnerability.setter
    def vulnerability(self, vulnerability):
        r"""Sets the vulnerability of this HostRiskResponseInfo.

        漏洞风险

        :param vulnerability: The vulnerability of this HostRiskResponseInfo.
        :type vulnerability: int
        """
        self._vulnerability = vulnerability

    @property
    def baseline(self):
        r"""Gets the baseline of this HostRiskResponseInfo.

        基线风险

        :return: The baseline of this HostRiskResponseInfo.
        :rtype: int
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this HostRiskResponseInfo.

        基线风险

        :param baseline: The baseline of this HostRiskResponseInfo.
        :type baseline: int
        """
        self._baseline = baseline

    @property
    def intrusion(self):
        r"""Gets the intrusion of this HostRiskResponseInfo.

        入侵风险

        :return: The intrusion of this HostRiskResponseInfo.
        :rtype: int
        """
        return self._intrusion

    @intrusion.setter
    def intrusion(self, intrusion):
        r"""Sets the intrusion of this HostRiskResponseInfo.

        入侵风险

        :param intrusion: The intrusion of this HostRiskResponseInfo.
        :type intrusion: int
        """
        self._intrusion = intrusion

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
        if not isinstance(other, HostRiskResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
