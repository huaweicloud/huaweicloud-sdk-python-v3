# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudIDEExtensionVersionProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'property_name': 'str',
        'property_value': 'str',
        'extension_version_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'property_name': 'property_name',
        'property_value': 'property_value',
        'extension_version_id': 'extension_version_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, property_name=None, property_value=None, extension_version_id=None, created_at=None, updated_at=None):
        """CloudIDEExtensionVersionProperty

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param property_name: 参数名
        :type property_name: str
        :param property_value: 参数值
        :type property_value: str
        :param extension_version_id: 插件版本id
        :type extension_version_id: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._property_name = None
        self._property_value = None
        self._extension_version_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if property_name is not None:
            self.property_name = property_name
        if property_value is not None:
            self.property_value = property_value
        if extension_version_id is not None:
            self.extension_version_id = extension_version_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this CloudIDEExtensionVersionProperty.

        id

        :return: The id of this CloudIDEExtensionVersionProperty.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudIDEExtensionVersionProperty.

        id

        :param id: The id of this CloudIDEExtensionVersionProperty.
        :type id: int
        """
        self._id = id

    @property
    def property_name(self):
        """Gets the property_name of this CloudIDEExtensionVersionProperty.

        参数名

        :return: The property_name of this CloudIDEExtensionVersionProperty.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this CloudIDEExtensionVersionProperty.

        参数名

        :param property_name: The property_name of this CloudIDEExtensionVersionProperty.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def property_value(self):
        """Gets the property_value of this CloudIDEExtensionVersionProperty.

        参数值

        :return: The property_value of this CloudIDEExtensionVersionProperty.
        :rtype: str
        """
        return self._property_value

    @property_value.setter
    def property_value(self, property_value):
        """Sets the property_value of this CloudIDEExtensionVersionProperty.

        参数值

        :param property_value: The property_value of this CloudIDEExtensionVersionProperty.
        :type property_value: str
        """
        self._property_value = property_value

    @property
    def extension_version_id(self):
        """Gets the extension_version_id of this CloudIDEExtensionVersionProperty.

        插件版本id

        :return: The extension_version_id of this CloudIDEExtensionVersionProperty.
        :rtype: str
        """
        return self._extension_version_id

    @extension_version_id.setter
    def extension_version_id(self, extension_version_id):
        """Sets the extension_version_id of this CloudIDEExtensionVersionProperty.

        插件版本id

        :param extension_version_id: The extension_version_id of this CloudIDEExtensionVersionProperty.
        :type extension_version_id: str
        """
        self._extension_version_id = extension_version_id

    @property
    def created_at(self):
        """Gets the created_at of this CloudIDEExtensionVersionProperty.

        创建时间

        :return: The created_at of this CloudIDEExtensionVersionProperty.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CloudIDEExtensionVersionProperty.

        创建时间

        :param created_at: The created_at of this CloudIDEExtensionVersionProperty.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CloudIDEExtensionVersionProperty.

        更新时间

        :return: The updated_at of this CloudIDEExtensionVersionProperty.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CloudIDEExtensionVersionProperty.

        更新时间

        :param updated_at: The updated_at of this CloudIDEExtensionVersionProperty.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CloudIDEExtensionVersionProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
