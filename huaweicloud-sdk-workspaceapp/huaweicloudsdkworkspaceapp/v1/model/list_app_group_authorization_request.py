# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppGroupAuthorizationRequest:

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
        'app_group_id': 'str',
        'account': 'str',
        'account_type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'app_group_id': 'app_group_id',
        'account': 'account',
        'account_type': 'account_type'
    }

    def __init__(self, limit=None, offset=None, app_group_id=None, account=None, account_type=None):
        """ListAppGroupAuthorizationRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]
        :type limit: int
        :param offset: 查询的偏移量
        :type offset: int
        :param app_group_id: 应用组ID
        :type app_group_id: str
        :param account: 应用授权的用户(组)名称，精确查询。
        :type account: str
        :param account_type: 应用授权的用户(组)类型 * &#39;USER&#39; - 用户 * &#39;USER_GROUP&#39; - 用户组
        :type account_type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._app_group_id = None
        self._account = None
        self._account_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if account is not None:
            self.account = account
        if account_type is not None:
            self.account_type = account_type

    @property
    def limit(self):
        """Gets the limit of this ListAppGroupAuthorizationRequest.

        单次查询的大小[1-100]

        :return: The limit of this ListAppGroupAuthorizationRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppGroupAuthorizationRequest.

        单次查询的大小[1-100]

        :param limit: The limit of this ListAppGroupAuthorizationRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppGroupAuthorizationRequest.

        查询的偏移量

        :return: The offset of this ListAppGroupAuthorizationRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppGroupAuthorizationRequest.

        查询的偏移量

        :param offset: The offset of this ListAppGroupAuthorizationRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def app_group_id(self):
        """Gets the app_group_id of this ListAppGroupAuthorizationRequest.

        应用组ID

        :return: The app_group_id of this ListAppGroupAuthorizationRequest.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        """Sets the app_group_id of this ListAppGroupAuthorizationRequest.

        应用组ID

        :param app_group_id: The app_group_id of this ListAppGroupAuthorizationRequest.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def account(self):
        """Gets the account of this ListAppGroupAuthorizationRequest.

        应用授权的用户(组)名称，精确查询。

        :return: The account of this ListAppGroupAuthorizationRequest.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ListAppGroupAuthorizationRequest.

        应用授权的用户(组)名称，精确查询。

        :param account: The account of this ListAppGroupAuthorizationRequest.
        :type account: str
        """
        self._account = account

    @property
    def account_type(self):
        """Gets the account_type of this ListAppGroupAuthorizationRequest.

        应用授权的用户(组)类型 * 'USER' - 用户 * 'USER_GROUP' - 用户组

        :return: The account_type of this ListAppGroupAuthorizationRequest.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this ListAppGroupAuthorizationRequest.

        应用授权的用户(组)类型 * 'USER' - 用户 * 'USER_GROUP' - 用户组

        :param account_type: The account_type of this ListAppGroupAuthorizationRequest.
        :type account_type: str
        """
        self._account_type = account_type

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
        if not isinstance(other, ListAppGroupAuthorizationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
