# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'resource_id': 'str',
        'workspace_id': 'str',
        'body': 'CreateResJobsReququestBody'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'resource_id': 'resource_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, content_type=None, resource_id=None, workspace_id=None, body=None):
        r"""CreateResJobsRequest

        The model defined in huaweicloud sdk

        :param content_type: 内容类型，包括application和json两种类型
        :type content_type: str
        :param resource_id: 资源id
        :type resource_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param body: Body of the CreateResJobsRequest
        :type body: :class:`huaweicloudsdkres.v1.CreateResJobsReququestBody`
        """
        
        

        self._content_type = None
        self._resource_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        self.resource_id = resource_id
        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def content_type(self):
        r"""Gets the content_type of this CreateResJobsRequest.

        内容类型，包括application和json两种类型

        :return: The content_type of this CreateResJobsRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this CreateResJobsRequest.

        内容类型，包括application和json两种类型

        :param content_type: The content_type of this CreateResJobsRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateResJobsRequest.

        资源id

        :return: The resource_id of this CreateResJobsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateResJobsRequest.

        资源id

        :param resource_id: The resource_id of this CreateResJobsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateResJobsRequest.

        工作空间id

        :return: The workspace_id of this CreateResJobsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateResJobsRequest.

        工作空间id

        :param workspace_id: The workspace_id of this CreateResJobsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this CreateResJobsRequest.

        :return: The body of this CreateResJobsRequest.
        :rtype: :class:`huaweicloudsdkres.v1.CreateResJobsReququestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateResJobsRequest.

        :param body: The body of this CreateResJobsRequest.
        :type body: :class:`huaweicloudsdkres.v1.CreateResJobsReququestBody`
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
        if not isinstance(other, CreateResJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
