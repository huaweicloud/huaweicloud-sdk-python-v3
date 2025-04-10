# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_reserve_gcb': 'bool',
        'global_eip_id': 'str'
    }

    attribute_map = {
        'is_reserve_gcb': 'is_reserve_gcb',
        'global_eip_id': 'global_eip_id'
    }

    def __init__(self, is_reserve_gcb=None, global_eip_id=None):
        r"""DisassociateInstanceRequest

        The model defined in huaweicloud sdk

        :param is_reserve_gcb: 解绑实例后是否保留GCB，false表示解绑实例后会同时删除GCB
        :type is_reserve_gcb: bool
        :param global_eip_id: 
        :type global_eip_id: str
        """
        
        

        self._is_reserve_gcb = None
        self._global_eip_id = None
        self.discriminator = None

        self.is_reserve_gcb = is_reserve_gcb
        self.global_eip_id = global_eip_id

    @property
    def is_reserve_gcb(self):
        r"""Gets the is_reserve_gcb of this DisassociateInstanceRequest.

        解绑实例后是否保留GCB，false表示解绑实例后会同时删除GCB

        :return: The is_reserve_gcb of this DisassociateInstanceRequest.
        :rtype: bool
        """
        return self._is_reserve_gcb

    @is_reserve_gcb.setter
    def is_reserve_gcb(self, is_reserve_gcb):
        r"""Sets the is_reserve_gcb of this DisassociateInstanceRequest.

        解绑实例后是否保留GCB，false表示解绑实例后会同时删除GCB

        :param is_reserve_gcb: The is_reserve_gcb of this DisassociateInstanceRequest.
        :type is_reserve_gcb: bool
        """
        self._is_reserve_gcb = is_reserve_gcb

    @property
    def global_eip_id(self):
        r"""Gets the global_eip_id of this DisassociateInstanceRequest.

        :return: The global_eip_id of this DisassociateInstanceRequest.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        r"""Sets the global_eip_id of this DisassociateInstanceRequest.

        :param global_eip_id: The global_eip_id of this DisassociateInstanceRequest.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

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
        if not isinstance(other, DisassociateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
