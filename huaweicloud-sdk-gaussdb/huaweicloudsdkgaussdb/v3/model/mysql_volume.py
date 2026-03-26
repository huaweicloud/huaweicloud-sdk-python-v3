# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'str',
        'type': 'str'
    }

    attribute_map = {
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, size=None, type=None):
        r"""MysqlVolume

        The model defined in huaweicloud sdk

        :param size: **参数解释**：  磁盘大小，单位GB。  **约束限制**：  必须为10的整数倍。创建按需实例时不可选。  **取值范围**：  10-128000。  **默认取值**：  10。
        :type size: str
        :param type: **参数解释**：  磁盘存储类型。  **约束限制**：  不涉及。  **取值范围**：  - DL6：DL6存储类型。 - DL5：DL5存储类型。  **默认取值**：  DL6。
        :type type: str
        """
        
        

        self._size = None
        self._type = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def size(self):
        r"""Gets the size of this MysqlVolume.

        **参数解释**：  磁盘大小，单位GB。  **约束限制**：  必须为10的整数倍。创建按需实例时不可选。  **取值范围**：  10-128000。  **默认取值**：  10。

        :return: The size of this MysqlVolume.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this MysqlVolume.

        **参数解释**：  磁盘大小，单位GB。  **约束限制**：  必须为10的整数倍。创建按需实例时不可选。  **取值范围**：  10-128000。  **默认取值**：  10。

        :param size: The size of this MysqlVolume.
        :type size: str
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this MysqlVolume.

        **参数解释**：  磁盘存储类型。  **约束限制**：  不涉及。  **取值范围**：  - DL6：DL6存储类型。 - DL5：DL5存储类型。  **默认取值**：  DL6。

        :return: The type of this MysqlVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MysqlVolume.

        **参数解释**：  磁盘存储类型。  **约束限制**：  不涉及。  **取值范围**：  - DL6：DL6存储类型。 - DL5：DL5存储类型。  **默认取值**：  DL6。

        :param type: The type of this MysqlVolume.
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
        if not isinstance(other, MysqlVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
