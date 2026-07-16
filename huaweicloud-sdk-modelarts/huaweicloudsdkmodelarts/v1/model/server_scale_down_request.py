# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerScaleDownRequest:

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
        'flavor': 'str',
        'server_ids': 'list[str]',
        'resource_flavor': 'str'
    }

    attribute_map = {
        'id': 'id',
        'flavor': 'flavor',
        'server_ids': 'server_ids',
        'resource_flavor': 'resource_flavor'
    }

    def __init__(self, id=None, flavor=None, server_ids=None, resource_flavor=None):
        r"""ServerScaleDownRequest

        The model defined in huaweicloud sdk

        :param id: 超节点ID
        :type id: str
        :param flavor: 规格信息
        :type flavor: str
        :param server_ids: 缩容节点id
        :type server_ids: list[str]
        :param resource_flavor: 资源规格信息
        :type resource_flavor: str
        """
        
        

        self._id = None
        self._flavor = None
        self._server_ids = None
        self._resource_flavor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if flavor is not None:
            self.flavor = flavor
        if server_ids is not None:
            self.server_ids = server_ids
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor

    @property
    def id(self):
        r"""Gets the id of this ServerScaleDownRequest.

        超节点ID

        :return: The id of this ServerScaleDownRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerScaleDownRequest.

        超节点ID

        :param id: The id of this ServerScaleDownRequest.
        :type id: str
        """
        self._id = id

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerScaleDownRequest.

        规格信息

        :return: The flavor of this ServerScaleDownRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerScaleDownRequest.

        规格信息

        :param flavor: The flavor of this ServerScaleDownRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def server_ids(self):
        r"""Gets the server_ids of this ServerScaleDownRequest.

        缩容节点id

        :return: The server_ids of this ServerScaleDownRequest.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        r"""Sets the server_ids of this ServerScaleDownRequest.

        缩容节点id

        :param server_ids: The server_ids of this ServerScaleDownRequest.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this ServerScaleDownRequest.

        资源规格信息

        :return: The resource_flavor of this ServerScaleDownRequest.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this ServerScaleDownRequest.

        资源规格信息

        :param resource_flavor: The resource_flavor of this ServerScaleDownRequest.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerScaleDownRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
