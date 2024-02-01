# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size_range': 'list[GlobalConnectionBandwidthSizeRange]',
        'charge_mode': 'list[str]',
        'services': 'list[str]',
        'gcb_type': 'list[str]',
        'ratio_95peak_guar': 'int',
        'crossborder': 'bool',
        'quotas': 'list[GlobalConnectionBandwidthQuotas]',
        'sla_level': 'list[str]',
        'bind_limit': 'int'
    }

    attribute_map = {
        'size_range': 'size_range',
        'charge_mode': 'charge_mode',
        'services': 'services',
        'gcb_type': 'gcb_type',
        'ratio_95peak_guar': 'ratio_95peak_guar',
        'crossborder': 'crossborder',
        'quotas': 'quotas',
        'sla_level': 'sla_level',
        'bind_limit': 'bind_limit'
    }

    def __init__(self, size_range=None, charge_mode=None, services=None, gcb_type=None, ratio_95peak_guar=None, crossborder=None, quotas=None, sla_level=None, bind_limit=None):
        """ListGlobalConnectionBandwidthConfigs

        The model defined in huaweicloud sdk

        :param size_range: 计费类型对应全域互联带宽大小范围。
        :type size_range: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSizeRange`]
        :param charge_mode: 支持的计费类型列表。
        :type charge_mode: list[str]
        :param services: 支持服务实例类型。
        :type services: list[str]
        :param gcb_type: 支持的带宽类型。
        :type gcb_type: list[str]
        :param ratio_95peak_guar: 按传统型95计费保底消费百分比。
        :type ratio_95peak_guar: int
        :param crossborder: 是否已经完成跨境审批。
        :type crossborder: bool
        :param quotas: 配额信息。
        :type quotas: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthQuotas`]
        :param sla_level: 支持线路分级。
        :type sla_level: list[str]
        :param bind_limit: 共享带宽允许绑定实例数量上限。
        :type bind_limit: int
        """
        
        

        self._size_range = None
        self._charge_mode = None
        self._services = None
        self._gcb_type = None
        self._ratio_95peak_guar = None
        self._crossborder = None
        self._quotas = None
        self._sla_level = None
        self._bind_limit = None
        self.discriminator = None

        self.size_range = size_range
        self.charge_mode = charge_mode
        self.services = services
        self.gcb_type = gcb_type
        if ratio_95peak_guar is not None:
            self.ratio_95peak_guar = ratio_95peak_guar
        self.crossborder = crossborder
        self.quotas = quotas
        self.sla_level = sla_level
        self.bind_limit = bind_limit

    @property
    def size_range(self):
        """Gets the size_range of this ListGlobalConnectionBandwidthConfigs.

        计费类型对应全域互联带宽大小范围。

        :return: The size_range of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSizeRange`]
        """
        return self._size_range

    @size_range.setter
    def size_range(self, size_range):
        """Sets the size_range of this ListGlobalConnectionBandwidthConfigs.

        计费类型对应全域互联带宽大小范围。

        :param size_range: The size_range of this ListGlobalConnectionBandwidthConfigs.
        :type size_range: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthSizeRange`]
        """
        self._size_range = size_range

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListGlobalConnectionBandwidthConfigs.

        支持的计费类型列表。

        :return: The charge_mode of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[str]
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListGlobalConnectionBandwidthConfigs.

        支持的计费类型列表。

        :param charge_mode: The charge_mode of this ListGlobalConnectionBandwidthConfigs.
        :type charge_mode: list[str]
        """
        self._charge_mode = charge_mode

    @property
    def services(self):
        """Gets the services of this ListGlobalConnectionBandwidthConfigs.

        支持服务实例类型。

        :return: The services of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ListGlobalConnectionBandwidthConfigs.

        支持服务实例类型。

        :param services: The services of this ListGlobalConnectionBandwidthConfigs.
        :type services: list[str]
        """
        self._services = services

    @property
    def gcb_type(self):
        """Gets the gcb_type of this ListGlobalConnectionBandwidthConfigs.

        支持的带宽类型。

        :return: The gcb_type of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[str]
        """
        return self._gcb_type

    @gcb_type.setter
    def gcb_type(self, gcb_type):
        """Sets the gcb_type of this ListGlobalConnectionBandwidthConfigs.

        支持的带宽类型。

        :param gcb_type: The gcb_type of this ListGlobalConnectionBandwidthConfigs.
        :type gcb_type: list[str]
        """
        self._gcb_type = gcb_type

    @property
    def ratio_95peak_guar(self):
        """Gets the ratio_95peak_guar of this ListGlobalConnectionBandwidthConfigs.

        按传统型95计费保底消费百分比。

        :return: The ratio_95peak_guar of this ListGlobalConnectionBandwidthConfigs.
        :rtype: int
        """
        return self._ratio_95peak_guar

    @ratio_95peak_guar.setter
    def ratio_95peak_guar(self, ratio_95peak_guar):
        """Sets the ratio_95peak_guar of this ListGlobalConnectionBandwidthConfigs.

        按传统型95计费保底消费百分比。

        :param ratio_95peak_guar: The ratio_95peak_guar of this ListGlobalConnectionBandwidthConfigs.
        :type ratio_95peak_guar: int
        """
        self._ratio_95peak_guar = ratio_95peak_guar

    @property
    def crossborder(self):
        """Gets the crossborder of this ListGlobalConnectionBandwidthConfigs.

        是否已经完成跨境审批。

        :return: The crossborder of this ListGlobalConnectionBandwidthConfigs.
        :rtype: bool
        """
        return self._crossborder

    @crossborder.setter
    def crossborder(self, crossborder):
        """Sets the crossborder of this ListGlobalConnectionBandwidthConfigs.

        是否已经完成跨境审批。

        :param crossborder: The crossborder of this ListGlobalConnectionBandwidthConfigs.
        :type crossborder: bool
        """
        self._crossborder = crossborder

    @property
    def quotas(self):
        """Gets the quotas of this ListGlobalConnectionBandwidthConfigs.

        配额信息。

        :return: The quotas of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthQuotas`]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this ListGlobalConnectionBandwidthConfigs.

        配额信息。

        :param quotas: The quotas of this ListGlobalConnectionBandwidthConfigs.
        :type quotas: list[:class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidthQuotas`]
        """
        self._quotas = quotas

    @property
    def sla_level(self):
        """Gets the sla_level of this ListGlobalConnectionBandwidthConfigs.

        支持线路分级。

        :return: The sla_level of this ListGlobalConnectionBandwidthConfigs.
        :rtype: list[str]
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        """Sets the sla_level of this ListGlobalConnectionBandwidthConfigs.

        支持线路分级。

        :param sla_level: The sla_level of this ListGlobalConnectionBandwidthConfigs.
        :type sla_level: list[str]
        """
        self._sla_level = sla_level

    @property
    def bind_limit(self):
        """Gets the bind_limit of this ListGlobalConnectionBandwidthConfigs.

        共享带宽允许绑定实例数量上限。

        :return: The bind_limit of this ListGlobalConnectionBandwidthConfigs.
        :rtype: int
        """
        return self._bind_limit

    @bind_limit.setter
    def bind_limit(self, bind_limit):
        """Sets the bind_limit of this ListGlobalConnectionBandwidthConfigs.

        共享带宽允许绑定实例数量上限。

        :param bind_limit: The bind_limit of this ListGlobalConnectionBandwidthConfigs.
        :type bind_limit: int
        """
        self._bind_limit = bind_limit

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
        if not isinstance(other, ListGlobalConnectionBandwidthConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
