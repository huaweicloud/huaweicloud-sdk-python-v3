# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClouddbaGetSearchPathFlagNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_path_flag': 'bool'
    }

    attribute_map = {
        'search_path_flag': 'search_path_flag'
    }

    def __init__(self, search_path_flag=None):
        r"""ShowClouddbaGetSearchPathFlagNewResponse

        The model defined in huaweicloud sdk

        :param search_path_flag: 搜索路径标志，true表示开启，false表示关闭
        :type search_path_flag: bool
        """
        
        super().__init__()

        self._search_path_flag = None
        self.discriminator = None

        if search_path_flag is not None:
            self.search_path_flag = search_path_flag

    @property
    def search_path_flag(self):
        r"""Gets the search_path_flag of this ShowClouddbaGetSearchPathFlagNewResponse.

        搜索路径标志，true表示开启，false表示关闭

        :return: The search_path_flag of this ShowClouddbaGetSearchPathFlagNewResponse.
        :rtype: bool
        """
        return self._search_path_flag

    @search_path_flag.setter
    def search_path_flag(self, search_path_flag):
        r"""Sets the search_path_flag of this ShowClouddbaGetSearchPathFlagNewResponse.

        搜索路径标志，true表示开启，false表示关闭

        :param search_path_flag: The search_path_flag of this ShowClouddbaGetSearchPathFlagNewResponse.
        :type search_path_flag: bool
        """
        self._search_path_flag = search_path_flag

    def to_dict(self):
        import warnings
        warnings.warn("ShowClouddbaGetSearchPathFlagNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowClouddbaGetSearchPathFlagNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
