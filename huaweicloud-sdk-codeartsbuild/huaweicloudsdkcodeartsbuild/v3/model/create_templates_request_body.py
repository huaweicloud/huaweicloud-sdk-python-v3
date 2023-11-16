# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplatesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'CreateTemplate',
        'name': 'str',
        'description': 'str',
        'tool_type': 'str',
        'parameters': 'list[CreateBuildJobParameter]'
    }

    attribute_map = {
        'template': 'template',
        'name': 'name',
        'description': 'description',
        'tool_type': 'tool_type',
        'parameters': 'parameters'
    }

    def __init__(self, template=None, name=None, description=None, tool_type=None, parameters=None):
        """CreateTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param template: 
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplate`
        :param name: 模板命名
        :type name: str
        :param description: 模板说明
        :type description: str
        :param tool_type: 工具类型
        :type tool_type: str
        :param parameters: 构建执行参数列表
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        
        

        self._template = None
        self._name = None
        self._description = None
        self._tool_type = None
        self._parameters = None
        self.discriminator = None

        self.template = template
        self.name = name
        if description is not None:
            self.description = description
        if tool_type is not None:
            self.tool_type = tool_type
        if parameters is not None:
            self.parameters = parameters

    @property
    def template(self):
        """Gets the template of this CreateTemplatesRequestBody.

        :return: The template of this CreateTemplatesRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateTemplatesRequestBody.

        :param template: The template of this CreateTemplatesRequestBody.
        :type template: :class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplate`
        """
        self._template = template

    @property
    def name(self):
        """Gets the name of this CreateTemplatesRequestBody.

        模板命名

        :return: The name of this CreateTemplatesRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplatesRequestBody.

        模板命名

        :param name: The name of this CreateTemplatesRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTemplatesRequestBody.

        模板说明

        :return: The description of this CreateTemplatesRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTemplatesRequestBody.

        模板说明

        :param description: The description of this CreateTemplatesRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def tool_type(self):
        """Gets the tool_type of this CreateTemplatesRequestBody.

        工具类型

        :return: The tool_type of this CreateTemplatesRequestBody.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this CreateTemplatesRequestBody.

        工具类型

        :param tool_type: The tool_type of this CreateTemplatesRequestBody.
        :type tool_type: str
        """
        self._tool_type = tool_type

    @property
    def parameters(self):
        """Gets the parameters of this CreateTemplatesRequestBody.

        构建执行参数列表

        :return: The parameters of this CreateTemplatesRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreateTemplatesRequestBody.

        构建执行参数列表

        :param parameters: The parameters of this CreateTemplatesRequestBody.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        self._parameters = parameters

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
        if not isinstance(other, CreateTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
