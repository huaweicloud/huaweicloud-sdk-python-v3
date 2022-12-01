# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeReqDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'log_configs': 'list[LogConfig]',
        'tags': 'list[TagObject]',
        'event_validity_period': 'int',
        'enable_gpu': 'bool',
        'enable_npu': 'bool',
        'npu_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'log_configs': 'log_configs',
        'tags': 'tags',
        'event_validity_period': 'event_validity_period',
        'enable_gpu': 'enable_gpu',
        'enable_npu': 'enable_npu',
        'npu_type': 'npu_type'
    }

    def __init__(self, description=None, log_configs=None, tags=None, event_validity_period=None, enable_gpu=None, enable_npu=None, npu_type=None):
        """UpdateNodeReqDetail

        The model defined in huaweicloud sdk

        :param description: 设备描述，最大长度255，不允许^, ~, ＃, $, %, &amp;, *, &lt;, &gt;, (, ), [, ], {, }, &#39;, \&quot;, \\
        :type description: str
        :param log_configs: 设备日志配置
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        :param tags: 设备标签，标签个数最多为20个
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        :param event_validity_period: 事件有效时间(单位：分钟)
        :type event_validity_period: int
        :param enable_gpu: 是否开启gpu
        :type enable_gpu: bool
        :param enable_npu: 是否开启npu
        :type enable_npu: bool
        :param npu_type: npu类型，如果选择开启npu, 可设置类型Ascend 310/ Ascend 710, 如果选择开启gpu，请设置值为null。
        :type npu_type: str
        """
        
        

        self._description = None
        self._log_configs = None
        self._tags = None
        self._event_validity_period = None
        self._enable_gpu = None
        self._enable_npu = None
        self._npu_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if log_configs is not None:
            self.log_configs = log_configs
        if tags is not None:
            self.tags = tags
        if event_validity_period is not None:
            self.event_validity_period = event_validity_period
        if enable_gpu is not None:
            self.enable_gpu = enable_gpu
        if enable_npu is not None:
            self.enable_npu = enable_npu
        if npu_type is not None:
            self.npu_type = npu_type

    @property
    def description(self):
        """Gets the description of this UpdateNodeReqDetail.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :return: The description of this UpdateNodeReqDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateNodeReqDetail.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :param description: The description of this UpdateNodeReqDetail.
        :type description: str
        """
        self._description = description

    @property
    def log_configs(self):
        """Gets the log_configs of this UpdateNodeReqDetail.

        设备日志配置

        :return: The log_configs of this UpdateNodeReqDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this UpdateNodeReqDetail.

        设备日志配置

        :param log_configs: The log_configs of this UpdateNodeReqDetail.
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        self._log_configs = log_configs

    @property
    def tags(self):
        """Gets the tags of this UpdateNodeReqDetail.

        设备标签，标签个数最多为20个

        :return: The tags of this UpdateNodeReqDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateNodeReqDetail.

        设备标签，标签个数最多为20个

        :param tags: The tags of this UpdateNodeReqDetail.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        self._tags = tags

    @property
    def event_validity_period(self):
        """Gets the event_validity_period of this UpdateNodeReqDetail.

        事件有效时间(单位：分钟)

        :return: The event_validity_period of this UpdateNodeReqDetail.
        :rtype: int
        """
        return self._event_validity_period

    @event_validity_period.setter
    def event_validity_period(self, event_validity_period):
        """Sets the event_validity_period of this UpdateNodeReqDetail.

        事件有效时间(单位：分钟)

        :param event_validity_period: The event_validity_period of this UpdateNodeReqDetail.
        :type event_validity_period: int
        """
        self._event_validity_period = event_validity_period

    @property
    def enable_gpu(self):
        """Gets the enable_gpu of this UpdateNodeReqDetail.

        是否开启gpu

        :return: The enable_gpu of this UpdateNodeReqDetail.
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        """Sets the enable_gpu of this UpdateNodeReqDetail.

        是否开启gpu

        :param enable_gpu: The enable_gpu of this UpdateNodeReqDetail.
        :type enable_gpu: bool
        """
        self._enable_gpu = enable_gpu

    @property
    def enable_npu(self):
        """Gets the enable_npu of this UpdateNodeReqDetail.

        是否开启npu

        :return: The enable_npu of this UpdateNodeReqDetail.
        :rtype: bool
        """
        return self._enable_npu

    @enable_npu.setter
    def enable_npu(self, enable_npu):
        """Sets the enable_npu of this UpdateNodeReqDetail.

        是否开启npu

        :param enable_npu: The enable_npu of this UpdateNodeReqDetail.
        :type enable_npu: bool
        """
        self._enable_npu = enable_npu

    @property
    def npu_type(self):
        """Gets the npu_type of this UpdateNodeReqDetail.

        npu类型，如果选择开启npu, 可设置类型Ascend 310/ Ascend 710, 如果选择开启gpu，请设置值为null。

        :return: The npu_type of this UpdateNodeReqDetail.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this UpdateNodeReqDetail.

        npu类型，如果选择开启npu, 可设置类型Ascend 310/ Ascend 710, 如果选择开启gpu，请设置值为null。

        :param npu_type: The npu_type of this UpdateNodeReqDetail.
        :type npu_type: str
        """
        self._npu_type = npu_type

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
        if not isinstance(other, UpdateNodeReqDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
