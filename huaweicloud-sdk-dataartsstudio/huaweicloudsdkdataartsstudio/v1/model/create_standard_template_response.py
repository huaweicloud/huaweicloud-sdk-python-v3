# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStandardTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'CreateStandardTemplateResultData'
    }

    attribute_map = {
        'data': 'data'
    }

    def __init__(self, data=None):
        r"""CreateStandardTemplateResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateResultData`
        """
        
        super().__init__()

        self._data = None
        self.discriminator = None

        if data is not None:
            self.data = data

    @property
    def data(self):
        r"""Gets the data of this CreateStandardTemplateResponse.

        :return: The data of this CreateStandardTemplateResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateResultData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreateStandardTemplateResponse.

        :param data: The data of this CreateStandardTemplateResponse.
        :type data: :class:`huaweicloudsdkdataartsstudio.v1.CreateStandardTemplateResultData`
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("CreateStandardTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateStandardTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
