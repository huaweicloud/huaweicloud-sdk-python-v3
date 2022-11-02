# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionsResponse:

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
        'database_name': 'str',
        'version': 'str',
        'shared_preload_libraries': 'str',
        'created': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'database_name': 'database_name',
        'version': 'version',
        'shared_preload_libraries': 'shared_preload_libraries',
        'created': 'created',
        'description': 'description'
    }

    def __init__(self, name=None, database_name=None, version=None, shared_preload_libraries=None, created=None, description=None):
        """ExtensionsResponse

        The model defined in huaweicloud sdk

        :param name: 插件名称。
        :type name: str
        :param database_name: 数据库名称。
        :type database_name: str
        :param version: 插件版本。
        :type version: str
        :param shared_preload_libraries: 依赖预加载库。
        :type shared_preload_libraries: str
        :param created: 是否创建。
        :type created: bool
        :param description: 插件描述。
        :type description: str
        """
        
        

        self._name = None
        self._database_name = None
        self._version = None
        self._shared_preload_libraries = None
        self._created = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if database_name is not None:
            self.database_name = database_name
        if version is not None:
            self.version = version
        if shared_preload_libraries is not None:
            self.shared_preload_libraries = shared_preload_libraries
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ExtensionsResponse.

        插件名称。

        :return: The name of this ExtensionsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtensionsResponse.

        插件名称。

        :param name: The name of this ExtensionsResponse.
        :type name: str
        """
        self._name = name

    @property
    def database_name(self):
        """Gets the database_name of this ExtensionsResponse.

        数据库名称。

        :return: The database_name of this ExtensionsResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ExtensionsResponse.

        数据库名称。

        :param database_name: The database_name of this ExtensionsResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def version(self):
        """Gets the version of this ExtensionsResponse.

        插件版本。

        :return: The version of this ExtensionsResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExtensionsResponse.

        插件版本。

        :param version: The version of this ExtensionsResponse.
        :type version: str
        """
        self._version = version

    @property
    def shared_preload_libraries(self):
        """Gets the shared_preload_libraries of this ExtensionsResponse.

        依赖预加载库。

        :return: The shared_preload_libraries of this ExtensionsResponse.
        :rtype: str
        """
        return self._shared_preload_libraries

    @shared_preload_libraries.setter
    def shared_preload_libraries(self, shared_preload_libraries):
        """Sets the shared_preload_libraries of this ExtensionsResponse.

        依赖预加载库。

        :param shared_preload_libraries: The shared_preload_libraries of this ExtensionsResponse.
        :type shared_preload_libraries: str
        """
        self._shared_preload_libraries = shared_preload_libraries

    @property
    def created(self):
        """Gets the created of this ExtensionsResponse.

        是否创建。

        :return: The created of this ExtensionsResponse.
        :rtype: bool
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ExtensionsResponse.

        是否创建。

        :param created: The created of this ExtensionsResponse.
        :type created: bool
        """
        self._created = created

    @property
    def description(self):
        """Gets the description of this ExtensionsResponse.

        插件描述。

        :return: The description of this ExtensionsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtensionsResponse.

        插件描述。

        :param description: The description of this ExtensionsResponse.
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
        if not isinstance(other, ExtensionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
