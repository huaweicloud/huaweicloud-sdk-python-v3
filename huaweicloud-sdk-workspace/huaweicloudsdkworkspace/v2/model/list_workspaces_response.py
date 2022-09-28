# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspacesResponse(SdkResponse):

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
        'ad_domains': 'AdInfo',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'access_mode': 'str',
        'dedicated_subnets': 'str',
        'dedicated_access_address': 'str',
        'internet_access_address': 'str',
        'internet_access_port': 'str',
        'status': 'str',
        'access_status': 'str',
        'subnet_ids': 'list[SubnetInfo]',
        'management_subnet_cidr': 'str',
        'infrastructure_security_group': 'SecurityGroup',
        'desktop_security_group': 'SecurityGroup',
        'closable': 'bool',
        'config_status': 'str',
        'progress': 'str',
        'job_id': 'str',
        'fail_code': 'int',
        'fail_reason': 'str',
        'enterprise_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ad_domains': 'ad_domains',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'access_mode': 'access_mode',
        'dedicated_subnets': 'dedicated_subnets',
        'dedicated_access_address': 'dedicated_access_address',
        'internet_access_address': 'internet_access_address',
        'internet_access_port': 'internet_access_port',
        'status': 'status',
        'access_status': 'access_status',
        'subnet_ids': 'subnet_ids',
        'management_subnet_cidr': 'management_subnet_cidr',
        'infrastructure_security_group': 'infrastructure_security_group',
        'desktop_security_group': 'desktop_security_group',
        'closable': 'closable',
        'config_status': 'config_status',
        'progress': 'progress',
        'job_id': 'job_id',
        'fail_code': 'fail_code',
        'fail_reason': 'fail_reason',
        'enterprise_id': 'enterprise_id'
    }

    def __init__(self, id=None, ad_domains=None, vpc_id=None, vpc_name=None, access_mode=None, dedicated_subnets=None, dedicated_access_address=None, internet_access_address=None, internet_access_port=None, status=None, access_status=None, subnet_ids=None, management_subnet_cidr=None, infrastructure_security_group=None, desktop_security_group=None, closable=None, config_status=None, progress=None, job_id=None, fail_code=None, fail_reason=None, enterprise_id=None):
        """ListWorkspacesResponse

        The model defined in huaweicloud sdk

        :param id: 唯一标识ID。
        :type id: str
        :param ad_domains: 
        :type ad_domains: :class:`huaweicloudsdkworkspace.v2.AdInfo`
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param vpc_name: VPC名称。
        :type vpc_name: str
        :param access_mode: 接入方式。 - INTERNET：表示互联网接入。 - DEDICATED：表示专线接入。 - BOTH：表示同时支持互联网接入和专线接入。
        :type access_mode: str
        :param dedicated_subnets: 专线接入网段，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。
        :type dedicated_subnets: str
        :param dedicated_access_address: 专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。
        :type dedicated_access_address: str
        :param internet_access_address: 互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。
        :type internet_access_address: str
        :param internet_access_port: 互联网接入端口。
        :type internet_access_port: str
        :param status: 云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。
        :type status: str
        :param access_status: 互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态。 - available： 可用 - 执行过任务且成功后恢复的正常状态。 - internetOpening： 开启中 - 开通互联网接入开启中。 - dedicatedOpening： 开启中 - 开通专线接入开启中。 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败。 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败。 - openSuccess： 开启成功 - 开通互联网接入成功。 - internetClosing： 关闭中 - 关闭互联网接入关闭中。 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中。 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败。 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败。 - closeSuccess： 关闭成功 - 关闭接入方式成功。 - internetAccessPortModifying： 互联网接入端口修改中。 - internetAccessPortModifyFailed： 端口修改失败。
        :type access_status: str
        :param subnet_ids: 业务子网，可以指定返回的网络ID订购桌面。
        :type subnet_ids: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        :param management_subnet_cidr: 管理组件的子网网段。
        :type management_subnet_cidr: str
        :param infrastructure_security_group: 
        :type infrastructure_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        :param desktop_security_group: 
        :type desktop_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        :param closable: 是否可以取消服务。
        :type closable: bool
        :param config_status: 配置状态。 - \&quot;0\&quot;： 开通服务成功，且对接AD成功。 - \&quot;1\&quot;： 开通服务成功，但AD配置失败。 - \&quot;2\&quot;： 开通服务成功，但AD配置失败后存在其他错误。 - \&quot;3\&quot;： 开通服务成功，AD未开启对接。
        :type config_status: str
        :param progress: 开通服务或注销服务的进度，格式为百分比，如：100%。
        :type progress: str
        :param job_id: 开通服务或取消服务的任务ID。
        :type job_id: str
        :param fail_code: 失败错误码。
        :type fail_code: int
        :param fail_reason: 失败原因。
        :type fail_reason: str
        :param enterprise_id: 企业ID。
        :type enterprise_id: str
        """
        
        super(ListWorkspacesResponse, self).__init__()

        self._id = None
        self._ad_domains = None
        self._vpc_id = None
        self._vpc_name = None
        self._access_mode = None
        self._dedicated_subnets = None
        self._dedicated_access_address = None
        self._internet_access_address = None
        self._internet_access_port = None
        self._status = None
        self._access_status = None
        self._subnet_ids = None
        self._management_subnet_cidr = None
        self._infrastructure_security_group = None
        self._desktop_security_group = None
        self._closable = None
        self._config_status = None
        self._progress = None
        self._job_id = None
        self._fail_code = None
        self._fail_reason = None
        self._enterprise_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ad_domains is not None:
            self.ad_domains = ad_domains
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if access_mode is not None:
            self.access_mode = access_mode
        if dedicated_subnets is not None:
            self.dedicated_subnets = dedicated_subnets
        if dedicated_access_address is not None:
            self.dedicated_access_address = dedicated_access_address
        if internet_access_address is not None:
            self.internet_access_address = internet_access_address
        if internet_access_port is not None:
            self.internet_access_port = internet_access_port
        if status is not None:
            self.status = status
        if access_status is not None:
            self.access_status = access_status
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if management_subnet_cidr is not None:
            self.management_subnet_cidr = management_subnet_cidr
        if infrastructure_security_group is not None:
            self.infrastructure_security_group = infrastructure_security_group
        if desktop_security_group is not None:
            self.desktop_security_group = desktop_security_group
        if closable is not None:
            self.closable = closable
        if config_status is not None:
            self.config_status = config_status
        if progress is not None:
            self.progress = progress
        if job_id is not None:
            self.job_id = job_id
        if fail_code is not None:
            self.fail_code = fail_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id

    @property
    def id(self):
        """Gets the id of this ListWorkspacesResponse.

        唯一标识ID。

        :return: The id of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListWorkspacesResponse.

        唯一标识ID。

        :param id: The id of this ListWorkspacesResponse.
        :type id: str
        """
        self._id = id

    @property
    def ad_domains(self):
        """Gets the ad_domains of this ListWorkspacesResponse.


        :return: The ad_domains of this ListWorkspacesResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AdInfo`
        """
        return self._ad_domains

    @ad_domains.setter
    def ad_domains(self, ad_domains):
        """Sets the ad_domains of this ListWorkspacesResponse.


        :param ad_domains: The ad_domains of this ListWorkspacesResponse.
        :type ad_domains: :class:`huaweicloudsdkworkspace.v2.AdInfo`
        """
        self._ad_domains = ad_domains

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListWorkspacesResponse.

        VPC ID。

        :return: The vpc_id of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListWorkspacesResponse.

        VPC ID。

        :param vpc_id: The vpc_id of this ListWorkspacesResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this ListWorkspacesResponse.

        VPC名称。

        :return: The vpc_name of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this ListWorkspacesResponse.

        VPC名称。

        :param vpc_name: The vpc_name of this ListWorkspacesResponse.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def access_mode(self):
        """Gets the access_mode of this ListWorkspacesResponse.

        接入方式。 - INTERNET：表示互联网接入。 - DEDICATED：表示专线接入。 - BOTH：表示同时支持互联网接入和专线接入。

        :return: The access_mode of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this ListWorkspacesResponse.

        接入方式。 - INTERNET：表示互联网接入。 - DEDICATED：表示专线接入。 - BOTH：表示同时支持互联网接入和专线接入。

        :param access_mode: The access_mode of this ListWorkspacesResponse.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def dedicated_subnets(self):
        """Gets the dedicated_subnets of this ListWorkspacesResponse.

        专线接入网段，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :return: The dedicated_subnets of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._dedicated_subnets

    @dedicated_subnets.setter
    def dedicated_subnets(self, dedicated_subnets):
        """Sets the dedicated_subnets of this ListWorkspacesResponse.

        专线接入网段，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :param dedicated_subnets: The dedicated_subnets of this ListWorkspacesResponse.
        :type dedicated_subnets: str
        """
        self._dedicated_subnets = dedicated_subnets

    @property
    def dedicated_access_address(self):
        """Gets the dedicated_access_address of this ListWorkspacesResponse.

        专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :return: The dedicated_access_address of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._dedicated_access_address

    @dedicated_access_address.setter
    def dedicated_access_address(self, dedicated_access_address):
        """Sets the dedicated_access_address of this ListWorkspacesResponse.

        专线接入地址，只有access_mode为“DEDICATED”或“BOTH”时才会返回该参数。

        :param dedicated_access_address: The dedicated_access_address of this ListWorkspacesResponse.
        :type dedicated_access_address: str
        """
        self._dedicated_access_address = dedicated_access_address

    @property
    def internet_access_address(self):
        """Gets the internet_access_address of this ListWorkspacesResponse.

        互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。

        :return: The internet_access_address of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._internet_access_address

    @internet_access_address.setter
    def internet_access_address(self, internet_access_address):
        """Sets the internet_access_address of this ListWorkspacesResponse.

        互联网接入地址，只有access_mode为“INTERNET”或“BOTH”时才会返回该参数。

        :param internet_access_address: The internet_access_address of this ListWorkspacesResponse.
        :type internet_access_address: str
        """
        self._internet_access_address = internet_access_address

    @property
    def internet_access_port(self):
        """Gets the internet_access_port of this ListWorkspacesResponse.

        互联网接入端口。

        :return: The internet_access_port of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._internet_access_port

    @internet_access_port.setter
    def internet_access_port(self, internet_access_port):
        """Sets the internet_access_port of this ListWorkspacesResponse.

        互联网接入端口。

        :param internet_access_port: The internet_access_port of this ListWorkspacesResponse.
        :type internet_access_port: str
        """
        self._internet_access_port = internet_access_port

    @property
    def status(self):
        """Gets the status of this ListWorkspacesResponse.

        云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。

        :return: The status of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListWorkspacesResponse.

        云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。

        :param status: The status of this ListWorkspacesResponse.
        :type status: str
        """
        self._status = status

    @property
    def access_status(self):
        """Gets the access_status of this ListWorkspacesResponse.

        互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态。 - available： 可用 - 执行过任务且成功后恢复的正常状态。 - internetOpening： 开启中 - 开通互联网接入开启中。 - dedicatedOpening： 开启中 - 开通专线接入开启中。 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败。 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败。 - openSuccess： 开启成功 - 开通互联网接入成功。 - internetClosing： 关闭中 - 关闭互联网接入关闭中。 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中。 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败。 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败。 - closeSuccess： 关闭成功 - 关闭接入方式成功。 - internetAccessPortModifying： 互联网接入端口修改中。 - internetAccessPortModifyFailed： 端口修改失败。

        :return: The access_status of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this ListWorkspacesResponse.

        互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态。 - available： 可用 - 执行过任务且成功后恢复的正常状态。 - internetOpening： 开启中 - 开通互联网接入开启中。 - dedicatedOpening： 开启中 - 开通专线接入开启中。 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败。 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败。 - openSuccess： 开启成功 - 开通互联网接入成功。 - internetClosing： 关闭中 - 关闭互联网接入关闭中。 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中。 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败。 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败。 - closeSuccess： 关闭成功 - 关闭接入方式成功。 - internetAccessPortModifying： 互联网接入端口修改中。 - internetAccessPortModifyFailed： 端口修改失败。

        :param access_status: The access_status of this ListWorkspacesResponse.
        :type access_status: str
        """
        self._access_status = access_status

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this ListWorkspacesResponse.

        业务子网，可以指定返回的网络ID订购桌面。

        :return: The subnet_ids of this ListWorkspacesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this ListWorkspacesResponse.

        业务子网，可以指定返回的网络ID订购桌面。

        :param subnet_ids: The subnet_ids of this ListWorkspacesResponse.
        :type subnet_ids: list[:class:`huaweicloudsdkworkspace.v2.SubnetInfo`]
        """
        self._subnet_ids = subnet_ids

    @property
    def management_subnet_cidr(self):
        """Gets the management_subnet_cidr of this ListWorkspacesResponse.

        管理组件的子网网段。

        :return: The management_subnet_cidr of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._management_subnet_cidr

    @management_subnet_cidr.setter
    def management_subnet_cidr(self, management_subnet_cidr):
        """Sets the management_subnet_cidr of this ListWorkspacesResponse.

        管理组件的子网网段。

        :param management_subnet_cidr: The management_subnet_cidr of this ListWorkspacesResponse.
        :type management_subnet_cidr: str
        """
        self._management_subnet_cidr = management_subnet_cidr

    @property
    def infrastructure_security_group(self):
        """Gets the infrastructure_security_group of this ListWorkspacesResponse.


        :return: The infrastructure_security_group of this ListWorkspacesResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        return self._infrastructure_security_group

    @infrastructure_security_group.setter
    def infrastructure_security_group(self, infrastructure_security_group):
        """Sets the infrastructure_security_group of this ListWorkspacesResponse.


        :param infrastructure_security_group: The infrastructure_security_group of this ListWorkspacesResponse.
        :type infrastructure_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        self._infrastructure_security_group = infrastructure_security_group

    @property
    def desktop_security_group(self):
        """Gets the desktop_security_group of this ListWorkspacesResponse.


        :return: The desktop_security_group of this ListWorkspacesResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        return self._desktop_security_group

    @desktop_security_group.setter
    def desktop_security_group(self, desktop_security_group):
        """Sets the desktop_security_group of this ListWorkspacesResponse.


        :param desktop_security_group: The desktop_security_group of this ListWorkspacesResponse.
        :type desktop_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        self._desktop_security_group = desktop_security_group

    @property
    def closable(self):
        """Gets the closable of this ListWorkspacesResponse.

        是否可以取消服务。

        :return: The closable of this ListWorkspacesResponse.
        :rtype: bool
        """
        return self._closable

    @closable.setter
    def closable(self, closable):
        """Sets the closable of this ListWorkspacesResponse.

        是否可以取消服务。

        :param closable: The closable of this ListWorkspacesResponse.
        :type closable: bool
        """
        self._closable = closable

    @property
    def config_status(self):
        """Gets the config_status of this ListWorkspacesResponse.

        配置状态。 - \"0\"： 开通服务成功，且对接AD成功。 - \"1\"： 开通服务成功，但AD配置失败。 - \"2\"： 开通服务成功，但AD配置失败后存在其他错误。 - \"3\"： 开通服务成功，AD未开启对接。

        :return: The config_status of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this ListWorkspacesResponse.

        配置状态。 - \"0\"： 开通服务成功，且对接AD成功。 - \"1\"： 开通服务成功，但AD配置失败。 - \"2\"： 开通服务成功，但AD配置失败后存在其他错误。 - \"3\"： 开通服务成功，AD未开启对接。

        :param config_status: The config_status of this ListWorkspacesResponse.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def progress(self):
        """Gets the progress of this ListWorkspacesResponse.

        开通服务或注销服务的进度，格式为百分比，如：100%。

        :return: The progress of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ListWorkspacesResponse.

        开通服务或注销服务的进度，格式为百分比，如：100%。

        :param progress: The progress of this ListWorkspacesResponse.
        :type progress: str
        """
        self._progress = progress

    @property
    def job_id(self):
        """Gets the job_id of this ListWorkspacesResponse.

        开通服务或取消服务的任务ID。

        :return: The job_id of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListWorkspacesResponse.

        开通服务或取消服务的任务ID。

        :param job_id: The job_id of this ListWorkspacesResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def fail_code(self):
        """Gets the fail_code of this ListWorkspacesResponse.

        失败错误码。

        :return: The fail_code of this ListWorkspacesResponse.
        :rtype: int
        """
        return self._fail_code

    @fail_code.setter
    def fail_code(self, fail_code):
        """Sets the fail_code of this ListWorkspacesResponse.

        失败错误码。

        :param fail_code: The fail_code of this ListWorkspacesResponse.
        :type fail_code: int
        """
        self._fail_code = fail_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ListWorkspacesResponse.

        失败原因。

        :return: The fail_reason of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ListWorkspacesResponse.

        失败原因。

        :param fail_reason: The fail_reason of this ListWorkspacesResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this ListWorkspacesResponse.

        企业ID。

        :return: The enterprise_id of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this ListWorkspacesResponse.

        企业ID。

        :param enterprise_id: The enterprise_id of this ListWorkspacesResponse.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

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
        if not isinstance(other, ListWorkspacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
