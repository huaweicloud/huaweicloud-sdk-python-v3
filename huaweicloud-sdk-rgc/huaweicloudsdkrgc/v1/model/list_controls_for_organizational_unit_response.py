# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlsForOrganizationalUnitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_summaries': 'list[TargetControl]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'control_summaries': 'control_summaries',
        'page_info': 'page_info'
    }

    def __init__(self, control_summaries=None, page_info=None):
        r"""ListControlsForOrganizationalUnitResponse

        The model defined in huaweicloud sdk

        :param control_summaries: 治理策略概要。
        :type control_summaries: list[:class:`huaweicloudsdkrgc.v1.TargetControl`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        
        super(ListControlsForOrganizationalUnitResponse, self).__init__()

        self._control_summaries = None
        self._page_info = None
        self.discriminator = None

        if control_summaries is not None:
            self.control_summaries = control_summaries
        if page_info is not None:
            self.page_info = page_info

    @property
    def control_summaries(self):
        r"""Gets the control_summaries of this ListControlsForOrganizationalUnitResponse.

        治理策略概要。

        :return: The control_summaries of this ListControlsForOrganizationalUnitResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.TargetControl`]
        """
        return self._control_summaries

    @control_summaries.setter
    def control_summaries(self, control_summaries):
        r"""Sets the control_summaries of this ListControlsForOrganizationalUnitResponse.

        治理策略概要。

        :param control_summaries: The control_summaries of this ListControlsForOrganizationalUnitResponse.
        :type control_summaries: list[:class:`huaweicloudsdkrgc.v1.TargetControl`]
        """
        self._control_summaries = control_summaries

    @property
    def page_info(self):
        r"""Gets the page_info of this ListControlsForOrganizationalUnitResponse.

        :return: The page_info of this ListControlsForOrganizationalUnitResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListControlsForOrganizationalUnitResponse.

        :param page_info: The page_info of this ListControlsForOrganizationalUnitResponse.
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
        if not isinstance(other, ListControlsForOrganizationalUnitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
