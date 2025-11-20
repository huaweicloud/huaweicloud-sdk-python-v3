# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'user_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'user_id': 'user_id'
    }

    def __init__(self, limit=None, offset=None, user_id=None):
        r"""ListUserQuotasRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param user_id: 用户id
        :type user_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._user_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if user_id is not None:
            self.user_id = user_id

    @property
    def limit(self):
        r"""Gets the limit of this ListUserQuotasRequest.

        每页显示的条目数量。

        :return: The limit of this ListUserQuotasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserQuotasRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListUserQuotasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserQuotasRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListUserQuotasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserQuotasRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListUserQuotasRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def user_id(self):
        r"""Gets the user_id of this ListUserQuotasRequest.

        用户id

        :return: The user_id of this ListUserQuotasRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListUserQuotasRequest.

        用户id

        :param user_id: The user_id of this ListUserQuotasRequest.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ListUserQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
