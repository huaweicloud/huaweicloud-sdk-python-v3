# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushRuleDevelopersDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'object',
        'user_id': 'object',
        'user_name': 'object',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, user_id=None, user_name=None, nick_name=None, tenant_name=None):
        r"""PushRuleDevelopersDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 主键ID。
        :type id: object
        :param user_id: **参数解释：** 用户ID。
        :type user_id: object
        :param user_name: **参数解释：** 用户名。
        :type user_name: object
        :param nick_name: **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tenant_name: str
        """
        
        

        self._id = None
        self._user_id = None
        self._user_name = None
        self._nick_name = None
        self._tenant_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        r"""Gets the id of this PushRuleDevelopersDto.

        **参数解释：** 主键ID。

        :return: The id of this PushRuleDevelopersDto.
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PushRuleDevelopersDto.

        **参数解释：** 主键ID。

        :param id: The id of this PushRuleDevelopersDto.
        :type id: object
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this PushRuleDevelopersDto.

        **参数解释：** 用户ID。

        :return: The user_id of this PushRuleDevelopersDto.
        :rtype: object
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this PushRuleDevelopersDto.

        **参数解释：** 用户ID。

        :param user_id: The user_id of this PushRuleDevelopersDto.
        :type user_id: object
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this PushRuleDevelopersDto.

        **参数解释：** 用户名。

        :return: The user_name of this PushRuleDevelopersDto.
        :rtype: object
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this PushRuleDevelopersDto.

        **参数解释：** 用户名。

        :param user_name: The user_name of this PushRuleDevelopersDto.
        :type user_name: object
        """
        self._user_name = user_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this PushRuleDevelopersDto.

        **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The nick_name of this PushRuleDevelopersDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this PushRuleDevelopersDto.

        **参数解释：** 昵称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param nick_name: The nick_name of this PushRuleDevelopersDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this PushRuleDevelopersDto.

        **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tenant_name of this PushRuleDevelopersDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this PushRuleDevelopersDto.

        **参数解释：** 租户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tenant_name: The tenant_name of this PushRuleDevelopersDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, PushRuleDevelopersDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
