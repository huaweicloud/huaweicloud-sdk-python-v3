# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAdOuUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_infos': 'list[AdOuUserInfo]',
        'total_count': 'int',
        'enable_create_count': 'int'
    }

    attribute_map = {
        'user_infos': 'user_infos',
        'total_count': 'total_count',
        'enable_create_count': 'enable_create_count'
    }

    def __init__(self, user_infos=None, total_count=None, enable_create_count=None):
        r"""ListAdOuUsersResponse

        The model defined in huaweicloud sdk

        :param user_infos: OU对象。
        :type user_infos: list[:class:`huaweicloudsdkworkspace.v2.AdOuUserInfo`]
        :param total_count: 用户数。
        :type total_count: int
        :param enable_create_count: 可以创建的用户数量。
        :type enable_create_count: int
        """
        
        super(ListAdOuUsersResponse, self).__init__()

        self._user_infos = None
        self._total_count = None
        self._enable_create_count = None
        self.discriminator = None

        if user_infos is not None:
            self.user_infos = user_infos
        if total_count is not None:
            self.total_count = total_count
        if enable_create_count is not None:
            self.enable_create_count = enable_create_count

    @property
    def user_infos(self):
        r"""Gets the user_infos of this ListAdOuUsersResponse.

        OU对象。

        :return: The user_infos of this ListAdOuUsersResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AdOuUserInfo`]
        """
        return self._user_infos

    @user_infos.setter
    def user_infos(self, user_infos):
        r"""Sets the user_infos of this ListAdOuUsersResponse.

        OU对象。

        :param user_infos: The user_infos of this ListAdOuUsersResponse.
        :type user_infos: list[:class:`huaweicloudsdkworkspace.v2.AdOuUserInfo`]
        """
        self._user_infos = user_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAdOuUsersResponse.

        用户数。

        :return: The total_count of this ListAdOuUsersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAdOuUsersResponse.

        用户数。

        :param total_count: The total_count of this ListAdOuUsersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def enable_create_count(self):
        r"""Gets the enable_create_count of this ListAdOuUsersResponse.

        可以创建的用户数量。

        :return: The enable_create_count of this ListAdOuUsersResponse.
        :rtype: int
        """
        return self._enable_create_count

    @enable_create_count.setter
    def enable_create_count(self, enable_create_count):
        r"""Sets the enable_create_count of this ListAdOuUsersResponse.

        可以创建的用户数量。

        :param enable_create_count: The enable_create_count of this ListAdOuUsersResponse.
        :type enable_create_count: int
        """
        self._enable_create_count = enable_create_count

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
        if not isinstance(other, ListAdOuUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
