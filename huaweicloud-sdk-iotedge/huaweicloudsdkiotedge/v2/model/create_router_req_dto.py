# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRouterReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_id': 'str',
        'sql': 'str'
    }

    attribute_map = {
        'route_id': 'route_id',
        'sql': 'sql'
    }

    def __init__(self, route_id=None, sql=None):
        r"""CreateRouterReqDTO

        The model defined in huaweicloud sdk

        :param route_id: 路由ID，节点下唯一
        :type route_id: str
        :param sql: sql參數
        :type sql: str
        """
        
        

        self._route_id = None
        self._sql = None
        self.discriminator = None

        self.route_id = route_id
        self.sql = sql

    @property
    def route_id(self):
        r"""Gets the route_id of this CreateRouterReqDTO.

        路由ID，节点下唯一

        :return: The route_id of this CreateRouterReqDTO.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        r"""Sets the route_id of this CreateRouterReqDTO.

        路由ID，节点下唯一

        :param route_id: The route_id of this CreateRouterReqDTO.
        :type route_id: str
        """
        self._route_id = route_id

    @property
    def sql(self):
        r"""Gets the sql of this CreateRouterReqDTO.

        sql參數

        :return: The sql of this CreateRouterReqDTO.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this CreateRouterReqDTO.

        sql參數

        :param sql: The sql of this CreateRouterReqDTO.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, CreateRouterReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
