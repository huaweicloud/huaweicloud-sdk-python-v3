# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert': 'bool',
        'allow_alert': 'bool',
        'allow_lts': 'bool',
        'csvc_display': 'str',
        'datasets': 'list[DatasetInfo]',
        'region': 'bool',
        'source_display': 'str',
        'success': 'bool',
        'total': 'int'
    }

    attribute_map = {
        'alert': 'alert',
        'allow_alert': 'allow_alert',
        'allow_lts': 'allow_lts',
        'csvc_display': 'csvc_display',
        'datasets': 'datasets',
        'region': 'region',
        'source_display': 'source_display',
        'success': 'success',
        'total': 'total'
    }

    def __init__(self, alert=None, allow_alert=None, allow_lts=None, csvc_display=None, datasets=None, region=None, source_display=None, success=None, total=None):
        r"""ConfigResponse

        The model defined in huaweicloud sdk

        :param alert: 自动转告警的开关
        :type alert: bool
        :param allow_alert: 能否开自动转告警
        :type allow_alert: bool
        :param allow_lts: 是否允许长期存储
        :type allow_lts: bool
        :param csvc_display: 云服务描述
        :type csvc_display: str
        :param datasets: 关联的数据集列表
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        :param region: 是否按区域分片采集
        :type region: bool
        :param source_display: 数据源描述
        :type source_display: str
        :param success: 是否创建成功
        :type success: bool
        :param total: 当前已采集的日志条数
        :type total: int
        """
        
        

        self._alert = None
        self._allow_alert = None
        self._allow_lts = None
        self._csvc_display = None
        self._datasets = None
        self._region = None
        self._source_display = None
        self._success = None
        self._total = None
        self.discriminator = None

        if alert is not None:
            self.alert = alert
        if allow_alert is not None:
            self.allow_alert = allow_alert
        if allow_lts is not None:
            self.allow_lts = allow_lts
        if csvc_display is not None:
            self.csvc_display = csvc_display
        if datasets is not None:
            self.datasets = datasets
        if region is not None:
            self.region = region
        if source_display is not None:
            self.source_display = source_display
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total

    @property
    def alert(self):
        r"""Gets the alert of this ConfigResponse.

        自动转告警的开关

        :return: The alert of this ConfigResponse.
        :rtype: bool
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        r"""Sets the alert of this ConfigResponse.

        自动转告警的开关

        :param alert: The alert of this ConfigResponse.
        :type alert: bool
        """
        self._alert = alert

    @property
    def allow_alert(self):
        r"""Gets the allow_alert of this ConfigResponse.

        能否开自动转告警

        :return: The allow_alert of this ConfigResponse.
        :rtype: bool
        """
        return self._allow_alert

    @allow_alert.setter
    def allow_alert(self, allow_alert):
        r"""Sets the allow_alert of this ConfigResponse.

        能否开自动转告警

        :param allow_alert: The allow_alert of this ConfigResponse.
        :type allow_alert: bool
        """
        self._allow_alert = allow_alert

    @property
    def allow_lts(self):
        r"""Gets the allow_lts of this ConfigResponse.

        是否允许长期存储

        :return: The allow_lts of this ConfigResponse.
        :rtype: bool
        """
        return self._allow_lts

    @allow_lts.setter
    def allow_lts(self, allow_lts):
        r"""Sets the allow_lts of this ConfigResponse.

        是否允许长期存储

        :param allow_lts: The allow_lts of this ConfigResponse.
        :type allow_lts: bool
        """
        self._allow_lts = allow_lts

    @property
    def csvc_display(self):
        r"""Gets the csvc_display of this ConfigResponse.

        云服务描述

        :return: The csvc_display of this ConfigResponse.
        :rtype: str
        """
        return self._csvc_display

    @csvc_display.setter
    def csvc_display(self, csvc_display):
        r"""Sets the csvc_display of this ConfigResponse.

        云服务描述

        :param csvc_display: The csvc_display of this ConfigResponse.
        :type csvc_display: str
        """
        self._csvc_display = csvc_display

    @property
    def datasets(self):
        r"""Gets the datasets of this ConfigResponse.

        关联的数据集列表

        :return: The datasets of this ConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        r"""Sets the datasets of this ConfigResponse.

        关联的数据集列表

        :param datasets: The datasets of this ConfigResponse.
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetInfo`]
        """
        self._datasets = datasets

    @property
    def region(self):
        r"""Gets the region of this ConfigResponse.

        是否按区域分片采集

        :return: The region of this ConfigResponse.
        :rtype: bool
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ConfigResponse.

        是否按区域分片采集

        :param region: The region of this ConfigResponse.
        :type region: bool
        """
        self._region = region

    @property
    def source_display(self):
        r"""Gets the source_display of this ConfigResponse.

        数据源描述

        :return: The source_display of this ConfigResponse.
        :rtype: str
        """
        return self._source_display

    @source_display.setter
    def source_display(self, source_display):
        r"""Sets the source_display of this ConfigResponse.

        数据源描述

        :param source_display: The source_display of this ConfigResponse.
        :type source_display: str
        """
        self._source_display = source_display

    @property
    def success(self):
        r"""Gets the success of this ConfigResponse.

        是否创建成功

        :return: The success of this ConfigResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ConfigResponse.

        是否创建成功

        :param success: The success of this ConfigResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this ConfigResponse.

        当前已采集的日志条数

        :return: The total of this ConfigResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ConfigResponse.

        当前已采集的日志条数

        :param total: The total of this ConfigResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
