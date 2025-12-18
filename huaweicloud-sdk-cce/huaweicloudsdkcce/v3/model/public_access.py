# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicAccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'cidrs': 'cidrs'
    }

    def __init__(self, cidrs=None):
        r"""PublicAccess

        The model defined in huaweicloud sdk

        :param cidrs: **参数解释：** 允许访问集群API的白名单网段列表，建议对VPC网段、容器网段放通。 **约束限制：** 该字段仅支持创建集群时传入，更新时指定无效 **取值范围：** 不涉及 **默认取值：** 默认无白名单配置，为[\&quot;0.0.0.0/0\&quot;]。 
        :type cidrs: list[str]
        """
        
        

        self._cidrs = None
        self.discriminator = None

        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def cidrs(self):
        r"""Gets the cidrs of this PublicAccess.

        **参数解释：** 允许访问集群API的白名单网段列表，建议对VPC网段、容器网段放通。 **约束限制：** 该字段仅支持创建集群时传入，更新时指定无效 **取值范围：** 不涉及 **默认取值：** 默认无白名单配置，为[\"0.0.0.0/0\"]。 

        :return: The cidrs of this PublicAccess.
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        r"""Sets the cidrs of this PublicAccess.

        **参数解释：** 允许访问集群API的白名单网段列表，建议对VPC网段、容器网段放通。 **约束限制：** 该字段仅支持创建集群时传入，更新时指定无效 **取值范围：** 不涉及 **默认取值：** 默认无白名单配置，为[\"0.0.0.0/0\"]。 

        :param cidrs: The cidrs of this PublicAccess.
        :type cidrs: list[str]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, PublicAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
