# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str',
        'white_remote_address': 'str',
        'admin': 'bool',
        'default_topic_perm': 'str',
        'default_group_perm': 'str',
        'topic_perms': 'list[UserTopicPerms]',
        'group_perms': 'list[UserGroupPerms]'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'white_remote_address': 'white_remote_address',
        'admin': 'admin',
        'default_topic_perm': 'default_topic_perm',
        'default_group_perm': 'default_group_perm',
        'topic_perms': 'topic_perms',
        'group_perms': 'group_perms'
    }

    def __init__(self, access_key=None, secret_key=None, white_remote_address=None, admin=None, default_topic_perm=None, default_group_perm=None, topic_perms=None, group_perms=None):
        """UpdateUserResponse

        The model defined in huaweicloud sdk

        :param access_key: 用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。
        :type access_key: str
        :param secret_key: 密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符&#x60;~!@#$%^&amp;*()-_&#x3D;+\\\\|[{}];:\\&#39;\\\&quot;,&lt;.&gt;/?密钥。 不能与名称或倒序的名称相同。
        :type secret_key: str
        :param white_remote_address: IP白名单。
        :type white_remote_address: str
        :param admin: 是否为管理员。
        :type admin: bool
        :param default_topic_perm: 默认的主题权限。
        :type default_topic_perm: str
        :param default_group_perm: 默认的消费组权限。
        :type default_group_perm: str
        :param topic_perms: 特殊的主题权限。
        :type topic_perms: list[:class:`huaweicloudsdkrocketmq.v2.UserTopicPerms`]
        :param group_perms: 特殊的消费组权限。
        :type group_perms: list[:class:`huaweicloudsdkrocketmq.v2.UserGroupPerms`]
        """
        
        super(UpdateUserResponse, self).__init__()

        self._access_key = None
        self._secret_key = None
        self._white_remote_address = None
        self._admin = None
        self._default_topic_perm = None
        self._default_group_perm = None
        self._topic_perms = None
        self._group_perms = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if white_remote_address is not None:
            self.white_remote_address = white_remote_address
        if admin is not None:
            self.admin = admin
        if default_topic_perm is not None:
            self.default_topic_perm = default_topic_perm
        if default_group_perm is not None:
            self.default_group_perm = default_group_perm
        if topic_perms is not None:
            self.topic_perms = topic_perms
        if group_perms is not None:
            self.group_perms = group_perms

    @property
    def access_key(self):
        """Gets the access_key of this UpdateUserResponse.

        用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。

        :return: The access_key of this UpdateUserResponse.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this UpdateUserResponse.

        用户名，只能英文字母开头，且由英文字母、数字、中划线、下划线组成，长度为7~64个字符。

        :param access_key: The access_key of this UpdateUserResponse.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this UpdateUserResponse.

        密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?密钥。 不能与名称或倒序的名称相同。

        :return: The secret_key of this UpdateUserResponse.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this UpdateUserResponse.

        密钥。 8-32个字符。 至少包含以下字符中的3种：   - 大写字母   - 小写字母   - 数字   - 特殊字符`~!@#$%^&*()-_=+\\\\|[{}];:\\'\\\",<.>/?密钥。 不能与名称或倒序的名称相同。

        :param secret_key: The secret_key of this UpdateUserResponse.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def white_remote_address(self):
        """Gets the white_remote_address of this UpdateUserResponse.

        IP白名单。

        :return: The white_remote_address of this UpdateUserResponse.
        :rtype: str
        """
        return self._white_remote_address

    @white_remote_address.setter
    def white_remote_address(self, white_remote_address):
        """Sets the white_remote_address of this UpdateUserResponse.

        IP白名单。

        :param white_remote_address: The white_remote_address of this UpdateUserResponse.
        :type white_remote_address: str
        """
        self._white_remote_address = white_remote_address

    @property
    def admin(self):
        """Gets the admin of this UpdateUserResponse.

        是否为管理员。

        :return: The admin of this UpdateUserResponse.
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this UpdateUserResponse.

        是否为管理员。

        :param admin: The admin of this UpdateUserResponse.
        :type admin: bool
        """
        self._admin = admin

    @property
    def default_topic_perm(self):
        """Gets the default_topic_perm of this UpdateUserResponse.

        默认的主题权限。

        :return: The default_topic_perm of this UpdateUserResponse.
        :rtype: str
        """
        return self._default_topic_perm

    @default_topic_perm.setter
    def default_topic_perm(self, default_topic_perm):
        """Sets the default_topic_perm of this UpdateUserResponse.

        默认的主题权限。

        :param default_topic_perm: The default_topic_perm of this UpdateUserResponse.
        :type default_topic_perm: str
        """
        self._default_topic_perm = default_topic_perm

    @property
    def default_group_perm(self):
        """Gets the default_group_perm of this UpdateUserResponse.

        默认的消费组权限。

        :return: The default_group_perm of this UpdateUserResponse.
        :rtype: str
        """
        return self._default_group_perm

    @default_group_perm.setter
    def default_group_perm(self, default_group_perm):
        """Sets the default_group_perm of this UpdateUserResponse.

        默认的消费组权限。

        :param default_group_perm: The default_group_perm of this UpdateUserResponse.
        :type default_group_perm: str
        """
        self._default_group_perm = default_group_perm

    @property
    def topic_perms(self):
        """Gets the topic_perms of this UpdateUserResponse.

        特殊的主题权限。

        :return: The topic_perms of this UpdateUserResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.UserTopicPerms`]
        """
        return self._topic_perms

    @topic_perms.setter
    def topic_perms(self, topic_perms):
        """Sets the topic_perms of this UpdateUserResponse.

        特殊的主题权限。

        :param topic_perms: The topic_perms of this UpdateUserResponse.
        :type topic_perms: list[:class:`huaweicloudsdkrocketmq.v2.UserTopicPerms`]
        """
        self._topic_perms = topic_perms

    @property
    def group_perms(self):
        """Gets the group_perms of this UpdateUserResponse.

        特殊的消费组权限。

        :return: The group_perms of this UpdateUserResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.UserGroupPerms`]
        """
        return self._group_perms

    @group_perms.setter
    def group_perms(self, group_perms):
        """Sets the group_perms of this UpdateUserResponse.

        特殊的消费组权限。

        :param group_perms: The group_perms of this UpdateUserResponse.
        :type group_perms: list[:class:`huaweicloudsdkrocketmq.v2.UserGroupPerms`]
        """
        self._group_perms = group_perms

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
        if not isinstance(other, UpdateUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
