# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSpriteTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'output': 'ImageSpriteTaskOutPut'
    }

    attribute_map = {
        'status': 'status',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'output': 'output'
    }

    def __init__(self, status=None, error_code=None, error_msg=None, output=None):
        r"""ImageSpriteTask

        The model defined in huaweicloud sdk

        :param status: 任务状态，包含成功，失败
        :type status: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ImageSpriteTaskOutPut`
        """
        
        

        self._status = None
        self._error_code = None
        self._error_msg = None
        self._output = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if output is not None:
            self.output = output

    @property
    def status(self):
        r"""Gets the status of this ImageSpriteTask.

        任务状态，包含成功，失败

        :return: The status of this ImageSpriteTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ImageSpriteTask.

        任务状态，包含成功，失败

        :param status: The status of this ImageSpriteTask.
        :type status: str
        """
        self._status = status

    @property
    def error_code(self):
        r"""Gets the error_code of this ImageSpriteTask.

        错误码

        :return: The error_code of this ImageSpriteTask.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ImageSpriteTask.

        错误码

        :param error_code: The error_code of this ImageSpriteTask.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ImageSpriteTask.

        错误信息

        :return: The error_msg of this ImageSpriteTask.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ImageSpriteTask.

        错误信息

        :param error_msg: The error_msg of this ImageSpriteTask.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def output(self):
        r"""Gets the output of this ImageSpriteTask.

        :return: The output of this ImageSpriteTask.
        :rtype: :class:`huaweicloudsdkvod.v1.ImageSpriteTaskOutPut`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ImageSpriteTask.

        :param output: The output of this ImageSpriteTask.
        :type output: :class:`huaweicloudsdkvod.v1.ImageSpriteTaskOutPut`
        """
        self._output = output

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
        if not isinstance(other, ImageSpriteTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
