# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBasicPluginResponse(SdkResponse):

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
        'name': 'str',
        'friendly_name': 'str',
        'category': 'str',
        'description': 'str',
        'version': 'str',
        'version_description': 'str',
        'inputs': 'list[NewExtensionInputs]',
        'data_source_bindings': 'list[NewExtensionDataSourceBindings]',
        'outputs': 'list[NewExtensionOutputs]',
        'execution': 'NewExtensionExecution'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'friendly_name': 'friendly_name',
        'category': 'category',
        'description': 'description',
        'version': 'version',
        'version_description': 'version_description',
        'inputs': 'inputs',
        'data_source_bindings': 'data_source_bindings',
        'outputs': 'outputs',
        'execution': 'execution'
    }

    def __init__(self, type=None, name=None, friendly_name=None, category=None, description=None, version=None, version_description=None, inputs=None, data_source_bindings=None, outputs=None, execution=None):
        r"""ShowBasicPluginResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 插件类型。 **取值范围**： 不涉及。 
        :type type: str
        :param name: **参数解释**： 插件名称。 **取值范围**： 不涉及。 
        :type name: str
        :param friendly_name: **参数解释**： 插件展示名。 **取值范围**： 不涉及。 
        :type friendly_name: str
        :param category: **参数解释**： 业务类型。 **取值范围**： 不涉及。 
        :type category: str
        :param description: **参数解释**： 插件描述。 **取值范围**： 不涉及。 
        :type description: str
        :param version: **参数解释**： 插件版本。 **取值范围**： 不涉及。 
        :type version: str
        :param version_description: **参数解释**： 插件版本说明。 **取值范围**： 不涉及。 
        :type version_description: str
        :param inputs: **参数解释**： 输入信息。 **取值范围**： 不涉及。 
        :type inputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        :param data_source_bindings: **参数解释**： 数据源绑定信息。 **取值范围**： 不涉及。 
        :type data_source_bindings: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionDataSourceBindings`]
        :param outputs: **参数解释**： 输出信息。 **取值范围**： 不涉及。 
        :type outputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionOutputs`]
        :param execution: 
        :type execution: :class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionExecution`
        """
        
        super(ShowBasicPluginResponse, self).__init__()

        self._type = None
        self._name = None
        self._friendly_name = None
        self._category = None
        self._description = None
        self._version = None
        self._version_description = None
        self._inputs = None
        self._data_source_bindings = None
        self._outputs = None
        self._execution = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if version_description is not None:
            self.version_description = version_description
        if inputs is not None:
            self.inputs = inputs
        if data_source_bindings is not None:
            self.data_source_bindings = data_source_bindings
        if outputs is not None:
            self.outputs = outputs
        if execution is not None:
            self.execution = execution

    @property
    def type(self):
        r"""Gets the type of this ShowBasicPluginResponse.

        **参数解释**： 插件类型。 **取值范围**： 不涉及。 

        :return: The type of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowBasicPluginResponse.

        **参数解释**： 插件类型。 **取值范围**： 不涉及。 

        :param type: The type of this ShowBasicPluginResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ShowBasicPluginResponse.

        **参数解释**： 插件名称。 **取值范围**： 不涉及。 

        :return: The name of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBasicPluginResponse.

        **参数解释**： 插件名称。 **取值范围**： 不涉及。 

        :param name: The name of this ShowBasicPluginResponse.
        :type name: str
        """
        self._name = name

    @property
    def friendly_name(self):
        r"""Gets the friendly_name of this ShowBasicPluginResponse.

        **参数解释**： 插件展示名。 **取值范围**： 不涉及。 

        :return: The friendly_name of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        r"""Sets the friendly_name of this ShowBasicPluginResponse.

        **参数解释**： 插件展示名。 **取值范围**： 不涉及。 

        :param friendly_name: The friendly_name of this ShowBasicPluginResponse.
        :type friendly_name: str
        """
        self._friendly_name = friendly_name

    @property
    def category(self):
        r"""Gets the category of this ShowBasicPluginResponse.

        **参数解释**： 业务类型。 **取值范围**： 不涉及。 

        :return: The category of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowBasicPluginResponse.

        **参数解释**： 业务类型。 **取值范围**： 不涉及。 

        :param category: The category of this ShowBasicPluginResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this ShowBasicPluginResponse.

        **参数解释**： 插件描述。 **取值范围**： 不涉及。 

        :return: The description of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowBasicPluginResponse.

        **参数解释**： 插件描述。 **取值范围**： 不涉及。 

        :param description: The description of this ShowBasicPluginResponse.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        r"""Gets the version of this ShowBasicPluginResponse.

        **参数解释**： 插件版本。 **取值范围**： 不涉及。 

        :return: The version of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowBasicPluginResponse.

        **参数解释**： 插件版本。 **取值范围**： 不涉及。 

        :param version: The version of this ShowBasicPluginResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_description(self):
        r"""Gets the version_description of this ShowBasicPluginResponse.

        **参数解释**： 插件版本说明。 **取值范围**： 不涉及。 

        :return: The version_description of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ShowBasicPluginResponse.

        **参数解释**： 插件版本说明。 **取值范围**： 不涉及。 

        :param version_description: The version_description of this ShowBasicPluginResponse.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def inputs(self):
        r"""Gets the inputs of this ShowBasicPluginResponse.

        **参数解释**： 输入信息。 **取值范围**： 不涉及。 

        :return: The inputs of this ShowBasicPluginResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this ShowBasicPluginResponse.

        **参数解释**： 输入信息。 **取值范围**： 不涉及。 

        :param inputs: The inputs of this ShowBasicPluginResponse.
        :type inputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        """
        self._inputs = inputs

    @property
    def data_source_bindings(self):
        r"""Gets the data_source_bindings of this ShowBasicPluginResponse.

        **参数解释**： 数据源绑定信息。 **取值范围**： 不涉及。 

        :return: The data_source_bindings of this ShowBasicPluginResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionDataSourceBindings`]
        """
        return self._data_source_bindings

    @data_source_bindings.setter
    def data_source_bindings(self, data_source_bindings):
        r"""Sets the data_source_bindings of this ShowBasicPluginResponse.

        **参数解释**： 数据源绑定信息。 **取值范围**： 不涉及。 

        :param data_source_bindings: The data_source_bindings of this ShowBasicPluginResponse.
        :type data_source_bindings: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionDataSourceBindings`]
        """
        self._data_source_bindings = data_source_bindings

    @property
    def outputs(self):
        r"""Gets the outputs of this ShowBasicPluginResponse.

        **参数解释**： 输出信息。 **取值范围**： 不涉及。 

        :return: The outputs of this ShowBasicPluginResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionOutputs`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this ShowBasicPluginResponse.

        **参数解释**： 输出信息。 **取值范围**： 不涉及。 

        :param outputs: The outputs of this ShowBasicPluginResponse.
        :type outputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionOutputs`]
        """
        self._outputs = outputs

    @property
    def execution(self):
        r"""Gets the execution of this ShowBasicPluginResponse.

        :return: The execution of this ShowBasicPluginResponse.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionExecution`
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        r"""Sets the execution of this ShowBasicPluginResponse.

        :param execution: The execution of this ShowBasicPluginResponse.
        :type execution: :class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionExecution`
        """
        self._execution = execution

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
        if not isinstance(other, ShowBasicPluginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
