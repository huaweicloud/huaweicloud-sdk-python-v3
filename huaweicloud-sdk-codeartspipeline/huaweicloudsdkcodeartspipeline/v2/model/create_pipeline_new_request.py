# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipelineNewRequest:

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
        'component_id': 'str',
        'body': 'PipelineDTO'
    }

    attribute_map = {
        'project_id': 'project_id',
        'component_id': 'component_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, component_id=None, body=None):
        """CreatePipelineNewRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param component_id: 组件ID
        :type component_id: str
        :param body: Body of the CreatePipelineNewRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineDTO`
        """
        
        

        self._project_id = None
        self._component_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if component_id is not None:
            self.component_id = component_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this CreatePipelineNewRequest.

        项目ID

        :return: The project_id of this CreatePipelineNewRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatePipelineNewRequest.

        项目ID

        :param project_id: The project_id of this CreatePipelineNewRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def component_id(self):
        """Gets the component_id of this CreatePipelineNewRequest.

        组件ID

        :return: The component_id of this CreatePipelineNewRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this CreatePipelineNewRequest.

        组件ID

        :param component_id: The component_id of this CreatePipelineNewRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def body(self):
        """Gets the body of this CreatePipelineNewRequest.

        :return: The body of this CreatePipelineNewRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePipelineNewRequest.

        :param body: The body of this CreatePipelineNewRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineDTO`
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
        if not isinstance(other, CreatePipelineNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
