# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamForbiddenList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'stream_name': 'str',
        'resume_time': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'resume_time': 'resume_time'
    }

    def __init__(self, app_name=None, stream_name=None, resume_time=None):
        """StreamForbiddenList

        The model defined in huaweicloud sdk

        :param app_name: 流应用名称
        :type app_name: str
        :param stream_name: 流名称
        :type stream_name: str
        :param resume_time: 恢复流时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间，不指定则默认7天，最大禁推为90天
        :type resume_time: str
        """
        
        

        self._app_name = None
        self._stream_name = None
        self._resume_time = None
        self.discriminator = None

        self.app_name = app_name
        self.stream_name = stream_name
        if resume_time is not None:
            self.resume_time = resume_time

    @property
    def app_name(self):
        """Gets the app_name of this StreamForbiddenList.

        流应用名称

        :return: The app_name of this StreamForbiddenList.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this StreamForbiddenList.

        流应用名称

        :param app_name: The app_name of this StreamForbiddenList.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this StreamForbiddenList.

        流名称

        :return: The stream_name of this StreamForbiddenList.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this StreamForbiddenList.

        流名称

        :param stream_name: The stream_name of this StreamForbiddenList.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def resume_time(self):
        """Gets the resume_time of this StreamForbiddenList.

        恢复流时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间，不指定则默认7天，最大禁推为90天

        :return: The resume_time of this StreamForbiddenList.
        :rtype: str
        """
        return self._resume_time

    @resume_time.setter
    def resume_time(self, resume_time):
        """Sets the resume_time of this StreamForbiddenList.

        恢复流时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间，不指定则默认7天，最大禁推为90天

        :param resume_time: The resume_time of this StreamForbiddenList.
        :type resume_time: str
        """
        self._resume_time = resume_time

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
        if not isinstance(other, StreamForbiddenList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
