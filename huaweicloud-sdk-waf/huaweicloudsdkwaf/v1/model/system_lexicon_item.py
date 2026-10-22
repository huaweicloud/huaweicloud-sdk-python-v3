# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemLexiconItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'label': 'label',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, label=None, name=None, type=None):
        r"""SystemLexiconItem

        The model defined in huaweicloud sdk

        :param label: 词典编码
        :type label: str
        :param name: 词典名称
        :type name: str
        :param type: 词典类型
        :type type: str
        """
        
        

        self._label = None
        self._name = None
        self._type = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def label(self):
        r"""Gets the label of this SystemLexiconItem.

        词典编码

        :return: The label of this SystemLexiconItem.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this SystemLexiconItem.

        词典编码

        :param label: The label of this SystemLexiconItem.
        :type label: str
        """
        self._label = label

    @property
    def name(self):
        r"""Gets the name of this SystemLexiconItem.

        词典名称

        :return: The name of this SystemLexiconItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SystemLexiconItem.

        词典名称

        :param name: The name of this SystemLexiconItem.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this SystemLexiconItem.

        词典类型

        :return: The type of this SystemLexiconItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SystemLexiconItem.

        词典类型

        :param type: The type of this SystemLexiconItem.
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
        if not isinstance(other, SystemLexiconItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
