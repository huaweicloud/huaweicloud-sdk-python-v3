# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDetachInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[DetachInstancesDesktopInfo]'
    }

    attribute_map = {
        'desktops': 'desktops'
    }

    def __init__(self, desktops=None):
        r"""BatchDetachInstancesReq

        The model defined in huaweicloud sdk

        :param desktops: 解绑的桌面信息列表。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.DetachInstancesDesktopInfo`]
        """
        
        

        self._desktops = None
        self.discriminator = None

        if desktops is not None:
            self.desktops = desktops

    @property
    def desktops(self):
        r"""Gets the desktops of this BatchDetachInstancesReq.

        解绑的桌面信息列表。

        :return: The desktops of this BatchDetachInstancesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DetachInstancesDesktopInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        r"""Sets the desktops of this BatchDetachInstancesReq.

        解绑的桌面信息列表。

        :param desktops: The desktops of this BatchDetachInstancesReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.DetachInstancesDesktopInfo`]
        """
        self._desktops = desktops

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
        if not isinstance(other, BatchDetachInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
