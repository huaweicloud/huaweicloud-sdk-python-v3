# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IamBpMfaUnconfiguredDetails:

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
        'user_created_at': 'datetime'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_created_at': 'user_created_at'
    }

    def __init__(self, user_id=None, user_created_at=None):
        r"""IamBpMfaUnconfiguredDetails

        The model defined in huaweicloud sdk

        :param user_id: 用户的唯一标识符（ID）。
        :type user_id: str
        :param user_created_at: 用户的创建时间。
        :type user_created_at: datetime
        """
        
        

        self._user_id = None
        self._user_created_at = None
        self.discriminator = None

        self.user_id = user_id
        self.user_created_at = user_created_at

    @property
    def user_id(self):
        r"""Gets the user_id of this IamBpMfaUnconfiguredDetails.

        用户的唯一标识符（ID）。

        :return: The user_id of this IamBpMfaUnconfiguredDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this IamBpMfaUnconfiguredDetails.

        用户的唯一标识符（ID）。

        :param user_id: The user_id of this IamBpMfaUnconfiguredDetails.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_created_at(self):
        r"""Gets the user_created_at of this IamBpMfaUnconfiguredDetails.

        用户的创建时间。

        :return: The user_created_at of this IamBpMfaUnconfiguredDetails.
        :rtype: datetime
        """
        return self._user_created_at

    @user_created_at.setter
    def user_created_at(self, user_created_at):
        r"""Sets the user_created_at of this IamBpMfaUnconfiguredDetails.

        用户的创建时间。

        :param user_created_at: The user_created_at of this IamBpMfaUnconfiguredDetails.
        :type user_created_at: datetime
        """
        self._user_created_at = user_created_at

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
        if not isinstance(other, IamBpMfaUnconfiguredDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
