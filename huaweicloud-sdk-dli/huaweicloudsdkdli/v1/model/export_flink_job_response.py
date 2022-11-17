# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFlinkJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'zip_file': 'list[str]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'zip_file': 'zip_file'
    }

    def __init__(self, is_success=None, message=None, zip_file=None):
        """ExportFlinkJobResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 消息内容
        :type message: str
        :param zip_file: OBS上导出作业zip文件名。
        :type zip_file: list[str]
        """
        
        super(ExportFlinkJobResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._zip_file = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if zip_file is not None:
            self.zip_file = zip_file

    @property
    def is_success(self):
        """Gets the is_success of this ExportFlinkJobResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ExportFlinkJobResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ExportFlinkJobResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ExportFlinkJobResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ExportFlinkJobResponse.

        消息内容

        :return: The message of this ExportFlinkJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ExportFlinkJobResponse.

        消息内容

        :param message: The message of this ExportFlinkJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def zip_file(self):
        """Gets the zip_file of this ExportFlinkJobResponse.

        OBS上导出作业zip文件名。

        :return: The zip_file of this ExportFlinkJobResponse.
        :rtype: list[str]
        """
        return self._zip_file

    @zip_file.setter
    def zip_file(self, zip_file):
        """Sets the zip_file of this ExportFlinkJobResponse.

        OBS上导出作业zip文件名。

        :param zip_file: The zip_file of this ExportFlinkJobResponse.
        :type zip_file: list[str]
        """
        self._zip_file = zip_file

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
        if not isinstance(other, ExportFlinkJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
