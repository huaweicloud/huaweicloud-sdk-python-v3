# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'user_info': 'str'
    }

    attribute_map = {
        'org_id': 'org_id',
        'offset': 'offset',
        'limit': 'limit',
        'user_info': 'user_info'
    }

    def __init__(self, org_id=None, offset=None, limit=None, user_info=None):
        r"""ListUsersRequest

        The model defined in huaweicloud sdk

        :param org_id: 组织id，为空时查询所有用户。
        :type org_id: str
        :param offset: 第几页。最小值：0
        :type offset: int
        :param limit: 每页多少条。最小值：10。最大值：100
        :type limit: int
        :param user_info: 最长64位，用户名，支持模糊查询
        :type user_info: str
        """
        
        

        self._org_id = None
        self._offset = None
        self._limit = None
        self._user_info = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        self.offset = offset
        self.limit = limit
        if user_info is not None:
            self.user_info = user_info

    @property
    def org_id(self):
        r"""Gets the org_id of this ListUsersRequest.

        组织id，为空时查询所有用户。

        :return: The org_id of this ListUsersRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        r"""Sets the org_id of this ListUsersRequest.

        组织id，为空时查询所有用户。

        :param org_id: The org_id of this ListUsersRequest.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def offset(self):
        r"""Gets the offset of this ListUsersRequest.

        第几页。最小值：0

        :return: The offset of this ListUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUsersRequest.

        第几页。最小值：0

        :param offset: The offset of this ListUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUsersRequest.

        每页多少条。最小值：10。最大值：100

        :return: The limit of this ListUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUsersRequest.

        每页多少条。最小值：10。最大值：100

        :param limit: The limit of this ListUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def user_info(self):
        r"""Gets the user_info of this ListUsersRequest.

        最长64位，用户名，支持模糊查询

        :return: The user_info of this ListUsersRequest.
        :rtype: str
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        r"""Sets the user_info of this ListUsersRequest.

        最长64位，用户名，支持模糊查询

        :param user_info: The user_info of this ListUsersRequest.
        :type user_info: str
        """
        self._user_info = user_info

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
        if not isinstance(other, ListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
