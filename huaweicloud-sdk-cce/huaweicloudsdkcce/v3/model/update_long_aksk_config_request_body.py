# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLongAKSKConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_long_aksk_in_new_cluster': 'bool'
    }

    attribute_map = {
        'enable_long_aksk_in_new_cluster': 'enableLongAKSKInNewCluster'
    }

    def __init__(self, enable_long_aksk_in_new_cluster=None):
        r"""UpdateLongAKSKConfigRequestBody

        The model defined in huaweicloud sdk

        :param enable_long_aksk_in_new_cluster: **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 
        :type enable_long_aksk_in_new_cluster: bool
        """
        
        

        self._enable_long_aksk_in_new_cluster = None
        self.discriminator = None

        self.enable_long_aksk_in_new_cluster = enable_long_aksk_in_new_cluster

    @property
    def enable_long_aksk_in_new_cluster(self):
        r"""Gets the enable_long_aksk_in_new_cluster of this UpdateLongAKSKConfigRequestBody.

        **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 

        :return: The enable_long_aksk_in_new_cluster of this UpdateLongAKSKConfigRequestBody.
        :rtype: bool
        """
        return self._enable_long_aksk_in_new_cluster

    @enable_long_aksk_in_new_cluster.setter
    def enable_long_aksk_in_new_cluster(self, enable_long_aksk_in_new_cluster):
        r"""Sets the enable_long_aksk_in_new_cluster of this UpdateLongAKSKConfigRequestBody.

        **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 

        :param enable_long_aksk_in_new_cluster: The enable_long_aksk_in_new_cluster of this UpdateLongAKSKConfigRequestBody.
        :type enable_long_aksk_in_new_cluster: bool
        """
        self._enable_long_aksk_in_new_cluster = enable_long_aksk_in_new_cluster

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
        if not isinstance(other, UpdateLongAKSKConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
