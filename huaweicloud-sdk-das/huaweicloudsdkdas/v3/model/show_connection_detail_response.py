# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectionDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'das_conn_info': 'DasConnInfo'
    }

    attribute_map = {
        'das_conn_info': 'das_conn_info'
    }

    def __init__(self, das_conn_info=None):
        r"""ShowConnectionDetailResponse

        The model defined in huaweicloud sdk

        :param das_conn_info: 
        :type das_conn_info: :class:`huaweicloudsdkdas.v3.DasConnInfo`
        """
        
        super().__init__()

        self._das_conn_info = None
        self.discriminator = None

        if das_conn_info is not None:
            self.das_conn_info = das_conn_info

    @property
    def das_conn_info(self):
        r"""Gets the das_conn_info of this ShowConnectionDetailResponse.

        :return: The das_conn_info of this ShowConnectionDetailResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.DasConnInfo`
        """
        return self._das_conn_info

    @das_conn_info.setter
    def das_conn_info(self, das_conn_info):
        r"""Sets the das_conn_info of this ShowConnectionDetailResponse.

        :param das_conn_info: The das_conn_info of this ShowConnectionDetailResponse.
        :type das_conn_info: :class:`huaweicloudsdkdas.v3.DasConnInfo`
        """
        self._das_conn_info = das_conn_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowConnectionDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowConnectionDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
