# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRouteTableReq:

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
        'description': 'str',
        'routes': 'dict(str, list[RouteTableRoute])'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'routes': 'routes'
    }

    def __init__(self, name=None, description=None, routes=None):
        """UpdateRouteTableReq

        The model defined in huaweicloud sdk

        :param name: 功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param routes: 功能说明：路由对象  取值范围：参见route字段说明。更新存在三种动作：     1）add：新增路由条目，type，destination，nexthop必选。     2）mod：修改路由信息，type，destination，nexthop必选。     3）del：删除路由条目，destination必选  约束：     每个路由表最大关联200条路由。     不支持直接修改destination，如需修改，只能使用del先删除对应路由，然后使用add新增路由。
        :type routes: dict(str, list[RouteTableRoute])
        """
        
        

        self._name = None
        self._description = None
        self._routes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if routes is not None:
            self.routes = routes

    @property
    def name(self):
        """Gets the name of this UpdateRouteTableReq.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateRouteTableReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRouteTableReq.

        功能说明：路由表名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateRouteTableReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateRouteTableReq.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this UpdateRouteTableReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRouteTableReq.

        功能说明：路由表描述信息  取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this UpdateRouteTableReq.
        :type description: str
        """
        self._description = description

    @property
    def routes(self):
        """Gets the routes of this UpdateRouteTableReq.

        功能说明：路由对象  取值范围：参见route字段说明。更新存在三种动作：     1）add：新增路由条目，type，destination，nexthop必选。     2）mod：修改路由信息，type，destination，nexthop必选。     3）del：删除路由条目，destination必选  约束：     每个路由表最大关联200条路由。     不支持直接修改destination，如需修改，只能使用del先删除对应路由，然后使用add新增路由。

        :return: The routes of this UpdateRouteTableReq.
        :rtype: dict(str, list[RouteTableRoute])
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this UpdateRouteTableReq.

        功能说明：路由对象  取值范围：参见route字段说明。更新存在三种动作：     1）add：新增路由条目，type，destination，nexthop必选。     2）mod：修改路由信息，type，destination，nexthop必选。     3）del：删除路由条目，destination必选  约束：     每个路由表最大关联200条路由。     不支持直接修改destination，如需修改，只能使用del先删除对应路由，然后使用add新增路由。

        :param routes: The routes of this UpdateRouteTableReq.
        :type routes: dict(str, list[RouteTableRoute])
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
        if not isinstance(other, UpdateRouteTableReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
