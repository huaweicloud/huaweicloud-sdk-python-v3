# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSummaryUsageDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'business_type': 'str',
        'number': 'int',
        'usage': 'float',
        'unit': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'business_type': 'business_type',
        'number': 'number',
        'usage': 'usage',
        'unit': 'unit',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, resource_type=None, business_type=None, number=None, usage=None, unit=None, x_request_id=None):
        r"""ShowSummaryUsageDataResponse

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param business_type: 业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作
        :type business_type: str
        :param number: 使用个数(视频制作的视频个数,直播的场次)
        :type number: int
        :param usage: 使用量
        :type usage: float
        :param unit: 使用量的单位。 * MIN：分钟 * HOUR：小时
        :type unit: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._resource_type = None
        self._business_type = None
        self._number = None
        self._usage = None
        self._unit = None
        self._x_request_id = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if business_type is not None:
            self.business_type = business_type
        if number is not None:
            self.number = number
        if usage is not None:
            self.usage = usage
        if unit is not None:
            self.unit = unit
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowSummaryUsageDataResponse.

        资源类型

        :return: The resource_type of this ShowSummaryUsageDataResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowSummaryUsageDataResponse.

        资源类型

        :param resource_type: The resource_type of this ShowSummaryUsageDataResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def business_type(self):
        r"""Gets the business_type of this ShowSummaryUsageDataResponse.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :return: The business_type of this ShowSummaryUsageDataResponse.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ShowSummaryUsageDataResponse.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :param business_type: The business_type of this ShowSummaryUsageDataResponse.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def number(self):
        r"""Gets the number of this ShowSummaryUsageDataResponse.

        使用个数(视频制作的视频个数,直播的场次)

        :return: The number of this ShowSummaryUsageDataResponse.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ShowSummaryUsageDataResponse.

        使用个数(视频制作的视频个数,直播的场次)

        :param number: The number of this ShowSummaryUsageDataResponse.
        :type number: int
        """
        self._number = number

    @property
    def usage(self):
        r"""Gets the usage of this ShowSummaryUsageDataResponse.

        使用量

        :return: The usage of this ShowSummaryUsageDataResponse.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ShowSummaryUsageDataResponse.

        使用量

        :param usage: The usage of this ShowSummaryUsageDataResponse.
        :type usage: float
        """
        self._usage = usage

    @property
    def unit(self):
        r"""Gets the unit of this ShowSummaryUsageDataResponse.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :return: The unit of this ShowSummaryUsageDataResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ShowSummaryUsageDataResponse.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :param unit: The unit of this ShowSummaryUsageDataResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSummaryUsageDataResponse.

        :return: The x_request_id of this ShowSummaryUsageDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSummaryUsageDataResponse.

        :param x_request_id: The x_request_id of this ShowSummaryUsageDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowSummaryUsageDataResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowSummaryUsageDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
