# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopPoolVolumesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'handle_type': 'str',
        'desktop_ids': 'list[str]',
        'volumes': 'list[ExpandDesktopPoolVolumesReqVolumes]'
    }

    attribute_map = {
        'handle_type': 'handle_type',
        'desktop_ids': 'desktop_ids',
        'volumes': 'volumes'
    }

    def __init__(self, handle_type=None, desktop_ids=None, volumes=None):
        r"""ExpandDesktopPoolVolumesReq

        The model defined in huaweicloud sdk

        :param handle_type: 处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效
        :type handle_type: str
        :param desktop_ids: 桌面id
        :type desktop_ids: list[str]
        :param volumes: 扩容的桌面池磁盘列表。
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolVolumesReqVolumes`]
        """
        
        

        self._handle_type = None
        self._desktop_ids = None
        self._volumes = None
        self.discriminator = None

        if handle_type is not None:
            self.handle_type = handle_type
        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if volumes is not None:
            self.volumes = volumes

    @property
    def handle_type(self):
        r"""Gets the handle_type of this ExpandDesktopPoolVolumesReq.

        处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效

        :return: The handle_type of this ExpandDesktopPoolVolumesReq.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this ExpandDesktopPoolVolumesReq.

        处理类型 - ONLY_FOR_EXPAND：仅对新扩容桌面生效 - FOR_EXPAND_AND_IDLE：对新扩容桌面与空闲桌面生效 - FOR_EXPAND_AND_ALL：对新扩容桌面与已有全部桌面生效

        :param handle_type: The handle_type of this ExpandDesktopPoolVolumesReq.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this ExpandDesktopPoolVolumesReq.

        桌面id

        :return: The desktop_ids of this ExpandDesktopPoolVolumesReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this ExpandDesktopPoolVolumesReq.

        桌面id

        :param desktop_ids: The desktop_ids of this ExpandDesktopPoolVolumesReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def volumes(self):
        r"""Gets the volumes of this ExpandDesktopPoolVolumesReq.

        扩容的桌面池磁盘列表。

        :return: The volumes of this ExpandDesktopPoolVolumesReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolVolumesReqVolumes`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this ExpandDesktopPoolVolumesReq.

        扩容的桌面池磁盘列表。

        :param volumes: The volumes of this ExpandDesktopPoolVolumesReq.
        :type volumes: list[:class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolVolumesReqVolumes`]
        """
        self._volumes = volumes

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
        if not isinstance(other, ExpandDesktopPoolVolumesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
