# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyWorkspaceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'ad_domains': 'AdDomain',
        'third_gateway_info': 'ThirdGatewayConfigInfo',
        'enterprise_id': 'str',
        'vpc_id': 'str',
        'subnet_ids': 'list[Subnet]',
        'manage_subnet_cidr': 'str',
        'access_mode': 'str',
        'apply_shared_vpc_dedicated_param': 'ApplySharedVpcDedicatedParam',
        'dedicated_subnets': 'str',
        'availability_zone': 'str',
        'publicip_type': 'str',
        'assist_auth_config': 'AssistAuthMethodConfigRequest',
        'site_configs': 'list[SiteConfigsRequest]',
        'is_send_email': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'ad_domains': 'ad_domains',
        'third_gateway_info': 'third_gateway_info',
        'enterprise_id': 'enterprise_id',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'manage_subnet_cidr': 'manage_subnet_cidr',
        'access_mode': 'access_mode',
        'apply_shared_vpc_dedicated_param': 'apply_shared_vpc_dedicated_param',
        'dedicated_subnets': 'dedicated_subnets',
        'availability_zone': 'availability_zone',
        'publicip_type': 'publicip_type',
        'assist_auth_config': 'assist_auth_config',
        'site_configs': 'site_configs',
        'is_send_email': 'is_send_email',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, auth_type=None, ad_domains=None, third_gateway_info=None, enterprise_id=None, vpc_id=None, subnet_ids=None, manage_subnet_cidr=None, access_mode=None, apply_shared_vpc_dedicated_param=None, dedicated_subnets=None, availability_zone=None, publicip_type=None, assist_auth_config=None, site_configs=None, is_send_email=None, enterprise_project_id=None):
        """ApplyWorkspaceReq

        The model defined in huaweicloud sdk

        :param auth_type: 主认证方式。 - KERBEROS：KERBEROS。 - KERBEROS_THIRD_SSO：第三方登录认证。
        :type auth_type: str
        :param ad_domains: 
        :type ad_domains: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        :param third_gateway_info: 
        :type third_gateway_info: :class:`huaweicloudsdkworkspace.v2.ThirdGatewayConfigInfo`
        :param enterprise_id: 企业ID。 企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。
        :type enterprise_id: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param subnet_ids: 指定业务子网的网络ID，子网不能与172.16.0.0/12冲突。
        :type subnet_ids: list[:class:`huaweicloudsdkworkspace.v2.Subnet`]
        :param manage_subnet_cidr: 管理子网网段。 注：不能与172.16.0.0/12以及subnet_ids参数下子网的网段冲突。
        :type manage_subnet_cidr: str
        :param access_mode: 接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。
        :type access_mode: str
        :param apply_shared_vpc_dedicated_param: 
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        :param dedicated_subnets: 专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。
        :type dedicated_subnets: str
        :param availability_zone: 开通服务资源使用的可用分区。
        :type availability_zone: str
        :param publicip_type: 外部网络。
        :type publicip_type: str
        :param assist_auth_config: 
        :type assist_auth_config: :class:`huaweicloudsdkworkspace.v2.AssistAuthMethodConfigRequest`
        :param site_configs: 边缘开户信息
        :type site_configs: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        :param is_send_email: 桌面退订是否发送邮件通知。
        :type is_send_email: bool
        :param enterprise_project_id: 企业项目ID，默认\&quot;0\&quot;
        :type enterprise_project_id: str
        """
        
        

        self._auth_type = None
        self._ad_domains = None
        self._third_gateway_info = None
        self._enterprise_id = None
        self._vpc_id = None
        self._subnet_ids = None
        self._manage_subnet_cidr = None
        self._access_mode = None
        self._apply_shared_vpc_dedicated_param = None
        self._dedicated_subnets = None
        self._availability_zone = None
        self._publicip_type = None
        self._assist_auth_config = None
        self._site_configs = None
        self._is_send_email = None
        self._enterprise_project_id = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        self.ad_domains = ad_domains
        if third_gateway_info is not None:
            self.third_gateway_info = third_gateway_info
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if manage_subnet_cidr is not None:
            self.manage_subnet_cidr = manage_subnet_cidr
        if access_mode is not None:
            self.access_mode = access_mode
        if apply_shared_vpc_dedicated_param is not None:
            self.apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param
        if dedicated_subnets is not None:
            self.dedicated_subnets = dedicated_subnets
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if publicip_type is not None:
            self.publicip_type = publicip_type
        if assist_auth_config is not None:
            self.assist_auth_config = assist_auth_config
        if site_configs is not None:
            self.site_configs = site_configs
        if is_send_email is not None:
            self.is_send_email = is_send_email
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def auth_type(self):
        """Gets the auth_type of this ApplyWorkspaceReq.

        主认证方式。 - KERBEROS：KERBEROS。 - KERBEROS_THIRD_SSO：第三方登录认证。

        :return: The auth_type of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ApplyWorkspaceReq.

        主认证方式。 - KERBEROS：KERBEROS。 - KERBEROS_THIRD_SSO：第三方登录认证。

        :param auth_type: The auth_type of this ApplyWorkspaceReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def ad_domains(self):
        """Gets the ad_domains of this ApplyWorkspaceReq.

        :return: The ad_domains of this ApplyWorkspaceReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        """
        return self._ad_domains

    @ad_domains.setter
    def ad_domains(self, ad_domains):
        """Sets the ad_domains of this ApplyWorkspaceReq.

        :param ad_domains: The ad_domains of this ApplyWorkspaceReq.
        :type ad_domains: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        """
        self._ad_domains = ad_domains

    @property
    def third_gateway_info(self):
        """Gets the third_gateway_info of this ApplyWorkspaceReq.

        :return: The third_gateway_info of this ApplyWorkspaceReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ThirdGatewayConfigInfo`
        """
        return self._third_gateway_info

    @third_gateway_info.setter
    def third_gateway_info(self, third_gateway_info):
        """Sets the third_gateway_info of this ApplyWorkspaceReq.

        :param third_gateway_info: The third_gateway_info of this ApplyWorkspaceReq.
        :type third_gateway_info: :class:`huaweicloudsdkworkspace.v2.ThirdGatewayConfigInfo`
        """
        self._third_gateway_info = third_gateway_info

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this ApplyWorkspaceReq.

        企业ID。 企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。

        :return: The enterprise_id of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this ApplyWorkspaceReq.

        企业ID。 企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。

        :param enterprise_id: The enterprise_id of this ApplyWorkspaceReq.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ApplyWorkspaceReq.

        VPC ID。

        :return: The vpc_id of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ApplyWorkspaceReq.

        VPC ID。

        :param vpc_id: The vpc_id of this ApplyWorkspaceReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this ApplyWorkspaceReq.

        指定业务子网的网络ID，子网不能与172.16.0.0/12冲突。

        :return: The subnet_ids of this ApplyWorkspaceReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Subnet`]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this ApplyWorkspaceReq.

        指定业务子网的网络ID，子网不能与172.16.0.0/12冲突。

        :param subnet_ids: The subnet_ids of this ApplyWorkspaceReq.
        :type subnet_ids: list[:class:`huaweicloudsdkworkspace.v2.Subnet`]
        """
        self._subnet_ids = subnet_ids

    @property
    def manage_subnet_cidr(self):
        """Gets the manage_subnet_cidr of this ApplyWorkspaceReq.

        管理子网网段。 注：不能与172.16.0.0/12以及subnet_ids参数下子网的网段冲突。

        :return: The manage_subnet_cidr of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._manage_subnet_cidr

    @manage_subnet_cidr.setter
    def manage_subnet_cidr(self, manage_subnet_cidr):
        """Sets the manage_subnet_cidr of this ApplyWorkspaceReq.

        管理子网网段。 注：不能与172.16.0.0/12以及subnet_ids参数下子网的网段冲突。

        :param manage_subnet_cidr: The manage_subnet_cidr of this ApplyWorkspaceReq.
        :type manage_subnet_cidr: str
        """
        self._manage_subnet_cidr = manage_subnet_cidr

    @property
    def access_mode(self):
        """Gets the access_mode of this ApplyWorkspaceReq.

        接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。

        :return: The access_mode of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this ApplyWorkspaceReq.

        接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。

        :param access_mode: The access_mode of this ApplyWorkspaceReq.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def apply_shared_vpc_dedicated_param(self):
        """Gets the apply_shared_vpc_dedicated_param of this ApplyWorkspaceReq.

        :return: The apply_shared_vpc_dedicated_param of this ApplyWorkspaceReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        return self._apply_shared_vpc_dedicated_param

    @apply_shared_vpc_dedicated_param.setter
    def apply_shared_vpc_dedicated_param(self, apply_shared_vpc_dedicated_param):
        """Sets the apply_shared_vpc_dedicated_param of this ApplyWorkspaceReq.

        :param apply_shared_vpc_dedicated_param: The apply_shared_vpc_dedicated_param of this ApplyWorkspaceReq.
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        self._apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param

    @property
    def dedicated_subnets(self):
        """Gets the dedicated_subnets of this ApplyWorkspaceReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。

        :return: The dedicated_subnets of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._dedicated_subnets

    @dedicated_subnets.setter
    def dedicated_subnets(self, dedicated_subnets):
        """Sets the dedicated_subnets of this ApplyWorkspaceReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。

        :param dedicated_subnets: The dedicated_subnets of this ApplyWorkspaceReq.
        :type dedicated_subnets: str
        """
        self._dedicated_subnets = dedicated_subnets

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ApplyWorkspaceReq.

        开通服务资源使用的可用分区。

        :return: The availability_zone of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ApplyWorkspaceReq.

        开通服务资源使用的可用分区。

        :param availability_zone: The availability_zone of this ApplyWorkspaceReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def publicip_type(self):
        """Gets the publicip_type of this ApplyWorkspaceReq.

        外部网络。

        :return: The publicip_type of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        """Sets the publicip_type of this ApplyWorkspaceReq.

        外部网络。

        :param publicip_type: The publicip_type of this ApplyWorkspaceReq.
        :type publicip_type: str
        """
        self._publicip_type = publicip_type

    @property
    def assist_auth_config(self):
        """Gets the assist_auth_config of this ApplyWorkspaceReq.

        :return: The assist_auth_config of this ApplyWorkspaceReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AssistAuthMethodConfigRequest`
        """
        return self._assist_auth_config

    @assist_auth_config.setter
    def assist_auth_config(self, assist_auth_config):
        """Sets the assist_auth_config of this ApplyWorkspaceReq.

        :param assist_auth_config: The assist_auth_config of this ApplyWorkspaceReq.
        :type assist_auth_config: :class:`huaweicloudsdkworkspace.v2.AssistAuthMethodConfigRequest`
        """
        self._assist_auth_config = assist_auth_config

    @property
    def site_configs(self):
        """Gets the site_configs of this ApplyWorkspaceReq.

        边缘开户信息

        :return: The site_configs of this ApplyWorkspaceReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        """
        return self._site_configs

    @site_configs.setter
    def site_configs(self, site_configs):
        """Sets the site_configs of this ApplyWorkspaceReq.

        边缘开户信息

        :param site_configs: The site_configs of this ApplyWorkspaceReq.
        :type site_configs: list[:class:`huaweicloudsdkworkspace.v2.SiteConfigsRequest`]
        """
        self._site_configs = site_configs

    @property
    def is_send_email(self):
        """Gets the is_send_email of this ApplyWorkspaceReq.

        桌面退订是否发送邮件通知。

        :return: The is_send_email of this ApplyWorkspaceReq.
        :rtype: bool
        """
        return self._is_send_email

    @is_send_email.setter
    def is_send_email(self, is_send_email):
        """Sets the is_send_email of this ApplyWorkspaceReq.

        桌面退订是否发送邮件通知。

        :param is_send_email: The is_send_email of this ApplyWorkspaceReq.
        :type is_send_email: bool
        """
        self._is_send_email = is_send_email

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ApplyWorkspaceReq.

        企业项目ID，默认\"0\"

        :return: The enterprise_project_id of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ApplyWorkspaceReq.

        企业项目ID，默认\"0\"

        :param enterprise_project_id: The enterprise_project_id of this ApplyWorkspaceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ApplyWorkspaceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
