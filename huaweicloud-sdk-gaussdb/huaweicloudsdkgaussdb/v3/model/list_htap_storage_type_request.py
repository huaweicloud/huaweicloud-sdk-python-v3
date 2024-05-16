# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHtapStorageTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'version_name': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'database': 'database',
        'version_name': 'version_name',
        'x_language': 'X-Language'
    }

    def __init__(self, database=None, version_name=None, x_language=None):
        """ListHtapStorageTypeRequest

        The model defined in huaweicloud sdk

        :param database: HTAP数据库名。 取值范围： - star-rocks - click-house
        :type database: str
        :param version_name: 数据库大版本号
        :type version_name: str
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        """
        
        

        self._database = None
        self._version_name = None
        self._x_language = None
        self.discriminator = None

        self.database = database
        self.version_name = version_name
        if x_language is not None:
            self.x_language = x_language

    @property
    def database(self):
        """Gets the database of this ListHtapStorageTypeRequest.

        HTAP数据库名。 取值范围： - star-rocks - click-house

        :return: The database of this ListHtapStorageTypeRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ListHtapStorageTypeRequest.

        HTAP数据库名。 取值范围： - star-rocks - click-house

        :param database: The database of this ListHtapStorageTypeRequest.
        :type database: str
        """
        self._database = database

    @property
    def version_name(self):
        """Gets the version_name of this ListHtapStorageTypeRequest.

        数据库大版本号

        :return: The version_name of this ListHtapStorageTypeRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this ListHtapStorageTypeRequest.

        数据库大版本号

        :param version_name: The version_name of this ListHtapStorageTypeRequest.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def x_language(self):
        """Gets the x_language of this ListHtapStorageTypeRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ListHtapStorageTypeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListHtapStorageTypeRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ListHtapStorageTypeRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListHtapStorageTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
