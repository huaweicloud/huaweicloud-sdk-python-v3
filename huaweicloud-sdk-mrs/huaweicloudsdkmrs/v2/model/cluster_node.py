# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'resource_id': 'str',
        'node_group_name': 'str',
        'node_type': 'str',
        'billing_type': 'str',
        'deployment_type': 'str',
        'server_info': 'ServerInfo',
        'tags': 'list[Tag]',
        'node_detail': 'NodeDetail',
        'node_status': 'str',
        'component_infos': 'list[ComponentInfo]'
    }

    attribute_map = {
        'node_name': 'node_name',
        'resource_id': 'resource_id',
        'node_group_name': 'node_group_name',
        'node_type': 'node_type',
        'billing_type': 'billing_type',
        'deployment_type': 'deployment_type',
        'server_info': 'server_info',
        'tags': 'tags',
        'node_detail': 'node_detail',
        'node_status': 'node_status',
        'component_infos': 'component_infos'
    }

    def __init__(self, node_name=None, resource_id=None, node_group_name=None, node_type=None, billing_type=None, deployment_type=None, server_info=None, tags=None, node_detail=None, node_status=None, component_infos=None):
        r"""ClusterNode

        The model defined in huaweicloud sdk

        :param node_name: 节点名称，对应manager里的节点名称。
        :type node_name: str
        :param resource_id: 资源id。确定节点的唯一性，包周期节点可用于计费的查询。
        :type resource_id: str
        :param node_group_name: 节点组名称。
        :type node_group_name: str
        :param node_type: 节点类型。Task、Core、Master等。
        :type node_type: str
        :param billing_type: on-period包周期或者on-quantity按需。
        :type billing_type: str
        :param deployment_type: 部署类型。支持Server主机类型。
        :type deployment_type: str
        :param server_info: 
        :type server_info: :class:`huaweicloudsdkmrs.v2.ServerInfo`
        :param tags: 节点标签
        :type tags: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        :param node_detail: 
        :type node_detail: :class:`huaweicloudsdkmrs.v2.NodeDetail`
        :param node_status: 节点状态。对应页面上的操作状态。
        :type node_status: str
        :param component_infos: 组件实例信息数组。
        :type component_infos: list[:class:`huaweicloudsdkmrs.v2.ComponentInfo`]
        """
        
        

        self._node_name = None
        self._resource_id = None
        self._node_group_name = None
        self._node_type = None
        self._billing_type = None
        self._deployment_type = None
        self._server_info = None
        self._tags = None
        self._node_detail = None
        self._node_status = None
        self._component_infos = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if resource_id is not None:
            self.resource_id = resource_id
        if node_group_name is not None:
            self.node_group_name = node_group_name
        if node_type is not None:
            self.node_type = node_type
        if billing_type is not None:
            self.billing_type = billing_type
        self.deployment_type = deployment_type
        if server_info is not None:
            self.server_info = server_info
        if tags is not None:
            self.tags = tags
        if node_detail is not None:
            self.node_detail = node_detail
        if node_status is not None:
            self.node_status = node_status
        if component_infos is not None:
            self.component_infos = component_infos

    @property
    def node_name(self):
        r"""Gets the node_name of this ClusterNode.

        节点名称，对应manager里的节点名称。

        :return: The node_name of this ClusterNode.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ClusterNode.

        节点名称，对应manager里的节点名称。

        :param node_name: The node_name of this ClusterNode.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ClusterNode.

        资源id。确定节点的唯一性，包周期节点可用于计费的查询。

        :return: The resource_id of this ClusterNode.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ClusterNode.

        资源id。确定节点的唯一性，包周期节点可用于计费的查询。

        :param resource_id: The resource_id of this ClusterNode.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def node_group_name(self):
        r"""Gets the node_group_name of this ClusterNode.

        节点组名称。

        :return: The node_group_name of this ClusterNode.
        :rtype: str
        """
        return self._node_group_name

    @node_group_name.setter
    def node_group_name(self, node_group_name):
        r"""Sets the node_group_name of this ClusterNode.

        节点组名称。

        :param node_group_name: The node_group_name of this ClusterNode.
        :type node_group_name: str
        """
        self._node_group_name = node_group_name

    @property
    def node_type(self):
        r"""Gets the node_type of this ClusterNode.

        节点类型。Task、Core、Master等。

        :return: The node_type of this ClusterNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ClusterNode.

        节点类型。Task、Core、Master等。

        :param node_type: The node_type of this ClusterNode.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def billing_type(self):
        r"""Gets the billing_type of this ClusterNode.

        on-period包周期或者on-quantity按需。

        :return: The billing_type of this ClusterNode.
        :rtype: str
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        r"""Sets the billing_type of this ClusterNode.

        on-period包周期或者on-quantity按需。

        :param billing_type: The billing_type of this ClusterNode.
        :type billing_type: str
        """
        self._billing_type = billing_type

    @property
    def deployment_type(self):
        r"""Gets the deployment_type of this ClusterNode.

        部署类型。支持Server主机类型。

        :return: The deployment_type of this ClusterNode.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        r"""Sets the deployment_type of this ClusterNode.

        部署类型。支持Server主机类型。

        :param deployment_type: The deployment_type of this ClusterNode.
        :type deployment_type: str
        """
        self._deployment_type = deployment_type

    @property
    def server_info(self):
        r"""Gets the server_info of this ClusterNode.

        :return: The server_info of this ClusterNode.
        :rtype: :class:`huaweicloudsdkmrs.v2.ServerInfo`
        """
        return self._server_info

    @server_info.setter
    def server_info(self, server_info):
        r"""Sets the server_info of this ClusterNode.

        :param server_info: The server_info of this ClusterNode.
        :type server_info: :class:`huaweicloudsdkmrs.v2.ServerInfo`
        """
        self._server_info = server_info

    @property
    def tags(self):
        r"""Gets the tags of this ClusterNode.

        节点标签

        :return: The tags of this ClusterNode.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ClusterNode.

        节点标签

        :param tags: The tags of this ClusterNode.
        :type tags: list[:class:`huaweicloudsdkmrs.v2.Tag`]
        """
        self._tags = tags

    @property
    def node_detail(self):
        r"""Gets the node_detail of this ClusterNode.

        :return: The node_detail of this ClusterNode.
        :rtype: :class:`huaweicloudsdkmrs.v2.NodeDetail`
        """
        return self._node_detail

    @node_detail.setter
    def node_detail(self, node_detail):
        r"""Sets the node_detail of this ClusterNode.

        :param node_detail: The node_detail of this ClusterNode.
        :type node_detail: :class:`huaweicloudsdkmrs.v2.NodeDetail`
        """
        self._node_detail = node_detail

    @property
    def node_status(self):
        r"""Gets the node_status of this ClusterNode.

        节点状态。对应页面上的操作状态。

        :return: The node_status of this ClusterNode.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this ClusterNode.

        节点状态。对应页面上的操作状态。

        :param node_status: The node_status of this ClusterNode.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def component_infos(self):
        r"""Gets the component_infos of this ClusterNode.

        组件实例信息数组。

        :return: The component_infos of this ClusterNode.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.ComponentInfo`]
        """
        return self._component_infos

    @component_infos.setter
    def component_infos(self, component_infos):
        r"""Sets the component_infos of this ClusterNode.

        组件实例信息数组。

        :param component_infos: The component_infos of this ClusterNode.
        :type component_infos: list[:class:`huaweicloudsdkmrs.v2.ComponentInfo`]
        """
        self._component_infos = component_infos

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
        if not isinstance(other, ClusterNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
