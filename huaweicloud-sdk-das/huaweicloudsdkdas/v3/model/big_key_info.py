# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BigKeyInfo:

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
        'size': 'int',
        'db_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'db_id': 'db_id'
    }

    def __init__(self, name=None, type=None, size=None, db_id=None):
        r"""BigKeyInfo

        The model defined in huaweicloud sdk

        :param name: key名称
        :type name: str
        :param type: key类型。取值：string、hash、list、zset、set、stream、exhash
        :type type: str
        :param size: 长度或存储占用值
        :type size: int
        :param db_id: DB ID
        :type db_id: str
        """
        
        

        self._name = None
        self._type = None
        self._size = None
        self._db_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if db_id is not None:
            self.db_id = db_id

    @property
    def name(self):
        r"""Gets the name of this BigKeyInfo.

        key名称

        :return: The name of this BigKeyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BigKeyInfo.

        key名称

        :param name: The name of this BigKeyInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this BigKeyInfo.

        key类型。取值：string、hash、list、zset、set、stream、exhash

        :return: The type of this BigKeyInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BigKeyInfo.

        key类型。取值：string、hash、list、zset、set、stream、exhash

        :param type: The type of this BigKeyInfo.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this BigKeyInfo.

        长度或存储占用值

        :return: The size of this BigKeyInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BigKeyInfo.

        长度或存储占用值

        :param size: The size of this BigKeyInfo.
        :type size: int
        """
        self._size = size

    @property
    def db_id(self):
        r"""Gets the db_id of this BigKeyInfo.

        DB ID

        :return: The db_id of this BigKeyInfo.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this BigKeyInfo.

        DB ID

        :param db_id: The db_id of this BigKeyInfo.
        :type db_id: str
        """
        self._db_id = db_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BigKeyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
