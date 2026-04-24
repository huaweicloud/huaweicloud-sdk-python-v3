# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscribeAiAssistantUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'users': 'list[SubscribeUserInfo]',
        'usergroups': 'list[SubscribeUserGroupInfo]',
        'project': 'SubscribeAiAssistantListResponseProject'
    }

    attribute_map = {
        'total_count': 'total_count',
        'users': 'users',
        'usergroups': 'usergroups',
        'project': 'project'
    }

    def __init__(self, total_count=None, users=None, usergroups=None, project=None):
        r"""ListSubscribeAiAssistantUsersResponse

        The model defined in huaweicloud sdk

        :param total_count: 订阅用户总数。
        :type total_count: int
        :param users: 订阅用户列表。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserInfo`]
        :param usergroups: 订阅用户组列表。
        :type usergroups: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserGroupInfo`]
        :param project: 
        :type project: :class:`huaweicloudsdkworkspace.v2.SubscribeAiAssistantListResponseProject`
        """
        
        super().__init__()

        self._total_count = None
        self._users = None
        self._usergroups = None
        self._project = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if users is not None:
            self.users = users
        if usergroups is not None:
            self.usergroups = usergroups
        if project is not None:
            self.project = project

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSubscribeAiAssistantUsersResponse.

        订阅用户总数。

        :return: The total_count of this ListSubscribeAiAssistantUsersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSubscribeAiAssistantUsersResponse.

        订阅用户总数。

        :param total_count: The total_count of this ListSubscribeAiAssistantUsersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def users(self):
        r"""Gets the users of this ListSubscribeAiAssistantUsersResponse.

        订阅用户列表。

        :return: The users of this ListSubscribeAiAssistantUsersResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListSubscribeAiAssistantUsersResponse.

        订阅用户列表。

        :param users: The users of this ListSubscribeAiAssistantUsersResponse.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserInfo`]
        """
        self._users = users

    @property
    def usergroups(self):
        r"""Gets the usergroups of this ListSubscribeAiAssistantUsersResponse.

        订阅用户组列表。

        :return: The usergroups of this ListSubscribeAiAssistantUsersResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserGroupInfo`]
        """
        return self._usergroups

    @usergroups.setter
    def usergroups(self, usergroups):
        r"""Sets the usergroups of this ListSubscribeAiAssistantUsersResponse.

        订阅用户组列表。

        :param usergroups: The usergroups of this ListSubscribeAiAssistantUsersResponse.
        :type usergroups: list[:class:`huaweicloudsdkworkspace.v2.SubscribeUserGroupInfo`]
        """
        self._usergroups = usergroups

    @property
    def project(self):
        r"""Gets the project of this ListSubscribeAiAssistantUsersResponse.

        :return: The project of this ListSubscribeAiAssistantUsersResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SubscribeAiAssistantListResponseProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this ListSubscribeAiAssistantUsersResponse.

        :param project: The project of this ListSubscribeAiAssistantUsersResponse.
        :type project: :class:`huaweicloudsdkworkspace.v2.SubscribeAiAssistantListResponseProject`
        """
        self._project = project

    def to_dict(self):
        import warnings
        warnings.warn("ListSubscribeAiAssistantUsersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListSubscribeAiAssistantUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
