# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullSqlSampleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample': 'FullSqlSampleInfo'
    }

    attribute_map = {
        'sample': 'sample'
    }

    def __init__(self, sample=None):
        r"""ShowFullSqlSampleResponse

        The model defined in huaweicloud sdk

        :param sample: 
        :type sample: :class:`huaweicloudsdkdas.v3.FullSqlSampleInfo`
        """
        
        super().__init__()

        self._sample = None
        self.discriminator = None

        if sample is not None:
            self.sample = sample

    @property
    def sample(self):
        r"""Gets the sample of this ShowFullSqlSampleResponse.

        :return: The sample of this ShowFullSqlSampleResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.FullSqlSampleInfo`
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        r"""Sets the sample of this ShowFullSqlSampleResponse.

        :param sample: The sample of this ShowFullSqlSampleResponse.
        :type sample: :class:`huaweicloudsdkdas.v3.FullSqlSampleInfo`
        """
        self._sample = sample

    def to_dict(self):
        import warnings
        warnings.warn("ShowFullSqlSampleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFullSqlSampleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
