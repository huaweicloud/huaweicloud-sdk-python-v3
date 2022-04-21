# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcOption:

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
        'cidr': 'str',
        'routes': 'list[Route]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'routes': 'routes'
    }

    def __init__(self, name=None, description=None, cidr=None, routes=None):
        """UpdateVpcOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：如果名称不为空，则同一个租户下的VPC不允许重名。
        :type name: str
        :param description: 功能说明：虚拟私有云的描述  取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param cidr: 功能说明：虚拟私有云下可用子网的范围  取值范围：  - 10.0.0.0/8 ~ 10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28  约束：必须是ipv4 cidr格式，例如：192.168.0.0/16
        :type cidr: str
        :param routes: 功能说明：路由信息列表，详情参见route对象
        :type routes: list[:class:`huaweicloudsdkvpc.v2.Route`]
        """
        
        

        self._name = None
        self._description = None
        self._cidr = None
        self._routes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cidr is not None:
            self.cidr = cidr
        if routes is not None:
            self.routes = routes

    @property
    def name(self):
        """Gets the name of this UpdateVpcOption.

        功能说明：虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：如果名称不为空，则同一个租户下的VPC不允许重名。

        :return: The name of this UpdateVpcOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVpcOption.

        功能说明：虚拟私有云名称  取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  约束：如果名称不为空，则同一个租户下的VPC不允许重名。

        :param name: The name of this UpdateVpcOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateVpcOption.

        功能说明：虚拟私有云的描述  取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this UpdateVpcOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVpcOption.

        功能说明：虚拟私有云的描述  取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this UpdateVpcOption.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this UpdateVpcOption.

        功能说明：虚拟私有云下可用子网的范围  取值范围：  - 10.0.0.0/8 ~ 10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28  约束：必须是ipv4 cidr格式，例如：192.168.0.0/16

        :return: The cidr of this UpdateVpcOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this UpdateVpcOption.

        功能说明：虚拟私有云下可用子网的范围  取值范围：  - 10.0.0.0/8 ~ 10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28  约束：必须是ipv4 cidr格式，例如：192.168.0.0/16

        :param cidr: The cidr of this UpdateVpcOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def routes(self):
        """Gets the routes of this UpdateVpcOption.

        功能说明：路由信息列表，详情参见route对象

        :return: The routes of this UpdateVpcOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.Route`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this UpdateVpcOption.

        功能说明：路由信息列表，详情参见route对象

        :param routes: The routes of this UpdateVpcOption.
        :type routes: list[:class:`huaweicloudsdkvpc.v2.Route`]
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
        if not isinstance(other, UpdateVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
