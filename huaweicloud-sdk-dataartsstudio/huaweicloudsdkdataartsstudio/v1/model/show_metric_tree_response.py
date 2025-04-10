# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'architecture': 'list[ArchitectureStatistic]'
    }

    attribute_map = {
        'architecture': 'architecture'
    }

    def __init__(self, architecture=None):
        r"""ShowMetricTreeResponse

        The model defined in huaweicloud sdk

        :param architecture: 结构体系
        :type architecture: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        """
        
        super(ShowMetricTreeResponse, self).__init__()

        self._architecture = None
        self.discriminator = None

        if architecture is not None:
            self.architecture = architecture

    @property
    def architecture(self):
        r"""Gets the architecture of this ShowMetricTreeResponse.

        结构体系

        :return: The architecture of this ShowMetricTreeResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this ShowMetricTreeResponse.

        结构体系

        :param architecture: The architecture of this ShowMetricTreeResponse.
        :type architecture: list[:class:`huaweicloudsdkdataartsstudio.v1.ArchitectureStatistic`]
        """
        self._architecture = architecture

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowMetricTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
