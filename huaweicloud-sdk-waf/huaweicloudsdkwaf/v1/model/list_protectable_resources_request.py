# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectableResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'region': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'region': 'region',
        'resource_type': 'resource_type'
    }

    def __init__(self, vpc_id=None, region=None, resource_type=None):
        r"""ListProtectableResourcesRequest

        The model defined in huaweicloud sdk

        :param vpc_id: **参数解释：** 负载均衡器所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vpc_id: str
        :param region: **参数解释：** 租户region **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type region: str
        :param resource_type: **参数解释：** 查询的防护资源类型，目前支持的资源类型为:elb **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** elb
        :type resource_type: str
        """
        
        

        self._vpc_id = None
        self._region = None
        self._resource_type = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if region is not None:
            self.region = region
        self.resource_type = resource_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListProtectableResourcesRequest.

        **参数解释：** 负载均衡器所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vpc_id of this ListProtectableResourcesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListProtectableResourcesRequest.

        **参数解释：** 负载均衡器所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vpc_id: The vpc_id of this ListProtectableResourcesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def region(self):
        r"""Gets the region of this ListProtectableResourcesRequest.

        **参数解释：** 租户region **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The region of this ListProtectableResourcesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListProtectableResourcesRequest.

        **参数解释：** 租户region **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param region: The region of this ListProtectableResourcesRequest.
        :type region: str
        """
        self._region = region

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListProtectableResourcesRequest.

        **参数解释：** 查询的防护资源类型，目前支持的资源类型为:elb **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** elb

        :return: The resource_type of this ListProtectableResourcesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListProtectableResourcesRequest.

        **参数解释：** 查询的防护资源类型，目前支持的资源类型为:elb **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** elb

        :param resource_type: The resource_type of this ListProtectableResourcesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ListProtectableResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
