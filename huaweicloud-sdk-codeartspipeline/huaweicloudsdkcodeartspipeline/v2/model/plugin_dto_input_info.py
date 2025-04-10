# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDTOInputInfo:

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
        'default_value': 'str',
        'type': 'str',
        'validation': 'str',
        'layout_content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'default_value': 'default_value',
        'type': 'type',
        'validation': 'validation',
        'layout_content': 'layout_content'
    }

    def __init__(self, name=None, default_value=None, type=None, validation=None, layout_content=None):
        r"""PluginDTOInputInfo

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param default_value: 默认值
        :type default_value: str
        :param type: 输入类型
        :type type: str
        :param validation: 验证
        :type validation: str
        :param layout_content: 样式信息
        :type layout_content: str
        """
        
        

        self._name = None
        self._default_value = None
        self._type = None
        self._validation = None
        self._layout_content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if default_value is not None:
            self.default_value = default_value
        if type is not None:
            self.type = type
        if validation is not None:
            self.validation = validation
        if layout_content is not None:
            self.layout_content = layout_content

    @property
    def name(self):
        r"""Gets the name of this PluginDTOInputInfo.

        名称

        :return: The name of this PluginDTOInputInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PluginDTOInputInfo.

        名称

        :param name: The name of this PluginDTOInputInfo.
        :type name: str
        """
        self._name = name

    @property
    def default_value(self):
        r"""Gets the default_value of this PluginDTOInputInfo.

        默认值

        :return: The default_value of this PluginDTOInputInfo.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this PluginDTOInputInfo.

        默认值

        :param default_value: The default_value of this PluginDTOInputInfo.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def type(self):
        r"""Gets the type of this PluginDTOInputInfo.

        输入类型

        :return: The type of this PluginDTOInputInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PluginDTOInputInfo.

        输入类型

        :param type: The type of this PluginDTOInputInfo.
        :type type: str
        """
        self._type = type

    @property
    def validation(self):
        r"""Gets the validation of this PluginDTOInputInfo.

        验证

        :return: The validation of this PluginDTOInputInfo.
        :rtype: str
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        r"""Sets the validation of this PluginDTOInputInfo.

        验证

        :param validation: The validation of this PluginDTOInputInfo.
        :type validation: str
        """
        self._validation = validation

    @property
    def layout_content(self):
        r"""Gets the layout_content of this PluginDTOInputInfo.

        样式信息

        :return: The layout_content of this PluginDTOInputInfo.
        :rtype: str
        """
        return self._layout_content

    @layout_content.setter
    def layout_content(self, layout_content):
        r"""Sets the layout_content of this PluginDTOInputInfo.

        样式信息

        :param layout_content: The layout_content of this PluginDTOInputInfo.
        :type layout_content: str
        """
        self._layout_content = layout_content

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
        if not isinstance(other, PluginDTOInputInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
