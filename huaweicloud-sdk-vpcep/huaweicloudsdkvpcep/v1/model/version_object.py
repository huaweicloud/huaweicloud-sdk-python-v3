# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionObject:

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
        'id': 'str',
        'updated': 'str',
        'version': 'str',
        'min_version': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'updated': 'updated',
        'version': 'version',
        'min_version': 'min_version',
        'links': 'links'
    }

    def __init__(self, status=None, id=None, updated=None, version=None, min_version=None, links=None):
        """VersionObject

        The model defined in huaweicloud sdk

        :param status: 版本状态。 ● CURRENT：表示该版本为主推版本。 ● SUPPORT：表示为老版本，但是现在还在继续支持。 ● DEPRECATED：表示为废弃版本，存在后续删除的可能。
        :type status: str
        :param id: 版本ID。
        :type id: str
        :param updated: 版本发布时间。采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ
        :type updated: str
        :param version: 支持的版本号。
        :type version: str
        :param min_version: 支持的微版本号。若该版本API不支持微版本，则为空。
        :type min_version: str
        :param links: API的URL地址
        :type links: list[:class:`huaweicloudsdkvpcep.v1.Link`]
        """
        
        

        self._status = None
        self._id = None
        self._updated = None
        self._version = None
        self._min_version = None
        self._links = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if updated is not None:
            self.updated = updated
        if version is not None:
            self.version = version
        if min_version is not None:
            self.min_version = min_version
        if links is not None:
            self.links = links

    @property
    def status(self):
        """Gets the status of this VersionObject.

        版本状态。 ● CURRENT：表示该版本为主推版本。 ● SUPPORT：表示为老版本，但是现在还在继续支持。 ● DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :return: The status of this VersionObject.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionObject.

        版本状态。 ● CURRENT：表示该版本为主推版本。 ● SUPPORT：表示为老版本，但是现在还在继续支持。 ● DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :param status: The status of this VersionObject.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this VersionObject.

        版本ID。

        :return: The id of this VersionObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionObject.

        版本ID。

        :param id: The id of this VersionObject.
        :type id: str
        """
        self._id = id

    @property
    def updated(self):
        """Gets the updated of this VersionObject.

        版本发布时间。采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :return: The updated of this VersionObject.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this VersionObject.

        版本发布时间。采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :param updated: The updated of this VersionObject.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this VersionObject.

        支持的版本号。

        :return: The version of this VersionObject.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionObject.

        支持的版本号。

        :param version: The version of this VersionObject.
        :type version: str
        """
        self._version = version

    @property
    def min_version(self):
        """Gets the min_version of this VersionObject.

        支持的微版本号。若该版本API不支持微版本，则为空。

        :return: The min_version of this VersionObject.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this VersionObject.

        支持的微版本号。若该版本API不支持微版本，则为空。

        :param min_version: The min_version of this VersionObject.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def links(self):
        """Gets the links of this VersionObject.

        API的URL地址

        :return: The links of this VersionObject.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionObject.

        API的URL地址

        :param links: The links of this VersionObject.
        :type links: list[:class:`huaweicloudsdkvpcep.v1.Link`]
        """
        self._links = links

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
        if not isinstance(other, VersionObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
