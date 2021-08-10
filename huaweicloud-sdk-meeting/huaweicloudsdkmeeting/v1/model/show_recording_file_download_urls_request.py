# coding: utf-8

import re
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
        """ShowRecordingFileDownloadUrlsRequest - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the conf_uuid of this ShowRecordingFileDownloadUrlsRequest.

        会议的ConfUUID(通过查询录制文件列表获取)。

        :return: The conf_uuid of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this ShowRecordingFileDownloadUrlsRequest.

        会议的ConfUUID(通过查询录制文件列表获取)。

        :param conf_uuid: The conf_uuid of this ShowRecordingFileDownloadUrlsRequest.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def offset(self):
        """Gets the offset of this ShowRecordingFileDownloadUrlsRequest.

        数据偏移记录。

        :return: The offset of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowRecordingFileDownloadUrlsRequest.

        数据偏移记录。

        :param offset: The offset of this ShowRecordingFileDownloadUrlsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowRecordingFileDownloadUrlsRequest.

        指定返回的记录数，最大500条。

        :return: The limit of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowRecordingFileDownloadUrlsRequest.

        指定返回的记录数，最大500条。

        :param limit: The limit of this ShowRecordingFileDownloadUrlsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.

        标识是否为第三方portal过来的请求。

        :return: The x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.

        标识是否为第三方portal过来的请求。

        :param x_authorization_type: The x_authorization_type of this ShowRecordingFileDownloadUrlsRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this ShowRecordingFileDownloadUrlsRequest.

        用于区分到哪个HCSO站点鉴权。

        :return: The x_site_id of this ShowRecordingFileDownloadUrlsRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this ShowRecordingFileDownloadUrlsRequest.

        用于区分到哪个HCSO站点鉴权。

        :param x_site_id: The x_site_id of this ShowRecordingFileDownloadUrlsRequest.
        :type: str
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
