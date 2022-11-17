# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryByCloudIdeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'repository_id': 'str',
        'repository_ssh_url': 'str',
        'region_id': 'str',
        'space_prefix': 'str',
        'is_open_last': 'bool',
        'is_free': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'repository_id': 'repository_id',
        'repository_ssh_url': 'repository_ssh_url',
        'region_id': 'region_id',
        'space_prefix': 'space_prefix',
        'is_open_last': 'is_open_last',
        'is_free': 'is_free'
    }

    def __init__(self, x_language=None, repository_id=None, repository_ssh_url=None, region_id=None, space_prefix=None, is_open_last=None, is_free=None):
        """ShowRepositoryByCloudIdeRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param repository_id: 仓库id。
        :type repository_id: str
        :param repository_ssh_url: 仓库下载地址。
        :type repository_ssh_url: str
        :param region_id: 区域ID，目前仅支持北京四：cn-north-4及北京一：cn-north-1。
        :type region_id: str
        :param space_prefix: 工作空间名称前缀，仅在is_open_last为false时生效，由用户自定义，支持大小写字母、中文、_、-，长度1-256。
        :type space_prefix: str
        :param is_open_last: 是否打开上一次的工作空间，true表示打开上一次工作空间，如果没有上一次工作空间会返回空，false代表打开一个全新的工作空间。
        :type is_open_last: bool
        :param is_free: 是否创建 CloudIDE 免费实例链接，true表示创建一个 CloudIDE 免费实例链接，false表示创建一个 CloudIDE 收费实例链接。
        :type is_free: bool
        """
        
        

        self._x_language = None
        self._repository_id = None
        self._repository_ssh_url = None
        self._region_id = None
        self._space_prefix = None
        self._is_open_last = None
        self._is_free = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.repository_id = repository_id
        self.repository_ssh_url = repository_ssh_url
        if region_id is not None:
            self.region_id = region_id
        if space_prefix is not None:
            self.space_prefix = space_prefix
        if is_open_last is not None:
            self.is_open_last = is_open_last
        if is_free is not None:
            self.is_free = is_free

    @property
    def x_language(self):
        """Gets the x_language of this ShowRepositoryByCloudIdeRequest.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this ShowRepositoryByCloudIdeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowRepositoryByCloudIdeRequest.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this ShowRepositoryByCloudIdeRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def repository_id(self):
        """Gets the repository_id of this ShowRepositoryByCloudIdeRequest.

        仓库id。

        :return: The repository_id of this ShowRepositoryByCloudIdeRequest.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this ShowRepositoryByCloudIdeRequest.

        仓库id。

        :param repository_id: The repository_id of this ShowRepositoryByCloudIdeRequest.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def repository_ssh_url(self):
        """Gets the repository_ssh_url of this ShowRepositoryByCloudIdeRequest.

        仓库下载地址。

        :return: The repository_ssh_url of this ShowRepositoryByCloudIdeRequest.
        :rtype: str
        """
        return self._repository_ssh_url

    @repository_ssh_url.setter
    def repository_ssh_url(self, repository_ssh_url):
        """Sets the repository_ssh_url of this ShowRepositoryByCloudIdeRequest.

        仓库下载地址。

        :param repository_ssh_url: The repository_ssh_url of this ShowRepositoryByCloudIdeRequest.
        :type repository_ssh_url: str
        """
        self._repository_ssh_url = repository_ssh_url

    @property
    def region_id(self):
        """Gets the region_id of this ShowRepositoryByCloudIdeRequest.

        区域ID，目前仅支持北京四：cn-north-4及北京一：cn-north-1。

        :return: The region_id of this ShowRepositoryByCloudIdeRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowRepositoryByCloudIdeRequest.

        区域ID，目前仅支持北京四：cn-north-4及北京一：cn-north-1。

        :param region_id: The region_id of this ShowRepositoryByCloudIdeRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def space_prefix(self):
        """Gets the space_prefix of this ShowRepositoryByCloudIdeRequest.

        工作空间名称前缀，仅在is_open_last为false时生效，由用户自定义，支持大小写字母、中文、_、-，长度1-256。

        :return: The space_prefix of this ShowRepositoryByCloudIdeRequest.
        :rtype: str
        """
        return self._space_prefix

    @space_prefix.setter
    def space_prefix(self, space_prefix):
        """Sets the space_prefix of this ShowRepositoryByCloudIdeRequest.

        工作空间名称前缀，仅在is_open_last为false时生效，由用户自定义，支持大小写字母、中文、_、-，长度1-256。

        :param space_prefix: The space_prefix of this ShowRepositoryByCloudIdeRequest.
        :type space_prefix: str
        """
        self._space_prefix = space_prefix

    @property
    def is_open_last(self):
        """Gets the is_open_last of this ShowRepositoryByCloudIdeRequest.

        是否打开上一次的工作空间，true表示打开上一次工作空间，如果没有上一次工作空间会返回空，false代表打开一个全新的工作空间。

        :return: The is_open_last of this ShowRepositoryByCloudIdeRequest.
        :rtype: bool
        """
        return self._is_open_last

    @is_open_last.setter
    def is_open_last(self, is_open_last):
        """Sets the is_open_last of this ShowRepositoryByCloudIdeRequest.

        是否打开上一次的工作空间，true表示打开上一次工作空间，如果没有上一次工作空间会返回空，false代表打开一个全新的工作空间。

        :param is_open_last: The is_open_last of this ShowRepositoryByCloudIdeRequest.
        :type is_open_last: bool
        """
        self._is_open_last = is_open_last

    @property
    def is_free(self):
        """Gets the is_free of this ShowRepositoryByCloudIdeRequest.

        是否创建 CloudIDE 免费实例链接，true表示创建一个 CloudIDE 免费实例链接，false表示创建一个 CloudIDE 收费实例链接。

        :return: The is_free of this ShowRepositoryByCloudIdeRequest.
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        """Sets the is_free of this ShowRepositoryByCloudIdeRequest.

        是否创建 CloudIDE 免费实例链接，true表示创建一个 CloudIDE 免费实例链接，false表示创建一个 CloudIDE 收费实例链接。

        :param is_free: The is_free of this ShowRepositoryByCloudIdeRequest.
        :type is_free: bool
        """
        self._is_free = is_free

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
        if not isinstance(other, ShowRepositoryByCloudIdeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
