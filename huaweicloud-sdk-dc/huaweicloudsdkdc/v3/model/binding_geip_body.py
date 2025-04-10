# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindingGeipBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eip_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'global_eip_id': 'global_eip_id',
        'type': 'type'
    }

    def __init__(self, global_eip_id=None, type=None):
        r"""BindingGeipBody

        The model defined in huaweicloud sdk

        :param global_eip_id: 全局弹性公网IP的ID
        :type global_eip_id: str
        :param type: geip子网类型
        :type type: str
        """
        
        

        self._global_eip_id = None
        self._type = None
        self.discriminator = None

        self.global_eip_id = global_eip_id
        if type is not None:
            self.type = type

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this BindingGeipBody.

        全局弹性公网IP的ID

        :return: The global_eip_id of this BindingGeipBody.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this BindingGeipBody.

        全局弹性公网IP的ID

        :param global_eip_id: The global_eip_id of this BindingGeipBody.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def type(self):
        r"""Gets the type of this BindingGeipBody.

        geip子网类型

        :return: The type of this BindingGeipBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BindingGeipBody.

        geip子网类型

        :param type: The type of this BindingGeipBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BindingGeipBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
