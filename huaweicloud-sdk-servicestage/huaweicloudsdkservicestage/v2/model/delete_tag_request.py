# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_repo_auth': 'str',
        'namespace': 'str',
        'project': 'str',
        'tag_name': 'str'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth',
        'namespace': 'namespace',
        'project': 'project',
        'tag_name': 'tag_name'
    }

    def __init__(self, x_repo_auth=None, namespace=None, project=None, tag_name=None):
        """DeleteTagRequest

        The model defined in huaweicloud sdk

        :param x_repo_auth: 授权名称。
        :type x_repo_auth: str
        :param namespace: 命名空间ID或者URL编码名称。
        :type namespace: str
        :param project: 仓库项目ID，如果含有“/”，需要将“/”替换为“:”。
        :type project: str
        :param tag_name: tag标签名称。
        :type tag_name: str
        """
        
        

        self._x_repo_auth = None
        self._namespace = None
        self._project = None
        self._tag_name = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth
        self.namespace = namespace
        self.project = project
        self.tag_name = tag_name

    @property
    def x_repo_auth(self):
        """Gets the x_repo_auth of this DeleteTagRequest.

        授权名称。

        :return: The x_repo_auth of this DeleteTagRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        """Sets the x_repo_auth of this DeleteTagRequest.

        授权名称。

        :param x_repo_auth: The x_repo_auth of this DeleteTagRequest.
        :type x_repo_auth: str
        """
        self._x_repo_auth = x_repo_auth

    @property
    def namespace(self):
        """Gets the namespace of this DeleteTagRequest.

        命名空间ID或者URL编码名称。

        :return: The namespace of this DeleteTagRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeleteTagRequest.

        命名空间ID或者URL编码名称。

        :param namespace: The namespace of this DeleteTagRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project(self):
        """Gets the project of this DeleteTagRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :return: The project of this DeleteTagRequest.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DeleteTagRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :param project: The project of this DeleteTagRequest.
        :type project: str
        """
        self._project = project

    @property
    def tag_name(self):
        """Gets the tag_name of this DeleteTagRequest.

        tag标签名称。

        :return: The tag_name of this DeleteTagRequest.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this DeleteTagRequest.

        tag标签名称。

        :param tag_name: The tag_name of this DeleteTagRequest.
        :type tag_name: str
        """
        self._tag_name = tag_name

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
        if not isinstance(other, DeleteTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
