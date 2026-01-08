# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachDesktopPoolsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_pool_id': 'str',
        'desktop_pool_name': 'str',
        'is_attached': 'bool'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_pool_name': 'desktop_pool_name',
        'is_attached': 'is_attached'
    }

    def __init__(self, desktop_pool_id=None, desktop_pool_name=None, is_attached=None):
        r"""AttachDesktopPoolsInfo

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池id
        :type desktop_pool_id: str
        :param desktop_pool_name: 桌面池名称
        :type desktop_pool_name: str
        :param is_attached: 是否分配了桌面
        :type is_attached: bool
        """
        
        

        self._desktop_pool_id = None
        self._desktop_pool_name = None
        self._is_attached = None
        self.discriminator = None

        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if desktop_pool_name is not None:
            self.desktop_pool_name = desktop_pool_name
        if is_attached is not None:
            self.is_attached = is_attached

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this AttachDesktopPoolsInfo.

        桌面池id

        :return: The desktop_pool_id of this AttachDesktopPoolsInfo.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this AttachDesktopPoolsInfo.

        桌面池id

        :param desktop_pool_id: The desktop_pool_id of this AttachDesktopPoolsInfo.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_pool_name(self):
        r"""Gets the desktop_pool_name of this AttachDesktopPoolsInfo.

        桌面池名称

        :return: The desktop_pool_name of this AttachDesktopPoolsInfo.
        :rtype: str
        """
        return self._desktop_pool_name

    @desktop_pool_name.setter
    def desktop_pool_name(self, desktop_pool_name):
        r"""Sets the desktop_pool_name of this AttachDesktopPoolsInfo.

        桌面池名称

        :param desktop_pool_name: The desktop_pool_name of this AttachDesktopPoolsInfo.
        :type desktop_pool_name: str
        """
        self._desktop_pool_name = desktop_pool_name

    @property
    def is_attached(self):
        r"""Gets the is_attached of this AttachDesktopPoolsInfo.

        是否分配了桌面

        :return: The is_attached of this AttachDesktopPoolsInfo.
        :rtype: bool
        """
        return self._is_attached

    @is_attached.setter
    def is_attached(self, is_attached):
        r"""Sets the is_attached of this AttachDesktopPoolsInfo.

        是否分配了桌面

        :param is_attached: The is_attached of this AttachDesktopPoolsInfo.
        :type is_attached: bool
        """
        self._is_attached = is_attached

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
        if not isinstance(other, AttachDesktopPoolsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
