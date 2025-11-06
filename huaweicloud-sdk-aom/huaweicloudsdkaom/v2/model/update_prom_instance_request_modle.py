# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePromInstanceRequestModle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prom_id': 'str',
        'prom_limits': 'PromLimits',
        'prom_name': 'str',
        'aggr_prometheus_info': 'list[AggrPrometheusInfo]'
    }

    attribute_map = {
        'prom_id': 'prom_id',
        'prom_limits': 'prom_limits',
        'prom_name': 'prom_name',
        'aggr_prometheus_info': 'aggr_prometheus_info'
    }

    def __init__(self, prom_id=None, prom_limits=None, prom_name=None, aggr_prometheus_info=None):
        r"""UpdatePromInstanceRequestModle

        The model defined in huaweicloud sdk

        :param prom_id: 待修改的普罗实例id。
        :type prom_id: str
        :param prom_limits: 
        :type prom_limits: :class:`huaweicloudsdkaom.v2.PromLimits`
        :param prom_name: 待修改的普罗实例名称，名称不能以下划线或中划线开头和结尾，只含有中文，英文，数字，下划线，中划线，长度1-100。
        :type prom_name: str
        :param aggr_prometheus_info: 被聚合的账号和普罗实例列表。
        :type aggr_prometheus_info: list[:class:`huaweicloudsdkaom.v2.AggrPrometheusInfo`]
        """
        
        

        self._prom_id = None
        self._prom_limits = None
        self._prom_name = None
        self._aggr_prometheus_info = None
        self.discriminator = None

        self.prom_id = prom_id
        if prom_limits is not None:
            self.prom_limits = prom_limits
        if prom_name is not None:
            self.prom_name = prom_name
        if aggr_prometheus_info is not None:
            self.aggr_prometheus_info = aggr_prometheus_info

    @property
    def prom_id(self):
        r"""Gets the prom_id of this UpdatePromInstanceRequestModle.

        待修改的普罗实例id。

        :return: The prom_id of this UpdatePromInstanceRequestModle.
        :rtype: str
        """
        return self._prom_id

    @prom_id.setter
    def prom_id(self, prom_id):
        r"""Sets the prom_id of this UpdatePromInstanceRequestModle.

        待修改的普罗实例id。

        :param prom_id: The prom_id of this UpdatePromInstanceRequestModle.
        :type prom_id: str
        """
        self._prom_id = prom_id

    @property
    def prom_limits(self):
        r"""Gets the prom_limits of this UpdatePromInstanceRequestModle.

        :return: The prom_limits of this UpdatePromInstanceRequestModle.
        :rtype: :class:`huaweicloudsdkaom.v2.PromLimits`
        """
        return self._prom_limits

    @prom_limits.setter
    def prom_limits(self, prom_limits):
        r"""Sets the prom_limits of this UpdatePromInstanceRequestModle.

        :param prom_limits: The prom_limits of this UpdatePromInstanceRequestModle.
        :type prom_limits: :class:`huaweicloudsdkaom.v2.PromLimits`
        """
        self._prom_limits = prom_limits

    @property
    def prom_name(self):
        r"""Gets the prom_name of this UpdatePromInstanceRequestModle.

        待修改的普罗实例名称，名称不能以下划线或中划线开头和结尾，只含有中文，英文，数字，下划线，中划线，长度1-100。

        :return: The prom_name of this UpdatePromInstanceRequestModle.
        :rtype: str
        """
        return self._prom_name

    @prom_name.setter
    def prom_name(self, prom_name):
        r"""Sets the prom_name of this UpdatePromInstanceRequestModle.

        待修改的普罗实例名称，名称不能以下划线或中划线开头和结尾，只含有中文，英文，数字，下划线，中划线，长度1-100。

        :param prom_name: The prom_name of this UpdatePromInstanceRequestModle.
        :type prom_name: str
        """
        self._prom_name = prom_name

    @property
    def aggr_prometheus_info(self):
        r"""Gets the aggr_prometheus_info of this UpdatePromInstanceRequestModle.

        被聚合的账号和普罗实例列表。

        :return: The aggr_prometheus_info of this UpdatePromInstanceRequestModle.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AggrPrometheusInfo`]
        """
        return self._aggr_prometheus_info

    @aggr_prometheus_info.setter
    def aggr_prometheus_info(self, aggr_prometheus_info):
        r"""Sets the aggr_prometheus_info of this UpdatePromInstanceRequestModle.

        被聚合的账号和普罗实例列表。

        :param aggr_prometheus_info: The aggr_prometheus_info of this UpdatePromInstanceRequestModle.
        :type aggr_prometheus_info: list[:class:`huaweicloudsdkaom.v2.AggrPrometheusInfo`]
        """
        self._aggr_prometheus_info = aggr_prometheus_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePromInstanceRequestModle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
