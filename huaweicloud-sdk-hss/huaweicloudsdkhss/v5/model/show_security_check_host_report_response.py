# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityCheckHostReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_result': 'SecurityCheckHostResultResponseInfo',
        'host_status': 'str',
        'scan_period_start': 'int',
        'scan_period_end': 'int',
        'risk_rating': 'int',
        'severity': 'str',
        'risk_num': 'int',
        'scan_time': 'int',
        'free': 'bool',
        'event_num_info': 'SecurityCheckRiskNumInfo',
        'vul_num_info': 'SecurityCheckRiskNumInfo',
        'baseline_num_info': 'SecurityCheckRiskNumInfo',
        'asset_num_info': 'SecurityCheckRiskNumInfo',
        'asset_change_num': 'int',
        'app_num': 'int',
        'port_num': 'int',
        'event_list': 'list[SecurityCheckRiskEventInfo]',
        'vul_list': 'list[SecurityCheckVulInfo]',
        'security_config_list': 'list[SecurityConfigInfo]',
        'security_config_item_list': 'list[SecurityConfigItemInfo]',
        'pwd_policy_list': 'list[SecurityConfigPwdPolicyInfo]',
        'weak_pwd_list': 'list[SecurityConfigWeakPwdInfo]',
        'user_change_list': 'list[SecurityConfigUserChangeInfo]',
        'port_list': 'list[SecurityConfigPortInfo]',
        'app_list': 'list[AppResponseInfo]'
    }

    attribute_map = {
        'host_result': 'host_result',
        'host_status': 'host_status',
        'scan_period_start': 'scan_period_start',
        'scan_period_end': 'scan_period_end',
        'risk_rating': 'risk_rating',
        'severity': 'severity',
        'risk_num': 'risk_num',
        'scan_time': 'scan_time',
        'free': 'free',
        'event_num_info': 'event_num_info',
        'vul_num_info': 'vul_num_info',
        'baseline_num_info': 'baseline_num_info',
        'asset_num_info': 'asset_num_info',
        'asset_change_num': 'asset_change_num',
        'app_num': 'app_num',
        'port_num': 'port_num',
        'event_list': 'event_list',
        'vul_list': 'vul_list',
        'security_config_list': 'security_config_list',
        'security_config_item_list': 'security_config_item_list',
        'pwd_policy_list': 'pwd_policy_list',
        'weak_pwd_list': 'weak_pwd_list',
        'user_change_list': 'user_change_list',
        'port_list': 'port_list',
        'app_list': 'app_list'
    }

    def __init__(self, host_result=None, host_status=None, scan_period_start=None, scan_period_end=None, risk_rating=None, severity=None, risk_num=None, scan_time=None, free=None, event_num_info=None, vul_num_info=None, baseline_num_info=None, asset_num_info=None, asset_change_num=None, app_num=None, port_num=None, event_list=None, vul_list=None, security_config_list=None, security_config_item_list=None, pwd_policy_list=None, weak_pwd_list=None, user_change_list=None, port_list=None, app_list=None):
        r"""ShowSecurityCheckHostReportResponse

        The model defined in huaweicloud sdk

        :param host_result: 
        :type host_result: :class:`huaweicloudsdkhss.v5.SecurityCheckHostResultResponseInfo`
        :param host_status: **参数解释**： 服务器运行状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 
        :type host_status: str
        :param scan_period_start: **参数解释**： 体检周期开始时间 **取值范围**： 不涉及 
        :type scan_period_start: int
        :param scan_period_end: **参数解释**： 体检周期结束时间 **取值范围**： 不涉及 
        :type scan_period_end: int
        :param risk_rating: **参数解释**： 风险评分 **取值范围**： 不涉及 
        :type risk_rating: int
        :param severity: **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 
        :type severity: str
        :param risk_num: **参数解释**： 安全风险数量 **取值范围**： 不涉及 
        :type risk_num: int
        :param scan_time: **参数解释**： 最新检测时间 **取值范围**： 不涉及 
        :type scan_time: int
        :param free: **参数解释**: 是否是免费安全体检的报告 **取值范围**: - true：免费安全体检的报告 - false：非免费安全体检的报告 
        :type free: bool
        :param event_num_info: 
        :type event_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        :param vul_num_info: 
        :type vul_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        :param baseline_num_info: 
        :type baseline_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        :param asset_num_info: 
        :type asset_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        :param asset_change_num: **参数解释**： 主机资产变动记录数量 **取值范围**： 不涉及 
        :type asset_change_num: int
        :param app_num: **参数解释**： 软件数量 **取值范围**： 不涉及 
        :type app_num: int
        :param port_num: **参数解释**： 危险端口数量 **取值范围**： 不涉及 
        :type port_num: int
        :param event_list: **参数解释**： 入侵事件列表 **取值范围**： 不涉及 
        :type event_list: list[:class:`huaweicloudsdkhss.v5.SecurityCheckRiskEventInfo`]
        :param vul_list: **参数解释**： 漏洞列表 **取值范围**： 不涉及 
        :type vul_list: list[:class:`huaweicloudsdkhss.v5.SecurityCheckVulInfo`]
        :param security_config_list: **参数解释**： 配置检测列表 **取值范围**： 不涉及 
        :type security_config_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigInfo`]
        :param security_config_item_list: **参数解释**： 配置检查项列表 **取值范围**： 不涉及 
        :type security_config_item_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigItemInfo`]
        :param pwd_policy_list: **参数解释**： 口令复杂度策略列表 **取值范围**： 不涉及 
        :type pwd_policy_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPwdPolicyInfo`]
        :param weak_pwd_list: **参数解释**： 经典弱口令列表 **取值范围**： 不涉及 
        :type weak_pwd_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigWeakPwdInfo`]
        :param user_change_list: **参数解释**： 主机账户的历史变动记录 **取值范围**： 不涉及 
        :type user_change_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigUserChangeInfo`]
        :param port_list: **参数解释**： 危险开放端口列表 **取值范围**： 不涉及 
        :type port_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPortInfo`]
        :param app_list: **参数解释**： 资产的软件列表 **取值范围**： 不涉及 
        :type app_list: list[:class:`huaweicloudsdkhss.v5.AppResponseInfo`]
        """
        
        super(ShowSecurityCheckHostReportResponse, self).__init__()

        self._host_result = None
        self._host_status = None
        self._scan_period_start = None
        self._scan_period_end = None
        self._risk_rating = None
        self._severity = None
        self._risk_num = None
        self._scan_time = None
        self._free = None
        self._event_num_info = None
        self._vul_num_info = None
        self._baseline_num_info = None
        self._asset_num_info = None
        self._asset_change_num = None
        self._app_num = None
        self._port_num = None
        self._event_list = None
        self._vul_list = None
        self._security_config_list = None
        self._security_config_item_list = None
        self._pwd_policy_list = None
        self._weak_pwd_list = None
        self._user_change_list = None
        self._port_list = None
        self._app_list = None
        self.discriminator = None

        if host_result is not None:
            self.host_result = host_result
        if host_status is not None:
            self.host_status = host_status
        if scan_period_start is not None:
            self.scan_period_start = scan_period_start
        if scan_period_end is not None:
            self.scan_period_end = scan_period_end
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if severity is not None:
            self.severity = severity
        if risk_num is not None:
            self.risk_num = risk_num
        if scan_time is not None:
            self.scan_time = scan_time
        if free is not None:
            self.free = free
        if event_num_info is not None:
            self.event_num_info = event_num_info
        if vul_num_info is not None:
            self.vul_num_info = vul_num_info
        if baseline_num_info is not None:
            self.baseline_num_info = baseline_num_info
        if asset_num_info is not None:
            self.asset_num_info = asset_num_info
        if asset_change_num is not None:
            self.asset_change_num = asset_change_num
        if app_num is not None:
            self.app_num = app_num
        if port_num is not None:
            self.port_num = port_num
        if event_list is not None:
            self.event_list = event_list
        if vul_list is not None:
            self.vul_list = vul_list
        if security_config_list is not None:
            self.security_config_list = security_config_list
        if security_config_item_list is not None:
            self.security_config_item_list = security_config_item_list
        if pwd_policy_list is not None:
            self.pwd_policy_list = pwd_policy_list
        if weak_pwd_list is not None:
            self.weak_pwd_list = weak_pwd_list
        if user_change_list is not None:
            self.user_change_list = user_change_list
        if port_list is not None:
            self.port_list = port_list
        if app_list is not None:
            self.app_list = app_list

    @property
    def host_result(self):
        r"""Gets the host_result of this ShowSecurityCheckHostReportResponse.

        :return: The host_result of this ShowSecurityCheckHostReportResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckHostResultResponseInfo`
        """
        return self._host_result

    @host_result.setter
    def host_result(self, host_result):
        r"""Sets the host_result of this ShowSecurityCheckHostReportResponse.

        :param host_result: The host_result of this ShowSecurityCheckHostReportResponse.
        :type host_result: :class:`huaweicloudsdkhss.v5.SecurityCheckHostResultResponseInfo`
        """
        self._host_result = host_result

    @property
    def host_status(self):
        r"""Gets the host_status of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 服务器运行状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :return: The host_status of this ShowSecurityCheckHostReportResponse.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 服务器运行状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :param host_status: The host_status of this ShowSecurityCheckHostReportResponse.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def scan_period_start(self):
        r"""Gets the scan_period_start of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 体检周期开始时间 **取值范围**： 不涉及 

        :return: The scan_period_start of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._scan_period_start

    @scan_period_start.setter
    def scan_period_start(self, scan_period_start):
        r"""Sets the scan_period_start of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 体检周期开始时间 **取值范围**： 不涉及 

        :param scan_period_start: The scan_period_start of this ShowSecurityCheckHostReportResponse.
        :type scan_period_start: int
        """
        self._scan_period_start = scan_period_start

    @property
    def scan_period_end(self):
        r"""Gets the scan_period_end of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 体检周期结束时间 **取值范围**： 不涉及 

        :return: The scan_period_end of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._scan_period_end

    @scan_period_end.setter
    def scan_period_end(self, scan_period_end):
        r"""Sets the scan_period_end of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 体检周期结束时间 **取值范围**： 不涉及 

        :param scan_period_end: The scan_period_end of this ShowSecurityCheckHostReportResponse.
        :type scan_period_end: int
        """
        self._scan_period_end = scan_period_end

    @property
    def risk_rating(self):
        r"""Gets the risk_rating of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 风险评分 **取值范围**： 不涉及 

        :return: The risk_rating of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        r"""Sets the risk_rating of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 风险评分 **取值范围**： 不涉及 

        :param risk_rating: The risk_rating of this ShowSecurityCheckHostReportResponse.
        :type risk_rating: int
        """
        self._risk_rating = risk_rating

    @property
    def severity(self):
        r"""Gets the severity of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :return: The severity of this ShowSecurityCheckHostReportResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 风险级别 **取值范围**： - high：高危 - medium：中危 - low：低危 - safe：安全，无风险 

        :param severity: The severity of this ShowSecurityCheckHostReportResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 安全风险数量 **取值范围**： 不涉及 

        :return: The risk_num of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 安全风险数量 **取值范围**： 不涉及 

        :param risk_num: The risk_num of this ShowSecurityCheckHostReportResponse.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :return: The scan_time of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this ShowSecurityCheckHostReportResponse.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def free(self):
        r"""Gets the free of this ShowSecurityCheckHostReportResponse.

        **参数解释**: 是否是免费安全体检的报告 **取值范围**: - true：免费安全体检的报告 - false：非免费安全体检的报告 

        :return: The free of this ShowSecurityCheckHostReportResponse.
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        r"""Sets the free of this ShowSecurityCheckHostReportResponse.

        **参数解释**: 是否是免费安全体检的报告 **取值范围**: - true：免费安全体检的报告 - false：非免费安全体检的报告 

        :param free: The free of this ShowSecurityCheckHostReportResponse.
        :type free: bool
        """
        self._free = free

    @property
    def event_num_info(self):
        r"""Gets the event_num_info of this ShowSecurityCheckHostReportResponse.

        :return: The event_num_info of this ShowSecurityCheckHostReportResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        return self._event_num_info

    @event_num_info.setter
    def event_num_info(self, event_num_info):
        r"""Sets the event_num_info of this ShowSecurityCheckHostReportResponse.

        :param event_num_info: The event_num_info of this ShowSecurityCheckHostReportResponse.
        :type event_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        self._event_num_info = event_num_info

    @property
    def vul_num_info(self):
        r"""Gets the vul_num_info of this ShowSecurityCheckHostReportResponse.

        :return: The vul_num_info of this ShowSecurityCheckHostReportResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        return self._vul_num_info

    @vul_num_info.setter
    def vul_num_info(self, vul_num_info):
        r"""Sets the vul_num_info of this ShowSecurityCheckHostReportResponse.

        :param vul_num_info: The vul_num_info of this ShowSecurityCheckHostReportResponse.
        :type vul_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        self._vul_num_info = vul_num_info

    @property
    def baseline_num_info(self):
        r"""Gets the baseline_num_info of this ShowSecurityCheckHostReportResponse.

        :return: The baseline_num_info of this ShowSecurityCheckHostReportResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        return self._baseline_num_info

    @baseline_num_info.setter
    def baseline_num_info(self, baseline_num_info):
        r"""Sets the baseline_num_info of this ShowSecurityCheckHostReportResponse.

        :param baseline_num_info: The baseline_num_info of this ShowSecurityCheckHostReportResponse.
        :type baseline_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        self._baseline_num_info = baseline_num_info

    @property
    def asset_num_info(self):
        r"""Gets the asset_num_info of this ShowSecurityCheckHostReportResponse.

        :return: The asset_num_info of this ShowSecurityCheckHostReportResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        return self._asset_num_info

    @asset_num_info.setter
    def asset_num_info(self, asset_num_info):
        r"""Sets the asset_num_info of this ShowSecurityCheckHostReportResponse.

        :param asset_num_info: The asset_num_info of this ShowSecurityCheckHostReportResponse.
        :type asset_num_info: :class:`huaweicloudsdkhss.v5.SecurityCheckRiskNumInfo`
        """
        self._asset_num_info = asset_num_info

    @property
    def asset_change_num(self):
        r"""Gets the asset_change_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 主机资产变动记录数量 **取值范围**： 不涉及 

        :return: The asset_change_num of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._asset_change_num

    @asset_change_num.setter
    def asset_change_num(self, asset_change_num):
        r"""Sets the asset_change_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 主机资产变动记录数量 **取值范围**： 不涉及 

        :param asset_change_num: The asset_change_num of this ShowSecurityCheckHostReportResponse.
        :type asset_change_num: int
        """
        self._asset_change_num = asset_change_num

    @property
    def app_num(self):
        r"""Gets the app_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 软件数量 **取值范围**： 不涉及 

        :return: The app_num of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._app_num

    @app_num.setter
    def app_num(self, app_num):
        r"""Sets the app_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 软件数量 **取值范围**： 不涉及 

        :param app_num: The app_num of this ShowSecurityCheckHostReportResponse.
        :type app_num: int
        """
        self._app_num = app_num

    @property
    def port_num(self):
        r"""Gets the port_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 危险端口数量 **取值范围**： 不涉及 

        :return: The port_num of this ShowSecurityCheckHostReportResponse.
        :rtype: int
        """
        return self._port_num

    @port_num.setter
    def port_num(self, port_num):
        r"""Sets the port_num of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 危险端口数量 **取值范围**： 不涉及 

        :param port_num: The port_num of this ShowSecurityCheckHostReportResponse.
        :type port_num: int
        """
        self._port_num = port_num

    @property
    def event_list(self):
        r"""Gets the event_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 入侵事件列表 **取值范围**： 不涉及 

        :return: The event_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityCheckRiskEventInfo`]
        """
        return self._event_list

    @event_list.setter
    def event_list(self, event_list):
        r"""Sets the event_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 入侵事件列表 **取值范围**： 不涉及 

        :param event_list: The event_list of this ShowSecurityCheckHostReportResponse.
        :type event_list: list[:class:`huaweicloudsdkhss.v5.SecurityCheckRiskEventInfo`]
        """
        self._event_list = event_list

    @property
    def vul_list(self):
        r"""Gets the vul_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 漏洞列表 **取值范围**： 不涉及 

        :return: The vul_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityCheckVulInfo`]
        """
        return self._vul_list

    @vul_list.setter
    def vul_list(self, vul_list):
        r"""Sets the vul_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 漏洞列表 **取值范围**： 不涉及 

        :param vul_list: The vul_list of this ShowSecurityCheckHostReportResponse.
        :type vul_list: list[:class:`huaweicloudsdkhss.v5.SecurityCheckVulInfo`]
        """
        self._vul_list = vul_list

    @property
    def security_config_list(self):
        r"""Gets the security_config_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 配置检测列表 **取值范围**： 不涉及 

        :return: The security_config_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigInfo`]
        """
        return self._security_config_list

    @security_config_list.setter
    def security_config_list(self, security_config_list):
        r"""Sets the security_config_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 配置检测列表 **取值范围**： 不涉及 

        :param security_config_list: The security_config_list of this ShowSecurityCheckHostReportResponse.
        :type security_config_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigInfo`]
        """
        self._security_config_list = security_config_list

    @property
    def security_config_item_list(self):
        r"""Gets the security_config_item_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 配置检查项列表 **取值范围**： 不涉及 

        :return: The security_config_item_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigItemInfo`]
        """
        return self._security_config_item_list

    @security_config_item_list.setter
    def security_config_item_list(self, security_config_item_list):
        r"""Sets the security_config_item_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 配置检查项列表 **取值范围**： 不涉及 

        :param security_config_item_list: The security_config_item_list of this ShowSecurityCheckHostReportResponse.
        :type security_config_item_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigItemInfo`]
        """
        self._security_config_item_list = security_config_item_list

    @property
    def pwd_policy_list(self):
        r"""Gets the pwd_policy_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 口令复杂度策略列表 **取值范围**： 不涉及 

        :return: The pwd_policy_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPwdPolicyInfo`]
        """
        return self._pwd_policy_list

    @pwd_policy_list.setter
    def pwd_policy_list(self, pwd_policy_list):
        r"""Sets the pwd_policy_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 口令复杂度策略列表 **取值范围**： 不涉及 

        :param pwd_policy_list: The pwd_policy_list of this ShowSecurityCheckHostReportResponse.
        :type pwd_policy_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPwdPolicyInfo`]
        """
        self._pwd_policy_list = pwd_policy_list

    @property
    def weak_pwd_list(self):
        r"""Gets the weak_pwd_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 经典弱口令列表 **取值范围**： 不涉及 

        :return: The weak_pwd_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigWeakPwdInfo`]
        """
        return self._weak_pwd_list

    @weak_pwd_list.setter
    def weak_pwd_list(self, weak_pwd_list):
        r"""Sets the weak_pwd_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 经典弱口令列表 **取值范围**： 不涉及 

        :param weak_pwd_list: The weak_pwd_list of this ShowSecurityCheckHostReportResponse.
        :type weak_pwd_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigWeakPwdInfo`]
        """
        self._weak_pwd_list = weak_pwd_list

    @property
    def user_change_list(self):
        r"""Gets the user_change_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 主机账户的历史变动记录 **取值范围**： 不涉及 

        :return: The user_change_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigUserChangeInfo`]
        """
        return self._user_change_list

    @user_change_list.setter
    def user_change_list(self, user_change_list):
        r"""Sets the user_change_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 主机账户的历史变动记录 **取值范围**： 不涉及 

        :param user_change_list: The user_change_list of this ShowSecurityCheckHostReportResponse.
        :type user_change_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigUserChangeInfo`]
        """
        self._user_change_list = user_change_list

    @property
    def port_list(self):
        r"""Gets the port_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 危险开放端口列表 **取值范围**： 不涉及 

        :return: The port_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPortInfo`]
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        r"""Sets the port_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 危险开放端口列表 **取值范围**： 不涉及 

        :param port_list: The port_list of this ShowSecurityCheckHostReportResponse.
        :type port_list: list[:class:`huaweicloudsdkhss.v5.SecurityConfigPortInfo`]
        """
        self._port_list = port_list

    @property
    def app_list(self):
        r"""Gets the app_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 资产的软件列表 **取值范围**： 不涉及 

        :return: The app_list of this ShowSecurityCheckHostReportResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AppResponseInfo`]
        """
        return self._app_list

    @app_list.setter
    def app_list(self, app_list):
        r"""Sets the app_list of this ShowSecurityCheckHostReportResponse.

        **参数解释**： 资产的软件列表 **取值范围**： 不涉及 

        :param app_list: The app_list of this ShowSecurityCheckHostReportResponse.
        :type app_list: list[:class:`huaweicloudsdkhss.v5.AppResponseInfo`]
        """
        self._app_list = app_list

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
        if not isinstance(other, ShowSecurityCheckHostReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
