# coding: utf-8

import pprint
import re

import six





class ScriptInfo:


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
        'type': 'str',
        'directory': 'str',
        'content': 'str',
        'connection_name': 'str',
        'database': 'str',
        'queue_name': 'str',
        'configuration': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'directory': 'directory',
        'content': 'content',
        'connection_name': 'connectionName',
        'database': 'database',
        'queue_name': 'queueName',
        'configuration': 'configuration'
    }

    def __init__(self, name=None, type=None, directory=None, content=None, connection_name=None, database=None, queue_name=None, configuration=None):
        """ScriptInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._directory = None
        self._content = None
        self._connection_name = None
        self._database = None
        self._queue_name = None
        self._configuration = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if directory is not None:
            self.directory = directory
        if content is not None:
            self.content = content
        if connection_name is not None:
            self.connection_name = connection_name
        if database is not None:
            self.database = database
        if queue_name is not None:
            self.queue_name = queue_name
        if configuration is not None:
            self.configuration = configuration

    @property
    def name(self):
        """Gets the name of this ScriptInfo.


        :return: The name of this ScriptInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScriptInfo.


        :param name: The name of this ScriptInfo.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ScriptInfo.

        脚本类型

        :return: The type of this ScriptInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScriptInfo.

        脚本类型

        :param type: The type of this ScriptInfo.
        :type: str
        """
        self._type = type

    @property
    def directory(self):
        """Gets the directory of this ScriptInfo.

        脚本关联的目录

        :return: The directory of this ScriptInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ScriptInfo.

        脚本关联的目录

        :param directory: The directory of this ScriptInfo.
        :type: str
        """
        self._directory = directory

    @property
    def content(self):
        """Gets the content of this ScriptInfo.

        脚本内容

        :return: The content of this ScriptInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ScriptInfo.

        脚本内容

        :param content: The content of this ScriptInfo.
        :type: str
        """
        self._content = content

    @property
    def connection_name(self):
        """Gets the connection_name of this ScriptInfo.

        脚本关联的连接名称

        :return: The connection_name of this ScriptInfo.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this ScriptInfo.

        脚本关联的连接名称

        :param connection_name: The connection_name of this ScriptInfo.
        :type: str
        """
        self._connection_name = connection_name

    @property
    def database(self):
        """Gets the database of this ScriptInfo.

        脚本执行所在的数据库

        :return: The database of this ScriptInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ScriptInfo.

        脚本执行所在的数据库

        :param database: The database of this ScriptInfo.
        :type: str
        """
        self._database = database

    @property
    def queue_name(self):
        """Gets the queue_name of this ScriptInfo.

        脚本关联的DLI队列名称

        :return: The queue_name of this ScriptInfo.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ScriptInfo.

        脚本关联的DLI队列名称

        :param queue_name: The queue_name of this ScriptInfo.
        :type: str
        """
        self._queue_name = queue_name

    @property
    def configuration(self):
        """Gets the configuration of this ScriptInfo.

        脚本的配置项参数

        :return: The configuration of this ScriptInfo.
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ScriptInfo.

        脚本的配置项参数

        :param configuration: The configuration of this ScriptInfo.
        :type: str
        """
        self._configuration = configuration

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
        if not isinstance(other, ScriptInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
