# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussListDatabase:

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
        'owner': 'str',
        'character_set': 'str',
        'collate_set': 'str',
        'size': 'str'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'character_set': 'character_set',
        'collate_set': 'collate_set',
        'size': 'size'
    }

    def __init__(self, name=None, owner=None, character_set=None, collate_set=None, size=None):
        """GaussDBforOpenGaussListDatabase

        The model defined in huaweicloud sdk

        :param name: 数据库名称。
        :type name: str
        :param owner: 数据库所属用户。
        :type owner: str
        :param character_set: 数据库使用的字符集，例如UTF8。
        :type character_set: str
        :param collate_set: 数据库排序集，例如en_US.UTF-8等。
        :type collate_set: str
        :param size: 数据库大小（单位：MB）。
        :type size: str
        """
        
        

        self._name = None
        self._owner = None
        self._character_set = None
        self._collate_set = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if character_set is not None:
            self.character_set = character_set
        if collate_set is not None:
            self.collate_set = collate_set
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this GaussDBforOpenGaussListDatabase.

        数据库名称。

        :return: The name of this GaussDBforOpenGaussListDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GaussDBforOpenGaussListDatabase.

        数据库名称。

        :param name: The name of this GaussDBforOpenGaussListDatabase.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this GaussDBforOpenGaussListDatabase.

        数据库所属用户。

        :return: The owner of this GaussDBforOpenGaussListDatabase.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GaussDBforOpenGaussListDatabase.

        数据库所属用户。

        :param owner: The owner of this GaussDBforOpenGaussListDatabase.
        :type owner: str
        """
        self._owner = owner

    @property
    def character_set(self):
        """Gets the character_set of this GaussDBforOpenGaussListDatabase.

        数据库使用的字符集，例如UTF8。

        :return: The character_set of this GaussDBforOpenGaussListDatabase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this GaussDBforOpenGaussListDatabase.

        数据库使用的字符集，例如UTF8。

        :param character_set: The character_set of this GaussDBforOpenGaussListDatabase.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def collate_set(self):
        """Gets the collate_set of this GaussDBforOpenGaussListDatabase.

        数据库排序集，例如en_US.UTF-8等。

        :return: The collate_set of this GaussDBforOpenGaussListDatabase.
        :rtype: str
        """
        return self._collate_set

    @collate_set.setter
    def collate_set(self, collate_set):
        """Sets the collate_set of this GaussDBforOpenGaussListDatabase.

        数据库排序集，例如en_US.UTF-8等。

        :param collate_set: The collate_set of this GaussDBforOpenGaussListDatabase.
        :type collate_set: str
        """
        self._collate_set = collate_set

    @property
    def size(self):
        """Gets the size of this GaussDBforOpenGaussListDatabase.

        数据库大小（单位：MB）。

        :return: The size of this GaussDBforOpenGaussListDatabase.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GaussDBforOpenGaussListDatabase.

        数据库大小（单位：MB）。

        :param size: The size of this GaussDBforOpenGaussListDatabase.
        :type size: str
        """
        self._size = size

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
        if not isinstance(other, GaussDBforOpenGaussListDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
