# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateDesktopsEipReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_id': 'str',
        'desktop_id': 'str'
    }

    attribute_map = {
        'eip_id': 'eip_id',
        'desktop_id': 'desktop_id'
    }

    def __init__(self, eip_id=None, desktop_id=None):
        """AssociateDesktopsEipReq

        The model defined in huaweicloud sdk

        :param eip_id: 桌面绑定的Eip的id。
        :type eip_id: str
        :param desktop_id: 桌面id。
        :type desktop_id: str
        """
        
        

        self._eip_id = None
        self._desktop_id = None
        self.discriminator = None

        self.eip_id = eip_id
        self.desktop_id = desktop_id

    @property
    def eip_id(self):
        """Gets the eip_id of this AssociateDesktopsEipReq.

        桌面绑定的Eip的id。

        :return: The eip_id of this AssociateDesktopsEipReq.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this AssociateDesktopsEipReq.

        桌面绑定的Eip的id。

        :param eip_id: The eip_id of this AssociateDesktopsEipReq.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def desktop_id(self):
        """Gets the desktop_id of this AssociateDesktopsEipReq.

        桌面id。

        :return: The desktop_id of this AssociateDesktopsEipReq.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this AssociateDesktopsEipReq.

        桌面id。

        :param desktop_id: The desktop_id of this AssociateDesktopsEipReq.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

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
        if not isinstance(other, AssociateDesktopsEipReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
