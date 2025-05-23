# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultRootDb:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'db_encoding': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'db_encoding': 'db_encoding'
    }

    def __init__(self, db_name=None, db_encoding=None):
        r"""DefaultRootDb

        The model defined in huaweicloud sdk

        :param db_name: 库名。
        :type db_name: str
        :param db_encoding: 编码格式。
        :type db_encoding: str
        """
        
        

        self._db_name = None
        self._db_encoding = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if db_encoding is not None:
            self.db_encoding = db_encoding

    @property
    def db_name(self):
        r"""Gets the db_name of this DefaultRootDb.

        库名。

        :return: The db_name of this DefaultRootDb.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this DefaultRootDb.

        库名。

        :param db_name: The db_name of this DefaultRootDb.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_encoding(self):
        r"""Gets the db_encoding of this DefaultRootDb.

        编码格式。

        :return: The db_encoding of this DefaultRootDb.
        :rtype: str
        """
        return self._db_encoding

    @db_encoding.setter
    def db_encoding(self, db_encoding):
        r"""Sets the db_encoding of this DefaultRootDb.

        编码格式。

        :param db_encoding: The db_encoding of this DefaultRootDb.
        :type db_encoding: str
        """
        self._db_encoding = db_encoding

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
        if not isinstance(other, DefaultRootDb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
