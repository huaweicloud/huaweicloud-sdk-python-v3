# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyGraphRespLockedData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_index': 'int',
        'hex': 'str',
        'decoded': 'str',
        'column_name': 'str'
    }

    attribute_map = {
        'field_index': 'field_index',
        'hex': 'hex',
        'decoded': 'decoded',
        'column_name': 'column_name'
    }

    def __init__(self, field_index=None, hex=None, decoded=None, column_name=None):
        r"""ShowDeadLockTopologyGraphRespLockedData

        The model defined in huaweicloud sdk

        :param field_index: 字段序号
        :type field_index: int
        :param hex: 十六进制原始值
        :type hex: str
        :param decoded: 可读解码值
        :type decoded: str
        :param column_name: 列名
        :type column_name: str
        """
        
        

        self._field_index = None
        self._hex = None
        self._decoded = None
        self._column_name = None
        self.discriminator = None

        self.field_index = field_index
        self.hex = hex
        self.decoded = decoded
        self.column_name = column_name

    @property
    def field_index(self):
        r"""Gets the field_index of this ShowDeadLockTopologyGraphRespLockedData.

        字段序号

        :return: The field_index of this ShowDeadLockTopologyGraphRespLockedData.
        :rtype: int
        """
        return self._field_index

    @field_index.setter
    def field_index(self, field_index):
        r"""Sets the field_index of this ShowDeadLockTopologyGraphRespLockedData.

        字段序号

        :param field_index: The field_index of this ShowDeadLockTopologyGraphRespLockedData.
        :type field_index: int
        """
        self._field_index = field_index

    @property
    def hex(self):
        r"""Gets the hex of this ShowDeadLockTopologyGraphRespLockedData.

        十六进制原始值

        :return: The hex of this ShowDeadLockTopologyGraphRespLockedData.
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        r"""Sets the hex of this ShowDeadLockTopologyGraphRespLockedData.

        十六进制原始值

        :param hex: The hex of this ShowDeadLockTopologyGraphRespLockedData.
        :type hex: str
        """
        self._hex = hex

    @property
    def decoded(self):
        r"""Gets the decoded of this ShowDeadLockTopologyGraphRespLockedData.

        可读解码值

        :return: The decoded of this ShowDeadLockTopologyGraphRespLockedData.
        :rtype: str
        """
        return self._decoded

    @decoded.setter
    def decoded(self, decoded):
        r"""Sets the decoded of this ShowDeadLockTopologyGraphRespLockedData.

        可读解码值

        :param decoded: The decoded of this ShowDeadLockTopologyGraphRespLockedData.
        :type decoded: str
        """
        self._decoded = decoded

    @property
    def column_name(self):
        r"""Gets the column_name of this ShowDeadLockTopologyGraphRespLockedData.

        列名

        :return: The column_name of this ShowDeadLockTopologyGraphRespLockedData.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this ShowDeadLockTopologyGraphRespLockedData.

        列名

        :param column_name: The column_name of this ShowDeadLockTopologyGraphRespLockedData.
        :type column_name: str
        """
        self._column_name = column_name

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
        if not isinstance(other, ShowDeadLockTopologyGraphRespLockedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
