# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FeatureResult:

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
        'status': 'str',
        'description': 'str',
        'type': 'str',
        'value': 'str',
        'range': 'str',
        'range_description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'description': 'description',
        'type': 'type',
        'value': 'value',
        'range': 'range',
        'range_description': 'range_description'
    }

    def __init__(self, name=None, status=None, description=None, type=None, value=None, range=None, range_description=None):
        r"""FeatureResult

        The model defined in huaweicloud sdk

        :param name: 特性名称。
        :type name: str
        :param status: 特性是否开启。
        :type status: str
        :param description: 特性中文描述。
        :type description: str
        :param type: 特性值类型。
        :type type: str
        :param value: 特性值。
        :type value: str
        :param range: 特性值范围。
        :type range: str
        :param range_description: 特性范围描述。
        :type range_description: str
        """
        
        

        self._name = None
        self._status = None
        self._description = None
        self._type = None
        self._value = None
        self._range = None
        self._range_description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if range is not None:
            self.range = range
        if range_description is not None:
            self.range_description = range_description

    @property
    def name(self):
        r"""Gets the name of this FeatureResult.

        特性名称。

        :return: The name of this FeatureResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FeatureResult.

        特性名称。

        :param name: The name of this FeatureResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this FeatureResult.

        特性是否开启。

        :return: The status of this FeatureResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FeatureResult.

        特性是否开启。

        :param status: The status of this FeatureResult.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this FeatureResult.

        特性中文描述。

        :return: The description of this FeatureResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FeatureResult.

        特性中文描述。

        :param description: The description of this FeatureResult.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this FeatureResult.

        特性值类型。

        :return: The type of this FeatureResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FeatureResult.

        特性值类型。

        :param type: The type of this FeatureResult.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this FeatureResult.

        特性值。

        :return: The value of this FeatureResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this FeatureResult.

        特性值。

        :param value: The value of this FeatureResult.
        :type value: str
        """
        self._value = value

    @property
    def range(self):
        r"""Gets the range of this FeatureResult.

        特性值范围。

        :return: The range of this FeatureResult.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this FeatureResult.

        特性值范围。

        :param range: The range of this FeatureResult.
        :type range: str
        """
        self._range = range

    @property
    def range_description(self):
        r"""Gets the range_description of this FeatureResult.

        特性范围描述。

        :return: The range_description of this FeatureResult.
        :rtype: str
        """
        return self._range_description

    @range_description.setter
    def range_description(self, range_description):
        r"""Sets the range_description of this FeatureResult.

        特性范围描述。

        :param range_description: The range_description of this FeatureResult.
        :type range_description: str
        """
        self._range_description = range_description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeatureResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
