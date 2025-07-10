# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'vpc_name': 'str',
        'subnet_ids': 'list[str]',
        'management_subnet_cidr': 'str',
        'management_node_subnet_id': 'str',
        'vpc_config_infos': 'list[VpcConfigInfo]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'subnet_ids': 'subnet_ids',
        'management_subnet_cidr': 'management_subnet_cidr',
        'management_node_subnet_id': 'management_node_subnet_id',
        'vpc_config_infos': 'vpc_config_infos'
    }

    def __init__(self, vpc_id=None, vpc_name=None, subnet_ids=None, management_subnet_cidr=None, management_node_subnet_id=None, vpc_config_infos=None):
        r"""NetworkConfig

        The model defined in huaweicloud sdk

        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param vpc_name: VPC名称。
        :type vpc_name: str
        :param subnet_ids: 业务子网，可以指定返回的网络ID订购桌面。
        :type subnet_ids: list[str]
        :param management_subnet_cidr: 后端管理组件占用的子网网段。
        :type management_subnet_cidr: str
        :param management_node_subnet_id: subnet_ids所返回的业务子网中,被管理节点所占用的子网id。
        :type management_node_subnet_id: str
        :param vpc_config_infos: VPC配置信息列表。
        :type vpc_config_infos: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        
        

        self._vpc_id = None
        self._vpc_name = None
        self._subnet_ids = None
        self._management_subnet_cidr = None
        self._management_node_subnet_id = None
        self._vpc_config_infos = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if management_subnet_cidr is not None:
            self.management_subnet_cidr = management_subnet_cidr
        if management_node_subnet_id is not None:
            self.management_node_subnet_id = management_node_subnet_id
        if vpc_config_infos is not None:
            self.vpc_config_infos = vpc_config_infos

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this NetworkConfig.

        VPC ID。

        :return: The vpc_id of this NetworkConfig.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this NetworkConfig.

        VPC ID。

        :param vpc_id: The vpc_id of this NetworkConfig.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this NetworkConfig.

        VPC名称。

        :return: The vpc_name of this NetworkConfig.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this NetworkConfig.

        VPC名称。

        :param vpc_name: The vpc_name of this NetworkConfig.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_ids(self):
        r"""Gets the subnet_ids of this NetworkConfig.

        业务子网，可以指定返回的网络ID订购桌面。

        :return: The subnet_ids of this NetworkConfig.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        r"""Sets the subnet_ids of this NetworkConfig.

        业务子网，可以指定返回的网络ID订购桌面。

        :param subnet_ids: The subnet_ids of this NetworkConfig.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def management_subnet_cidr(self):
        r"""Gets the management_subnet_cidr of this NetworkConfig.

        后端管理组件占用的子网网段。

        :return: The management_subnet_cidr of this NetworkConfig.
        :rtype: str
        """
        return self._management_subnet_cidr

    @management_subnet_cidr.setter
    def management_subnet_cidr(self, management_subnet_cidr):
        r"""Sets the management_subnet_cidr of this NetworkConfig.

        后端管理组件占用的子网网段。

        :param management_subnet_cidr: The management_subnet_cidr of this NetworkConfig.
        :type management_subnet_cidr: str
        """
        self._management_subnet_cidr = management_subnet_cidr

    @property
    def management_node_subnet_id(self):
        r"""Gets the management_node_subnet_id of this NetworkConfig.

        subnet_ids所返回的业务子网中,被管理节点所占用的子网id。

        :return: The management_node_subnet_id of this NetworkConfig.
        :rtype: str
        """
        return self._management_node_subnet_id

    @management_node_subnet_id.setter
    def management_node_subnet_id(self, management_node_subnet_id):
        r"""Sets the management_node_subnet_id of this NetworkConfig.

        subnet_ids所返回的业务子网中,被管理节点所占用的子网id。

        :param management_node_subnet_id: The management_node_subnet_id of this NetworkConfig.
        :type management_node_subnet_id: str
        """
        self._management_node_subnet_id = management_node_subnet_id

    @property
    def vpc_config_infos(self):
        r"""Gets the vpc_config_infos of this NetworkConfig.

        VPC配置信息列表。

        :return: The vpc_config_infos of this NetworkConfig.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        return self._vpc_config_infos

    @vpc_config_infos.setter
    def vpc_config_infos(self, vpc_config_infos):
        r"""Sets the vpc_config_infos of this NetworkConfig.

        VPC配置信息列表。

        :param vpc_config_infos: The vpc_config_infos of this NetworkConfig.
        :type vpc_config_infos: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        self._vpc_config_infos = vpc_config_infos

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
        if not isinstance(other, NetworkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
