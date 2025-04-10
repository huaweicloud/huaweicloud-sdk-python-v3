# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVodRetrievalResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'interval': 'int',
        'sample_data': 'list[VodRetrievalData]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'interval': 'interval',
        'sample_data': 'sample_data'
    }

    def __init__(self, start_time=None, interval=None, sample_data=None):
        r"""ShowVodRetrievalResponse

        The model defined in huaweicloud sdk

        :param start_time: 统计起始时间 
        :type start_time: str
        :param interval: 采样时间间隔 
        :type interval: int
        :param sample_data: 
        :type sample_data: list[:class:`huaweicloudsdkvod.v1.VodRetrievalData`]
        """
        
        super(ShowVodRetrievalResponse, self).__init__()

        self._start_time = None
        self._interval = None
        self._sample_data = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if interval is not None:
            self.interval = interval
        if sample_data is not None:
            self.sample_data = sample_data

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowVodRetrievalResponse.

        统计起始时间 

        :return: The start_time of this ShowVodRetrievalResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowVodRetrievalResponse.

        统计起始时间 

        :param start_time: The start_time of this ShowVodRetrievalResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def interval(self):
        r"""Gets the interval of this ShowVodRetrievalResponse.

        采样时间间隔 

        :return: The interval of this ShowVodRetrievalResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowVodRetrievalResponse.

        采样时间间隔 

        :param interval: The interval of this ShowVodRetrievalResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def sample_data(self):
        r"""Gets the sample_data of this ShowVodRetrievalResponse.

        :return: The sample_data of this ShowVodRetrievalResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.VodRetrievalData`]
        """
        return self._sample_data

    @sample_data.setter
    def sample_data(self, sample_data):
        r"""Sets the sample_data of this ShowVodRetrievalResponse.

        :param sample_data: The sample_data of this ShowVodRetrievalResponse.
        :type sample_data: list[:class:`huaweicloudsdkvod.v1.VodRetrievalData`]
        """
        self._sample_data = sample_data

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
        if not isinstance(other, ShowVodRetrievalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
