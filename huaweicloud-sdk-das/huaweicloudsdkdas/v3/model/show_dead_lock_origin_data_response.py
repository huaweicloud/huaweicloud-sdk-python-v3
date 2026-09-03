# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockOriginDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_data': 'str'
    }

    attribute_map = {
        'origin_data': 'origin_data'
    }

    def __init__(self, origin_data=None):
        r"""ShowDeadLockOriginDataResponse

        The model defined in huaweicloud sdk

        :param origin_data: 原始数据
        :type origin_data: str
        """
        
        super().__init__()

        self._origin_data = None
        self.discriminator = None

        if origin_data is not None:
            self.origin_data = origin_data

    @property
    def origin_data(self):
        r"""Gets the origin_data of this ShowDeadLockOriginDataResponse.

        原始数据

        :return: The origin_data of this ShowDeadLockOriginDataResponse.
        :rtype: str
        """
        return self._origin_data

    @origin_data.setter
    def origin_data(self, origin_data):
        r"""Sets the origin_data of this ShowDeadLockOriginDataResponse.

        原始数据

        :param origin_data: The origin_data of this ShowDeadLockOriginDataResponse.
        :type origin_data: str
        """
        self._origin_data = origin_data

    def to_dict(self):
        import warnings
        warnings.warn("ShowDeadLockOriginDataResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDeadLockOriginDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
