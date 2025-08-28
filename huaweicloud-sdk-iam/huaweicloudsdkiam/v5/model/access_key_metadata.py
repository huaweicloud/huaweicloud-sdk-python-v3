# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessKeyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'access_key_id': 'str',
        'created_at': 'datetime',
        'status': 'AccessKeyStatus'
    }

    attribute_map = {
        'user_id': 'user_id',
        'access_key_id': 'access_key_id',
        'created_at': 'created_at',
        'status': 'status'
    }

    def __init__(self, user_id=None, access_key_id=None, created_at=None, status=None):
        r"""AccessKeyMetadata

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。
        :type user_id: str
        :param access_key_id: 永久访问密钥ID，即AK。
        :type access_key_id: str
        :param created_at: 访问密钥创建时间。
        :type created_at: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkiam.v5.AccessKeyStatus`
        """
        
        

        self._user_id = None
        self._access_key_id = None
        self._created_at = None
        self._status = None
        self.discriminator = None

        self.user_id = user_id
        self.access_key_id = access_key_id
        self.created_at = created_at
        self.status = status

    @property
    def user_id(self):
        r"""Gets the user_id of this AccessKeyMetadata.

        IAM用户ID。

        :return: The user_id of this AccessKeyMetadata.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this AccessKeyMetadata.

        IAM用户ID。

        :param user_id: The user_id of this AccessKeyMetadata.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this AccessKeyMetadata.

        永久访问密钥ID，即AK。

        :return: The access_key_id of this AccessKeyMetadata.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this AccessKeyMetadata.

        永久访问密钥ID，即AK。

        :param access_key_id: The access_key_id of this AccessKeyMetadata.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def created_at(self):
        r"""Gets the created_at of this AccessKeyMetadata.

        访问密钥创建时间。

        :return: The created_at of this AccessKeyMetadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AccessKeyMetadata.

        访问密钥创建时间。

        :param created_at: The created_at of this AccessKeyMetadata.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this AccessKeyMetadata.

        :return: The status of this AccessKeyMetadata.
        :rtype: :class:`huaweicloudsdkiam.v5.AccessKeyStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccessKeyMetadata.

        :param status: The status of this AccessKeyMetadata.
        :type status: :class:`huaweicloudsdkiam.v5.AccessKeyStatus`
        """
        self._status = status

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
        if not isinstance(other, AccessKeyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
