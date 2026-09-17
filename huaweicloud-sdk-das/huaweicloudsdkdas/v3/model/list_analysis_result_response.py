# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAnalysisResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'risk': 'bool',
        'data': 'object'
    }

    attribute_map = {
        'success': 'success',
        'risk': 'risk',
        'data': 'data'
    }

    def __init__(self, success=None, risk=None, data=None):
        r"""ListAnalysisResultResponse

        The model defined in huaweicloud sdk

        :param success: 是否成功
        :type success: bool
        :param risk: 是否有风险
        :type risk: bool
        :param data: 分析数据
        :type data: object
        """
        
        super().__init__()

        self._success = None
        self._risk = None
        self._data = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if risk is not None:
            self.risk = risk
        if data is not None:
            self.data = data

    @property
    def success(self):
        r"""Gets the success of this ListAnalysisResultResponse.

        是否成功

        :return: The success of this ListAnalysisResultResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ListAnalysisResultResponse.

        是否成功

        :param success: The success of this ListAnalysisResultResponse.
        :type success: bool
        """
        self._success = success

    @property
    def risk(self):
        r"""Gets the risk of this ListAnalysisResultResponse.

        是否有风险

        :return: The risk of this ListAnalysisResultResponse.
        :rtype: bool
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        r"""Sets the risk of this ListAnalysisResultResponse.

        是否有风险

        :param risk: The risk of this ListAnalysisResultResponse.
        :type risk: bool
        """
        self._risk = risk

    @property
    def data(self):
        r"""Gets the data of this ListAnalysisResultResponse.

        分析数据

        :return: The data of this ListAnalysisResultResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAnalysisResultResponse.

        分析数据

        :param data: The data of this ListAnalysisResultResponse.
        :type data: object
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ListAnalysisResultResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAnalysisResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
