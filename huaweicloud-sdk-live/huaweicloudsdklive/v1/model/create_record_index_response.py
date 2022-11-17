# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordIndexResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_url': 'str',
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'duration': 'int',
        'weight': 'int',
        'height': 'int',
        'location': 'str',
        'bucket': 'str',
        'object': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'index_url': 'index_url',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration',
        'weight': 'weight',
        'height': 'height',
        'location': 'location',
        'bucket': 'bucket',
        'object': 'object',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, index_url=None, publish_domain=None, app=None, stream=None, start_time=None, end_time=None, duration=None, weight=None, height=None, location=None, bucket=None, object=None, x_request_id=None):
        """CreateRecordIndexResponse

        The model defined in huaweicloud sdk

        :param index_url: 索引文件地址
        :type index_url: str
        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: 应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*
        :type app: str
        :param stream: 录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*
        :type stream: str
        :param start_time: 开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的开始时间)
        :type start_time: datetime
        :param end_time: 结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的结束时间)
        :type end_time: datetime
        :param duration: 录制时长。单位：秒。
        :type duration: int
        :param weight: 视频宽。
        :type weight: int
        :param height: 视频高。
        :type height: int
        :param location: OBS Bucket所在RegionID
        :type location: str
        :param bucket: 桶名称
        :type bucket: str
        :param object: m3u8文件路径。默认Index/{publish_domain}/{app}/{stream}-{start_time}-{end_time}
        :type object: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateRecordIndexResponse, self).__init__()

        self._index_url = None
        self._publish_domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._weight = None
        self._height = None
        self._location = None
        self._bucket = None
        self._object = None
        self._x_request_id = None
        self.discriminator = None

        if index_url is not None:
            self.index_url = index_url
        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if location is not None:
            self.location = location
        if bucket is not None:
            self.bucket = bucket
        if object is not None:
            self.object = object
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def index_url(self):
        """Gets the index_url of this CreateRecordIndexResponse.

        索引文件地址

        :return: The index_url of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._index_url

    @index_url.setter
    def index_url(self, index_url):
        """Sets the index_url of this CreateRecordIndexResponse.

        索引文件地址

        :param index_url: The index_url of this CreateRecordIndexResponse.
        :type index_url: str
        """
        self._index_url = index_url

    @property
    def publish_domain(self):
        """Gets the publish_domain of this CreateRecordIndexResponse.

        直播推流域名

        :return: The publish_domain of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this CreateRecordIndexResponse.

        直播推流域名

        :param publish_domain: The publish_domain of this CreateRecordIndexResponse.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this CreateRecordIndexResponse.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :return: The app of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this CreateRecordIndexResponse.

        应用名，如果任意应用填写*。录制规则匹配的时候，优先精确app匹配，如果匹配不到，则匹配*

        :param app: The app of this CreateRecordIndexResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this CreateRecordIndexResponse.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :return: The stream of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this CreateRecordIndexResponse.

        录制的流名，如果任意流名则填写*。录制规则匹配的时候，优先精确stream匹配，如果匹配不到，则匹配*

        :param stream: The stream of this CreateRecordIndexResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        """Gets the start_time of this CreateRecordIndexResponse.

        开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的开始时间)

        :return: The start_time of this CreateRecordIndexResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateRecordIndexResponse.

        开始时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的开始时间)

        :param start_time: The start_time of this CreateRecordIndexResponse.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CreateRecordIndexResponse.

        结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的结束时间)

        :return: The end_time of this CreateRecordIndexResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateRecordIndexResponse.

        结束时间。格式为：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。(实际视频的结束时间)

        :param end_time: The end_time of this CreateRecordIndexResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this CreateRecordIndexResponse.

        录制时长。单位：秒。

        :return: The duration of this CreateRecordIndexResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CreateRecordIndexResponse.

        录制时长。单位：秒。

        :param duration: The duration of this CreateRecordIndexResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def weight(self):
        """Gets the weight of this CreateRecordIndexResponse.

        视频宽。

        :return: The weight of this CreateRecordIndexResponse.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateRecordIndexResponse.

        视频宽。

        :param weight: The weight of this CreateRecordIndexResponse.
        :type weight: int
        """
        self._weight = weight

    @property
    def height(self):
        """Gets the height of this CreateRecordIndexResponse.

        视频高。

        :return: The height of this CreateRecordIndexResponse.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CreateRecordIndexResponse.

        视频高。

        :param height: The height of this CreateRecordIndexResponse.
        :type height: int
        """
        self._height = height

    @property
    def location(self):
        """Gets the location of this CreateRecordIndexResponse.

        OBS Bucket所在RegionID

        :return: The location of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateRecordIndexResponse.

        OBS Bucket所在RegionID

        :param location: The location of this CreateRecordIndexResponse.
        :type location: str
        """
        self._location = location

    @property
    def bucket(self):
        """Gets the bucket of this CreateRecordIndexResponse.

        桶名称

        :return: The bucket of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CreateRecordIndexResponse.

        桶名称

        :param bucket: The bucket of this CreateRecordIndexResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """Gets the object of this CreateRecordIndexResponse.

        m3u8文件路径。默认Index/{publish_domain}/{app}/{stream}-{start_time}-{end_time}

        :return: The object of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CreateRecordIndexResponse.

        m3u8文件路径。默认Index/{publish_domain}/{app}/{stream}-{start_time}-{end_time}

        :param object: The object of this CreateRecordIndexResponse.
        :type object: str
        """
        self._object = object

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CreateRecordIndexResponse.

        :return: The x_request_id of this CreateRecordIndexResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CreateRecordIndexResponse.

        :param x_request_id: The x_request_id of this CreateRecordIndexResponse.
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
        if not isinstance(other, CreateRecordIndexResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
