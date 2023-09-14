# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipelineByTemplateIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'template_id': 'str',
        'component_id': 'str',
        'body': 'PipelineByTemplateDTO'
    }

    attribute_map = {
        'project_id': 'project_id',
        'template_id': 'template_id',
        'component_id': 'component_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, template_id=None, component_id=None, body=None):
        """CreatePipelineByTemplateIdRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param template_id: 模板ID
        :type template_id: str
        :param component_id: 微服务ID
        :type component_id: str
        :param body: Body of the CreatePipelineByTemplateIdRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTO`
        """
        
        

        self._project_id = None
        self._template_id = None
        self._component_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.template_id = template_id
        if component_id is not None:
            self.component_id = component_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this CreatePipelineByTemplateIdRequest.

        项目ID

        :return: The project_id of this CreatePipelineByTemplateIdRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatePipelineByTemplateIdRequest.

        项目ID

        :param project_id: The project_id of this CreatePipelineByTemplateIdRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def template_id(self):
        """Gets the template_id of this CreatePipelineByTemplateIdRequest.

        模板ID

        :return: The template_id of this CreatePipelineByTemplateIdRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreatePipelineByTemplateIdRequest.

        模板ID

        :param template_id: The template_id of this CreatePipelineByTemplateIdRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def component_id(self):
        """Gets the component_id of this CreatePipelineByTemplateIdRequest.

        微服务ID

        :return: The component_id of this CreatePipelineByTemplateIdRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this CreatePipelineByTemplateIdRequest.

        微服务ID

        :param component_id: The component_id of this CreatePipelineByTemplateIdRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def body(self):
        """Gets the body of this CreatePipelineByTemplateIdRequest.

        :return: The body of this CreatePipelineByTemplateIdRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePipelineByTemplateIdRequest.

        :param body: The body of this CreatePipelineByTemplateIdRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineByTemplateDTO`
        """
        self._body = body

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
        if not isinstance(other, CreatePipelineByTemplateIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
