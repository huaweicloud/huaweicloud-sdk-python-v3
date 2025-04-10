# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsSendDetailQueryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cid': 'str',
        'msisdn': 'str',
        'sent_time': 'datetime',
        'received_time': 'datetime',
        'sms_status': 'int',
        'sms_content': 'str'
    }

    attribute_map = {
        'cid': 'cid',
        'msisdn': 'msisdn',
        'sent_time': 'sent_time',
        'received_time': 'received_time',
        'sms_status': 'sms_status',
        'sms_content': 'sms_content'
    }

    def __init__(self, cid=None, msisdn=None, sent_time=None, received_time=None, sms_status=None, sms_content=None):
        r"""SmsSendDetailQueryVo

        The model defined in huaweicloud sdk

        :param cid: 容器ID
        :type cid: str
        :param msisdn: MSISDN
        :type msisdn: str
        :param sent_time: 发送时间
        :type sent_time: datetime
        :param received_time: 接收时间
        :type received_time: datetime
        :param sms_status: 短信状态:1发送中 2.已送达 3.失败
        :type sms_status: int
        :param sms_content: 短信内容
        :type sms_content: str
        """
        
        

        self._cid = None
        self._msisdn = None
        self._sent_time = None
        self._received_time = None
        self._sms_status = None
        self._sms_content = None
        self.discriminator = None

        if cid is not None:
            self.cid = cid
        if msisdn is not None:
            self.msisdn = msisdn
        if sent_time is not None:
            self.sent_time = sent_time
        if received_time is not None:
            self.received_time = received_time
        if sms_status is not None:
            self.sms_status = sms_status
        if sms_content is not None:
            self.sms_content = sms_content

    @property
    def cid(self):
        r"""Gets the cid of this SmsSendDetailQueryVo.

        容器ID

        :return: The cid of this SmsSendDetailQueryVo.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        r"""Sets the cid of this SmsSendDetailQueryVo.

        容器ID

        :param cid: The cid of this SmsSendDetailQueryVo.
        :type cid: str
        """
        self._cid = cid

    @property
    def msisdn(self):
        r"""Gets the msisdn of this SmsSendDetailQueryVo.

        MSISDN

        :return: The msisdn of this SmsSendDetailQueryVo.
        :rtype: str
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        r"""Sets the msisdn of this SmsSendDetailQueryVo.

        MSISDN

        :param msisdn: The msisdn of this SmsSendDetailQueryVo.
        :type msisdn: str
        """
        self._msisdn = msisdn

    @property
    def sent_time(self):
        r"""Gets the sent_time of this SmsSendDetailQueryVo.

        发送时间

        :return: The sent_time of this SmsSendDetailQueryVo.
        :rtype: datetime
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        r"""Sets the sent_time of this SmsSendDetailQueryVo.

        发送时间

        :param sent_time: The sent_time of this SmsSendDetailQueryVo.
        :type sent_time: datetime
        """
        self._sent_time = sent_time

    @property
    def received_time(self):
        r"""Gets the received_time of this SmsSendDetailQueryVo.

        接收时间

        :return: The received_time of this SmsSendDetailQueryVo.
        :rtype: datetime
        """
        return self._received_time

    @received_time.setter
    def received_time(self, received_time):
        r"""Sets the received_time of this SmsSendDetailQueryVo.

        接收时间

        :param received_time: The received_time of this SmsSendDetailQueryVo.
        :type received_time: datetime
        """
        self._received_time = received_time

    @property
    def sms_status(self):
        r"""Gets the sms_status of this SmsSendDetailQueryVo.

        短信状态:1发送中 2.已送达 3.失败

        :return: The sms_status of this SmsSendDetailQueryVo.
        :rtype: int
        """
        return self._sms_status

    @sms_status.setter
    def sms_status(self, sms_status):
        r"""Sets the sms_status of this SmsSendDetailQueryVo.

        短信状态:1发送中 2.已送达 3.失败

        :param sms_status: The sms_status of this SmsSendDetailQueryVo.
        :type sms_status: int
        """
        self._sms_status = sms_status

    @property
    def sms_content(self):
        r"""Gets the sms_content of this SmsSendDetailQueryVo.

        短信内容

        :return: The sms_content of this SmsSendDetailQueryVo.
        :rtype: str
        """
        return self._sms_content

    @sms_content.setter
    def sms_content(self, sms_content):
        r"""Sets the sms_content of this SmsSendDetailQueryVo.

        短信内容

        :param sms_content: The sms_content of this SmsSendDetailQueryVo.
        :type sms_content: str
        """
        self._sms_content = sms_content

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
        if not isinstance(other, SmsSendDetailQueryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
