# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDefaultSecurityCheckPolicyDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'check_details': 'list[SecurityCheckPolicyDetailInfoResponseInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'check_details': 'check_details'
    }

    def __init__(self, total_num=None, check_details=None):
        r"""ShowDefaultSecurityCheckPolicyDetailsResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释** 检查项列表总数 **取值范围** 取值0-2147483647
        :type total_num: int
        :param check_details: **参数解释** 检查项列表
        :type check_details: list[:class:`huaweicloudsdkhss.v5.SecurityCheckPolicyDetailInfoResponseInfo`]
        """
        
        super().__init__()

        self._total_num = None
        self._check_details = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if check_details is not None:
            self.check_details = check_details

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowDefaultSecurityCheckPolicyDetailsResponse.

        **参数解释** 检查项列表总数 **取值范围** 取值0-2147483647

        :return: The total_num of this ShowDefaultSecurityCheckPolicyDetailsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowDefaultSecurityCheckPolicyDetailsResponse.

        **参数解释** 检查项列表总数 **取值范围** 取值0-2147483647

        :param total_num: The total_num of this ShowDefaultSecurityCheckPolicyDetailsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def check_details(self):
        r"""Gets the check_details of this ShowDefaultSecurityCheckPolicyDetailsResponse.

        **参数解释** 检查项列表

        :return: The check_details of this ShowDefaultSecurityCheckPolicyDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.SecurityCheckPolicyDetailInfoResponseInfo`]
        """
        return self._check_details

    @check_details.setter
    def check_details(self, check_details):
        r"""Sets the check_details of this ShowDefaultSecurityCheckPolicyDetailsResponse.

        **参数解释** 检查项列表

        :param check_details: The check_details of this ShowDefaultSecurityCheckPolicyDetailsResponse.
        :type check_details: list[:class:`huaweicloudsdkhss.v5.SecurityCheckPolicyDetailInfoResponseInfo`]
        """
        self._check_details = check_details

    def to_dict(self):
        import warnings
        warnings.warn("ShowDefaultSecurityCheckPolicyDetailsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDefaultSecurityCheckPolicyDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
