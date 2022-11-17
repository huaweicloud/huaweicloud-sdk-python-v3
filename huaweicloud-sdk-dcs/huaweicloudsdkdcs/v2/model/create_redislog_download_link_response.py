# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedislogDownloadLinkResponse(SdkResponse):

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
        'link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'link': 'link'
    }

    def __init__(self, id=None, link=None):
        """CreateRedislogDownloadLinkResponse

        The model defined in huaweicloud sdk

        :param id: 日志id
        :type id: str
        :param link: 日志下载链接，默认有效时间为24小时
        :type link: str
        """
        
        super(CreateRedislogDownloadLinkResponse, self).__init__()

        self._id = None
        self._link = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if link is not None:
            self.link = link

    @property
    def id(self):
        """Gets the id of this CreateRedislogDownloadLinkResponse.

        日志id

        :return: The id of this CreateRedislogDownloadLinkResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRedislogDownloadLinkResponse.

        日志id

        :param id: The id of this CreateRedislogDownloadLinkResponse.
        :type id: str
        """
        self._id = id

    @property
    def link(self):
        """Gets the link of this CreateRedislogDownloadLinkResponse.

        日志下载链接，默认有效时间为24小时

        :return: The link of this CreateRedislogDownloadLinkResponse.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this CreateRedislogDownloadLinkResponse.

        日志下载链接，默认有效时间为24小时

        :param link: The link of this CreateRedislogDownloadLinkResponse.
        :type link: str
        """
        self._link = link

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
        if not isinstance(other, CreateRedislogDownloadLinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
