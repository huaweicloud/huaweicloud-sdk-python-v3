# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopsVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expand_volumes_req': 'list[ExpandVolumesReq]'
    }

    attribute_map = {
        'expand_volumes_req': 'expandVolumesReq'
    }

    def __init__(self, expand_volumes_req=None):
        """ExpandDesktopsVolumesReq

        The model defined in huaweicloud sdk

        :param expand_volumes_req: 扩容磁盘参数。
        :type expand_volumes_req: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        
        

        self._expand_volumes_req = None
        self.discriminator = None

        if expand_volumes_req is not None:
            self.expand_volumes_req = expand_volumes_req

    @property
    def expand_volumes_req(self):
        """Gets the expand_volumes_req of this ExpandDesktopsVolumesReq.

        扩容磁盘参数。

        :return: The expand_volumes_req of this ExpandDesktopsVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        return self._expand_volumes_req

    @expand_volumes_req.setter
    def expand_volumes_req(self, expand_volumes_req):
        """Sets the expand_volumes_req of this ExpandDesktopsVolumesReq.

        扩容磁盘参数。

        :param expand_volumes_req: The expand_volumes_req of this ExpandDesktopsVolumesReq.
        :type expand_volumes_req: list[:class:`huaweicloudsdkworkspace.v2.ExpandVolumesReq`]
        """
        self._expand_volumes_req = expand_volumes_req

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
        if not isinstance(other, ExpandDesktopsVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
