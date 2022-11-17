# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordIndexRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'object': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'object': 'object'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, start_time=None, end_time=None, object=None):
        """RecordIndexRequestBody

        The model defined in huaweicloud sdk

        :param publish_domain: 推流域名
        :type publish_domain: str
        :param app: app名
        :type app: str
        :param stream: 流名
        :type stream: str
        :param start_time: 开始时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。
        :type start_time: datetime
        :param end_time: 结束时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。结束时间不允许大于当前时间。
        :type end_time: datetime
        :param object: \&quot;m3u8文件在OBS中的储存路径。支持下列字符串的转义   - {publish_domain}   - {app}   - {stream}   - {start_time}   - {end_time} 其中{start_time},{end_time}为返回结果的实际时间。 默认值为Index/{publish_domain}/{app}/{stream}/{stream}-{start_time}-{end_time}\&quot;
        :type object: str
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._object = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream
        self.start_time = start_time
        self.end_time = end_time
        if object is not None:
            self.object = object

    @property
    def publish_domain(self):
        """Gets the publish_domain of this RecordIndexRequestBody.

        推流域名

        :return: The publish_domain of this RecordIndexRequestBody.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this RecordIndexRequestBody.

        推流域名

        :param publish_domain: The publish_domain of this RecordIndexRequestBody.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this RecordIndexRequestBody.

        app名

        :return: The app of this RecordIndexRequestBody.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RecordIndexRequestBody.

        app名

        :param app: The app of this RecordIndexRequestBody.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this RecordIndexRequestBody.

        流名

        :return: The stream of this RecordIndexRequestBody.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this RecordIndexRequestBody.

        流名

        :param stream: The stream of this RecordIndexRequestBody.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        """Gets the start_time of this RecordIndexRequestBody.

        开始时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。

        :return: The start_time of this RecordIndexRequestBody.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RecordIndexRequestBody.

        开始时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。

        :param start_time: The start_time of this RecordIndexRequestBody.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RecordIndexRequestBody.

        结束时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。结束时间不允许大于当前时间。

        :return: The end_time of this RecordIndexRequestBody.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RecordIndexRequestBody.

        结束时间。格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间），开始时间与结束时间的间隔最大为12小时。结束时间不允许大于当前时间。

        :param end_time: The end_time of this RecordIndexRequestBody.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def object(self):
        """Gets the object of this RecordIndexRequestBody.

        \"m3u8文件在OBS中的储存路径。支持下列字符串的转义   - {publish_domain}   - {app}   - {stream}   - {start_time}   - {end_time} 其中{start_time},{end_time}为返回结果的实际时间。 默认值为Index/{publish_domain}/{app}/{stream}/{stream}-{start_time}-{end_time}\"

        :return: The object of this RecordIndexRequestBody.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this RecordIndexRequestBody.

        \"m3u8文件在OBS中的储存路径。支持下列字符串的转义   - {publish_domain}   - {app}   - {stream}   - {start_time}   - {end_time} 其中{start_time},{end_time}为返回结果的实际时间。 默认值为Index/{publish_domain}/{app}/{stream}/{stream}-{start_time}-{end_time}\"

        :param object: The object of this RecordIndexRequestBody.
        :type object: str
        """
        self._object = object

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
        if not isinstance(other, RecordIndexRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
