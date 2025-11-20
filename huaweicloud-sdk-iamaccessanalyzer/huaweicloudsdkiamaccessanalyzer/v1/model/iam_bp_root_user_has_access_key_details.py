# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IamBpRootUserHasAccessKeyDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_id': 'str',
        'last_accessed': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'last_accessed': 'last_accessed',
        'created_at': 'created_at'
    }

    def __init__(self, access_key_id=None, last_accessed=None, created_at=None):
        r"""IamBpRootUserHasAccessKeyDetails

        The model defined in huaweicloud sdk

        :param access_key_id: 用户访问密钥唯一标识符（ID）。
        :type access_key_id: str
        :param last_accessed: 用户访问密钥的最后访问时间。
        :type last_accessed: datetime
        :param created_at: 用户访问密钥的创建时间。
        :type created_at: datetime
        """
        
        

        self._access_key_id = None
        self._last_accessed = None
        self._created_at = None
        self.discriminator = None

        self.access_key_id = access_key_id
        if last_accessed is not None:
            self.last_accessed = last_accessed
        self.created_at = created_at

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥唯一标识符（ID）。

        :return: The access_key_id of this IamBpRootUserHasAccessKeyDetails.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥唯一标识符（ID）。

        :param access_key_id: The access_key_id of this IamBpRootUserHasAccessKeyDetails.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def last_accessed(self):
        r"""Gets the last_accessed of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥的最后访问时间。

        :return: The last_accessed of this IamBpRootUserHasAccessKeyDetails.
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        r"""Sets the last_accessed of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥的最后访问时间。

        :param last_accessed: The last_accessed of this IamBpRootUserHasAccessKeyDetails.
        :type last_accessed: datetime
        """
        self._last_accessed = last_accessed

    @property
    def created_at(self):
        r"""Gets the created_at of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥的创建时间。

        :return: The created_at of this IamBpRootUserHasAccessKeyDetails.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this IamBpRootUserHasAccessKeyDetails.

        用户访问密钥的创建时间。

        :param created_at: The created_at of this IamBpRootUserHasAccessKeyDetails.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, IamBpRootUserHasAccessKeyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
