# coding: utf-8

import pprint
import re

import six


class RoleResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'flag': 'str',
        'description_cn': 'str',
        'catalog': 'str',
        'name': 'str',
        'description': 'str',
        'links': 'Links',
        'id': 'str',
        'display_name': 'str',
        'type': 'str',
        'policy': 'RolePolicy',
        'updated_time': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'flag': 'flag',
        'description_cn': 'description_cn',
        'catalog': 'catalog',
        'name': 'name',
        'description': 'description',
        'links': 'links',
        'id': 'id',
        'display_name': 'display_name',
        'type': 'type',
        'policy': 'policy',
        'updated_time': 'updated_time',
        'created_time': 'created_time'
    }

    def __init__(self, domain_id=None, flag=None, description_cn=None, catalog=None, name=None, description=None, links=None, id=None, display_name=None, type=None, policy=None, updated_time=None, created_time=None):  # noqa: E501
        """RoleResult - a model defined in huaweicloud sdk"""

        self._domain_id = None
        self._flag = None
        self._description_cn = None
        self._catalog = None
        self._name = None
        self._description = None
        self._links = None
        self._id = None
        self._display_name = None
        self._type = None
        self._policy = None
        self._updated_time = None
        self._created_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if flag is not None:
            self.flag = flag
        if description_cn is not None:
            self.description_cn = description_cn
        if catalog is not None:
            self.catalog = catalog
        self.name = name
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        self.id = id
        if display_name is not None:
            self.display_name = display_name
        self.type = type
        self.policy = policy
        if updated_time is not None:
            self.updated_time = updated_time
        if created_time is not None:
            self.created_time = created_time

    @property
    def domain_id(self):
        """Gets the domain_id of this RoleResult.

        权限所属账号ID。

        :return: The domain_id of this RoleResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this RoleResult.

        权限所属账号ID。

        :param domain_id: The domain_id of this RoleResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def flag(self):
        """Gets the flag of this RoleResult.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :return: The flag of this RoleResult.
        :rtype: str
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this RoleResult.

        该参数值为fine_grained时，标识此权限为系统内置的策略。

        :param flag: The flag of this RoleResult.
        :type: str
        """
        self._flag = flag

    @property
    def description_cn(self):
        """Gets the description_cn of this RoleResult.

        权限的中文描述信息。

        :return: The description_cn of this RoleResult.
        :rtype: str
        """
        return self._description_cn

    @description_cn.setter
    def description_cn(self, description_cn):
        """Sets the description_cn of this RoleResult.

        权限的中文描述信息。

        :param description_cn: The description_cn of this RoleResult.
        :type: str
        """
        self._description_cn = description_cn

    @property
    def catalog(self):
        """Gets the catalog of this RoleResult.

        权限所在目录。

        :return: The catalog of this RoleResult.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this RoleResult.

        权限所在目录。

        :param catalog: The catalog of this RoleResult.
        :type: str
        """
        self._catalog = catalog

    @property
    def name(self):
        """Gets the name of this RoleResult.

        权限名。携带在用户的token中，云服务根据该名称来判断用户是否有权限访问。

        :return: The name of this RoleResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleResult.

        权限名。携带在用户的token中，云服务根据该名称来判断用户是否有权限访问。

        :param name: The name of this RoleResult.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleResult.

        权限描述信息。

        :return: The description of this RoleResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleResult.

        权限描述信息。

        :param description: The description of this RoleResult.
        :type: str
        """
        self._description = description

    @property
    def links(self):
        """Gets the links of this RoleResult.


        :return: The links of this RoleResult.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RoleResult.


        :param links: The links of this RoleResult.
        :type: Links
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this RoleResult.

        权限ID。

        :return: The id of this RoleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleResult.

        权限ID。

        :param id: The id of this RoleResult.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this RoleResult.

        权限展示名。

        :return: The display_name of this RoleResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RoleResult.

        权限展示名。

        :param display_name: The display_name of this RoleResult.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this RoleResult.

        权限的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - AA表示在domain和project层均显示。   > - XX表示在domain和project层均不显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :return: The type of this RoleResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RoleResult.

        权限的显示模式。   > - AX表示在domain层显示。   > - XA表示在project层显示。   > - AA表示在domain和project层均显示。   > - XX表示在domain和project层均不显示。   > - 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）。

        :param type: The type of this RoleResult.
        :type: str
        """
        self._type = type

    @property
    def policy(self):
        """Gets the policy of this RoleResult.


        :return: The policy of this RoleResult.
        :rtype: RolePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this RoleResult.


        :param policy: The policy of this RoleResult.
        :type: RolePolicy
        """
        self._policy = policy

    @property
    def updated_time(self):
        """Gets the updated_time of this RoleResult.

        权限更新时间。

        :return: The updated_time of this RoleResult.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this RoleResult.

        权限更新时间。

        :param updated_time: The updated_time of this RoleResult.
        :type: str
        """
        self._updated_time = updated_time

    @property
    def created_time(self):
        """Gets the created_time of this RoleResult.

        权限创建时间。

        :return: The created_time of this RoleResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this RoleResult.

        权限创建时间。

        :param created_time: The created_time of this RoleResult.
        :type: str
        """
        self._created_time = created_time

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
        if not isinstance(other, RoleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other