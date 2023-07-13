# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationalUnitsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organizational_units': 'list[OrganizationalUnitDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'organizational_units': 'organizational_units',
        'page_info': 'page_info'
    }

    def __init__(self, organizational_units=None, page_info=None):
        """ListOrganizationalUnitsResponse

        The model defined in huaweicloud sdk

        :param organizational_units: 组织单元列表。
        :type organizational_units: list[:class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListOrganizationalUnitsResponse, self).__init__()

        self._organizational_units = None
        self._page_info = None
        self.discriminator = None

        if organizational_units is not None:
            self.organizational_units = organizational_units
        if page_info is not None:
            self.page_info = page_info

    @property
    def organizational_units(self):
        """Gets the organizational_units of this ListOrganizationalUnitsResponse.

        组织单元列表。

        :return: The organizational_units of this ListOrganizationalUnitsResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`]
        """
        return self._organizational_units

    @organizational_units.setter
    def organizational_units(self, organizational_units):
        """Sets the organizational_units of this ListOrganizationalUnitsResponse.

        组织单元列表。

        :param organizational_units: The organizational_units of this ListOrganizationalUnitsResponse.
        :type organizational_units: list[:class:`huaweicloudsdkorganizations.v1.OrganizationalUnitDto`]
        """
        self._organizational_units = organizational_units

    @property
    def page_info(self):
        """Gets the page_info of this ListOrganizationalUnitsResponse.

        :return: The page_info of this ListOrganizationalUnitsResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListOrganizationalUnitsResponse.

        :param page_info: The page_info of this ListOrganizationalUnitsResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
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
        if not isinstance(other, ListOrganizationalUnitsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
