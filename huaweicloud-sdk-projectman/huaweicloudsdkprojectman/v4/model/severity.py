# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Severity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, name=None, id=None):
        r"""Severity

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 工作项的重要程度。 **取值范围：** - 关键 - 重要 - 一般 - 提示
        :type name: str
        :param id: **参数解释：** 重要程度id。 **取值范围：** 10 （关键） 11 （重要） 12 （一般） 13 （提示）
        :type id: int
        """
        
        

        self._name = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this Severity.

        **参数解释：** 工作项的重要程度。 **取值范围：** - 关键 - 重要 - 一般 - 提示

        :return: The name of this Severity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Severity.

        **参数解释：** 工作项的重要程度。 **取值范围：** - 关键 - 重要 - 一般 - 提示

        :param name: The name of this Severity.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Severity.

        **参数解释：** 重要程度id。 **取值范围：** 10 （关键） 11 （重要） 12 （一般） 13 （提示）

        :return: The id of this Severity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Severity.

        **参数解释：** 重要程度id。 **取值范围：** 10 （关键） 11 （重要） 12 （一般） 13 （提示）

        :param id: The id of this Severity.
        :type id: int
        """
        self._id = id

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
        if not isinstance(other, Severity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
