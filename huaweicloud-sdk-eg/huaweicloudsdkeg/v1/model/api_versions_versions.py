# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiVersionsVersions:

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
        'links': 'list[ApiVersionsLinks]',
        'version': 'str',
        'min_version': 'str',
        'status': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'version': 'version',
        'min_version': 'min_version',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, version=None, min_version=None, status=None, updated=None):
        """ApiVersionsVersions

        The model defined in huaweicloud sdk

        :param id: 版本号，如v1
        :type id: str
        :param links: url地址
        :type links: list[:class:`huaweicloudsdkeg.v1.ApiVersionsLinks`]
        :param version: 若该版本API支持微版本，则为支持的最大微版本号，如果不支持微版本，则为空
        :type version: str
        :param min_version: 若该版本API支持微版本，则为支持的最小微版本号，如果不支持微版本，则为空
        :type min_version: str
        :param status: 版本状态，支持CURRENT：推荐版本；SUPPORTED：老版本，仍支持使用；DEPRECATED：废弃版本，后续会删除
        :type status: str
        :param updated: 版本发布UTC时间
        :type updated: str
        """
        
        

        self._id = None
        self._links = None
        self._version = None
        self._min_version = None
        self._status = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if version is not None:
            self.version = version
        if min_version is not None:
            self.min_version = min_version
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this ApiVersionsVersions.

        版本号，如v1

        :return: The id of this ApiVersionsVersions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiVersionsVersions.

        版本号，如v1

        :param id: The id of this ApiVersionsVersions.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this ApiVersionsVersions.

        url地址

        :return: The links of this ApiVersionsVersions.
        :rtype: list[:class:`huaweicloudsdkeg.v1.ApiVersionsLinks`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiVersionsVersions.

        url地址

        :param links: The links of this ApiVersionsVersions.
        :type links: list[:class:`huaweicloudsdkeg.v1.ApiVersionsLinks`]
        """
        self._links = links

    @property
    def version(self):
        """Gets the version of this ApiVersionsVersions.

        若该版本API支持微版本，则为支持的最大微版本号，如果不支持微版本，则为空

        :return: The version of this ApiVersionsVersions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiVersionsVersions.

        若该版本API支持微版本，则为支持的最大微版本号，如果不支持微版本，则为空

        :param version: The version of this ApiVersionsVersions.
        :type version: str
        """
        self._version = version

    @property
    def min_version(self):
        """Gets the min_version of this ApiVersionsVersions.

        若该版本API支持微版本，则为支持的最小微版本号，如果不支持微版本，则为空

        :return: The min_version of this ApiVersionsVersions.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this ApiVersionsVersions.

        若该版本API支持微版本，则为支持的最小微版本号，如果不支持微版本，则为空

        :param min_version: The min_version of this ApiVersionsVersions.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this ApiVersionsVersions.

        版本状态，支持CURRENT：推荐版本；SUPPORTED：老版本，仍支持使用；DEPRECATED：废弃版本，后续会删除

        :return: The status of this ApiVersionsVersions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiVersionsVersions.

        版本状态，支持CURRENT：推荐版本；SUPPORTED：老版本，仍支持使用；DEPRECATED：废弃版本，后续会删除

        :param status: The status of this ApiVersionsVersions.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ApiVersionsVersions.

        版本发布UTC时间

        :return: The updated of this ApiVersionsVersions.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApiVersionsVersions.

        版本发布UTC时间

        :param updated: The updated of this ApiVersionsVersions.
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
        if not isinstance(other, ApiVersionsVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
