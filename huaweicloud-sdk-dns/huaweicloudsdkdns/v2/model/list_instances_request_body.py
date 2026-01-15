# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dim_name': 'list[str]',
        'ids': 'list[list[str]]'
    }

    attribute_map = {
        'dim_name': 'dim_name',
        'ids': 'ids'
    }

    def __init__(self, dim_name=None, ids=None):
        r"""ListInstancesRequestBody

        The model defined in huaweicloud sdk

        :param dim_name: **参数解释：** DNS批量查询接口支持查询的维度。 **约束限制：** 不涉及。 **取值范围：** - dns_public_zone_id：公网域名ID - dns_public_recordset_id：公网记录集ID，需与dns_public_zone_id组合使用 - dns_private_zone_id：内网域名ID - vpc_id：VPC ID，需与dns_private_zone_id组合使用 **默认取值：** 不涉及。
        :type dim_name: list[str]
        :param ids: DNS上报的资源ID列表。
        :type ids: list[list[str]]
        """
        
        

        self._dim_name = None
        self._ids = None
        self.discriminator = None

        self.dim_name = dim_name
        self.ids = ids

    @property
    def dim_name(self):
        r"""Gets the dim_name of this ListInstancesRequestBody.

        **参数解释：** DNS批量查询接口支持查询的维度。 **约束限制：** 不涉及。 **取值范围：** - dns_public_zone_id：公网域名ID - dns_public_recordset_id：公网记录集ID，需与dns_public_zone_id组合使用 - dns_private_zone_id：内网域名ID - vpc_id：VPC ID，需与dns_private_zone_id组合使用 **默认取值：** 不涉及。

        :return: The dim_name of this ListInstancesRequestBody.
        :rtype: list[str]
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        r"""Sets the dim_name of this ListInstancesRequestBody.

        **参数解释：** DNS批量查询接口支持查询的维度。 **约束限制：** 不涉及。 **取值范围：** - dns_public_zone_id：公网域名ID - dns_public_recordset_id：公网记录集ID，需与dns_public_zone_id组合使用 - dns_private_zone_id：内网域名ID - vpc_id：VPC ID，需与dns_private_zone_id组合使用 **默认取值：** 不涉及。

        :param dim_name: The dim_name of this ListInstancesRequestBody.
        :type dim_name: list[str]
        """
        self._dim_name = dim_name

    @property
    def ids(self):
        r"""Gets the ids of this ListInstancesRequestBody.

        DNS上报的资源ID列表。

        :return: The ids of this ListInstancesRequestBody.
        :rtype: list[list[str]]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ListInstancesRequestBody.

        DNS上报的资源ID列表。

        :param ids: The ids of this ListInstancesRequestBody.
        :type ids: list[list[str]]
        """
        self._ids = ids

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
