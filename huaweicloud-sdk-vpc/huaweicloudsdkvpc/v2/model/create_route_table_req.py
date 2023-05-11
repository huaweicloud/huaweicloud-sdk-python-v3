# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRouteTableReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'routes': 'list[RouteTableRoute]',
        'vpc_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'routes': 'routes',
        'vpc_id': 'vpc_id',
        'description': 'description'
    }

    def __init__(self, name=None, routes=None, vpc_id=None, description=None):
        """CreateRouteTableReq

        The model defined in huaweicloud sdk

        :param name: 功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param routes: 功能说明：路由对象，参见route字段说明  约束：每个路由表最大关联200条路由
        :type routes: list[:class:`huaweicloudsdkvpc.v2.RouteTableRoute`]
        :param vpc_id: 路由表所在的虚拟私有云ID
        :type vpc_id: str
        :param description: 功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        """
        
        

        self._name = None
        self._routes = None
        self._vpc_id = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if routes is not None:
            self.routes = routes
        self.vpc_id = vpc_id
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CreateRouteTableReq.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateRouteTableReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRouteTableReq.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateRouteTableReq.
        :type name: str
        """
        self._name = name

    @property
    def routes(self):
        """Gets the routes of this CreateRouteTableReq.

        功能说明：路由对象，参见route字段说明  约束：每个路由表最大关联200条路由

        :return: The routes of this CreateRouteTableReq.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.RouteTableRoute`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this CreateRouteTableReq.

        功能说明：路由对象，参见route字段说明  约束：每个路由表最大关联200条路由

        :param routes: The routes of this CreateRouteTableReq.
        :type routes: list[:class:`huaweicloudsdkvpc.v2.RouteTableRoute`]
        """
        self._routes = routes

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateRouteTableReq.

        路由表所在的虚拟私有云ID

        :return: The vpc_id of this CreateRouteTableReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateRouteTableReq.

        路由表所在的虚拟私有云ID

        :param vpc_id: The vpc_id of this CreateRouteTableReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this CreateRouteTableReq.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this CreateRouteTableReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRouteTableReq.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this CreateRouteTableReq.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateRouteTableReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
