# coding: utf-8

import pprint
import re

import six





class AddSubscriptionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'protocol': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'protocol': 'protocol',
        'remark': 'remark'
    }

    def __init__(self, endpoint=None, protocol=None, remark=None):
        """AddSubscriptionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._endpoint = None
        self._protocol = None
        self._remark = None
        self.discriminator = None

        self.endpoint = endpoint
        self.protocol = protocol
        self.remark = remark

    @property
    def endpoint(self):
        """Gets the endpoint of this AddSubscriptionRequestBody.

        说明：http协议，接入点必须以“http://”开头。  https协议，接入点必须以“https://”开头。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  dms协议，接入点必须是一个消息队列。  application协议，接入点必须是一个应用平台的设备终端。  callnotify协议，接入点必须是一个电话号码。

        :return: The endpoint of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this AddSubscriptionRequestBody.

        说明：http协议，接入点必须以“http://”开头。  https协议，接入点必须以“https://”开头。  email协议，接入点必须是邮件地址。  sms协议，接入点必须是一个电话号码。  functionstage协议，接入点必须是一个函数。  functiongraph协议，接入点必须是一个函数工作流。  dms协议，接入点必须是一个消息队列。  application协议，接入点必须是一个应用平台的设备终端。  callnotify协议，接入点必须是一个电话号码。

        :param endpoint: The endpoint of this AddSubscriptionRequestBody.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def protocol(self):
        """Gets the protocol of this AddSubscriptionRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “default”  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。

        :return: The protocol of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AddSubscriptionRequestBody.

        不同协议对应不同的endpoint（接受消息的接入点）。 目前支持的协议包括：  “email”：邮件传输协议，endpoint为邮箱地址。  “default”  “sms”：短信传输协议，endpoint为手机号码。  “functionstage”：FunctionGraph（函数）传输协议，endpoint为一个函数。  “functiongraph”：FunctionGraph（工作流）传输协议，endpoint为由一组函数编排成的工作流。  “http”、“https”：HTTP/HTTPS传输协议，endpoint为URL。  “callnotify”：语音通知传输协议，endpoint为手机号码。

        :param protocol: The protocol of this AddSubscriptionRequestBody.
        :type: str
        """
        self._protocol = protocol

    @property
    def remark(self):
        """Gets the remark of this AddSubscriptionRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :return: The remark of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AddSubscriptionRequestBody.

        备注。最大支持128字节，约42个中文，必须是UTF-8编码的字符串，否则无法正常显示中文。

        :param remark: The remark of this AddSubscriptionRequestBody.
        :type: str
        """
        self._remark = remark

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
