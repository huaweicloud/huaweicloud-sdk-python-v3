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
        'outputs': 'outputs',
        'execution': 'execution'
    }

    def __init__(self, type=None, name=None, friendly_name=None, category=None, description=None, version=None, version_description=None, inputs=None, outputs=None, execution=None):
        r"""ShowBasicPluginResponse

        The model defined in huaweicloud sdk

        :param type: 类型
        :type type: str
        :param name: 名称
        :type name: str
        :param friendly_name: 展示名
        :type friendly_name: str
        :param category: 业务类型
        :type category: str
        :param description: 描述
        :type description: str
        :param version: 版本
        :type version: str
        :param version_description: 版本说明
        :type version_description: str
        :param inputs: 输入信息
        :type inputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        :param outputs: 输出信息
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
        if outputs is not None:
            self.outputs = outputs
        if execution is not None:
            self.execution = execution

    @property
    def type(self):
        r"""Gets the type of this ShowBasicPluginResponse.

        类型

        :return: The type of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowBasicPluginResponse.

        类型

        :param type: The type of this ShowBasicPluginResponse.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ShowBasicPluginResponse.

        名称

        :return: The name of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBasicPluginResponse.

        名称

        :param name: The name of this ShowBasicPluginResponse.
        :type name: str
        """
        self._name = name

    @property
    def friendly_name(self):
        r"""Gets the friendly_name of this ShowBasicPluginResponse.

        展示名

        :return: The friendly_name of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        r"""Sets the friendly_name of this ShowBasicPluginResponse.

        展示名

        :param friendly_name: The friendly_name of this ShowBasicPluginResponse.
        :type friendly_name: str
        """
        self._friendly_name = friendly_name

    @property
    def category(self):
        r"""Gets the category of this ShowBasicPluginResponse.

        业务类型

        :return: The category of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowBasicPluginResponse.

        业务类型

        :param category: The category of this ShowBasicPluginResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this ShowBasicPluginResponse.

        描述

        :return: The description of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowBasicPluginResponse.

        描述

        :param description: The description of this ShowBasicPluginResponse.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        r"""Gets the version of this ShowBasicPluginResponse.

        版本

        :return: The version of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowBasicPluginResponse.

        版本

        :param version: The version of this ShowBasicPluginResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_description(self):
        r"""Gets the version_description of this ShowBasicPluginResponse.

        版本说明

        :return: The version_description of this ShowBasicPluginResponse.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ShowBasicPluginResponse.

        版本说明

        :param version_description: The version_description of this ShowBasicPluginResponse.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def inputs(self):
        r"""Gets the inputs of this ShowBasicPluginResponse.

        输入信息

        :return: The inputs of this ShowBasicPluginResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this ShowBasicPluginResponse.

        输入信息

        :param inputs: The inputs of this ShowBasicPluginResponse.
        :type inputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionInputs`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this ShowBasicPluginResponse.

        输出信息

        :return: The outputs of this ShowBasicPluginResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.NewExtensionOutputs`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this ShowBasicPluginResponse.

        输出信息

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
