# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelSqlResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, message=None, status=None):
        """CancelSqlResponse - a model defined in huaweicloud sdk"""
        
        super(CancelSqlResponse, self).__init__()

        self._message = None
        self._status = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def message(self):
        """Gets the message of this CancelSqlResponse.

        错误信息。

        :return: The message of this CancelSqlResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CancelSqlResponse.

        错误信息。

        :param message: The message of this CancelSqlResponse.
        :type: str
        """
        self._message = message

    @property
    def status(self):
        """Gets the status of this CancelSqlResponse.

        取消SQL的执行结果。  说明： 默认返回SUCCEED，对于已经结束的任务也会返回SUCCEED，只有取消正在运行的SQL时没成功才会FAILED。  枚举值： - SUCCEED：成功 - FAILED：失败

        :return: The status of this CancelSqlResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CancelSqlResponse.

        取消SQL的执行结果。  说明： 默认返回SUCCEED，对于已经结束的任务也会返回SUCCEED，只有取消正在运行的SQL时没成功才会FAILED。  枚举值： - SUCCEED：成功 - FAILED：失败

        :param status: The status of this CancelSqlResponse.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, CancelSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other