# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2BitrateInfo:

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
        'start_time': 'str',
        'end_time': 'str',
        'data_list': 'list[int]'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'data_list': 'data_list'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, start_time=None, end_time=None, data_list=None):
        """V2BitrateInfo

        The model defined in huaweicloud sdk

        :param publish_domain: 域名。
        :type publish_domain: str
        :param app: 应用名称。
        :type app: str
        :param stream: 流名。
        :type stream: str
        :param start_time: 采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type start_time: str
        :param end_time: 采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type end_time: str
        :param data_list: 码率信息列表，单位为Kbps。
        :type data_list: list[int]
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._data_list = None
        self.discriminator = None

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
        if data_list is not None:
            self.data_list = data_list

    @property
    def publish_domain(self):
        """Gets the publish_domain of this V2BitrateInfo.

        域名。

        :return: The publish_domain of this V2BitrateInfo.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this V2BitrateInfo.

        域名。

        :param publish_domain: The publish_domain of this V2BitrateInfo.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this V2BitrateInfo.

        应用名称。

        :return: The app of this V2BitrateInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this V2BitrateInfo.

        应用名称。

        :param app: The app of this V2BitrateInfo.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this V2BitrateInfo.

        流名。

        :return: The stream of this V2BitrateInfo.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this V2BitrateInfo.

        流名。

        :param stream: The stream of this V2BitrateInfo.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        """Gets the start_time of this V2BitrateInfo.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The start_time of this V2BitrateInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V2BitrateInfo.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param start_time: The start_time of this V2BitrateInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this V2BitrateInfo.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The end_time of this V2BitrateInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this V2BitrateInfo.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param end_time: The end_time of this V2BitrateInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def data_list(self):
        """Gets the data_list of this V2BitrateInfo.

        码率信息列表，单位为Kbps。

        :return: The data_list of this V2BitrateInfo.
        :rtype: list[int]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        """Sets the data_list of this V2BitrateInfo.

        码率信息列表，单位为Kbps。

        :param data_list: The data_list of this V2BitrateInfo.
        :type data_list: list[int]
        """
        self._data_list = data_list

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
        if not isinstance(other, V2BitrateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
