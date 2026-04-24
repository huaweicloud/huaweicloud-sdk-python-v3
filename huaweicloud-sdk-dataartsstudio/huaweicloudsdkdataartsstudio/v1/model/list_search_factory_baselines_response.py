# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchFactoryBaselinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baselines': 'list[BaselineV2]',
        'total': 'int'
    }

    attribute_map = {
        'baselines': 'baselines',
        'total': 'total'
    }

    def __init__(self, baselines=None, total=None):
        r"""ListSearchFactoryBaselinesResponse

        The model defined in huaweicloud sdk

        :param baselines: 基线任务。
        :type baselines: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineV2`]
        :param total: 总数。
        :type total: int
        """
        
        super().__init__()

        self._baselines = None
        self._total = None
        self.discriminator = None

        if baselines is not None:
            self.baselines = baselines
        if total is not None:
            self.total = total

    @property
    def baselines(self):
        r"""Gets the baselines of this ListSearchFactoryBaselinesResponse.

        基线任务。

        :return: The baselines of this ListSearchFactoryBaselinesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineV2`]
        """
        return self._baselines

    @baselines.setter
    def baselines(self, baselines):
        r"""Sets the baselines of this ListSearchFactoryBaselinesResponse.

        基线任务。

        :param baselines: The baselines of this ListSearchFactoryBaselinesResponse.
        :type baselines: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineV2`]
        """
        self._baselines = baselines

    @property
    def total(self):
        r"""Gets the total of this ListSearchFactoryBaselinesResponse.

        总数。

        :return: The total of this ListSearchFactoryBaselinesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSearchFactoryBaselinesResponse.

        总数。

        :param total: The total of this ListSearchFactoryBaselinesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListSearchFactoryBaselinesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSearchFactoryBaselinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
