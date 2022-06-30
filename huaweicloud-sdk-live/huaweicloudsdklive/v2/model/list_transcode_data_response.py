# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'transcode_data_list': 'list[TranscodeData]',
        'summary_list': 'list[TranscodeSummary]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'transcode_data_list': 'transcode_data_list',
        'summary_list': 'summary_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, transcode_data_list=None, summary_list=None, x_request_id=None):
        """ListTranscodeDataResponse

        The model defined in huaweicloud sdk

        :param transcode_data_list: 采样数据列表。
        :type transcode_data_list: list[:class:`huaweicloudsdklive.v2.TranscodeData`]
        :param summary_list: 指定时间区间内各转码规格转码时长总和。
        :type summary_list: list[:class:`huaweicloudsdklive.v2.TranscodeSummary`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListTranscodeDataResponse, self).__init__()

        self._transcode_data_list = None
        self._summary_list = None
        self._x_request_id = None
        self.discriminator = None

        if transcode_data_list is not None:
            self.transcode_data_list = transcode_data_list
        if summary_list is not None:
            self.summary_list = summary_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def transcode_data_list(self):
        """Gets the transcode_data_list of this ListTranscodeDataResponse.

        采样数据列表。

        :return: The transcode_data_list of this ListTranscodeDataResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.TranscodeData`]
        """
        return self._transcode_data_list

    @transcode_data_list.setter
    def transcode_data_list(self, transcode_data_list):
        """Sets the transcode_data_list of this ListTranscodeDataResponse.

        采样数据列表。

        :param transcode_data_list: The transcode_data_list of this ListTranscodeDataResponse.
        :type transcode_data_list: list[:class:`huaweicloudsdklive.v2.TranscodeData`]
        """
        self._transcode_data_list = transcode_data_list

    @property
    def summary_list(self):
        """Gets the summary_list of this ListTranscodeDataResponse.

        指定时间区间内各转码规格转码时长总和。

        :return: The summary_list of this ListTranscodeDataResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.TranscodeSummary`]
        """
        return self._summary_list

    @summary_list.setter
    def summary_list(self, summary_list):
        """Sets the summary_list of this ListTranscodeDataResponse.

        指定时间区间内各转码规格转码时长总和。

        :param summary_list: The summary_list of this ListTranscodeDataResponse.
        :type summary_list: list[:class:`huaweicloudsdklive.v2.TranscodeSummary`]
        """
        self._summary_list = summary_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListTranscodeDataResponse.


        :return: The x_request_id of this ListTranscodeDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListTranscodeDataResponse.


        :param x_request_id: The x_request_id of this ListTranscodeDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListTranscodeDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
