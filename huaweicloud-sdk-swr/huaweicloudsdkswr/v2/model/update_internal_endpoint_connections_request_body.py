# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternalEndpointConnectionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'action': 'action'
    }

    def __init__(self, endpoints=None, action=None):
        r"""UpdateInternalEndpointConnectionsRequestBody

        The model defined in huaweicloud sdk

        :param endpoints: VPC终端节点ID列表
        :type endpoints: list[str]
        :param action: 允许或拒绝连接 取值范围: - receive:允许连接 - reject:拒绝连接
        :type action: str
        """
        
        

        self._endpoints = None
        self._action = None
        self.discriminator = None

        self.endpoints = endpoints
        self.action = action

    @property
    def endpoints(self):
        r"""Gets the endpoints of this UpdateInternalEndpointConnectionsRequestBody.

        VPC终端节点ID列表

        :return: The endpoints of this UpdateInternalEndpointConnectionsRequestBody.
        :rtype: list[str]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this UpdateInternalEndpointConnectionsRequestBody.

        VPC终端节点ID列表

        :param endpoints: The endpoints of this UpdateInternalEndpointConnectionsRequestBody.
        :type endpoints: list[str]
        """
        self._endpoints = endpoints

    @property
    def action(self):
        r"""Gets the action of this UpdateInternalEndpointConnectionsRequestBody.

        允许或拒绝连接 取值范围: - receive:允许连接 - reject:拒绝连接

        :return: The action of this UpdateInternalEndpointConnectionsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateInternalEndpointConnectionsRequestBody.

        允许或拒绝连接 取值范围: - receive:允许连接 - reject:拒绝连接

        :param action: The action of this UpdateInternalEndpointConnectionsRequestBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, UpdateInternalEndpointConnectionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
