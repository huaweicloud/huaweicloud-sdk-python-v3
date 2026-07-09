# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSwitchConfigInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_info': 'SwitchInfo',
        'version_info': 'VersionInfo'
    }

    attribute_map = {
        'switch_info': 'switch_info',
        'version_info': 'version_info'
    }

    def __init__(self, switch_info=None, version_info=None):
        r"""ListSwitchConfigInfoResponse

        The model defined in huaweicloud sdk

        :param switch_info: 
        :type switch_info: :class:`huaweicloudsdkcbh.v2.SwitchInfo`
        :param version_info: 
        :type version_info: :class:`huaweicloudsdkcbh.v2.VersionInfo`
        """
        
        super().__init__()

        self._switch_info = None
        self._version_info = None
        self.discriminator = None

        if switch_info is not None:
            self.switch_info = switch_info
        if version_info is not None:
            self.version_info = version_info

    @property
    def switch_info(self):
        r"""Gets the switch_info of this ListSwitchConfigInfoResponse.

        :return: The switch_info of this ListSwitchConfigInfoResponse.
        :rtype: :class:`huaweicloudsdkcbh.v2.SwitchInfo`
        """
        return self._switch_info

    @switch_info.setter
    def switch_info(self, switch_info):
        r"""Sets the switch_info of this ListSwitchConfigInfoResponse.

        :param switch_info: The switch_info of this ListSwitchConfigInfoResponse.
        :type switch_info: :class:`huaweicloudsdkcbh.v2.SwitchInfo`
        """
        self._switch_info = switch_info

    @property
    def version_info(self):
        r"""Gets the version_info of this ListSwitchConfigInfoResponse.

        :return: The version_info of this ListSwitchConfigInfoResponse.
        :rtype: :class:`huaweicloudsdkcbh.v2.VersionInfo`
        """
        return self._version_info

    @version_info.setter
    def version_info(self, version_info):
        r"""Sets the version_info of this ListSwitchConfigInfoResponse.

        :param version_info: The version_info of this ListSwitchConfigInfoResponse.
        :type version_info: :class:`huaweicloudsdkcbh.v2.VersionInfo`
        """
        self._version_info = version_info

    def to_dict(self):
        import warnings
        warnings.warn("ListSwitchConfigInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSwitchConfigInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
