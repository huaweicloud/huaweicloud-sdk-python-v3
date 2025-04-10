# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRestrictionOfInstanceV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restrict_cidrs': 'list[str]',
        'resource_subnet_cidr': 'str'
    }

    attribute_map = {
        'restrict_cidrs': 'restrict_cidrs',
        'resource_subnet_cidr': 'resource_subnet_cidr'
    }

    def __init__(self, restrict_cidrs=None, resource_subnet_cidr=None):
        r"""ShowRestrictionOfInstanceV2Response

        The model defined in huaweicloud sdk

        :param restrict_cidrs: 受限的IP网段的CIDR列表。
        :type restrict_cidrs: list[str]
        :param resource_subnet_cidr: 资源租户的IP网段的CIDR。
        :type resource_subnet_cidr: str
        """
        
        super(ShowRestrictionOfInstanceV2Response, self).__init__()

        self._restrict_cidrs = None
        self._resource_subnet_cidr = None
        self.discriminator = None

        if restrict_cidrs is not None:
            self.restrict_cidrs = restrict_cidrs
        if resource_subnet_cidr is not None:
            self.resource_subnet_cidr = resource_subnet_cidr

    @property
    def restrict_cidrs(self):
        r"""Gets the restrict_cidrs of this ShowRestrictionOfInstanceV2Response.

        受限的IP网段的CIDR列表。

        :return: The restrict_cidrs of this ShowRestrictionOfInstanceV2Response.
        :rtype: list[str]
        """
        return self._restrict_cidrs

    @restrict_cidrs.setter
    def restrict_cidrs(self, restrict_cidrs):
        r"""Sets the restrict_cidrs of this ShowRestrictionOfInstanceV2Response.

        受限的IP网段的CIDR列表。

        :param restrict_cidrs: The restrict_cidrs of this ShowRestrictionOfInstanceV2Response.
        :type restrict_cidrs: list[str]
        """
        self._restrict_cidrs = restrict_cidrs

    @property
    def resource_subnet_cidr(self):
        r"""Gets the resource_subnet_cidr of this ShowRestrictionOfInstanceV2Response.

        资源租户的IP网段的CIDR。

        :return: The resource_subnet_cidr of this ShowRestrictionOfInstanceV2Response.
        :rtype: str
        """
        return self._resource_subnet_cidr

    @resource_subnet_cidr.setter
    def resource_subnet_cidr(self, resource_subnet_cidr):
        r"""Sets the resource_subnet_cidr of this ShowRestrictionOfInstanceV2Response.

        资源租户的IP网段的CIDR。

        :param resource_subnet_cidr: The resource_subnet_cidr of this ShowRestrictionOfInstanceV2Response.
        :type resource_subnet_cidr: str
        """
        self._resource_subnet_cidr = resource_subnet_cidr

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
        if not isinstance(other, ShowRestrictionOfInstanceV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
