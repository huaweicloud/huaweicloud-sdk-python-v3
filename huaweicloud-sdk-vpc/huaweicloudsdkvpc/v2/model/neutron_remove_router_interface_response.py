# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronRemoveRouterInterfaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'subnet_id': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'subnet_id': 'subnet_id',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'id': 'id'
    }

    def __init__(self, port_id=None, subnet_id=None, tenant_id=None, project_id=None, id=None):
        """NeutronRemoveRouterInterfaceResponse

        The model defined in huaweicloud sdk

        :param port_id: 路由器添加的端口对应的ID
        :type port_id: str
        :param subnet_id: 路由器添加的子网对应的ID
        :type subnet_id: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param id: 路由器的ID
        :type id: str
        """
        
        super(NeutronRemoveRouterInterfaceResponse, self).__init__()

        self._port_id = None
        self._subnet_id = None
        self._tenant_id = None
        self._project_id = None
        self._id = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if id is not None:
            self.id = id

    @property
    def port_id(self):
        """Gets the port_id of this NeutronRemoveRouterInterfaceResponse.

        路由器添加的端口对应的ID

        :return: The port_id of this NeutronRemoveRouterInterfaceResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NeutronRemoveRouterInterfaceResponse.

        路由器添加的端口对应的ID

        :param port_id: The port_id of this NeutronRemoveRouterInterfaceResponse.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this NeutronRemoveRouterInterfaceResponse.

        路由器添加的子网对应的ID

        :return: The subnet_id of this NeutronRemoveRouterInterfaceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this NeutronRemoveRouterInterfaceResponse.

        路由器添加的子网对应的ID

        :param subnet_id: The subnet_id of this NeutronRemoveRouterInterfaceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronRemoveRouterInterfaceResponse.

        项目ID

        :return: The tenant_id of this NeutronRemoveRouterInterfaceResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronRemoveRouterInterfaceResponse.

        项目ID

        :param tenant_id: The tenant_id of this NeutronRemoveRouterInterfaceResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronRemoveRouterInterfaceResponse.

        项目ID

        :return: The project_id of this NeutronRemoveRouterInterfaceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronRemoveRouterInterfaceResponse.

        项目ID

        :param project_id: The project_id of this NeutronRemoveRouterInterfaceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this NeutronRemoveRouterInterfaceResponse.

        路由器的ID

        :return: The id of this NeutronRemoveRouterInterfaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronRemoveRouterInterfaceResponse.

        路由器的ID

        :param id: The id of this NeutronRemoveRouterInterfaceResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, NeutronRemoveRouterInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
