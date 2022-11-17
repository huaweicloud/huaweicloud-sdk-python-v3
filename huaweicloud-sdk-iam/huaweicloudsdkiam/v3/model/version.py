# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Version:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'updated': 'str',
        'links': 'list[VersionLinks]',
        'id': 'str',
        'media_types': 'list[VersionMediatypes]'
    }

    attribute_map = {
        'status': 'status',
        'updated': 'updated',
        'links': 'links',
        'id': 'id',
        'media_types': 'media-types'
    }

    def __init__(self, status=None, updated=None, links=None, id=None, media_types=None):
        """Version

        The model defined in huaweicloud sdk

        :param status: 版本状态。
        :type status: str
        :param updated: 最后更新时间。
        :type updated: str
        :param links: 版本的资源链接信息。
        :type links: list[:class:`huaweicloudsdkiam.v3.VersionLinks`]
        :param id: 版本号，如v3.6。
        :type id: str
        :param media_types: 支持的消息格式。
        :type media_types: list[:class:`huaweicloudsdkiam.v3.VersionMediatypes`]
        """
        
        

        self._status = None
        self._updated = None
        self._links = None
        self._id = None
        self._media_types = None
        self.discriminator = None

        self.status = status
        self.updated = updated
        self.links = links
        self.id = id
        self.media_types = media_types

    @property
    def status(self):
        """Gets the status of this Version.

        版本状态。

        :return: The status of this Version.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Version.

        版本状态。

        :param status: The status of this Version.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this Version.

        最后更新时间。

        :return: The updated of this Version.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Version.

        最后更新时间。

        :param updated: The updated of this Version.
        :type updated: str
        """
        self._updated = updated

    @property
    def links(self):
        """Gets the links of this Version.

        版本的资源链接信息。

        :return: The links of this Version.
        :rtype: list[:class:`huaweicloudsdkiam.v3.VersionLinks`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Version.

        版本的资源链接信息。

        :param links: The links of this Version.
        :type links: list[:class:`huaweicloudsdkiam.v3.VersionLinks`]
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this Version.

        版本号，如v3.6。

        :return: The id of this Version.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Version.

        版本号，如v3.6。

        :param id: The id of this Version.
        :type id: str
        """
        self._id = id

    @property
    def media_types(self):
        """Gets the media_types of this Version.

        支持的消息格式。

        :return: The media_types of this Version.
        :rtype: list[:class:`huaweicloudsdkiam.v3.VersionMediatypes`]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this Version.

        支持的消息格式。

        :param media_types: The media_types of this Version.
        :type media_types: list[:class:`huaweicloudsdkiam.v3.VersionMediatypes`]
        """
        self._media_types = media_types

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
