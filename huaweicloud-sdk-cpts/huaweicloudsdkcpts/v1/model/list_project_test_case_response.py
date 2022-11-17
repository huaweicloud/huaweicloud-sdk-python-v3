# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectTestCaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'directory': 'list[ProjectDirectory]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'directory': 'directory'
    }

    def __init__(self, code=None, message=None, directory=None):
        """ListProjectTestCaseResponse

        The model defined in huaweicloud sdk

        :param code: 状态码
        :type code: str
        :param message: 描述
        :type message: str
        :param directory: 用例集
        :type directory: list[:class:`huaweicloudsdkcpts.v1.ProjectDirectory`]
        """
        
        super(ListProjectTestCaseResponse, self).__init__()

        self._code = None
        self._message = None
        self._directory = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if directory is not None:
            self.directory = directory

    @property
    def code(self):
        """Gets the code of this ListProjectTestCaseResponse.

        状态码

        :return: The code of this ListProjectTestCaseResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListProjectTestCaseResponse.

        状态码

        :param code: The code of this ListProjectTestCaseResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListProjectTestCaseResponse.

        描述

        :return: The message of this ListProjectTestCaseResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListProjectTestCaseResponse.

        描述

        :param message: The message of this ListProjectTestCaseResponse.
        :type message: str
        """
        self._message = message

    @property
    def directory(self):
        """Gets the directory of this ListProjectTestCaseResponse.

        用例集

        :return: The directory of this ListProjectTestCaseResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.ProjectDirectory`]
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ListProjectTestCaseResponse.

        用例集

        :param directory: The directory of this ListProjectTestCaseResponse.
        :type directory: list[:class:`huaweicloudsdkcpts.v1.ProjectDirectory`]
        """
        self._directory = directory

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
        if not isinstance(other, ListProjectTestCaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
