# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssessResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'speed': 'AssessProperty',
        'sound': 'AssessProperty',
        'snr': 'AssessProperty',
        'reverb': 'AssessProperty',
        'dnsmos_ovrl': 'AssessProperty',
        'dnsmos_bak': 'AssessProperty',
        'suggestion': 'str'
    }

    attribute_map = {
        'speed': 'speed',
        'sound': 'sound',
        'snr': 'snr',
        'reverb': 'reverb',
        'dnsmos_ovrl': 'dnsmos_ovrl',
        'dnsmos_bak': 'dnsmos_bak',
        'suggestion': 'suggestion'
    }

    def __init__(self, speed=None, sound=None, snr=None, reverb=None, dnsmos_ovrl=None, dnsmos_bak=None, suggestion=None):
        r"""AssessResult

        The model defined in huaweicloud sdk

        :param speed: 
        :type speed: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param sound: 
        :type sound: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param snr: 
        :type snr: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param reverb: 
        :type reverb: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param dnsmos_ovrl: 
        :type dnsmos_ovrl: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param dnsmos_bak: 
        :type dnsmos_bak: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        :param suggestion: 综合建议
        :type suggestion: str
        """
        
        

        self._speed = None
        self._sound = None
        self._snr = None
        self._reverb = None
        self._dnsmos_ovrl = None
        self._dnsmos_bak = None
        self._suggestion = None
        self.discriminator = None

        if speed is not None:
            self.speed = speed
        if sound is not None:
            self.sound = sound
        if snr is not None:
            self.snr = snr
        if reverb is not None:
            self.reverb = reverb
        if dnsmos_ovrl is not None:
            self.dnsmos_ovrl = dnsmos_ovrl
        if dnsmos_bak is not None:
            self.dnsmos_bak = dnsmos_bak
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def speed(self):
        r"""Gets the speed of this AssessResult.

        :return: The speed of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this AssessResult.

        :param speed: The speed of this AssessResult.
        :type speed: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._speed = speed

    @property
    def sound(self):
        r"""Gets the sound of this AssessResult.

        :return: The sound of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._sound

    @sound.setter
    def sound(self, sound):
        r"""Sets the sound of this AssessResult.

        :param sound: The sound of this AssessResult.
        :type sound: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._sound = sound

    @property
    def snr(self):
        r"""Gets the snr of this AssessResult.

        :return: The snr of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        r"""Sets the snr of this AssessResult.

        :param snr: The snr of this AssessResult.
        :type snr: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._snr = snr

    @property
    def reverb(self):
        r"""Gets the reverb of this AssessResult.

        :return: The reverb of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._reverb

    @reverb.setter
    def reverb(self, reverb):
        r"""Sets the reverb of this AssessResult.

        :param reverb: The reverb of this AssessResult.
        :type reverb: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._reverb = reverb

    @property
    def dnsmos_ovrl(self):
        r"""Gets the dnsmos_ovrl of this AssessResult.

        :return: The dnsmos_ovrl of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._dnsmos_ovrl

    @dnsmos_ovrl.setter
    def dnsmos_ovrl(self, dnsmos_ovrl):
        r"""Sets the dnsmos_ovrl of this AssessResult.

        :param dnsmos_ovrl: The dnsmos_ovrl of this AssessResult.
        :type dnsmos_ovrl: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._dnsmos_ovrl = dnsmos_ovrl

    @property
    def dnsmos_bak(self):
        r"""Gets the dnsmos_bak of this AssessResult.

        :return: The dnsmos_bak of this AssessResult.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        return self._dnsmos_bak

    @dnsmos_bak.setter
    def dnsmos_bak(self, dnsmos_bak):
        r"""Sets the dnsmos_bak of this AssessResult.

        :param dnsmos_bak: The dnsmos_bak of this AssessResult.
        :type dnsmos_bak: :class:`huaweicloudsdkmetastudio.v1.AssessProperty`
        """
        self._dnsmos_bak = dnsmos_bak

    @property
    def suggestion(self):
        r"""Gets the suggestion of this AssessResult.

        综合建议

        :return: The suggestion of this AssessResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this AssessResult.

        综合建议

        :param suggestion: The suggestion of this AssessResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

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
        if not isinstance(other, AssessResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
