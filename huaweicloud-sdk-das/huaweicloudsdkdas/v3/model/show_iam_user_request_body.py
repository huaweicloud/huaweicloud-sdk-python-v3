# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIamUserRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_ids': 'str',
        'connection_id': 'str'
    }

    attribute_map = {
        'user_ids': 'user_ids',
        'connection_id': 'connection_id'
    }

    def __init__(self, user_ids=None, connection_id=None):
        r"""ShowIamUserRequestBody

        The model defined in huaweicloud sdk

        :param user_ids: 账号ID
        :type user_ids: str
        :param connection_id: 账号名称
        :type connection_id: str
        """
        
        

        self._user_ids = None
        self._connection_id = None
        self.discriminator = None

        if user_ids is not None:
            self.user_ids = user_ids
        if connection_id is not None:
            self.connection_id = connection_id

    @property
    def user_ids(self):
        r"""Gets the user_ids of this ShowIamUserRequestBody.

        账号ID

        :return: The user_ids of this ShowIamUserRequestBody.
        :rtype: str
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        r"""Sets the user_ids of this ShowIamUserRequestBody.

        账号ID

        :param user_ids: The user_ids of this ShowIamUserRequestBody.
        :type user_ids: str
        """
        self._user_ids = user_ids

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ShowIamUserRequestBody.

        账号名称

        :return: The connection_id of this ShowIamUserRequestBody.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ShowIamUserRequestBody.

        账号名称

        :param connection_id: The connection_id of this ShowIamUserRequestBody.
        :type connection_id: str
        """
        self._connection_id = connection_id

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
        if not isinstance(other, ShowIamUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
