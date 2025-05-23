# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcIgwsTenantResp:

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
        'project_id': 'str',
        'vpc_id': 'str',
        'name': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'network_id': 'str',
        'enable_ipv6': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'vpc_id': 'vpc_id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'network_id': 'network_id',
        'enable_ipv6': 'enable_ipv6'
    }

    def __init__(self, id=None, project_id=None, vpc_id=None, name=None, created_at=None, updated_at=None, network_id=None, enable_ipv6=None):
        r"""VpcIgwsTenantResp

        The model defined in huaweicloud sdk

        :param id: 虚拟IGW的uuid
        :type id: str
        :param project_id: 虚拟IGW的租户id
        :type project_id: str
        :param vpc_id: 虚拟IGW的vpcid
        :type vpc_id: str
        :param name: 虚拟IGW的名称
        :type name: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param network_id: 创建IGW使用的VPC具体子网
        :type network_id: str
        :param enable_ipv6: 是否使能IPV6
        :type enable_ipv6: bool
        """
        
        

        self._id = None
        self._project_id = None
        self._vpc_id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._network_id = None
        self._enable_ipv6 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if network_id is not None:
            self.network_id = network_id
        if enable_ipv6 is not None:
            self.enable_ipv6 = enable_ipv6

    @property
    def id(self):
        r"""Gets the id of this VpcIgwsTenantResp.

        虚拟IGW的uuid

        :return: The id of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcIgwsTenantResp.

        虚拟IGW的uuid

        :param id: The id of this VpcIgwsTenantResp.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this VpcIgwsTenantResp.

        虚拟IGW的租户id

        :return: The project_id of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VpcIgwsTenantResp.

        虚拟IGW的租户id

        :param project_id: The project_id of this VpcIgwsTenantResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VpcIgwsTenantResp.

        虚拟IGW的vpcid

        :return: The vpc_id of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VpcIgwsTenantResp.

        虚拟IGW的vpcid

        :param vpc_id: The vpc_id of this VpcIgwsTenantResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this VpcIgwsTenantResp.

        虚拟IGW的名称

        :return: The name of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpcIgwsTenantResp.

        虚拟IGW的名称

        :param name: The name of this VpcIgwsTenantResp.
        :type name: str
        """
        self._name = name

    @property
    def created_at(self):
        r"""Gets the created_at of this VpcIgwsTenantResp.

        创建时间

        :return: The created_at of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this VpcIgwsTenantResp.

        创建时间

        :param created_at: The created_at of this VpcIgwsTenantResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this VpcIgwsTenantResp.

        更新时间

        :return: The updated_at of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this VpcIgwsTenantResp.

        更新时间

        :param updated_at: The updated_at of this VpcIgwsTenantResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def network_id(self):
        r"""Gets the network_id of this VpcIgwsTenantResp.

        创建IGW使用的VPC具体子网

        :return: The network_id of this VpcIgwsTenantResp.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this VpcIgwsTenantResp.

        创建IGW使用的VPC具体子网

        :param network_id: The network_id of this VpcIgwsTenantResp.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def enable_ipv6(self):
        r"""Gets the enable_ipv6 of this VpcIgwsTenantResp.

        是否使能IPV6

        :return: The enable_ipv6 of this VpcIgwsTenantResp.
        :rtype: bool
        """
        return self._enable_ipv6

    @enable_ipv6.setter
    def enable_ipv6(self, enable_ipv6):
        r"""Sets the enable_ipv6 of this VpcIgwsTenantResp.

        是否使能IPV6

        :param enable_ipv6: The enable_ipv6 of this VpcIgwsTenantResp.
        :type enable_ipv6: bool
        """
        self._enable_ipv6 = enable_ipv6

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
        if not isinstance(other, VpcIgwsTenantResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
