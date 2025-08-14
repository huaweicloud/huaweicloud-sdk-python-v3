# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServices:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'data_volumes': 'list[Volume]',
        'nics': 'list[Nic]',
        'ou_name': 'str',
        'product_id': 'str',
        'flavor_id': 'str',
        'os_type': 'str',
        'root_volume': 'Volume',
        'server_group_id': 'str',
        'service_type': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'security_groups': 'list[SecurityGroup]',
        'update_access_agent': 'bool'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'data_volumes': 'data_volumes',
        'nics': 'nics',
        'ou_name': 'ou_name',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'os_type': 'os_type',
        'root_volume': 'root_volume',
        'server_group_id': 'server_group_id',
        'service_type': 'service_type',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'security_groups': 'security_groups',
        'update_access_agent': 'update_access_agent'
    }

    def __init__(self, availability_zone=None, data_volumes=None, nics=None, ou_name=None, product_id=None, flavor_id=None, os_type=None, root_volume=None, server_group_id=None, service_type=None, subnet_id=None, vpc_id=None, security_groups=None, update_access_agent=None):
        r"""CreateServices

        The model defined in huaweicloud sdk

        :param availability_zone: 可用分区。 &gt; - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 &gt; - 获取方式详见可用区管理ListAvailabilityZone：\&quot;GET  /v1/{project_id}/availability-zone\&quot;。
        :type availability_zone: str
        :param data_volumes: 数据盘。
        :type data_volumes: list[:class:`huaweicloudsdkworkspaceapp.v1.Volume`]
        :param nics: 网卡信息，该字段当前未使用。
        :type nics: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        :param ou_name: OU名称，在对接AD时使用，需提前在AD中创建OU。
        :type ou_name: str
        :param product_id: 产品ID。 &gt; - 获取方式详见产品套餐管理ListProduct：\&quot;GET  /v1/{project_id}/product\&quot;。
        :type product_id: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param os_type: 操作系统类型，当前仅支持Windows - Linux - Windows
        :type os_type: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        :param server_group_id: 服务器组ID, 云应用创建服务组时生成。
        :type server_group_id: str
        :param service_type: 云服务类型，云桌面固定为DEDICATED。
        :type service_type: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param vpc_id: 自动开户的时候,用于LiteAs第一次开户传进来。
        :type vpc_id: str
        :param security_groups: 服务器使用的安全组，如果不指定则默认使用服务器代理中指定的安全组。 **⚠ 警告: 预留属性，目前未使用**
        :type security_groups: list[:class:`huaweicloudsdkworkspaceapp.v1.SecurityGroup`]
        :param update_access_agent: 是否自动升级hda版本。
        :type update_access_agent: bool
        """
        
        

        self._availability_zone = None
        self._data_volumes = None
        self._nics = None
        self._ou_name = None
        self._product_id = None
        self._flavor_id = None
        self._os_type = None
        self._root_volume = None
        self._server_group_id = None
        self._service_type = None
        self._subnet_id = None
        self._vpc_id = None
        self._security_groups = None
        self._update_access_agent = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if nics is not None:
            self.nics = nics
        if ou_name is not None:
            self.ou_name = ou_name
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if os_type is not None:
            self.os_type = os_type
        self.root_volume = root_volume
        self.server_group_id = server_group_id
        if service_type is not None:
            self.service_type = service_type
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        if security_groups is not None:
            self.security_groups = security_groups
        if update_access_agent is not None:
            self.update_access_agent = update_access_agent

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateServices.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :return: The availability_zone of this CreateServices.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateServices.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :param availability_zone: The availability_zone of this CreateServices.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this CreateServices.

        数据盘。

        :return: The data_volumes of this CreateServices.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this CreateServices.

        数据盘。

        :param data_volumes: The data_volumes of this CreateServices.
        :type data_volumes: list[:class:`huaweicloudsdkworkspaceapp.v1.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def nics(self):
        r"""Gets the nics of this CreateServices.

        网卡信息，该字段当前未使用。

        :return: The nics of this CreateServices.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this CreateServices.

        网卡信息，该字段当前未使用。

        :param nics: The nics of this CreateServices.
        :type nics: list[:class:`huaweicloudsdkworkspaceapp.v1.Nic`]
        """
        self._nics = nics

    @property
    def ou_name(self):
        r"""Gets the ou_name of this CreateServices.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :return: The ou_name of this CreateServices.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this CreateServices.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :param ou_name: The ou_name of this CreateServices.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateServices.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET  /v1/{project_id}/product\"。

        :return: The product_id of this CreateServices.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateServices.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET  /v1/{project_id}/product\"。

        :param product_id: The product_id of this CreateServices.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateServices.

        规格ID。

        :return: The flavor_id of this CreateServices.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateServices.

        规格ID。

        :param flavor_id: The flavor_id of this CreateServices.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def os_type(self):
        r"""Gets the os_type of this CreateServices.

        操作系统类型，当前仅支持Windows - Linux - Windows

        :return: The os_type of this CreateServices.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CreateServices.

        操作系统类型，当前仅支持Windows - Linux - Windows

        :param os_type: The os_type of this CreateServices.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def root_volume(self):
        r"""Gets the root_volume of this CreateServices.

        :return: The root_volume of this CreateServices.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this CreateServices.

        :param root_volume: The root_volume of this CreateServices.
        :type root_volume: :class:`huaweicloudsdkworkspaceapp.v1.Volume`
        """
        self._root_volume = root_volume

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this CreateServices.

        服务器组ID, 云应用创建服务组时生成。

        :return: The server_group_id of this CreateServices.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this CreateServices.

        服务器组ID, 云应用创建服务组时生成。

        :param server_group_id: The server_group_id of this CreateServices.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def service_type(self):
        r"""Gets the service_type of this CreateServices.

        云服务类型，云桌面固定为DEDICATED。

        :return: The service_type of this CreateServices.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CreateServices.

        云服务类型，云桌面固定为DEDICATED。

        :param service_type: The service_type of this CreateServices.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateServices.

        子网ID。

        :return: The subnet_id of this CreateServices.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateServices.

        子网ID。

        :param subnet_id: The subnet_id of this CreateServices.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateServices.

        自动开户的时候,用于LiteAs第一次开户传进来。

        :return: The vpc_id of this CreateServices.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateServices.

        自动开户的时候,用于LiteAs第一次开户传进来。

        :param vpc_id: The vpc_id of this CreateServices.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CreateServices.

        服务器使用的安全组，如果不指定则默认使用服务器代理中指定的安全组。 **⚠ 警告: 预留属性，目前未使用**

        :return: The security_groups of this CreateServices.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CreateServices.

        服务器使用的安全组，如果不指定则默认使用服务器代理中指定的安全组。 **⚠ 警告: 预留属性，目前未使用**

        :param security_groups: The security_groups of this CreateServices.
        :type security_groups: list[:class:`huaweicloudsdkworkspaceapp.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def update_access_agent(self):
        r"""Gets the update_access_agent of this CreateServices.

        是否自动升级hda版本。

        :return: The update_access_agent of this CreateServices.
        :rtype: bool
        """
        return self._update_access_agent

    @update_access_agent.setter
    def update_access_agent(self, update_access_agent):
        r"""Sets the update_access_agent of this CreateServices.

        是否自动升级hda版本。

        :param update_access_agent: The update_access_agent of this CreateServices.
        :type update_access_agent: bool
        """
        self._update_access_agent = update_access_agent

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
        if not isinstance(other, CreateServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
