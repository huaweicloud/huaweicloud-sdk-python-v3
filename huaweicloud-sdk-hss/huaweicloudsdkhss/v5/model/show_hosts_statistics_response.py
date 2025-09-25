# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostsStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'risk_num': 'int',
        'unprotected_num': 'int',
        'not_installed_num': 'int',
        'installed_failed_num': 'int',
        'not_online_num': 'int',
        'version_basic_num': 'int',
        'version_advanced_num': 'int',
        'version_enterprise_num': 'int',
        'version_premium_num': 'int',
        'version_wtp_num': 'int',
        'version_container_num': 'int',
        'host_group_num': 'int',
        'server_group_num': 'int',
        'asset_value_list': 'list[AssetValueHostNumInfo]',
        'server_group_list': 'list[ServerGroupItem]',
        'ignore_host_num': 'int',
        'protected_num': 'int',
        'protect_interrupt_num': 'int',
        'idle_num': 'int',
        'premium_non_sp_num': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'risk_num': 'risk_num',
        'unprotected_num': 'unprotected_num',
        'not_installed_num': 'not_installed_num',
        'installed_failed_num': 'installed_failed_num',
        'not_online_num': 'not_online_num',
        'version_basic_num': 'version_basic_num',
        'version_advanced_num': 'version_advanced_num',
        'version_enterprise_num': 'version_enterprise_num',
        'version_premium_num': 'version_premium_num',
        'version_wtp_num': 'version_wtp_num',
        'version_container_num': 'version_container_num',
        'host_group_num': 'host_group_num',
        'server_group_num': 'server_group_num',
        'asset_value_list': 'asset_value_list',
        'server_group_list': 'server_group_list',
        'ignore_host_num': 'ignore_host_num',
        'protected_num': 'protected_num',
        'protect_interrupt_num': 'protect_interrupt_num',
        'idle_num': 'idle_num',
        'premium_non_sp_num': 'premium_non_sp_num'
    }

    def __init__(self, total_num=None, risk_num=None, unprotected_num=None, not_installed_num=None, installed_failed_num=None, not_online_num=None, version_basic_num=None, version_advanced_num=None, version_enterprise_num=None, version_premium_num=None, version_wtp_num=None, version_container_num=None, host_group_num=None, server_group_num=None, asset_value_list=None, server_group_list=None, ignore_host_num=None, protected_num=None, protect_interrupt_num=None, idle_num=None, premium_non_sp_num=None):
        r"""ShowHostsStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_num: 服务器总数
        :type total_num: int
        :param risk_num: 有风险服务器数
        :type risk_num: int
        :param unprotected_num: 未防护服务器数
        :type unprotected_num: int
        :param not_installed_num: Agent未安装数
        :type not_installed_num: int
        :param installed_failed_num: Agent安装失败数
        :type installed_failed_num: int
        :param not_online_num: Agent不在线数
        :type not_online_num: int
        :param version_basic_num: 开启基础版服务器数
        :type version_basic_num: int
        :param version_advanced_num: 开启专业版服务器数
        :type version_advanced_num: int
        :param version_enterprise_num: 开启企业版服务器数
        :type version_enterprise_num: int
        :param version_premium_num: 开启旗舰版服务器数
        :type version_premium_num: int
        :param version_wtp_num: 开启网页防篡改版服务器数
        :type version_wtp_num: int
        :param version_container_num: 开启容器版服务器数
        :type version_container_num: int
        :param host_group_num: 服务器组总数
        :type host_group_num: int
        :param server_group_num: 资产服务器组数量
        :type server_group_num: int
        :param asset_value_list: 资产重要性列表
        :type asset_value_list: list[:class:`huaweicloudsdkhss.v5.AssetValueHostNumInfo`]
        :param server_group_list: 服务器组列表
        :type server_group_list: list[:class:`huaweicloudsdkhss.v5.ServerGroupItem`]
        :param ignore_host_num: 已忽略服务器数
        :type ignore_host_num: int
        :param protected_num: 防护中服务器数
        :type protected_num: int
        :param protect_interrupt_num: 防护中断服务器数
        :type protect_interrupt_num: int
        :param idle_num: 空闲配额数
        :type idle_num: int
        :param premium_non_sp_num: 旗舰版主机未开启agent自保护数
        :type premium_non_sp_num: int
        """
        
        super(ShowHostsStatisticsResponse, self).__init__()

        self._total_num = None
        self._risk_num = None
        self._unprotected_num = None
        self._not_installed_num = None
        self._installed_failed_num = None
        self._not_online_num = None
        self._version_basic_num = None
        self._version_advanced_num = None
        self._version_enterprise_num = None
        self._version_premium_num = None
        self._version_wtp_num = None
        self._version_container_num = None
        self._host_group_num = None
        self._server_group_num = None
        self._asset_value_list = None
        self._server_group_list = None
        self._ignore_host_num = None
        self._protected_num = None
        self._protect_interrupt_num = None
        self._idle_num = None
        self._premium_non_sp_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if risk_num is not None:
            self.risk_num = risk_num
        if unprotected_num is not None:
            self.unprotected_num = unprotected_num
        if not_installed_num is not None:
            self.not_installed_num = not_installed_num
        if installed_failed_num is not None:
            self.installed_failed_num = installed_failed_num
        if not_online_num is not None:
            self.not_online_num = not_online_num
        if version_basic_num is not None:
            self.version_basic_num = version_basic_num
        if version_advanced_num is not None:
            self.version_advanced_num = version_advanced_num
        if version_enterprise_num is not None:
            self.version_enterprise_num = version_enterprise_num
        if version_premium_num is not None:
            self.version_premium_num = version_premium_num
        if version_wtp_num is not None:
            self.version_wtp_num = version_wtp_num
        if version_container_num is not None:
            self.version_container_num = version_container_num
        if host_group_num is not None:
            self.host_group_num = host_group_num
        if server_group_num is not None:
            self.server_group_num = server_group_num
        if asset_value_list is not None:
            self.asset_value_list = asset_value_list
        if server_group_list is not None:
            self.server_group_list = server_group_list
        if ignore_host_num is not None:
            self.ignore_host_num = ignore_host_num
        if protected_num is not None:
            self.protected_num = protected_num
        if protect_interrupt_num is not None:
            self.protect_interrupt_num = protect_interrupt_num
        if idle_num is not None:
            self.idle_num = idle_num
        if premium_non_sp_num is not None:
            self.premium_non_sp_num = premium_non_sp_num

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowHostsStatisticsResponse.

        服务器总数

        :return: The total_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowHostsStatisticsResponse.

        服务器总数

        :param total_num: The total_num of this ShowHostsStatisticsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ShowHostsStatisticsResponse.

        有风险服务器数

        :return: The risk_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ShowHostsStatisticsResponse.

        有风险服务器数

        :param risk_num: The risk_num of this ShowHostsStatisticsResponse.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def unprotected_num(self):
        r"""Gets the unprotected_num of this ShowHostsStatisticsResponse.

        未防护服务器数

        :return: The unprotected_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._unprotected_num

    @unprotected_num.setter
    def unprotected_num(self, unprotected_num):
        r"""Sets the unprotected_num of this ShowHostsStatisticsResponse.

        未防护服务器数

        :param unprotected_num: The unprotected_num of this ShowHostsStatisticsResponse.
        :type unprotected_num: int
        """
        self._unprotected_num = unprotected_num

    @property
    def not_installed_num(self):
        r"""Gets the not_installed_num of this ShowHostsStatisticsResponse.

        Agent未安装数

        :return: The not_installed_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._not_installed_num

    @not_installed_num.setter
    def not_installed_num(self, not_installed_num):
        r"""Sets the not_installed_num of this ShowHostsStatisticsResponse.

        Agent未安装数

        :param not_installed_num: The not_installed_num of this ShowHostsStatisticsResponse.
        :type not_installed_num: int
        """
        self._not_installed_num = not_installed_num

    @property
    def installed_failed_num(self):
        r"""Gets the installed_failed_num of this ShowHostsStatisticsResponse.

        Agent安装失败数

        :return: The installed_failed_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._installed_failed_num

    @installed_failed_num.setter
    def installed_failed_num(self, installed_failed_num):
        r"""Sets the installed_failed_num of this ShowHostsStatisticsResponse.

        Agent安装失败数

        :param installed_failed_num: The installed_failed_num of this ShowHostsStatisticsResponse.
        :type installed_failed_num: int
        """
        self._installed_failed_num = installed_failed_num

    @property
    def not_online_num(self):
        r"""Gets the not_online_num of this ShowHostsStatisticsResponse.

        Agent不在线数

        :return: The not_online_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._not_online_num

    @not_online_num.setter
    def not_online_num(self, not_online_num):
        r"""Sets the not_online_num of this ShowHostsStatisticsResponse.

        Agent不在线数

        :param not_online_num: The not_online_num of this ShowHostsStatisticsResponse.
        :type not_online_num: int
        """
        self._not_online_num = not_online_num

    @property
    def version_basic_num(self):
        r"""Gets the version_basic_num of this ShowHostsStatisticsResponse.

        开启基础版服务器数

        :return: The version_basic_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_basic_num

    @version_basic_num.setter
    def version_basic_num(self, version_basic_num):
        r"""Sets the version_basic_num of this ShowHostsStatisticsResponse.

        开启基础版服务器数

        :param version_basic_num: The version_basic_num of this ShowHostsStatisticsResponse.
        :type version_basic_num: int
        """
        self._version_basic_num = version_basic_num

    @property
    def version_advanced_num(self):
        r"""Gets the version_advanced_num of this ShowHostsStatisticsResponse.

        开启专业版服务器数

        :return: The version_advanced_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_advanced_num

    @version_advanced_num.setter
    def version_advanced_num(self, version_advanced_num):
        r"""Sets the version_advanced_num of this ShowHostsStatisticsResponse.

        开启专业版服务器数

        :param version_advanced_num: The version_advanced_num of this ShowHostsStatisticsResponse.
        :type version_advanced_num: int
        """
        self._version_advanced_num = version_advanced_num

    @property
    def version_enterprise_num(self):
        r"""Gets the version_enterprise_num of this ShowHostsStatisticsResponse.

        开启企业版服务器数

        :return: The version_enterprise_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_enterprise_num

    @version_enterprise_num.setter
    def version_enterprise_num(self, version_enterprise_num):
        r"""Sets the version_enterprise_num of this ShowHostsStatisticsResponse.

        开启企业版服务器数

        :param version_enterprise_num: The version_enterprise_num of this ShowHostsStatisticsResponse.
        :type version_enterprise_num: int
        """
        self._version_enterprise_num = version_enterprise_num

    @property
    def version_premium_num(self):
        r"""Gets the version_premium_num of this ShowHostsStatisticsResponse.

        开启旗舰版服务器数

        :return: The version_premium_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_premium_num

    @version_premium_num.setter
    def version_premium_num(self, version_premium_num):
        r"""Sets the version_premium_num of this ShowHostsStatisticsResponse.

        开启旗舰版服务器数

        :param version_premium_num: The version_premium_num of this ShowHostsStatisticsResponse.
        :type version_premium_num: int
        """
        self._version_premium_num = version_premium_num

    @property
    def version_wtp_num(self):
        r"""Gets the version_wtp_num of this ShowHostsStatisticsResponse.

        开启网页防篡改版服务器数

        :return: The version_wtp_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_wtp_num

    @version_wtp_num.setter
    def version_wtp_num(self, version_wtp_num):
        r"""Sets the version_wtp_num of this ShowHostsStatisticsResponse.

        开启网页防篡改版服务器数

        :param version_wtp_num: The version_wtp_num of this ShowHostsStatisticsResponse.
        :type version_wtp_num: int
        """
        self._version_wtp_num = version_wtp_num

    @property
    def version_container_num(self):
        r"""Gets the version_container_num of this ShowHostsStatisticsResponse.

        开启容器版服务器数

        :return: The version_container_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._version_container_num

    @version_container_num.setter
    def version_container_num(self, version_container_num):
        r"""Sets the version_container_num of this ShowHostsStatisticsResponse.

        开启容器版服务器数

        :param version_container_num: The version_container_num of this ShowHostsStatisticsResponse.
        :type version_container_num: int
        """
        self._version_container_num = version_container_num

    @property
    def host_group_num(self):
        r"""Gets the host_group_num of this ShowHostsStatisticsResponse.

        服务器组总数

        :return: The host_group_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._host_group_num

    @host_group_num.setter
    def host_group_num(self, host_group_num):
        r"""Sets the host_group_num of this ShowHostsStatisticsResponse.

        服务器组总数

        :param host_group_num: The host_group_num of this ShowHostsStatisticsResponse.
        :type host_group_num: int
        """
        self._host_group_num = host_group_num

    @property
    def server_group_num(self):
        r"""Gets the server_group_num of this ShowHostsStatisticsResponse.

        资产服务器组数量

        :return: The server_group_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._server_group_num

    @server_group_num.setter
    def server_group_num(self, server_group_num):
        r"""Sets the server_group_num of this ShowHostsStatisticsResponse.

        资产服务器组数量

        :param server_group_num: The server_group_num of this ShowHostsStatisticsResponse.
        :type server_group_num: int
        """
        self._server_group_num = server_group_num

    @property
    def asset_value_list(self):
        r"""Gets the asset_value_list of this ShowHostsStatisticsResponse.

        资产重要性列表

        :return: The asset_value_list of this ShowHostsStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AssetValueHostNumInfo`]
        """
        return self._asset_value_list

    @asset_value_list.setter
    def asset_value_list(self, asset_value_list):
        r"""Sets the asset_value_list of this ShowHostsStatisticsResponse.

        资产重要性列表

        :param asset_value_list: The asset_value_list of this ShowHostsStatisticsResponse.
        :type asset_value_list: list[:class:`huaweicloudsdkhss.v5.AssetValueHostNumInfo`]
        """
        self._asset_value_list = asset_value_list

    @property
    def server_group_list(self):
        r"""Gets the server_group_list of this ShowHostsStatisticsResponse.

        服务器组列表

        :return: The server_group_list of this ShowHostsStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ServerGroupItem`]
        """
        return self._server_group_list

    @server_group_list.setter
    def server_group_list(self, server_group_list):
        r"""Sets the server_group_list of this ShowHostsStatisticsResponse.

        服务器组列表

        :param server_group_list: The server_group_list of this ShowHostsStatisticsResponse.
        :type server_group_list: list[:class:`huaweicloudsdkhss.v5.ServerGroupItem`]
        """
        self._server_group_list = server_group_list

    @property
    def ignore_host_num(self):
        r"""Gets the ignore_host_num of this ShowHostsStatisticsResponse.

        已忽略服务器数

        :return: The ignore_host_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._ignore_host_num

    @ignore_host_num.setter
    def ignore_host_num(self, ignore_host_num):
        r"""Sets the ignore_host_num of this ShowHostsStatisticsResponse.

        已忽略服务器数

        :param ignore_host_num: The ignore_host_num of this ShowHostsStatisticsResponse.
        :type ignore_host_num: int
        """
        self._ignore_host_num = ignore_host_num

    @property
    def protected_num(self):
        r"""Gets the protected_num of this ShowHostsStatisticsResponse.

        防护中服务器数

        :return: The protected_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._protected_num

    @protected_num.setter
    def protected_num(self, protected_num):
        r"""Sets the protected_num of this ShowHostsStatisticsResponse.

        防护中服务器数

        :param protected_num: The protected_num of this ShowHostsStatisticsResponse.
        :type protected_num: int
        """
        self._protected_num = protected_num

    @property
    def protect_interrupt_num(self):
        r"""Gets the protect_interrupt_num of this ShowHostsStatisticsResponse.

        防护中断服务器数

        :return: The protect_interrupt_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._protect_interrupt_num

    @protect_interrupt_num.setter
    def protect_interrupt_num(self, protect_interrupt_num):
        r"""Sets the protect_interrupt_num of this ShowHostsStatisticsResponse.

        防护中断服务器数

        :param protect_interrupt_num: The protect_interrupt_num of this ShowHostsStatisticsResponse.
        :type protect_interrupt_num: int
        """
        self._protect_interrupt_num = protect_interrupt_num

    @property
    def idle_num(self):
        r"""Gets the idle_num of this ShowHostsStatisticsResponse.

        空闲配额数

        :return: The idle_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._idle_num

    @idle_num.setter
    def idle_num(self, idle_num):
        r"""Sets the idle_num of this ShowHostsStatisticsResponse.

        空闲配额数

        :param idle_num: The idle_num of this ShowHostsStatisticsResponse.
        :type idle_num: int
        """
        self._idle_num = idle_num

    @property
    def premium_non_sp_num(self):
        r"""Gets the premium_non_sp_num of this ShowHostsStatisticsResponse.

        旗舰版主机未开启agent自保护数

        :return: The premium_non_sp_num of this ShowHostsStatisticsResponse.
        :rtype: int
        """
        return self._premium_non_sp_num

    @premium_non_sp_num.setter
    def premium_non_sp_num(self, premium_non_sp_num):
        r"""Sets the premium_non_sp_num of this ShowHostsStatisticsResponse.

        旗舰版主机未开启agent自保护数

        :param premium_non_sp_num: The premium_non_sp_num of this ShowHostsStatisticsResponse.
        :type premium_non_sp_num: int
        """
        self._premium_non_sp_num = premium_non_sp_num

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
        if not isinstance(other, ShowHostsStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
