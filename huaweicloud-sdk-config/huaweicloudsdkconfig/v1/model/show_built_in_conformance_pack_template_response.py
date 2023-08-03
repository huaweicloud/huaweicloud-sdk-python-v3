# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBuiltInConformancePackTemplateResponse(SdkResponse):

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
        'template_key': 'str',
        'description': 'str',
        'template_body': 'str',
        'parameters': 'dict(str, TemplateParameterDefinition)'
    }

    attribute_map = {
        'id': 'id',
        'template_key': 'template_key',
        'description': 'description',
        'template_body': 'template_body',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, template_key=None, description=None, template_body=None, parameters=None):
        """ShowBuiltInConformancePackTemplateResponse

        The model defined in huaweicloud sdk

        :param id: 预定义合规包模板ID。
        :type id: str
        :param template_key: 预定义合规包模板名称。
        :type template_key: str
        :param description: 预定义合规包模板描述。
        :type description: str
        :param template_body: 预定义合规包模板内容。
        :type template_body: str
        :param parameters: 预定义合规包模板参数。
        :type parameters: dict(str, TemplateParameterDefinition)
        """
        
        super(ShowBuiltInConformancePackTemplateResponse, self).__init__()

        self._id = None
        self._template_key = None
        self._description = None
        self._template_body = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_key is not None:
            self.template_key = template_key
        if description is not None:
            self.description = description
        if template_body is not None:
            self.template_body = template_body
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板ID。

        :return: The id of this ShowBuiltInConformancePackTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板ID。

        :param id: The id of this ShowBuiltInConformancePackTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def template_key(self):
        """Gets the template_key of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板名称。

        :return: The template_key of this ShowBuiltInConformancePackTemplateResponse.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        """Sets the template_key of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板名称。

        :param template_key: The template_key of this ShowBuiltInConformancePackTemplateResponse.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def description(self):
        """Gets the description of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板描述。

        :return: The description of this ShowBuiltInConformancePackTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板描述。

        :param description: The description of this ShowBuiltInConformancePackTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def template_body(self):
        """Gets the template_body of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板内容。

        :return: The template_body of this ShowBuiltInConformancePackTemplateResponse.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板内容。

        :param template_body: The template_body of this ShowBuiltInConformancePackTemplateResponse.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def parameters(self):
        """Gets the parameters of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板参数。

        :return: The parameters of this ShowBuiltInConformancePackTemplateResponse.
        :rtype: dict(str, TemplateParameterDefinition)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ShowBuiltInConformancePackTemplateResponse.

        预定义合规包模板参数。

        :param parameters: The parameters of this ShowBuiltInConformancePackTemplateResponse.
        :type parameters: dict(str, TemplateParameterDefinition)
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
        if not isinstance(other, ShowBuiltInConformancePackTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
