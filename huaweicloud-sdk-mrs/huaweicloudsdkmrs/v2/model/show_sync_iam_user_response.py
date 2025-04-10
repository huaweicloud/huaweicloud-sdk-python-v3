# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSyncIamUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_names': 'list[str]',
        'group_names': 'list[str]'
    }

    attribute_map = {
        'user_names': 'user_names',
        'group_names': 'group_names'
    }

    def __init__(self, user_names=None, group_names=None):
        r"""ShowSyncIamUserResponse

        The model defined in huaweicloud sdk

        :param user_names: 已经同步了的用户
        :type user_names: list[str]
        :param group_names: 已经同步了的用户组
        :type group_names: list[str]
        """
        
        super(ShowSyncIamUserResponse, self).__init__()

        self._user_names = None
        self._group_names = None
        self.discriminator = None

        if user_names is not None:
            self.user_names = user_names
        if group_names is not None:
            self.group_names = group_names

    @property
    def user_names(self):
        r"""Gets the user_names of this ShowSyncIamUserResponse.

        已经同步了的用户

        :return: The user_names of this ShowSyncIamUserResponse.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        r"""Sets the user_names of this ShowSyncIamUserResponse.

        已经同步了的用户

        :param user_names: The user_names of this ShowSyncIamUserResponse.
        :type user_names: list[str]
        """
        self._user_names = user_names

    @property
    def group_names(self):
        r"""Gets the group_names of this ShowSyncIamUserResponse.

        已经同步了的用户组

        :return: The group_names of this ShowSyncIamUserResponse.
        :rtype: list[str]
        """
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        r"""Sets the group_names of this ShowSyncIamUserResponse.

        已经同步了的用户组

        :param group_names: The group_names of this ShowSyncIamUserResponse.
        :type group_names: list[str]
        """
        self._group_names = group_names

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
        if not isinstance(other, ShowSyncIamUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
