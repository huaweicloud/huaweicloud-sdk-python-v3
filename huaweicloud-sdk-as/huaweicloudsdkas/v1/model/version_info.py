# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionInfo:

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
        'links': 'list[Links]',
        'min_version': 'str',
        'status': 'str',
        'update': 'datetime',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'min_version': 'min_version',
        'status': 'status',
        'update': 'update',
        'version': 'version'
    }

    def __init__(self, id=None, links=None, min_version=None, status=None, update=None, version=None):
        """VersionInfo

        The model defined in huaweicloud sdk

        :param id: API版本ID。
        :type id: str
        :param links: API的URL相关信息。
        :type links: list[:class:`huaweicloudsdkas.v1.Links`]
        :param min_version: 该版本API支持的最小微版本号。
        :type min_version: str
        :param status: 版本状态，为如下3种：CURRENT：表示该版本为主推版本；SUPPORT：表示为老版本，但是现在还继续支持；DEPRECATED：表示为废弃版本，存在后续删除的可能。
        :type status: str
        :param update: 版本发布时间，使用UTC时间。
        :type update: datetime
        :param version: 该版本API支持的最大微版本号。
        :type version: str
        """
        
        

        self._id = None
        self._links = None
        self._min_version = None
        self._status = None
        self._update = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if min_version is not None:
            self.min_version = min_version
        if status is not None:
            self.status = status
        if update is not None:
            self.update = update
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this VersionInfo.

        API版本ID。

        :return: The id of this VersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionInfo.

        API版本ID。

        :param id: The id of this VersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VersionInfo.

        API的URL相关信息。

        :return: The links of this VersionInfo.
        :rtype: list[:class:`huaweicloudsdkas.v1.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionInfo.

        API的URL相关信息。

        :param links: The links of this VersionInfo.
        :type links: list[:class:`huaweicloudsdkas.v1.Links`]
        """
        self._links = links

    @property
    def min_version(self):
        """Gets the min_version of this VersionInfo.

        该版本API支持的最小微版本号。

        :return: The min_version of this VersionInfo.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this VersionInfo.

        该版本API支持的最小微版本号。

        :param min_version: The min_version of this VersionInfo.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this VersionInfo.

        版本状态，为如下3种：CURRENT：表示该版本为主推版本；SUPPORT：表示为老版本，但是现在还继续支持；DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :return: The status of this VersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionInfo.

        版本状态，为如下3种：CURRENT：表示该版本为主推版本；SUPPORT：表示为老版本，但是现在还继续支持；DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :param status: The status of this VersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def update(self):
        """Gets the update of this VersionInfo.

        版本发布时间，使用UTC时间。

        :return: The update of this VersionInfo.
        :rtype: datetime
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this VersionInfo.

        版本发布时间，使用UTC时间。

        :param update: The update of this VersionInfo.
        :type update: datetime
        """
        self._update = update

    @property
    def version(self):
        """Gets the version of this VersionInfo.

        该版本API支持的最大微版本号。

        :return: The version of this VersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionInfo.

        该版本API支持的最大微版本号。

        :param version: The version of this VersionInfo.
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
        if not isinstance(other, VersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
