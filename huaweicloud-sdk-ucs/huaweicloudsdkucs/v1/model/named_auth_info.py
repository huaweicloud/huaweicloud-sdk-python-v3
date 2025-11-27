# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamedAuthInfo:

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
        'user': 'AuthInfo'
    }

    attribute_map = {
        'name': 'name',
        'user': 'user'
    }

    def __init__(self, name=None, user=None):
        r"""NamedAuthInfo

        The model defined in huaweicloud sdk

        :param name: 用户名
        :type name: str
        :param user: 
        :type user: :class:`huaweicloudsdkucs.v1.AuthInfo`
        """
        
        

        self._name = None
        self._user = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user is not None:
            self.user = user

    @property
    def name(self):
        r"""Gets the name of this NamedAuthInfo.

        用户名

        :return: The name of this NamedAuthInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NamedAuthInfo.

        用户名

        :param name: The name of this NamedAuthInfo.
        :type name: str
        """
        self._name = name

    @property
    def user(self):
        r"""Gets the user of this NamedAuthInfo.

        :return: The user of this NamedAuthInfo.
        :rtype: :class:`huaweicloudsdkucs.v1.AuthInfo`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this NamedAuthInfo.

        :param user: The user of this NamedAuthInfo.
        :type user: :class:`huaweicloudsdkucs.v1.AuthInfo`
        """
        self._user = user

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
        if not isinstance(other, NamedAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
