# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPointResponseBodyAccessPoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_point_id': 'str',
        'keyspace_id': 'str',
        'access_point_name': 'str',
        'state': 'int',
        'type': 'int',
        'created_by': 'str',
        'create_time': 'str',
        'lsat_modify_time': 'str'
    }

    attribute_map = {
        'access_point_id': 'access_point_id',
        'keyspace_id': 'keyspace_id',
        'access_point_name': 'access_point_name',
        'state': 'state',
        'type': 'type',
        'created_by': 'created_by',
        'create_time': 'create_time',
        'lsat_modify_time': 'lsat_modify_time'
    }

    def __init__(self, access_point_id=None, keyspace_id=None, access_point_name=None, state=None, type=None, created_by=None, create_time=None, lsat_modify_time=None):
        r"""ListAccessPointResponseBodyAccessPoints

        The model defined in huaweicloud sdk

        :param access_point_id: **参数解释：** 接入点ID **取值范围：** 不涉及
        :type access_point_id: str
        :param keyspace_id: **参数解释：** 密钥空间ID **取值范围：** 不涉及
        :type keyspace_id: str
        :param access_point_name: **参数解释：** 接入点名称 **取值范围：** 不涉及
        :type access_point_name: str
        :param state: **参数解释：** 接入点状态 **取值范围：** 0:禁用，1：启用
        :type state: int
        :param type: **参数解释：** 接入点类型 **取值范围：** 1:ECS，2：CCE，3：Custom
        :type type: int
        :param created_by: **参数解释：** 接入点创建人 **取值范围：** 不涉及
        :type created_by: str
        :param create_time: **参数解释：** 接入点创建时间 **取值范围：** 不涉及
        :type create_time: str
        :param lsat_modify_time: **参数解释：** 接入点最近更新时间 **取值范围：** 不涉及
        :type lsat_modify_time: str
        """
        
        

        self._access_point_id = None
        self._keyspace_id = None
        self._access_point_name = None
        self._state = None
        self._type = None
        self._created_by = None
        self._create_time = None
        self._lsat_modify_time = None
        self.discriminator = None

        self.access_point_id = access_point_id
        self.keyspace_id = keyspace_id
        self.access_point_name = access_point_name
        self.state = state
        self.type = type
        self.created_by = created_by
        self.create_time = create_time
        self.lsat_modify_time = lsat_modify_time

    @property
    def access_point_id(self):
        r"""Gets the access_point_id of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点ID **取值范围：** 不涉及

        :return: The access_point_id of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._access_point_id

    @access_point_id.setter
    def access_point_id(self, access_point_id):
        r"""Sets the access_point_id of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点ID **取值范围：** 不涉及

        :param access_point_id: The access_point_id of this ListAccessPointResponseBodyAccessPoints.
        :type access_point_id: str
        """
        self._access_point_id = access_point_id

    @property
    def keyspace_id(self):
        r"""Gets the keyspace_id of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :return: The keyspace_id of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._keyspace_id

    @keyspace_id.setter
    def keyspace_id(self, keyspace_id):
        r"""Sets the keyspace_id of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 密钥空间ID **取值范围：** 不涉及

        :param keyspace_id: The keyspace_id of this ListAccessPointResponseBodyAccessPoints.
        :type keyspace_id: str
        """
        self._keyspace_id = keyspace_id

    @property
    def access_point_name(self):
        r"""Gets the access_point_name of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点名称 **取值范围：** 不涉及

        :return: The access_point_name of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._access_point_name

    @access_point_name.setter
    def access_point_name(self, access_point_name):
        r"""Sets the access_point_name of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点名称 **取值范围：** 不涉及

        :param access_point_name: The access_point_name of this ListAccessPointResponseBodyAccessPoints.
        :type access_point_name: str
        """
        self._access_point_name = access_point_name

    @property
    def state(self):
        r"""Gets the state of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点状态 **取值范围：** 0:禁用，1：启用

        :return: The state of this ListAccessPointResponseBodyAccessPoints.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点状态 **取值范围：** 0:禁用，1：启用

        :param state: The state of this ListAccessPointResponseBodyAccessPoints.
        :type state: int
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点类型 **取值范围：** 1:ECS，2：CCE，3：Custom

        :return: The type of this ListAccessPointResponseBodyAccessPoints.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点类型 **取值范围：** 1:ECS，2：CCE，3：Custom

        :param type: The type of this ListAccessPointResponseBodyAccessPoints.
        :type type: int
        """
        self._type = type

    @property
    def created_by(self):
        r"""Gets the created_by of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点创建人 **取值范围：** 不涉及

        :return: The created_by of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点创建人 **取值范围：** 不涉及

        :param created_by: The created_by of this ListAccessPointResponseBodyAccessPoints.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def create_time(self):
        r"""Gets the create_time of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点创建时间 **取值范围：** 不涉及

        :return: The create_time of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点创建时间 **取值范围：** 不涉及

        :param create_time: The create_time of this ListAccessPointResponseBodyAccessPoints.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lsat_modify_time(self):
        r"""Gets the lsat_modify_time of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点最近更新时间 **取值范围：** 不涉及

        :return: The lsat_modify_time of this ListAccessPointResponseBodyAccessPoints.
        :rtype: str
        """
        return self._lsat_modify_time

    @lsat_modify_time.setter
    def lsat_modify_time(self, lsat_modify_time):
        r"""Sets the lsat_modify_time of this ListAccessPointResponseBodyAccessPoints.

        **参数解释：** 接入点最近更新时间 **取值范围：** 不涉及

        :param lsat_modify_time: The lsat_modify_time of this ListAccessPointResponseBodyAccessPoints.
        :type lsat_modify_time: str
        """
        self._lsat_modify_time = lsat_modify_time

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
        if not isinstance(other, ListAccessPointResponseBodyAccessPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
