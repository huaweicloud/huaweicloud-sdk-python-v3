# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMixJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mix_param': 'UpdateMixParam'
    }

    attribute_map = {
        'mix_param': 'mix_param'
    }

    def __init__(self, mix_param=None):
        """UpdateMixJobReq

        The model defined in huaweicloud sdk

        :param mix_param: 
        :type mix_param: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixParam`
        """
        
        

        self._mix_param = None
        self.discriminator = None

        self.mix_param = mix_param

    @property
    def mix_param(self):
        """Gets the mix_param of this UpdateMixJobReq.

        :return: The mix_param of this UpdateMixJobReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixParam`
        """
        return self._mix_param

    @mix_param.setter
    def mix_param(self, mix_param):
        """Sets the mix_param of this UpdateMixJobReq.

        :param mix_param: The mix_param of this UpdateMixJobReq.
        :type mix_param: :class:`huaweicloudsdkcloudrtc.v2.UpdateMixParam`
        """
        self._mix_param = mix_param

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
        if not isinstance(other, UpdateMixJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
