# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCentralNetworkGdgwAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'enterprise_router_id': 'str',
        'global_dc_gateway_id': 'str',
        'global_dc_gateway_project_id': 'str',
        'global_dc_gateway_region_id': 'str',
        'enterprise_router_project_id': 'str',
        'enterprise_router_region_id': 'str',
        'central_network_plane_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_router_id': 'enterprise_router_id',
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'global_dc_gateway_project_id': 'global_dc_gateway_project_id',
        'global_dc_gateway_region_id': 'global_dc_gateway_region_id',
        'enterprise_router_project_id': 'enterprise_router_project_id',
        'enterprise_router_region_id': 'enterprise_router_region_id',
        'central_network_plane_id': 'central_network_plane_id'
    }

    def __init__(self, name=None, description=None, enterprise_router_id=None, global_dc_gateway_id=None, global_dc_gateway_project_id=None, global_dc_gateway_region_id=None, enterprise_router_project_id=None, enterprise_router_region_id=None, central_network_plane_id=None):
        r"""CreateCentralNetworkGdgwAttachment

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param enterprise_router_id: 企业路由器的ID。
        :type enterprise_router_id: str
        :param global_dc_gateway_id: Gdgw的ID。
        :type global_dc_gateway_id: str
        :param global_dc_gateway_project_id: Gdgw的项目ID。
        :type global_dc_gateway_project_id: str
        :param global_dc_gateway_region_id: Gdgw的RegionID。
        :type global_dc_gateway_region_id: str
        :param enterprise_router_project_id: 企业路由器的项目ID。
        :type enterprise_router_project_id: str
        :param enterprise_router_region_id: ER路由器的regionID。
        :type enterprise_router_region_id: str
        :param central_network_plane_id: 中心网络平面ID。
        :type central_network_plane_id: str
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_router_id = None
        self._global_dc_gateway_id = None
        self._global_dc_gateway_project_id = None
        self._global_dc_gateway_region_id = None
        self._enterprise_router_project_id = None
        self._enterprise_router_region_id = None
        self._central_network_plane_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.enterprise_router_id = enterprise_router_id
        self.global_dc_gateway_id = global_dc_gateway_id
        self.global_dc_gateway_project_id = global_dc_gateway_project_id
        self.global_dc_gateway_region_id = global_dc_gateway_region_id
        self.enterprise_router_project_id = enterprise_router_project_id
        self.enterprise_router_region_id = enterprise_router_region_id
        if central_network_plane_id is not None:
            self.central_network_plane_id = central_network_plane_id

    @property
    def name(self):
        r"""Gets the name of this CreateCentralNetworkGdgwAttachment.

        实例名称。

        :return: The name of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCentralNetworkGdgwAttachment.

        实例名称。

        :param name: The name of this CreateCentralNetworkGdgwAttachment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCentralNetworkGdgwAttachment.

        实例描述。不支持 <>。

        :return: The description of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCentralNetworkGdgwAttachment.

        实例描述。不支持 <>。

        :param description: The description of this CreateCentralNetworkGdgwAttachment.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this CreateCentralNetworkGdgwAttachment.

        企业路由器的ID。

        :return: The enterprise_router_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this CreateCentralNetworkGdgwAttachment.

        企业路由器的ID。

        :param enterprise_router_id: The enterprise_router_id of this CreateCentralNetworkGdgwAttachment.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def global_dc_gateway_id(self):
        r"""Gets the global_dc_gateway_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的ID。

        :return: The global_dc_gateway_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        r"""Sets the global_dc_gateway_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的ID。

        :param global_dc_gateway_id: The global_dc_gateway_id of this CreateCentralNetworkGdgwAttachment.
        :type global_dc_gateway_id: str
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def global_dc_gateway_project_id(self):
        r"""Gets the global_dc_gateway_project_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的项目ID。

        :return: The global_dc_gateway_project_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_project_id

    @global_dc_gateway_project_id.setter
    def global_dc_gateway_project_id(self, global_dc_gateway_project_id):
        r"""Sets the global_dc_gateway_project_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的项目ID。

        :param global_dc_gateway_project_id: The global_dc_gateway_project_id of this CreateCentralNetworkGdgwAttachment.
        :type global_dc_gateway_project_id: str
        """
        self._global_dc_gateway_project_id = global_dc_gateway_project_id

    @property
    def global_dc_gateway_region_id(self):
        r"""Gets the global_dc_gateway_region_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的RegionID。

        :return: The global_dc_gateway_region_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._global_dc_gateway_region_id

    @global_dc_gateway_region_id.setter
    def global_dc_gateway_region_id(self, global_dc_gateway_region_id):
        r"""Sets the global_dc_gateway_region_id of this CreateCentralNetworkGdgwAttachment.

        Gdgw的RegionID。

        :param global_dc_gateway_region_id: The global_dc_gateway_region_id of this CreateCentralNetworkGdgwAttachment.
        :type global_dc_gateway_region_id: str
        """
        self._global_dc_gateway_region_id = global_dc_gateway_region_id

    @property
    def enterprise_router_project_id(self):
        r"""Gets the enterprise_router_project_id of this CreateCentralNetworkGdgwAttachment.

        企业路由器的项目ID。

        :return: The enterprise_router_project_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_project_id

    @enterprise_router_project_id.setter
    def enterprise_router_project_id(self, enterprise_router_project_id):
        r"""Sets the enterprise_router_project_id of this CreateCentralNetworkGdgwAttachment.

        企业路由器的项目ID。

        :param enterprise_router_project_id: The enterprise_router_project_id of this CreateCentralNetworkGdgwAttachment.
        :type enterprise_router_project_id: str
        """
        self._enterprise_router_project_id = enterprise_router_project_id

    @property
    def enterprise_router_region_id(self):
        r"""Gets the enterprise_router_region_id of this CreateCentralNetworkGdgwAttachment.

        ER路由器的regionID。

        :return: The enterprise_router_region_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._enterprise_router_region_id

    @enterprise_router_region_id.setter
    def enterprise_router_region_id(self, enterprise_router_region_id):
        r"""Sets the enterprise_router_region_id of this CreateCentralNetworkGdgwAttachment.

        ER路由器的regionID。

        :param enterprise_router_region_id: The enterprise_router_region_id of this CreateCentralNetworkGdgwAttachment.
        :type enterprise_router_region_id: str
        """
        self._enterprise_router_region_id = enterprise_router_region_id

    @property
    def central_network_plane_id(self):
        r"""Gets the central_network_plane_id of this CreateCentralNetworkGdgwAttachment.

        中心网络平面ID。

        :return: The central_network_plane_id of this CreateCentralNetworkGdgwAttachment.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        r"""Sets the central_network_plane_id of this CreateCentralNetworkGdgwAttachment.

        中心网络平面ID。

        :param central_network_plane_id: The central_network_plane_id of this CreateCentralNetworkGdgwAttachment.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

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
        if not isinstance(other, CreateCentralNetworkGdgwAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
