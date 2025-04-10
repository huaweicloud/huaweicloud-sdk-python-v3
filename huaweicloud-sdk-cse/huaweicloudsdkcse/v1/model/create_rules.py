# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'precedence': 'int',
        'match': 'CreateMatch',
        'route': 'list[CreateRoute]'
    }

    attribute_map = {
        'precedence': 'precedence',
        'match': 'match',
        'route': 'route'
    }

    def __init__(self, precedence=None, match=None, route=None):
        r"""CreateRules

        The model defined in huaweicloud sdk

        :param precedence: 优先级，数字越大，优先级越高。
        :type precedence: int
        :param match: 
        :type match: :class:`huaweicloudsdkcse.v1.CreateMatch`
        :param route: 路由规则列表。
        :type route: list[:class:`huaweicloudsdkcse.v1.CreateRoute`]
        """
        
        

        self._precedence = None
        self._match = None
        self._route = None
        self.discriminator = None

        if precedence is not None:
            self.precedence = precedence
        if match is not None:
            self.match = match
        if route is not None:
            self.route = route

    @property
    def precedence(self):
        r"""Gets the precedence of this CreateRules.

        优先级，数字越大，优先级越高。

        :return: The precedence of this CreateRules.
        :rtype: int
        """
        return self._precedence

    @precedence.setter
    def precedence(self, precedence):
        r"""Sets the precedence of this CreateRules.

        优先级，数字越大，优先级越高。

        :param precedence: The precedence of this CreateRules.
        :type precedence: int
        """
        self._precedence = precedence

    @property
    def match(self):
        r"""Gets the match of this CreateRules.

        :return: The match of this CreateRules.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateMatch`
        """
        return self._match

    @match.setter
    def match(self, match):
        r"""Sets the match of this CreateRules.

        :param match: The match of this CreateRules.
        :type match: :class:`huaweicloudsdkcse.v1.CreateMatch`
        """
        self._match = match

    @property
    def route(self):
        r"""Gets the route of this CreateRules.

        路由规则列表。

        :return: The route of this CreateRules.
        :rtype: list[:class:`huaweicloudsdkcse.v1.CreateRoute`]
        """
        return self._route

    @route.setter
    def route(self, route):
        r"""Sets the route of this CreateRules.

        路由规则列表。

        :param route: The route of this CreateRules.
        :type route: list[:class:`huaweicloudsdkcse.v1.CreateRoute`]
        """
        self._route = route

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
        if not isinstance(other, CreateRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
