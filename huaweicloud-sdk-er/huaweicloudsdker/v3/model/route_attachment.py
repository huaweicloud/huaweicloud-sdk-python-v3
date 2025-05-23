# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type': 'str',
        'attachment_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'attachment_id': 'attachment_id'
    }

    def __init__(self, resource_id=None, resource_type=None, attachment_id=None):
        r"""RouteAttachment

        The model defined in huaweicloud sdk

        :param resource_id: 连接关联的资源ID
        :type resource_id: str
        :param resource_type: 连接关联的资源类型: - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -
        :type resource_type: str
        :param attachment_id: 连接ID
        :type attachment_id: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._attachment_id = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_type = resource_type
        self.attachment_id = attachment_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this RouteAttachment.

        连接关联的资源ID

        :return: The resource_id of this RouteAttachment.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this RouteAttachment.

        连接关联的资源ID

        :param resource_id: The resource_id of this RouteAttachment.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this RouteAttachment.

        连接关联的资源类型: - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -

        :return: The resource_type of this RouteAttachment.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this RouteAttachment.

        连接关联的资源类型: - vpc：虚拟私有云 - vpn：vpn网关 - vgw：云专线的虚拟网关 - vpn：vpn网关 - vgw：云专线的虚拟网关 - peering：对等连接，通过云连接CC加载不同区域的企业路由器来创建“对等连接（Peering）”连接 -  -  -

        :param resource_type: The resource_type of this RouteAttachment.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def attachment_id(self):
        r"""Gets the attachment_id of this RouteAttachment.

        连接ID

        :return: The attachment_id of this RouteAttachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        r"""Sets the attachment_id of this RouteAttachment.

        连接ID

        :param attachment_id: The attachment_id of this RouteAttachment.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

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
        if not isinstance(other, RouteAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
