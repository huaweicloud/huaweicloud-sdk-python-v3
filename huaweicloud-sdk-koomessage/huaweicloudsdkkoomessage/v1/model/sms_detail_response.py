# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsDetailResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'to': 'str',
        'channel_num': 'str',
        'msg_id': 'str',
        'send_status': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'to': 'to',
        'channel_num': 'channel_num',
        'msg_id': 'msg_id',
        'send_status': 'send_status',
        'create_time': 'create_time'
    }

    def __init__(self, to=None, channel_num=None, msg_id=None, send_status=None, create_time=None):
        """SmsDetailResponse

        The model defined in huaweicloud sdk

        :param to: 短信接收方的号码。
        :type to: str
        :param channel_num: 短信发送方的号码。
        :type channel_num: str
        :param msg_id: 短信的唯一标识。
        :type msg_id: str
        :param send_status: 短信状态码。  以下举例状态码及其说明，具体处理建议请参考[API错误码](https://support.huaweicloud.com/api-msgsms/sms_05_0050.html)。  - 000000：短信平台处理请求成功 - E200015：待发送短信数量太大 - E200028：模板变量校验失败 - E200029：模板类型校验失败 - E200030：模板未激活 - E200031：协议校验失败 - E200033：模板类型不正确 - E200041：同一短信内容接收号码重复
        :type send_status: str
        :param create_time: 短信资源的创建时间。  即短信平台接收到用户发送短信请求的时间，为UTC时间。 格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。
        :type create_time: str
        """
        
        

        self._to = None
        self._channel_num = None
        self._msg_id = None
        self._send_status = None
        self._create_time = None
        self.discriminator = None

        self.to = to
        self.channel_num = channel_num
        self.msg_id = msg_id
        self.send_status = send_status
        self.create_time = create_time

    @property
    def to(self):
        """Gets the to of this SmsDetailResponse.

        短信接收方的号码。

        :return: The to of this SmsDetailResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SmsDetailResponse.

        短信接收方的号码。

        :param to: The to of this SmsDetailResponse.
        :type to: str
        """
        self._to = to

    @property
    def channel_num(self):
        """Gets the channel_num of this SmsDetailResponse.

        短信发送方的号码。

        :return: The channel_num of this SmsDetailResponse.
        :rtype: str
        """
        return self._channel_num

    @channel_num.setter
    def channel_num(self, channel_num):
        """Sets the channel_num of this SmsDetailResponse.

        短信发送方的号码。

        :param channel_num: The channel_num of this SmsDetailResponse.
        :type channel_num: str
        """
        self._channel_num = channel_num

    @property
    def msg_id(self):
        """Gets the msg_id of this SmsDetailResponse.

        短信的唯一标识。

        :return: The msg_id of this SmsDetailResponse.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        """Sets the msg_id of this SmsDetailResponse.

        短信的唯一标识。

        :param msg_id: The msg_id of this SmsDetailResponse.
        :type msg_id: str
        """
        self._msg_id = msg_id

    @property
    def send_status(self):
        """Gets the send_status of this SmsDetailResponse.

        短信状态码。  以下举例状态码及其说明，具体处理建议请参考[API错误码](https://support.huaweicloud.com/api-msgsms/sms_05_0050.html)。  - 000000：短信平台处理请求成功 - E200015：待发送短信数量太大 - E200028：模板变量校验失败 - E200029：模板类型校验失败 - E200030：模板未激活 - E200031：协议校验失败 - E200033：模板类型不正确 - E200041：同一短信内容接收号码重复

        :return: The send_status of this SmsDetailResponse.
        :rtype: str
        """
        return self._send_status

    @send_status.setter
    def send_status(self, send_status):
        """Sets the send_status of this SmsDetailResponse.

        短信状态码。  以下举例状态码及其说明，具体处理建议请参考[API错误码](https://support.huaweicloud.com/api-msgsms/sms_05_0050.html)。  - 000000：短信平台处理请求成功 - E200015：待发送短信数量太大 - E200028：模板变量校验失败 - E200029：模板类型校验失败 - E200030：模板未激活 - E200031：协议校验失败 - E200033：模板类型不正确 - E200041：同一短信内容接收号码重复

        :param send_status: The send_status of this SmsDetailResponse.
        :type send_status: str
        """
        self._send_status = send_status

    @property
    def create_time(self):
        """Gets the create_time of this SmsDetailResponse.

        短信资源的创建时间。  即短信平台接收到用户发送短信请求的时间，为UTC时间。 格式为：yyyy-MM-dd'T'HH:mm:ss'Z'。

        :return: The create_time of this SmsDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SmsDetailResponse.

        短信资源的创建时间。  即短信平台接收到用户发送短信请求的时间，为UTC时间。 格式为：yyyy-MM-dd'T'HH:mm:ss'Z'。

        :param create_time: The create_time of this SmsDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, SmsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
