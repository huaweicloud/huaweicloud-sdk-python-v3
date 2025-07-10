# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDrugModelResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'resources': 'list[PanguDrugModelResourceRsp]',
        'x_resource_mappings': 'str'
    }

    attribute_map = {
        'count': 'count',
        'resources': 'resources',
        'x_resource_mappings': 'X-Resource-Mappings'
    }

    def __init__(self, count=None, resources=None, x_resource_mappings=None):
        r"""ListDrugModelResourceResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        :param resources: **参数解释**： 模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type resources: list[:class:`huaweicloudsdkeihealth.v1.PanguDrugModelResourceRsp`]
        :param x_resource_mappings: 
        :type x_resource_mappings: str
        """
        
        super(ListDrugModelResourceResponse, self).__init__()

        self._count = None
        self._resources = None
        self._x_resource_mappings = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if resources is not None:
            self.resources = resources
        if x_resource_mappings is not None:
            self.x_resource_mappings = x_resource_mappings

    @property
    def count(self):
        r"""Gets the count of this ListDrugModelResourceResponse.

        **参数解释**： 总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListDrugModelResourceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDrugModelResourceResponse.

        **参数解释**： 总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListDrugModelResourceResponse.
        :type count: int
        """
        self._count = count

    @property
    def resources(self):
        r"""Gets the resources of this ListDrugModelResourceResponse.

        **参数解释**： 模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The resources of this ListDrugModelResourceResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.PanguDrugModelResourceRsp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListDrugModelResourceResponse.

        **参数解释**： 模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param resources: The resources of this ListDrugModelResourceResponse.
        :type resources: list[:class:`huaweicloudsdkeihealth.v1.PanguDrugModelResourceRsp`]
        """
        self._resources = resources

    @property
    def x_resource_mappings(self):
        r"""Gets the x_resource_mappings of this ListDrugModelResourceResponse.

        :return: The x_resource_mappings of this ListDrugModelResourceResponse.
        :rtype: str
        """
        return self._x_resource_mappings

    @x_resource_mappings.setter
    def x_resource_mappings(self, x_resource_mappings):
        r"""Sets the x_resource_mappings of this ListDrugModelResourceResponse.

        :param x_resource_mappings: The x_resource_mappings of this ListDrugModelResourceResponse.
        :type x_resource_mappings: str
        """
        self._x_resource_mappings = x_resource_mappings

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
        if not isinstance(other, ListDrugModelResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
