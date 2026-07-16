# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkspaceResponse:

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
        'auth_type': 'str',
        'enterprise_project_id': 'str',
        'update_time': 'int',
        'create_time': 'int',
        'enterprise_project_name': 'str',
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'status': 'str',
        'status_info': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'auth_type': 'auth_type',
        'enterprise_project_id': 'enterprise_project_id',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'enterprise_project_name': 'enterprise_project_name',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'status': 'status',
        'status_info': 'status_info'
    }

    def __init__(self, owner=None, auth_type=None, enterprise_project_id=None, update_time=None, create_time=None, enterprise_project_name=None, name=None, description=None, id=None, status=None, status_info=None):
        r"""WorkspaceResponse

        The model defined in huaweicloud sdk

        :param owner: 创建者名称。
        :type owner: str
        :param auth_type: 授权类型。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。
        :type auth_type: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param update_time: 最后修改时间，UTC。
        :type update_time: int
        :param create_time: 创建时间，UTC。
        :type create_time: int
        :param enterprise_project_name: 企业项目名称。
        :type enterprise_project_name: str
        :param name: 工作空间名称。
        :type name: str
        :param description: 工作空间描述。
        :type description: str
        :param id: 工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为&#39;0&#39;。
        :type id: str
        :param status: 工作空间状态。 - CREATE_FAILED：创建失败。 - NORMAL：状态正常。 - DELETING：正在删除。 - DELETE_FAILED：删除失败。
        :type status: str
        :param status_info: 状态描述，默认为空。该字段会补充显示状态的详细信息。如删除失败时，可通过该字段查看删除失败的原因。
        :type status_info: str
        """
        
        

        self._owner = None
        self._auth_type = None
        self._enterprise_project_id = None
        self._update_time = None
        self._create_time = None
        self._enterprise_project_name = None
        self._name = None
        self._description = None
        self._id = None
        self._status = None
        self._status_info = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if auth_type is not None:
            self.auth_type = auth_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if status_info is not None:
            self.status_info = status_info

    @property
    def owner(self):
        r"""Gets the owner of this WorkspaceResponse.

        创建者名称。

        :return: The owner of this WorkspaceResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this WorkspaceResponse.

        创建者名称。

        :param owner: The owner of this WorkspaceResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def auth_type(self):
        r"""Gets the auth_type of this WorkspaceResponse.

        授权类型。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :return: The auth_type of this WorkspaceResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this WorkspaceResponse.

        授权类型。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :param auth_type: The auth_type of this WorkspaceResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this WorkspaceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this WorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this WorkspaceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this WorkspaceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this WorkspaceResponse.

        最后修改时间，UTC。

        :return: The update_time of this WorkspaceResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WorkspaceResponse.

        最后修改时间，UTC。

        :param update_time: The update_time of this WorkspaceResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkspaceResponse.

        创建时间，UTC。

        :return: The create_time of this WorkspaceResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkspaceResponse.

        创建时间，UTC。

        :param create_time: The create_time of this WorkspaceResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this WorkspaceResponse.

        企业项目名称。

        :return: The enterprise_project_name of this WorkspaceResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this WorkspaceResponse.

        企业项目名称。

        :param enterprise_project_name: The enterprise_project_name of this WorkspaceResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def name(self):
        r"""Gets the name of this WorkspaceResponse.

        工作空间名称。

        :return: The name of this WorkspaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkspaceResponse.

        工作空间名称。

        :param name: The name of this WorkspaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WorkspaceResponse.

        工作空间描述。

        :return: The description of this WorkspaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkspaceResponse.

        工作空间描述。

        :param description: The description of this WorkspaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this WorkspaceResponse.

        工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为'0'。

        :return: The id of this WorkspaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkspaceResponse.

        工作空间ID，系统生成的32位UUID，不带橫线。默认的工作空间id为'0'。

        :param id: The id of this WorkspaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this WorkspaceResponse.

        工作空间状态。 - CREATE_FAILED：创建失败。 - NORMAL：状态正常。 - DELETING：正在删除。 - DELETE_FAILED：删除失败。

        :return: The status of this WorkspaceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkspaceResponse.

        工作空间状态。 - CREATE_FAILED：创建失败。 - NORMAL：状态正常。 - DELETING：正在删除。 - DELETE_FAILED：删除失败。

        :param status: The status of this WorkspaceResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_info(self):
        r"""Gets the status_info of this WorkspaceResponse.

        状态描述，默认为空。该字段会补充显示状态的详细信息。如删除失败时，可通过该字段查看删除失败的原因。

        :return: The status_info of this WorkspaceResponse.
        :rtype: str
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        r"""Sets the status_info of this WorkspaceResponse.

        状态描述，默认为空。该字段会补充显示状态的详细信息。如删除失败时，可通过该字段查看删除失败的原因。

        :param status_info: The status_info of this WorkspaceResponse.
        :type status_info: str
        """
        self._status_info = status_info

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
        if not isinstance(other, WorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
