# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'enable_gpu': 'bool',
        'log_configs': 'list[LogConfigs]',
        'device_infos': 'list[DeviceInfos]',
        'enable_npu': 'bool',
        'npu_type': 'str',
        'attributes': 'list[Attributes]',
        'enable_docker': 'bool',
        'tags': 'list[NodeResTag]',
        'mqtt_config': 'MqttConfigs'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enable_gpu': 'enable_gpu',
        'log_configs': 'log_configs',
        'device_infos': 'device_infos',
        'enable_npu': 'enable_npu',
        'npu_type': 'npu_type',
        'attributes': 'attributes',
        'enable_docker': 'enable_docker',
        'tags': 'tags',
        'mqtt_config': 'mqtt_config'
    }

    def __init__(self, name=None, description=None, enable_gpu=None, log_configs=None, device_infos=None, enable_npu=None, npu_type=None, attributes=None, enable_docker=None, tags=None, mqtt_config=None):
        """EdgeNode

        The model defined in huaweicloud sdk

        :param name: 边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本帐号中唯一。
        :type name: str
        :param description: 边缘节点描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param enable_gpu: 边缘节点是否开启GPU，默认为false
        :type enable_gpu: bool
        :param log_configs: 边缘节点日志配置
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        :param device_infos: 关联设备信息
        :type device_infos: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        :param enable_npu: 边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false
        :type enable_npu: bool
        :param npu_type: NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。
        :type npu_type: str
        :param attributes: 边缘节点属性，关联属性个数最多为32个
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param enable_docker: 边缘节点启用Docker，默认为true
        :type enable_docker: bool
        :param tags: 边缘节点标签，标签个数最多为20个
        :type tags: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
        :param mqtt_config: 
        :type mqtt_config: :class:`huaweicloudsdkief.v1.MqttConfigs`
        """
        
        

        self._name = None
        self._description = None
        self._enable_gpu = None
        self._log_configs = None
        self._device_infos = None
        self._enable_npu = None
        self._npu_type = None
        self._attributes = None
        self._enable_docker = None
        self._tags = None
        self._mqtt_config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enable_gpu is not None:
            self.enable_gpu = enable_gpu
        if log_configs is not None:
            self.log_configs = log_configs
        if device_infos is not None:
            self.device_infos = device_infos
        if enable_npu is not None:
            self.enable_npu = enable_npu
        if npu_type is not None:
            self.npu_type = npu_type
        if attributes is not None:
            self.attributes = attributes
        if enable_docker is not None:
            self.enable_docker = enable_docker
        if tags is not None:
            self.tags = tags
        if mqtt_config is not None:
            self.mqtt_config = mqtt_config

    @property
    def name(self):
        """Gets the name of this EdgeNode.

        边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本帐号中唯一。

        :return: The name of this EdgeNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeNode.

        边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本帐号中唯一。

        :param name: The name of this EdgeNode.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EdgeNode.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgeNode.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeNode.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgeNode.
        :type description: str
        """
        self._description = description

    @property
    def enable_gpu(self):
        """Gets the enable_gpu of this EdgeNode.

        边缘节点是否开启GPU，默认为false

        :return: The enable_gpu of this EdgeNode.
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        """Sets the enable_gpu of this EdgeNode.

        边缘节点是否开启GPU，默认为false

        :param enable_gpu: The enable_gpu of this EdgeNode.
        :type enable_gpu: bool
        """
        self._enable_gpu = enable_gpu

    @property
    def log_configs(self):
        """Gets the log_configs of this EdgeNode.

        边缘节点日志配置

        :return: The log_configs of this EdgeNode.
        :rtype: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this EdgeNode.

        边缘节点日志配置

        :param log_configs: The log_configs of this EdgeNode.
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        self._log_configs = log_configs

    @property
    def device_infos(self):
        """Gets the device_infos of this EdgeNode.

        关联设备信息

        :return: The device_infos of this EdgeNode.
        :rtype: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        """
        return self._device_infos

    @device_infos.setter
    def device_infos(self, device_infos):
        """Sets the device_infos of this EdgeNode.

        关联设备信息

        :param device_infos: The device_infos of this EdgeNode.
        :type device_infos: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        """
        self._device_infos = device_infos

    @property
    def enable_npu(self):
        """Gets the enable_npu of this EdgeNode.

        边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false

        :return: The enable_npu of this EdgeNode.
        :rtype: bool
        """
        return self._enable_npu

    @enable_npu.setter
    def enable_npu(self, enable_npu):
        """Sets the enable_npu of this EdgeNode.

        边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false

        :param enable_npu: The enable_npu of this EdgeNode.
        :type enable_npu: bool
        """
        self._enable_npu = enable_npu

    @property
    def npu_type(self):
        """Gets the npu_type of this EdgeNode.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :return: The npu_type of this EdgeNode.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        """Sets the npu_type of this EdgeNode.

        NPU类型，支持D310类型和D910类型。 - D310表示D310类型。 - D910表示D910类型。 - 不填表示为D310类型。

        :param npu_type: The npu_type of this EdgeNode.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def attributes(self):
        """Gets the attributes of this EdgeNode.

        边缘节点属性，关联属性个数最多为32个

        :return: The attributes of this EdgeNode.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EdgeNode.

        边缘节点属性，关联属性个数最多为32个

        :param attributes: The attributes of this EdgeNode.
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._attributes = attributes

    @property
    def enable_docker(self):
        """Gets the enable_docker of this EdgeNode.

        边缘节点启用Docker，默认为true

        :return: The enable_docker of this EdgeNode.
        :rtype: bool
        """
        return self._enable_docker

    @enable_docker.setter
    def enable_docker(self, enable_docker):
        """Sets the enable_docker of this EdgeNode.

        边缘节点启用Docker，默认为true

        :param enable_docker: The enable_docker of this EdgeNode.
        :type enable_docker: bool
        """
        self._enable_docker = enable_docker

    @property
    def tags(self):
        """Gets the tags of this EdgeNode.

        边缘节点标签，标签个数最多为20个

        :return: The tags of this EdgeNode.
        :rtype: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EdgeNode.

        边缘节点标签，标签个数最多为20个

        :param tags: The tags of this EdgeNode.
        :type tags: list[:class:`huaweicloudsdkief.v1.NodeResTag`]
        """
        self._tags = tags

    @property
    def mqtt_config(self):
        """Gets the mqtt_config of this EdgeNode.

        :return: The mqtt_config of this EdgeNode.
        :rtype: :class:`huaweicloudsdkief.v1.MqttConfigs`
        """
        return self._mqtt_config

    @mqtt_config.setter
    def mqtt_config(self, mqtt_config):
        """Sets the mqtt_config of this EdgeNode.

        :param mqtt_config: The mqtt_config of this EdgeNode.
        :type mqtt_config: :class:`huaweicloudsdkief.v1.MqttConfigs`
        """
        self._mqtt_config = mqtt_config

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
        if not isinstance(other, EdgeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
