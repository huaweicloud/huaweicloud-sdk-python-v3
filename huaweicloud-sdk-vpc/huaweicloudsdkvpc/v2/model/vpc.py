# coding: utf-8

import pprint
import re

import six





class Vpc:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'cidr': 'str',
        'description': 'str',
        'routes': 'list[Route]',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'description': 'description',
        'routes': 'routes',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, cidr=None, description=None, routes=None, status=None, enterprise_project_id=None):
        """Vpc - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self._description = None
        self._routes = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.cidr = cidr
        self.description = description
        self.routes = routes
        self.status = status
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this Vpc.

        功能说明：虚拟私有云ID 取值范围：带\"-\"的UUID

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vpc.

        功能说明：虚拟私有云ID 取值范围：带\"-\"的UUID

        :param id: The id of this Vpc.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vpc.

        功能说明：虚拟私有云名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 约束：如果名称不为空，则同一个租户下的名称不能重复

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vpc.

        功能说明：虚拟私有云名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 约束：如果名称不为空，则同一个租户下的名称不能重复

        :param name: The name of this Vpc.
        :type: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this Vpc.

        功能说明：虚拟私有云下可用子网的范围 取值范围： - 10.0.0.0/8~10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为空 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :return: The cidr of this Vpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Vpc.

        功能说明：虚拟私有云下可用子网的范围 取值范围： - 10.0.0.0/8~10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 不指定cidr时，默认值为空 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this Vpc.
        :type: str
        """
        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this Vpc.

        功能说明：虚拟私有云的描述 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this Vpc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vpc.

        功能说明：虚拟私有云的描述 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this Vpc.
        :type: str
        """
        self._description = description

    @property
    def routes(self):
        """Gets the routes of this Vpc.

        功能说明：路由信息列表，详情参见route对象

        :return: The routes of this Vpc.
        :rtype: list[Route]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this Vpc.

        功能说明：路由信息列表，详情参见route对象

        :param routes: The routes of this Vpc.
        :type: list[Route]
        """
        self._routes = routes

    @property
    def status(self):
        """Gets the status of this Vpc.

        功能说明：虚拟私有云的状态 取值范围： - CREATING：创建中 - OK：创建成功

        :return: The status of this Vpc.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Vpc.

        功能说明：虚拟私有云的状态 取值范围： - CREATING：创建中 - OK：创建成功

        :param status: The status of this Vpc.
        :type: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Vpc.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this Vpc.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Vpc.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this Vpc.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
