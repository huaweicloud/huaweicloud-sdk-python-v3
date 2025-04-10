# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetBandwidthDetail:

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
        'bandwidth_name': 'str',
        'charge_mode': 'str',
        'size': 'int',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'str',
        'order_id': 'str',
        'status': 'str',
        'control_mode': 'str'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name',
        'charge_mode': 'charge_mode',
        'size': 'size',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'order_id': 'order_id',
        'status': 'status',
        'control_mode': 'control_mode'
    }

    def __init__(self, bandwidth_id=None, bandwidth_name=None, charge_mode=None, size=None, vpc_id=None, vpc_name=None, subnet_id=None, subnet_name=None, enterprise_project_id=None, created_at=None, order_id=None, status=None, control_mode=None):
        r"""SubnetBandwidthDetail

        The model defined in huaweicloud sdk

        :param bandwidth_id: 云办公带宽id。
        :type bandwidth_id: str
        :param bandwidth_name: 云办公带宽名称。
        :type bandwidth_name: str
        :param charge_mode: 云办公带宽计费方式。
        :type charge_mode: str
        :param size: 云办公带宽大小。
        :type size: int
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param vpc_name: VPC名称。
        :type vpc_name: str
        :param subnet_id: 子网 ID。
        :type subnet_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param order_id: 订单id。
        :type order_id: str
        :param status: 状态。 - CREATING：创建中。 - ACTIVE：使用中。 - INACTIVE：已停用。 - UPDATING：更新中。 - DELETING：删除中。
        :type status: str
        :param control_mode: 状态。 - BLACK：黑名单管控模式。 - WHITE：白名单管控模式。
        :type control_mode: str
        """
        
        

        self._bandwidth_id = None
        self._bandwidth_name = None
        self._charge_mode = None
        self._size = None
        self._vpc_id = None
        self._vpc_name = None
        self._subnet_id = None
        self._subnet_name = None
        self._enterprise_project_id = None
        self._created_at = None
        self._order_id = None
        self._status = None
        self._control_mode = None
        self.discriminator = None

        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if size is not None:
            self.size = size
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if created_at is not None:
            self.created_at = created_at
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if control_mode is not None:
            self.control_mode = control_mode

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this SubnetBandwidthDetail.

        云办公带宽id。

        :return: The bandwidth_id of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this SubnetBandwidthDetail.

        云办公带宽id。

        :param bandwidth_id: The bandwidth_id of this SubnetBandwidthDetail.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        r"""Gets the bandwidth_name of this SubnetBandwidthDetail.

        云办公带宽名称。

        :return: The bandwidth_name of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        r"""Sets the bandwidth_name of this SubnetBandwidthDetail.

        云办公带宽名称。

        :param bandwidth_name: The bandwidth_name of this SubnetBandwidthDetail.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this SubnetBandwidthDetail.

        云办公带宽计费方式。

        :return: The charge_mode of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this SubnetBandwidthDetail.

        云办公带宽计费方式。

        :param charge_mode: The charge_mode of this SubnetBandwidthDetail.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def size(self):
        r"""Gets the size of this SubnetBandwidthDetail.

        云办公带宽大小。

        :return: The size of this SubnetBandwidthDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SubnetBandwidthDetail.

        云办公带宽大小。

        :param size: The size of this SubnetBandwidthDetail.
        :type size: int
        """
        self._size = size

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this SubnetBandwidthDetail.

        VPC ID。

        :return: The vpc_id of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this SubnetBandwidthDetail.

        VPC ID。

        :param vpc_id: The vpc_id of this SubnetBandwidthDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this SubnetBandwidthDetail.

        VPC名称。

        :return: The vpc_name of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this SubnetBandwidthDetail.

        VPC名称。

        :param vpc_name: The vpc_name of this SubnetBandwidthDetail.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this SubnetBandwidthDetail.

        子网 ID。

        :return: The subnet_id of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this SubnetBandwidthDetail.

        子网 ID。

        :param subnet_id: The subnet_id of this SubnetBandwidthDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this SubnetBandwidthDetail.

        子网名称。

        :return: The subnet_name of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this SubnetBandwidthDetail.

        子网名称。

        :param subnet_name: The subnet_name of this SubnetBandwidthDetail.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SubnetBandwidthDetail.

        企业项目ID。

        :return: The enterprise_project_id of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SubnetBandwidthDetail.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SubnetBandwidthDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this SubnetBandwidthDetail.

        创建时间。

        :return: The created_at of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SubnetBandwidthDetail.

        创建时间。

        :param created_at: The created_at of this SubnetBandwidthDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def order_id(self):
        r"""Gets the order_id of this SubnetBandwidthDetail.

        订单id。

        :return: The order_id of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this SubnetBandwidthDetail.

        订单id。

        :param order_id: The order_id of this SubnetBandwidthDetail.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def status(self):
        r"""Gets the status of this SubnetBandwidthDetail.

        状态。 - CREATING：创建中。 - ACTIVE：使用中。 - INACTIVE：已停用。 - UPDATING：更新中。 - DELETING：删除中。

        :return: The status of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubnetBandwidthDetail.

        状态。 - CREATING：创建中。 - ACTIVE：使用中。 - INACTIVE：已停用。 - UPDATING：更新中。 - DELETING：删除中。

        :param status: The status of this SubnetBandwidthDetail.
        :type status: str
        """
        self._status = status

    @property
    def control_mode(self):
        r"""Gets the control_mode of this SubnetBandwidthDetail.

        状态。 - BLACK：黑名单管控模式。 - WHITE：白名单管控模式。

        :return: The control_mode of this SubnetBandwidthDetail.
        :rtype: str
        """
        return self._control_mode

    @control_mode.setter
    def control_mode(self, control_mode):
        r"""Sets the control_mode of this SubnetBandwidthDetail.

        状态。 - BLACK：黑名单管控模式。 - WHITE：白名单管控模式。

        :param control_mode: The control_mode of this SubnetBandwidthDetail.
        :type control_mode: str
        """
        self._control_mode = control_mode

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
        if not isinstance(other, SubnetBandwidthDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
