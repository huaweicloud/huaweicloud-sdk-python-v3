# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListManagedOrganizationalUnitsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_organization_units': 'list[ManagedOrganizationUnit]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'managed_organization_units': 'managed_organization_units',
        'page_info': 'page_info'
    }

    def __init__(self, managed_organization_units=None, page_info=None):
        """ListManagedOrganizationalUnitsResponse

        The model defined in huaweicloud sdk

        :param managed_organization_units: 注册OU信息。
        :type managed_organization_units: list[:class:`huaweicloudsdkrgc.v1.ManagedOrganizationUnit`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        
        super(ListManagedOrganizationalUnitsResponse, self).__init__()

        self._managed_organization_units = None
        self._page_info = None
        self.discriminator = None

        if managed_organization_units is not None:
            self.managed_organization_units = managed_organization_units
        if page_info is not None:
            self.page_info = page_info

    @property
    def managed_organization_units(self):
        """Gets the managed_organization_units of this ListManagedOrganizationalUnitsResponse.

        注册OU信息。

        :return: The managed_organization_units of this ListManagedOrganizationalUnitsResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.ManagedOrganizationUnit`]
        """
        return self._managed_organization_units

    @managed_organization_units.setter
    def managed_organization_units(self, managed_organization_units):
        """Sets the managed_organization_units of this ListManagedOrganizationalUnitsResponse.

        注册OU信息。

        :param managed_organization_units: The managed_organization_units of this ListManagedOrganizationalUnitsResponse.
        :type managed_organization_units: list[:class:`huaweicloudsdkrgc.v1.ManagedOrganizationUnit`]
        """
        self._managed_organization_units = managed_organization_units

    @property
    def page_info(self):
        """Gets the page_info of this ListManagedOrganizationalUnitsResponse.

        :return: The page_info of this ListManagedOrganizationalUnitsResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListManagedOrganizationalUnitsResponse.

        :param page_info: The page_info of this ListManagedOrganizationalUnitsResponse.
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
        if not isinstance(other, ListManagedOrganizationalUnitsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
