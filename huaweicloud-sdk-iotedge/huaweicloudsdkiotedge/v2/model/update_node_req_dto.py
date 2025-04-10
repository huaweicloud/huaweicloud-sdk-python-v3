# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeReqDTO:

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
        'storage_period': 'int',
        'log_configs': 'list[LogConfigDTO]',
        'ha_config': 'HaConfigDTO',
        'hardware_model': 'str',
        'npu_library_path': 'str',
        'automatic_upgrade': 'str',
        'device_data_record': 'DeviceDataRecord',
        'metric_report': 'str',
        'offline_cache_configs': 'UpdateOfflineCacheConfigsDTO'
    }

    attribute_map = {
        'name': 'name',
        'storage_period': 'storage_period',
        'log_configs': 'log_configs',
        'ha_config': 'ha_config',
        'hardware_model': 'hardware_model',
        'npu_library_path': 'npu_library_path',
        'automatic_upgrade': 'automatic_upgrade',
        'device_data_record': 'device_data_record',
        'metric_report': 'metric_report',
        'offline_cache_configs': 'offline_cache_configs'
    }

    def __init__(self, name=None, storage_period=None, log_configs=None, ha_config=None, hardware_model=None, npu_library_path=None, automatic_upgrade=None, device_data_record=None, metric_report=None, offline_cache_configs=None):
        r"""UpdateNodeReqDTO

        The model defined in huaweicloud sdk

        :param name: 边缘节点名称，只允许中、数字、英文大小写、中划线、下划线
        :type name: str
        :param storage_period: 节点的存储周期，默认0天，取值范围0~7天，0天则不存储。
        :type storage_period: int
        :param log_configs: 边缘节点在IEF日志配置参数
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        :param ha_config: 
        :type ha_config: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        :param hardware_model: 网关型号
        :type hardware_model: str
        :param npu_library_path: npu驱动动态库路径
        :type npu_library_path: str
        :param automatic_upgrade: 自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开
        :type automatic_upgrade: str
        :param device_data_record: 
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        :param metric_report: omagent监控运维工具是否上报指标
        :type metric_report: str
        :param offline_cache_configs: 
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.UpdateOfflineCacheConfigsDTO`
        """
        
        

        self._name = None
        self._storage_period = None
        self._log_configs = None
        self._ha_config = None
        self._hardware_model = None
        self._npu_library_path = None
        self._automatic_upgrade = None
        self._device_data_record = None
        self._metric_report = None
        self._offline_cache_configs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if storage_period is not None:
            self.storage_period = storage_period
        if log_configs is not None:
            self.log_configs = log_configs
        if ha_config is not None:
            self.ha_config = ha_config
        if hardware_model is not None:
            self.hardware_model = hardware_model
        if npu_library_path is not None:
            self.npu_library_path = npu_library_path
        if automatic_upgrade is not None:
            self.automatic_upgrade = automatic_upgrade
        if device_data_record is not None:
            self.device_data_record = device_data_record
        if metric_report is not None:
            self.metric_report = metric_report
        if offline_cache_configs is not None:
            self.offline_cache_configs = offline_cache_configs

    @property
    def name(self):
        r"""Gets the name of this UpdateNodeReqDTO.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :return: The name of this UpdateNodeReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateNodeReqDTO.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :param name: The name of this UpdateNodeReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def storage_period(self):
        r"""Gets the storage_period of this UpdateNodeReqDTO.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :return: The storage_period of this UpdateNodeReqDTO.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        r"""Sets the storage_period of this UpdateNodeReqDTO.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :param storage_period: The storage_period of this UpdateNodeReqDTO.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def log_configs(self):
        r"""Gets the log_configs of this UpdateNodeReqDTO.

        边缘节点在IEF日志配置参数

        :return: The log_configs of this UpdateNodeReqDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this UpdateNodeReqDTO.

        边缘节点在IEF日志配置参数

        :param log_configs: The log_configs of this UpdateNodeReqDTO.
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        self._log_configs = log_configs

    @property
    def ha_config(self):
        r"""Gets the ha_config of this UpdateNodeReqDTO.

        :return: The ha_config of this UpdateNodeReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        """
        return self._ha_config

    @ha_config.setter
    def ha_config(self, ha_config):
        r"""Sets the ha_config of this UpdateNodeReqDTO.

        :param ha_config: The ha_config of this UpdateNodeReqDTO.
        :type ha_config: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        """
        self._ha_config = ha_config

    @property
    def hardware_model(self):
        r"""Gets the hardware_model of this UpdateNodeReqDTO.

        网关型号

        :return: The hardware_model of this UpdateNodeReqDTO.
        :rtype: str
        """
        return self._hardware_model

    @hardware_model.setter
    def hardware_model(self, hardware_model):
        r"""Sets the hardware_model of this UpdateNodeReqDTO.

        网关型号

        :param hardware_model: The hardware_model of this UpdateNodeReqDTO.
        :type hardware_model: str
        """
        self._hardware_model = hardware_model

    @property
    def npu_library_path(self):
        r"""Gets the npu_library_path of this UpdateNodeReqDTO.

        npu驱动动态库路径

        :return: The npu_library_path of this UpdateNodeReqDTO.
        :rtype: str
        """
        return self._npu_library_path

    @npu_library_path.setter
    def npu_library_path(self, npu_library_path):
        r"""Sets the npu_library_path of this UpdateNodeReqDTO.

        npu驱动动态库路径

        :param npu_library_path: The npu_library_path of this UpdateNodeReqDTO.
        :type npu_library_path: str
        """
        self._npu_library_path = npu_library_path

    @property
    def automatic_upgrade(self):
        r"""Gets the automatic_upgrade of this UpdateNodeReqDTO.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :return: The automatic_upgrade of this UpdateNodeReqDTO.
        :rtype: str
        """
        return self._automatic_upgrade

    @automatic_upgrade.setter
    def automatic_upgrade(self, automatic_upgrade):
        r"""Sets the automatic_upgrade of this UpdateNodeReqDTO.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :param automatic_upgrade: The automatic_upgrade of this UpdateNodeReqDTO.
        :type automatic_upgrade: str
        """
        self._automatic_upgrade = automatic_upgrade

    @property
    def device_data_record(self):
        r"""Gets the device_data_record of this UpdateNodeReqDTO.

        :return: The device_data_record of this UpdateNodeReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        return self._device_data_record

    @device_data_record.setter
    def device_data_record(self, device_data_record):
        r"""Sets the device_data_record of this UpdateNodeReqDTO.

        :param device_data_record: The device_data_record of this UpdateNodeReqDTO.
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        self._device_data_record = device_data_record

    @property
    def metric_report(self):
        r"""Gets the metric_report of this UpdateNodeReqDTO.

        omagent监控运维工具是否上报指标

        :return: The metric_report of this UpdateNodeReqDTO.
        :rtype: str
        """
        return self._metric_report

    @metric_report.setter
    def metric_report(self, metric_report):
        r"""Sets the metric_report of this UpdateNodeReqDTO.

        omagent监控运维工具是否上报指标

        :param metric_report: The metric_report of this UpdateNodeReqDTO.
        :type metric_report: str
        """
        self._metric_report = metric_report

    @property
    def offline_cache_configs(self):
        r"""Gets the offline_cache_configs of this UpdateNodeReqDTO.

        :return: The offline_cache_configs of this UpdateNodeReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateOfflineCacheConfigsDTO`
        """
        return self._offline_cache_configs

    @offline_cache_configs.setter
    def offline_cache_configs(self, offline_cache_configs):
        r"""Sets the offline_cache_configs of this UpdateNodeReqDTO.

        :param offline_cache_configs: The offline_cache_configs of this UpdateNodeReqDTO.
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.UpdateOfflineCacheConfigsDTO`
        """
        self._offline_cache_configs = offline_cache_configs

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
        if not isinstance(other, UpdateNodeReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
