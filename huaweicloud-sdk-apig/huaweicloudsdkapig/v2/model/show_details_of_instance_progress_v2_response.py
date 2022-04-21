# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfInstanceProgressV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'progress': 'int',
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'progress': 'progress',
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, progress=None, status=None, error_code=None, error_msg=None, start_time=None, end_time=None):
        """ShowDetailsOfInstanceProgressV2Response

        The model defined in huaweicloud sdk

        :param progress: 实例创建进度  单位：百分比
        :type progress: int
        :param status: 实例创建状态 - creating：创建中 - success：创建成功 - failed：创建失败
        :type status: str
        :param error_code: 实例创建失败错误码
        :type error_code: str
        :param error_msg: 实例创建失败错误信息
        :type error_msg: str
        :param start_time: 实例创建开始时间。unix时间戳格式。
        :type start_time: int
        :param end_time: 实例创建结束时间。unix时间戳格式。
        :type end_time: int
        """
        
        super(ShowDetailsOfInstanceProgressV2Response, self).__init__()

        self._progress = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def progress(self):
        """Gets the progress of this ShowDetailsOfInstanceProgressV2Response.

        实例创建进度  单位：百分比

        :return: The progress of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowDetailsOfInstanceProgressV2Response.

        实例创建进度  单位：百分比

        :param progress: The progress of this ShowDetailsOfInstanceProgressV2Response.
        :type progress: int
        """
        self._progress = progress

    @property
    def status(self):
        """Gets the status of this ShowDetailsOfInstanceProgressV2Response.

        实例创建状态 - creating：创建中 - success：创建成功 - failed：创建失败

        :return: The status of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDetailsOfInstanceProgressV2Response.

        实例创建状态 - creating：创建中 - success：创建成功 - failed：创建失败

        :param status: The status of this ShowDetailsOfInstanceProgressV2Response.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this ShowDetailsOfInstanceProgressV2Response.

        实例创建失败错误码

        :return: The error_code of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowDetailsOfInstanceProgressV2Response.

        实例创建失败错误码

        :param error_code: The error_code of this ShowDetailsOfInstanceProgressV2Response.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ShowDetailsOfInstanceProgressV2Response.

        实例创建失败错误信息

        :return: The error_msg of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ShowDetailsOfInstanceProgressV2Response.

        实例创建失败错误信息

        :param error_msg: The error_msg of this ShowDetailsOfInstanceProgressV2Response.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def start_time(self):
        """Gets the start_time of this ShowDetailsOfInstanceProgressV2Response.

        实例创建开始时间。unix时间戳格式。

        :return: The start_time of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDetailsOfInstanceProgressV2Response.

        实例创建开始时间。unix时间戳格式。

        :param start_time: The start_time of this ShowDetailsOfInstanceProgressV2Response.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDetailsOfInstanceProgressV2Response.

        实例创建结束时间。unix时间戳格式。

        :return: The end_time of this ShowDetailsOfInstanceProgressV2Response.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDetailsOfInstanceProgressV2Response.

        实例创建结束时间。unix时间戳格式。

        :param end_time: The end_time of this ShowDetailsOfInstanceProgressV2Response.
        :type end_time: int
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
        if not isinstance(other, ShowDetailsOfInstanceProgressV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
