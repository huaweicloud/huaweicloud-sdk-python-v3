# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubnetBandwidthControlListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_id': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'user_name': 'str',
        'control_mode': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'user_name': 'user_name',
        'control_mode': 'control_mode',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, bandwidth_id=None, desktop_id=None, desktop_name=None, user_name=None, control_mode=None, offset=None, limit=None):
        r"""ShowSubnetBandwidthControlListRequest

        The model defined in huaweicloud sdk

        :param bandwidth_id: 云办公带宽id。
        :type bandwidth_id: str
        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param user_name: 桌面分配用户。
        :type user_name: str
        :param control_mode: 控制模式，支持： - BLACK 黑名单 - WHITE 白名单
        :type control_mode: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。
        :type limit: int
        """
        
        

        self._bandwidth_id = None
        self._desktop_id = None
        self._desktop_name = None
        self._user_name = None
        self._control_mode = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.bandwidth_id = bandwidth_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if user_name is not None:
            self.user_name = user_name
        if control_mode is not None:
            self.control_mode = control_mode
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this ShowSubnetBandwidthControlListRequest.

        云办公带宽id。

        :return: The bandwidth_id of this ShowSubnetBandwidthControlListRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this ShowSubnetBandwidthControlListRequest.

        云办公带宽id。

        :param bandwidth_id: The bandwidth_id of this ShowSubnetBandwidthControlListRequest.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ShowSubnetBandwidthControlListRequest.

        桌面id。

        :return: The desktop_id of this ShowSubnetBandwidthControlListRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ShowSubnetBandwidthControlListRequest.

        桌面id。

        :param desktop_id: The desktop_id of this ShowSubnetBandwidthControlListRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ShowSubnetBandwidthControlListRequest.

        桌面名称。

        :return: The desktop_name of this ShowSubnetBandwidthControlListRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ShowSubnetBandwidthControlListRequest.

        桌面名称。

        :param desktop_name: The desktop_name of this ShowSubnetBandwidthControlListRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowSubnetBandwidthControlListRequest.

        桌面分配用户。

        :return: The user_name of this ShowSubnetBandwidthControlListRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowSubnetBandwidthControlListRequest.

        桌面分配用户。

        :param user_name: The user_name of this ShowSubnetBandwidthControlListRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def control_mode(self):
        r"""Gets the control_mode of this ShowSubnetBandwidthControlListRequest.

        控制模式，支持： - BLACK 黑名单 - WHITE 白名单

        :return: The control_mode of this ShowSubnetBandwidthControlListRequest.
        :rtype: str
        """
        return self._control_mode

    @control_mode.setter
    def control_mode(self, control_mode):
        r"""Sets the control_mode of this ShowSubnetBandwidthControlListRequest.

        控制模式，支持： - BLACK 黑名单 - WHITE 白名单

        :param control_mode: The control_mode of this ShowSubnetBandwidthControlListRequest.
        :type control_mode: str
        """
        self._control_mode = control_mode

    @property
    def offset(self):
        r"""Gets the offset of this ShowSubnetBandwidthControlListRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ShowSubnetBandwidthControlListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSubnetBandwidthControlListRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ShowSubnetBandwidthControlListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowSubnetBandwidthControlListRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :return: The limit of this ShowSubnetBandwidthControlListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSubnetBandwidthControlListRequest.

        用于分页查询，返回桌面数量限制。如果不指定，则返回所有符合条件的记录。

        :param limit: The limit of this ShowSubnetBandwidthControlListRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowSubnetBandwidthControlListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
