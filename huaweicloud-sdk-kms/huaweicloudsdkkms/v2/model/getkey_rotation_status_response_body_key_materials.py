# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetkeyRotationStatusResponseBodyKeyMaterials:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'material_id': 'str',
        'charge_id': 'str',
        'create_time': 'str',
        'expiration_time': 'str',
        'state': 'int'
    }

    attribute_map = {
        'material_id': 'material_id',
        'charge_id': 'charge_id',
        'create_time': 'create_time',
        'expiration_time': 'expiration_time',
        'state': 'state'
    }

    def __init__(self, material_id=None, charge_id=None, create_time=None, expiration_time=None, state=None):
        r"""GetkeyRotationStatusResponseBodyKeyMaterials

        The model defined in huaweicloud sdk

        :param material_id: **参数解释：** 密钥材料ID **取值范围：** uuid格式
        :type material_id: str
        :param charge_id: **参数解释：** 计费ID **取值范围：** 不涉及
        :type charge_id: str
        :param create_time: **参数解释：** 密钥材料创建时间 **取值范围：** 不涉及
        :type create_time: str
        :param expiration_time: **参数解释：** 密钥材料过期时间 **取值范围：** 不涉及
        :type expiration_time: str
        :param state: **参数解释：** 密钥材料状态 **取值范围：** 0：等待轮转状态；2：启用状态
        :type state: int
        """
        
        

        self._material_id = None
        self._charge_id = None
        self._create_time = None
        self._expiration_time = None
        self._state = None
        self.discriminator = None

        if material_id is not None:
            self.material_id = material_id
        if charge_id is not None:
            self.charge_id = charge_id
        if create_time is not None:
            self.create_time = create_time
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if state is not None:
            self.state = state

    @property
    def material_id(self):
        r"""Gets the material_id of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料ID **取值范围：** uuid格式

        :return: The material_id of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        r"""Sets the material_id of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料ID **取值范围：** uuid格式

        :param material_id: The material_id of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def charge_id(self):
        r"""Gets the charge_id of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 计费ID **取值范围：** 不涉及

        :return: The charge_id of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :rtype: str
        """
        return self._charge_id

    @charge_id.setter
    def charge_id(self, charge_id):
        r"""Sets the charge_id of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 计费ID **取值范围：** 不涉及

        :param charge_id: The charge_id of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :type charge_id: str
        """
        self._charge_id = charge_id

    @property
    def create_time(self):
        r"""Gets the create_time of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料创建时间 **取值范围：** 不涉及

        :return: The create_time of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料创建时间 **取值范围：** 不涉及

        :param create_time: The create_time of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料过期时间 **取值范围：** 不涉及

        :return: The expiration_time of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料过期时间 **取值范围：** 不涉及

        :param expiration_time: The expiration_time of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

    @property
    def state(self):
        r"""Gets the state of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料状态 **取值范围：** 0：等待轮转状态；2：启用状态

        :return: The state of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this GetkeyRotationStatusResponseBodyKeyMaterials.

        **参数解释：** 密钥材料状态 **取值范围：** 0：等待轮转状态；2：启用状态

        :param state: The state of this GetkeyRotationStatusResponseBodyKeyMaterials.
        :type state: int
        """
        self._state = state

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
        if not isinstance(other, GetkeyRotationStatusResponseBodyKeyMaterials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
