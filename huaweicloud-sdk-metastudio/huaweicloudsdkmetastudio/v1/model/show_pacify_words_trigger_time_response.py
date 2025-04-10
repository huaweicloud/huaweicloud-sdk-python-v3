# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPacifyWordsTriggerTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_time': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'trigger_time': 'trigger_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, trigger_time=None, x_request_id=None):
        r"""ShowPacifyWordsTriggerTimeResponse

        The model defined in huaweicloud sdk

        :param trigger_time: 安抚话术等待触发时长，单位毫秒
        :type trigger_time: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowPacifyWordsTriggerTimeResponse, self).__init__()

        self._trigger_time = None
        self._x_request_id = None
        self.discriminator = None

        if trigger_time is not None:
            self.trigger_time = trigger_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this ShowPacifyWordsTriggerTimeResponse.

        安抚话术等待触发时长，单位毫秒

        :return: The trigger_time of this ShowPacifyWordsTriggerTimeResponse.
        :rtype: int
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this ShowPacifyWordsTriggerTimeResponse.

        安抚话术等待触发时长，单位毫秒

        :param trigger_time: The trigger_time of this ShowPacifyWordsTriggerTimeResponse.
        :type trigger_time: int
        """
        self._trigger_time = trigger_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowPacifyWordsTriggerTimeResponse.

        :return: The x_request_id of this ShowPacifyWordsTriggerTimeResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowPacifyWordsTriggerTimeResponse.

        :param x_request_id: The x_request_id of this ShowPacifyWordsTriggerTimeResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowPacifyWordsTriggerTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
