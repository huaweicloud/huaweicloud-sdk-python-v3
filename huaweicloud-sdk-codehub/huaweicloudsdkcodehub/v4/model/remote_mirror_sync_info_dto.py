# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteMirrorSyncInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'password': 'str',
        'endpoint_uuid': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'endpoint_uuid': 'endpoint_uuid'
    }

    def __init__(self, username=None, password=None, endpoint_uuid=None):
        r"""RemoteMirrorSyncInfoDto

        The model defined in huaweicloud sdk

        :param username: **参数解释：** 用户名(需要base64加密)。
        :type username: str
        :param password: **参数解释：** 密码(需要base64加密)。
        :type password: str
        :param endpoint_uuid: **参数解释：** 拓展点uuid。
        :type endpoint_uuid: str
        """
        
        

        self._username = None
        self._password = None
        self._endpoint_uuid = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if endpoint_uuid is not None:
            self.endpoint_uuid = endpoint_uuid

    @property
    def username(self):
        r"""Gets the username of this RemoteMirrorSyncInfoDto.

        **参数解释：** 用户名(需要base64加密)。

        :return: The username of this RemoteMirrorSyncInfoDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RemoteMirrorSyncInfoDto.

        **参数解释：** 用户名(需要base64加密)。

        :param username: The username of this RemoteMirrorSyncInfoDto.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this RemoteMirrorSyncInfoDto.

        **参数解释：** 密码(需要base64加密)。

        :return: The password of this RemoteMirrorSyncInfoDto.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RemoteMirrorSyncInfoDto.

        **参数解释：** 密码(需要base64加密)。

        :param password: The password of this RemoteMirrorSyncInfoDto.
        :type password: str
        """
        self._password = password

    @property
    def endpoint_uuid(self):
        r"""Gets the endpoint_uuid of this RemoteMirrorSyncInfoDto.

        **参数解释：** 拓展点uuid。

        :return: The endpoint_uuid of this RemoteMirrorSyncInfoDto.
        :rtype: str
        """
        return self._endpoint_uuid

    @endpoint_uuid.setter
    def endpoint_uuid(self, endpoint_uuid):
        r"""Sets the endpoint_uuid of this RemoteMirrorSyncInfoDto.

        **参数解释：** 拓展点uuid。

        :param endpoint_uuid: The endpoint_uuid of this RemoteMirrorSyncInfoDto.
        :type endpoint_uuid: str
        """
        self._endpoint_uuid = endpoint_uuid

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
        if not isinstance(other, RemoteMirrorSyncInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
