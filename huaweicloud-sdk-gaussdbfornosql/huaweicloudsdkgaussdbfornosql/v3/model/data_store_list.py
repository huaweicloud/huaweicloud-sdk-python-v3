# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataStoreList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'datastore_name': 'datastore_name',
        'version': 'version'
    }

    def __init__(self, datastore_name=None, version=None):
        """DataStoreList

        The model defined in huaweicloud sdk

        :param datastore_name: 数据库引擎。
        :type datastore_name: str
        :param version: 数据库引擎版本。
        :type version: str
        """
        
        

        self._datastore_name = None
        self._version = None
        self.discriminator = None

        self.datastore_name = datastore_name
        self.version = version

    @property
    def datastore_name(self):
        """Gets the datastore_name of this DataStoreList.

        数据库引擎。

        :return: The datastore_name of this DataStoreList.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this DataStoreList.

        数据库引擎。

        :param datastore_name: The datastore_name of this DataStoreList.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def version(self):
        """Gets the version of this DataStoreList.

        数据库引擎版本。

        :return: The version of this DataStoreList.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DataStoreList.

        数据库引擎版本。

        :param version: The version of this DataStoreList.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, DataStoreList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
