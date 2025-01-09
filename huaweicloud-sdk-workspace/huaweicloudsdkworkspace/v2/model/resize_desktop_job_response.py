# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeDesktopJobResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'desktop_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'desktop_id': 'desktop_id',
        'job_id': 'job_id'
    }

    def __init__(self, error_code=None, error_msg=None, desktop_id=None, job_id=None):
        """ResizeDesktopJobResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码，失败时返回。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._desktop_id = None
        self._job_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def error_code(self):
        """Gets the error_code of this ResizeDesktopJobResponse.

        错误码，失败时返回。

        :return: The error_code of this ResizeDesktopJobResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ResizeDesktopJobResponse.

        错误码，失败时返回。

        :param error_code: The error_code of this ResizeDesktopJobResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ResizeDesktopJobResponse.

        错误描述。

        :return: The error_msg of this ResizeDesktopJobResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ResizeDesktopJobResponse.

        错误描述。

        :param error_msg: The error_msg of this ResizeDesktopJobResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ResizeDesktopJobResponse.

        桌面ID。

        :return: The desktop_id of this ResizeDesktopJobResponse.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ResizeDesktopJobResponse.

        桌面ID。

        :param desktop_id: The desktop_id of this ResizeDesktopJobResponse.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def job_id(self):
        """Gets the job_id of this ResizeDesktopJobResponse.

        任务ID。

        :return: The job_id of this ResizeDesktopJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ResizeDesktopJobResponse.

        任务ID。

        :param job_id: The job_id of this ResizeDesktopJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ResizeDesktopJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
