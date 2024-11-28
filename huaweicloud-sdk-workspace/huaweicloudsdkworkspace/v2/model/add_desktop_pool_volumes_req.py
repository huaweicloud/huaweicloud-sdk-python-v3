# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDesktopPoolVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'volumes': 'list[VolumeAddInfo]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'volumes': 'volumes'
    }

    def __init__(self, order_id=None, volumes=None):
        """AddDesktopPoolVolumesReq

        The model defined in huaweicloud sdk

        :param order_id: 包周期订购ID，CBC订购回调时使用。
        :type order_id: str
        :param volumes: 增加的磁盘列表。
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeAddInfo`]
        """
        
        

        self._order_id = None
        self._volumes = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if volumes is not None:
            self.volumes = volumes

    @property
    def order_id(self):
        """Gets the order_id of this AddDesktopPoolVolumesReq.

        包周期订购ID，CBC订购回调时使用。

        :return: The order_id of this AddDesktopPoolVolumesReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this AddDesktopPoolVolumesReq.

        包周期订购ID，CBC订购回调时使用。

        :param order_id: The order_id of this AddDesktopPoolVolumesReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def volumes(self):
        """Gets the volumes of this AddDesktopPoolVolumesReq.

        增加的磁盘列表。

        :return: The volumes of this AddDesktopPoolVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VolumeAddInfo`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AddDesktopPoolVolumesReq.

        增加的磁盘列表。

        :param volumes: The volumes of this AddDesktopPoolVolumesReq.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeAddInfo`]
        """
        self._volumes = volumes

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
        if not isinstance(other, AddDesktopPoolVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
