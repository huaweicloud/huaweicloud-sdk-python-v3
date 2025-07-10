# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSimAlgorithmImagesResponse(SdkResponse):

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
        'command': 'str',
        'workspace': 'str',
        'keyword': 'str',
        'pkg_log_dir': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'command': 'command',
        'workspace': 'workspace',
        'keyword': 'keyword',
        'pkg_log_dir': 'pkg_log_dir'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, command=None, workspace=None, keyword=None, pkg_log_dir=None):
        r"""UpdateSimAlgorithmImagesResponse

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param command: 运行命令
        :type command: str
        :param workspace: 运行目录，构建类型需要
        :type workspace: str
        :param keyword: 算法关键字
        :type keyword: str
        :param pkg_log_dir: 目录打包路径
        :type pkg_log_dir: str
        """
        
        super(UpdateSimAlgorithmImagesResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._command = None
        self._workspace = None
        self._keyword = None
        self._pkg_log_dir = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if command is not None:
            self.command = command
        if workspace is not None:
            self.workspace = workspace
        if keyword is not None:
            self.keyword = keyword
        if pkg_log_dir is not None:
            self.pkg_log_dir = pkg_log_dir

    @property
    def url(self):
        r"""Gets the url of this UpdateSimAlgorithmImagesResponse.

        :return: The url of this UpdateSimAlgorithmImagesResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateSimAlgorithmImagesResponse.

        :param url: The url of this UpdateSimAlgorithmImagesResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this UpdateSimAlgorithmImagesResponse.

        :return: The id of this UpdateSimAlgorithmImagesResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSimAlgorithmImagesResponse.

        :param id: The id of this UpdateSimAlgorithmImagesResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateSimAlgorithmImagesResponse.

        :return: The created_at of this UpdateSimAlgorithmImagesResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateSimAlgorithmImagesResponse.

        :param created_at: The created_at of this UpdateSimAlgorithmImagesResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateSimAlgorithmImagesResponse.

        :return: The updated_at of this UpdateSimAlgorithmImagesResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateSimAlgorithmImagesResponse.

        :param updated_at: The updated_at of this UpdateSimAlgorithmImagesResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def command(self):
        r"""Gets the command of this UpdateSimAlgorithmImagesResponse.

        运行命令

        :return: The command of this UpdateSimAlgorithmImagesResponse.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this UpdateSimAlgorithmImagesResponse.

        运行命令

        :param command: The command of this UpdateSimAlgorithmImagesResponse.
        :type command: str
        """
        self._command = command

    @property
    def workspace(self):
        r"""Gets the workspace of this UpdateSimAlgorithmImagesResponse.

        运行目录，构建类型需要

        :return: The workspace of this UpdateSimAlgorithmImagesResponse.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this UpdateSimAlgorithmImagesResponse.

        运行目录，构建类型需要

        :param workspace: The workspace of this UpdateSimAlgorithmImagesResponse.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def keyword(self):
        r"""Gets the keyword of this UpdateSimAlgorithmImagesResponse.

        算法关键字

        :return: The keyword of this UpdateSimAlgorithmImagesResponse.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this UpdateSimAlgorithmImagesResponse.

        算法关键字

        :param keyword: The keyword of this UpdateSimAlgorithmImagesResponse.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def pkg_log_dir(self):
        r"""Gets the pkg_log_dir of this UpdateSimAlgorithmImagesResponse.

        目录打包路径

        :return: The pkg_log_dir of this UpdateSimAlgorithmImagesResponse.
        :rtype: str
        """
        return self._pkg_log_dir

    @pkg_log_dir.setter
    def pkg_log_dir(self, pkg_log_dir):
        r"""Sets the pkg_log_dir of this UpdateSimAlgorithmImagesResponse.

        目录打包路径

        :param pkg_log_dir: The pkg_log_dir of this UpdateSimAlgorithmImagesResponse.
        :type pkg_log_dir: str
        """
        self._pkg_log_dir = pkg_log_dir

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
        if not isinstance(other, UpdateSimAlgorithmImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
