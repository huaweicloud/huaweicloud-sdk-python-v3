# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordingFileDownloadUrlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_urls': 'list[RecordDownloadInfoBO]'
    }

    attribute_map = {
        'record_urls': 'recordUrls'
    }

    def __init__(self, record_urls=None):
        r"""ShowRecordingFileDownloadUrlsResponse

        The model defined in huaweicloud sdk

        :param record_urls: 录制文件下载链接。
        :type record_urls: list[:class:`huaweicloudsdkmeeting.v1.RecordDownloadInfoBO`]
        """
        
        super(ShowRecordingFileDownloadUrlsResponse, self).__init__()

        self._record_urls = None
        self.discriminator = None

        if record_urls is not None:
            self.record_urls = record_urls

    @property
    def record_urls(self):
        r"""Gets the record_urls of this ShowRecordingFileDownloadUrlsResponse.

        录制文件下载链接。

        :return: The record_urls of this ShowRecordingFileDownloadUrlsResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.RecordDownloadInfoBO`]
        """
        return self._record_urls

    @record_urls.setter
    def record_urls(self, record_urls):
        r"""Sets the record_urls of this ShowRecordingFileDownloadUrlsResponse.

        录制文件下载链接。

        :param record_urls: The record_urls of this ShowRecordingFileDownloadUrlsResponse.
        :type record_urls: list[:class:`huaweicloudsdkmeeting.v1.RecordDownloadInfoBO`]
        """
        self._record_urls = record_urls

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
        if not isinstance(other, ShowRecordingFileDownloadUrlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
