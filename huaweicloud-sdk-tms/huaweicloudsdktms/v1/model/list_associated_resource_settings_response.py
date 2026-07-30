# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedResourceSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'settings': 'list[AssociatedResourceSetting]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'settings': 'settings',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, settings=None, total_count=None, page_info=None):
        r"""ListAssociatedResourceSettingsResponse

        The model defined in huaweicloud sdk

        :param settings: 规则的配置信息
        :type settings: list[:class:`huaweicloudsdktms.v1.AssociatedResourceSetting`]
        :param total_count: 记录总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        
        super().__init__()

        self._settings = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def settings(self):
        r"""Gets the settings of this ListAssociatedResourceSettingsResponse.

        规则的配置信息

        :return: The settings of this ListAssociatedResourceSettingsResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.AssociatedResourceSetting`]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        r"""Sets the settings of this ListAssociatedResourceSettingsResponse.

        规则的配置信息

        :param settings: The settings of this ListAssociatedResourceSettingsResponse.
        :type settings: list[:class:`huaweicloudsdktms.v1.AssociatedResourceSetting`]
        """
        self._settings = settings

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAssociatedResourceSettingsResponse.

        记录总数

        :return: The total_count of this ListAssociatedResourceSettingsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAssociatedResourceSettingsResponse.

        记录总数

        :param total_count: The total_count of this ListAssociatedResourceSettingsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAssociatedResourceSettingsResponse.

        :return: The page_info of this ListAssociatedResourceSettingsResponse.
        :rtype: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAssociatedResourceSettingsResponse.

        :param page_info: The page_info of this ListAssociatedResourceSettingsResponse.
        :type page_info: :class:`huaweicloudsdktms.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListAssociatedResourceSettingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAssociatedResourceSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
