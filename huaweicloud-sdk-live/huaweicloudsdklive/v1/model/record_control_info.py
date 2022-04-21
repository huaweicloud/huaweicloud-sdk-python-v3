# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordControlInfo:

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
        'stream': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream'
    }

    def __init__(self, publish_domain=None, app=None, stream=None):
        """RecordControlInfo

        The model defined in huaweicloud sdk

        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param app: 应用名
        :type app: str
        :param stream: 待启动或停止录制的流名
        :type stream: str
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream

    @property
    def publish_domain(self):
        """Gets the publish_domain of this RecordControlInfo.

        直播推流域名

        :return: The publish_domain of this RecordControlInfo.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        """Sets the publish_domain of this RecordControlInfo.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordControlInfo.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        """Gets the app of this RecordControlInfo.

        应用名

        :return: The app of this RecordControlInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this RecordControlInfo.

        应用名

        :param app: The app of this RecordControlInfo.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this RecordControlInfo.

        待启动或停止录制的流名

        :return: The stream of this RecordControlInfo.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this RecordControlInfo.

        待启动或停止录制的流名

        :param stream: The stream of this RecordControlInfo.
        :type stream: str
        """
        self._stream = stream

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
        if not isinstance(other, RecordControlInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
