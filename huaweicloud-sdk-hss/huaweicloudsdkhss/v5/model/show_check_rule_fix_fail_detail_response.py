# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckRuleFixFailDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail_detail_list': 'list[CheckRuleFixFailDetailInfo]'
    }

    attribute_map = {
        'fail_detail_list': 'fail_detail_list'
    }

    def __init__(self, fail_detail_list=None):
        r"""ShowCheckRuleFixFailDetailResponse

        The model defined in huaweicloud sdk

        :param fail_detail_list: 修复失败原因列表
        :type fail_detail_list: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixFailDetailInfo`]
        """
        
        super().__init__()

        self._fail_detail_list = None
        self.discriminator = None

        if fail_detail_list is not None:
            self.fail_detail_list = fail_detail_list

    @property
    def fail_detail_list(self):
        r"""Gets the fail_detail_list of this ShowCheckRuleFixFailDetailResponse.

        修复失败原因列表

        :return: The fail_detail_list of this ShowCheckRuleFixFailDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixFailDetailInfo`]
        """
        return self._fail_detail_list

    @fail_detail_list.setter
    def fail_detail_list(self, fail_detail_list):
        r"""Sets the fail_detail_list of this ShowCheckRuleFixFailDetailResponse.

        修复失败原因列表

        :param fail_detail_list: The fail_detail_list of this ShowCheckRuleFixFailDetailResponse.
        :type fail_detail_list: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixFailDetailInfo`]
        """
        self._fail_detail_list = fail_detail_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowCheckRuleFixFailDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCheckRuleFixFailDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
