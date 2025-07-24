# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerHardwareAttributesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'summary': 'HardwareSummary',
        'memorys': 'list[Memory]',
        'processors': 'list[Processors]',
        'network_adapters': 'list[NetworkAdapter]',
        'fans': 'list[Fan]',
        'powers': 'list[Power]',
        'storage_controllers': 'list[StorageController]'
    }

    attribute_map = {
        'summary': 'summary',
        'memorys': 'memorys',
        'processors': 'processors',
        'network_adapters': 'network_adapters',
        'fans': 'fans',
        'powers': 'powers',
        'storage_controllers': 'storage_controllers'
    }

    def __init__(self, summary=None, memorys=None, processors=None, network_adapters=None, fans=None, powers=None, storage_controllers=None):
        r"""ShowServerHardwareAttributesResponse

        The model defined in huaweicloud sdk

        :param summary: 
        :type summary: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        :param memorys: 内存列表
        :type memorys: list[:class:`huaweicloudsdkclouddc.v1.Memory`]
        :param processors: cpu列表
        :type processors: list[:class:`huaweicloudsdkclouddc.v1.Processors`]
        :param network_adapters: 网络适配器详细信息
        :type network_adapters: list[:class:`huaweicloudsdkclouddc.v1.NetworkAdapter`]
        :param fans: 风扇列表
        :type fans: list[:class:`huaweicloudsdkclouddc.v1.Fan`]
        :param powers: 电源列表
        :type powers: list[:class:`huaweicloudsdkclouddc.v1.Power`]
        :param storage_controllers: 存储控制器列表
        :type storage_controllers: list[:class:`huaweicloudsdkclouddc.v1.StorageController`]
        """
        
        super(ShowServerHardwareAttributesResponse, self).__init__()

        self._summary = None
        self._memorys = None
        self._processors = None
        self._network_adapters = None
        self._fans = None
        self._powers = None
        self._storage_controllers = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if memorys is not None:
            self.memorys = memorys
        if processors is not None:
            self.processors = processors
        if network_adapters is not None:
            self.network_adapters = network_adapters
        if fans is not None:
            self.fans = fans
        if powers is not None:
            self.powers = powers
        if storage_controllers is not None:
            self.storage_controllers = storage_controllers

    @property
    def summary(self):
        r"""Gets the summary of this ShowServerHardwareAttributesResponse.

        :return: The summary of this ShowServerHardwareAttributesResponse.
        :rtype: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ShowServerHardwareAttributesResponse.

        :param summary: The summary of this ShowServerHardwareAttributesResponse.
        :type summary: :class:`huaweicloudsdkclouddc.v1.HardwareSummary`
        """
        self._summary = summary

    @property
    def memorys(self):
        r"""Gets the memorys of this ShowServerHardwareAttributesResponse.

        内存列表

        :return: The memorys of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Memory`]
        """
        return self._memorys

    @memorys.setter
    def memorys(self, memorys):
        r"""Sets the memorys of this ShowServerHardwareAttributesResponse.

        内存列表

        :param memorys: The memorys of this ShowServerHardwareAttributesResponse.
        :type memorys: list[:class:`huaweicloudsdkclouddc.v1.Memory`]
        """
        self._memorys = memorys

    @property
    def processors(self):
        r"""Gets the processors of this ShowServerHardwareAttributesResponse.

        cpu列表

        :return: The processors of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Processors`]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        r"""Sets the processors of this ShowServerHardwareAttributesResponse.

        cpu列表

        :param processors: The processors of this ShowServerHardwareAttributesResponse.
        :type processors: list[:class:`huaweicloudsdkclouddc.v1.Processors`]
        """
        self._processors = processors

    @property
    def network_adapters(self):
        r"""Gets the network_adapters of this ShowServerHardwareAttributesResponse.

        网络适配器详细信息

        :return: The network_adapters of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.NetworkAdapter`]
        """
        return self._network_adapters

    @network_adapters.setter
    def network_adapters(self, network_adapters):
        r"""Sets the network_adapters of this ShowServerHardwareAttributesResponse.

        网络适配器详细信息

        :param network_adapters: The network_adapters of this ShowServerHardwareAttributesResponse.
        :type network_adapters: list[:class:`huaweicloudsdkclouddc.v1.NetworkAdapter`]
        """
        self._network_adapters = network_adapters

    @property
    def fans(self):
        r"""Gets the fans of this ShowServerHardwareAttributesResponse.

        风扇列表

        :return: The fans of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Fan`]
        """
        return self._fans

    @fans.setter
    def fans(self, fans):
        r"""Sets the fans of this ShowServerHardwareAttributesResponse.

        风扇列表

        :param fans: The fans of this ShowServerHardwareAttributesResponse.
        :type fans: list[:class:`huaweicloudsdkclouddc.v1.Fan`]
        """
        self._fans = fans

    @property
    def powers(self):
        r"""Gets the powers of this ShowServerHardwareAttributesResponse.

        电源列表

        :return: The powers of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Power`]
        """
        return self._powers

    @powers.setter
    def powers(self, powers):
        r"""Sets the powers of this ShowServerHardwareAttributesResponse.

        电源列表

        :param powers: The powers of this ShowServerHardwareAttributesResponse.
        :type powers: list[:class:`huaweicloudsdkclouddc.v1.Power`]
        """
        self._powers = powers

    @property
    def storage_controllers(self):
        r"""Gets the storage_controllers of this ShowServerHardwareAttributesResponse.

        存储控制器列表

        :return: The storage_controllers of this ShowServerHardwareAttributesResponse.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.StorageController`]
        """
        return self._storage_controllers

    @storage_controllers.setter
    def storage_controllers(self, storage_controllers):
        r"""Sets the storage_controllers of this ShowServerHardwareAttributesResponse.

        存储控制器列表

        :param storage_controllers: The storage_controllers of this ShowServerHardwareAttributesResponse.
        :type storage_controllers: list[:class:`huaweicloudsdkclouddc.v1.StorageController`]
        """
        self._storage_controllers = storage_controllers

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
        if not isinstance(other, ShowServerHardwareAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
