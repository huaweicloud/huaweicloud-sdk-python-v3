# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsMultiTemplateTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sms_content': 'list[MsgContent]',
        'channel_num': 'str',
        'extend': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'sms_content': 'sms_content',
        'channel_num': 'channel_num',
        'extend': 'extend',
        'task_name': 'task_name'
    }

    def __init__(self, sms_content=None, channel_num=None, extend=None, task_name=None):
        """SmsMultiTemplateTaskRequestBody

        The model defined in huaweicloud sdk

        :param sms_content: 短信内容。
        :type sms_content: list[:class:`huaweicloudsdkkoomessage.v1.MsgContent`]
        :param channel_num: 短信通道号。  &gt; 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。 &gt; 签名和模板为对应关系，模板所属签名可在“短消息模板管理”查看。未填写时默认取sms_content第一条数据模板所属签名的通道号。
        :type channel_num: str
        :param extend: 扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。
        :type extend: str
        :param task_name: 发送任务名称。  &gt; 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。
        :type task_name: str
        """
        
        

        self._sms_content = None
        self._channel_num = None
        self._extend = None
        self._task_name = None
        self.discriminator = None

        self.sms_content = sms_content
        self.channel_num = channel_num
        if extend is not None:
            self.extend = extend
        if task_name is not None:
            self.task_name = task_name

    @property
    def sms_content(self):
        """Gets the sms_content of this SmsMultiTemplateTaskRequestBody.

        短信内容。

        :return: The sms_content of this SmsMultiTemplateTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.MsgContent`]
        """
        return self._sms_content

    @sms_content.setter
    def sms_content(self, sms_content):
        """Sets the sms_content of this SmsMultiTemplateTaskRequestBody.

        短信内容。

        :param sms_content: The sms_content of this SmsMultiTemplateTaskRequestBody.
        :type sms_content: list[:class:`huaweicloudsdkkoomessage.v1.MsgContent`]
        """
        self._sms_content = sms_content

    @property
    def channel_num(self):
        """Gets the channel_num of this SmsMultiTemplateTaskRequestBody.

        短信通道号。  > 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。 > 签名和模板为对应关系，模板所属签名可在“短消息模板管理”查看。未填写时默认取sms_content第一条数据模板所属签名的通道号。

        :return: The channel_num of this SmsMultiTemplateTaskRequestBody.
        :rtype: str
        """
        return self._channel_num

    @channel_num.setter
    def channel_num(self, channel_num):
        """Sets the channel_num of this SmsMultiTemplateTaskRequestBody.

        短信通道号。  > 模板所属签名的通道号，可以从“云消息服务KooMessage-管理控制台-短消息配置（国内）-短消息签名管理-通道号”中获取。 > 签名和模板为对应关系，模板所属签名可在“短消息模板管理”查看。未填写时默认取sms_content第一条数据模板所属签名的通道号。

        :param channel_num: The channel_num of this SmsMultiTemplateTaskRequestBody.
        :type channel_num: str
        """
        self._channel_num = channel_num

    @property
    def extend(self):
        """Gets the extend of this SmsMultiTemplateTaskRequestBody.

        扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。

        :return: The extend of this SmsMultiTemplateTaskRequestBody.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this SmsMultiTemplateTaskRequestBody.

        扩展参数。  在状态报告中会原样返回。  不允许赋空值，不允许携带以下字符：“{”，“}”（即大括号）。

        :param extend: The extend of this SmsMultiTemplateTaskRequestBody.
        :type extend: str
        """
        self._extend = extend

    @property
    def task_name(self):
        """Gets the task_name of this SmsMultiTemplateTaskRequestBody.

        发送任务名称。  > 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。

        :return: The task_name of this SmsMultiTemplateTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this SmsMultiTemplateTaskRequestBody.

        发送任务名称。  > 不能为空白字符串，允许重复，为空时默认为Task_拼接当前时间值。

        :param task_name: The task_name of this SmsMultiTemplateTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, SmsMultiTemplateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
