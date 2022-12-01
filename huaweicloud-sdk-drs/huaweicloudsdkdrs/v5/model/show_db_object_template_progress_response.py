# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDbObjectTemplateProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'send_success': 'bool',
        'process_status': 'str',
        'parsed_success_number': 'str'
    }

    attribute_map = {
        'send_success': 'send_success',
        'process_status': 'process_status',
        'parsed_success_number': 'parsed_success_number'
    }

    def __init__(self, send_success=None, process_status=None, parsed_success_number=None):
        """ShowDbObjectTemplateProgressResponse

        The model defined in huaweicloud sdk

        :param send_success: 是否上传完成。
        :type send_success: bool
        :param process_status: 文件解析状态。
        :type process_status: str
        :param parsed_success_number: 解析成功的行数。
        :type parsed_success_number: str
        """
        
        super(ShowDbObjectTemplateProgressResponse, self).__init__()

        self._send_success = None
        self._process_status = None
        self._parsed_success_number = None
        self.discriminator = None

        if send_success is not None:
            self.send_success = send_success
        if process_status is not None:
            self.process_status = process_status
        if parsed_success_number is not None:
            self.parsed_success_number = parsed_success_number

    @property
    def send_success(self):
        """Gets the send_success of this ShowDbObjectTemplateProgressResponse.

        是否上传完成。

        :return: The send_success of this ShowDbObjectTemplateProgressResponse.
        :rtype: bool
        """
        return self._send_success

    @send_success.setter
    def send_success(self, send_success):
        """Sets the send_success of this ShowDbObjectTemplateProgressResponse.

        是否上传完成。

        :param send_success: The send_success of this ShowDbObjectTemplateProgressResponse.
        :type send_success: bool
        """
        self._send_success = send_success

    @property
    def process_status(self):
        """Gets the process_status of this ShowDbObjectTemplateProgressResponse.

        文件解析状态。

        :return: The process_status of this ShowDbObjectTemplateProgressResponse.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        """Sets the process_status of this ShowDbObjectTemplateProgressResponse.

        文件解析状态。

        :param process_status: The process_status of this ShowDbObjectTemplateProgressResponse.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def parsed_success_number(self):
        """Gets the parsed_success_number of this ShowDbObjectTemplateProgressResponse.

        解析成功的行数。

        :return: The parsed_success_number of this ShowDbObjectTemplateProgressResponse.
        :rtype: str
        """
        return self._parsed_success_number

    @parsed_success_number.setter
    def parsed_success_number(self, parsed_success_number):
        """Sets the parsed_success_number of this ShowDbObjectTemplateProgressResponse.

        解析成功的行数。

        :param parsed_success_number: The parsed_success_number of this ShowDbObjectTemplateProgressResponse.
        :type parsed_success_number: str
        """
        self._parsed_success_number = parsed_success_number

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
        if not isinstance(other, ShowDbObjectTemplateProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
