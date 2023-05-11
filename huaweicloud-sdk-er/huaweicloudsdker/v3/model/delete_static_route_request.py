# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStaticRouteRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_table_id': 'str',
        'route_id': 'str'
    }

    attribute_map = {
        'route_table_id': 'route_table_id',
        'route_id': 'route_id'
    }

    def __init__(self, route_table_id=None, route_id=None):
        """DeleteStaticRouteRequest

        The model defined in huaweicloud sdk

        :param route_table_id: 路由表ID
        :type route_table_id: str
        :param route_id: 路由ID
        :type route_id: str
        """
        
        

        self._route_table_id = None
        self._route_id = None
        self.discriminator = None

        self.route_table_id = route_table_id
        self.route_id = route_id

    @property
    def route_table_id(self):
        """Gets the route_table_id of this DeleteStaticRouteRequest.

        路由表ID

        :return: The route_table_id of this DeleteStaticRouteRequest.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this DeleteStaticRouteRequest.

        路由表ID

        :param route_table_id: The route_table_id of this DeleteStaticRouteRequest.
        :type route_table_id: str
        """
        self._route_table_id = route_table_id

    @property
    def route_id(self):
        """Gets the route_id of this DeleteStaticRouteRequest.

        路由ID

        :return: The route_id of this DeleteStaticRouteRequest.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this DeleteStaticRouteRequest.

        路由ID

        :param route_id: The route_id of this DeleteStaticRouteRequest.
        :type route_id: str
        """
        self._route_id = route_id

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
        if not isinstance(other, DeleteStaticRouteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
