# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetypeVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bss_param': 'BssParamForRetypeVolume',
        'os_retype': 'RetypeVolume'
    }

    attribute_map = {
        'bss_param': 'bssParam',
        'os_retype': 'os-retype'
    }

    def __init__(self, bss_param=None, os_retype=None):
        r"""RetypeVolumeRequestBody

        The model defined in huaweicloud sdk

        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkevs.v2.BssParamForRetypeVolume`
        :param os_retype: 
        :type os_retype: :class:`huaweicloudsdkevs.v2.RetypeVolume`
        """
        
        

        self._bss_param = None
        self._os_retype = None
        self.discriminator = None

        if bss_param is not None:
            self.bss_param = bss_param
        self.os_retype = os_retype

    @property
    def bss_param(self):
        r"""Gets the bss_param of this RetypeVolumeRequestBody.

        :return: The bss_param of this RetypeVolumeRequestBody.
        :rtype: :class:`huaweicloudsdkevs.v2.BssParamForRetypeVolume`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        r"""Sets the bss_param of this RetypeVolumeRequestBody.

        :param bss_param: The bss_param of this RetypeVolumeRequestBody.
        :type bss_param: :class:`huaweicloudsdkevs.v2.BssParamForRetypeVolume`
        """
        self._bss_param = bss_param

    @property
    def os_retype(self):
        r"""Gets the os_retype of this RetypeVolumeRequestBody.

        :return: The os_retype of this RetypeVolumeRequestBody.
        :rtype: :class:`huaweicloudsdkevs.v2.RetypeVolume`
        """
        return self._os_retype

    @os_retype.setter
    def os_retype(self, os_retype):
        r"""Sets the os_retype of this RetypeVolumeRequestBody.

        :param os_retype: The os_retype of this RetypeVolumeRequestBody.
        :type os_retype: :class:`huaweicloudsdkevs.v2.RetypeVolume`
        """
        self._os_retype = os_retype

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
        if not isinstance(other, RetypeVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
