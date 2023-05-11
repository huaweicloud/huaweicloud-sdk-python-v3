# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Product:

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
        'description': 'str',
        'attributes': 'dict(str, ProductAttributes)',
        'project_id': 'str',
        'created_at': 'int',
        'tags': 'list[Attributes]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'attributes': 'attributes',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, attributes=None, project_id=None, created_at=None, tags=None):
        """Product

        The model defined in huaweicloud sdk

        :param id: 产品id
        :type id: str
        :param name: 产品名称
        :type name: str
        :param description: 产品描述
        :type description: str
        :param attributes: 产品属性值
        :type attributes: dict(str, ProductAttributes)
        :param project_id: 产品所属账号的项目ID
        :type project_id: str
        :param created_at: 产品创建时间
        :type created_at: int
        :param tags: 产品标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._attributes = None
        self._project_id = None
        self._created_at = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this Product.

        产品id

        :return: The id of this Product.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Product.

        产品id

        :param id: The id of this Product.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Product.

        产品名称

        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        产品名称

        :param name: The name of this Product.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Product.

        产品描述

        :return: The description of this Product.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.

        产品描述

        :param description: The description of this Product.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        """Gets the attributes of this Product.

        产品属性值

        :return: The attributes of this Product.
        :rtype: dict(str, ProductAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Product.

        产品属性值

        :param attributes: The attributes of this Product.
        :type attributes: dict(str, ProductAttributes)
        """
        self._attributes = attributes

    @property
    def project_id(self):
        """Gets the project_id of this Product.

        产品所属账号的项目ID

        :return: The project_id of this Product.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Product.

        产品所属账号的项目ID

        :param project_id: The project_id of this Product.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this Product.

        产品创建时间

        :return: The created_at of this Product.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Product.

        产品创建时间

        :param created_at: The created_at of this Product.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def tags(self):
        """Gets the tags of this Product.

        产品标签

        :return: The tags of this Product.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Product.

        产品标签

        :param tags: The tags of this Product.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
