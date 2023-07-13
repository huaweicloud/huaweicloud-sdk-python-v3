# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronRemoveRouterInterfaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'router_id': 'str',
        'body': 'RouterInterfaceRequestBody'
    }

    attribute_map = {
        'router_id': 'router_id',
        'body': 'body'
    }

    def __init__(self, router_id=None, body=None):
        """NeutronRemoveRouterInterfaceRequest

        The model defined in huaweicloud sdk

        :param router_id: 路由器ID
        :type router_id: str
        :param body: Body of the NeutronRemoveRouterInterfaceRequest
        :type body: :class:`huaweicloudsdkvpc.v2.RouterInterfaceRequestBody`
        """
        
        

        self._router_id = None
        self._body = None
        self.discriminator = None

        self.router_id = router_id
        if body is not None:
            self.body = body

    @property
    def router_id(self):
        """Gets the router_id of this NeutronRemoveRouterInterfaceRequest.

        路由器ID

        :return: The router_id of this NeutronRemoveRouterInterfaceRequest.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this NeutronRemoveRouterInterfaceRequest.

        路由器ID

        :param router_id: The router_id of this NeutronRemoveRouterInterfaceRequest.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def body(self):
        """Gets the body of this NeutronRemoveRouterInterfaceRequest.

        :return: The body of this NeutronRemoveRouterInterfaceRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.RouterInterfaceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NeutronRemoveRouterInterfaceRequest.

        :param body: The body of this NeutronRemoveRouterInterfaceRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.RouterInterfaceRequestBody`
        """
        self._body = body

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
        if not isinstance(other, NeutronRemoveRouterInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
