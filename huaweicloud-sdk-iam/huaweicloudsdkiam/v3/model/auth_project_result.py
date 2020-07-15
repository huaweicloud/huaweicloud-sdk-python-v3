# coding: utf-8

import pprint
import re

import six





class AuthProjectResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_domain': 'bool',
        'description': 'str',
        'links': 'LinksSelf',
        'enabled': 'bool',
        'id': 'str',
        'parent_id': 'str',
        'domain_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'is_domain': 'is_domain',
        'description': 'description',
        'links': 'links',
        'enabled': 'enabled',
        'id': 'id',
        'parent_id': 'parent_id',
        'domain_id': 'domain_id',
        'name': 'name'
    }

    def __init__(self, is_domain=None, description=None, links=None, enabled=None, id=None, parent_id=None, domain_id=None, name=None):
        """AuthProjectResult - a model defined in huaweicloud sdk"""
        
        

        self._is_domain = None
        self._description = None
        self._links = None
        self._enabled = None
        self._id = None
        self._parent_id = None
        self._domain_id = None
        self._name = None
        self.discriminator = None

        self.is_domain = is_domain
        self.description = description
        self.links = links
        self.enabled = enabled
        self.id = id
        self.parent_id = parent_id
        self.domain_id = domain_id
        self.name = name

    @property
    def is_domain(self):
        """Gets the is_domain of this AuthProjectResult.

        false.

        :return: The is_domain of this AuthProjectResult.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        """Sets the is_domain of this AuthProjectResult.

        false.

        :param is_domain: The is_domain of this AuthProjectResult.
        :type: bool
        """
        self._is_domain = is_domain

    @property
    def description(self):
        """Gets the description of this AuthProjectResult.

        项目描述信息。

        :return: The description of this AuthProjectResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthProjectResult.

        项目描述信息。

        :param description: The description of this AuthProjectResult.
        :type: str
        """
        self._description = description

    @property
    def links(self):
        """Gets the links of this AuthProjectResult.


        :return: The links of this AuthProjectResult.
        :rtype: LinksSelf
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AuthProjectResult.


        :param links: The links of this AuthProjectResult.
        :type: LinksSelf
        """
        self._links = links

    @property
    def enabled(self):
        """Gets the enabled of this AuthProjectResult.

        项目是否可用。

        :return: The enabled of this AuthProjectResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AuthProjectResult.

        项目是否可用。

        :param enabled: The enabled of this AuthProjectResult.
        :type: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AuthProjectResult.

        项目ID。

        :return: The id of this AuthProjectResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthProjectResult.

        项目ID。

        :param id: The id of this AuthProjectResult.
        :type: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this AuthProjectResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。    如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :return: The parent_id of this AuthProjectResult.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this AuthProjectResult.

        如果查询自己创建的项目，则此处返回所属区域的项目ID。    如果查询的是系统内置项目，如cn-north-4，则此处返回账号ID。

        :param parent_id: The parent_id of this AuthProjectResult.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def domain_id(self):
        """Gets the domain_id of this AuthProjectResult.

        项目所属账号ID。

        :return: The domain_id of this AuthProjectResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AuthProjectResult.

        项目所属账号ID。

        :param domain_id: The domain_id of this AuthProjectResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this AuthProjectResult.

        项目名称。

        :return: The name of this AuthProjectResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthProjectResult.

        项目名称。

        :param name: The name of this AuthProjectResult.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, AuthProjectResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
