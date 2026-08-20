# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionParameterDisplaySettings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dev_cloud_control_type': 'str',
        'dev_cloud_control_type_default': 'str',
        'dev_cloud_control_type_select': 'list[str]',
        'dev_cloud_control_type_radio': 'list[ExtensionRadioOption]'
    }

    attribute_map = {
        'dev_cloud_control_type': 'DevCloud.ControlType',
        'dev_cloud_control_type_default': 'DevCloud.ControlType.Default',
        'dev_cloud_control_type_select': 'DevCloud.ControlType.Select',
        'dev_cloud_control_type_radio': 'DevCloud.ControlType.Radio'
    }

    def __init__(self, dev_cloud_control_type=None, dev_cloud_control_type_default=None, dev_cloud_control_type_select=None, dev_cloud_control_type_radio=None):
        r"""ExtensionParameterDisplaySettings

        The model defined in huaweicloud sdk

        :param dev_cloud_control_type: 控件类型，如 Select/CodeText/Radio/SingleLineText/Hidden
        :type dev_cloud_control_type: str
        :param dev_cloud_control_type_default: 默认选中值。可能为字符串，也可能为对象(如 {displayName, value})。
        :type dev_cloud_control_type_default: str
        :param dev_cloud_control_type_select: 下拉选项(Select类型)。
        :type dev_cloud_control_type_select: list[str]
        :param dev_cloud_control_type_radio: 单选选项(Radio类型)。
        :type dev_cloud_control_type_radio: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionRadioOption`]
        """
        
        

        self._dev_cloud_control_type = None
        self._dev_cloud_control_type_default = None
        self._dev_cloud_control_type_select = None
        self._dev_cloud_control_type_radio = None
        self.discriminator = None

        if dev_cloud_control_type is not None:
            self.dev_cloud_control_type = dev_cloud_control_type
        if dev_cloud_control_type_default is not None:
            self.dev_cloud_control_type_default = dev_cloud_control_type_default
        if dev_cloud_control_type_select is not None:
            self.dev_cloud_control_type_select = dev_cloud_control_type_select
        if dev_cloud_control_type_radio is not None:
            self.dev_cloud_control_type_radio = dev_cloud_control_type_radio

    @property
    def dev_cloud_control_type(self):
        r"""Gets the dev_cloud_control_type of this ExtensionParameterDisplaySettings.

        控件类型，如 Select/CodeText/Radio/SingleLineText/Hidden

        :return: The dev_cloud_control_type of this ExtensionParameterDisplaySettings.
        :rtype: str
        """
        return self._dev_cloud_control_type

    @dev_cloud_control_type.setter
    def dev_cloud_control_type(self, dev_cloud_control_type):
        r"""Sets the dev_cloud_control_type of this ExtensionParameterDisplaySettings.

        控件类型，如 Select/CodeText/Radio/SingleLineText/Hidden

        :param dev_cloud_control_type: The dev_cloud_control_type of this ExtensionParameterDisplaySettings.
        :type dev_cloud_control_type: str
        """
        self._dev_cloud_control_type = dev_cloud_control_type

    @property
    def dev_cloud_control_type_default(self):
        r"""Gets the dev_cloud_control_type_default of this ExtensionParameterDisplaySettings.

        默认选中值。可能为字符串，也可能为对象(如 {displayName, value})。

        :return: The dev_cloud_control_type_default of this ExtensionParameterDisplaySettings.
        :rtype: str
        """
        return self._dev_cloud_control_type_default

    @dev_cloud_control_type_default.setter
    def dev_cloud_control_type_default(self, dev_cloud_control_type_default):
        r"""Sets the dev_cloud_control_type_default of this ExtensionParameterDisplaySettings.

        默认选中值。可能为字符串，也可能为对象(如 {displayName, value})。

        :param dev_cloud_control_type_default: The dev_cloud_control_type_default of this ExtensionParameterDisplaySettings.
        :type dev_cloud_control_type_default: str
        """
        self._dev_cloud_control_type_default = dev_cloud_control_type_default

    @property
    def dev_cloud_control_type_select(self):
        r"""Gets the dev_cloud_control_type_select of this ExtensionParameterDisplaySettings.

        下拉选项(Select类型)。

        :return: The dev_cloud_control_type_select of this ExtensionParameterDisplaySettings.
        :rtype: list[str]
        """
        return self._dev_cloud_control_type_select

    @dev_cloud_control_type_select.setter
    def dev_cloud_control_type_select(self, dev_cloud_control_type_select):
        r"""Sets the dev_cloud_control_type_select of this ExtensionParameterDisplaySettings.

        下拉选项(Select类型)。

        :param dev_cloud_control_type_select: The dev_cloud_control_type_select of this ExtensionParameterDisplaySettings.
        :type dev_cloud_control_type_select: list[str]
        """
        self._dev_cloud_control_type_select = dev_cloud_control_type_select

    @property
    def dev_cloud_control_type_radio(self):
        r"""Gets the dev_cloud_control_type_radio of this ExtensionParameterDisplaySettings.

        单选选项(Radio类型)。

        :return: The dev_cloud_control_type_radio of this ExtensionParameterDisplaySettings.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionRadioOption`]
        """
        return self._dev_cloud_control_type_radio

    @dev_cloud_control_type_radio.setter
    def dev_cloud_control_type_radio(self, dev_cloud_control_type_radio):
        r"""Sets the dev_cloud_control_type_radio of this ExtensionParameterDisplaySettings.

        单选选项(Radio类型)。

        :param dev_cloud_control_type_radio: The dev_cloud_control_type_radio of this ExtensionParameterDisplaySettings.
        :type dev_cloud_control_type_radio: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionRadioOption`]
        """
        self._dev_cloud_control_type_radio = dev_cloud_control_type_radio

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
        if not isinstance(other, ExtensionParameterDisplaySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
