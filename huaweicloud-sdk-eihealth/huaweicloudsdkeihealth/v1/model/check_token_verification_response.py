# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTokenVerificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expires_time': 'datetime',
        'project': 'ProjectDto',
        'roles': 'list[RoleDto]',
        'user': 'UserDto'
    }

    attribute_map = {
        'expires_time': 'expires_time',
        'project': 'project',
        'roles': 'roles',
        'user': 'user'
    }

    def __init__(self, expires_time=None, project=None, roles=None, user=None):
        r"""CheckTokenVerificationResponse

        The model defined in huaweicloud sdk

        :param expires_time: 过期时间
        :type expires_time: datetime
        :param project: 
        :type project: :class:`huaweicloudsdkeihealth.v1.ProjectDto`
        :param roles: 角色
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.RoleDto`]
        :param user: 
        :type user: :class:`huaweicloudsdkeihealth.v1.UserDto`
        """
        
        super(CheckTokenVerificationResponse, self).__init__()

        self._expires_time = None
        self._project = None
        self._roles = None
        self._user = None
        self.discriminator = None

        if expires_time is not None:
            self.expires_time = expires_time
        if project is not None:
            self.project = project
        if roles is not None:
            self.roles = roles
        if user is not None:
            self.user = user

    @property
    def expires_time(self):
        r"""Gets the expires_time of this CheckTokenVerificationResponse.

        过期时间

        :return: The expires_time of this CheckTokenVerificationResponse.
        :rtype: datetime
        """
        return self._expires_time

    @expires_time.setter
    def expires_time(self, expires_time):
        r"""Sets the expires_time of this CheckTokenVerificationResponse.

        过期时间

        :param expires_time: The expires_time of this CheckTokenVerificationResponse.
        :type expires_time: datetime
        """
        self._expires_time = expires_time

    @property
    def project(self):
        r"""Gets the project of this CheckTokenVerificationResponse.

        :return: The project of this CheckTokenVerificationResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ProjectDto`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this CheckTokenVerificationResponse.

        :param project: The project of this CheckTokenVerificationResponse.
        :type project: :class:`huaweicloudsdkeihealth.v1.ProjectDto`
        """
        self._project = project

    @property
    def roles(self):
        r"""Gets the roles of this CheckTokenVerificationResponse.

        角色

        :return: The roles of this CheckTokenVerificationResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.RoleDto`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this CheckTokenVerificationResponse.

        角色

        :param roles: The roles of this CheckTokenVerificationResponse.
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.RoleDto`]
        """
        self._roles = roles

    @property
    def user(self):
        r"""Gets the user of this CheckTokenVerificationResponse.

        :return: The user of this CheckTokenVerificationResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UserDto`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this CheckTokenVerificationResponse.

        :param user: The user of this CheckTokenVerificationResponse.
        :type user: :class:`huaweicloudsdkeihealth.v1.UserDto`
        """
        self._user = user

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
        if not isinstance(other, CheckTokenVerificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
