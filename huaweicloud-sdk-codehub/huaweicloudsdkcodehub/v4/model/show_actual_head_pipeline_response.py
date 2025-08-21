# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowActualHeadPipelineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'PipelineDetailDto',
        'is_valid': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'is_valid': 'is_valid'
    }

    def __init__(self, data=None, is_valid=None):
        r"""ShowActualHeadPipelineResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkcodehub.v4.PipelineDetailDto`
        :param is_valid: 最新的commit是否有对应的流水线
        :type is_valid: bool
        """
        
        super(ShowActualHeadPipelineResponse, self).__init__()

        self._data = None
        self._is_valid = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def data(self):
        r"""Gets the data of this ShowActualHeadPipelineResponse.

        :return: The data of this ShowActualHeadPipelineResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.PipelineDetailDto`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowActualHeadPipelineResponse.

        :param data: The data of this ShowActualHeadPipelineResponse.
        :type data: :class:`huaweicloudsdkcodehub.v4.PipelineDetailDto`
        """
        self._data = data

    @property
    def is_valid(self):
        r"""Gets the is_valid of this ShowActualHeadPipelineResponse.

        最新的commit是否有对应的流水线

        :return: The is_valid of this ShowActualHeadPipelineResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this ShowActualHeadPipelineResponse.

        最新的commit是否有对应的流水线

        :param is_valid: The is_valid of this ShowActualHeadPipelineResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

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
        if not isinstance(other, ShowActualHeadPipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
