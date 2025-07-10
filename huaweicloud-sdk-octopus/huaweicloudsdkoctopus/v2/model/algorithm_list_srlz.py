# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmListSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'updated_at': 'float',
        'created_at': 'float',
        'category': 'CategoryF62Enum',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'category': 'category',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, url=None, id=None, updated_at=None, created_at=None, category=None, name=None, description=None):
        r"""AlgorithmListSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param updated_at: 
        :type updated_at: float
        :param created_at: 
        :type created_at: float
        :param category: 算法类型  * &#x60;code&#x60; - Code * &#x60;artifact&#x60; - Artifact * &#x60;image&#x60; - Image
        :type category: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._url = None
        self._id = None
        self._updated_at = None
        self._created_at = None
        self._category = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.url = url
        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.category = category
        self.name = name
        self.description = description

    @property
    def url(self):
        r"""Gets the url of this AlgorithmListSrlz.

        :return: The url of this AlgorithmListSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AlgorithmListSrlz.

        :param url: The url of this AlgorithmListSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this AlgorithmListSrlz.

        :return: The id of this AlgorithmListSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlgorithmListSrlz.

        :param id: The id of this AlgorithmListSrlz.
        :type id: int
        """
        self._id = id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AlgorithmListSrlz.

        :return: The updated_at of this AlgorithmListSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AlgorithmListSrlz.

        :param updated_at: The updated_at of this AlgorithmListSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def created_at(self):
        r"""Gets the created_at of this AlgorithmListSrlz.

        :return: The created_at of this AlgorithmListSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AlgorithmListSrlz.

        :param created_at: The created_at of this AlgorithmListSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def category(self):
        r"""Gets the category of this AlgorithmListSrlz.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :return: The category of this AlgorithmListSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AlgorithmListSrlz.

        算法类型  * `code` - Code * `artifact` - Artifact * `image` - Image

        :param category: The category of this AlgorithmListSrlz.
        :type category: :class:`huaweicloudsdkoctopus.v2.CategoryF62Enum`
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this AlgorithmListSrlz.

        名称

        :return: The name of this AlgorithmListSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmListSrlz.

        名称

        :param name: The name of this AlgorithmListSrlz.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AlgorithmListSrlz.

        描述

        :return: The description of this AlgorithmListSrlz.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlgorithmListSrlz.

        描述

        :param description: The description of this AlgorithmListSrlz.
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
        if not isinstance(other, AlgorithmListSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
