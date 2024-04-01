# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'links': 'list[NovaLink]',
        'min_version': 'str',
        'status': 'str',
        'version': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'min_version': 'min_version',
        'status': 'status',
        'version': 'version',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, min_version=None, status=None, version=None, updated=None):
        """NovaVersion

        The model defined in huaweicloud sdk

        :param id: 所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。
        :type id: str
        :param links: 版本相关标记快捷链接信息。
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        :param min_version: 如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。
        :type min_version: str
        :param status: 这个是API版本的状态。可以是：  - CURRENT，这是使用的API的首选版本 - SUPPORTED，这是一个较老的，但仍然支持的API版本 - DEPRECATED，一个被废弃的API版本，该版本将被删除
        :type status: str
        :param version: 如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。
        :type version: str
        :param updated: 一个有特定值的字符串。API版本为2.0时，值为&#39;2011-01-21T11:33:21Z&#39;，API版本是2.1时，值为&#39; 2013-07-23T11:33:21Z&#39;。
        :type updated: str
        """
        
        

        self._id = None
        self._links = None
        self._min_version = None
        self._status = None
        self._version = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.min_version = min_version
        self.status = status
        self.version = version
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this NovaVersion.

        所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。

        :return: The id of this NovaVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaVersion.

        所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。

        :param id: The id of this NovaVersion.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaVersion.

        版本相关标记快捷链接信息。

        :return: The links of this NovaVersion.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaVersion.

        版本相关标记快捷链接信息。

        :param links: The links of this NovaVersion.
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        self._links = links

    @property
    def min_version(self):
        """Gets the min_version of this NovaVersion.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :return: The min_version of this NovaVersion.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this NovaVersion.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :param min_version: The min_version of this NovaVersion.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this NovaVersion.

        这个是API版本的状态。可以是：  - CURRENT，这是使用的API的首选版本 - SUPPORTED，这是一个较老的，但仍然支持的API版本 - DEPRECATED，一个被废弃的API版本，该版本将被删除

        :return: The status of this NovaVersion.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaVersion.

        这个是API版本的状态。可以是：  - CURRENT，这是使用的API的首选版本 - SUPPORTED，这是一个较老的，但仍然支持的API版本 - DEPRECATED，一个被废弃的API版本，该版本将被删除

        :param status: The status of this NovaVersion.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this NovaVersion.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :return: The version of this NovaVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NovaVersion.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :param version: The version of this NovaVersion.
        :type version: str
        """
        self._version = version

    @property
    def updated(self):
        """Gets the updated of this NovaVersion.

        一个有特定值的字符串。API版本为2.0时，值为'2011-01-21T11:33:21Z'，API版本是2.1时，值为' 2013-07-23T11:33:21Z'。

        :return: The updated of this NovaVersion.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NovaVersion.

        一个有特定值的字符串。API版本为2.0时，值为'2011-01-21T11:33:21Z'，API版本是2.1时，值为' 2013-07-23T11:33:21Z'。

        :param updated: The updated of this NovaVersion.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, NovaVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
