# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCentralNetworkErRouteTableAttachment:

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
        'enterprise_router_project_id': 'str',
        'enterprise_router_region_id': 'str',
        'central_network_plane_id': 'str',
        'attachment_id': 'str',
        'enterprise_router_table_id': 'str',
        'attached_er_table_project_id': 'str',
        'attached_er_table_region_id': 'str',
        'attached_er_id': 'str',
        'attached_er_table_id': 'str',
        'hosted_cloud': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_router_id': 'enterprise_router_id',
        'enterprise_router_project_id': 'enterprise_router_project_id',
        'enterprise_router_region_id': 'enterprise_router_region_id',
        'central_network_plane_id': 'central_network_plane_id',
        'attachment_id': 'attachment_id',
        'enterprise_router_table_id': 'enterprise_router_table_id',
        'attached_er_table_project_id': 'attached_er_table_project_id',
        'attached_er_table_region_id': 'attached_er_table_region_id',
        'attached_er_id': 'attached_er_id',
        'attached_er_table_id': 'attached_er_table_id',
        'hosted_cloud': 'hosted_cloud'
    }

    def __init__(self, name=None, description=None, enterprise_router_id=None, enterprise_router_project_id=None, enterprise_router_region_id=None, central_network_plane_id=None, attachment_id=None, enterprise_router_table_id=None, attached_er_table_project_id=None, attached_er_table_region_id=None, attached_er_id=None, attached_er_table_id=None, hosted_cloud=None):
        r"""CreateCentralNetworkErRouteTableAttachment

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param enterprise_router_id: 企业路由器的ID。
        :type enterprise_router_id: str
        :param enterprise_router_project_id: 企业路由器的项目ID。
        :type enterprise_router_project_id: str
        :param enterprise_router_region_id: ER路由器的regionID。
        :type enterprise_router_region_id: str
        :param central_network_plane_id: 中心网络平面ID。
        :type central_network_plane_id: str
        :param attachment_id: 中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。
        :type attachment_id: str
        :param enterprise_router_table_id: 企业路由器的路由表ID。
        :type enterprise_router_table_id: str
        :param attached_er_table_project_id: 被挂载的企业路由器的项目ID。
        :type attached_er_table_project_id: str
        :param attached_er_table_region_id: ER路由器的regionID。
        :type attached_er_table_region_id: str
        :param attached_er_id: 被挂载的企业路由器ID。
        :type attached_er_id: str
        :param attached_er_table_id: 被挂载的企业路由器的路由表ID。
        :type attached_er_table_id: str
        :param hosted_cloud: - HWCloud (华为云) - Ireland (爱尔兰)
        :type hosted_cloud: str
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_router_id = None
        self._enterprise_router_project_id = None
        self._enterprise_router_region_id = None
        self._central_network_plane_id = None
        self._attachment_id = None
        self._enterprise_router_table_id = None
        self._attached_er_table_project_id = None
        self._attached_er_table_region_id = None
        self._attached_er_id = None
        self._attached_er_table_id = None
        self._hosted_cloud = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.enterprise_router_id = enterprise_router_id
        self.enterprise_router_project_id = enterprise_router_project_id
        self.enterprise_router_region_id = enterprise_router_region_id
        self.central_network_plane_id = central_network_plane_id
        if attachment_id is not None:
            self.attachment_id = attachment_id
        self.enterprise_router_table_id = enterprise_router_table_id
        self.attached_er_table_project_id = attached_er_table_project_id
        self.attached_er_table_region_id = attached_er_table_region_id
        self.attached_er_id = attached_er_id
        self.attached_er_table_id = attached_er_table_id
        self.hosted_cloud = hosted_cloud

    @property
    def name(self):
        r"""Gets the name of this CreateCentralNetworkErRouteTableAttachment.

        实例名称。

        :return: The name of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCentralNetworkErRouteTableAttachment.

        实例名称。

        :param name: The name of this CreateCentralNetworkErRouteTableAttachment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCentralNetworkErRouteTableAttachment.

        实例描述。不支持 <>。

        :return: The description of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCentralNetworkErRouteTableAttachment.

        实例描述。不支持 <>。

        :param description: The description of this CreateCentralNetworkErRouteTableAttachment.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_router_id(self):
        r"""Gets the enterprise_router_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的ID。

        :return: The enterprise_router_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_id

    @enterprise_router_id.setter
    def enterprise_router_id(self, enterprise_router_id):
        r"""Sets the enterprise_router_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的ID。

        :param enterprise_router_id: The enterprise_router_id of this CreateCentralNetworkErRouteTableAttachment.
        :type enterprise_router_id: str
        """
        self._enterprise_router_id = enterprise_router_id

    @property
    def enterprise_router_project_id(self):
        r"""Gets the enterprise_router_project_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的项目ID。

        :return: The enterprise_router_project_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_project_id

    @enterprise_router_project_id.setter
    def enterprise_router_project_id(self, enterprise_router_project_id):
        r"""Sets the enterprise_router_project_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的项目ID。

        :param enterprise_router_project_id: The enterprise_router_project_id of this CreateCentralNetworkErRouteTableAttachment.
        :type enterprise_router_project_id: str
        """
        self._enterprise_router_project_id = enterprise_router_project_id

    @property
    def enterprise_router_region_id(self):
        r"""Gets the enterprise_router_region_id of this CreateCentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :return: The enterprise_router_region_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_region_id

    @enterprise_router_region_id.setter
    def enterprise_router_region_id(self, enterprise_router_region_id):
        r"""Sets the enterprise_router_region_id of this CreateCentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :param enterprise_router_region_id: The enterprise_router_region_id of this CreateCentralNetworkErRouteTableAttachment.
        :type enterprise_router_region_id: str
        """
        self._enterprise_router_region_id = enterprise_router_region_id

    @property
    def central_network_plane_id(self):
        r"""Gets the central_network_plane_id of this CreateCentralNetworkErRouteTableAttachment.

        中心网络平面ID。

        :return: The central_network_plane_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        r"""Sets the central_network_plane_id of this CreateCentralNetworkErRouteTableAttachment.

        中心网络平面ID。

        :param central_network_plane_id: The central_network_plane_id of this CreateCentralNetworkErRouteTableAttachment.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this CreateCentralNetworkErRouteTableAttachment.

        中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。

        :return: The attachment_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this CreateCentralNetworkErRouteTableAttachment.

        中心网络附件对端实例的连接ID，企业路由器的连接ID或者GDGW的连接ID。

        :param attachment_id: The attachment_id of this CreateCentralNetworkErRouteTableAttachment.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def enterprise_router_table_id(self):
        r"""Gets the enterprise_router_table_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的路由表ID。

        :return: The enterprise_router_table_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._enterprise_router_table_id

    @enterprise_router_table_id.setter
    def enterprise_router_table_id(self, enterprise_router_table_id):
        r"""Sets the enterprise_router_table_id of this CreateCentralNetworkErRouteTableAttachment.

        企业路由器的路由表ID。

        :param enterprise_router_table_id: The enterprise_router_table_id of this CreateCentralNetworkErRouteTableAttachment.
        :type enterprise_router_table_id: str
        """
        self._enterprise_router_table_id = enterprise_router_table_id

    @property
    def attached_er_table_project_id(self):
        r"""Gets the attached_er_table_project_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的项目ID。

        :return: The attached_er_table_project_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_project_id

    @attached_er_table_project_id.setter
    def attached_er_table_project_id(self, attached_er_table_project_id):
        r"""Sets the attached_er_table_project_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的项目ID。

        :param attached_er_table_project_id: The attached_er_table_project_id of this CreateCentralNetworkErRouteTableAttachment.
        :type attached_er_table_project_id: str
        """
        self._attached_er_table_project_id = attached_er_table_project_id

    @property
    def attached_er_table_region_id(self):
        r"""Gets the attached_er_table_region_id of this CreateCentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :return: The attached_er_table_region_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_region_id

    @attached_er_table_region_id.setter
    def attached_er_table_region_id(self, attached_er_table_region_id):
        r"""Sets the attached_er_table_region_id of this CreateCentralNetworkErRouteTableAttachment.

        ER路由器的regionID。

        :param attached_er_table_region_id: The attached_er_table_region_id of this CreateCentralNetworkErRouteTableAttachment.
        :type attached_er_table_region_id: str
        """
        self._attached_er_table_region_id = attached_er_table_region_id

    @property
    def attached_er_id(self):
        r"""Gets the attached_er_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器ID。

        :return: The attached_er_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_id

    @attached_er_id.setter
    def attached_er_id(self, attached_er_id):
        r"""Sets the attached_er_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器ID。

        :param attached_er_id: The attached_er_id of this CreateCentralNetworkErRouteTableAttachment.
        :type attached_er_id: str
        """
        self._attached_er_id = attached_er_id

    @property
    def attached_er_table_id(self):
        r"""Gets the attached_er_table_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的路由表ID。

        :return: The attached_er_table_id of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._attached_er_table_id

    @attached_er_table_id.setter
    def attached_er_table_id(self, attached_er_table_id):
        r"""Sets the attached_er_table_id of this CreateCentralNetworkErRouteTableAttachment.

        被挂载的企业路由器的路由表ID。

        :param attached_er_table_id: The attached_er_table_id of this CreateCentralNetworkErRouteTableAttachment.
        :type attached_er_table_id: str
        """
        self._attached_er_table_id = attached_er_table_id

    @property
    def hosted_cloud(self):
        r"""Gets the hosted_cloud of this CreateCentralNetworkErRouteTableAttachment.

        - HWCloud (华为云) - Ireland (爱尔兰)

        :return: The hosted_cloud of this CreateCentralNetworkErRouteTableAttachment.
        :rtype: str
        """
        return self._hosted_cloud

    @hosted_cloud.setter
    def hosted_cloud(self, hosted_cloud):
        r"""Sets the hosted_cloud of this CreateCentralNetworkErRouteTableAttachment.

        - HWCloud (华为云) - Ireland (爱尔兰)

        :param hosted_cloud: The hosted_cloud of this CreateCentralNetworkErRouteTableAttachment.
        :type hosted_cloud: str
        """
        self._hosted_cloud = hosted_cloud

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
        if not isinstance(other, CreateCentralNetworkErRouteTableAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
