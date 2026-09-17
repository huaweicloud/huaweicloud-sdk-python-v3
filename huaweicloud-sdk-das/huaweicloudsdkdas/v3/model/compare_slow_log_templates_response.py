# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareSlowLogTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contrasts': 'list[SlowLogTplContrast]'
    }

    attribute_map = {
        'contrasts': 'contrasts'
    }

    def __init__(self, contrasts=None):
        r"""CompareSlowLogTemplatesResponse

        The model defined in huaweicloud sdk

        :param contrasts: 模板数据对比结果列表
        :type contrasts: list[:class:`huaweicloudsdkdas.v3.SlowLogTplContrast`]
        """
        
        super().__init__()

        self._contrasts = None
        self.discriminator = None

        if contrasts is not None:
            self.contrasts = contrasts

    @property
    def contrasts(self):
        r"""Gets the contrasts of this CompareSlowLogTemplatesResponse.

        模板数据对比结果列表

        :return: The contrasts of this CompareSlowLogTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTplContrast`]
        """
        return self._contrasts

    @contrasts.setter
    def contrasts(self, contrasts):
        r"""Sets the contrasts of this CompareSlowLogTemplatesResponse.

        模板数据对比结果列表

        :param contrasts: The contrasts of this CompareSlowLogTemplatesResponse.
        :type contrasts: list[:class:`huaweicloudsdkdas.v3.SlowLogTplContrast`]
        """
        self._contrasts = contrasts

    def to_dict(self):
        import warnings
        warnings.warn("CompareSlowLogTemplatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CompareSlowLogTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
