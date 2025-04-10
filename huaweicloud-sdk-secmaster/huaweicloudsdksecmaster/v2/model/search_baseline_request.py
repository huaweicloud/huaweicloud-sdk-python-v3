# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchBaselineRequest:

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
        'workspace_id': 'str',
        'x_language': 'str',
        'body': 'BaselineSearchRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, x_language=None, body=None):
        r"""SearchBaselineRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param x_language: 语言，参考值：zh-CN、en-US
        :type x_language: str
        :param body: Body of the SearchBaselineRequest
        :type body: :class:`huaweicloudsdksecmaster.v2.BaselineSearchRequestBody`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this SearchBaselineRequest.

        项目id

        :return: The project_id of this SearchBaselineRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SearchBaselineRequest.

        项目id

        :param project_id: The project_id of this SearchBaselineRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this SearchBaselineRequest.

        工作空间id

        :return: The workspace_id of this SearchBaselineRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this SearchBaselineRequest.

        工作空间id

        :param workspace_id: The workspace_id of this SearchBaselineRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def x_language(self):
        r"""Gets the x_language of this SearchBaselineRequest.

        语言，参考值：zh-CN、en-US

        :return: The x_language of this SearchBaselineRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this SearchBaselineRequest.

        语言，参考值：zh-CN、en-US

        :param x_language: The x_language of this SearchBaselineRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this SearchBaselineRequest.

        :return: The body of this SearchBaselineRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v2.BaselineSearchRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SearchBaselineRequest.

        :param body: The body of this SearchBaselineRequest.
        :type body: :class:`huaweicloudsdksecmaster.v2.BaselineSearchRequestBody`
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
        if not isinstance(other, SearchBaselineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
