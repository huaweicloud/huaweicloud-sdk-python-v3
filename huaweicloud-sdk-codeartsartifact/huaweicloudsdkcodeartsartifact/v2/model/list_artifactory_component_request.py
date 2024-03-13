# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListArtifactoryComponentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'project_id': 'str',
        'repo_name': 'str',
        'path': 'str',
        'format': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'repo_name': 'repo_name',
        'path': 'path',
        'format': 'format',
        'instance_id': 'instance_id'
    }

    def __init__(self, tenant_id=None, project_id=None, repo_name=None, path=None, format=None, instance_id=None):
        """ListArtifactoryComponentRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param project_id: 项目id
        :type project_id: str
        :param repo_name: 仓库名称
        :type repo_name: str
        :param path: 仓库中路径
        :type path: str
        :param format: 仓库格式
        :type format: str
        :param instance_id: 实例id
        :type instance_id: str
        """
        
        

        self._tenant_id = None
        self._project_id = None
        self._repo_name = None
        self._path = None
        self._format = None
        self._instance_id = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.project_id = project_id
        self.repo_name = repo_name
        self.path = path
        self.format = format
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListArtifactoryComponentRequest.

        租户id

        :return: The tenant_id of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListArtifactoryComponentRequest.

        租户id

        :param tenant_id: The tenant_id of this ListArtifactoryComponentRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this ListArtifactoryComponentRequest.

        项目id

        :return: The project_id of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListArtifactoryComponentRequest.

        项目id

        :param project_id: The project_id of this ListArtifactoryComponentRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo_name(self):
        """Gets the repo_name of this ListArtifactoryComponentRequest.

        仓库名称

        :return: The repo_name of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this ListArtifactoryComponentRequest.

        仓库名称

        :param repo_name: The repo_name of this ListArtifactoryComponentRequest.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def path(self):
        """Gets the path of this ListArtifactoryComponentRequest.

        仓库中路径

        :return: The path of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListArtifactoryComponentRequest.

        仓库中路径

        :param path: The path of this ListArtifactoryComponentRequest.
        :type path: str
        """
        self._path = path

    @property
    def format(self):
        """Gets the format of this ListArtifactoryComponentRequest.

        仓库格式

        :return: The format of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ListArtifactoryComponentRequest.

        仓库格式

        :param format: The format of this ListArtifactoryComponentRequest.
        :type format: str
        """
        self._format = format

    @property
    def instance_id(self):
        """Gets the instance_id of this ListArtifactoryComponentRequest.

        实例id

        :return: The instance_id of this ListArtifactoryComponentRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListArtifactoryComponentRequest.

        实例id

        :param instance_id: The instance_id of this ListArtifactoryComponentRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListArtifactoryComponentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
