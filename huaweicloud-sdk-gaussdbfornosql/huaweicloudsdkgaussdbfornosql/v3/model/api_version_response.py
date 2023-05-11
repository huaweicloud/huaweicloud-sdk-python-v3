# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiVersionResponse:

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
        'status': 'str',
        'version': 'str',
        'min_version': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'status': 'status',
        'version': 'version',
        'min_version': 'min_version',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, status=None, version=None, min_version=None, updated=None):
        """ApiVersionResponse

        The model defined in huaweicloud sdk

        :param id: API版本号。
        :type id: str
        :param links: 对应API的链接信息,v3版本该字段为[]。
        :type links: list[:class:`huaweicloudsdkgaussdbfornosql.v3.Links`]
        :param status: 版本状态。 取值为“CURRENT”，表示该版本目前已对外公布。
        :type status: str
        :param version: API版本的子版本信息。
        :type version: str
        :param min_version: API版本的最小版本号。
        :type min_version: str
        :param updated: 版本更新时间。格式为“yyyy-mm-dd Thh:mm:ssZ”。其中，T指某个时间的开始，Z指UTC时间。
        :type updated: str
        """
        
        

        self._id = None
        self._links = None
        self._status = None
        self._version = None
        self._min_version = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.status = status
        self.version = version
        self.min_version = min_version
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this ApiVersionResponse.

        API版本号。

        :return: The id of this ApiVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiVersionResponse.

        API版本号。

        :param id: The id of this ApiVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this ApiVersionResponse.

        对应API的链接信息,v3版本该字段为[]。

        :return: The links of this ApiVersionResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiVersionResponse.

        对应API的链接信息,v3版本该字段为[]。

        :param links: The links of this ApiVersionResponse.
        :type links: list[:class:`huaweicloudsdkgaussdbfornosql.v3.Links`]
        """
        self._links = links

    @property
    def status(self):
        """Gets the status of this ApiVersionResponse.

        版本状态。 取值为“CURRENT”，表示该版本目前已对外公布。

        :return: The status of this ApiVersionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiVersionResponse.

        版本状态。 取值为“CURRENT”，表示该版本目前已对外公布。

        :param status: The status of this ApiVersionResponse.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this ApiVersionResponse.

        API版本的子版本信息。

        :return: The version of this ApiVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiVersionResponse.

        API版本的子版本信息。

        :param version: The version of this ApiVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def min_version(self):
        """Gets the min_version of this ApiVersionResponse.

        API版本的最小版本号。

        :return: The min_version of this ApiVersionResponse.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this ApiVersionResponse.

        API版本的最小版本号。

        :param min_version: The min_version of this ApiVersionResponse.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def updated(self):
        """Gets the updated of this ApiVersionResponse.

        版本更新时间。格式为“yyyy-mm-dd Thh:mm:ssZ”。其中，T指某个时间的开始，Z指UTC时间。

        :return: The updated of this ApiVersionResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ApiVersionResponse.

        版本更新时间。格式为“yyyy-mm-dd Thh:mm:ssZ”。其中，T指某个时间的开始，Z指UTC时间。

        :param updated: The updated of this ApiVersionResponse.
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
        if not isinstance(other, ApiVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
