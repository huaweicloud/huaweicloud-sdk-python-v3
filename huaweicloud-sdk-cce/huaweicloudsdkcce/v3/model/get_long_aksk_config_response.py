# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetLongAkskConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_uploaded_long_aksk': 'bool',
        'enable_long_aksk_in_new_cluster': 'bool'
    }

    attribute_map = {
        'has_uploaded_long_aksk': 'hasUploadedLongAKSK',
        'enable_long_aksk_in_new_cluster': 'enableLongAKSKInNewCluster'
    }

    def __init__(self, has_uploaded_long_aksk=None, enable_long_aksk_in_new_cluster=None):
        r"""GetLongAkskConfigResponse

        The model defined in huaweicloud sdk

        :param has_uploaded_long_aksk: **参数解释：** 项目是否上传了LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 未上传LongAKSK - true: 已上传LongAKSK  **默认取值：** 不涉及
        :type has_uploaded_long_aksk: bool
        :param enable_long_aksk_in_new_cluster: **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 
        :type enable_long_aksk_in_new_cluster: bool
        """
        
        super().__init__()

        self._has_uploaded_long_aksk = None
        self._enable_long_aksk_in_new_cluster = None
        self.discriminator = None

        if has_uploaded_long_aksk is not None:
            self.has_uploaded_long_aksk = has_uploaded_long_aksk
        if enable_long_aksk_in_new_cluster is not None:
            self.enable_long_aksk_in_new_cluster = enable_long_aksk_in_new_cluster

    @property
    def has_uploaded_long_aksk(self):
        r"""Gets the has_uploaded_long_aksk of this GetLongAkskConfigResponse.

        **参数解释：** 项目是否上传了LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 未上传LongAKSK - true: 已上传LongAKSK  **默认取值：** 不涉及

        :return: The has_uploaded_long_aksk of this GetLongAkskConfigResponse.
        :rtype: bool
        """
        return self._has_uploaded_long_aksk

    @has_uploaded_long_aksk.setter
    def has_uploaded_long_aksk(self, has_uploaded_long_aksk):
        r"""Sets the has_uploaded_long_aksk of this GetLongAkskConfigResponse.

        **参数解释：** 项目是否上传了LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 未上传LongAKSK - true: 已上传LongAKSK  **默认取值：** 不涉及

        :param has_uploaded_long_aksk: The has_uploaded_long_aksk of this GetLongAkskConfigResponse.
        :type has_uploaded_long_aksk: bool
        """
        self._has_uploaded_long_aksk = has_uploaded_long_aksk

    @property
    def enable_long_aksk_in_new_cluster(self):
        r"""Gets the enable_long_aksk_in_new_cluster of this GetLongAkskConfigResponse.

        **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 

        :return: The enable_long_aksk_in_new_cluster of this GetLongAkskConfigResponse.
        :rtype: bool
        """
        return self._enable_long_aksk_in_new_cluster

    @enable_long_aksk_in_new_cluster.setter
    def enable_long_aksk_in_new_cluster(self, enable_long_aksk_in_new_cluster):
        r"""Sets the enable_long_aksk_in_new_cluster of this GetLongAkskConfigResponse.

        **参数解释：** 新建集群是否启用LongAKSK。 **约束限制：** 不涉及 **取值范围：** - false: 新建集群不启用LongAKSK - true: 新建集群启用LongAKSK  **默认取值：** 不涉及 

        :param enable_long_aksk_in_new_cluster: The enable_long_aksk_in_new_cluster of this GetLongAkskConfigResponse.
        :type enable_long_aksk_in_new_cluster: bool
        """
        self._enable_long_aksk_in_new_cluster = enable_long_aksk_in_new_cluster

    def to_dict(self):
        import warnings
        warnings.warn("GetLongAkskConfigResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, GetLongAkskConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
