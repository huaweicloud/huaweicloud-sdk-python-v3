# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_label_list': 'list[ClusterLabelInfo]'
    }

    attribute_map = {
        'cluster_label_list': 'cluster_label_list'
    }

    def __init__(self, cluster_label_list=None):
        r"""UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo

        The model defined in huaweicloud sdk

        :param cluster_label_list: **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        """
        
        

        self._cluster_label_list = None
        self.discriminator = None

        if cluster_label_list is not None:
            self.cluster_label_list = cluster_label_list

    @property
    def cluster_label_list(self):
        r"""Gets the cluster_label_list of this UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo.

        **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :return: The cluster_label_list of this UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        """
        return self._cluster_label_list

    @cluster_label_list.setter
    def cluster_label_list(self, cluster_label_list):
        r"""Sets the cluster_label_list of this UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo.

        **参数解释**: 集群标签列表 **约束限制**: protect_type值为“cluster”时生效 **取值范围**: 最少0条，最多10条 **默认取值**: 不涉及 

        :param cluster_label_list: The cluster_label_list of this UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo.
        :type cluster_label_list: list[:class:`huaweicloudsdkhss.v5.ClusterLabelInfo`]
        """
        self._cluster_label_list = cluster_label_list

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
        if not isinstance(other, UpdateWebTamperProtectionConfigRequestInfoContainerWtpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
