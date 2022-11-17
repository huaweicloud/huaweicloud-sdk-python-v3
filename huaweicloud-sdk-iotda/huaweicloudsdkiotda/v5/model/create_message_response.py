# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'result': 'MessageResult'
    }

    attribute_map = {
        'message_id': 'message_id',
        'result': 'result'
    }

    def __init__(self, message_id=None, result=None):
        """CreateMessageResponse

        The model defined in huaweicloud sdk

        :param message_id: 消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户不填写，则由物联网平台生成。
        :type message_id: str
        :param result: 
        :type result: :class:`huaweicloudsdkiotda.v5.MessageResult`
        """
        
        super(CreateMessageResponse, self).__init__()

        self._message_id = None
        self._result = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if result is not None:
            self.result = result

    @property
    def message_id(self):
        """Gets the message_id of this CreateMessageResponse.

        消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户不填写，则由物联网平台生成。

        :return: The message_id of this CreateMessageResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this CreateMessageResponse.

        消息id，由用户生成（推荐使用UUID），同一个设备下唯一， 如果用户不填写，则由物联网平台生成。

        :param message_id: The message_id of this CreateMessageResponse.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def result(self):
        """Gets the result of this CreateMessageResponse.

        :return: The result of this CreateMessageResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.MessageResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateMessageResponse.

        :param result: The result of this CreateMessageResponse.
        :type result: :class:`huaweicloudsdkiotda.v5.MessageResult`
        """
        self._result = result

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
        if not isinstance(other, CreateMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
