# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserQuotaInfo:

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
        'quota': 'UserQuotaDetail'
    }

    attribute_map = {
        'user_id': 'user_id',
        'quota': 'quota'
    }

    def __init__(self, user_id=None, quota=None):
        r"""CreateUserQuotaInfo

        The model defined in huaweicloud sdk

        :param user_id: 子账户（用户）ID。
        :type user_id: str
        :param quota: 
        :type quota: :class:`huaweicloudsdkmetastudio.v1.UserQuotaDetail`
        """
        
        

        self._user_id = None
        self._quota = None
        self.discriminator = None

        self.user_id = user_id
        self.quota = quota

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateUserQuotaInfo.

        子账户（用户）ID。

        :return: The user_id of this CreateUserQuotaInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateUserQuotaInfo.

        子账户（用户）ID。

        :param user_id: The user_id of this CreateUserQuotaInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def quota(self):
        r"""Gets the quota of this CreateUserQuotaInfo.

        :return: The quota of this CreateUserQuotaInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UserQuotaDetail`
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this CreateUserQuotaInfo.

        :param quota: The quota of this CreateUserQuotaInfo.
        :type quota: :class:`huaweicloudsdkmetastudio.v1.UserQuotaDetail`
        """
        self._quota = quota

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
        if not isinstance(other, CreateUserQuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
