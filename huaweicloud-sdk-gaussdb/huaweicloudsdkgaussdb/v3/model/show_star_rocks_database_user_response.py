# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStarRocksDatabaseUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_details': 'list[ShowStarRocksDatabaseUsersUserDetails]',
        'total_count': 'int'
    }

    attribute_map = {
        'user_details': 'user_details',
        'total_count': 'total_count'
    }

    def __init__(self, user_details=None, total_count=None):
        """ShowStarRocksDatabaseUserResponse

        The model defined in huaweicloud sdk

        :param user_details: 数据库账户信息。
        :type user_details: list[:class:`huaweicloudsdkgaussdb.v3.ShowStarRocksDatabaseUsersUserDetails`]
        :param total_count: 数据库账户数量。
        :type total_count: int
        """
        
        super(ShowStarRocksDatabaseUserResponse, self).__init__()

        self._user_details = None
        self._total_count = None
        self.discriminator = None

        if user_details is not None:
            self.user_details = user_details
        if total_count is not None:
            self.total_count = total_count

    @property
    def user_details(self):
        """Gets the user_details of this ShowStarRocksDatabaseUserResponse.

        数据库账户信息。

        :return: The user_details of this ShowStarRocksDatabaseUserResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ShowStarRocksDatabaseUsersUserDetails`]
        """
        return self._user_details

    @user_details.setter
    def user_details(self, user_details):
        """Sets the user_details of this ShowStarRocksDatabaseUserResponse.

        数据库账户信息。

        :param user_details: The user_details of this ShowStarRocksDatabaseUserResponse.
        :type user_details: list[:class:`huaweicloudsdkgaussdb.v3.ShowStarRocksDatabaseUsersUserDetails`]
        """
        self._user_details = user_details

    @property
    def total_count(self):
        """Gets the total_count of this ShowStarRocksDatabaseUserResponse.

        数据库账户数量。

        :return: The total_count of this ShowStarRocksDatabaseUserResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowStarRocksDatabaseUserResponse.

        数据库账户数量。

        :param total_count: The total_count of this ShowStarRocksDatabaseUserResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowStarRocksDatabaseUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
