# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFileRequest:

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
        'path': 'str',
        'ref': 'str',
        'body': 'FileCreate'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth',
        'namespace': 'namespace',
        'project': 'project',
        'path': 'path',
        'ref': 'ref',
        'body': 'body'
    }

    def __init__(self, x_repo_auth=None, namespace=None, project=None, path=None, ref=None, body=None):
        r"""CreateFileRequest

        The model defined in huaweicloud sdk

        :param x_repo_auth: 授权名称。
        :type x_repo_auth: str
        :param namespace: 命名空间ID或者URL编码名称。
        :type namespace: str
        :param project: 仓库项目ID，如果含有“/”，需要将“/”替换为“:”。
        :type project: str
        :param path: 文件路径，需要将“/”替换为“:”。
        :type path: str
        :param ref: 分支名称或者tag标签名称或者commit sha。
        :type ref: str
        :param body: Body of the CreateFileRequest
        :type body: :class:`huaweicloudsdkservicestage.v2.FileCreate`
        """
        
        

        self._x_repo_auth = None
        self._namespace = None
        self._project = None
        self._path = None
        self._ref = None
        self._body = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth
        self.namespace = namespace
        self.project = project
        self.path = path
        self.ref = ref
        if body is not None:
            self.body = body

    @property
    def x_repo_auth(self):
        r"""Gets the x_repo_auth of this CreateFileRequest.

        授权名称。

        :return: The x_repo_auth of this CreateFileRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        r"""Sets the x_repo_auth of this CreateFileRequest.

        授权名称。

        :param x_repo_auth: The x_repo_auth of this CreateFileRequest.
        :type x_repo_auth: str
        """
        self._x_repo_auth = x_repo_auth

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateFileRequest.

        命名空间ID或者URL编码名称。

        :return: The namespace of this CreateFileRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateFileRequest.

        命名空间ID或者URL编码名称。

        :param namespace: The namespace of this CreateFileRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def project(self):
        r"""Gets the project of this CreateFileRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :return: The project of this CreateFileRequest.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this CreateFileRequest.

        仓库项目ID，如果含有“/”，需要将“/”替换为“:”。

        :param project: The project of this CreateFileRequest.
        :type project: str
        """
        self._project = project

    @property
    def path(self):
        r"""Gets the path of this CreateFileRequest.

        文件路径，需要将“/”替换为“:”。

        :return: The path of this CreateFileRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CreateFileRequest.

        文件路径，需要将“/”替换为“:”。

        :param path: The path of this CreateFileRequest.
        :type path: str
        """
        self._path = path

    @property
    def ref(self):
        r"""Gets the ref of this CreateFileRequest.

        分支名称或者tag标签名称或者commit sha。

        :return: The ref of this CreateFileRequest.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this CreateFileRequest.

        分支名称或者tag标签名称或者commit sha。

        :param ref: The ref of this CreateFileRequest.
        :type ref: str
        """
        self._ref = ref

    @property
    def body(self):
        r"""Gets the body of this CreateFileRequest.

        :return: The body of this CreateFileRequest.
        :rtype: :class:`huaweicloudsdkservicestage.v2.FileCreate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateFileRequest.

        :param body: The body of this CreateFileRequest.
        :type body: :class:`huaweicloudsdkservicestage.v2.FileCreate`
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
        if not isinstance(other, CreateFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
