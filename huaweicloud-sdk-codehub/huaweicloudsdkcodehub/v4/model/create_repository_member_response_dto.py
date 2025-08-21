# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepositoryMemberResponseDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_iam_id': 'str',
        'user_name': 'str',
        'tenant_name': 'str',
        'user_nick_name': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'user_iam_id': 'user_iam_id',
        'user_name': 'user_name',
        'tenant_name': 'tenant_name',
        'user_nick_name': 'user_nick_name',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, user_iam_id=None, user_name=None, tenant_name=None, user_nick_name=None, status=None, message=None):
        r"""CreateRepositoryMemberResponseDto

        The model defined in huaweicloud sdk

        :param user_iam_id: **参数解释：** 用户iamId **约束限制：** 不涉及。
        :type user_iam_id: str
        :param user_name: **参数解释：** 用户名称。 **约束限制：** 不涉及。
        :type user_name: str
        :param tenant_name: **参数解释：** 租户名称。 **约束限制：** - 不涉及。
        :type tenant_name: str
        :param user_nick_name: **参数解释：** 用户昵称。 **约束限制：** - 不涉及。    
        :type user_nick_name: str
        :param status: **参数解释：** 角色id。 **约束限制：** **约束限制：** - success，添加成功。 - error，添加失败。  
        :type status: str
        :param message: **参数解释：** 成员添加结果信息。 **约束限制：** - 不涉及。    
        :type message: str
        """
        
        

        self._user_iam_id = None
        self._user_name = None
        self._tenant_name = None
        self._user_nick_name = None
        self._status = None
        self._message = None
        self.discriminator = None

        if user_iam_id is not None:
            self.user_iam_id = user_iam_id
        if user_name is not None:
            self.user_name = user_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if user_nick_name is not None:
            self.user_nick_name = user_nick_name
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def user_iam_id(self):
        r"""Gets the user_iam_id of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户iamId **约束限制：** 不涉及。

        :return: The user_iam_id of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._user_iam_id

    @user_iam_id.setter
    def user_iam_id(self, user_iam_id):
        r"""Sets the user_iam_id of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户iamId **约束限制：** 不涉及。

        :param user_iam_id: The user_iam_id of this CreateRepositoryMemberResponseDto.
        :type user_iam_id: str
        """
        self._user_iam_id = user_iam_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户名称。 **约束限制：** 不涉及。

        :return: The user_name of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户名称。 **约束限制：** 不涉及。

        :param user_name: The user_name of this CreateRepositoryMemberResponseDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 租户名称。 **约束限制：** - 不涉及。

        :return: The tenant_name of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 租户名称。 **约束限制：** - 不涉及。

        :param tenant_name: The tenant_name of this CreateRepositoryMemberResponseDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def user_nick_name(self):
        r"""Gets the user_nick_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户昵称。 **约束限制：** - 不涉及。    

        :return: The user_nick_name of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._user_nick_name

    @user_nick_name.setter
    def user_nick_name(self, user_nick_name):
        r"""Sets the user_nick_name of this CreateRepositoryMemberResponseDto.

        **参数解释：** 用户昵称。 **约束限制：** - 不涉及。    

        :param user_nick_name: The user_nick_name of this CreateRepositoryMemberResponseDto.
        :type user_nick_name: str
        """
        self._user_nick_name = user_nick_name

    @property
    def status(self):
        r"""Gets the status of this CreateRepositoryMemberResponseDto.

        **参数解释：** 角色id。 **约束限制：** **约束限制：** - success，添加成功。 - error，添加失败。  

        :return: The status of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateRepositoryMemberResponseDto.

        **参数解释：** 角色id。 **约束限制：** **约束限制：** - success，添加成功。 - error，添加失败。  

        :param status: The status of this CreateRepositoryMemberResponseDto.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this CreateRepositoryMemberResponseDto.

        **参数解释：** 成员添加结果信息。 **约束限制：** - 不涉及。    

        :return: The message of this CreateRepositoryMemberResponseDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateRepositoryMemberResponseDto.

        **参数解释：** 成员添加结果信息。 **约束限制：** - 不涉及。    

        :param message: The message of this CreateRepositoryMemberResponseDto.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, CreateRepositoryMemberResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
