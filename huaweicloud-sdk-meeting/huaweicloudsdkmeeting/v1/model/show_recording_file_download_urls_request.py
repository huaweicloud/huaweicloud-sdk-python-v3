# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordingFileDownloadUrlsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'offset': 'offset',
        'limit': 'limit',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conf_uuid=None, offset=None, limit=None, x_authorization_type=None, x_site_id=None):
        r"""ShowRecordingFileDownloadUrlsRequest

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议UUID(通过[[查询录制列表](https://support.huaweicloud.com/api-meeting/meeting_21_0048.html)](tag:hws)[[查询录制列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0048.html)](tag:hk)获取)。
        :type conf_uuid: str
        :param offset: 查询偏移量。默认为0。
        :type offset: int
        :param limit: 查询数量。默认是20，最大500条。
        :type limit: int
        :param x_authorization_type: 标识是否为第三方portal过来的请求。 &gt; 该参数将废弃，请勿使用。 
        :type x_authorization_type: str
        :param x_site_id: 用于区分到哪个HCSO站点鉴权。 &gt; 该参数将废弃，请勿使用。 
        :type x_site_id: str
        """
        
        

        self._conf_uuid = None
        self._offset = None
        self._limit = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conf_uuid(self):
        r"""Gets the conf_uuid of this ShowRecordingFileDownloadUrlsRequest.

        会议UUID(通过[[查询录制列表](https://support.huaweicloud.com/api-meeting/meeting_21_0048.html)](tag:hws)[[查询录制列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0048.html)](tag:hk)获取)。

        :return: The conf_uuid of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        r"""Sets the conf_uuid of this ShowRecordingFileDownloadUrlsRequest.

        会议UUID(通过[[查询录制列表](https://support.huaweicloud.com/api-meeting/meeting_21_0048.html)](tag:hws)[[查询录制列表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0048.html)](tag:hk)获取)。

        :param conf_uuid: The conf_uuid of this ShowRecordingFileDownloadUrlsRequest.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def offset(self):
        r"""Gets the offset of this ShowRecordingFileDownloadUrlsRequest.

        查询偏移量。默认为0。

        :return: The offset of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowRecordingFileDownloadUrlsRequest.

        查询偏移量。默认为0。

        :param offset: The offset of this ShowRecordingFileDownloadUrlsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowRecordingFileDownloadUrlsRequest.

        查询数量。默认是20，最大500条。

        :return: The limit of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowRecordingFileDownloadUrlsRequest.

        查询数量。默认是20，最大500条。

        :param limit: The limit of this ShowRecordingFileDownloadUrlsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_authorization_type(self):
        r"""Gets the x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :return: The x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        r"""Sets the x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.

        标识是否为第三方portal过来的请求。 > 该参数将废弃，请勿使用。 

        :param x_authorization_type: The x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.
        :type x_authorization_type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        r"""Gets the x_site_id of this ShowRecordingFileDownloadUrlsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :return: The x_site_id of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        r"""Sets the x_site_id of this ShowRecordingFileDownloadUrlsRequest.

        用于区分到哪个HCSO站点鉴权。 > 该参数将废弃，请勿使用。 

        :param x_site_id: The x_site_id of this ShowRecordingFileDownloadUrlsRequest.
        :type x_site_id: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, ShowRecordingFileDownloadUrlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
