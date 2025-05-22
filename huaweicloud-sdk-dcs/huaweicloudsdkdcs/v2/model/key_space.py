# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeySpace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_idx': 'str',
        'keys': 'str',
        'expires': 'str',
        'avg_ttl': 'str'
    }

    attribute_map = {
        'db_idx': 'db_idx',
        'keys': 'keys',
        'expires': 'expires',
        'avg_ttl': 'avg_ttl'
    }

    def __init__(self, db_idx=None, keys=None, expires=None, avg_ttl=None):
        r"""KeySpace

        The model defined in huaweicloud sdk

        :param db_idx: **参数解释**： db索引值。 **取值范围**： 不涉及。 
        :type db_idx: str
        :param keys: **参数解释**： 节点键数量。 **取值范围**： 不涉及。 
        :type keys: str
        :param expires: **参数解释**： 节点过期键数量。 **取值范围**： 不涉及。 
        :type expires: str
        :param avg_ttl: **参数解释**： 节点键的平均过期时间。 **取值范围**： 不涉及。
        :type avg_ttl: str
        """
        
        

        self._db_idx = None
        self._keys = None
        self._expires = None
        self._avg_ttl = None
        self.discriminator = None

        if db_idx is not None:
            self.db_idx = db_idx
        if keys is not None:
            self.keys = keys
        if expires is not None:
            self.expires = expires
        if avg_ttl is not None:
            self.avg_ttl = avg_ttl

    @property
    def db_idx(self):
        r"""Gets the db_idx of this KeySpace.

        **参数解释**： db索引值。 **取值范围**： 不涉及。 

        :return: The db_idx of this KeySpace.
        :rtype: str
        """
        return self._db_idx

    @db_idx.setter
    def db_idx(self, db_idx):
        r"""Sets the db_idx of this KeySpace.

        **参数解释**： db索引值。 **取值范围**： 不涉及。 

        :param db_idx: The db_idx of this KeySpace.
        :type db_idx: str
        """
        self._db_idx = db_idx

    @property
    def keys(self):
        r"""Gets the keys of this KeySpace.

        **参数解释**： 节点键数量。 **取值范围**： 不涉及。 

        :return: The keys of this KeySpace.
        :rtype: str
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this KeySpace.

        **参数解释**： 节点键数量。 **取值范围**： 不涉及。 

        :param keys: The keys of this KeySpace.
        :type keys: str
        """
        self._keys = keys

    @property
    def expires(self):
        r"""Gets the expires of this KeySpace.

        **参数解释**： 节点过期键数量。 **取值范围**： 不涉及。 

        :return: The expires of this KeySpace.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        r"""Sets the expires of this KeySpace.

        **参数解释**： 节点过期键数量。 **取值范围**： 不涉及。 

        :param expires: The expires of this KeySpace.
        :type expires: str
        """
        self._expires = expires

    @property
    def avg_ttl(self):
        r"""Gets the avg_ttl of this KeySpace.

        **参数解释**： 节点键的平均过期时间。 **取值范围**： 不涉及。

        :return: The avg_ttl of this KeySpace.
        :rtype: str
        """
        return self._avg_ttl

    @avg_ttl.setter
    def avg_ttl(self, avg_ttl):
        r"""Sets the avg_ttl of this KeySpace.

        **参数解释**： 节点键的平均过期时间。 **取值范围**： 不涉及。

        :param avg_ttl: The avg_ttl of this KeySpace.
        :type avg_ttl: str
        """
        self._avg_ttl = avg_ttl

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
        if not isinstance(other, KeySpace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
