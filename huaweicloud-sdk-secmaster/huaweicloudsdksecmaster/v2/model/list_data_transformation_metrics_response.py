# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataTransformationMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'Object1Map',
        'usage': 'Object2Map'
    }

    attribute_map = {
        'status': 'status',
        'usage': 'usage'
    }

    def __init__(self, status=None, usage=None):
        r"""ListDataTransformationMetricsResponse

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdksecmaster.v2.Object1Map`
        :param usage: 
        :type usage: :class:`huaweicloudsdksecmaster.v2.Object2Map`
        """
        
        super().__init__()

        self._status = None
        self._usage = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if usage is not None:
            self.usage = usage

    @property
    def status(self):
        r"""Gets the status of this ListDataTransformationMetricsResponse.

        :return: The status of this ListDataTransformationMetricsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.Object1Map`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDataTransformationMetricsResponse.

        :param status: The status of this ListDataTransformationMetricsResponse.
        :type status: :class:`huaweicloudsdksecmaster.v2.Object1Map`
        """
        self._status = status

    @property
    def usage(self):
        r"""Gets the usage of this ListDataTransformationMetricsResponse.

        :return: The usage of this ListDataTransformationMetricsResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.Object2Map`
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        r"""Sets the usage of this ListDataTransformationMetricsResponse.

        :param usage: The usage of this ListDataTransformationMetricsResponse.
        :type usage: :class:`huaweicloudsdksecmaster.v2.Object2Map`
        """
        self._usage = usage

    def to_dict(self):
        import warnings
        warnings.warn("ListDataTransformationMetricsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDataTransformationMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
