# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantRepositoryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'capacity': 'float',
        'status': 'int',
        'moderation_result': 'bool',
        'create_time': 'str',
        'member_number': 'int',
        'repository_id': 'int',
        'repository_name': 'str',
        'project_name': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'capacity': 'capacity',
        'status': 'status',
        'moderation_result': 'moderation_result',
        'create_time': 'create_time',
        'member_number': 'member_number',
        'repository_id': 'repository_id',
        'repository_name': 'repository_name',
        'project_name': 'project_name',
        'project_id': 'project_id'
    }

    def __init__(self, owner=None, capacity=None, status=None, moderation_result=None, create_time=None, member_number=None, repository_id=None, repository_name=None, project_name=None, project_id=None):
        r"""TenantRepositoryDto

        The model defined in huaweicloud sdk

        :param owner: **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。
        :type owner: str
        :param capacity: **参数解释：** 仓库容量,单位:MB,保留2位小数。 **取值范围：** 不涉及。
        :type capacity: float
        :param status: **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。
        :type status: int
        :param moderation_result: **参数解释：** 内容审核结果。 **取值范围：** true，审核通过。 false，审核未通过。
        :type moderation_result: bool
        :param create_time: **参数解释：** 创建时间。 **取值范围：** 不涉及。
        :type create_time: str
        :param member_number: **参数解释：** 成员数量。 **取值范围：** 不涉及。
        :type member_number: int
        :param repository_id: **参数解释：** 仓库Id。 **取值范围：** 不涉及。
        :type repository_id: int
        :param repository_name: **参数解释：** 仓库名。 **取值范围：** 不涉及。
        :type repository_name: str
        :param project_name: **参数解释：** 项目名。 **取值范围：** 不涉及。
        :type project_name: str
        :param project_id: **参数解释：** 项目Id。 **取值范围：** 不涉及。
        :type project_id: str
        """
        
        

        self._owner = None
        self._capacity = None
        self._status = None
        self._moderation_result = None
        self._create_time = None
        self._member_number = None
        self._repository_id = None
        self._repository_name = None
        self._project_name = None
        self._project_id = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if capacity is not None:
            self.capacity = capacity
        if status is not None:
            self.status = status
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if create_time is not None:
            self.create_time = create_time
        if member_number is not None:
            self.member_number = member_number
        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id

    @property
    def owner(self):
        r"""Gets the owner of this TenantRepositoryDto.

        **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。

        :return: The owner of this TenantRepositoryDto.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TenantRepositoryDto.

        **参数解释：** 仓库所有者。 **取值范围：** 字符串长度不少于1，不超过128。

        :param owner: The owner of this TenantRepositoryDto.
        :type owner: str
        """
        self._owner = owner

    @property
    def capacity(self):
        r"""Gets the capacity of this TenantRepositoryDto.

        **参数解释：** 仓库容量,单位:MB,保留2位小数。 **取值范围：** 不涉及。

        :return: The capacity of this TenantRepositoryDto.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this TenantRepositoryDto.

        **参数解释：** 仓库容量,单位:MB,保留2位小数。 **取值范围：** 不涉及。

        :param capacity: The capacity of this TenantRepositoryDto.
        :type capacity: float
        """
        self._capacity = capacity

    @property
    def status(self):
        r"""Gets the status of this TenantRepositoryDto.

        **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。

        :return: The status of this TenantRepositoryDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TenantRepositoryDto.

        **参数解释：** 仓库状态。 **取值范围：** - 0，正常。 - 3，冻结。 - 4，关闭。 - 5，清理中。 - 7，删除中。

        :param status: The status of this TenantRepositoryDto.
        :type status: int
        """
        self._status = status

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this TenantRepositoryDto.

        **参数解释：** 内容审核结果。 **取值范围：** true，审核通过。 false，审核未通过。

        :return: The moderation_result of this TenantRepositoryDto.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this TenantRepositoryDto.

        **参数解释：** 内容审核结果。 **取值范围：** true，审核通过。 false，审核未通过。

        :param moderation_result: The moderation_result of this TenantRepositoryDto.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def create_time(self):
        r"""Gets the create_time of this TenantRepositoryDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :return: The create_time of this TenantRepositoryDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TenantRepositoryDto.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。

        :param create_time: The create_time of this TenantRepositoryDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def member_number(self):
        r"""Gets the member_number of this TenantRepositoryDto.

        **参数解释：** 成员数量。 **取值范围：** 不涉及。

        :return: The member_number of this TenantRepositoryDto.
        :rtype: int
        """
        return self._member_number

    @member_number.setter
    def member_number(self, member_number):
        r"""Sets the member_number of this TenantRepositoryDto.

        **参数解释：** 成员数量。 **取值范围：** 不涉及。

        :param member_number: The member_number of this TenantRepositoryDto.
        :type member_number: int
        """
        self._member_number = member_number

    @property
    def repository_id(self):
        r"""Gets the repository_id of this TenantRepositoryDto.

        **参数解释：** 仓库Id。 **取值范围：** 不涉及。

        :return: The repository_id of this TenantRepositoryDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this TenantRepositoryDto.

        **参数解释：** 仓库Id。 **取值范围：** 不涉及。

        :param repository_id: The repository_id of this TenantRepositoryDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this TenantRepositoryDto.

        **参数解释：** 仓库名。 **取值范围：** 不涉及。

        :return: The repository_name of this TenantRepositoryDto.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this TenantRepositoryDto.

        **参数解释：** 仓库名。 **取值范围：** 不涉及。

        :param repository_name: The repository_name of this TenantRepositoryDto.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def project_name(self):
        r"""Gets the project_name of this TenantRepositoryDto.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :return: The project_name of this TenantRepositoryDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TenantRepositoryDto.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :param project_name: The project_name of this TenantRepositoryDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this TenantRepositoryDto.

        **参数解释：** 项目Id。 **取值范围：** 不涉及。

        :return: The project_id of this TenantRepositoryDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TenantRepositoryDto.

        **参数解释：** 项目Id。 **取值范围：** 不涉及。

        :param project_id: The project_id of this TenantRepositoryDto.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, TenantRepositoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
