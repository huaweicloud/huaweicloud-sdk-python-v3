# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMSendTaskSmsChannel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_number': 'str',
        'sms_tpl_id': 'str',
        'sms_sign': 'str',
        'sms_app_name': 'str'
    }

    attribute_map = {
        'channel_number': 'channel_number',
        'sms_tpl_id': 'sms_tpl_id',
        'sms_sign': 'sms_sign',
        'sms_app_name': 'sms_app_name'
    }

    def __init__(self, channel_number=None, sms_tpl_id=None, sms_sign=None, sms_app_name=None):
        r"""AIMSendTaskSmsChannel

        The model defined in huaweicloud sdk

        :param channel_number: 短信通道号。  &gt; 预留字段，暂时为空。 
        :type channel_number: str
        :param sms_tpl_id: 短信模板ID。
        :type sms_tpl_id: str
        :param sms_sign: 短信签名。
        :type sms_sign: str
        :param sms_app_name: 短信应用名称。  &gt; 预留字段，暂时为空。 
        :type sms_app_name: str
        """
        
        

        self._channel_number = None
        self._sms_tpl_id = None
        self._sms_sign = None
        self._sms_app_name = None
        self.discriminator = None

        if channel_number is not None:
            self.channel_number = channel_number
        if sms_tpl_id is not None:
            self.sms_tpl_id = sms_tpl_id
        if sms_sign is not None:
            self.sms_sign = sms_sign
        if sms_app_name is not None:
            self.sms_app_name = sms_app_name

    @property
    def channel_number(self):
        r"""Gets the channel_number of this AIMSendTaskSmsChannel.

        短信通道号。  > 预留字段，暂时为空。 

        :return: The channel_number of this AIMSendTaskSmsChannel.
        :rtype: str
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        r"""Sets the channel_number of this AIMSendTaskSmsChannel.

        短信通道号。  > 预留字段，暂时为空。 

        :param channel_number: The channel_number of this AIMSendTaskSmsChannel.
        :type channel_number: str
        """
        self._channel_number = channel_number

    @property
    def sms_tpl_id(self):
        r"""Gets the sms_tpl_id of this AIMSendTaskSmsChannel.

        短信模板ID。

        :return: The sms_tpl_id of this AIMSendTaskSmsChannel.
        :rtype: str
        """
        return self._sms_tpl_id

    @sms_tpl_id.setter
    def sms_tpl_id(self, sms_tpl_id):
        r"""Sets the sms_tpl_id of this AIMSendTaskSmsChannel.

        短信模板ID。

        :param sms_tpl_id: The sms_tpl_id of this AIMSendTaskSmsChannel.
        :type sms_tpl_id: str
        """
        self._sms_tpl_id = sms_tpl_id

    @property
    def sms_sign(self):
        r"""Gets the sms_sign of this AIMSendTaskSmsChannel.

        短信签名。

        :return: The sms_sign of this AIMSendTaskSmsChannel.
        :rtype: str
        """
        return self._sms_sign

    @sms_sign.setter
    def sms_sign(self, sms_sign):
        r"""Sets the sms_sign of this AIMSendTaskSmsChannel.

        短信签名。

        :param sms_sign: The sms_sign of this AIMSendTaskSmsChannel.
        :type sms_sign: str
        """
        self._sms_sign = sms_sign

    @property
    def sms_app_name(self):
        r"""Gets the sms_app_name of this AIMSendTaskSmsChannel.

        短信应用名称。  > 预留字段，暂时为空。 

        :return: The sms_app_name of this AIMSendTaskSmsChannel.
        :rtype: str
        """
        return self._sms_app_name

    @sms_app_name.setter
    def sms_app_name(self, sms_app_name):
        r"""Sets the sms_app_name of this AIMSendTaskSmsChannel.

        短信应用名称。  > 预留字段，暂时为空。 

        :param sms_app_name: The sms_app_name of this AIMSendTaskSmsChannel.
        :type sms_app_name: str
        """
        self._sms_app_name = sms_app_name

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
        if not isinstance(other, AIMSendTaskSmsChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
