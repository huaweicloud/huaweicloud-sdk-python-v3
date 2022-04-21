# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRoutesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'routes': 'list[DeleteRouteOption]'
    }

    attribute_map = {
        'routes': 'routes'
    }

    def __init__(self, routes=None):
        """DeleteRoutesRequestBody

        The model defined in huaweicloud sdk

        :param routes: 待删除的路由信息
        :type routes: list[:class:`huaweicloudsdkiec.v1.DeleteRouteOption`]
        """
        
        

        self._routes = None
        self.discriminator = None

        self.routes = routes

    @property
    def routes(self):
        """Gets the routes of this DeleteRoutesRequestBody.

        待删除的路由信息

        :return: The routes of this DeleteRoutesRequestBody.
        :rtype: list[:class:`huaweicloudsdkiec.v1.DeleteRouteOption`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this DeleteRoutesRequestBody.

        待删除的路由信息

        :param routes: The routes of this DeleteRoutesRequestBody.
        :type routes: list[:class:`huaweicloudsdkiec.v1.DeleteRouteOption`]
        """
        self._routes = routes

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
        if not isinstance(other, DeleteRoutesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
