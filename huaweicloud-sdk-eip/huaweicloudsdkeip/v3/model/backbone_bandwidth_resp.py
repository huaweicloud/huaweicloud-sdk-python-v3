# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackboneBandwidthResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'admin_status': 'str',
        'size': 'int',
        'short_id': 'str',
        'sla_level': 'str',
        'dscp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'admin_status': 'admin_status',
        'size': 'size',
        'short_id': 'short_id',
        'sla_level': 'sla_level',
        'dscp': 'dscp'
    }

    def __init__(self, id=None, admin_status=None, size=None, short_id=None, sla_level=None, dscp=None):
        r"""BackboneBandwidthResp

        The model defined in huaweicloud sdk

        :param id: 骨干带宽的uuid
        :type id: str
        :param admin_status: 骨干带宽的状态
        :type admin_status: str
        :param size: 骨干带宽的大小
        :type size: int
        :param short_id: 骨干带宽的short_id
        :type short_id: str
        :param sla_level: 描述网络等级，从高到低分为铂金、金、银、铜
        :type sla_level: str
        :param dscp: 线路质量金银铜对应的DSCP值
        :type dscp: int
        """
        
        

        self._id = None
        self._admin_status = None
        self._size = None
        self._short_id = None
        self._sla_level = None
        self._dscp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if admin_status is not None:
            self.admin_status = admin_status
        if size is not None:
            self.size = size
        if short_id is not None:
            self.short_id = short_id
        if sla_level is not None:
            self.sla_level = sla_level
        if dscp is not None:
            self.dscp = dscp

    @property
    def id(self):
        r"""Gets the id of this BackboneBandwidthResp.

        骨干带宽的uuid

        :return: The id of this BackboneBandwidthResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackboneBandwidthResp.

        骨干带宽的uuid

        :param id: The id of this BackboneBandwidthResp.
        :type id: str
        """
        self._id = id

    @property
    def admin_status(self):
        r"""Gets the admin_status of this BackboneBandwidthResp.

        骨干带宽的状态

        :return: The admin_status of this BackboneBandwidthResp.
        :rtype: str
        """
        return self._admin_status

    @admin_status.setter
    def admin_status(self, admin_status):
        r"""Sets the admin_status of this BackboneBandwidthResp.

        骨干带宽的状态

        :param admin_status: The admin_status of this BackboneBandwidthResp.
        :type admin_status: str
        """
        self._admin_status = admin_status

    @property
    def size(self):
        r"""Gets the size of this BackboneBandwidthResp.

        骨干带宽的大小

        :return: The size of this BackboneBandwidthResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackboneBandwidthResp.

        骨干带宽的大小

        :param size: The size of this BackboneBandwidthResp.
        :type size: int
        """
        self._size = size

    @property
    def short_id(self):
        r"""Gets the short_id of this BackboneBandwidthResp.

        骨干带宽的short_id

        :return: The short_id of this BackboneBandwidthResp.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        r"""Sets the short_id of this BackboneBandwidthResp.

        骨干带宽的short_id

        :param short_id: The short_id of this BackboneBandwidthResp.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def sla_level(self):
        r"""Gets the sla_level of this BackboneBandwidthResp.

        描述网络等级，从高到低分为铂金、金、银、铜

        :return: The sla_level of this BackboneBandwidthResp.
        :rtype: str
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        r"""Sets the sla_level of this BackboneBandwidthResp.

        描述网络等级，从高到低分为铂金、金、银、铜

        :param sla_level: The sla_level of this BackboneBandwidthResp.
        :type sla_level: str
        """
        self._sla_level = sla_level

    @property
    def dscp(self):
        r"""Gets the dscp of this BackboneBandwidthResp.

        线路质量金银铜对应的DSCP值

        :return: The dscp of this BackboneBandwidthResp.
        :rtype: int
        """
        return self._dscp

    @dscp.setter
    def dscp(self, dscp):
        r"""Sets the dscp of this BackboneBandwidthResp.

        线路质量金银铜对应的DSCP值

        :param dscp: The dscp of this BackboneBandwidthResp.
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
        if not isinstance(other, BackboneBandwidthResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
