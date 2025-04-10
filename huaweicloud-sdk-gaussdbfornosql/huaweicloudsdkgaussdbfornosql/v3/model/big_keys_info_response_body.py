# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BigKeysInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'int',
        'key_type': 'str',
        'key_name': 'str',
        'key_size': 'int'
    }

    attribute_map = {
        'db_id': 'db_id',
        'key_type': 'key_type',
        'key_name': 'key_name',
        'key_size': 'key_size'
    }

    def __init__(self, db_id=None, key_type=None, key_name=None, key_size=None):
        r"""BigKeysInfoResponseBody

        The model defined in huaweicloud sdk

        :param db_id: 大Key所在的DB。
        :type db_id: int
        :param key_type: 大Key类型。
        :type key_type: str
        :param key_name: 大Key名。
        :type key_name: str
        :param key_size: 大Key的长度。
        :type key_size: int
        """
        
        

        self._db_id = None
        self._key_type = None
        self._key_name = None
        self._key_size = None
        self.discriminator = None

        if db_id is not None:
            self.db_id = db_id
        if key_type is not None:
            self.key_type = key_type
        if key_name is not None:
            self.key_name = key_name
        if key_size is not None:
            self.key_size = key_size

    @property
    def db_id(self):
        r"""Gets the db_id of this BigKeysInfoResponseBody.

        大Key所在的DB。

        :return: The db_id of this BigKeysInfoResponseBody.
        :rtype: int
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this BigKeysInfoResponseBody.

        大Key所在的DB。

        :param db_id: The db_id of this BigKeysInfoResponseBody.
        :type db_id: int
        """
        self._db_id = db_id

    @property
    def key_type(self):
        r"""Gets the key_type of this BigKeysInfoResponseBody.

        大Key类型。

        :return: The key_type of this BigKeysInfoResponseBody.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        r"""Sets the key_type of this BigKeysInfoResponseBody.

        大Key类型。

        :param key_type: The key_type of this BigKeysInfoResponseBody.
        :type key_type: str
        """
        self._key_type = key_type

    @property
    def key_name(self):
        r"""Gets the key_name of this BigKeysInfoResponseBody.

        大Key名。

        :return: The key_name of this BigKeysInfoResponseBody.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this BigKeysInfoResponseBody.

        大Key名。

        :param key_name: The key_name of this BigKeysInfoResponseBody.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def key_size(self):
        r"""Gets the key_size of this BigKeysInfoResponseBody.

        大Key的长度。

        :return: The key_size of this BigKeysInfoResponseBody.
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        r"""Sets the key_size of this BigKeysInfoResponseBody.

        大Key的长度。

        :param key_size: The key_size of this BigKeysInfoResponseBody.
        :type key_size: int
        """
        self._key_size = key_size

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
        if not isinstance(other, BigKeysInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
