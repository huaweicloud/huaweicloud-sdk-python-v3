# coding: utf-8

import re
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
        'ad_domains': 'AdDomain',
        'enterprise_id': 'str',
        'vpc_id': 'str',
        'subnet_ids': 'list[Subnet]',
        'manage_subnet_cidr': 'str',
        'access_mode': 'str',
        'dedicated_subnets': 'str'
    }

    attribute_map = {
        'ad_domains': 'ad_domains',
        'enterprise_id': 'enterprise_id',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'manage_subnet_cidr': 'manage_subnet_cidr',
        'access_mode': 'access_mode',
        'dedicated_subnets': 'dedicated_subnets'
    }

    def __init__(self, ad_domains=None, enterprise_id=None, vpc_id=None, subnet_ids=None, manage_subnet_cidr=None, access_mode=None, dedicated_subnets=None):
        """ApplyWorkspaceReq

        The model defined in huaweicloud sdk

        :param ad_domains: 
        :type ad_domains: :class:`huaweicloudsdkworkspace.v2.AdDomain`
        :param enterprise_id: 企业ID。  企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。
        :type enterprise_id: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param subnet_ids: 指定业务子网的网络ID，子网不能与172.16.0.0/12冲突。
        :type subnet_ids: list[:class:`huaweicloudsdkworkspace.v2.Subnet`]
        :param manage_subnet_cidr: 管理子网网段。 注：不能与172.16.0.0/12以及subnet_ids参数下子网的网段冲突。
        :type manage_subnet_cidr: str
        :param access_mode: 接入方式。 - INTERNET：表示Internet接入。 - DEDICATED：表示专线接入。 - BOTH：表示两种接入方式都支持。
        :type access_mode: str
        :param dedicated_subnets: 专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。
        :type dedicated_subnets: str
        """
        
        

        self._ad_domains = None
        self._enterprise_id = None
        self._vpc_id = None
        self._subnet_ids = None
        self._manage_subnet_cidr = None
        self._access_mode = None
        self._dedicated_subnets = None
        self.discriminator = None

        self.ad_domains = ad_domains
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        self.vpc_id = vpc_id
        self.subnet_ids = subnet_ids
        if manage_subnet_cidr is not None:
            self.manage_subnet_cidr = manage_subnet_cidr
        self.access_mode = access_mode
        if dedicated_subnets is not None:
            self.dedicated_subnets = dedicated_subnets

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
    def enterprise_id(self):
        """Gets the enterprise_id of this ApplyWorkspaceReq.

        企业ID。  企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。

        :return: The enterprise_id of this ApplyWorkspaceReq.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this ApplyWorkspaceReq.

        企业ID。  企业ID是您在云桌面服务的唯一标识，终端用户登录时需要填写企业ID，若不自定义设置企业ID，系统将自动生成您的企业ID。格式为由半角数字、字母、_-组成，长度范围小于等于32个字符。

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
