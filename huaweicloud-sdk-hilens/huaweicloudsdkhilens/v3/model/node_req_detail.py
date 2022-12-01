# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeReqDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch': 'int',
        'description': 'str',
        'enable_gpu': 'bool',
        'enable_npu': 'bool',
        'iam_user_id': 'str',
        'log_configs': 'list[LogConfig]',
        'name': 'str',
        'npu_type': 'str',
        'tags': 'list[TagObject]',
        'workspace_id': 'str',
        'event_validity_period': 'int'
    }

    attribute_map = {
        'batch': 'batch',
        'description': 'description',
        'enable_gpu': 'enable_gpu',
        'enable_npu': 'enable_npu',
        'iam_user_id': 'iam_user_id',
        'log_configs': 'log_configs',
        'name': 'name',
        'npu_type': 'npu_type',
        'tags': 'tags',
        'workspace_id': 'workspace_id',
        'event_validity_period': 'event_validity_period'
    }

    def __init__(self, batch=None, description=None, enable_gpu=None, enable_npu=None, iam_user_id=None, log_configs=None, name=None, npu_type=None, tags=None, workspace_id=None, event_validity_period=None):
        """NodeReqDetail

        The model defined in huaweicloud sdk

        :param batch: 批量注册数量。默认为单设备注册，即batch&#x3D;1，如果大于1即为批量注册的最大数量。最大上限数量为100000
        :type batch: int
        :param description: 设备描述，最大长度255，不允许^, ~, ＃, $, %, &amp;, *, &lt;, &gt;, (, ), [, ], {, }, &#39;, \&quot;, \\
        :type description: str
        :param enable_gpu: 是否开启GPU，true表示开启，false表示不开启，默认为false
        :type enable_gpu: bool
        :param enable_npu: 是否开启NPU，true表示开启，false表示不开启，默认为false
        :type enable_npu: bool
        :param iam_user_id: 子账号ID。当主账号注册设备时，可以指定将设备注册到指定的子账号下面。不填默认为该发起注册行为用户的user_id
        :type iam_user_id: str
        :param log_configs: 设备日志配置
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        :param name: 设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param npu_type: NPU类型，D310/D910。不填表示为D310类型。
        :type npu_type: str
        :param tags: 设备标签，标签个数最多为20个
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        :param workspace_id: 工作空间ID，不填为为主账号/子账号的默认工作空间
        :type workspace_id: str
        :param event_validity_period: 事件有效时间（单位：分钟）
        :type event_validity_period: int
        """
        
        

        self._batch = None
        self._description = None
        self._enable_gpu = None
        self._enable_npu = None
        self._iam_user_id = None
        self._log_configs = None
        self._name = None
        self._npu_type = None
        self._tags = None
        self._workspace_id = None
        self._event_validity_period = None
        self.discriminator = None

        if batch is not None:
            self.batch = batch
        if description is not None:
            self.description = description
        if enable_gpu is not None:
            self.enable_gpu = enable_gpu
        if enable_npu is not None:
            self.enable_npu = enable_npu
        if iam_user_id is not None:
            self.iam_user_id = iam_user_id
        if log_configs is not None:
            self.log_configs = log_configs
        self.name = name
        if npu_type is not None:
            self.npu_type = npu_type
        if tags is not None:
            self.tags = tags
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if event_validity_period is not None:
            self.event_validity_period = event_validity_period

    @property
    def batch(self):
        """Gets the batch of this NodeReqDetail.

        批量注册数量。默认为单设备注册，即batch=1，如果大于1即为批量注册的最大数量。最大上限数量为100000

        :return: The batch of this NodeReqDetail.
        :rtype: int
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this NodeReqDetail.

        批量注册数量。默认为单设备注册，即batch=1，如果大于1即为批量注册的最大数量。最大上限数量为100000

        :param batch: The batch of this NodeReqDetail.
        :type batch: int
        """
        self._batch = batch

    @property
    def description(self):
        """Gets the description of this NodeReqDetail.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :return: The description of this NodeReqDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NodeReqDetail.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :param description: The description of this NodeReqDetail.
        :type description: str
        """
        self._description = description

    @property
    def enable_gpu(self):
        """Gets the enable_gpu of this NodeReqDetail.

        是否开启GPU，true表示开启，false表示不开启，默认为false

        :return: The enable_gpu of this NodeReqDetail.
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        """Sets the enable_gpu of this NodeReqDetail.

        是否开启GPU，true表示开启，false表示不开启，默认为false

        :param enable_gpu: The enable_gpu of this NodeReqDetail.
        :type enable_gpu: bool
        """
        self._enable_gpu = enable_gpu

    @property
    def enable_npu(self):
        """Gets the enable_npu of this NodeReqDetail.

        是否开启NPU，true表示开启，false表示不开启，默认为false

        :return: The enable_npu of this NodeReqDetail.
        :rtype: bool
        """
        return self._enable_npu

    @enable_npu.setter
    def enable_npu(self, enable_npu):
        """Sets the enable_npu of this NodeReqDetail.

        是否开启NPU，true表示开启，false表示不开启，默认为false

        :param enable_npu: The enable_npu of this NodeReqDetail.
        :type enable_npu: bool
        """
        self._enable_npu = enable_npu

    @property
    def iam_user_id(self):
        """Gets the iam_user_id of this NodeReqDetail.

        子账号ID。当主账号注册设备时，可以指定将设备注册到指定的子账号下面。不填默认为该发起注册行为用户的user_id

        :return: The iam_user_id of this NodeReqDetail.
        :rtype: str
        """
        return self._iam_user_id

    @iam_user_id.setter
    def iam_user_id(self, iam_user_id):
        """Sets the iam_user_id of this NodeReqDetail.

        子账号ID。当主账号注册设备时，可以指定将设备注册到指定的子账号下面。不填默认为该发起注册行为用户的user_id

        :param iam_user_id: The iam_user_id of this NodeReqDetail.
        :type iam_user_id: str
        """
        self._iam_user_id = iam_user_id

    @property
    def log_configs(self):
        """Gets the log_configs of this NodeReqDetail.

        设备日志配置

        :return: The log_configs of this NodeReqDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this NodeReqDetail.

        设备日志配置

        :param log_configs: The log_configs of this NodeReqDetail.
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        self._log_configs = log_configs

    @property
    def name(self):
        """Gets the name of this NodeReqDetail.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this NodeReqDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeReqDetail.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this NodeReqDetail.
        :type name: str
        """
        self._name = name

    @property
    def npu_type(self):
        """Gets the npu_type of this NodeReqDetail.

        NPU类型，D310/D910。不填表示为D310类型。

        :return: The npu_type of this NodeReqDetail.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this NodeReqDetail.

        NPU类型，D310/D910。不填表示为D310类型。

        :param npu_type: The npu_type of this NodeReqDetail.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def tags(self):
        """Gets the tags of this NodeReqDetail.

        设备标签，标签个数最多为20个

        :return: The tags of this NodeReqDetail.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NodeReqDetail.

        设备标签，标签个数最多为20个

        :param tags: The tags of this NodeReqDetail.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.TagObject`]
        """
        self._tags = tags

    @property
    def workspace_id(self):
        """Gets the workspace_id of this NodeReqDetail.

        工作空间ID，不填为为主账号/子账号的默认工作空间

        :return: The workspace_id of this NodeReqDetail.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this NodeReqDetail.

        工作空间ID，不填为为主账号/子账号的默认工作空间

        :param workspace_id: The workspace_id of this NodeReqDetail.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def event_validity_period(self):
        """Gets the event_validity_period of this NodeReqDetail.

        事件有效时间（单位：分钟）

        :return: The event_validity_period of this NodeReqDetail.
        :rtype: int
        """
        return self._event_validity_period

    @event_validity_period.setter
    def event_validity_period(self, event_validity_period):
        """Sets the event_validity_period of this NodeReqDetail.

        事件有效时间（单位：分钟）

        :param event_validity_period: The event_validity_period of this NodeReqDetail.
        :type event_validity_period: int
        """
        self._event_validity_period = event_validity_period

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
        if not isinstance(other, NodeReqDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
