# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'volumes': 'list[Volume]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'volumes': 'volumes'
    }

    def __init__(self, desktop_id=None, volumes=None):
        r"""AddVolumes

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID
        :type desktop_id: str
        :param volumes: 订单的磁盘信息列表
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        
        

        self._desktop_id = None
        self._volumes = None
        self.discriminator = None

        self.desktop_id = desktop_id
        self.volumes = volumes

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this AddVolumes.

        桌面ID

        :return: The desktop_id of this AddVolumes.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this AddVolumes.

        桌面ID

        :param desktop_id: The desktop_id of this AddVolumes.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def volumes(self):
        r"""Gets the volumes of this AddVolumes.

        订单的磁盘信息列表

        :return: The volumes of this AddVolumes.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this AddVolumes.

        订单的磁盘信息列表

        :param volumes: The volumes of this AddVolumes.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
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
        if not isinstance(other, AddVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
