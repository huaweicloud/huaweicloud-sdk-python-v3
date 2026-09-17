# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDbDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, type=None, data=None):
        r"""ValidateDbDataReq

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 类型。 **取值范围**： - schema - table
        :type type: str
        :param data: schema或者table列表。
        :type data: list[str]
        """
        
        

        self._type = None
        self._data = None
        self.discriminator = None

        self.type = type
        self.data = data

    @property
    def type(self):
        r"""Gets the type of this ValidateDbDataReq.

        **参数解释**： 类型。 **取值范围**： - schema - table

        :return: The type of this ValidateDbDataReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ValidateDbDataReq.

        **参数解释**： 类型。 **取值范围**： - schema - table

        :param type: The type of this ValidateDbDataReq.
        :type type: str
        """
        self._type = type

    @property
    def data(self):
        r"""Gets the data of this ValidateDbDataReq.

        schema或者table列表。

        :return: The data of this ValidateDbDataReq.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ValidateDbDataReq.

        schema或者table列表。

        :param data: The data of this ValidateDbDataReq.
        :type data: list[str]
        """
        self._data = data

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
        if not isinstance(other, ValidateDbDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
