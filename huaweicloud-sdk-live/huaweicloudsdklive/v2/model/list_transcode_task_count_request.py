# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeTaskCountRequest:


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
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domain=None, app=None, start_time=None, end_time=None):
        """ListTranscodeTaskCountRequest - a model defined in huaweicloud sdk"""
        
        

        self._publish_domain = None
        self._app = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domain(self):
        """Gets the publish_domain of this ListTranscodeTaskCountRequest.

        推流域名

        :return: The publish_domain of this ListTranscodeTaskCountRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this ListTranscodeTaskCountRequest.

        推流域名

        :param publish_domain: The publish_domain of this ListTranscodeTaskCountRequest.
        :type: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this ListTranscodeTaskCountRequest.

        应用名称，若查询结果为空，表示该应用下没有转码任务。

        :return: The app of this ListTranscodeTaskCountRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListTranscodeTaskCountRequest.

        应用名称，若查询结果为空，表示该应用下没有转码任务。

        :param app: The app of this ListTranscodeTaskCountRequest.
        :type: str
        """
        self._app = app

    @property
    def start_time(self):
        """Gets the start_time of this ListTranscodeTaskCountRequest.

        查询起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度7天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ListTranscodeTaskCountRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListTranscodeTaskCountRequest.

        查询起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度7天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ListTranscodeTaskCountRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListTranscodeTaskCountRequest.

        查询结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度7天，最大查询周期90天。  结束时间需大于起始时间。  若参数为空，默认为当前时间。 

        :return: The end_time of this ListTranscodeTaskCountRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListTranscodeTaskCountRequest.

        查询结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度7天，最大查询周期90天。  结束时间需大于起始时间。  若参数为空，默认为当前时间。 

        :param end_time: The end_time of this ListTranscodeTaskCountRequest.
        :type: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListTranscodeTaskCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other