# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagSatisfactionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'updated_time': 'updated_time'
    }

    def __init__(self, request_id=None, updated_time=None):
        """TagSatisfactionResponse

        The model defined in huaweicloud sdk

        :param request_id: 调用成功时的返回请求ID。  调用失败时无此字段。
        :type request_id: str
        :param updated_time: 反馈满意度的时间。格式为“yyyy-MM-dd THH:mm:ssZ”。其中，T指某个时间的开始；Z指UTC时间。  调用失败时无此字段。
        :type updated_time: str
        """
        
        super(TagSatisfactionResponse, self).__init__()

        self._request_id = None
        self._updated_time = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def request_id(self):
        """Gets the request_id of this TagSatisfactionResponse.

        调用成功时的返回请求ID。  调用失败时无此字段。

        :return: The request_id of this TagSatisfactionResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TagSatisfactionResponse.

        调用成功时的返回请求ID。  调用失败时无此字段。

        :param request_id: The request_id of this TagSatisfactionResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def updated_time(self):
        """Gets the updated_time of this TagSatisfactionResponse.

        反馈满意度的时间。格式为“yyyy-MM-dd THH:mm:ssZ”。其中，T指某个时间的开始；Z指UTC时间。  调用失败时无此字段。

        :return: The updated_time of this TagSatisfactionResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this TagSatisfactionResponse.

        反馈满意度的时间。格式为“yyyy-MM-dd THH:mm:ssZ”。其中，T指某个时间的开始；Z指UTC时间。  调用失败时无此字段。

        :param updated_time: The updated_time of this TagSatisfactionResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, TagSatisfactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
