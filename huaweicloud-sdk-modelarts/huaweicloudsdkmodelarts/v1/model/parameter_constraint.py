# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterConstraint:

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
        'editable': 'bool',
        'required': 'bool',
        'sensitive': 'bool',
        'valid_type': 'str',
        'valid_range': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'editable': 'editable',
        'required': 'required',
        'sensitive': 'sensitive',
        'valid_type': 'valid_type',
        'valid_range': 'valid_range'
    }

    def __init__(self, type=None, editable=None, required=None, sensitive=None, valid_type=None, valid_range=None):
        r"""ParameterConstraint

        The model defined in huaweicloud sdk

        :param type: 参数种类。
        :type type: str
        :param editable: 是否可编辑。
        :type editable: bool
        :param required: 是否必须。
        :type required: bool
        :param sensitive: 是否敏感。该功能暂未实现。
        :type sensitive: bool
        :param valid_type: 有效种类。
        :type valid_type: str
        :param valid_range: 有效范围。
        :type valid_range: list[str]
        """
        
        

        self._type = None
        self._editable = None
        self._required = None
        self._sensitive = None
        self._valid_type = None
        self._valid_range = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if editable is not None:
            self.editable = editable
        if required is not None:
            self.required = required
        if sensitive is not None:
            self.sensitive = sensitive
        if valid_type is not None:
            self.valid_type = valid_type
        if valid_range is not None:
            self.valid_range = valid_range

    @property
    def type(self):
        r"""Gets the type of this ParameterConstraint.

        参数种类。

        :return: The type of this ParameterConstraint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ParameterConstraint.

        参数种类。

        :param type: The type of this ParameterConstraint.
        :type type: str
        """
        self._type = type

    @property
    def editable(self):
        r"""Gets the editable of this ParameterConstraint.

        是否可编辑。

        :return: The editable of this ParameterConstraint.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        r"""Sets the editable of this ParameterConstraint.

        是否可编辑。

        :param editable: The editable of this ParameterConstraint.
        :type editable: bool
        """
        self._editable = editable

    @property
    def required(self):
        r"""Gets the required of this ParameterConstraint.

        是否必须。

        :return: The required of this ParameterConstraint.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this ParameterConstraint.

        是否必须。

        :param required: The required of this ParameterConstraint.
        :type required: bool
        """
        self._required = required

    @property
    def sensitive(self):
        r"""Gets the sensitive of this ParameterConstraint.

        是否敏感。该功能暂未实现。

        :return: The sensitive of this ParameterConstraint.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        r"""Sets the sensitive of this ParameterConstraint.

        是否敏感。该功能暂未实现。

        :param sensitive: The sensitive of this ParameterConstraint.
        :type sensitive: bool
        """
        self._sensitive = sensitive

    @property
    def valid_type(self):
        r"""Gets the valid_type of this ParameterConstraint.

        有效种类。

        :return: The valid_type of this ParameterConstraint.
        :rtype: str
        """
        return self._valid_type

    @valid_type.setter
    def valid_type(self, valid_type):
        r"""Sets the valid_type of this ParameterConstraint.

        有效种类。

        :param valid_type: The valid_type of this ParameterConstraint.
        :type valid_type: str
        """
        self._valid_type = valid_type

    @property
    def valid_range(self):
        r"""Gets the valid_range of this ParameterConstraint.

        有效范围。

        :return: The valid_range of this ParameterConstraint.
        :rtype: list[str]
        """
        return self._valid_range

    @valid_range.setter
    def valid_range(self, valid_range):
        r"""Sets the valid_range of this ParameterConstraint.

        有效范围。

        :param valid_range: The valid_range of this ParameterConstraint.
        :type valid_range: list[str]
        """
        self._valid_range = valid_range

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
        if not isinstance(other, ParameterConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
