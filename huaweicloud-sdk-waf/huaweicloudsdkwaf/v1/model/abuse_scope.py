# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbuseScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'user_identifier': 'str'
    }

    attribute_map = {
        'type': 'type',
        'user_identifier': 'user_identifier'
    }

    def __init__(self, type=None, user_identifier=None):
        r"""AbuseScope

        The model defined in huaweicloud sdk

        :param type: 统计范围类型。all_users: 所有用户, single_user: 单个用户
        :type type: str
        :param user_identifier: 用户标识字段名，当前支持extra.end_user
        :type user_identifier: str
        """
        
        

        self._type = None
        self._user_identifier = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if user_identifier is not None:
            self.user_identifier = user_identifier

    @property
    def type(self):
        r"""Gets the type of this AbuseScope.

        统计范围类型。all_users: 所有用户, single_user: 单个用户

        :return: The type of this AbuseScope.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AbuseScope.

        统计范围类型。all_users: 所有用户, single_user: 单个用户

        :param type: The type of this AbuseScope.
        :type type: str
        """
        self._type = type

    @property
    def user_identifier(self):
        r"""Gets the user_identifier of this AbuseScope.

        用户标识字段名，当前支持extra.end_user

        :return: The user_identifier of this AbuseScope.
        :rtype: str
        """
        return self._user_identifier

    @user_identifier.setter
    def user_identifier(self, user_identifier):
        r"""Sets the user_identifier of this AbuseScope.

        用户标识字段名，当前支持extra.end_user

        :param user_identifier: The user_identifier of this AbuseScope.
        :type user_identifier: str
        """
        self._user_identifier = user_identifier

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
        if not isinstance(other, AbuseScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
