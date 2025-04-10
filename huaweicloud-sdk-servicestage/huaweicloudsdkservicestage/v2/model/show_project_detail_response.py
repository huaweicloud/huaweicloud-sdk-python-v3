# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace_id': 'str',
        'namespace': 'str',
        'project_id': 'str',
        'project': 'str'
    }

    attribute_map = {
        'namespace_id': 'namespace_id',
        'namespace': 'namespace',
        'project_id': 'project_id',
        'project': 'project'
    }

    def __init__(self, namespace_id=None, namespace=None, project_id=None, project=None):
        r"""ShowProjectDetailResponse

        The model defined in huaweicloud sdk

        :param namespace_id: 命名空间ID。
        :type namespace_id: str
        :param namespace: 命名空间。
        :type namespace: str
        :param project_id: 仓库项目ID。
        :type project_id: str
        :param project: 仓库项目。
        :type project: str
        """
        
        super(ShowProjectDetailResponse, self).__init__()

        self._namespace_id = None
        self._namespace = None
        self._project_id = None
        self._project = None
        self.discriminator = None

        if namespace_id is not None:
            self.namespace_id = namespace_id
        if namespace is not None:
            self.namespace = namespace
        if project_id is not None:
            self.project_id = project_id
        if project is not None:
            self.project = project

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ShowProjectDetailResponse.

        命名空间ID。

        :return: The namespace_id of this ShowProjectDetailResponse.
        :rtype: str
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ShowProjectDetailResponse.

        命名空间ID。

        :param namespace_id: The namespace_id of this ShowProjectDetailResponse.
        :type namespace_id: str
        """
        self._namespace_id = namespace_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowProjectDetailResponse.

        命名空间。

        :return: The namespace of this ShowProjectDetailResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowProjectDetailResponse.

        命名空间。

        :param namespace: The namespace of this ShowProjectDetailResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowProjectDetailResponse.

        仓库项目ID。

        :return: The project_id of this ShowProjectDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowProjectDetailResponse.

        仓库项目ID。

        :param project_id: The project_id of this ShowProjectDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project(self):
        r"""Gets the project of this ShowProjectDetailResponse.

        仓库项目。

        :return: The project of this ShowProjectDetailResponse.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this ShowProjectDetailResponse.

        仓库项目。

        :param project: The project of this ShowProjectDetailResponse.
        :type project: str
        """
        self._project = project

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
        if not isinstance(other, ShowProjectDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
