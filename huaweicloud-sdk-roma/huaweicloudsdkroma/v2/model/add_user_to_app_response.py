# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddUserToAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'id': 'str',
        'users': 'list[AppUsersUsers]'
    }

    attribute_map = {
        'total': 'total',
        'id': 'id',
        'users': 'users'
    }

    def __init__(self, total=None, id=None, users=None):
        r"""AddUserToAppResponse

        The model defined in huaweicloud sdk

        :param total: 应用的总成员数量
        :type total: int
        :param id: 应用ID
        :type id: str
        :param users: 用户成员列表
        :type users: list[:class:`huaweicloudsdkroma.v2.AppUsersUsers`]
        """
        
        super(AddUserToAppResponse, self).__init__()

        self._total = None
        self._id = None
        self._users = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if id is not None:
            self.id = id
        if users is not None:
            self.users = users

    @property
    def total(self):
        r"""Gets the total of this AddUserToAppResponse.

        应用的总成员数量

        :return: The total of this AddUserToAppResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AddUserToAppResponse.

        应用的总成员数量

        :param total: The total of this AddUserToAppResponse.
        :type total: int
        """
        self._total = total

    @property
    def id(self):
        r"""Gets the id of this AddUserToAppResponse.

        应用ID

        :return: The id of this AddUserToAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AddUserToAppResponse.

        应用ID

        :param id: The id of this AddUserToAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def users(self):
        r"""Gets the users of this AddUserToAppResponse.

        用户成员列表

        :return: The users of this AddUserToAppResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.AppUsersUsers`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this AddUserToAppResponse.

        用户成员列表

        :param users: The users of this AddUserToAppResponse.
        :type users: list[:class:`huaweicloudsdkroma.v2.AppUsersUsers`]
        """
        self._users = users

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
        if not isinstance(other, AddUserToAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
