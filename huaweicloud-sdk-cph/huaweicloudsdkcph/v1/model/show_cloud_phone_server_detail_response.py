# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudPhoneServerDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'server_name': 'str',
        'availability_zone': 'str',
        'server_id': 'str',
        'server_model_name': 'str',
        'phone_model_name': 'str',
        'keypair_name': 'str',
        'status': 'int',
        'vpc_id': 'str',
        'cidr': 'str',
        'vpc_cidr': 'str',
        'subnet_id': 'str',
        'subnet_cidr': 'str',
        'resource_project_id': 'str',
        'metadata': 'ShowCloudPhoneServerDetailResponseBodyMetadata',
        'addresses': 'list[Address]',
        'band_widths': 'list[Bandwidth]',
        'volumes': 'list[Volume]',
        'network_version': 'str',
        'enterprise_project_id': 'str',
        'security_groups': 'list[str]',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'server_name': 'server_name',
        'availability_zone': 'availability_zone',
        'server_id': 'server_id',
        'server_model_name': 'server_model_name',
        'phone_model_name': 'phone_model_name',
        'keypair_name': 'keypair_name',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'cidr': 'cidr',
        'vpc_cidr': 'vpc_cidr',
        'subnet_id': 'subnet_id',
        'subnet_cidr': 'subnet_cidr',
        'resource_project_id': 'resource_project_id',
        'metadata': 'metadata',
        'addresses': 'addresses',
        'band_widths': 'band_widths',
        'volumes': 'volumes',
        'network_version': 'network_version',
        'enterprise_project_id': 'enterprise_project_id',
        'security_groups': 'security_groups',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, request_id=None, server_name=None, availability_zone=None, server_id=None, server_model_name=None, phone_model_name=None, keypair_name=None, status=None, vpc_id=None, cidr=None, vpc_cidr=None, subnet_id=None, subnet_cidr=None, resource_project_id=None, metadata=None, addresses=None, band_widths=None, volumes=None, network_version=None, enterprise_project_id=None, security_groups=None, create_time=None, update_time=None):
        """ShowCloudPhoneServerDetailResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param server_name: 云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。
        :type server_name: str
        :param availability_zone: 云手机服务器所在的可用区。
        :type availability_zone: str
        :param server_id: 云手机服务器的唯一标识，不超过32个字节。
        :type server_id: str
        :param server_model_name: 云手机服务器规格名称，不超过64个字节。
        :type server_model_name: str
        :param phone_model_name: 云手机规格名称，不超过64个字节。
        :type phone_model_name: str
        :param keypair_name: 连接云手机所使用的密钥对的名称，不超过64个字节。
        :type keypair_name: str
        :param status: 服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中
        :type status: int
        :param vpc_id: 云手机服务器所属虚拟私有云（简称VPC）的ID。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC ID；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC ID。
        :type vpc_id: str
        :param cidr: 云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。
        :type cidr: str
        :param vpc_cidr: 云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。
        :type vpc_cidr: str
        :param subnet_id: 云手机服务器所属子网的ID。仅在网络版本 network_version 取值为“v2”时，该取值表示租户创建服务器时指定子网的 ID；网络版本取值为“v1”时，该字段表示云手机服务器所属资源租户的子网ID。
        :type subnet_id: str
        :param subnet_cidr: 云手机服务器所属子网的网段。网络版本 network_version取值为“v2”时，表示租户创建服务器时指定子网的 CIDR；取值为“v1”时，表示云手机服务器所属资源租户的子网CIDR。
        :type subnet_cidr: str
        :param resource_project_id: 云手机服务器的项目ID。
        :type resource_project_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponseBodyMetadata`
        :param addresses: 云手机服务器的IP相关信息。
        :type addresses: list[:class:`huaweicloudsdkcph.v1.Address`]
        :param band_widths: 云手机服务器带宽信息的结构体数组。
        :type band_widths: list[:class:`huaweicloudsdkcph.v1.Bandwidth`]
        :param volumes: 云手机服务器卷信息的结构体数组。
        :type volumes: list[:class:`huaweicloudsdkcph.v1.Volume`]
        :param network_version: 是否为自定义网络的云手机服务器标识。\&quot;v1\&quot;，非自定义网络的云手机服务器。\&quot;v2\&quot;，自定义网络的云手机服务器。支持按照网络版本字段进行筛选。
        :type network_version: str
        :param enterprise_project_id: 云手机服务器所属企业项目ID。
        :type enterprise_project_id: str
        :param security_groups: 服务器扩展网卡绑定的安全组信息。 系统定义网络的服务器，该字段返回为空列表。
        :type security_groups: list[str]
        :param create_time: 创建时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param update_time: 更新时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        """
        
        super(ShowCloudPhoneServerDetailResponse, self).__init__()

        self._request_id = None
        self._server_name = None
        self._availability_zone = None
        self._server_id = None
        self._server_model_name = None
        self._phone_model_name = None
        self._keypair_name = None
        self._status = None
        self._vpc_id = None
        self._cidr = None
        self._vpc_cidr = None
        self._subnet_id = None
        self._subnet_cidr = None
        self._resource_project_id = None
        self._metadata = None
        self._addresses = None
        self._band_widths = None
        self._volumes = None
        self._network_version = None
        self._enterprise_project_id = None
        self._security_groups = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if server_name is not None:
            self.server_name = server_name
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if server_id is not None:
            self.server_id = server_id
        if server_model_name is not None:
            self.server_model_name = server_model_name
        if phone_model_name is not None:
            self.phone_model_name = phone_model_name
        if keypair_name is not None:
            self.keypair_name = keypair_name
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if cidr is not None:
            self.cidr = cidr
        if vpc_cidr is not None:
            self.vpc_cidr = vpc_cidr
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id
        if metadata is not None:
            self.metadata = metadata
        if addresses is not None:
            self.addresses = addresses
        if band_widths is not None:
            self.band_widths = band_widths
        if volumes is not None:
            self.volumes = volumes
        if network_version is not None:
            self.network_version = network_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if security_groups is not None:
            self.security_groups = security_groups
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def request_id(self):
        """Gets the request_id of this ShowCloudPhoneServerDetailResponse.

        请求的唯一标识ID。

        :return: The request_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowCloudPhoneServerDetailResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ShowCloudPhoneServerDetailResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def server_name(self):
        """Gets the server_name of this ShowCloudPhoneServerDetailResponse.

        云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。

        :return: The server_name of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this ShowCloudPhoneServerDetailResponse.

        云手机服务器名称， 不超过65字符，只支持英文字母、数字、汉字、下划线和中划线。

        :param server_name: The server_name of this ShowCloudPhoneServerDetailResponse.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所在的可用区。

        :return: The availability_zone of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所在的可用区。

        :param availability_zone: The availability_zone of this ShowCloudPhoneServerDetailResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def server_id(self):
        """Gets the server_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的唯一标识，不超过32个字节。

        :return: The server_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的唯一标识，不超过32个字节。

        :param server_id: The server_id of this ShowCloudPhoneServerDetailResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_model_name(self):
        """Gets the server_model_name of this ShowCloudPhoneServerDetailResponse.

        云手机服务器规格名称，不超过64个字节。

        :return: The server_model_name of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        """Sets the server_model_name of this ShowCloudPhoneServerDetailResponse.

        云手机服务器规格名称，不超过64个字节。

        :param server_model_name: The server_model_name of this ShowCloudPhoneServerDetailResponse.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this ShowCloudPhoneServerDetailResponse.

        云手机规格名称，不超过64个字节。

        :return: The phone_model_name of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this ShowCloudPhoneServerDetailResponse.

        云手机规格名称，不超过64个字节。

        :param phone_model_name: The phone_model_name of this ShowCloudPhoneServerDetailResponse.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def keypair_name(self):
        """Gets the keypair_name of this ShowCloudPhoneServerDetailResponse.

        连接云手机所使用的密钥对的名称，不超过64个字节。

        :return: The keypair_name of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this ShowCloudPhoneServerDetailResponse.

        连接云手机所使用的密钥对的名称，不超过64个字节。

        :param keypair_name: The keypair_name of this ShowCloudPhoneServerDetailResponse.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def status(self):
        """Gets the status of this ShowCloudPhoneServerDetailResponse.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :return: The status of this ShowCloudPhoneServerDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowCloudPhoneServerDetailResponse.

        服务器状态。 - 0、1、3、4：创建中 - 2：异常 - 5：正常 - 8：冻结 - 10：关机 - 11：关机中 - 12：关机失败 - 13：开机中

        :param status: The status of this ShowCloudPhoneServerDetailResponse.
        :type status: int
        """
        self._status = status

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的ID。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC ID；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC ID。

        :return: The vpc_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的ID。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC ID；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC ID。

        :param vpc_id: The vpc_id of this ShowCloudPhoneServerDetailResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def cidr(self):
        """Gets the cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。

        :return: The cidr of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。

        :param cidr: The cidr of this ShowCloudPhoneServerDetailResponse.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def vpc_cidr(self):
        """Gets the vpc_cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。

        :return: The vpc_cidr of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        """Sets the vpc_cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属虚拟私有云（简称VPC）的网段。网络版本 network_version 取值为“v1”时，表示云手机服务器所属资源租户的VPC CIDR；取值为“v2”时，表示租户创建服务器时指定 VPC 的 VPC CIDR。

        :param vpc_cidr: The vpc_cidr of this ShowCloudPhoneServerDetailResponse.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属子网的ID。仅在网络版本 network_version 取值为“v2”时，该取值表示租户创建服务器时指定子网的 ID；网络版本取值为“v1”时，该字段表示云手机服务器所属资源租户的子网ID。

        :return: The subnet_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属子网的ID。仅在网络版本 network_version 取值为“v2”时，该取值表示租户创建服务器时指定子网的 ID；网络版本取值为“v1”时，该字段表示云手机服务器所属资源租户的子网ID。

        :param subnet_id: The subnet_id of this ShowCloudPhoneServerDetailResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属子网的网段。网络版本 network_version取值为“v2”时，表示租户创建服务器时指定子网的 CIDR；取值为“v1”时，表示云手机服务器所属资源租户的子网CIDR。

        :return: The subnet_cidr of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属子网的网段。网络版本 network_version取值为“v2”时，表示租户创建服务器时指定子网的 CIDR；取值为“v1”时，表示云手机服务器所属资源租户的子网CIDR。

        :param subnet_cidr: The subnet_cidr of this ShowCloudPhoneServerDetailResponse.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def resource_project_id(self):
        """Gets the resource_project_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的项目ID。

        :return: The resource_project_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        """Sets the resource_project_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的项目ID。

        :param resource_project_id: The resource_project_id of this ShowCloudPhoneServerDetailResponse.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def metadata(self):
        """Gets the metadata of this ShowCloudPhoneServerDetailResponse.

        :return: The metadata of this ShowCloudPhoneServerDetailResponse.
        :rtype: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponseBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowCloudPhoneServerDetailResponse.

        :param metadata: The metadata of this ShowCloudPhoneServerDetailResponse.
        :type metadata: :class:`huaweicloudsdkcph.v1.ShowCloudPhoneServerDetailResponseBodyMetadata`
        """
        self._metadata = metadata

    @property
    def addresses(self):
        """Gets the addresses of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的IP相关信息。

        :return: The addresses of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Address`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ShowCloudPhoneServerDetailResponse.

        云手机服务器的IP相关信息。

        :param addresses: The addresses of this ShowCloudPhoneServerDetailResponse.
        :type addresses: list[:class:`huaweicloudsdkcph.v1.Address`]
        """
        self._addresses = addresses

    @property
    def band_widths(self):
        """Gets the band_widths of this ShowCloudPhoneServerDetailResponse.

        云手机服务器带宽信息的结构体数组。

        :return: The band_widths of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Bandwidth`]
        """
        return self._band_widths

    @band_widths.setter
    def band_widths(self, band_widths):
        """Sets the band_widths of this ShowCloudPhoneServerDetailResponse.

        云手机服务器带宽信息的结构体数组。

        :param band_widths: The band_widths of this ShowCloudPhoneServerDetailResponse.
        :type band_widths: list[:class:`huaweicloudsdkcph.v1.Bandwidth`]
        """
        self._band_widths = band_widths

    @property
    def volumes(self):
        """Gets the volumes of this ShowCloudPhoneServerDetailResponse.

        云手机服务器卷信息的结构体数组。

        :return: The volumes of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ShowCloudPhoneServerDetailResponse.

        云手机服务器卷信息的结构体数组。

        :param volumes: The volumes of this ShowCloudPhoneServerDetailResponse.
        :type volumes: list[:class:`huaweicloudsdkcph.v1.Volume`]
        """
        self._volumes = volumes

    @property
    def network_version(self):
        """Gets the network_version of this ShowCloudPhoneServerDetailResponse.

        是否为自定义网络的云手机服务器标识。\"v1\"，非自定义网络的云手机服务器。\"v2\"，自定义网络的云手机服务器。支持按照网络版本字段进行筛选。

        :return: The network_version of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._network_version

    @network_version.setter
    def network_version(self, network_version):
        """Sets the network_version of this ShowCloudPhoneServerDetailResponse.

        是否为自定义网络的云手机服务器标识。\"v1\"，非自定义网络的云手机服务器。\"v2\"，自定义网络的云手机服务器。支持按照网络版本字段进行筛选。

        :param network_version: The network_version of this ShowCloudPhoneServerDetailResponse.
        :type network_version: str
        """
        self._network_version = network_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属企业项目ID。

        :return: The enterprise_project_id of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowCloudPhoneServerDetailResponse.

        云手机服务器所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowCloudPhoneServerDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_groups(self):
        """Gets the security_groups of this ShowCloudPhoneServerDetailResponse.

        服务器扩展网卡绑定的安全组信息。 系统定义网络的服务器，该字段返回为空列表。

        :return: The security_groups of this ShowCloudPhoneServerDetailResponse.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ShowCloudPhoneServerDetailResponse.

        服务器扩展网卡绑定的安全组信息。 系统定义网络的服务器，该字段返回为空列表。

        :param security_groups: The security_groups of this ShowCloudPhoneServerDetailResponse.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def create_time(self):
        """Gets the create_time of this ShowCloudPhoneServerDetailResponse.

        创建时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowCloudPhoneServerDetailResponse.

        创建时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ShowCloudPhoneServerDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowCloudPhoneServerDetailResponse.

        更新时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this ShowCloudPhoneServerDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowCloudPhoneServerDetailResponse.

        更新时间， 时间格式为UTC，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this ShowCloudPhoneServerDetailResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowCloudPhoneServerDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
