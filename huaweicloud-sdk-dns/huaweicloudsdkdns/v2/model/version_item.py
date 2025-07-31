# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionItem:

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
        'status': 'str',
        'links': 'list[LinksItem]',
        'updated': 'str',
        'version': 'str',
        'min_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'links': 'links',
        'updated': 'updated',
        'version': 'version',
        'min_version': 'min_version'
    }

    def __init__(self, id=None, status=None, links=None, updated=None, version=None, min_version=None):
        r"""VersionItem

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 版本号。 **取值范围：** v2。
        :type id: str
        :param status: **参数解释：** 版本状态。 **取值范围：** - CURRENT：表示该版本为主推版本。 - SUPPORTED：表示为老版本，但是现在还继续支持。 - DEPRECATED：表示为废弃版本，存在后续删除的可能。
        :type status: str
        :param links: **参数解释：** API的URL地址。 **取值范围：** 不涉及。
        :type links: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        :param updated: **参数解释：** 版本发布时间。 **取值范围：** 不涉及。
        :type updated: str
        :param version: **参数解释：** 支持的最大微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。
        :type version: str
        :param min_version: **参数解释：** 支持的最小微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。
        :type min_version: str
        """
        
        

        self._id = None
        self._status = None
        self._links = None
        self._updated = None
        self._version = None
        self._min_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if links is not None:
            self.links = links
        if updated is not None:
            self.updated = updated
        if version is not None:
            self.version = version
        if min_version is not None:
            self.min_version = min_version

    @property
    def id(self):
        r"""Gets the id of this VersionItem.

        **参数解释：** 版本号。 **取值范围：** v2。

        :return: The id of this VersionItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VersionItem.

        **参数解释：** 版本号。 **取值范围：** v2。

        :param id: The id of this VersionItem.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this VersionItem.

        **参数解释：** 版本状态。 **取值范围：** - CURRENT：表示该版本为主推版本。 - SUPPORTED：表示为老版本，但是现在还继续支持。 - DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :return: The status of this VersionItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VersionItem.

        **参数解释：** 版本状态。 **取值范围：** - CURRENT：表示该版本为主推版本。 - SUPPORTED：表示为老版本，但是现在还继续支持。 - DEPRECATED：表示为废弃版本，存在后续删除的可能。

        :param status: The status of this VersionItem.
        :type status: str
        """
        self._status = status

    @property
    def links(self):
        r"""Gets the links of this VersionItem.

        **参数解释：** API的URL地址。 **取值范围：** 不涉及。

        :return: The links of this VersionItem.
        :rtype: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this VersionItem.

        **参数解释：** API的URL地址。 **取值范围：** 不涉及。

        :param links: The links of this VersionItem.
        :type links: list[:class:`huaweicloudsdkdns.v2.LinksItem`]
        """
        self._links = links

    @property
    def updated(self):
        r"""Gets the updated of this VersionItem.

        **参数解释：** 版本发布时间。 **取值范围：** 不涉及。

        :return: The updated of this VersionItem.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this VersionItem.

        **参数解释：** 版本发布时间。 **取值范围：** 不涉及。

        :param updated: The updated of this VersionItem.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        r"""Gets the version of this VersionItem.

        **参数解释：** 支持的最大微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。

        :return: The version of this VersionItem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VersionItem.

        **参数解释：** 支持的最大微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。

        :param version: The version of this VersionItem.
        :type version: str
        """
        self._version = version

    @property
    def min_version(self):
        r"""Gets the min_version of this VersionItem.

        **参数解释：** 支持的最小微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。

        :return: The min_version of this VersionItem.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        r"""Sets the min_version of this VersionItem.

        **参数解释：** 支持的最小微版本号。 **取值范围：** 若该版本API不支持微版本，则为空。

        :param min_version: The min_version of this VersionItem.
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
        if not isinstance(other, VersionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
