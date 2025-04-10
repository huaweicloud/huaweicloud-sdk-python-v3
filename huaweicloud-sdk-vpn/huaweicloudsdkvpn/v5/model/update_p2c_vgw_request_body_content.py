# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateP2cVgwRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'eip_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'eip_id': 'eip_id'
    }

    def __init__(self, name=None, eip_id=None):
        r"""UpdateP2cVgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线
        :type name: str
        :param eip_id: eip的ID。用于给P2C VPN网关绑定新的EIP，需要先解绑当前的EIP
        :type eip_id: str
        """
        
        

        self._name = None
        self._eip_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if eip_id is not None:
            self.eip_id = eip_id

    @property
    def name(self):
        r"""Gets the name of this UpdateP2cVgwRequestBodyContent.

        P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线

        :return: The name of this UpdateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateP2cVgwRequestBodyContent.

        P2C VPN网关名称。1-64字符，中文、英文、数字包含下划线

        :param name: The name of this UpdateP2cVgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def eip_id(self):
        r"""Gets the eip_id of this UpdateP2cVgwRequestBodyContent.

        eip的ID。用于给P2C VPN网关绑定新的EIP，需要先解绑当前的EIP

        :return: The eip_id of this UpdateP2cVgwRequestBodyContent.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        r"""Sets the eip_id of this UpdateP2cVgwRequestBodyContent.

        eip的ID。用于给P2C VPN网关绑定新的EIP，需要先解绑当前的EIP

        :param eip_id: The eip_id of this UpdateP2cVgwRequestBodyContent.
        :type eip_id: str
        """
        self._eip_id = eip_id

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
        if not isinstance(other, UpdateP2cVgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
