# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaVersionDetail:

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
        'media_types': 'list[NovaVersionMediaType]',
        'min_version': 'str',
        'status': 'str',
        'updated': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'media_types': 'media-types',
        'min_version': 'min_version',
        'status': 'status',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, id=None, links=None, media_types=None, min_version=None, status=None, updated=None, version=None):
        """NovaVersionDetail

        The model defined in huaweicloud sdk

        :param id: 所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。
        :type id: str
        :param links: 链接到资源的问题。有关更多信息，请参见[OpenStack Documentation](http://developer.openstack.org/api-guide/compute/links_and_references.html)。
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        :param media_types: 媒体类型。
        :type media_types: list[:class:`huaweicloudsdkecs.v2.NovaVersionMediaType`]
        :param min_version: 如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。
        :type min_version: str
        :param status: 这个是API版本的状态。  可以是：  - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除
        :type status: str
        :param updated: 一个有特定值的字符串。API版本为2.0时，值为&#39;2011-01-21T11:33:21Z&#39; ，API版本是2.1时，值为&#39; 2013-07-23T11:33:21Z&#39;。
        :type updated: str
        :param version: 如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。
        :type version: str
        """
        
        

        self._id = None
        self._links = None
        self._media_types = None
        self._min_version = None
        self._status = None
        self._updated = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.media_types = media_types
        self.min_version = min_version
        self.status = status
        self.updated = updated
        self.version = version

    @property
    def id(self):
        """Gets the id of this NovaVersionDetail.

        所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。

        :return: The id of this NovaVersionDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaVersionDetail.

        所讨论的版本的通用名称。仅仅是信息性的，它没有真正的语义。

        :param id: The id of this NovaVersionDetail.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaVersionDetail.

        链接到资源的问题。有关更多信息，请参见[OpenStack Documentation](http://developer.openstack.org/api-guide/compute/links_and_references.html)。

        :return: The links of this NovaVersionDetail.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaVersionDetail.

        链接到资源的问题。有关更多信息，请参见[OpenStack Documentation](http://developer.openstack.org/api-guide/compute/links_and_references.html)。

        :param links: The links of this NovaVersionDetail.
        :type links: list[:class:`huaweicloudsdkecs.v2.NovaLink`]
        """
        self._links = links

    @property
    def media_types(self):
        """Gets the media_types of this NovaVersionDetail.

        媒体类型。

        :return: The media_types of this NovaVersionDetail.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaVersionMediaType`]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this NovaVersionDetail.

        媒体类型。

        :param media_types: The media_types of this NovaVersionDetail.
        :type media_types: list[:class:`huaweicloudsdkecs.v2.NovaVersionMediaType`]
        """
        self._media_types = media_types

    @property
    def min_version(self):
        """Gets the min_version of this NovaVersionDetail.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :return: The min_version of this NovaVersionDetail.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this NovaVersionDetail.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :param min_version: The min_version of this NovaVersionDetail.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this NovaVersionDetail.

        这个是API版本的状态。  可以是：  - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除

        :return: The status of this NovaVersionDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaVersionDetail.

        这个是API版本的状态。  可以是：  - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除

        :param status: The status of this NovaVersionDetail.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this NovaVersionDetail.

        一个有特定值的字符串。API版本为2.0时，值为'2011-01-21T11:33:21Z' ，API版本是2.1时，值为' 2013-07-23T11:33:21Z'。

        :return: The updated of this NovaVersionDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NovaVersionDetail.

        一个有特定值的字符串。API版本为2.0时，值为'2011-01-21T11:33:21Z' ，API版本是2.1时，值为' 2013-07-23T11:33:21Z'。

        :param updated: The updated of this NovaVersionDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this NovaVersionDetail.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :return: The version of this NovaVersionDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NovaVersionDetail.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :param version: The version of this NovaVersionDetail.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, NovaVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
