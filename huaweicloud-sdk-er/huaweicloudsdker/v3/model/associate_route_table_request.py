# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRouteTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_client_token')

    openapi_types = {
        'x_client_token': 'str',
        'er_id': 'str',
        'route_table_id': 'str',
        'body': 'AssociationRequestBody'
    }

    attribute_map = {
        'x_client_token': 'X-Client-Token',
        'er_id': 'er_id',
        'route_table_id': 'route_table_id',
        'body': 'body'
    }

    def __init__(self, x_client_token=None, er_id=None, route_table_id=None, body=None):
        """AssociateRouteTableRequest

        The model defined in huaweicloud sdk

        :param x_client_token: 幂等性标识
        :type x_client_token: str
        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param body: Body of the AssociateRouteTableRequest
        :type body: :class:`huaweicloudsdker.v3.AssociationRequestBody`
        """
        
        

        self._x_client_token = None
        self._er_id = None
        self._route_table_id = None
        self._body = None
        self.discriminator = None

        if x_client_token is not None:
            self.x_client_token = x_client_token
        self.er_id = er_id
        self.route_table_id = route_table_id
        if body is not None:
            self.body = body

    @property
    def x_client_token(self):
        """Gets the x_client_token of this AssociateRouteTableRequest.

        幂等性标识

        :return: The x_client_token of this AssociateRouteTableRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this AssociateRouteTableRequest.

        幂等性标识

        :param x_client_token: The x_client_token of this AssociateRouteTableRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def er_id(self):
        """Gets the er_id of this AssociateRouteTableRequest.

        企业路由器实例ID

        :return: The er_id of this AssociateRouteTableRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this AssociateRouteTableRequest.

        企业路由器实例ID

        :param er_id: The er_id of this AssociateRouteTableRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def route_table_id(self):
        """Gets the route_table_id of this AssociateRouteTableRequest.

        路由表ID

        :return: The route_table_id of this AssociateRouteTableRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this AssociateRouteTableRequest.

        路由表ID

        :param route_table_id: The route_table_id of this AssociateRouteTableRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def body(self):
        """Gets the body of this AssociateRouteTableRequest.

        :return: The body of this AssociateRouteTableRequest.
        :rtype: :class:`huaweicloudsdker.v3.AssociationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AssociateRouteTableRequest.

        :param body: The body of this AssociateRouteTableRequest.
        :type body: :class:`huaweicloudsdker.v3.AssociationRequestBody`
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
        if not isinstance(other, AssociateRouteTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
