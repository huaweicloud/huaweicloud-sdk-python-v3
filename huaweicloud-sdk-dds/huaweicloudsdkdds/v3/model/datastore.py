# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datastore:

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
        """Datastore

        The model defined in huaweicloud sdk

        :param type: 数据库版本类型。取值“DDS-Community”。
        :type type: str
        :param version: 数据库版本。支持3.4、3.2和4.0版本。取值为“3.4”、“3.2”或“4.0”。
        :type version: str
        :param storage_engine: 存储引擎。支持WiredTiger存储引擎。取值为“wiredTiger”。
        :type storage_engine: str
        """
        
        

        self._type = None
        self._version = None
        self._storage_engine = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.storage_engine = storage_engine

    @property
    def type(self):
        """Gets the type of this Datastore.

        数据库版本类型。取值“DDS-Community”。

        :return: The type of this Datastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datastore.

        数据库版本类型。取值“DDS-Community”。

        :param type: The type of this Datastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this Datastore.

        数据库版本。支持3.4、3.2和4.0版本。取值为“3.4”、“3.2”或“4.0”。

        :return: The version of this Datastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Datastore.

        数据库版本。支持3.4、3.2和4.0版本。取值为“3.4”、“3.2”或“4.0”。

        :param version: The version of this Datastore.
        :type version: str
        """
        self._version = version

    @property
    def storage_engine(self):
        """Gets the storage_engine of this Datastore.

        存储引擎。支持WiredTiger存储引擎。取值为“wiredTiger”。

        :return: The storage_engine of this Datastore.
        :rtype: str
        """
        return self._storage_engine

    @storage_engine.setter
    def storage_engine(self, storage_engine):
        """Sets the storage_engine of this Datastore.

        存储引擎。支持WiredTiger存储引擎。取值为“wiredTiger”。

        :param storage_engine: The storage_engine of this Datastore.
        :type storage_engine: str
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
        if not isinstance(other, Datastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
