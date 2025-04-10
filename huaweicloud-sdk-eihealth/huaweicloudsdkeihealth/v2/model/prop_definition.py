# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropDefinition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'value_range': 'ValueRange',
        'optimal_range': 'ValueRange',
        'warning_range': 'ValueRange',
        'style': 'str',
        'confidential_interval': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'value_range': 'value_range',
        'optimal_range': 'optimal_range',
        'warning_range': 'warning_range',
        'style': 'style',
        'confidential_interval': 'confidential_interval'
    }

    def __init__(self, id=None, name=None, type=None, description=None, value_range=None, optimal_range=None, warning_range=None, style=None, confidential_interval=None):
        r"""PropDefinition

        The model defined in huaweicloud sdk

        :param id: 属性业务侧ID
        :type id: str
        :param name: 属性名称
        :type name: str
        :param type: 属性类型
        :type type: str
        :param description: 属性具体描述信息
        :type description: str
        :param value_range: 
        :type value_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        :param optimal_range: 
        :type optimal_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        :param warning_range: 
        :type warning_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        :param style: 模型参数呈现类型
        :type style: str
        :param confidential_interval: 模型推理是否呈现置信区间
        :type confidential_interval: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._value_range = None
        self._optimal_range = None
        self._warning_range = None
        self._style = None
        self._confidential_interval = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if value_range is not None:
            self.value_range = value_range
        if optimal_range is not None:
            self.optimal_range = optimal_range
        if warning_range is not None:
            self.warning_range = warning_range
        if style is not None:
            self.style = style
        if confidential_interval is not None:
            self.confidential_interval = confidential_interval

    @property
    def id(self):
        r"""Gets the id of this PropDefinition.

        属性业务侧ID

        :return: The id of this PropDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PropDefinition.

        属性业务侧ID

        :param id: The id of this PropDefinition.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PropDefinition.

        属性名称

        :return: The name of this PropDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PropDefinition.

        属性名称

        :param name: The name of this PropDefinition.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PropDefinition.

        属性类型

        :return: The type of this PropDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PropDefinition.

        属性类型

        :param type: The type of this PropDefinition.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this PropDefinition.

        属性具体描述信息

        :return: The description of this PropDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PropDefinition.

        属性具体描述信息

        :param description: The description of this PropDefinition.
        :type description: str
        """
        self._description = description

    @property
    def value_range(self):
        r"""Gets the value_range of this PropDefinition.

        :return: The value_range of this PropDefinition.
        :rtype: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this PropDefinition.

        :param value_range: The value_range of this PropDefinition.
        :type value_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        self._value_range = value_range

    @property
    def optimal_range(self):
        r"""Gets the optimal_range of this PropDefinition.

        :return: The optimal_range of this PropDefinition.
        :rtype: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        return self._optimal_range

    @optimal_range.setter
    def optimal_range(self, optimal_range):
        r"""Sets the optimal_range of this PropDefinition.

        :param optimal_range: The optimal_range of this PropDefinition.
        :type optimal_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        self._optimal_range = optimal_range

    @property
    def warning_range(self):
        r"""Gets the warning_range of this PropDefinition.

        :return: The warning_range of this PropDefinition.
        :rtype: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        return self._warning_range

    @warning_range.setter
    def warning_range(self, warning_range):
        r"""Sets the warning_range of this PropDefinition.

        :param warning_range: The warning_range of this PropDefinition.
        :type warning_range: :class:`huaweicloudsdkeihealth.v2.ValueRange`
        """
        self._warning_range = warning_range

    @property
    def style(self):
        r"""Gets the style of this PropDefinition.

        模型参数呈现类型

        :return: The style of this PropDefinition.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        r"""Sets the style of this PropDefinition.

        模型参数呈现类型

        :param style: The style of this PropDefinition.
        :type style: str
        """
        self._style = style

    @property
    def confidential_interval(self):
        r"""Gets the confidential_interval of this PropDefinition.

        模型推理是否呈现置信区间

        :return: The confidential_interval of this PropDefinition.
        :rtype: bool
        """
        return self._confidential_interval

    @confidential_interval.setter
    def confidential_interval(self, confidential_interval):
        r"""Sets the confidential_interval of this PropDefinition.

        模型推理是否呈现置信区间

        :param confidential_interval: The confidential_interval of this PropDefinition.
        :type confidential_interval: bool
        """
        self._confidential_interval = confidential_interval

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
        if not isinstance(other, PropDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
