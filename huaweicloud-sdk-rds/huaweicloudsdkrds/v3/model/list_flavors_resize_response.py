# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsResizeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_groups': 'list[ComputeFlavorGroup]'
    }

    attribute_map = {
        'flavor_groups': 'flavor_groups'
    }

    def __init__(self, flavor_groups=None):
        r"""ListFlavorsResizeResponse

        The model defined in huaweicloud sdk

        :param flavor_groups: 规格组列表  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型
        :type flavor_groups: list[:class:`huaweicloudsdkrds.v3.ComputeFlavorGroup`]
        """
        
        super(ListFlavorsResizeResponse, self).__init__()

        self._flavor_groups = None
        self.discriminator = None

        if flavor_groups is not None:
            self.flavor_groups = flavor_groups

    @property
    def flavor_groups(self):
        r"""Gets the flavor_groups of this ListFlavorsResizeResponse.

        规格组列表  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型

        :return: The flavor_groups of this ListFlavorsResizeResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ComputeFlavorGroup`]
        """
        return self._flavor_groups

    @flavor_groups.setter
    def flavor_groups(self, flavor_groups):
        r"""Sets the flavor_groups of this ListFlavorsResizeResponse.

        规格组列表  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型

        :param flavor_groups: The flavor_groups of this ListFlavorsResizeResponse.
        :type flavor_groups: list[:class:`huaweicloudsdkrds.v3.ComputeFlavorGroup`]
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
        if not isinstance(other, ListFlavorsResizeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
