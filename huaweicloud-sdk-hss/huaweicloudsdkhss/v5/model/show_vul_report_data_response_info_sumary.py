# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulReportDataResponseInfoSumary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_num_repair_necessity': 'int',
        'vul_num_unfixed': 'int',
        'vul_num_linux': 'int',
        'vul_num_windows': 'int',
        'vul_num_web_cms': 'int',
        'vul_num_app': 'int',
        'host_num_risk': 'int',
        'host_num_high_risk': 'int',
        'host_num_medium_risk': 'int',
        'host_num_low_risk': 'int',
        'affect_asset_num_important': 'int',
        'affect_asset_num_common': 'int',
        'affect_asset_num_test': 'int'
    }

    attribute_map = {
        'vul_num_repair_necessity': 'vul_num_repair_necessity',
        'vul_num_unfixed': 'vul_num_unfixed',
        'vul_num_linux': 'vul_num_linux',
        'vul_num_windows': 'vul_num_windows',
        'vul_num_web_cms': 'vul_num_web_cms',
        'vul_num_app': 'vul_num_app',
        'host_num_risk': 'host_num_risk',
        'host_num_high_risk': 'host_num_high_risk',
        'host_num_medium_risk': 'host_num_medium_risk',
        'host_num_low_risk': 'host_num_low_risk',
        'affect_asset_num_important': 'affect_asset_num_important',
        'affect_asset_num_common': 'affect_asset_num_common',
        'affect_asset_num_test': 'affect_asset_num_test'
    }

    def __init__(self, vul_num_repair_necessity=None, vul_num_unfixed=None, vul_num_linux=None, vul_num_windows=None, vul_num_web_cms=None, vul_num_app=None, host_num_risk=None, host_num_high_risk=None, host_num_medium_risk=None, host_num_low_risk=None, affect_asset_num_important=None, affect_asset_num_common=None, affect_asset_num_test=None):
        r"""ShowVulReportDataResponseInfoSumary

        The model defined in huaweicloud sdk

        :param vul_num_repair_necessity: **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_repair_necessity: int
        :param vul_num_unfixed: **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_unfixed: int
        :param vul_num_linux: **参数解释**: linxu漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_linux: int
        :param vul_num_windows: **参数解释**: windows的漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_windows: int
        :param vul_num_web_cms: **参数解释**: web-cms的漏洞数量 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_web_cms: int
        :param vul_num_app: **参数解释**: 应用漏洞 **取值范围**: 最小值0，最大值1000000 
        :type vul_num_app: int
        :param host_num_risk: **参数解释**: 有风险的主机数量 **取值范围**: 最小值0，最大值1000000 
        :type host_num_risk: int
        :param host_num_high_risk: **参数解释**: 有高危风险的主机数量 **取值范围**: 最小值0，最大值1000000 
        :type host_num_high_risk: int
        :param host_num_medium_risk: **参数解释**: 有中危风险的主机数量 **取值范围**: 最小值0，最大值1000000 
        :type host_num_medium_risk: int
        :param host_num_low_risk: **参数解释**: 有低危风险的主机数量 **取值范围**: 最小值0，最大值1000000 
        :type host_num_low_risk: int
        :param affect_asset_num_important: **参数解释**: 受影响的重要资产数量 **取值范围**: 最小值0，最大值1000000 
        :type affect_asset_num_important: int
        :param affect_asset_num_common: **参数解释**: 受影响的一般资产数量 **取值范围**: 最小值0，最大值1000000 
        :type affect_asset_num_common: int
        :param affect_asset_num_test: **参数解释**: 受影响的测试资产数量 **取值范围**: 最小值0，最大值1000000 
        :type affect_asset_num_test: int
        """
        
        

        self._vul_num_repair_necessity = None
        self._vul_num_unfixed = None
        self._vul_num_linux = None
        self._vul_num_windows = None
        self._vul_num_web_cms = None
        self._vul_num_app = None
        self._host_num_risk = None
        self._host_num_high_risk = None
        self._host_num_medium_risk = None
        self._host_num_low_risk = None
        self._affect_asset_num_important = None
        self._affect_asset_num_common = None
        self._affect_asset_num_test = None
        self.discriminator = None

        if vul_num_repair_necessity is not None:
            self.vul_num_repair_necessity = vul_num_repair_necessity
        if vul_num_unfixed is not None:
            self.vul_num_unfixed = vul_num_unfixed
        if vul_num_linux is not None:
            self.vul_num_linux = vul_num_linux
        if vul_num_windows is not None:
            self.vul_num_windows = vul_num_windows
        if vul_num_web_cms is not None:
            self.vul_num_web_cms = vul_num_web_cms
        if vul_num_app is not None:
            self.vul_num_app = vul_num_app
        if host_num_risk is not None:
            self.host_num_risk = host_num_risk
        if host_num_high_risk is not None:
            self.host_num_high_risk = host_num_high_risk
        if host_num_medium_risk is not None:
            self.host_num_medium_risk = host_num_medium_risk
        if host_num_low_risk is not None:
            self.host_num_low_risk = host_num_low_risk
        if affect_asset_num_important is not None:
            self.affect_asset_num_important = affect_asset_num_important
        if affect_asset_num_common is not None:
            self.affect_asset_num_common = affect_asset_num_common
        if affect_asset_num_test is not None:
            self.affect_asset_num_test = affect_asset_num_test

    @property
    def vul_num_repair_necessity(self):
        r"""Gets the vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_repair_necessity

    @vul_num_repair_necessity.setter
    def vul_num_repair_necessity(self, vul_num_repair_necessity):
        r"""Sets the vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 紧急修复漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_repair_necessity: The vul_num_repair_necessity of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_repair_necessity: int
        """
        self._vul_num_repair_necessity = vul_num_repair_necessity

    @property
    def vul_num_unfixed(self):
        r"""Gets the vul_num_unfixed of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_unfixed of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_unfixed

    @vul_num_unfixed.setter
    def vul_num_unfixed(self, vul_num_unfixed):
        r"""Sets the vul_num_unfixed of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 未完成修复的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_unfixed: The vul_num_unfixed of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_unfixed: int
        """
        self._vul_num_unfixed = vul_num_unfixed

    @property
    def vul_num_linux(self):
        r"""Gets the vul_num_linux of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: linxu漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_linux of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_linux

    @vul_num_linux.setter
    def vul_num_linux(self, vul_num_linux):
        r"""Sets the vul_num_linux of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: linxu漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_linux: The vul_num_linux of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_linux: int
        """
        self._vul_num_linux = vul_num_linux

    @property
    def vul_num_windows(self):
        r"""Gets the vul_num_windows of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: windows的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_windows of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_windows

    @vul_num_windows.setter
    def vul_num_windows(self, vul_num_windows):
        r"""Sets the vul_num_windows of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: windows的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_windows: The vul_num_windows of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_windows: int
        """
        self._vul_num_windows = vul_num_windows

    @property
    def vul_num_web_cms(self):
        r"""Gets the vul_num_web_cms of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: web-cms的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_web_cms of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_web_cms

    @vul_num_web_cms.setter
    def vul_num_web_cms(self, vul_num_web_cms):
        r"""Sets the vul_num_web_cms of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: web-cms的漏洞数量 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_web_cms: The vul_num_web_cms of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_web_cms: int
        """
        self._vul_num_web_cms = vul_num_web_cms

    @property
    def vul_num_app(self):
        r"""Gets the vul_num_app of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 应用漏洞 **取值范围**: 最小值0，最大值1000000 

        :return: The vul_num_app of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._vul_num_app

    @vul_num_app.setter
    def vul_num_app(self, vul_num_app):
        r"""Sets the vul_num_app of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 应用漏洞 **取值范围**: 最小值0，最大值1000000 

        :param vul_num_app: The vul_num_app of this ShowVulReportDataResponseInfoSumary.
        :type vul_num_app: int
        """
        self._vul_num_app = vul_num_app

    @property
    def host_num_risk(self):
        r"""Gets the host_num_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :return: The host_num_risk of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._host_num_risk

    @host_num_risk.setter
    def host_num_risk(self, host_num_risk):
        r"""Sets the host_num_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :param host_num_risk: The host_num_risk of this ShowVulReportDataResponseInfoSumary.
        :type host_num_risk: int
        """
        self._host_num_risk = host_num_risk

    @property
    def host_num_high_risk(self):
        r"""Gets the host_num_high_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有高危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :return: The host_num_high_risk of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._host_num_high_risk

    @host_num_high_risk.setter
    def host_num_high_risk(self, host_num_high_risk):
        r"""Sets the host_num_high_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有高危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :param host_num_high_risk: The host_num_high_risk of this ShowVulReportDataResponseInfoSumary.
        :type host_num_high_risk: int
        """
        self._host_num_high_risk = host_num_high_risk

    @property
    def host_num_medium_risk(self):
        r"""Gets the host_num_medium_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有中危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :return: The host_num_medium_risk of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._host_num_medium_risk

    @host_num_medium_risk.setter
    def host_num_medium_risk(self, host_num_medium_risk):
        r"""Sets the host_num_medium_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有中危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :param host_num_medium_risk: The host_num_medium_risk of this ShowVulReportDataResponseInfoSumary.
        :type host_num_medium_risk: int
        """
        self._host_num_medium_risk = host_num_medium_risk

    @property
    def host_num_low_risk(self):
        r"""Gets the host_num_low_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有低危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :return: The host_num_low_risk of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._host_num_low_risk

    @host_num_low_risk.setter
    def host_num_low_risk(self, host_num_low_risk):
        r"""Sets the host_num_low_risk of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 有低危风险的主机数量 **取值范围**: 最小值0，最大值1000000 

        :param host_num_low_risk: The host_num_low_risk of this ShowVulReportDataResponseInfoSumary.
        :type host_num_low_risk: int
        """
        self._host_num_low_risk = host_num_low_risk

    @property
    def affect_asset_num_important(self):
        r"""Gets the affect_asset_num_important of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的重要资产数量 **取值范围**: 最小值0，最大值1000000 

        :return: The affect_asset_num_important of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._affect_asset_num_important

    @affect_asset_num_important.setter
    def affect_asset_num_important(self, affect_asset_num_important):
        r"""Sets the affect_asset_num_important of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的重要资产数量 **取值范围**: 最小值0，最大值1000000 

        :param affect_asset_num_important: The affect_asset_num_important of this ShowVulReportDataResponseInfoSumary.
        :type affect_asset_num_important: int
        """
        self._affect_asset_num_important = affect_asset_num_important

    @property
    def affect_asset_num_common(self):
        r"""Gets the affect_asset_num_common of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的一般资产数量 **取值范围**: 最小值0，最大值1000000 

        :return: The affect_asset_num_common of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._affect_asset_num_common

    @affect_asset_num_common.setter
    def affect_asset_num_common(self, affect_asset_num_common):
        r"""Sets the affect_asset_num_common of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的一般资产数量 **取值范围**: 最小值0，最大值1000000 

        :param affect_asset_num_common: The affect_asset_num_common of this ShowVulReportDataResponseInfoSumary.
        :type affect_asset_num_common: int
        """
        self._affect_asset_num_common = affect_asset_num_common

    @property
    def affect_asset_num_test(self):
        r"""Gets the affect_asset_num_test of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的测试资产数量 **取值范围**: 最小值0，最大值1000000 

        :return: The affect_asset_num_test of this ShowVulReportDataResponseInfoSumary.
        :rtype: int
        """
        return self._affect_asset_num_test

    @affect_asset_num_test.setter
    def affect_asset_num_test(self, affect_asset_num_test):
        r"""Sets the affect_asset_num_test of this ShowVulReportDataResponseInfoSumary.

        **参数解释**: 受影响的测试资产数量 **取值范围**: 最小值0，最大值1000000 

        :param affect_asset_num_test: The affect_asset_num_test of this ShowVulReportDataResponseInfoSumary.
        :type affect_asset_num_test: int
        """
        self._affect_asset_num_test = affect_asset_num_test

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
        if not isinstance(other, ShowVulReportDataResponseInfoSumary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
