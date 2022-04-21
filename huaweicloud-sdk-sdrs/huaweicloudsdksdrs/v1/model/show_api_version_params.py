# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiVersionParams:

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
        'links': 'list[ShowApiVersionLinksParams]',
        'version': 'str',
        'status': 'str',
        'updated': 'str',
        'min_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'version': 'version',
        'status': 'status',
        'updated': 'updated',
        'min_version': 'min_version'
    }

    def __init__(self, id=None, links=None, version=None, status=None, updated=None, min_version=None):
        """ShowApiVersionParams

        The model defined in huaweicloud sdk

        :param id: 版本ID（版本号），如v1。
        :type id: str
        :param links: 版本号查询链接
        :type links: list[:class:`huaweicloudsdksdrs.v1.ShowApiVersionLinksParams`]
        :param version: 若该版本API支持微版本，则返回支持的最大微版本号，如果不支持微版本，则返回空。
        :type version: str
        :param status: 版本状态，为如下3种： CURRENT：表示该版本为主推版本 SUPPORTED：表示为老版本，但是现在还继续支持 DEPRECATED：表示为废弃版本，存在后续删除的可能
        :type status: str
        :param updated: 版本发布时间，采用UTC时间表示。如v1发布的时间2018-05-30T15:00:00Z。
        :type updated: str
        :param min_version: 若该版本API 支持微版本，则返回支持的最小微版本号，如果不支持微版本，则返回空。
        :type min_version: str
        """
        
        

        self._id = None
        self._links = None
        self._version = None
        self._status = None
        self._updated = None
        self._min_version = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.version = version
        self.status = status
        self.updated = updated
        self.min_version = min_version

    @property
    def id(self):
        """Gets the id of this ShowApiVersionParams.

        版本ID（版本号），如v1。

        :return: The id of this ShowApiVersionParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowApiVersionParams.

        版本ID（版本号），如v1。

        :param id: The id of this ShowApiVersionParams.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this ShowApiVersionParams.

        版本号查询链接

        :return: The links of this ShowApiVersionParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ShowApiVersionLinksParams`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowApiVersionParams.

        版本号查询链接

        :param links: The links of this ShowApiVersionParams.
        :type links: list[:class:`huaweicloudsdksdrs.v1.ShowApiVersionLinksParams`]
        """
        self._links = links

    @property
    def version(self):
        """Gets the version of this ShowApiVersionParams.

        若该版本API支持微版本，则返回支持的最大微版本号，如果不支持微版本，则返回空。

        :return: The version of this ShowApiVersionParams.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowApiVersionParams.

        若该版本API支持微版本，则返回支持的最大微版本号，如果不支持微版本，则返回空。

        :param version: The version of this ShowApiVersionParams.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        """Gets the status of this ShowApiVersionParams.

        版本状态，为如下3种： CURRENT：表示该版本为主推版本 SUPPORTED：表示为老版本，但是现在还继续支持 DEPRECATED：表示为废弃版本，存在后续删除的可能

        :return: The status of this ShowApiVersionParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowApiVersionParams.

        版本状态，为如下3种： CURRENT：表示该版本为主推版本 SUPPORTED：表示为老版本，但是现在还继续支持 DEPRECATED：表示为废弃版本，存在后续删除的可能

        :param status: The status of this ShowApiVersionParams.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ShowApiVersionParams.

        版本发布时间，采用UTC时间表示。如v1发布的时间2018-05-30T15:00:00Z。

        :return: The updated of this ShowApiVersionParams.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ShowApiVersionParams.

        版本发布时间，采用UTC时间表示。如v1发布的时间2018-05-30T15:00:00Z。

        :param updated: The updated of this ShowApiVersionParams.
        :type updated: str
        """
        self._updated = updated

    @property
    def min_version(self):
        """Gets the min_version of this ShowApiVersionParams.

        若该版本API 支持微版本，则返回支持的最小微版本号，如果不支持微版本，则返回空。

        :return: The min_version of this ShowApiVersionParams.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this ShowApiVersionParams.

        若该版本API 支持微版本，则返回支持的最小微版本号，如果不支持微版本，则返回空。

        :param min_version: The min_version of this ShowApiVersionParams.
        :type min_version: str
        """
        self._min_version = min_version

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
        if not isinstance(other, ShowApiVersionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
