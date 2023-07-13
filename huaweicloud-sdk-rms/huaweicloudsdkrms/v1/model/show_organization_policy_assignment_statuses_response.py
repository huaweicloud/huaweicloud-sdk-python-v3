# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationPolicyAssignmentStatusesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'list[OrganizationPolicyAssignmentStatusResponse]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'value': 'value',
        'page_info': 'page_info'
    }

    def __init__(self, value=None, page_info=None):
        """ShowOrganizationPolicyAssignmentStatusesResponse

        The model defined in huaweicloud sdk

        :param value: 组织合规规则部署状态结果列表。
        :type value: list[:class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentStatusResponse`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        
        super(ShowOrganizationPolicyAssignmentStatusesResponse, self).__init__()

        self._value = None
        self._page_info = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if page_info is not None:
            self.page_info = page_info

    @property
    def value(self):
        """Gets the value of this ShowOrganizationPolicyAssignmentStatusesResponse.

        组织合规规则部署状态结果列表。

        :return: The value of this ShowOrganizationPolicyAssignmentStatusesResponse.
        :rtype: list[:class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentStatusResponse`]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowOrganizationPolicyAssignmentStatusesResponse.

        组织合规规则部署状态结果列表。

        :param value: The value of this ShowOrganizationPolicyAssignmentStatusesResponse.
        :type value: list[:class:`huaweicloudsdkrms.v1.OrganizationPolicyAssignmentStatusResponse`]
        """
        self._value = value

    @property
    def page_info(self):
        """Gets the page_info of this ShowOrganizationPolicyAssignmentStatusesResponse.

        :return: The page_info of this ShowOrganizationPolicyAssignmentStatusesResponse.
        :rtype: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ShowOrganizationPolicyAssignmentStatusesResponse.

        :param page_info: The page_info of this ShowOrganizationPolicyAssignmentStatusesResponse.
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
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
        if not isinstance(other, ShowOrganizationPolicyAssignmentStatusesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
