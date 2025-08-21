# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupMergeRequestCanBeAssignedReviewersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'username': 'str',
        'state': 'str',
        'service_license_status': 'int',
        'avatar_url': 'str',
        'avatar_path': 'str',
        'email': 'str',
        'name_cn': 'str',
        'web_url': 'str',
        'nick_name': 'str',
        'tenant_name': 'str',
        'error_message': 'str',
        'is_committer': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username',
        'state': 'state',
        'service_license_status': 'service_license_status',
        'avatar_url': 'avatar_url',
        'avatar_path': 'avatar_path',
        'email': 'email',
        'name_cn': 'name_cn',
        'web_url': 'web_url',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name',
        'error_message': 'error_message',
        'is_committer': 'is_committer'
    }

    def __init__(self, id=None, name=None, username=None, state=None, service_license_status=None, avatar_url=None, avatar_path=None, email=None, name_cn=None, web_url=None, nick_name=None, tenant_name=None, error_message=None, is_committer=None):
        r"""ListGroupMergeRequestCanBeAssignedReviewersResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 用户id。
        :type id: int
        :param name: **参数解释：** 用户名称。
        :type name: str
        :param username: **参数解释：** 用户名。
        :type username: str
        :param state: 用户状态
        :type state: str
        :param service_license_status: 服务级权限状态 0：停用 1：启用
        :type service_license_status: int
        :param avatar_url: 用户头像url
        :type avatar_url: str
        :param avatar_path: 用户头像路径
        :type avatar_path: str
        :param email: 用户邮箱
        :type email: str
        :param name_cn: 用户中文名称
        :type name_cn: str
        :param web_url: 用户个人首页
        :type web_url: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param error_message: **参数解释：** 部分查询接口校验到传参里的用户权限不足或不存在时，返回该用户但该字段不为空用于提示。
        :type error_message: str
        :param is_committer: **参数解释：** 是否为committer。
        :type is_committer: bool
        """
        
        super(ListGroupMergeRequestCanBeAssignedReviewersResponse, self).__init__()

        self._id = None
        self._name = None
        self._username = None
        self._state = None
        self._service_license_status = None
        self._avatar_url = None
        self._avatar_path = None
        self._email = None
        self._name_cn = None
        self._web_url = None
        self._nick_name = None
        self._tenant_name = None
        self._error_message = None
        self._is_committer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if state is not None:
            self.state = state
        if service_license_status is not None:
            self.service_license_status = service_license_status
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if avatar_path is not None:
            self.avatar_path = avatar_path
        if email is not None:
            self.email = email
        if name_cn is not None:
            self.name_cn = name_cn
        if web_url is not None:
            self.web_url = web_url
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if error_message is not None:
            self.error_message = error_message
        if is_committer is not None:
            self.is_committer = is_committer

    @property
    def id(self):
        r"""Gets the id of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户id。

        :return: The id of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户id。

        :param id: The id of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户名称。

        :return: The name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户名称。

        :param name: The name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户名。

        :return: The username of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 用户名。

        :param username: The username of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type username: str
        """
        self._username = username

    @property
    def state(self):
        r"""Gets the state of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户状态

        :return: The state of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户状态

        :param state: The state of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type state: str
        """
        self._state = state

    @property
    def service_license_status(self):
        r"""Gets the service_license_status of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        服务级权限状态 0：停用 1：启用

        :return: The service_license_status of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: int
        """
        return self._service_license_status

    @service_license_status.setter
    def service_license_status(self, service_license_status):
        r"""Sets the service_license_status of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        服务级权限状态 0：停用 1：启用

        :param service_license_status: The service_license_status of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type service_license_status: int
        """
        self._service_license_status = service_license_status

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户头像url

        :return: The avatar_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户头像url

        :param avatar_url: The avatar_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def avatar_path(self):
        r"""Gets the avatar_path of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户头像路径

        :return: The avatar_path of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._avatar_path

    @avatar_path.setter
    def avatar_path(self, avatar_path):
        r"""Sets the avatar_path of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户头像路径

        :param avatar_path: The avatar_path of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type avatar_path: str
        """
        self._avatar_path = avatar_path

    @property
    def email(self):
        r"""Gets the email of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户邮箱

        :return: The email of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户邮箱

        :param email: The email of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type email: str
        """
        self._email = email

    @property
    def name_cn(self):
        r"""Gets the name_cn of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户中文名称

        :return: The name_cn of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户中文名称

        :param name_cn: The name_cn of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type name_cn: str
        """
        self._name_cn = name_cn

    @property
    def web_url(self):
        r"""Gets the web_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户个人首页

        :return: The web_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户个人首页

        :param web_url: The web_url of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户昵称

        :return: The nick_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        用户昵称

        :param nick_name: The nick_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        租户名称

        :return: The tenant_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        租户名称

        :param tenant_name: The tenant_name of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def error_message(self):
        r"""Gets the error_message of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 部分查询接口校验到传参里的用户权限不足或不存在时，返回该用户但该字段不为空用于提示。

        :return: The error_message of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 部分查询接口校验到传参里的用户权限不足或不存在时，返回该用户但该字段不为空用于提示。

        :param error_message: The error_message of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def is_committer(self):
        r"""Gets the is_committer of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 是否为committer。

        :return: The is_committer of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :rtype: bool
        """
        return self._is_committer

    @is_committer.setter
    def is_committer(self, is_committer):
        r"""Sets the is_committer of this ListGroupMergeRequestCanBeAssignedReviewersResponse.

        **参数解释：** 是否为committer。

        :param is_committer: The is_committer of this ListGroupMergeRequestCanBeAssignedReviewersResponse.
        :type is_committer: bool
        """
        self._is_committer = is_committer

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
        if not isinstance(other, ListGroupMergeRequestCanBeAssignedReviewersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
