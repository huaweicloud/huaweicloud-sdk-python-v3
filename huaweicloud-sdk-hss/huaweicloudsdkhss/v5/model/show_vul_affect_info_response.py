# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulAffectInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affect_host_ids': 'list[str]',
        'affect_vul_ids': 'list[str]'
    }

    attribute_map = {
        'affect_host_ids': 'affect_host_ids',
        'affect_vul_ids': 'affect_vul_ids'
    }

    def __init__(self, affect_host_ids=None, affect_vul_ids=None):
        r"""ShowVulAffectInfoResponse

        The model defined in huaweicloud sdk

        :param affect_host_ids: **参数解释**: 漏洞影响的主机ID列表 **取值范围**: 最小值0，最大值65535 
        :type affect_host_ids: list[str]
        :param affect_vul_ids: **参数解释**: 主机下的漏洞ID列表 **取值范围**: 最小值0，最大值65535 
        :type affect_vul_ids: list[str]
        """
        
        super().__init__()

        self._affect_host_ids = None
        self._affect_vul_ids = None
        self.discriminator = None

        if affect_host_ids is not None:
            self.affect_host_ids = affect_host_ids
        if affect_vul_ids is not None:
            self.affect_vul_ids = affect_vul_ids

    @property
    def affect_host_ids(self):
        r"""Gets the affect_host_ids of this ShowVulAffectInfoResponse.

        **参数解释**: 漏洞影响的主机ID列表 **取值范围**: 最小值0，最大值65535 

        :return: The affect_host_ids of this ShowVulAffectInfoResponse.
        :rtype: list[str]
        """
        return self._affect_host_ids

    @affect_host_ids.setter
    def affect_host_ids(self, affect_host_ids):
        r"""Sets the affect_host_ids of this ShowVulAffectInfoResponse.

        **参数解释**: 漏洞影响的主机ID列表 **取值范围**: 最小值0，最大值65535 

        :param affect_host_ids: The affect_host_ids of this ShowVulAffectInfoResponse.
        :type affect_host_ids: list[str]
        """
        self._affect_host_ids = affect_host_ids

    @property
    def affect_vul_ids(self):
        r"""Gets the affect_vul_ids of this ShowVulAffectInfoResponse.

        **参数解释**: 主机下的漏洞ID列表 **取值范围**: 最小值0，最大值65535 

        :return: The affect_vul_ids of this ShowVulAffectInfoResponse.
        :rtype: list[str]
        """
        return self._affect_vul_ids

    @affect_vul_ids.setter
    def affect_vul_ids(self, affect_vul_ids):
        r"""Sets the affect_vul_ids of this ShowVulAffectInfoResponse.

        **参数解释**: 主机下的漏洞ID列表 **取值范围**: 最小值0，最大值65535 

        :param affect_vul_ids: The affect_vul_ids of this ShowVulAffectInfoResponse.
        :type affect_vul_ids: list[str]
        """
        self._affect_vul_ids = affect_vul_ids

    def to_dict(self):
        import warnings
        warnings.warn("ShowVulAffectInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVulAffectInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
