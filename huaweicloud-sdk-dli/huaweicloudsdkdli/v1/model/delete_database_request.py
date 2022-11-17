# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        '_async': 'bool',
        'cascade': 'bool'
    }

    attribute_map = {
        'database_name': 'database_name',
        '_async': 'async',
        'cascade': 'cascade'
    }

    def __init__(self, database_name=None, _async=None, cascade=None):
        """DeleteDatabaseRequest

        The model defined in huaweicloud sdk

        :param database_name: 删除的数据库名称。
        :type database_name: str
        :param _async: 
        :type _async: bool
        :param cascade: 
        :type cascade: bool
        """
        
        

        self._database_name = None
        self.__async = None
        self._cascade = None
        self.discriminator = None

        self.database_name = database_name
        if _async is not None:
            self._async = _async
        if cascade is not None:
            self.cascade = cascade

    @property
    def database_name(self):
        """Gets the database_name of this DeleteDatabaseRequest.

        删除的数据库名称。

        :return: The database_name of this DeleteDatabaseRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DeleteDatabaseRequest.

        删除的数据库名称。

        :param database_name: The database_name of this DeleteDatabaseRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def _async(self):
        """Gets the _async of this DeleteDatabaseRequest.

        :return: The _async of this DeleteDatabaseRequest.
        :rtype: bool
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        """Sets the _async of this DeleteDatabaseRequest.

        :param _async: The _async of this DeleteDatabaseRequest.
        :type _async: bool
        """
        self.__async = _async

    @property
    def cascade(self):
        """Gets the cascade of this DeleteDatabaseRequest.

        :return: The cascade of this DeleteDatabaseRequest.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        """Sets the cascade of this DeleteDatabaseRequest.

        :param cascade: The cascade of this DeleteDatabaseRequest.
        :type cascade: bool
        """
        self._cascade = cascade

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
        if not isinstance(other, DeleteDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
