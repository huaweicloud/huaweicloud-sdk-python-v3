# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayUpdateMcpProtocolConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_configuration': 'CoreGatewaySearchConfiguration',
        'session_configuration': 'CoreGatewaySessionConfiguration'
    }

    attribute_map = {
        'search_configuration': 'search_configuration',
        'session_configuration': 'session_configuration'
    }

    def __init__(self, search_configuration=None, session_configuration=None):
        r"""CoreGatewayUpdateMcpProtocolConfiguration

        The model defined in huaweicloud sdk

        :param search_configuration: 
        :type search_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        :param session_configuration: 
        :type session_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySessionConfiguration`
        """
        
        

        self._search_configuration = None
        self._session_configuration = None
        self.discriminator = None

        if search_configuration is not None:
            self.search_configuration = search_configuration
        if session_configuration is not None:
            self.session_configuration = session_configuration

    @property
    def search_configuration(self):
        r"""Gets the search_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.

        :return: The search_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        """
        return self._search_configuration

    @search_configuration.setter
    def search_configuration(self, search_configuration):
        r"""Sets the search_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.

        :param search_configuration: The search_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.
        :type search_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        """
        self._search_configuration = search_configuration

    @property
    def session_configuration(self):
        r"""Gets the session_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.

        :return: The session_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySessionConfiguration`
        """
        return self._session_configuration

    @session_configuration.setter
    def session_configuration(self, session_configuration):
        r"""Sets the session_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.

        :param session_configuration: The session_configuration of this CoreGatewayUpdateMcpProtocolConfiguration.
        :type session_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySessionConfiguration`
        """
        self._session_configuration = session_configuration

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
        if not isinstance(other, CoreGatewayUpdateMcpProtocolConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
