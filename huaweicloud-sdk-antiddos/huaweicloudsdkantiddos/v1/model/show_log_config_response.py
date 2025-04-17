# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogConfigResponse(SdkResponse):

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
        'lts_id_info': 'LtsConfigRequestAndResponseLtsIdInfo'
    }

    attribute_map = {
        'enabled': 'enabled',
        'lts_id_info': 'lts_id_info'
    }

    def __init__(self, enabled=None, lts_id_info=None):
        r"""ShowLogConfigResponse

        The model defined in huaweicloud sdk

        :param enabled: 是否开启日志
        :type enabled: bool
        :param lts_id_info: 
        :type lts_id_info: :class:`huaweicloudsdkantiddos.v1.LtsConfigRequestAndResponseLtsIdInfo`
        """
        
        super(ShowLogConfigResponse, self).__init__()

        self._enabled = None
        self._lts_id_info = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if lts_id_info is not None:
            self.lts_id_info = lts_id_info

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowLogConfigResponse.

        是否开启日志

        :return: The enabled of this ShowLogConfigResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowLogConfigResponse.

        是否开启日志

        :param enabled: The enabled of this ShowLogConfigResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def lts_id_info(self):
        r"""Gets the lts_id_info of this ShowLogConfigResponse.

        :return: The lts_id_info of this ShowLogConfigResponse.
        :rtype: :class:`huaweicloudsdkantiddos.v1.LtsConfigRequestAndResponseLtsIdInfo`
        """
        return self._lts_id_info

    @lts_id_info.setter
    def lts_id_info(self, lts_id_info):
        r"""Sets the lts_id_info of this ShowLogConfigResponse.

        :param lts_id_info: The lts_id_info of this ShowLogConfigResponse.
        :type lts_id_info: :class:`huaweicloudsdkantiddos.v1.LtsConfigRequestAndResponseLtsIdInfo`
        """
        self._lts_id_info = lts_id_info

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
        if not isinstance(other, ShowLogConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
