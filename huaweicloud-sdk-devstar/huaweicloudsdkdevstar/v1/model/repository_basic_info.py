# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryBasicInfo:

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
        'id': 'str',
        'name': 'str',
        'https_url': 'str',
        'ssh_url': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'id': 'id',
        'name': 'name',
        'https_url': 'https_url',
        'ssh_url': 'ssh_url',
        'web_url': 'web_url'
    }

    def __init__(self, uuid=None, id=None, name=None, https_url=None, ssh_url=None, web_url=None):
        """RepositoryBasicInfo

        The model defined in huaweicloud sdk

        :param uuid: 仓库uuid
        :type uuid: str
        :param id: 仓库id
        :type id: str
        :param name: 仓库名称
        :type name: str
        :param https_url: 仓库git的https下载地址
        :type https_url: str
        :param ssh_url: 仓库git的ssh下载地址
        :type ssh_url: str
        :param web_url: 仓库codehub内容浏览页面地址
        :type web_url: str
        """
        
        

        self._uuid = None
        self._id = None
        self._name = None
        self._https_url = None
        self._ssh_url = None
        self._web_url = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if https_url is not None:
            self.https_url = https_url
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if web_url is not None:
            self.web_url = web_url

    @property
    def uuid(self):
        """Gets the uuid of this RepositoryBasicInfo.

        仓库uuid

        :return: The uuid of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RepositoryBasicInfo.

        仓库uuid

        :param uuid: The uuid of this RepositoryBasicInfo.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def id(self):
        """Gets the id of this RepositoryBasicInfo.

        仓库id

        :return: The id of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepositoryBasicInfo.

        仓库id

        :param id: The id of this RepositoryBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RepositoryBasicInfo.

        仓库名称

        :return: The name of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryBasicInfo.

        仓库名称

        :param name: The name of this RepositoryBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def https_url(self):
        """Gets the https_url of this RepositoryBasicInfo.

        仓库git的https下载地址

        :return: The https_url of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """Sets the https_url of this RepositoryBasicInfo.

        仓库git的https下载地址

        :param https_url: The https_url of this RepositoryBasicInfo.
        :type https_url: str
        """
        self._https_url = https_url

    @property
    def ssh_url(self):
        """Gets the ssh_url of this RepositoryBasicInfo.

        仓库git的ssh下载地址

        :return: The ssh_url of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this RepositoryBasicInfo.

        仓库git的ssh下载地址

        :param ssh_url: The ssh_url of this RepositoryBasicInfo.
        :type ssh_url: str
        """
        self._ssh_url = ssh_url

    @property
    def web_url(self):
        """Gets the web_url of this RepositoryBasicInfo.

        仓库codehub内容浏览页面地址

        :return: The web_url of this RepositoryBasicInfo.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this RepositoryBasicInfo.

        仓库codehub内容浏览页面地址

        :param web_url: The web_url of this RepositoryBasicInfo.
        :type web_url: str
        """
        self._web_url = web_url

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
        if not isinstance(other, RepositoryBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
