# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLandingZoneStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployed_version': 'str',
        'landing_zone_status': 'str',
        'percentage_complete': 'int',
        'percentage_details': 'list[PercentageDetail]',
        'landing_zone_action_type': 'str',
        'message': 'list[LandingZoneErrorMessage]',
        'regions': 'list[RegionConfigurationList]'
    }

    attribute_map = {
        'deployed_version': 'deployed_version',
        'landing_zone_status': 'landing_zone_status',
        'percentage_complete': 'percentage_complete',
        'percentage_details': 'percentage_details',
        'landing_zone_action_type': 'landing_zone_action_type',
        'message': 'message',
        'regions': 'regions'
    }

    def __init__(self, deployed_version=None, landing_zone_status=None, percentage_complete=None, percentage_details=None, landing_zone_action_type=None, message=None, regions=None):
        r"""ShowLandingZoneStatusResponse

        The model defined in huaweicloud sdk

        :param deployed_version: 部署的Landing Zone版本。
        :type deployed_version: str
        :param landing_zone_status: Landing Zone的设置状态，包括进行中，已完成。
        :type landing_zone_status: str
        :param percentage_complete: Landing Zone的完成进度。
        :type percentage_complete: int
        :param percentage_details: Landing Zone设置的详细进度信息。
        :type percentage_details: list[:class:`huaweicloudsdkrgc.v1.PercentageDetail`]
        :param landing_zone_action_type: Landing Zone当前需要执行的动作。
        :type landing_zone_action_type: str
        :param message: Landing Zone错误消息。
        :type message: list[:class:`huaweicloudsdkrgc.v1.LandingZoneErrorMessage`]
        :param regions: 纳管的区域信息。
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        
        super(ShowLandingZoneStatusResponse, self).__init__()

        self._deployed_version = None
        self._landing_zone_status = None
        self._percentage_complete = None
        self._percentage_details = None
        self._landing_zone_action_type = None
        self._message = None
        self._regions = None
        self.discriminator = None

        if deployed_version is not None:
            self.deployed_version = deployed_version
        if landing_zone_status is not None:
            self.landing_zone_status = landing_zone_status
        if percentage_complete is not None:
            self.percentage_complete = percentage_complete
        if percentage_details is not None:
            self.percentage_details = percentage_details
        if landing_zone_action_type is not None:
            self.landing_zone_action_type = landing_zone_action_type
        if message is not None:
            self.message = message
        if regions is not None:
            self.regions = regions

    @property
    def deployed_version(self):
        r"""Gets the deployed_version of this ShowLandingZoneStatusResponse.

        部署的Landing Zone版本。

        :return: The deployed_version of this ShowLandingZoneStatusResponse.
        :rtype: str
        """
        return self._deployed_version

    @deployed_version.setter
    def deployed_version(self, deployed_version):
        r"""Sets the deployed_version of this ShowLandingZoneStatusResponse.

        部署的Landing Zone版本。

        :param deployed_version: The deployed_version of this ShowLandingZoneStatusResponse.
        :type deployed_version: str
        """
        self._deployed_version = deployed_version

    @property
    def landing_zone_status(self):
        r"""Gets the landing_zone_status of this ShowLandingZoneStatusResponse.

        Landing Zone的设置状态，包括进行中，已完成。

        :return: The landing_zone_status of this ShowLandingZoneStatusResponse.
        :rtype: str
        """
        return self._landing_zone_status

    @landing_zone_status.setter
    def landing_zone_status(self, landing_zone_status):
        r"""Sets the landing_zone_status of this ShowLandingZoneStatusResponse.

        Landing Zone的设置状态，包括进行中，已完成。

        :param landing_zone_status: The landing_zone_status of this ShowLandingZoneStatusResponse.
        :type landing_zone_status: str
        """
        self._landing_zone_status = landing_zone_status

    @property
    def percentage_complete(self):
        r"""Gets the percentage_complete of this ShowLandingZoneStatusResponse.

        Landing Zone的完成进度。

        :return: The percentage_complete of this ShowLandingZoneStatusResponse.
        :rtype: int
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        r"""Sets the percentage_complete of this ShowLandingZoneStatusResponse.

        Landing Zone的完成进度。

        :param percentage_complete: The percentage_complete of this ShowLandingZoneStatusResponse.
        :type percentage_complete: int
        """
        self._percentage_complete = percentage_complete

    @property
    def percentage_details(self):
        r"""Gets the percentage_details of this ShowLandingZoneStatusResponse.

        Landing Zone设置的详细进度信息。

        :return: The percentage_details of this ShowLandingZoneStatusResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.PercentageDetail`]
        """
        return self._percentage_details

    @percentage_details.setter
    def percentage_details(self, percentage_details):
        r"""Sets the percentage_details of this ShowLandingZoneStatusResponse.

        Landing Zone设置的详细进度信息。

        :param percentage_details: The percentage_details of this ShowLandingZoneStatusResponse.
        :type percentage_details: list[:class:`huaweicloudsdkrgc.v1.PercentageDetail`]
        """
        self._percentage_details = percentage_details

    @property
    def landing_zone_action_type(self):
        r"""Gets the landing_zone_action_type of this ShowLandingZoneStatusResponse.

        Landing Zone当前需要执行的动作。

        :return: The landing_zone_action_type of this ShowLandingZoneStatusResponse.
        :rtype: str
        """
        return self._landing_zone_action_type

    @landing_zone_action_type.setter
    def landing_zone_action_type(self, landing_zone_action_type):
        r"""Sets the landing_zone_action_type of this ShowLandingZoneStatusResponse.

        Landing Zone当前需要执行的动作。

        :param landing_zone_action_type: The landing_zone_action_type of this ShowLandingZoneStatusResponse.
        :type landing_zone_action_type: str
        """
        self._landing_zone_action_type = landing_zone_action_type

    @property
    def message(self):
        r"""Gets the message of this ShowLandingZoneStatusResponse.

        Landing Zone错误消息。

        :return: The message of this ShowLandingZoneStatusResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.LandingZoneErrorMessage`]
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowLandingZoneStatusResponse.

        Landing Zone错误消息。

        :param message: The message of this ShowLandingZoneStatusResponse.
        :type message: list[:class:`huaweicloudsdkrgc.v1.LandingZoneErrorMessage`]
        """
        self._message = message

    @property
    def regions(self):
        r"""Gets the regions of this ShowLandingZoneStatusResponse.

        纳管的区域信息。

        :return: The regions of this ShowLandingZoneStatusResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        r"""Sets the regions of this ShowLandingZoneStatusResponse.

        纳管的区域信息。

        :param regions: The regions of this ShowLandingZoneStatusResponse.
        :type regions: list[:class:`huaweicloudsdkrgc.v1.RegionConfigurationList`]
        """
        self._regions = regions

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
        if not isinstance(other, ShowLandingZoneStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
