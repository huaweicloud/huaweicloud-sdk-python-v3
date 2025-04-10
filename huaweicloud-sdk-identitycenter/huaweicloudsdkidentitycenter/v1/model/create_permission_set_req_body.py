# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePermissionSetReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'relay_state': 'str',
        'session_duration': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'relay_state': 'relay_state',
        'session_duration': 'session_duration',
        'tags': 'tags'
    }

    def __init__(self, description=None, name=None, relay_state=None, session_duration=None, tags=None):
        r"""CreatePermissionSetReqBody

        The model defined in huaweicloud sdk

        :param description: 权限集描述.
        :type description: str
        :param name: 权限集名称.
        :type name: str
        :param relay_state: 用于在联合身份验证过程中重定向应用程序中的用户
        :type relay_state: str
        :param session_duration: 应用程序用户会话在ISO-8601标准中有效的时间长度
        :type session_duration: str
        :param tags: 要附加到新权限集的标签
        :type tags: list[:class:`huaweicloudsdkidentitycenter.v1.TagDto`]
        """
        
        

        self._description = None
        self._name = None
        self._relay_state = None
        self._session_duration = None
        self._tags = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        if relay_state is not None:
            self.relay_state = relay_state
        if session_duration is not None:
            self.session_duration = session_duration
        if tags is not None:
            self.tags = tags

    @property
    def description(self):
        r"""Gets the description of this CreatePermissionSetReqBody.

        权限集描述.

        :return: The description of this CreatePermissionSetReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePermissionSetReqBody.

        权限集描述.

        :param description: The description of this CreatePermissionSetReqBody.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreatePermissionSetReqBody.

        权限集名称.

        :return: The name of this CreatePermissionSetReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePermissionSetReqBody.

        权限集名称.

        :param name: The name of this CreatePermissionSetReqBody.
        :type name: str
        """
        self._name = name

    @property
    def relay_state(self):
        r"""Gets the relay_state of this CreatePermissionSetReqBody.

        用于在联合身份验证过程中重定向应用程序中的用户

        :return: The relay_state of this CreatePermissionSetReqBody.
        :rtype: str
        """
        return self._relay_state

    @relay_state.setter
    def relay_state(self, relay_state):
        r"""Sets the relay_state of this CreatePermissionSetReqBody.

        用于在联合身份验证过程中重定向应用程序中的用户

        :param relay_state: The relay_state of this CreatePermissionSetReqBody.
        :type relay_state: str
        """
        self._relay_state = relay_state

    @property
    def session_duration(self):
        r"""Gets the session_duration of this CreatePermissionSetReqBody.

        应用程序用户会话在ISO-8601标准中有效的时间长度

        :return: The session_duration of this CreatePermissionSetReqBody.
        :rtype: str
        """
        return self._session_duration

    @session_duration.setter
    def session_duration(self, session_duration):
        r"""Sets the session_duration of this CreatePermissionSetReqBody.

        应用程序用户会话在ISO-8601标准中有效的时间长度

        :param session_duration: The session_duration of this CreatePermissionSetReqBody.
        :type session_duration: str
        """
        self._session_duration = session_duration

    @property
    def tags(self):
        r"""Gets the tags of this CreatePermissionSetReqBody.

        要附加到新权限集的标签

        :return: The tags of this CreatePermissionSetReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreatePermissionSetReqBody.

        要附加到新权限集的标签

        :param tags: The tags of this CreatePermissionSetReqBody.
        :type tags: list[:class:`huaweicloudsdkidentitycenter.v1.TagDto`]
        """
        self._tags = tags

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
        if not isinstance(other, CreatePermissionSetReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
