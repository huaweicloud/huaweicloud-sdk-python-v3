# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tool:

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
        'url': 'str',
        'icon': 'str',
        'problem_type_id': 'str',
        'business_type_id': 'str',
        'product_type_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'icon': 'icon',
        'problem_type_id': 'problem_type_id',
        'business_type_id': 'business_type_id',
        'product_type_id': 'product_type_id'
    }

    def __init__(self, id=None, name=None, url=None, icon=None, problem_type_id=None, business_type_id=None, product_type_id=None):
        """Tool

        The model defined in huaweicloud sdk

        :param id: 工具Id
        :type id: str
        :param name: 工具名称
        :type name: str
        :param url: 工具链接
        :type url: str
        :param icon: 图标内容，Base64格式
        :type icon: str
        :param problem_type_id: 问题分类Id
        :type problem_type_id: str
        :param business_type_id: 业务类型Id
        :type business_type_id: str
        :param product_type_id: 产品类型Id
        :type product_type_id: str
        """
        
        

        self._id = None
        self._name = None
        self._url = None
        self._icon = None
        self._problem_type_id = None
        self._business_type_id = None
        self._product_type_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        if url is not None:
            self.url = url
        if icon is not None:
            self.icon = icon
        if problem_type_id is not None:
            self.problem_type_id = problem_type_id
        if business_type_id is not None:
            self.business_type_id = business_type_id
        if product_type_id is not None:
            self.product_type_id = product_type_id

    @property
    def id(self):
        """Gets the id of this Tool.

        工具Id

        :return: The id of this Tool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tool.

        工具Id

        :param id: The id of this Tool.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Tool.

        工具名称

        :return: The name of this Tool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tool.

        工具名称

        :param name: The name of this Tool.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        """Gets the url of this Tool.

        工具链接

        :return: The url of this Tool.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Tool.

        工具链接

        :param url: The url of this Tool.
        :type url: str
        """
        self._url = url

    @property
    def icon(self):
        """Gets the icon of this Tool.

        图标内容，Base64格式

        :return: The icon of this Tool.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Tool.

        图标内容，Base64格式

        :param icon: The icon of this Tool.
        :type icon: str
        """
        self._icon = icon

    @property
    def problem_type_id(self):
        """Gets the problem_type_id of this Tool.

        问题分类Id

        :return: The problem_type_id of this Tool.
        :rtype: str
        """
        return self._problem_type_id

    @problem_type_id.setter
    def problem_type_id(self, problem_type_id):
        """Sets the problem_type_id of this Tool.

        问题分类Id

        :param problem_type_id: The problem_type_id of this Tool.
        :type problem_type_id: str
        """
        self._problem_type_id = problem_type_id

    @property
    def business_type_id(self):
        """Gets the business_type_id of this Tool.

        业务类型Id

        :return: The business_type_id of this Tool.
        :rtype: str
        """
        return self._business_type_id

    @business_type_id.setter
    def business_type_id(self, business_type_id):
        """Sets the business_type_id of this Tool.

        业务类型Id

        :param business_type_id: The business_type_id of this Tool.
        :type business_type_id: str
        """
        self._business_type_id = business_type_id

    @property
    def product_type_id(self):
        """Gets the product_type_id of this Tool.

        产品类型Id

        :return: The product_type_id of this Tool.
        :rtype: str
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this Tool.

        产品类型Id

        :param product_type_id: The product_type_id of this Tool.
        :type product_type_id: str
        """
        self._product_type_id = product_type_id

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
        if not isinstance(other, Tool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
