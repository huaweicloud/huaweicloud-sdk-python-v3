# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gcb_id': 'str',
        'size': 'int',
        'gcb_type': 'str',
        'admin_state': 'str',
        'sla_level': 'str',
        'dscp': 'int'
    }

    attribute_map = {
        'gcb_id': 'gcb_id',
        'size': 'size',
        'gcb_type': 'gcb_type',
        'admin_state': 'admin_state',
        'sla_level': 'sla_level',
        'dscp': 'dscp'
    }

    def __init__(self, gcb_id=None, size=None, gcb_type=None, admin_state=None, sla_level=None, dscp=None):
        """GlobalConnectionBandwidthInfo

        The model defined in huaweicloud sdk

        :param gcb_id: 骨干带宽的ID
        :type gcb_id: str
        :param size: 骨干带宽的大小
        :type size: int
        :param gcb_type: 骨干带宽类型（城域、区域和大区）
        :type gcb_type: str
        :param admin_state: - 功能说明：骨干带宽状态 - 取值范围：NORMAL 正常、FREEZED 冻结
        :type admin_state: str
        :param sla_level: - 功能说明：网络服务等级 - 取值范围：Pt - 铂金，Au - 金牌，Ag - 银牌，Cu - 铜牌
        :type sla_level: str
        :param dscp: 线路质量金银铜对应的DSCP值
        :type dscp: int
        """
        
        

        self._gcb_id = None
        self._size = None
        self._gcb_type = None
        self._admin_state = None
        self._sla_level = None
        self._dscp = None
        self.discriminator = None

        if gcb_id is not None:
            self.gcb_id = gcb_id
        if size is not None:
            self.size = size
        if gcb_type is not None:
            self.gcb_type = gcb_type
        if admin_state is not None:
            self.admin_state = admin_state
        if sla_level is not None:
            self.sla_level = sla_level
        if dscp is not None:
            self.dscp = dscp

    @property
    def gcb_id(self):
        """Gets the gcb_id of this GlobalConnectionBandwidthInfo.

        骨干带宽的ID

        :return: The gcb_id of this GlobalConnectionBandwidthInfo.
        :rtype: str
        """
        return self._gcb_id

    @gcb_id.setter
    def gcb_id(self, gcb_id):
        """Sets the gcb_id of this GlobalConnectionBandwidthInfo.

        骨干带宽的ID

        :param gcb_id: The gcb_id of this GlobalConnectionBandwidthInfo.
        :type gcb_id: str
        """
        self._gcb_id = gcb_id

    @property
    def size(self):
        """Gets the size of this GlobalConnectionBandwidthInfo.

        骨干带宽的大小

        :return: The size of this GlobalConnectionBandwidthInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GlobalConnectionBandwidthInfo.

        骨干带宽的大小

        :param size: The size of this GlobalConnectionBandwidthInfo.
        :type size: int
        """
        self._size = size

    @property
    def gcb_type(self):
        """Gets the gcb_type of this GlobalConnectionBandwidthInfo.

        骨干带宽类型（城域、区域和大区）

        :return: The gcb_type of this GlobalConnectionBandwidthInfo.
        :rtype: str
        """
        return self._gcb_type

    @gcb_type.setter
    def gcb_type(self, gcb_type):
        """Sets the gcb_type of this GlobalConnectionBandwidthInfo.

        骨干带宽类型（城域、区域和大区）

        :param gcb_type: The gcb_type of this GlobalConnectionBandwidthInfo.
        :type gcb_type: str
        """
        self._gcb_type = gcb_type

    @property
    def admin_state(self):
        """Gets the admin_state of this GlobalConnectionBandwidthInfo.

        - 功能说明：骨干带宽状态 - 取值范围：NORMAL 正常、FREEZED 冻结

        :return: The admin_state of this GlobalConnectionBandwidthInfo.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this GlobalConnectionBandwidthInfo.

        - 功能说明：骨干带宽状态 - 取值范围：NORMAL 正常、FREEZED 冻结

        :param admin_state: The admin_state of this GlobalConnectionBandwidthInfo.
        :type admin_state: str
        """
        self._admin_state = admin_state

    @property
    def sla_level(self):
        """Gets the sla_level of this GlobalConnectionBandwidthInfo.

        - 功能说明：网络服务等级 - 取值范围：Pt - 铂金，Au - 金牌，Ag - 银牌，Cu - 铜牌

        :return: The sla_level of this GlobalConnectionBandwidthInfo.
        :rtype: str
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        """Sets the sla_level of this GlobalConnectionBandwidthInfo.

        - 功能说明：网络服务等级 - 取值范围：Pt - 铂金，Au - 金牌，Ag - 银牌，Cu - 铜牌

        :param sla_level: The sla_level of this GlobalConnectionBandwidthInfo.
        :type sla_level: str
        """
        self._sla_level = sla_level

    @property
    def dscp(self):
        """Gets the dscp of this GlobalConnectionBandwidthInfo.

        线路质量金银铜对应的DSCP值

        :return: The dscp of this GlobalConnectionBandwidthInfo.
        :rtype: int
        """
        return self._dscp

    @dscp.setter
    def dscp(self, dscp):
        """Sets the dscp of this GlobalConnectionBandwidthInfo.

        线路质量金银铜对应的DSCP值

        :param dscp: The dscp of this GlobalConnectionBandwidthInfo.
        :type dscp: int
        """
        self._dscp = dscp

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
        if not isinstance(other, GlobalConnectionBandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
