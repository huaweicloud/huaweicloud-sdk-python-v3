# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zones': 'list[AvailableZoneV2]',
        'default_az_code': 'str',
        'support_physical_az_group': 'bool'
    }

    attribute_map = {
        'available_zones': 'available_zones',
        'default_az_code': 'default_az_code',
        'support_physical_az_group': 'support_physical_az_group'
    }

    def __init__(self, available_zones=None, default_az_code=None, support_physical_az_group=None):
        r"""ListAvailableZonesResponse

        The model defined in huaweicloud sdk

        :param available_zones: 可用区列表
        :type available_zones: list[:class:`huaweicloudsdkmrs.v1.AvailableZoneV2`]
        :param default_az_code: 默认可用区编码
        :type default_az_code: str
        :param support_physical_az_group: 支持的物理可用区分组
        :type support_physical_az_group: bool
        """
        
        super(ListAvailableZonesResponse, self).__init__()

        self._available_zones = None
        self._default_az_code = None
        self._support_physical_az_group = None
        self.discriminator = None

        if available_zones is not None:
            self.available_zones = available_zones
        if default_az_code is not None:
            self.default_az_code = default_az_code
        if support_physical_az_group is not None:
            self.support_physical_az_group = support_physical_az_group

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListAvailableZonesResponse.

        可用区列表

        :return: The available_zones of this ListAvailableZonesResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.AvailableZoneV2`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListAvailableZonesResponse.

        可用区列表

        :param available_zones: The available_zones of this ListAvailableZonesResponse.
        :type available_zones: list[:class:`huaweicloudsdkmrs.v1.AvailableZoneV2`]
        """
        self._available_zones = available_zones

    @property
    def default_az_code(self):
        r"""Gets the default_az_code of this ListAvailableZonesResponse.

        默认可用区编码

        :return: The default_az_code of this ListAvailableZonesResponse.
        :rtype: str
        """
        return self._default_az_code

    @default_az_code.setter
    def default_az_code(self, default_az_code):
        r"""Sets the default_az_code of this ListAvailableZonesResponse.

        默认可用区编码

        :param default_az_code: The default_az_code of this ListAvailableZonesResponse.
        :type default_az_code: str
        """
        self._default_az_code = default_az_code

    @property
    def support_physical_az_group(self):
        r"""Gets the support_physical_az_group of this ListAvailableZonesResponse.

        支持的物理可用区分组

        :return: The support_physical_az_group of this ListAvailableZonesResponse.
        :rtype: bool
        """
        return self._support_physical_az_group

    @support_physical_az_group.setter
    def support_physical_az_group(self, support_physical_az_group):
        r"""Sets the support_physical_az_group of this ListAvailableZonesResponse.

        支持的物理可用区分组

        :param support_physical_az_group: The support_physical_az_group of this ListAvailableZonesResponse.
        :type support_physical_az_group: bool
        """
        self._support_physical_az_group = support_physical_az_group

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
        if not isinstance(other, ListAvailableZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
