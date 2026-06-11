# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHotClodSeparationStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opened': 'bool'
    }

    attribute_map = {
        'opened': 'opened'
    }

    def __init__(self, opened=None):
        r"""ShowHotClodSeparationStatusResponse

        The model defined in huaweicloud sdk

        :param opened: 功能是否开启
        :type opened: bool
        """
        
        super().__init__()

        self._opened = None
        self.discriminator = None

        if opened is not None:
            self.opened = opened

    @property
    def opened(self):
        r"""Gets the opened of this ShowHotClodSeparationStatusResponse.

        功能是否开启

        :return: The opened of this ShowHotClodSeparationStatusResponse.
        :rtype: bool
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        r"""Sets the opened of this ShowHotClodSeparationStatusResponse.

        功能是否开启

        :param opened: The opened of this ShowHotClodSeparationStatusResponse.
        :type opened: bool
        """
        self._opened = opened

    def to_dict(self):
        import warnings
        warnings.warn("ShowHotClodSeparationStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowHotClodSeparationStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
