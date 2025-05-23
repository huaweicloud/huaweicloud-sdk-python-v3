# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiVersionResponse(SdkResponse):

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
        'status': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, id=None, links=None, status=None, updated=None):
        r"""ShowApiVersionResponse

        The model defined in huaweicloud sdk

        :param id: API版本号。
        :type id: str
        :param links: API链接地址信息。
        :type links: list[:class:`huaweicloudsdksms.v3.Link`]
        :param status: 版本状态。 SUPPORTED表示支持的版本
        :type status: str
        :param updated: 版本更新时间。 格式为“yyyy-mm-dd Thh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。例如：2018-09-30T00:00:00Z
        :type updated: str
        """
        
        super(ShowApiVersionResponse, self).__init__()

        self._id = None
        self._links = None
        self._status = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        r"""Gets the id of this ShowApiVersionResponse.

        API版本号。

        :return: The id of this ShowApiVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowApiVersionResponse.

        API版本号。

        :param id: The id of this ShowApiVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        r"""Gets the links of this ShowApiVersionResponse.

        API链接地址信息。

        :return: The links of this ShowApiVersionResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ShowApiVersionResponse.

        API链接地址信息。

        :param links: The links of this ShowApiVersionResponse.
        :type links: list[:class:`huaweicloudsdksms.v3.Link`]
        """
        self._links = links

    @property
    def status(self):
        r"""Gets the status of this ShowApiVersionResponse.

        版本状态。 SUPPORTED表示支持的版本

        :return: The status of this ShowApiVersionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowApiVersionResponse.

        版本状态。 SUPPORTED表示支持的版本

        :param status: The status of this ShowApiVersionResponse.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        r"""Gets the updated of this ShowApiVersionResponse.

        版本更新时间。 格式为“yyyy-mm-dd Thh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。例如：2018-09-30T00:00:00Z

        :return: The updated of this ShowApiVersionResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowApiVersionResponse.

        版本更新时间。 格式为“yyyy-mm-dd Thh:mm:ssZ”。 其中，T指某个时间的开始；Z指UTC时间。例如：2018-09-30T00:00:00Z

        :param updated: The updated of this ShowApiVersionResponse.
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
        if not isinstance(other, ShowApiVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
