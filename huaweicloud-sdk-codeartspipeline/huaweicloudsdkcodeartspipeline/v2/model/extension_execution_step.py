# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionExecutionStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dsl_method': 'str',
        'display_name': 'str',
        'execution_mode': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'dsl_method': 'dslMethod',
        'display_name': 'displayName',
        'execution_mode': 'executionMode',
        'parameters': 'parameters'
    }

    def __init__(self, dsl_method=None, display_name=None, execution_mode=None, parameters=None):
        r"""ExtensionExecutionStep

        The model defined in huaweicloud sdk

        :param dsl_method: DSL方法名，如 preOperationsNpm/sh/releasemanArtifactsUploader
        :type dsl_method: str
        :param display_name: 步骤显示名
        :type display_name: str
        :param execution_mode: 执行模式，如 serial
        :type execution_mode: str
        :param parameters: 步骤参数，键值对，值多为 $${...} 变量引用语法。
        :type parameters: dict(str, str)
        """
        
        

        self._dsl_method = None
        self._display_name = None
        self._execution_mode = None
        self._parameters = None
        self.discriminator = None

        if dsl_method is not None:
            self.dsl_method = dsl_method
        if display_name is not None:
            self.display_name = display_name
        if execution_mode is not None:
            self.execution_mode = execution_mode
        if parameters is not None:
            self.parameters = parameters

    @property
    def dsl_method(self):
        r"""Gets the dsl_method of this ExtensionExecutionStep.

        DSL方法名，如 preOperationsNpm/sh/releasemanArtifactsUploader

        :return: The dsl_method of this ExtensionExecutionStep.
        :rtype: str
        """
        return self._dsl_method

    @dsl_method.setter
    def dsl_method(self, dsl_method):
        r"""Sets the dsl_method of this ExtensionExecutionStep.

        DSL方法名，如 preOperationsNpm/sh/releasemanArtifactsUploader

        :param dsl_method: The dsl_method of this ExtensionExecutionStep.
        :type dsl_method: str
        """
        self._dsl_method = dsl_method

    @property
    def display_name(self):
        r"""Gets the display_name of this ExtensionExecutionStep.

        步骤显示名

        :return: The display_name of this ExtensionExecutionStep.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ExtensionExecutionStep.

        步骤显示名

        :param display_name: The display_name of this ExtensionExecutionStep.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this ExtensionExecutionStep.

        执行模式，如 serial

        :return: The execution_mode of this ExtensionExecutionStep.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this ExtensionExecutionStep.

        执行模式，如 serial

        :param execution_mode: The execution_mode of this ExtensionExecutionStep.
        :type execution_mode: str
        """
        self._execution_mode = execution_mode

    @property
    def parameters(self):
        r"""Gets the parameters of this ExtensionExecutionStep.

        步骤参数，键值对，值多为 $${...} 变量引用语法。

        :return: The parameters of this ExtensionExecutionStep.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ExtensionExecutionStep.

        步骤参数，键值对，值多为 $${...} 变量引用语法。

        :param parameters: The parameters of this ExtensionExecutionStep.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

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
        if not isinstance(other, ExtensionExecutionStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
