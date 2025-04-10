# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevstarRepoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'repo_id': 'str',
        'repo_name': 'str',
        'ssh_url': 'str',
        'code_url': 'str',
        'detail_url': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'repo_id': 'repo_id',
        'repo_name': 'repo_name',
        'ssh_url': 'ssh_url',
        'code_url': 'code_url',
        'detail_url': 'detail_url'
    }

    def __init__(self, uuid=None, repo_id=None, repo_name=None, ssh_url=None, code_url=None, detail_url=None):
        r"""DevstarRepoInfo

        The model defined in huaweicloud sdk

        :param uuid: 仓库的uuid
        :type uuid: str
        :param repo_id: 仓库ID
        :type repo_id: str
        :param repo_name: 仓库名称
        :type repo_name: str
        :param ssh_url: 仓库SSH地址
        :type ssh_url: str
        :param code_url: 仓库HTTPS地址
        :type code_url: str
        :param detail_url: 仓库预览地址
        :type detail_url: str
        """
        
        

        self._uuid = None
        self._repo_id = None
        self._repo_name = None
        self._ssh_url = None
        self._code_url = None
        self._detail_url = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if repo_id is not None:
            self.repo_id = repo_id
        if repo_name is not None:
            self.repo_name = repo_name
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if code_url is not None:
            self.code_url = code_url
        if detail_url is not None:
            self.detail_url = detail_url

    @property
    def uuid(self):
        r"""Gets the uuid of this DevstarRepoInfo.

        仓库的uuid

        :return: The uuid of this DevstarRepoInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this DevstarRepoInfo.

        仓库的uuid

        :param uuid: The uuid of this DevstarRepoInfo.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def repo_id(self):
        r"""Gets the repo_id of this DevstarRepoInfo.

        仓库ID

        :return: The repo_id of this DevstarRepoInfo.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this DevstarRepoInfo.

        仓库ID

        :param repo_id: The repo_id of this DevstarRepoInfo.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this DevstarRepoInfo.

        仓库名称

        :return: The repo_name of this DevstarRepoInfo.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this DevstarRepoInfo.

        仓库名称

        :param repo_name: The repo_name of this DevstarRepoInfo.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def ssh_url(self):
        r"""Gets the ssh_url of this DevstarRepoInfo.

        仓库SSH地址

        :return: The ssh_url of this DevstarRepoInfo.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        r"""Sets the ssh_url of this DevstarRepoInfo.

        仓库SSH地址

        :param ssh_url: The ssh_url of this DevstarRepoInfo.
        :type ssh_url: str
        """
        self._ssh_url = ssh_url

    @property
    def code_url(self):
        r"""Gets the code_url of this DevstarRepoInfo.

        仓库HTTPS地址

        :return: The code_url of this DevstarRepoInfo.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this DevstarRepoInfo.

        仓库HTTPS地址

        :param code_url: The code_url of this DevstarRepoInfo.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def detail_url(self):
        r"""Gets the detail_url of this DevstarRepoInfo.

        仓库预览地址

        :return: The detail_url of this DevstarRepoInfo.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        r"""Sets the detail_url of this DevstarRepoInfo.

        仓库预览地址

        :param detail_url: The detail_url of this DevstarRepoInfo.
        :type detail_url: str
        """
        self._detail_url = detail_url

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
        if not isinstance(other, DevstarRepoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
