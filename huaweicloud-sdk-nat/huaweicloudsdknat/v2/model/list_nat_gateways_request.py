# coding: utf-8

import pprint
import re

import six





class ListNatGatewaysRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'id': 'str',
        'enterprise_project_id': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'status': 'list[str]',
        'spec': 'list[str]',
        'admin_state_up': 'bool',
        'internal_network_id': 'str',
        'router_id': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'created_at': 'created_at',
        'name': 'name',
        'status': 'status',
        'spec': 'spec',
        'admin_state_up': 'admin_state_up',
        'internal_network_id': 'internal_network_id',
        'router_id': 'router_id',
        'limit': 'limit'
    }

    def __init__(self, tenant_id=None, id=None, enterprise_project_id=None, description=None, created_at=None, name=None, status=None, spec=None, admin_state_up=None, internal_network_id=None, router_id=None, limit=2000):
        """ListNatGatewaysRequest - a model defined in huaweicloud sdk"""
        
        

        self._tenant_id = None
        self._id = None
        self._enterprise_project_id = None
        self._description = None
        self._created_at = None
        self._name = None
        self._status = None
        self._spec = None
        self._admin_state_up = None
        self._internal_network_id = None
        self._router_id = None
        self._limit = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if spec is not None:
            self.spec = spec
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if internal_network_id is not None:
            self.internal_network_id = internal_network_id
        if router_id is not None:
            self.router_id = router_id
        if limit is not None:
            self.limit = limit

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListNatGatewaysRequest.


        :return: The tenant_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListNatGatewaysRequest.


        :param tenant_id: The tenant_id of this ListNatGatewaysRequest.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this ListNatGatewaysRequest.


        :return: The id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListNatGatewaysRequest.


        :param id: The id of this ListNatGatewaysRequest.
        :type: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListNatGatewaysRequest.


        :return: The enterprise_project_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListNatGatewaysRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListNatGatewaysRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        """Gets the description of this ListNatGatewaysRequest.


        :return: The description of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListNatGatewaysRequest.


        :param description: The description of this ListNatGatewaysRequest.
        :type: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ListNatGatewaysRequest.


        :return: The created_at of this ListNatGatewaysRequest.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListNatGatewaysRequest.


        :param created_at: The created_at of this ListNatGatewaysRequest.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this ListNatGatewaysRequest.


        :return: The name of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListNatGatewaysRequest.


        :param name: The name of this ListNatGatewaysRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListNatGatewaysRequest.


        :return: The status of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListNatGatewaysRequest.


        :param status: The status of this ListNatGatewaysRequest.
        :type: list[str]
        """
        self._status = status

    @property
    def spec(self):
        """Gets the spec of this ListNatGatewaysRequest.


        :return: The spec of this ListNatGatewaysRequest.
        :rtype: list[str]
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ListNatGatewaysRequest.


        :param spec: The spec of this ListNatGatewaysRequest.
        :type: list[str]
        """
        self._spec = spec

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListNatGatewaysRequest.


        :return: The admin_state_up of this ListNatGatewaysRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListNatGatewaysRequest.


        :param admin_state_up: The admin_state_up of this ListNatGatewaysRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def internal_network_id(self):
        """Gets the internal_network_id of this ListNatGatewaysRequest.


        :return: The internal_network_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        """Sets the internal_network_id of this ListNatGatewaysRequest.


        :param internal_network_id: The internal_network_id of this ListNatGatewaysRequest.
        :type: str
        """
        self._internal_network_id = internal_network_id

    @property
    def router_id(self):
        """Gets the router_id of this ListNatGatewaysRequest.


        :return: The router_id of this ListNatGatewaysRequest.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this ListNatGatewaysRequest.


        :param router_id: The router_id of this ListNatGatewaysRequest.
        :type: str
        """
        self._router_id = router_id

    @property
    def limit(self):
        """Gets the limit of this ListNatGatewaysRequest.


        :return: The limit of this ListNatGatewaysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNatGatewaysRequest.


        :param limit: The limit of this ListNatGatewaysRequest.
        :type: int
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNatGatewaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
