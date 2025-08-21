# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepositoryMemberDto:

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
        'tenant_id': 'str',
        'repository_role_id': 'str'
    }

    attribute_map = {
        'user_iam_id': 'user_iam_id',
        'user_name': 'user_name',
        'tenant_name': 'tenant_name',
        'tenant_id': 'tenant_id',
        'repository_role_id': 'repository_role_Id'
    }

    def __init__(self, user_iam_id=None, user_name=None, tenant_name=None, tenant_id=None, repository_role_id=None):
        r"""CreateRepositoryMemberDto

        The model defined in huaweicloud sdk

        :param user_iam_id: **参数解释：** 用户iamId **约束限制：** 不涉及。
        :type user_iam_id: str
        :param user_name: **参数解释：** 用户名称。 **约束限制：** 不涉及。
        :type user_name: str
        :param tenant_name: **参数解释：** 租户名称。 **约束限制：** - 不涉及。
        :type tenant_name: str
        :param tenant_id: **参数解释：** 租户id。 **约束限制：** - 不涉及。    
        :type tenant_id: str
        :param repository_role_id: **参数解释：** 角色id。 **约束限制：** - 不涉及。    
        :type repository_role_id: str
        """
        
        

        self._user_iam_id = None
        self._user_name = None
        self._tenant_name = None
        self._tenant_id = None
        self._repository_role_id = None
        self.discriminator = None

        if user_iam_id is not None:
            self.user_iam_id = user_iam_id
        if user_name is not None:
            self.user_name = user_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if repository_role_id is not None:
            self.repository_role_id = repository_role_id

    @property
    def user_iam_id(self):
        r"""Gets the user_iam_id of this CreateRepositoryMemberDto.

        **参数解释：** 用户iamId **约束限制：** 不涉及。

        :return: The user_iam_id of this CreateRepositoryMemberDto.
        :rtype: str
        """
        return self._user_iam_id

    @user_iam_id.setter
    def user_iam_id(self, user_iam_id):
        r"""Sets the user_iam_id of this CreateRepositoryMemberDto.

        **参数解释：** 用户iamId **约束限制：** 不涉及。

        :param user_iam_id: The user_iam_id of this CreateRepositoryMemberDto.
        :type user_iam_id: str
        """
        self._user_iam_id = user_iam_id

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateRepositoryMemberDto.

        **参数解释：** 用户名称。 **约束限制：** 不涉及。

        :return: The user_name of this CreateRepositoryMemberDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateRepositoryMemberDto.

        **参数解释：** 用户名称。 **约束限制：** 不涉及。

        :param user_name: The user_name of this CreateRepositoryMemberDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this CreateRepositoryMemberDto.

        **参数解释：** 租户名称。 **约束限制：** - 不涉及。

        :return: The tenant_name of this CreateRepositoryMemberDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this CreateRepositoryMemberDto.

        **参数解释：** 租户名称。 **约束限制：** - 不涉及。

        :param tenant_name: The tenant_name of this CreateRepositoryMemberDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateRepositoryMemberDto.

        **参数解释：** 租户id。 **约束限制：** - 不涉及。    

        :return: The tenant_id of this CreateRepositoryMemberDto.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateRepositoryMemberDto.

        **参数解释：** 租户id。 **约束限制：** - 不涉及。    

        :param tenant_id: The tenant_id of this CreateRepositoryMemberDto.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def repository_role_id(self):
        r"""Gets the repository_role_id of this CreateRepositoryMemberDto.

        **参数解释：** 角色id。 **约束限制：** - 不涉及。    

        :return: The repository_role_id of this CreateRepositoryMemberDto.
        :rtype: str
        """
        return self._repository_role_id

    @repository_role_id.setter
    def repository_role_id(self, repository_role_id):
        r"""Sets the repository_role_id of this CreateRepositoryMemberDto.

        **参数解释：** 角色id。 **约束限制：** - 不涉及。    

        :param repository_role_id: The repository_role_id of this CreateRepositoryMemberDto.
        :type repository_role_id: str
        """
        self._repository_role_id = repository_role_id

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
        if not isinstance(other, CreateRepositoryMemberDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
