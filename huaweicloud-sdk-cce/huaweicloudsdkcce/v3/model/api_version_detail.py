# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class APIVersionDetail:

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
        'links': 'list[APIVersionLink]',
        'min_version': 'str',
        'status': 'str',
        'updated': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'min_version': 'min_version',
        'status': 'status',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, id=None, links=None, min_version=None, status=None, updated=None, version=None):
        """APIVersionDetail

        The model defined in huaweicloud sdk

        :param id: API版本ID。例如v3。
        :type id: str
        :param links: API版本的URL链接信息。
        :type links: list[:class:`huaweicloudsdkcce.v3.APIVersionLink`]
        :param min_version: 如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。
        :type min_version: str
        :param status: API版本的状态。 可以是： - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除
        :type status: str
        :param updated: API发布时间（UTC格式）。例如API版本为v3时，值为&#39;2018-09-15 00:00:00Z&#39;。
        :type updated: str
        :param version: 如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。
        :type version: str
        """
        
        

        self._id = None
        self._links = None
        self._min_version = None
        self._status = None
        self._updated = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.min_version = min_version
        self.status = status
        self.updated = updated
        self.version = version

    @property
    def id(self):
        """Gets the id of this APIVersionDetail.

        API版本ID。例如v3。

        :return: The id of this APIVersionDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APIVersionDetail.

        API版本ID。例如v3。

        :param id: The id of this APIVersionDetail.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this APIVersionDetail.

        API版本的URL链接信息。

        :return: The links of this APIVersionDetail.
        :rtype: list[:class:`huaweicloudsdkcce.v3.APIVersionLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this APIVersionDetail.

        API版本的URL链接信息。

        :param links: The links of this APIVersionDetail.
        :type links: list[:class:`huaweicloudsdkcce.v3.APIVersionLink`]
        """
        self._links = links

    @property
    def min_version(self):
        """Gets the min_version of this APIVersionDetail.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :return: The min_version of this APIVersionDetail.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this APIVersionDetail.

        如果API的这个版本支持微版本，则支持最小的微版本。如果不支持微版本，这将是空字符串。

        :param min_version: The min_version of this APIVersionDetail.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this APIVersionDetail.

        API版本的状态。 可以是： - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除

        :return: The status of this APIVersionDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this APIVersionDetail.

        API版本的状态。 可以是： - CURRENT这是使用的API的首选版本； - SUPPORTED：这是一个较老的，但仍然支持的API版本； - DEPRECATED：一个被废弃的API版本，该版本将被删除

        :param status: The status of this APIVersionDetail.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this APIVersionDetail.

        API发布时间（UTC格式）。例如API版本为v3时，值为'2018-09-15 00:00:00Z'。

        :return: The updated of this APIVersionDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this APIVersionDetail.

        API发布时间（UTC格式）。例如API版本为v3时，值为'2018-09-15 00:00:00Z'。

        :param updated: The updated of this APIVersionDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this APIVersionDetail.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :return: The version of this APIVersionDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this APIVersionDetail.

        如果API的这个版本支持微版本，则支持最大的微版本。如果不支持微版本，这将是空字符串。

        :param version: The version of this APIVersionDetail.
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
        if not isinstance(other, APIVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
