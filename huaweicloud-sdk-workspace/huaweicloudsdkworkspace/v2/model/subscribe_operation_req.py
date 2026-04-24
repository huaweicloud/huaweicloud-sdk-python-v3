# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeOperationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project': 'SubscribeOperationReqProject',
        'users': 'list[CreateSubscribeUserInfo]',
        'usergroups': 'list[CreateSubscribeUserGroupInfo]'
    }

    attribute_map = {
        'project': 'project',
        'users': 'users',
        'usergroups': 'usergroups'
    }

    def __init__(self, project=None, users=None, usergroups=None):
        r"""SubscribeOperationReq

        The model defined in huaweicloud sdk

        :param project: 
        :type project: :class:`huaweicloudsdkworkspace.v2.SubscribeOperationReqProject`
        :param users: 用户信息列表
        :type users: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserInfo`]
        :param usergroups: 用户组信息列表
        :type usergroups: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserGroupInfo`]
        """
        
        

        self._project = None
        self._users = None
        self._usergroups = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if users is not None:
            self.users = users
        if usergroups is not None:
            self.usergroups = usergroups

    @property
    def project(self):
        r"""Gets the project of this SubscribeOperationReq.

        :return: The project of this SubscribeOperationReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SubscribeOperationReqProject`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this SubscribeOperationReq.

        :param project: The project of this SubscribeOperationReq.
        :type project: :class:`huaweicloudsdkworkspace.v2.SubscribeOperationReqProject`
        """
        self._project = project

    @property
    def users(self):
        r"""Gets the users of this SubscribeOperationReq.

        用户信息列表

        :return: The users of this SubscribeOperationReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this SubscribeOperationReq.

        用户信息列表

        :param users: The users of this SubscribeOperationReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserInfo`]
        """
        self._users = users

    @property
    def usergroups(self):
        r"""Gets the usergroups of this SubscribeOperationReq.

        用户组信息列表

        :return: The usergroups of this SubscribeOperationReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserGroupInfo`]
        """
        return self._usergroups

    @usergroups.setter
    def usergroups(self, usergroups):
        r"""Sets the usergroups of this SubscribeOperationReq.

        用户组信息列表

        :param usergroups: The usergroups of this SubscribeOperationReq.
        :type usergroups: list[:class:`huaweicloudsdkworkspace.v2.CreateSubscribeUserGroupInfo`]
        """
        self._usergroups = usergroups

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
        if not isinstance(other, SubscribeOperationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
