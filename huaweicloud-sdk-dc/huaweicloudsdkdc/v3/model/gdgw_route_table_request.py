# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GdgwRouteTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_routes': 'list[AddGdgwRouteAction]',
        'del_routes': 'list[DeleteGdgwRouteAction]',
        'update_routes': 'list[UpdateRouteAction]'
    }

    attribute_map = {
        'add_routes': 'add_routes',
        'del_routes': 'del_routes',
        'update_routes': 'update_routes'
    }

    def __init__(self, add_routes=None, del_routes=None, update_routes=None):
        r"""GdgwRouteTableRequest

        The model defined in huaweicloud sdk

        :param add_routes: 需要添加的路由
        :type add_routes: list[:class:`huaweicloudsdkdc.v3.AddGdgwRouteAction`]
        :param del_routes: 需要删除的路由
        :type del_routes: list[:class:`huaweicloudsdkdc.v3.DeleteGdgwRouteAction`]
        :param update_routes: 需要更新的路由 仅更新该条路由的附加信息，不执行交换机的路由更新操作。当前支持更新：路由描述-description信息
        :type update_routes: list[:class:`huaweicloudsdkdc.v3.UpdateRouteAction`]
        """
        
        

        self._add_routes = None
        self._del_routes = None
        self._update_routes = None
        self.discriminator = None

        if add_routes is not None:
            self.add_routes = add_routes
        if del_routes is not None:
            self.del_routes = del_routes
        if update_routes is not None:
            self.update_routes = update_routes

    @property
    def add_routes(self):
        r"""Gets the add_routes of this GdgwRouteTableRequest.

        需要添加的路由

        :return: The add_routes of this GdgwRouteTableRequest.
        :rtype: list[:class:`huaweicloudsdkdc.v3.AddGdgwRouteAction`]
        """
        return self._add_routes

    @add_routes.setter
    def add_routes(self, add_routes):
        r"""Sets the add_routes of this GdgwRouteTableRequest.

        需要添加的路由

        :param add_routes: The add_routes of this GdgwRouteTableRequest.
        :type add_routes: list[:class:`huaweicloudsdkdc.v3.AddGdgwRouteAction`]
        """
        self._add_routes = add_routes

    @property
    def del_routes(self):
        r"""Gets the del_routes of this GdgwRouteTableRequest.

        需要删除的路由

        :return: The del_routes of this GdgwRouteTableRequest.
        :rtype: list[:class:`huaweicloudsdkdc.v3.DeleteGdgwRouteAction`]
        """
        return self._del_routes

    @del_routes.setter
    def del_routes(self, del_routes):
        r"""Sets the del_routes of this GdgwRouteTableRequest.

        需要删除的路由

        :param del_routes: The del_routes of this GdgwRouteTableRequest.
        :type del_routes: list[:class:`huaweicloudsdkdc.v3.DeleteGdgwRouteAction`]
        """
        self._del_routes = del_routes

    @property
    def update_routes(self):
        r"""Gets the update_routes of this GdgwRouteTableRequest.

        需要更新的路由 仅更新该条路由的附加信息，不执行交换机的路由更新操作。当前支持更新：路由描述-description信息

        :return: The update_routes of this GdgwRouteTableRequest.
        :rtype: list[:class:`huaweicloudsdkdc.v3.UpdateRouteAction`]
        """
        return self._update_routes

    @update_routes.setter
    def update_routes(self, update_routes):
        r"""Sets the update_routes of this GdgwRouteTableRequest.

        需要更新的路由 仅更新该条路由的附加信息，不执行交换机的路由更新操作。当前支持更新：路由描述-description信息

        :param update_routes: The update_routes of this GdgwRouteTableRequest.
        :type update_routes: list[:class:`huaweicloudsdkdc.v3.UpdateRouteAction`]
        """
        self._update_routes = update_routes

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
        if not isinstance(other, GdgwRouteTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
