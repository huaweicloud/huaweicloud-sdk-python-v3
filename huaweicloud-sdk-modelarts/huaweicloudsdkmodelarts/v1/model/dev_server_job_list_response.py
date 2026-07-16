# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerJobListResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'user_name': 'str',
        'description': 'str',
        'type': 'str',
        'status': 'str',
        'abnormal_count': 'int',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_name': 'user_name',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'abnormal_count': 'abnormal_count',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, name=None, user_name=None, description=None, type=None, status=None, abnormal_count=None, create_at=None, update_at=None):
        r"""DevServerJobListResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：任务id。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：任务名称。 **取值范围**：不涉及。
        :type name: str
        :param user_name: **参数解释**：用户名。 **取值范围**：不涉及。
        :type user_name: str
        :param description: **参数解释**：任务描述。 **取值范围**：不涉及。
        :type description: str
        :param type: **参数解释**：任务类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY  等。
        :type type: str
        :param status: **参数解释**：任务状态。 **取值范围**：- PROCESSING,  -FINISHED,  -DELETED。
        :type status: str
        :param abnormal_count: **参数解释**：task失败的节点数量。 **取值范围**：不涉及。
        :type abnormal_count: int
        :param create_at: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type create_at: str
        :param update_at: **参数解释**：更新时间。 **取值范围**：不涉及。
        :type update_at: str
        """
        
        

        self._id = None
        self._name = None
        self._user_name = None
        self._description = None
        self._type = None
        self._status = None
        self._abnormal_count = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if abnormal_count is not None:
            self.abnormal_count = abnormal_count
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this DevServerJobListResponse.

        **参数解释**：任务id。 **取值范围**：不涉及。

        :return: The id of this DevServerJobListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DevServerJobListResponse.

        **参数解释**：任务id。 **取值范围**：不涉及。

        :param id: The id of this DevServerJobListResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DevServerJobListResponse.

        **参数解释**：任务名称。 **取值范围**：不涉及。

        :return: The name of this DevServerJobListResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DevServerJobListResponse.

        **参数解释**：任务名称。 **取值范围**：不涉及。

        :param name: The name of this DevServerJobListResponse.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this DevServerJobListResponse.

        **参数解释**：用户名。 **取值范围**：不涉及。

        :return: The user_name of this DevServerJobListResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DevServerJobListResponse.

        **参数解释**：用户名。 **取值范围**：不涉及。

        :param user_name: The user_name of this DevServerJobListResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def description(self):
        r"""Gets the description of this DevServerJobListResponse.

        **参数解释**：任务描述。 **取值范围**：不涉及。

        :return: The description of this DevServerJobListResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DevServerJobListResponse.

        **参数解释**：任务描述。 **取值范围**：不涉及。

        :param description: The description of this DevServerJobListResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this DevServerJobListResponse.

        **参数解释**：任务类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY  等。

        :return: The type of this DevServerJobListResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DevServerJobListResponse.

        **参数解释**：任务类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY  等。

        :param type: The type of this DevServerJobListResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this DevServerJobListResponse.

        **参数解释**：任务状态。 **取值范围**：- PROCESSING,  -FINISHED,  -DELETED。

        :return: The status of this DevServerJobListResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DevServerJobListResponse.

        **参数解释**：任务状态。 **取值范围**：- PROCESSING,  -FINISHED,  -DELETED。

        :param status: The status of this DevServerJobListResponse.
        :type status: str
        """
        self._status = status

    @property
    def abnormal_count(self):
        r"""Gets the abnormal_count of this DevServerJobListResponse.

        **参数解释**：task失败的节点数量。 **取值范围**：不涉及。

        :return: The abnormal_count of this DevServerJobListResponse.
        :rtype: int
        """
        return self._abnormal_count

    @abnormal_count.setter
    def abnormal_count(self, abnormal_count):
        r"""Sets the abnormal_count of this DevServerJobListResponse.

        **参数解释**：task失败的节点数量。 **取值范围**：不涉及。

        :param abnormal_count: The abnormal_count of this DevServerJobListResponse.
        :type abnormal_count: int
        """
        self._abnormal_count = abnormal_count

    @property
    def create_at(self):
        r"""Gets the create_at of this DevServerJobListResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The create_at of this DevServerJobListResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DevServerJobListResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param create_at: The create_at of this DevServerJobListResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this DevServerJobListResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :return: The update_at of this DevServerJobListResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this DevServerJobListResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :param update_at: The update_at of this DevServerJobListResponse.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, DevServerJobListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
