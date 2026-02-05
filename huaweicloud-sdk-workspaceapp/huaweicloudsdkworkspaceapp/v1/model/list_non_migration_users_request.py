# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNonMigrationUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'user_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'config_id': 'config_id',
        'user_name': 'user_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, config_id=None, user_name=None, offset=None, limit=None):
        r"""ListNonMigrationUsersRequest

        The model defined in huaweicloud sdk

        :param config_id: 热点会话迁移配置ID。
        :type config_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]。
        :type limit: int
        """
        
        

        self._config_id = None
        self._user_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.config_id = config_id
        if user_name is not None:
            self.user_name = user_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def config_id(self):
        r"""Gets the config_id of this ListNonMigrationUsersRequest.

        热点会话迁移配置ID。

        :return: The config_id of this ListNonMigrationUsersRequest.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        r"""Sets the config_id of this ListNonMigrationUsersRequest.

        热点会话迁移配置ID。

        :param config_id: The config_id of this ListNonMigrationUsersRequest.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListNonMigrationUsersRequest.

        用户名。

        :return: The user_name of this ListNonMigrationUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListNonMigrationUsersRequest.

        用户名。

        :param user_name: The user_name of this ListNonMigrationUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def offset(self):
        r"""Gets the offset of this ListNonMigrationUsersRequest.

        查询的偏移量。

        :return: The offset of this ListNonMigrationUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNonMigrationUsersRequest.

        查询的偏移量。

        :param offset: The offset of this ListNonMigrationUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNonMigrationUsersRequest.

        查询的数量，值区间[1-100]。

        :return: The limit of this ListNonMigrationUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNonMigrationUsersRequest.

        查询的数量，值区间[1-100]。

        :param limit: The limit of this ListNonMigrationUsersRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNonMigrationUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
