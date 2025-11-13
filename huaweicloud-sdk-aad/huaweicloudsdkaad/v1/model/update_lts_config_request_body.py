# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLtsConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'lts_id_info': 'UpdateLtsConfigRequestBodyLtsIdInfo'
    }

    attribute_map = {
        'enabled': 'enabled',
        'lts_id_info': 'lts_id_info'
    }

    def __init__(self, enabled=None, lts_id_info=None):
        r"""UpdateLtsConfigRequestBody

        The model defined in huaweicloud sdk

        :param enabled: 日志配置开关
        :type enabled: bool
        :param lts_id_info: 
        :type lts_id_info: :class:`huaweicloudsdkaad.v1.UpdateLtsConfigRequestBodyLtsIdInfo`
        """
        
        

        self._enabled = None
        self._lts_id_info = None
        self.discriminator = None

        self.enabled = enabled
        if lts_id_info is not None:
            self.lts_id_info = lts_id_info

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateLtsConfigRequestBody.

        日志配置开关

        :return: The enabled of this UpdateLtsConfigRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateLtsConfigRequestBody.

        日志配置开关

        :param enabled: The enabled of this UpdateLtsConfigRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def lts_id_info(self):
        r"""Gets the lts_id_info of this UpdateLtsConfigRequestBody.

        :return: The lts_id_info of this UpdateLtsConfigRequestBody.
        :rtype: :class:`huaweicloudsdkaad.v1.UpdateLtsConfigRequestBodyLtsIdInfo`
        """
        return self._lts_id_info

    @lts_id_info.setter
    def lts_id_info(self, lts_id_info):
        r"""Sets the lts_id_info of this UpdateLtsConfigRequestBody.

        :param lts_id_info: The lts_id_info of this UpdateLtsConfigRequestBody.
        :type lts_id_info: :class:`huaweicloudsdkaad.v1.UpdateLtsConfigRequestBodyLtsIdInfo`
        """
        self._lts_id_info = lts_id_info

    def to_dict(self):
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
        if not isinstance(other, UpdateLtsConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
