# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Versions:

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
        'links': 'list[Link]',
        'media_types': 'list[MediaTypes]',
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
        r"""Versions

        The model defined in huaweicloud sdk

        :param id: 接口版本的ID
        :type id: str
        :param links: 接口版本信息的URI描述信息
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param media_types: 接口版本的请求消息类型信息
        :type media_types: list[:class:`huaweicloudsdkevs.v2.MediaTypes`]
        :param min_version: 接口版本的最小版本号
        :type min_version: str
        :param status: 接口版本的状态
        :type status: str
        :param updated: 接口版本更新时间
        :type updated: str
        :param version: 接口版本的版本号信息
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
        if min_version is not None:
            self.min_version = min_version
        self.status = status
        self.updated = updated
        self.version = version

    @property
    def id(self):
        r"""Gets the id of this Versions.

        接口版本的ID

        :return: The id of this Versions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Versions.

        接口版本的ID

        :param id: The id of this Versions.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        r"""Gets the links of this Versions.

        接口版本信息的URI描述信息

        :return: The links of this Versions.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this Versions.

        接口版本信息的URI描述信息

        :param links: The links of this Versions.
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def media_types(self):
        r"""Gets the media_types of this Versions.

        接口版本的请求消息类型信息

        :return: The media_types of this Versions.
        :rtype: list[:class:`huaweicloudsdkevs.v2.MediaTypes`]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        r"""Sets the media_types of this Versions.

        接口版本的请求消息类型信息

        :param media_types: The media_types of this Versions.
        :type media_types: list[:class:`huaweicloudsdkevs.v2.MediaTypes`]
        """
        self._media_types = media_types

    @property
    def min_version(self):
        r"""Gets the min_version of this Versions.

        接口版本的最小版本号

        :return: The min_version of this Versions.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        r"""Sets the min_version of this Versions.

        接口版本的最小版本号

        :param min_version: The min_version of this Versions.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        r"""Gets the status of this Versions.

        接口版本的状态

        :return: The status of this Versions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Versions.

        接口版本的状态

        :param status: The status of this Versions.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        r"""Gets the updated of this Versions.

        接口版本更新时间

        :return: The updated of this Versions.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this Versions.

        接口版本更新时间

        :param updated: The updated of this Versions.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        r"""Gets the version of this Versions.

        接口版本的版本号信息

        :return: The version of this Versions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Versions.

        接口版本的版本号信息

        :param version: The version of this Versions.
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
        if not isinstance(other, Versions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
