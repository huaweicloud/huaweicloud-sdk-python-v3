# coding: utf-8

import pprint
import re

import six





class CreateInstanceDatastoreOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'storage_engine': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'storage_engine': 'storage_engine'
    }

    def __init__(self, type=None, version=None, storage_engine=None):
        """CreateInstanceDatastoreOption - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._version = None
        self._storage_engine = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.storage_engine = storage_engine

    @property
    def type(self):
        """Gets the type of this CreateInstanceDatastoreOption.

        数据库版本类型。支持DDS社区版和增强版。 取值： - 取“DDS-Community”，表示创建社区版实例。 - 取“DDS-Enhanced”，表示创建增强版实例。

        :return: The type of this CreateInstanceDatastoreOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateInstanceDatastoreOption.

        数据库版本类型。支持DDS社区版和增强版。 取值： - 取“DDS-Community”，表示创建社区版实例。 - 取“DDS-Enhanced”，表示创建增强版实例。

        :param type: The type of this CreateInstanceDatastoreOption.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this CreateInstanceDatastoreOption.

        数据库版本。DDS社区版支持3.4、3.2和4.0版本，DDS增强版仅支持3.4版本。 取值： - 社区版引擎取“3.4”、“3.2”或“4.0”。 - 增强版引擎取“3.4”。

        :return: The version of this CreateInstanceDatastoreOption.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateInstanceDatastoreOption.

        数据库版本。DDS社区版支持3.4、3.2和4.0版本，DDS增强版仅支持3.4版本。 取值： - 社区版引擎取“3.4”、“3.2”或“4.0”。 - 增强版引擎取“3.4”。

        :param version: The version of this CreateInstanceDatastoreOption.
        :type: str
        """
        self._version = version

    @property
    def storage_engine(self):
        """Gets the storage_engine of this CreateInstanceDatastoreOption.

        存储引擎。DDS社区版支持WiredTiger存储引擎，DDS增强版支持RocksDB存储引擎。 取值： - 社区版引擎取“wiredTiger”。 - 增强版引擎取“rocksDB”。

        :return: The storage_engine of this CreateInstanceDatastoreOption.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        """Sets the storage_engine of this CreateInstanceDatastoreOption.

        存储引擎。DDS社区版支持WiredTiger存储引擎，DDS增强版支持RocksDB存储引擎。 取值： - 社区版引擎取“wiredTiger”。 - 增强版引擎取“rocksDB”。

        :param storage_engine: The storage_engine of this CreateInstanceDatastoreOption.
        :type: str
        """
        self._storage_engine = storage_engine

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
        if not isinstance(other, CreateInstanceDatastoreOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
