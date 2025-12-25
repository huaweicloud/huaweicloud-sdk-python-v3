# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcepServiceData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deprecated': 'bool',
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'deprecated': 'deprecated',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, deprecated=None, id=None, name=None, type=None):
        r"""VpcepServiceData

        The model defined in huaweicloud sdk

        :param deprecated: 已弃用
        :type deprecated: bool
        :param id: UUID
        :type id: str
        :param name: 所属租户名称
        :type name: str
        :param type: **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及
        :type type: str
        """
        
        

        self._deprecated = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        if deprecated is not None:
            self.deprecated = deprecated
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def deprecated(self):
        r"""Gets the deprecated of this VpcepServiceData.

        已弃用

        :return: The deprecated of this VpcepServiceData.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        r"""Sets the deprecated of this VpcepServiceData.

        已弃用

        :param deprecated: The deprecated of this VpcepServiceData.
        :type deprecated: bool
        """
        self._deprecated = deprecated

    @property
    def id(self):
        r"""Gets the id of this VpcepServiceData.

        UUID

        :return: The id of this VpcepServiceData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcepServiceData.

        UUID

        :param id: The id of this VpcepServiceData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VpcepServiceData.

        所属租户名称

        :return: The name of this VpcepServiceData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpcepServiceData.

        所属租户名称

        :param name: The name of this VpcepServiceData.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this VpcepServiceData.

        **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及

        :return: The type of this VpcepServiceData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VpcepServiceData.

        **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及

        :param type: The type of this VpcepServiceData.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, VpcepServiceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
