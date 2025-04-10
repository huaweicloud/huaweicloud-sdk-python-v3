# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnabledControlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled_controls': 'list[EnabledControl]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'enabled_controls': 'enabled_controls',
        'page_info': 'page_info'
    }

    def __init__(self, enabled_controls=None, page_info=None):
        r"""ListEnabledControlsResponse

        The model defined in huaweicloud sdk

        :param enabled_controls: 开启控制策略信息。
        :type enabled_controls: list[:class:`huaweicloudsdkrgc.v1.EnabledControl`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        
        super(ListEnabledControlsResponse, self).__init__()

        self._enabled_controls = None
        self._page_info = None
        self.discriminator = None

        if enabled_controls is not None:
            self.enabled_controls = enabled_controls
        if page_info is not None:
            self.page_info = page_info

    @property
    def enabled_controls(self):
        r"""Gets the enabled_controls of this ListEnabledControlsResponse.

        开启控制策略信息。

        :return: The enabled_controls of this ListEnabledControlsResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.EnabledControl`]
        """
        return self._enabled_controls

    @enabled_controls.setter
    def enabled_controls(self, enabled_controls):
        r"""Sets the enabled_controls of this ListEnabledControlsResponse.

        开启控制策略信息。

        :param enabled_controls: The enabled_controls of this ListEnabledControlsResponse.
        :type enabled_controls: list[:class:`huaweicloudsdkrgc.v1.EnabledControl`]
        """
        self._enabled_controls = enabled_controls

    @property
    def page_info(self):
        r"""Gets the page_info of this ListEnabledControlsResponse.

        :return: The page_info of this ListEnabledControlsResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListEnabledControlsResponse.

        :param page_info: The page_info of this ListEnabledControlsResponse.
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListEnabledControlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
