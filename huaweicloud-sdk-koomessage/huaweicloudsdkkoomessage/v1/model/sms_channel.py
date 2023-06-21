# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsChannel:

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
        """SmsChannel

        The model defined in huaweicloud sdk

        :param channel_number: 短信通道号。  &gt; 必须与另外三个字段sms_tpl_id、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信签名管理-通道号”中获取。 
        :type channel_number: str
        :param sms_tpl_id: 短信模板ID。  &gt; 必须与另外三个字段channel_number、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-模板ID”中获取。 
        :type sms_tpl_id: str
        :param sms_sign: 短信签名。  &gt; 必须与另外三个字段channel_number、sms_tpl_id、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属签名”中获取。 
        :type sms_sign: str
        :param sms_app_name: 短信应用名称。  &gt; 必须与另外三个字段channel_number、sms_sign、sms_tpl_id相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属应用”中获取。 
        :type sms_app_name: str
        """
        
        

        self._channel_number = None
        self._sms_tpl_id = None
        self._sms_sign = None
        self._sms_app_name = None
        self.discriminator = None

        self.channel_number = channel_number
        self.sms_tpl_id = sms_tpl_id
        self.sms_sign = sms_sign
        self.sms_app_name = sms_app_name

    @property
    def channel_number(self):
        """Gets the channel_number of this SmsChannel.

        短信通道号。  > 必须与另外三个字段sms_tpl_id、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信签名管理-通道号”中获取。 

        :return: The channel_number of this SmsChannel.
        :rtype: str
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this SmsChannel.

        短信通道号。  > 必须与另外三个字段sms_tpl_id、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信签名管理-通道号”中获取。 

        :param channel_number: The channel_number of this SmsChannel.
        :type channel_number: str
        """
        self._channel_number = channel_number

    @property
    def sms_tpl_id(self):
        """Gets the sms_tpl_id of this SmsChannel.

        短信模板ID。  > 必须与另外三个字段channel_number、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-模板ID”中获取。 

        :return: The sms_tpl_id of this SmsChannel.
        :rtype: str
        """
        return self._sms_tpl_id

    @sms_tpl_id.setter
    def sms_tpl_id(self, sms_tpl_id):
        """Sets the sms_tpl_id of this SmsChannel.

        短信模板ID。  > 必须与另外三个字段channel_number、sms_sign、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-模板ID”中获取。 

        :param sms_tpl_id: The sms_tpl_id of this SmsChannel.
        :type sms_tpl_id: str
        """
        self._sms_tpl_id = sms_tpl_id

    @property
    def sms_sign(self):
        """Gets the sms_sign of this SmsChannel.

        短信签名。  > 必须与另外三个字段channel_number、sms_tpl_id、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属签名”中获取。 

        :return: The sms_sign of this SmsChannel.
        :rtype: str
        """
        return self._sms_sign

    @sms_sign.setter
    def sms_sign(self, sms_sign):
        """Sets the sms_sign of this SmsChannel.

        短信签名。  > 必须与另外三个字段channel_number、sms_tpl_id、sms_app_name相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属签名”中获取。 

        :param sms_sign: The sms_sign of this SmsChannel.
        :type sms_sign: str
        """
        self._sms_sign = sms_sign

    @property
    def sms_app_name(self):
        """Gets the sms_app_name of this SmsChannel.

        短信应用名称。  > 必须与另外三个字段channel_number、sms_sign、sms_tpl_id相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属应用”中获取。 

        :return: The sms_app_name of this SmsChannel.
        :rtype: str
        """
        return self._sms_app_name

    @sms_app_name.setter
    def sms_app_name(self, sms_app_name):
        """Sets the sms_app_name of this SmsChannel.

        短信应用名称。  > 必须与另外三个字段channel_number、sms_sign、sms_tpl_id相匹配，这些字段信息可以从“云消息服务KooMessage-管理控制台-短信配置-短信模板管理-所属应用”中获取。 

        :param sms_app_name: The sms_app_name of this SmsChannel.
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
        if not isinstance(other, SmsChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
