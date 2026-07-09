# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support_unibuy': 'bool',
        'is_support_float_ipv6': 'bool',
        'is_support_admin_login': 'bool',
        'is_support_update_ha': 'bool',
        'is_support_tms': 'bool',
        'is_support_eps': 'bool',
        'is_support_iam_login': 'bool',
        'is_support_ipv6': 'bool',
        'is_support_ha': 'bool',
        'is_support_reset': 'bool',
        'is_support_upgrade_instance': 'bool',
        'is_support_change_security_group': 'bool',
        'is_support_manually_ip': 'bool',
        'is_support_capacity_expantion': 'bool',
        'is_support_ha_expantion': 'bool',
        'is_support_agency_authorize': 'bool',
        'is_support_change_vpc': 'bool',
        'is_support_cluster': 'bool',
        'is_support_ondemand': 'bool',
        'is_support_period': 'bool'
    }

    attribute_map = {
        'is_support_unibuy': 'is_support_unibuy',
        'is_support_float_ipv6': 'is_support_float_ipv6',
        'is_support_admin_login': 'is_support_admin_login',
        'is_support_update_ha': 'is_support_update_ha',
        'is_support_tms': 'is_support_tms',
        'is_support_eps': 'is_support_eps',
        'is_support_iam_login': 'is_support_iam_login',
        'is_support_ipv6': 'is_support_ipv6',
        'is_support_ha': 'is_support_ha',
        'is_support_reset': 'is_support_reset',
        'is_support_upgrade_instance': 'is_support_upgrade_instance',
        'is_support_change_security_group': 'is_support_change_security_group',
        'is_support_manually_ip': 'is_support_manually_ip',
        'is_support_capacity_expantion': 'is_support_capacity_expantion',
        'is_support_ha_expantion': 'is_support_ha_expantion',
        'is_support_agency_authorize': 'is_support_agency_authorize',
        'is_support_change_vpc': 'is_support_change_vpc',
        'is_support_cluster': 'is_support_cluster',
        'is_support_ondemand': 'is_support_ondemand',
        'is_support_period': 'is_support_period'
    }

    def __init__(self, is_support_unibuy=None, is_support_float_ipv6=None, is_support_admin_login=None, is_support_update_ha=None, is_support_tms=None, is_support_eps=None, is_support_iam_login=None, is_support_ipv6=None, is_support_ha=None, is_support_reset=None, is_support_upgrade_instance=None, is_support_change_security_group=None, is_support_manually_ip=None, is_support_capacity_expantion=None, is_support_ha_expantion=None, is_support_agency_authorize=None, is_support_change_vpc=None, is_support_cluster=None, is_support_ondemand=None, is_support_period=None):
        r"""SwitchInfo

        The model defined in huaweicloud sdk

        :param is_support_unibuy: 是否支持unibuy。 - true：是 - false：否
        :type is_support_unibuy: bool
        :param is_support_float_ipv6: 是否支持浮动IPv6。 - true：是 - false：否
        :type is_support_float_ipv6: bool
        :param is_support_admin_login: 是否支持管理员登录。 - true：是 - false：否
        :type is_support_admin_login: bool
        :param is_support_update_ha: 是否支持更新HA。 - true：是 - false：否
        :type is_support_update_ha: bool
        :param is_support_tms: 是否支持TMS。 - true：是 - false：否
        :type is_support_tms: bool
        :param is_support_eps: 是否支持EPS。 - true：是 - false：否
        :type is_support_eps: bool
        :param is_support_iam_login: 是否支持IAM登录。 - true：是 - false：否
        :type is_support_iam_login: bool
        :param is_support_ipv6: 是否支持IPv6。 - true：是 - false：否
        :type is_support_ipv6: bool
        :param is_support_ha: 是否支持HA。 - true：是 - false：否
        :type is_support_ha: bool
        :param is_support_reset: 是否支持重置。 - true：是 - false：否
        :type is_support_reset: bool
        :param is_support_upgrade_instance: 是否支持升级实例。 - true：是 - false：否
        :type is_support_upgrade_instance: bool
        :param is_support_change_security_group: 是否支持更改安全组。 - true：是 - false：否
        :type is_support_change_security_group: bool
        :param is_support_manually_ip: 是否支持手动IP。 - true：是 - false：否
        :type is_support_manually_ip: bool
        :param is_support_capacity_expantion: 是否支持容量扩展。 - true：是 - false：否
        :type is_support_capacity_expantion: bool
        :param is_support_ha_expantion: 是否支持HA扩展。 - true：是 - false：否
        :type is_support_ha_expantion: bool
        :param is_support_agency_authorize: 是否支持代理授权。 - true：是 - false：否
        :type is_support_agency_authorize: bool
        :param is_support_change_vpc: 是否支持更改VPC。 - true：是 - false：否
        :type is_support_change_vpc: bool
        :param is_support_cluster: 是否支持集群。 - true：是 - false：否
        :type is_support_cluster: bool
        :param is_support_ondemand: 是否支持按需。 - true：是 - false：否
        :type is_support_ondemand: bool
        :param is_support_period: 是否支持周期。 - true：是 - false：否
        :type is_support_period: bool
        """
        
        

        self._is_support_unibuy = None
        self._is_support_float_ipv6 = None
        self._is_support_admin_login = None
        self._is_support_update_ha = None
        self._is_support_tms = None
        self._is_support_eps = None
        self._is_support_iam_login = None
        self._is_support_ipv6 = None
        self._is_support_ha = None
        self._is_support_reset = None
        self._is_support_upgrade_instance = None
        self._is_support_change_security_group = None
        self._is_support_manually_ip = None
        self._is_support_capacity_expantion = None
        self._is_support_ha_expantion = None
        self._is_support_agency_authorize = None
        self._is_support_change_vpc = None
        self._is_support_cluster = None
        self._is_support_ondemand = None
        self._is_support_period = None
        self.discriminator = None

        if is_support_unibuy is not None:
            self.is_support_unibuy = is_support_unibuy
        if is_support_float_ipv6 is not None:
            self.is_support_float_ipv6 = is_support_float_ipv6
        if is_support_admin_login is not None:
            self.is_support_admin_login = is_support_admin_login
        if is_support_update_ha is not None:
            self.is_support_update_ha = is_support_update_ha
        if is_support_tms is not None:
            self.is_support_tms = is_support_tms
        if is_support_eps is not None:
            self.is_support_eps = is_support_eps
        if is_support_iam_login is not None:
            self.is_support_iam_login = is_support_iam_login
        if is_support_ipv6 is not None:
            self.is_support_ipv6 = is_support_ipv6
        if is_support_ha is not None:
            self.is_support_ha = is_support_ha
        if is_support_reset is not None:
            self.is_support_reset = is_support_reset
        if is_support_upgrade_instance is not None:
            self.is_support_upgrade_instance = is_support_upgrade_instance
        if is_support_change_security_group is not None:
            self.is_support_change_security_group = is_support_change_security_group
        if is_support_manually_ip is not None:
            self.is_support_manually_ip = is_support_manually_ip
        if is_support_capacity_expantion is not None:
            self.is_support_capacity_expantion = is_support_capacity_expantion
        if is_support_ha_expantion is not None:
            self.is_support_ha_expantion = is_support_ha_expantion
        if is_support_agency_authorize is not None:
            self.is_support_agency_authorize = is_support_agency_authorize
        if is_support_change_vpc is not None:
            self.is_support_change_vpc = is_support_change_vpc
        if is_support_cluster is not None:
            self.is_support_cluster = is_support_cluster
        if is_support_ondemand is not None:
            self.is_support_ondemand = is_support_ondemand
        if is_support_period is not None:
            self.is_support_period = is_support_period

    @property
    def is_support_unibuy(self):
        r"""Gets the is_support_unibuy of this SwitchInfo.

        是否支持unibuy。 - true：是 - false：否

        :return: The is_support_unibuy of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_unibuy

    @is_support_unibuy.setter
    def is_support_unibuy(self, is_support_unibuy):
        r"""Sets the is_support_unibuy of this SwitchInfo.

        是否支持unibuy。 - true：是 - false：否

        :param is_support_unibuy: The is_support_unibuy of this SwitchInfo.
        :type is_support_unibuy: bool
        """
        self._is_support_unibuy = is_support_unibuy

    @property
    def is_support_float_ipv6(self):
        r"""Gets the is_support_float_ipv6 of this SwitchInfo.

        是否支持浮动IPv6。 - true：是 - false：否

        :return: The is_support_float_ipv6 of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_float_ipv6

    @is_support_float_ipv6.setter
    def is_support_float_ipv6(self, is_support_float_ipv6):
        r"""Sets the is_support_float_ipv6 of this SwitchInfo.

        是否支持浮动IPv6。 - true：是 - false：否

        :param is_support_float_ipv6: The is_support_float_ipv6 of this SwitchInfo.
        :type is_support_float_ipv6: bool
        """
        self._is_support_float_ipv6 = is_support_float_ipv6

    @property
    def is_support_admin_login(self):
        r"""Gets the is_support_admin_login of this SwitchInfo.

        是否支持管理员登录。 - true：是 - false：否

        :return: The is_support_admin_login of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_admin_login

    @is_support_admin_login.setter
    def is_support_admin_login(self, is_support_admin_login):
        r"""Sets the is_support_admin_login of this SwitchInfo.

        是否支持管理员登录。 - true：是 - false：否

        :param is_support_admin_login: The is_support_admin_login of this SwitchInfo.
        :type is_support_admin_login: bool
        """
        self._is_support_admin_login = is_support_admin_login

    @property
    def is_support_update_ha(self):
        r"""Gets the is_support_update_ha of this SwitchInfo.

        是否支持更新HA。 - true：是 - false：否

        :return: The is_support_update_ha of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_update_ha

    @is_support_update_ha.setter
    def is_support_update_ha(self, is_support_update_ha):
        r"""Sets the is_support_update_ha of this SwitchInfo.

        是否支持更新HA。 - true：是 - false：否

        :param is_support_update_ha: The is_support_update_ha of this SwitchInfo.
        :type is_support_update_ha: bool
        """
        self._is_support_update_ha = is_support_update_ha

    @property
    def is_support_tms(self):
        r"""Gets the is_support_tms of this SwitchInfo.

        是否支持TMS。 - true：是 - false：否

        :return: The is_support_tms of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_tms

    @is_support_tms.setter
    def is_support_tms(self, is_support_tms):
        r"""Sets the is_support_tms of this SwitchInfo.

        是否支持TMS。 - true：是 - false：否

        :param is_support_tms: The is_support_tms of this SwitchInfo.
        :type is_support_tms: bool
        """
        self._is_support_tms = is_support_tms

    @property
    def is_support_eps(self):
        r"""Gets the is_support_eps of this SwitchInfo.

        是否支持EPS。 - true：是 - false：否

        :return: The is_support_eps of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_eps

    @is_support_eps.setter
    def is_support_eps(self, is_support_eps):
        r"""Sets the is_support_eps of this SwitchInfo.

        是否支持EPS。 - true：是 - false：否

        :param is_support_eps: The is_support_eps of this SwitchInfo.
        :type is_support_eps: bool
        """
        self._is_support_eps = is_support_eps

    @property
    def is_support_iam_login(self):
        r"""Gets the is_support_iam_login of this SwitchInfo.

        是否支持IAM登录。 - true：是 - false：否

        :return: The is_support_iam_login of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_iam_login

    @is_support_iam_login.setter
    def is_support_iam_login(self, is_support_iam_login):
        r"""Sets the is_support_iam_login of this SwitchInfo.

        是否支持IAM登录。 - true：是 - false：否

        :param is_support_iam_login: The is_support_iam_login of this SwitchInfo.
        :type is_support_iam_login: bool
        """
        self._is_support_iam_login = is_support_iam_login

    @property
    def is_support_ipv6(self):
        r"""Gets the is_support_ipv6 of this SwitchInfo.

        是否支持IPv6。 - true：是 - false：否

        :return: The is_support_ipv6 of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_ipv6

    @is_support_ipv6.setter
    def is_support_ipv6(self, is_support_ipv6):
        r"""Sets the is_support_ipv6 of this SwitchInfo.

        是否支持IPv6。 - true：是 - false：否

        :param is_support_ipv6: The is_support_ipv6 of this SwitchInfo.
        :type is_support_ipv6: bool
        """
        self._is_support_ipv6 = is_support_ipv6

    @property
    def is_support_ha(self):
        r"""Gets the is_support_ha of this SwitchInfo.

        是否支持HA。 - true：是 - false：否

        :return: The is_support_ha of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_ha

    @is_support_ha.setter
    def is_support_ha(self, is_support_ha):
        r"""Sets the is_support_ha of this SwitchInfo.

        是否支持HA。 - true：是 - false：否

        :param is_support_ha: The is_support_ha of this SwitchInfo.
        :type is_support_ha: bool
        """
        self._is_support_ha = is_support_ha

    @property
    def is_support_reset(self):
        r"""Gets the is_support_reset of this SwitchInfo.

        是否支持重置。 - true：是 - false：否

        :return: The is_support_reset of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_reset

    @is_support_reset.setter
    def is_support_reset(self, is_support_reset):
        r"""Sets the is_support_reset of this SwitchInfo.

        是否支持重置。 - true：是 - false：否

        :param is_support_reset: The is_support_reset of this SwitchInfo.
        :type is_support_reset: bool
        """
        self._is_support_reset = is_support_reset

    @property
    def is_support_upgrade_instance(self):
        r"""Gets the is_support_upgrade_instance of this SwitchInfo.

        是否支持升级实例。 - true：是 - false：否

        :return: The is_support_upgrade_instance of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_upgrade_instance

    @is_support_upgrade_instance.setter
    def is_support_upgrade_instance(self, is_support_upgrade_instance):
        r"""Sets the is_support_upgrade_instance of this SwitchInfo.

        是否支持升级实例。 - true：是 - false：否

        :param is_support_upgrade_instance: The is_support_upgrade_instance of this SwitchInfo.
        :type is_support_upgrade_instance: bool
        """
        self._is_support_upgrade_instance = is_support_upgrade_instance

    @property
    def is_support_change_security_group(self):
        r"""Gets the is_support_change_security_group of this SwitchInfo.

        是否支持更改安全组。 - true：是 - false：否

        :return: The is_support_change_security_group of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_change_security_group

    @is_support_change_security_group.setter
    def is_support_change_security_group(self, is_support_change_security_group):
        r"""Sets the is_support_change_security_group of this SwitchInfo.

        是否支持更改安全组。 - true：是 - false：否

        :param is_support_change_security_group: The is_support_change_security_group of this SwitchInfo.
        :type is_support_change_security_group: bool
        """
        self._is_support_change_security_group = is_support_change_security_group

    @property
    def is_support_manually_ip(self):
        r"""Gets the is_support_manually_ip of this SwitchInfo.

        是否支持手动IP。 - true：是 - false：否

        :return: The is_support_manually_ip of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_manually_ip

    @is_support_manually_ip.setter
    def is_support_manually_ip(self, is_support_manually_ip):
        r"""Sets the is_support_manually_ip of this SwitchInfo.

        是否支持手动IP。 - true：是 - false：否

        :param is_support_manually_ip: The is_support_manually_ip of this SwitchInfo.
        :type is_support_manually_ip: bool
        """
        self._is_support_manually_ip = is_support_manually_ip

    @property
    def is_support_capacity_expantion(self):
        r"""Gets the is_support_capacity_expantion of this SwitchInfo.

        是否支持容量扩展。 - true：是 - false：否

        :return: The is_support_capacity_expantion of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_capacity_expantion

    @is_support_capacity_expantion.setter
    def is_support_capacity_expantion(self, is_support_capacity_expantion):
        r"""Sets the is_support_capacity_expantion of this SwitchInfo.

        是否支持容量扩展。 - true：是 - false：否

        :param is_support_capacity_expantion: The is_support_capacity_expantion of this SwitchInfo.
        :type is_support_capacity_expantion: bool
        """
        self._is_support_capacity_expantion = is_support_capacity_expantion

    @property
    def is_support_ha_expantion(self):
        r"""Gets the is_support_ha_expantion of this SwitchInfo.

        是否支持HA扩展。 - true：是 - false：否

        :return: The is_support_ha_expantion of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_ha_expantion

    @is_support_ha_expantion.setter
    def is_support_ha_expantion(self, is_support_ha_expantion):
        r"""Sets the is_support_ha_expantion of this SwitchInfo.

        是否支持HA扩展。 - true：是 - false：否

        :param is_support_ha_expantion: The is_support_ha_expantion of this SwitchInfo.
        :type is_support_ha_expantion: bool
        """
        self._is_support_ha_expantion = is_support_ha_expantion

    @property
    def is_support_agency_authorize(self):
        r"""Gets the is_support_agency_authorize of this SwitchInfo.

        是否支持代理授权。 - true：是 - false：否

        :return: The is_support_agency_authorize of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_agency_authorize

    @is_support_agency_authorize.setter
    def is_support_agency_authorize(self, is_support_agency_authorize):
        r"""Sets the is_support_agency_authorize of this SwitchInfo.

        是否支持代理授权。 - true：是 - false：否

        :param is_support_agency_authorize: The is_support_agency_authorize of this SwitchInfo.
        :type is_support_agency_authorize: bool
        """
        self._is_support_agency_authorize = is_support_agency_authorize

    @property
    def is_support_change_vpc(self):
        r"""Gets the is_support_change_vpc of this SwitchInfo.

        是否支持更改VPC。 - true：是 - false：否

        :return: The is_support_change_vpc of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_change_vpc

    @is_support_change_vpc.setter
    def is_support_change_vpc(self, is_support_change_vpc):
        r"""Sets the is_support_change_vpc of this SwitchInfo.

        是否支持更改VPC。 - true：是 - false：否

        :param is_support_change_vpc: The is_support_change_vpc of this SwitchInfo.
        :type is_support_change_vpc: bool
        """
        self._is_support_change_vpc = is_support_change_vpc

    @property
    def is_support_cluster(self):
        r"""Gets the is_support_cluster of this SwitchInfo.

        是否支持集群。 - true：是 - false：否

        :return: The is_support_cluster of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_cluster

    @is_support_cluster.setter
    def is_support_cluster(self, is_support_cluster):
        r"""Sets the is_support_cluster of this SwitchInfo.

        是否支持集群。 - true：是 - false：否

        :param is_support_cluster: The is_support_cluster of this SwitchInfo.
        :type is_support_cluster: bool
        """
        self._is_support_cluster = is_support_cluster

    @property
    def is_support_ondemand(self):
        r"""Gets the is_support_ondemand of this SwitchInfo.

        是否支持按需。 - true：是 - false：否

        :return: The is_support_ondemand of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_ondemand

    @is_support_ondemand.setter
    def is_support_ondemand(self, is_support_ondemand):
        r"""Sets the is_support_ondemand of this SwitchInfo.

        是否支持按需。 - true：是 - false：否

        :param is_support_ondemand: The is_support_ondemand of this SwitchInfo.
        :type is_support_ondemand: bool
        """
        self._is_support_ondemand = is_support_ondemand

    @property
    def is_support_period(self):
        r"""Gets the is_support_period of this SwitchInfo.

        是否支持周期。 - true：是 - false：否

        :return: The is_support_period of this SwitchInfo.
        :rtype: bool
        """
        return self._is_support_period

    @is_support_period.setter
    def is_support_period(self, is_support_period):
        r"""Sets the is_support_period of this SwitchInfo.

        是否支持周期。 - true：是 - false：否

        :param is_support_period: The is_support_period of this SwitchInfo.
        :type is_support_period: bool
        """
        self._is_support_period = is_support_period

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
        if not isinstance(other, SwitchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
