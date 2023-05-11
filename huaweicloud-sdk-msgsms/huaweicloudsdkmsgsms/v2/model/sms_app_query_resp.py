# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsAppQueryResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'customer_id': 'str',
        'resource_id': 'str',
        'developer_account': 'str',
        'app_name': 'str',
        'omp_app_name': 'str',
        'app_key': 'str',
        'up_link_addr': 'str',
        'status': 'str',
        'industry': 'int',
        'region': 'str',
        'intl_channel_num': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'ip_white_list': 'str',
        'app_access_addr': 'str',
        'protocol': 'str',
        'platform': 'str',
        'is_support_multiomp': 'bool',
        'tenant': 'TenantBasic'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'customer_id': 'customer_id',
        'resource_id': 'resource_id',
        'developer_account': 'developer_account',
        'app_name': 'app_name',
        'omp_app_name': 'omp_app_name',
        'app_key': 'app_key',
        'up_link_addr': 'up_link_addr',
        'status': 'status',
        'industry': 'industry',
        'region': 'region',
        'intl_channel_num': 'intl_channel_num',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'ip_white_list': 'ip_white_list',
        'app_access_addr': 'app_access_addr',
        'protocol': 'protocol',
        'platform': 'platform',
        'is_support_multiomp': 'is_support_multiomp',
        'tenant': 'tenant'
    }

    def __init__(self, id=None, create_time=None, update_time=None, customer_id=None, resource_id=None, developer_account=None, app_name=None, omp_app_name=None, app_key=None, up_link_addr=None, status=None, industry=None, region=None, intl_channel_num=None, enterprise_project_id=None, enterprise_project_name=None, ip_white_list=None, app_access_addr=None, protocol=None, platform=None, is_support_multiomp=None, tenant=None):
        """SmsAppQueryResp

        The model defined in huaweicloud sdk

        :param id: 应用主键ID，用于获取、修改应用的唯一标识
        :type id: str
        :param create_time: 创建时间[yyyy-MM-dd HH:mm:ss]
        :type create_time: str
        :param update_time: 更新时间[yyyy-MM-dd HH:mm:ss]
        :type update_time: str
        :param customer_id: 租户customer id
        :type customer_id: str
        :param resource_id: 租户resource id
        :type resource_id: str
        :param developer_account: 租户开发者账号
        :type developer_account: str
        :param app_name: 应用名称
        :type app_name: str
        :param omp_app_name: omp应用名称
        :type omp_app_name: str
        :param app_key: 应用key
        :type app_key: str
        :param up_link_addr: 上行短信地址
        :type up_link_addr: str
        :param status: 应用状态   CREATED：待上线。应用暂未创建成功，请稍候。   SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   LAUNCHED：正常。应用添加成功，可以正常使用。
        :type status: str
        :param industry: 行业类型
        :type industry: int
        :param region: 地域 1. cn：国内 2. intl：国际
        :type region: str
        :param intl_channel_num: 国际/港澳台短信通道号
        :type intl_channel_num: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param ip_white_list: IP白名单
        :type ip_white_list: str
        :param app_access_addr: 接入地址
        :type app_access_addr: str
        :param protocol: 协议
        :type protocol: str
        :param platform: 平台
        :type platform: str
        :param is_support_multiomp: 是否支持多OMP
        :type is_support_multiomp: bool
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        
        

        self._id = None
        self._create_time = None
        self._update_time = None
        self._customer_id = None
        self._resource_id = None
        self._developer_account = None
        self._app_name = None
        self._omp_app_name = None
        self._app_key = None
        self._up_link_addr = None
        self._status = None
        self._industry = None
        self._region = None
        self._intl_channel_num = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._ip_white_list = None
        self._app_access_addr = None
        self._protocol = None
        self._platform = None
        self._is_support_multiomp = None
        self._tenant = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if customer_id is not None:
            self.customer_id = customer_id
        if resource_id is not None:
            self.resource_id = resource_id
        if developer_account is not None:
            self.developer_account = developer_account
        if app_name is not None:
            self.app_name = app_name
        if omp_app_name is not None:
            self.omp_app_name = omp_app_name
        if app_key is not None:
            self.app_key = app_key
        if up_link_addr is not None:
            self.up_link_addr = up_link_addr
        if status is not None:
            self.status = status
        if industry is not None:
            self.industry = industry
        if region is not None:
            self.region = region
        if intl_channel_num is not None:
            self.intl_channel_num = intl_channel_num
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if ip_white_list is not None:
            self.ip_white_list = ip_white_list
        if app_access_addr is not None:
            self.app_access_addr = app_access_addr
        if protocol is not None:
            self.protocol = protocol
        if platform is not None:
            self.platform = platform
        if is_support_multiomp is not None:
            self.is_support_multiomp = is_support_multiomp
        if tenant is not None:
            self.tenant = tenant

    @property
    def id(self):
        """Gets the id of this SmsAppQueryResp.

        应用主键ID，用于获取、修改应用的唯一标识

        :return: The id of this SmsAppQueryResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmsAppQueryResp.

        应用主键ID，用于获取、修改应用的唯一标识

        :param id: The id of this SmsAppQueryResp.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this SmsAppQueryResp.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :return: The create_time of this SmsAppQueryResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SmsAppQueryResp.

        创建时间[yyyy-MM-dd HH:mm:ss]

        :param create_time: The create_time of this SmsAppQueryResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SmsAppQueryResp.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :return: The update_time of this SmsAppQueryResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SmsAppQueryResp.

        更新时间[yyyy-MM-dd HH:mm:ss]

        :param update_time: The update_time of this SmsAppQueryResp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def customer_id(self):
        """Gets the customer_id of this SmsAppQueryResp.

        租户customer id

        :return: The customer_id of this SmsAppQueryResp.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SmsAppQueryResp.

        租户customer id

        :param customer_id: The customer_id of this SmsAppQueryResp.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def resource_id(self):
        """Gets the resource_id of this SmsAppQueryResp.

        租户resource id

        :return: The resource_id of this SmsAppQueryResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SmsAppQueryResp.

        租户resource id

        :param resource_id: The resource_id of this SmsAppQueryResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def developer_account(self):
        """Gets the developer_account of this SmsAppQueryResp.

        租户开发者账号

        :return: The developer_account of this SmsAppQueryResp.
        :rtype: str
        """
        return self._developer_account

    @developer_account.setter
    def developer_account(self, developer_account):
        """Sets the developer_account of this SmsAppQueryResp.

        租户开发者账号

        :param developer_account: The developer_account of this SmsAppQueryResp.
        :type developer_account: str
        """
        self._developer_account = developer_account

    @property
    def app_name(self):
        """Gets the app_name of this SmsAppQueryResp.

        应用名称

        :return: The app_name of this SmsAppQueryResp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this SmsAppQueryResp.

        应用名称

        :param app_name: The app_name of this SmsAppQueryResp.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def omp_app_name(self):
        """Gets the omp_app_name of this SmsAppQueryResp.

        omp应用名称

        :return: The omp_app_name of this SmsAppQueryResp.
        :rtype: str
        """
        return self._omp_app_name

    @omp_app_name.setter
    def omp_app_name(self, omp_app_name):
        """Sets the omp_app_name of this SmsAppQueryResp.

        omp应用名称

        :param omp_app_name: The omp_app_name of this SmsAppQueryResp.
        :type omp_app_name: str
        """
        self._omp_app_name = omp_app_name

    @property
    def app_key(self):
        """Gets the app_key of this SmsAppQueryResp.

        应用key

        :return: The app_key of this SmsAppQueryResp.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this SmsAppQueryResp.

        应用key

        :param app_key: The app_key of this SmsAppQueryResp.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def up_link_addr(self):
        """Gets the up_link_addr of this SmsAppQueryResp.

        上行短信地址

        :return: The up_link_addr of this SmsAppQueryResp.
        :rtype: str
        """
        return self._up_link_addr

    @up_link_addr.setter
    def up_link_addr(self, up_link_addr):
        """Sets the up_link_addr of this SmsAppQueryResp.

        上行短信地址

        :param up_link_addr: The up_link_addr of this SmsAppQueryResp.
        :type up_link_addr: str
        """
        self._up_link_addr = up_link_addr

    @property
    def status(self):
        """Gets the status of this SmsAppQueryResp.

        应用状态   CREATED：待上线。应用暂未创建成功，请稍候。   SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   LAUNCHED：正常。应用添加成功，可以正常使用。

        :return: The status of this SmsAppQueryResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SmsAppQueryResp.

        应用状态   CREATED：待上线。应用暂未创建成功，请稍候。   SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   LAUNCHED：正常。应用添加成功，可以正常使用。

        :param status: The status of this SmsAppQueryResp.
        :type status: str
        """
        self._status = status

    @property
    def industry(self):
        """Gets the industry of this SmsAppQueryResp.

        行业类型

        :return: The industry of this SmsAppQueryResp.
        :rtype: int
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this SmsAppQueryResp.

        行业类型

        :param industry: The industry of this SmsAppQueryResp.
        :type industry: int
        """
        self._industry = industry

    @property
    def region(self):
        """Gets the region of this SmsAppQueryResp.

        地域 1. cn：国内 2. intl：国际

        :return: The region of this SmsAppQueryResp.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SmsAppQueryResp.

        地域 1. cn：国内 2. intl：国际

        :param region: The region of this SmsAppQueryResp.
        :type region: str
        """
        self._region = region

    @property
    def intl_channel_num(self):
        """Gets the intl_channel_num of this SmsAppQueryResp.

        国际/港澳台短信通道号

        :return: The intl_channel_num of this SmsAppQueryResp.
        :rtype: str
        """
        return self._intl_channel_num

    @intl_channel_num.setter
    def intl_channel_num(self, intl_channel_num):
        """Sets the intl_channel_num of this SmsAppQueryResp.

        国际/港澳台短信通道号

        :param intl_channel_num: The intl_channel_num of this SmsAppQueryResp.
        :type intl_channel_num: str
        """
        self._intl_channel_num = intl_channel_num

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SmsAppQueryResp.

        企业项目ID

        :return: The enterprise_project_id of this SmsAppQueryResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SmsAppQueryResp.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this SmsAppQueryResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this SmsAppQueryResp.

        企业项目名称

        :return: The enterprise_project_name of this SmsAppQueryResp.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this SmsAppQueryResp.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this SmsAppQueryResp.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def ip_white_list(self):
        """Gets the ip_white_list of this SmsAppQueryResp.

        IP白名单

        :return: The ip_white_list of this SmsAppQueryResp.
        :rtype: str
        """
        return self._ip_white_list

    @ip_white_list.setter
    def ip_white_list(self, ip_white_list):
        """Sets the ip_white_list of this SmsAppQueryResp.

        IP白名单

        :param ip_white_list: The ip_white_list of this SmsAppQueryResp.
        :type ip_white_list: str
        """
        self._ip_white_list = ip_white_list

    @property
    def app_access_addr(self):
        """Gets the app_access_addr of this SmsAppQueryResp.

        接入地址

        :return: The app_access_addr of this SmsAppQueryResp.
        :rtype: str
        """
        return self._app_access_addr

    @app_access_addr.setter
    def app_access_addr(self, app_access_addr):
        """Sets the app_access_addr of this SmsAppQueryResp.

        接入地址

        :param app_access_addr: The app_access_addr of this SmsAppQueryResp.
        :type app_access_addr: str
        """
        self._app_access_addr = app_access_addr

    @property
    def protocol(self):
        """Gets the protocol of this SmsAppQueryResp.

        协议

        :return: The protocol of this SmsAppQueryResp.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SmsAppQueryResp.

        协议

        :param protocol: The protocol of this SmsAppQueryResp.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def platform(self):
        """Gets the platform of this SmsAppQueryResp.

        平台

        :return: The platform of this SmsAppQueryResp.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this SmsAppQueryResp.

        平台

        :param platform: The platform of this SmsAppQueryResp.
        :type platform: str
        """
        self._platform = platform

    @property
    def is_support_multiomp(self):
        """Gets the is_support_multiomp of this SmsAppQueryResp.

        是否支持多OMP

        :return: The is_support_multiomp of this SmsAppQueryResp.
        :rtype: bool
        """
        return self._is_support_multiomp

    @is_support_multiomp.setter
    def is_support_multiomp(self, is_support_multiomp):
        """Sets the is_support_multiomp of this SmsAppQueryResp.

        是否支持多OMP

        :param is_support_multiomp: The is_support_multiomp of this SmsAppQueryResp.
        :type is_support_multiomp: bool
        """
        self._is_support_multiomp = is_support_multiomp

    @property
    def tenant(self):
        """Gets the tenant of this SmsAppQueryResp.

        :return: The tenant of this SmsAppQueryResp.
        :rtype: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this SmsAppQueryResp.

        :param tenant: The tenant of this SmsAppQueryResp.
        :type tenant: :class:`huaweicloudsdkmsgsms.v2.TenantBasic`
        """
        self._tenant = tenant

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
        if not isinstance(other, SmsAppQueryResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
