# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckQuotaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'subscription_num': 'int',
        'disk_size': 'int',
        'disk_num': 'int',
        'is_period': 'bool',
        'deh_id': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'subscription_num': 'subscription_num',
        'disk_size': 'disk_size',
        'disk_num': 'disk_num',
        'is_period': 'is_period',
        'deh_id': 'deh_id',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, product_id=None, subscription_num=None, disk_size=None, disk_num=None, is_period=None, deh_id=None, cluster_id=None):
        """CheckQuotaRequest

        The model defined in huaweicloud sdk

        :param product_id: 产品id
        :type product_id: str
        :param subscription_num: 订单需要创建总实例数、订购数量
        :type subscription_num: int
        :param disk_size: 单台实例所需的磁盘大小（最大系统盘1块*1024、数据盘10块*32768）
        :type disk_size: int
        :param disk_num: 单台实例所需的磁盘数量（最大系统盘1块、数据盘10块）
        :type disk_num: int
        :param is_period: 是否包周期
        :type is_period: bool
        :param deh_id: 主机id
        :type deh_id: str
        :param cluster_id: 云专属分布式存储池id
        :type cluster_id: str
        """
        
        

        self._product_id = None
        self._subscription_num = None
        self._disk_size = None
        self._disk_num = None
        self._is_period = None
        self._deh_id = None
        self._cluster_id = None
        self.discriminator = None

        self.product_id = product_id
        self.subscription_num = subscription_num
        self.disk_size = disk_size
        self.disk_num = disk_num
        if is_period is not None:
            self.is_period = is_period
        if deh_id is not None:
            self.deh_id = deh_id
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def product_id(self):
        """Gets the product_id of this CheckQuotaRequest.

        产品id

        :return: The product_id of this CheckQuotaRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CheckQuotaRequest.

        产品id

        :param product_id: The product_id of this CheckQuotaRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CheckQuotaRequest.

        订单需要创建总实例数、订购数量

        :return: The subscription_num of this CheckQuotaRequest.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CheckQuotaRequest.

        订单需要创建总实例数、订购数量

        :param subscription_num: The subscription_num of this CheckQuotaRequest.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

    @property
    def disk_size(self):
        """Gets the disk_size of this CheckQuotaRequest.

        单台实例所需的磁盘大小（最大系统盘1块*1024、数据盘10块*32768）

        :return: The disk_size of this CheckQuotaRequest.
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this CheckQuotaRequest.

        单台实例所需的磁盘大小（最大系统盘1块*1024、数据盘10块*32768）

        :param disk_size: The disk_size of this CheckQuotaRequest.
        :type disk_size: int
        """
        self._disk_size = disk_size

    @property
    def disk_num(self):
        """Gets the disk_num of this CheckQuotaRequest.

        单台实例所需的磁盘数量（最大系统盘1块、数据盘10块）

        :return: The disk_num of this CheckQuotaRequest.
        :rtype: int
        """
        return self._disk_num

    @disk_num.setter
    def disk_num(self, disk_num):
        """Sets the disk_num of this CheckQuotaRequest.

        单台实例所需的磁盘数量（最大系统盘1块、数据盘10块）

        :param disk_num: The disk_num of this CheckQuotaRequest.
        :type disk_num: int
        """
        self._disk_num = disk_num

    @property
    def is_period(self):
        """Gets the is_period of this CheckQuotaRequest.

        是否包周期

        :return: The is_period of this CheckQuotaRequest.
        :rtype: bool
        """
        return self._is_period

    @is_period.setter
    def is_period(self, is_period):
        """Sets the is_period of this CheckQuotaRequest.

        是否包周期

        :param is_period: The is_period of this CheckQuotaRequest.
        :type is_period: bool
        """
        self._is_period = is_period

    @property
    def deh_id(self):
        """Gets the deh_id of this CheckQuotaRequest.

        主机id

        :return: The deh_id of this CheckQuotaRequest.
        :rtype: str
        """
        return self._deh_id

    @deh_id.setter
    def deh_id(self, deh_id):
        """Sets the deh_id of this CheckQuotaRequest.

        主机id

        :param deh_id: The deh_id of this CheckQuotaRequest.
        :type deh_id: str
        """
        self._deh_id = deh_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CheckQuotaRequest.

        云专属分布式存储池id

        :return: The cluster_id of this CheckQuotaRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CheckQuotaRequest.

        云专属分布式存储池id

        :param cluster_id: The cluster_id of this CheckQuotaRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, CheckQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
