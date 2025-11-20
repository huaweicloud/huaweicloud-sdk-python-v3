# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindVportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vport': 'Vport'
    }

    attribute_map = {
        'vport': 'vport'
    }

    def __init__(self, vport=None):
        r"""UnbindVportRequestBody

        The model defined in huaweicloud sdk

        :param vport: 
        :type vport: :class:`huaweicloudsdkesw.v3.Vport`
        """
        
        

        self._vport = None
        self.discriminator = None

        self.vport = vport

    @property
    def vport(self):
        r"""Gets the vport of this UnbindVportRequestBody.

        :return: The vport of this UnbindVportRequestBody.
        :rtype: :class:`huaweicloudsdkesw.v3.Vport`
        """
        return self._vport

    @vport.setter
    def vport(self, vport):
        r"""Sets the vport of this UnbindVportRequestBody.

        :param vport: The vport of this UnbindVportRequestBody.
        :type vport: :class:`huaweicloudsdkesw.v3.Vport`
        """
        self._vport = vport

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
        if not isinstance(other, UnbindVportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
