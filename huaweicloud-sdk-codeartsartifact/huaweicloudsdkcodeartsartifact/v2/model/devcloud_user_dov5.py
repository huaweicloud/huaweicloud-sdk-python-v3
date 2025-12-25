# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevcloudUserDOV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'domain_id': 'str',
        'region': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'created_user_id': 'str',
        'created_user_name': 'str',
        'modified_user_id': 'str',
        'modified_user_name': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_type': 'str',
        'enabled': 'str',
        'repo_user_name': 'str',
        'repo_number': 'int',
        'inner_repo_user_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'domain_id': 'domain_id',
        'region': 'region',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'created_user_id': 'created_user_id',
        'created_user_name': 'created_user_name',
        'modified_user_id': 'modified_user_id',
        'modified_user_name': 'modified_user_name',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_type': 'user_type',
        'enabled': 'enabled',
        'repo_user_name': 'repo_user_name',
        'repo_number': 'repo_number',
        'inner_repo_user_name': 'inner_repo_user_name'
    }

    def __init__(self, status=None, domain_id=None, region=None, created_time=None, modified_time=None, created_user_id=None, created_user_name=None, modified_user_id=None, modified_user_name=None, user_id=None, user_name=None, user_type=None, enabled=None, repo_user_name=None, repo_number=None, inner_repo_user_name=None):
        r"""DevcloudUserDOV5

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 
        :type status: str
        :param domain_id: **参数解释**: 租户id。 **取值范围**: 不涉及。
        :type domain_id: str
        :param region: **参数解释**: 区域。 **取值范围**: 不涉及。
        :type region: str
        :param created_time: **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type created_time: str
        :param modified_time: **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type modified_time: str
        :param created_user_id: **参数解释**: 创建人id。 **取值范围**: 不涉及。
        :type created_user_id: str
        :param created_user_name: **参数解释**: 创建人。 **取值范围**: 不涉及。
        :type created_user_name: str
        :param modified_user_id: **参数解释**: 修改人id。 **取值范围**: 不涉及。
        :type modified_user_id: str
        :param modified_user_name: **参数解释**: 修改人。 **取值范围**: 不涉及。
        :type modified_user_name: str
        :param user_id: **参数解释**: 用户id。 **取值范围**: 不涉及。
        :type user_id: str
        :param user_name: **参数解释**: 用户名。 **取值范围**: 不涉及。
        :type user_name: str
        :param user_type: **参数解释**: 用户类型。 **取值范围**: 不涉及。
        :type user_type: str
        :param enabled: **参数解释**: enabled。 **取值范围**: 不涉及。
        :type enabled: str
        :param repo_user_name: **参数解释**: 仓库用户名。 **取值范围**: 不涉及。
        :type repo_user_name: str
        :param repo_number: **参数解释**: repo_number。 **取值范围**: 不涉及。
        :type repo_number: int
        :param inner_repo_user_name: **参数解释**: 内部仓库用户名。 **取值范围**: 不涉及。
        :type inner_repo_user_name: str
        """
        
        

        self._status = None
        self._domain_id = None
        self._region = None
        self._created_time = None
        self._modified_time = None
        self._created_user_id = None
        self._created_user_name = None
        self._modified_user_id = None
        self._modified_user_name = None
        self._user_id = None
        self._user_name = None
        self._user_type = None
        self._enabled = None
        self._repo_user_name = None
        self._repo_number = None
        self._inner_repo_user_name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if domain_id is not None:
            self.domain_id = domain_id
        if region is not None:
            self.region = region
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if created_user_id is not None:
            self.created_user_id = created_user_id
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if modified_user_id is not None:
            self.modified_user_id = modified_user_id
        if modified_user_name is not None:
            self.modified_user_name = modified_user_name
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type
        if enabled is not None:
            self.enabled = enabled
        if repo_user_name is not None:
            self.repo_user_name = repo_user_name
        if repo_number is not None:
            self.repo_number = repo_number
        if inner_repo_user_name is not None:
            self.inner_repo_user_name = inner_repo_user_name

    @property
    def status(self):
        r"""Gets the status of this DevcloudUserDOV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :return: The status of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DevcloudUserDOV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :param status: The status of this DevcloudUserDOV5.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DevcloudUserDOV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :return: The domain_id of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DevcloudUserDOV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :param domain_id: The domain_id of this DevcloudUserDOV5.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this DevcloudUserDOV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :return: The region of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DevcloudUserDOV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :param region: The region of this DevcloudUserDOV5.
        :type region: str
        """
        self._region = region

    @property
    def created_time(self):
        r"""Gets the created_time of this DevcloudUserDOV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The created_time of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this DevcloudUserDOV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param created_time: The created_time of this DevcloudUserDOV5.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this DevcloudUserDOV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The modified_time of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this DevcloudUserDOV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param modified_time: The modified_time of this DevcloudUserDOV5.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def created_user_id(self):
        r"""Gets the created_user_id of this DevcloudUserDOV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :return: The created_user_id of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        r"""Sets the created_user_id of this DevcloudUserDOV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :param created_user_id: The created_user_id of this DevcloudUserDOV5.
        :type created_user_id: str
        """
        self._created_user_id = created_user_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this DevcloudUserDOV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :return: The created_user_name of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this DevcloudUserDOV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :param created_user_name: The created_user_name of this DevcloudUserDOV5.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this DevcloudUserDOV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :return: The modified_user_id of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this DevcloudUserDOV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :param modified_user_id: The modified_user_id of this DevcloudUserDOV5.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this DevcloudUserDOV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :return: The modified_user_name of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this DevcloudUserDOV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :param modified_user_name: The modified_user_name of this DevcloudUserDOV5.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this DevcloudUserDOV5.

        **参数解释**: 用户id。 **取值范围**: 不涉及。

        :return: The user_id of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DevcloudUserDOV5.

        **参数解释**: 用户id。 **取值范围**: 不涉及。

        :param user_id: The user_id of this DevcloudUserDOV5.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this DevcloudUserDOV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :return: The user_name of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DevcloudUserDOV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :param user_name: The user_name of this DevcloudUserDOV5.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_type(self):
        r"""Gets the user_type of this DevcloudUserDOV5.

        **参数解释**: 用户类型。 **取值范围**: 不涉及。

        :return: The user_type of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this DevcloudUserDOV5.

        **参数解释**: 用户类型。 **取值范围**: 不涉及。

        :param user_type: The user_type of this DevcloudUserDOV5.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def enabled(self):
        r"""Gets the enabled of this DevcloudUserDOV5.

        **参数解释**: enabled。 **取值范围**: 不涉及。

        :return: The enabled of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this DevcloudUserDOV5.

        **参数解释**: enabled。 **取值范围**: 不涉及。

        :param enabled: The enabled of this DevcloudUserDOV5.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def repo_user_name(self):
        r"""Gets the repo_user_name of this DevcloudUserDOV5.

        **参数解释**: 仓库用户名。 **取值范围**: 不涉及。

        :return: The repo_user_name of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._repo_user_name

    @repo_user_name.setter
    def repo_user_name(self, repo_user_name):
        r"""Sets the repo_user_name of this DevcloudUserDOV5.

        **参数解释**: 仓库用户名。 **取值范围**: 不涉及。

        :param repo_user_name: The repo_user_name of this DevcloudUserDOV5.
        :type repo_user_name: str
        """
        self._repo_user_name = repo_user_name

    @property
    def repo_number(self):
        r"""Gets the repo_number of this DevcloudUserDOV5.

        **参数解释**: repo_number。 **取值范围**: 不涉及。

        :return: The repo_number of this DevcloudUserDOV5.
        :rtype: int
        """
        return self._repo_number

    @repo_number.setter
    def repo_number(self, repo_number):
        r"""Sets the repo_number of this DevcloudUserDOV5.

        **参数解释**: repo_number。 **取值范围**: 不涉及。

        :param repo_number: The repo_number of this DevcloudUserDOV5.
        :type repo_number: int
        """
        self._repo_number = repo_number

    @property
    def inner_repo_user_name(self):
        r"""Gets the inner_repo_user_name of this DevcloudUserDOV5.

        **参数解释**: 内部仓库用户名。 **取值范围**: 不涉及。

        :return: The inner_repo_user_name of this DevcloudUserDOV5.
        :rtype: str
        """
        return self._inner_repo_user_name

    @inner_repo_user_name.setter
    def inner_repo_user_name(self, inner_repo_user_name):
        r"""Sets the inner_repo_user_name of this DevcloudUserDOV5.

        **参数解释**: 内部仓库用户名。 **取值范围**: 不涉及。

        :param inner_repo_user_name: The inner_repo_user_name of this DevcloudUserDOV5.
        :type inner_repo_user_name: str
        """
        self._inner_repo_user_name = inner_repo_user_name

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
        if not isinstance(other, DevcloudUserDOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
