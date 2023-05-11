# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteTableRouteAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add': 'list[AddRouteTableRoute]',
        'mod': 'list[ModRouteTableRoute]',
        '_del': 'list[DelRouteTableRoute]'
    }

    attribute_map = {
        'add': 'add',
        'mod': 'mod',
        '_del': 'del'
    }

    def __init__(self, add=None, mod=None, _del=None):
        """RouteTableRouteAction

        The model defined in huaweicloud sdk

        :param add: 新增路由条目，type，destination，nexthop必选
        :type add: list[:class:`huaweicloudsdkvpc.v2.AddRouteTableRoute`]
        :param mod: 修改路由条目，type，destination，nexthop必选
        :type mod: list[:class:`huaweicloudsdkvpc.v2.ModRouteTableRoute`]
        :param _del: 删除路由条目，destination必选
        :type _del: list[:class:`huaweicloudsdkvpc.v2.DelRouteTableRoute`]
        """
        
        

        self._add = None
        self._mod = None
        self.__del = None
        self.discriminator = None

        if add is not None:
            self.add = add
        if mod is not None:
            self.mod = mod
        if _del is not None:
            self._del = _del

    @property
    def add(self):
        """Gets the add of this RouteTableRouteAction.

        新增路由条目，type，destination，nexthop必选

        :return: The add of this RouteTableRouteAction.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AddRouteTableRoute`]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this RouteTableRouteAction.

        新增路由条目，type，destination，nexthop必选

        :param add: The add of this RouteTableRouteAction.
        :type add: list[:class:`huaweicloudsdkvpc.v2.AddRouteTableRoute`]
        """
        self._add = add

    @property
    def mod(self):
        """Gets the mod of this RouteTableRouteAction.

        修改路由条目，type，destination，nexthop必选

        :return: The mod of this RouteTableRouteAction.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ModRouteTableRoute`]
        """
        return self._mod

    @mod.setter
    def mod(self, mod):
        """Sets the mod of this RouteTableRouteAction.

        修改路由条目，type，destination，nexthop必选

        :param mod: The mod of this RouteTableRouteAction.
        :type mod: list[:class:`huaweicloudsdkvpc.v2.ModRouteTableRoute`]
        """
        self._mod = mod

    @property
    def _del(self):
        """Gets the _del of this RouteTableRouteAction.

        删除路由条目，destination必选

        :return: The _del of this RouteTableRouteAction.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.DelRouteTableRoute`]
        """
        return self.__del

    @_del.setter
    def _del(self, _del):
        """Sets the _del of this RouteTableRouteAction.

        删除路由条目，destination必选

        :param _del: The _del of this RouteTableRouteAction.
        :type _del: list[:class:`huaweicloudsdkvpc.v2.DelRouteTableRoute`]
        """
        self.__del = _del

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
        if not isinstance(other, RouteTableRouteAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
