# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputingClusterRsp:

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
        'name': 'str',
        'version': 'str',
        'flavor': 'str',
        'category': 'str',
        'status': 'str',
        'active_nodes_number': 'int',
        'total_nodes_number': 'int',
        'create_time': 'str',
        'cce_create_time': 'str',
        'cce_status': 'str',
        'cce_id': 'str',
        'billing_mode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version': 'version',
        'flavor': 'flavor',
        'category': 'category',
        'status': 'status',
        'active_nodes_number': 'active_nodes_number',
        'total_nodes_number': 'total_nodes_number',
        'create_time': 'create_time',
        'cce_create_time': 'cce_create_time',
        'cce_status': 'cce_status',
        'cce_id': 'cce_id',
        'billing_mode': 'billing_mode'
    }

    def __init__(self, id=None, name=None, version=None, flavor=None, category=None, status=None, active_nodes_number=None, total_nodes_number=None, create_time=None, cce_create_time=None, cce_status=None, cce_id=None, billing_mode=None):
        r"""ComputingClusterRsp

        The model defined in huaweicloud sdk

        :param id: 已绑定的集群ID。
        :type id: str
        :param name: 计算集群名称。
        :type name: str
        :param version: 计算集群版本。
        :type version: str
        :param flavor: 计算集群规格。
        :type flavor: str
        :param category: 计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。
        :type category: str
        :param status: 计算集群绑定状态，支持RUNNING|INSTALL_FAILED|UNINSTALL_FAILED|INSTALLING|UNINSTALLING。
        :type status: str
        :param active_nodes_number: 计算集群可用节点数。
        :type active_nodes_number: int
        :param total_nodes_number: 计算集群总节点数。
        :type total_nodes_number: int
        :param create_time: 计算集群绑定时间。
        :type create_time: str
        :param cce_create_time: cce集群创建时间。
        :type cce_create_time: str
        :param cce_status: cce集群绑态。
        :type cce_status: str
        :param cce_id: cce集群ID。
        :type cce_id: str
        :param billing_mode: 计费模式，prepaid表示包周期，postpaid表示按需。
        :type billing_mode: str
        """
        
        

        self._id = None
        self._name = None
        self._version = None
        self._flavor = None
        self._category = None
        self._status = None
        self._active_nodes_number = None
        self._total_nodes_number = None
        self._create_time = None
        self._cce_create_time = None
        self._cce_status = None
        self._cce_id = None
        self._billing_mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if flavor is not None:
            self.flavor = flavor
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if active_nodes_number is not None:
            self.active_nodes_number = active_nodes_number
        if total_nodes_number is not None:
            self.total_nodes_number = total_nodes_number
        if create_time is not None:
            self.create_time = create_time
        if cce_create_time is not None:
            self.cce_create_time = cce_create_time
        if cce_status is not None:
            self.cce_status = cce_status
        if cce_id is not None:
            self.cce_id = cce_id
        if billing_mode is not None:
            self.billing_mode = billing_mode

    @property
    def id(self):
        r"""Gets the id of this ComputingClusterRsp.

        已绑定的集群ID。

        :return: The id of this ComputingClusterRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComputingClusterRsp.

        已绑定的集群ID。

        :param id: The id of this ComputingClusterRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ComputingClusterRsp.

        计算集群名称。

        :return: The name of this ComputingClusterRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComputingClusterRsp.

        计算集群名称。

        :param name: The name of this ComputingClusterRsp.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ComputingClusterRsp.

        计算集群版本。

        :return: The version of this ComputingClusterRsp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComputingClusterRsp.

        计算集群版本。

        :param version: The version of this ComputingClusterRsp.
        :type version: str
        """
        self._version = version

    @property
    def flavor(self):
        r"""Gets the flavor of this ComputingClusterRsp.

        计算集群规格。

        :return: The flavor of this ComputingClusterRsp.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ComputingClusterRsp.

        计算集群规格。

        :param flavor: The flavor of this ComputingClusterRsp.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def category(self):
        r"""Gets the category of this ComputingClusterRsp.

        计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。

        :return: The category of this ComputingClusterRsp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ComputingClusterRsp.

        计算集群类别。CCE代表CCE集群，Turbo代表CCE Turbo集群。

        :param category: The category of this ComputingClusterRsp.
        :type category: str
        """
        self._category = category

    @property
    def status(self):
        r"""Gets the status of this ComputingClusterRsp.

        计算集群绑定状态，支持RUNNING|INSTALL_FAILED|UNINSTALL_FAILED|INSTALLING|UNINSTALLING。

        :return: The status of this ComputingClusterRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ComputingClusterRsp.

        计算集群绑定状态，支持RUNNING|INSTALL_FAILED|UNINSTALL_FAILED|INSTALLING|UNINSTALLING。

        :param status: The status of this ComputingClusterRsp.
        :type status: str
        """
        self._status = status

    @property
    def active_nodes_number(self):
        r"""Gets the active_nodes_number of this ComputingClusterRsp.

        计算集群可用节点数。

        :return: The active_nodes_number of this ComputingClusterRsp.
        :rtype: int
        """
        return self._active_nodes_number

    @active_nodes_number.setter
    def active_nodes_number(self, active_nodes_number):
        r"""Sets the active_nodes_number of this ComputingClusterRsp.

        计算集群可用节点数。

        :param active_nodes_number: The active_nodes_number of this ComputingClusterRsp.
        :type active_nodes_number: int
        """
        self._active_nodes_number = active_nodes_number

    @property
    def total_nodes_number(self):
        r"""Gets the total_nodes_number of this ComputingClusterRsp.

        计算集群总节点数。

        :return: The total_nodes_number of this ComputingClusterRsp.
        :rtype: int
        """
        return self._total_nodes_number

    @total_nodes_number.setter
    def total_nodes_number(self, total_nodes_number):
        r"""Sets the total_nodes_number of this ComputingClusterRsp.

        计算集群总节点数。

        :param total_nodes_number: The total_nodes_number of this ComputingClusterRsp.
        :type total_nodes_number: int
        """
        self._total_nodes_number = total_nodes_number

    @property
    def create_time(self):
        r"""Gets the create_time of this ComputingClusterRsp.

        计算集群绑定时间。

        :return: The create_time of this ComputingClusterRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComputingClusterRsp.

        计算集群绑定时间。

        :param create_time: The create_time of this ComputingClusterRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def cce_create_time(self):
        r"""Gets the cce_create_time of this ComputingClusterRsp.

        cce集群创建时间。

        :return: The cce_create_time of this ComputingClusterRsp.
        :rtype: str
        """
        return self._cce_create_time

    @cce_create_time.setter
    def cce_create_time(self, cce_create_time):
        r"""Sets the cce_create_time of this ComputingClusterRsp.

        cce集群创建时间。

        :param cce_create_time: The cce_create_time of this ComputingClusterRsp.
        :type cce_create_time: str
        """
        self._cce_create_time = cce_create_time

    @property
    def cce_status(self):
        r"""Gets the cce_status of this ComputingClusterRsp.

        cce集群绑态。

        :return: The cce_status of this ComputingClusterRsp.
        :rtype: str
        """
        return self._cce_status

    @cce_status.setter
    def cce_status(self, cce_status):
        r"""Sets the cce_status of this ComputingClusterRsp.

        cce集群绑态。

        :param cce_status: The cce_status of this ComputingClusterRsp.
        :type cce_status: str
        """
        self._cce_status = cce_status

    @property
    def cce_id(self):
        r"""Gets the cce_id of this ComputingClusterRsp.

        cce集群ID。

        :return: The cce_id of this ComputingClusterRsp.
        :rtype: str
        """
        return self._cce_id

    @cce_id.setter
    def cce_id(self, cce_id):
        r"""Sets the cce_id of this ComputingClusterRsp.

        cce集群ID。

        :param cce_id: The cce_id of this ComputingClusterRsp.
        :type cce_id: str
        """
        self._cce_id = cce_id

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ComputingClusterRsp.

        计费模式，prepaid表示包周期，postpaid表示按需。

        :return: The billing_mode of this ComputingClusterRsp.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ComputingClusterRsp.

        计费模式，prepaid表示包周期，postpaid表示按需。

        :param billing_mode: The billing_mode of this ComputingClusterRsp.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

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
        if not isinstance(other, ComputingClusterRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
