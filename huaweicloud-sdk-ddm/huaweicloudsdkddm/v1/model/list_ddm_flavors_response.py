# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdmFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_groups': 'list[FlavorGroupInfo]'
    }

    attribute_map = {
        'flavor_groups': 'flavor_groups'
    }

    def __init__(self, flavor_groups=None):
        """ListDdmFlavorsResponse

        The model defined in huaweicloud sdk

        :param flavor_groups: 规格组。
        :type flavor_groups: list[:class:`huaweicloudsdkddm.v1.FlavorGroupInfo`]
        """
        
        super(ListDdmFlavorsResponse, self).__init__()

        self._flavor_groups = None
        self.discriminator = None

        if flavor_groups is not None:
            self.flavor_groups = flavor_groups

    @property
    def flavor_groups(self):
        """Gets the flavor_groups of this ListDdmFlavorsResponse.

        规格组。

        :return: The flavor_groups of this ListDdmFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.FlavorGroupInfo`]
        """
        return self._flavor_groups

    @flavor_groups.setter
    def flavor_groups(self, flavor_groups):
        """Sets the flavor_groups of this ListDdmFlavorsResponse.

        规格组。

        :param flavor_groups: The flavor_groups of this ListDdmFlavorsResponse.
        :type flavor_groups: list[:class:`huaweicloudsdkddm.v1.FlavorGroupInfo`]
        """
        self._flavor_groups = flavor_groups

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
        if not isinstance(other, ListDdmFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
