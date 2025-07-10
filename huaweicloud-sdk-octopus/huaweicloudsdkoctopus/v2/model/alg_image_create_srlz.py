# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgImageCreateSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'type': 'Type87eEnum',
        'version': 'str',
        'command': 'str',
        'workspace': 'str',
        'keyword': 'str',
        'algorithm': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type',
        'version': 'version',
        'command': 'command',
        'workspace': 'workspace',
        'keyword': 'keyword',
        'algorithm': 'algorithm'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, type=None, version=None, command=None, workspace=None, keyword=None, algorithm=None):
        r"""AlgImageCreateSrlz

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param type: 镜像类型  * &#x60;build&#x60; - Build * &#x60;upload&#x60; - Upload
        :type type: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        :param version: 镜像版本
        :type version: str
        :param command: 运行命令
        :type command: str
        :param workspace: 运行目录，构建类型需要
        :type workspace: str
        :param keyword: 算法关键字
        :type keyword: str
        :param algorithm: 算法
        :type algorithm: str
        """
        
        

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self._version = None
        self._command = None
        self._workspace = None
        self._keyword = None
        self._algorithm = None
        self.discriminator = None

        self.url = url
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type
        self.version = version
        self.command = command
        self.workspace = workspace
        self.keyword = keyword
        self.algorithm = algorithm

    @property
    def url(self):
        r"""Gets the url of this AlgImageCreateSrlz.

        :return: The url of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AlgImageCreateSrlz.

        :param url: The url of this AlgImageCreateSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this AlgImageCreateSrlz.

        :return: The id of this AlgImageCreateSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlgImageCreateSrlz.

        :param id: The id of this AlgImageCreateSrlz.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this AlgImageCreateSrlz.

        :return: The created_at of this AlgImageCreateSrlz.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AlgImageCreateSrlz.

        :param created_at: The created_at of this AlgImageCreateSrlz.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this AlgImageCreateSrlz.

        :return: The updated_at of this AlgImageCreateSrlz.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this AlgImageCreateSrlz.

        :param updated_at: The updated_at of this AlgImageCreateSrlz.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def type(self):
        r"""Gets the type of this AlgImageCreateSrlz.

        镜像类型  * `build` - Build * `upload` - Upload

        :return: The type of this AlgImageCreateSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlgImageCreateSrlz.

        镜像类型  * `build` - Build * `upload` - Upload

        :param type: The type of this AlgImageCreateSrlz.
        :type type: :class:`huaweicloudsdkoctopus.v2.Type87eEnum`
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this AlgImageCreateSrlz.

        镜像版本

        :return: The version of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AlgImageCreateSrlz.

        镜像版本

        :param version: The version of this AlgImageCreateSrlz.
        :type version: str
        """
        self._version = version

    @property
    def command(self):
        r"""Gets the command of this AlgImageCreateSrlz.

        运行命令

        :return: The command of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this AlgImageCreateSrlz.

        运行命令

        :param command: The command of this AlgImageCreateSrlz.
        :type command: str
        """
        self._command = command

    @property
    def workspace(self):
        r"""Gets the workspace of this AlgImageCreateSrlz.

        运行目录，构建类型需要

        :return: The workspace of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this AlgImageCreateSrlz.

        运行目录，构建类型需要

        :param workspace: The workspace of this AlgImageCreateSrlz.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def keyword(self):
        r"""Gets the keyword of this AlgImageCreateSrlz.

        算法关键字

        :return: The keyword of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this AlgImageCreateSrlz.

        算法关键字

        :param keyword: The keyword of this AlgImageCreateSrlz.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def algorithm(self):
        r"""Gets the algorithm of this AlgImageCreateSrlz.

        算法

        :return: The algorithm of this AlgImageCreateSrlz.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this AlgImageCreateSrlz.

        算法

        :param algorithm: The algorithm of this AlgImageCreateSrlz.
        :type algorithm: str
        """
        self._algorithm = algorithm

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
        if not isinstance(other, AlgImageCreateSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
