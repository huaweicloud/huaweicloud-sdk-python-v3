# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNotifyPolicyResponse(SdkResponse):

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
        'id': 'str',
        'protocol': 'str',
        'polling': 'list[PollingPolicyResponse]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'id': 'id',
        'protocol': 'protocol',
        'polling': 'polling'
    }

    def __init__(self, request_id=None, id=None, protocol=None, polling=None):
        r"""ShowNotifyPolicyResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param id: 通知策略ID。
        :type id: str
        :param protocol: 通知策略类型，当前仅支持语音。
        :type protocol: str
        :param polling: 轮询策略订阅终端。
        :type polling: list[:class:`huaweicloudsdksmn.v2.PollingPolicyResponse`]
        """
        
        super(ShowNotifyPolicyResponse, self).__init__()

        self._request_id = None
        self._id = None
        self._protocol = None
        self._polling = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if id is not None:
            self.id = id
        if protocol is not None:
            self.protocol = protocol
        if polling is not None:
            self.polling = polling

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowNotifyPolicyResponse.

        请求ID。

        :return: The request_id of this ShowNotifyPolicyResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowNotifyPolicyResponse.

        请求ID。

        :param request_id: The request_id of this ShowNotifyPolicyResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def id(self):
        r"""Gets the id of this ShowNotifyPolicyResponse.

        通知策略ID。

        :return: The id of this ShowNotifyPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowNotifyPolicyResponse.

        通知策略ID。

        :param id: The id of this ShowNotifyPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def protocol(self):
        r"""Gets the protocol of this ShowNotifyPolicyResponse.

        通知策略类型，当前仅支持语音。

        :return: The protocol of this ShowNotifyPolicyResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ShowNotifyPolicyResponse.

        通知策略类型，当前仅支持语音。

        :param protocol: The protocol of this ShowNotifyPolicyResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def polling(self):
        r"""Gets the polling of this ShowNotifyPolicyResponse.

        轮询策略订阅终端。

        :return: The polling of this ShowNotifyPolicyResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.PollingPolicyResponse`]
        """
        return self._polling

    @polling.setter
    def polling(self, polling):
        r"""Sets the polling of this ShowNotifyPolicyResponse.

        轮询策略订阅终端。

        :param polling: The polling of this ShowNotifyPolicyResponse.
        :type polling: list[:class:`huaweicloudsdksmn.v2.PollingPolicyResponse`]
        """
        self._polling = polling

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
        if not isinstance(other, ShowNotifyPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
