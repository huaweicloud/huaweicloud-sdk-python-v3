# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSummaryUsageDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'user_id': 'str',
        'resource_type': 'str',
        'business_type': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'user_id': 'user_id',
        'resource_type': 'resource_type',
        'business_type': 'business_type',
        'unit': 'unit'
    }

    def __init__(self, x_app_user_id=None, user_id=None, resource_type=None, business_type=None, unit=None):
        r"""ShowSummaryUsageDataRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param user_id: 用户id(仅开启了子账号隔离功能的主账号携带才生效)
        :type user_id: str
        :param resource_type: 资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版
        :type resource_type: str
        :param business_type: 业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作
        :type business_type: str
        :param unit: 使用量的单位。 * MIN：分钟 * HOUR：小时
        :type unit: str
        """
        
        

        self._x_app_user_id = None
        self._user_id = None
        self._resource_type = None
        self._business_type = None
        self._unit = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if user_id is not None:
            self.user_id = user_id
        if resource_type is not None:
            self.resource_type = resource_type
        if business_type is not None:
            self.business_type = business_type
        if unit is not None:
            self.unit = unit

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ShowSummaryUsageDataRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ShowSummaryUsageDataRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ShowSummaryUsageDataRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ShowSummaryUsageDataRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowSummaryUsageDataRequest.

        用户id(仅开启了子账号隔离功能的主账号携带才生效)

        :return: The user_id of this ShowSummaryUsageDataRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowSummaryUsageDataRequest.

        用户id(仅开启了子账号隔离功能的主账号携带才生效)

        :param user_id: The user_id of this ShowSummaryUsageDataRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowSummaryUsageDataRequest.

        资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版

        :return: The resource_type of this ShowSummaryUsageDataRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowSummaryUsageDataRequest.

        资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版

        :param resource_type: The resource_type of this ShowSummaryUsageDataRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def business_type(self):
        r"""Gets the business_type of this ShowSummaryUsageDataRequest.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :return: The business_type of this ShowSummaryUsageDataRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ShowSummaryUsageDataRequest.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :param business_type: The business_type of this ShowSummaryUsageDataRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def unit(self):
        r"""Gets the unit of this ShowSummaryUsageDataRequest.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :return: The unit of this ShowSummaryUsageDataRequest.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ShowSummaryUsageDataRequest.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :param unit: The unit of this ShowSummaryUsageDataRequest.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ShowSummaryUsageDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
