# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrustedKeySpaceResponseBodyKeyspaces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyspace_id': 'str',
        'keyspace_name': 'str',
        'enterprise_project_id': 'str',
        'type': 'int',
        'state': 'int',
        'description': 'str',
        'created_by': 'str',
        'create_time': 'str',
        'last_modify_time': 'str'
    }

    attribute_map = {
        'keyspace_id': 'keyspace_id',
        'keyspace_name': 'keyspace_name',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'state': 'state',
        'description': 'description',
        'created_by': 'created_by',
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, keyspace_id=None, keyspace_name=None, enterprise_project_id=None, type=None, state=None, description=None, created_by=None, create_time=None, last_modify_time=None):
        r"""ListTrustedKeySpaceResponseBodyKeyspaces

        The model defined in huaweicloud sdk

        :param keyspace_id: **参数解释：** 密钥空间ID **取值范围：** 不涉及
        :type keyspace_id: str
        :param keyspace_name: **参数解释：** 密钥空间名称 **取值范围：** 不涉及
        :type keyspace_name: str
        :param enterprise_project_id: **参数解释：** 企业项目ID **取值范围：** 不涉及
        :type enterprise_project_id: str
        :param type: **参数解释：** 密钥空间类型 **取值范围：** 不涉及
        :type type: int
        :param state: **参数解释：** 密钥空间状态 **取值范围：** 1：启用，2：冻结
        :type state: int
        :param description: **参数解释：** 密钥空间描述信息 **取值范围：** 不涉及
        :type description: str
        :param created_by: **参数解释：** 密钥空间创建人 **取值范围：** 不涉及
        :type created_by: str
        :param create_time: **参数解释：** 密钥空间创建时间 **取值范围：** 不涉及
        :type create_time: str
        :param last_modify_time: **参数解释：** 密钥空间最近更新时间 **取值范围：** 不涉及
        :type last_modify_time: str
        """
        
        

        self._keyspace_id = None
        self._keyspace_name = None
        self._enterprise_project_id = None
        self._type = None
        self._state = None
        self._description = None
        self._created_by = None
        self._create_time = None
        self._last_modify_time = None
        self.discriminator = None

        self.keyspace_id = keyspace_id
        self.keyspace_name = keyspace_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.type = type
        self.state = state
        if description is not None:
            self.description = description
        self.created_by = created_by
        self.create_time = create_time
        self.last_modify_time = last_modify_time

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :return: The keyspace_id of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :param keyspace_id: The keyspace_id of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def keyspace_name(self):
        r"""Gets the keyspace_name of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间名称 **取值范围：** 不涉及

        :return: The keyspace_name of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._keyspace_name

    @keyspace_name.setter
    def keyspace_name(self, keyspace_name):
        r"""Sets the keyspace_name of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间名称 **取值范围：** 不涉及

        :param keyspace_name: The keyspace_name of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type keyspace_name: str
        """
        self._keyspace_name = keyspace_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 企业项目ID **取值范围：** 不涉及

        :return: The enterprise_project_id of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 企业项目ID **取值范围：** 不涉及

        :param enterprise_project_id: The enterprise_project_id of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间类型 **取值范围：** 不涉及

        :return: The type of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间类型 **取值范围：** 不涉及

        :param type: The type of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type type: int
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间状态 **取值范围：** 1：启用，2：冻结

        :return: The state of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间状态 **取值范围：** 1：启用，2：冻结

        :param state: The state of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type state: int
        """
        self._state = state

    @property
    def description(self):
        r"""Gets the description of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间描述信息 **取值范围：** 不涉及

        :return: The description of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间描述信息 **取值范围：** 不涉及

        :param description: The description of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        r"""Gets the created_by of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间创建人 **取值范围：** 不涉及

        :return: The created_by of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间创建人 **取值范围：** 不涉及

        :param created_by: The created_by of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间创建时间 **取值范围：** 不涉及

        :return: The create_time of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间创建时间 **取值范围：** 不涉及

        :param create_time: The create_time of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        r"""Gets the last_modify_time of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间最近更新时间 **取值范围：** 不涉及

        :return: The last_modify_time of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        r"""Sets the last_modify_time of this ListTrustedKeySpaceResponseBodyKeyspaces.

        **参数解释：** 密钥空间最近更新时间 **取值范围：** 不涉及

        :param last_modify_time: The last_modify_time of this ListTrustedKeySpaceResponseBodyKeyspaces.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

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
        if not isinstance(other, ListTrustedKeySpaceResponseBodyKeyspaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
