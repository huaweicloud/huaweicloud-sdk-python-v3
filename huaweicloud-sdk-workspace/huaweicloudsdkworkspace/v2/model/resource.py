# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'add_volumes': 'AddVolumes',
        'create_desktops': 'CreateDesktopReq',
        'deh_hosts': 'Hosts',
        'rebuild_desktops': 'RebuildDesktopsReq',
        'attach_desktops': 'AttachInstancesReq',
        'create_exclusive_hosts': 'CreateExclusiveHostsReq',
        'resize_exclusive_lites': 'ResizeExclusiveLitesReq',
        'create_desktop_pool': 'CreateDesktopPoolReq',
        'expand_desktop_pool': 'ExpandDesktopPoolOrderReq',
        'apply_desktops_internet': 'ApplyDesktopsInternet',
        'apply_subnet_bandwidth': 'ApplySubnetBandwidthReq',
        'subscribe_user_sharer': 'SubscribeUserSharerReq',
        'cloud_service_console_url': 'str'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'add_volumes': 'add_volumes',
        'create_desktops': 'create_desktops',
        'deh_hosts': 'deh_hosts',
        'rebuild_desktops': 'rebuild_desktops',
        'attach_desktops': 'attach_desktops',
        'create_exclusive_hosts': 'create_exclusive_hosts',
        'resize_exclusive_lites': 'resize_exclusive_lites',
        'create_desktop_pool': 'create_desktop_pool',
        'expand_desktop_pool': 'expand_desktop_pool',
        'apply_desktops_internet': 'apply_desktops_internet',
        'apply_subnet_bandwidth': 'apply_subnet_bandwidth',
        'subscribe_user_sharer': 'subscribe_user_sharer',
        'cloud_service_console_url': 'cloud_service_console_url'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_renew=None, add_volumes=None, create_desktops=None, deh_hosts=None, rebuild_desktops=None, attach_desktops=None, create_exclusive_hosts=None, resize_exclusive_lites=None, create_desktop_pool=None, expand_desktop_pool=None, apply_desktops_internet=None, apply_subnet_bandwidth=None, subscribe_user_sharer=None, cloud_service_console_url=None):
        """Resource

        The model defined in huaweicloud sdk

        :param period_type: 订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode&#x3D;1 一次性计费场景使用），必填
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param is_auto_renew: 是否续订
        :type is_auto_renew: int
        :param add_volumes: 
        :type add_volumes: :class:`huaweicloudsdkworkspace.v2.AddVolumes`
        :param create_desktops: 
        :type create_desktops: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        :param deh_hosts: 
        :type deh_hosts: :class:`huaweicloudsdkworkspace.v2.Hosts`
        :param rebuild_desktops: 
        :type rebuild_desktops: :class:`huaweicloudsdkworkspace.v2.RebuildDesktopsReq`
        :param attach_desktops: 
        :type attach_desktops: :class:`huaweicloudsdkworkspace.v2.AttachInstancesReq`
        :param create_exclusive_hosts: 
        :type create_exclusive_hosts: :class:`huaweicloudsdkworkspace.v2.CreateExclusiveHostsReq`
        :param resize_exclusive_lites: 
        :type resize_exclusive_lites: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        :param create_desktop_pool: 
        :type create_desktop_pool: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolReq`
        :param expand_desktop_pool: 
        :type expand_desktop_pool: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolOrderReq`
        :param apply_desktops_internet: 
        :type apply_desktops_internet: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternet`
        :param apply_subnet_bandwidth: 
        :type apply_subnet_bandwidth: :class:`huaweicloudsdkworkspace.v2.ApplySubnetBandwidthReq`
        :param subscribe_user_sharer: 
        :type subscribe_user_sharer: :class:`huaweicloudsdkworkspace.v2.SubscribeUserSharerReq`
        :param cloud_service_console_url: 支付后跳转的地址
        :type cloud_service_console_url: str
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._add_volumes = None
        self._create_desktops = None
        self._deh_hosts = None
        self._rebuild_desktops = None
        self._attach_desktops = None
        self._create_exclusive_hosts = None
        self._resize_exclusive_lites = None
        self._create_desktop_pool = None
        self._expand_desktop_pool = None
        self._apply_desktops_internet = None
        self._apply_subnet_bandwidth = None
        self._subscribe_user_sharer = None
        self._cloud_service_console_url = None
        self.discriminator = None

        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if add_volumes is not None:
            self.add_volumes = add_volumes
        if create_desktops is not None:
            self.create_desktops = create_desktops
        if deh_hosts is not None:
            self.deh_hosts = deh_hosts
        if rebuild_desktops is not None:
            self.rebuild_desktops = rebuild_desktops
        if attach_desktops is not None:
            self.attach_desktops = attach_desktops
        if create_exclusive_hosts is not None:
            self.create_exclusive_hosts = create_exclusive_hosts
        if resize_exclusive_lites is not None:
            self.resize_exclusive_lites = resize_exclusive_lites
        if create_desktop_pool is not None:
            self.create_desktop_pool = create_desktop_pool
        if expand_desktop_pool is not None:
            self.expand_desktop_pool = expand_desktop_pool
        if apply_desktops_internet is not None:
            self.apply_desktops_internet = apply_desktops_internet
        if apply_subnet_bandwidth is not None:
            self.apply_subnet_bandwidth = apply_subnet_bandwidth
        if subscribe_user_sharer is not None:
            self.subscribe_user_sharer = subscribe_user_sharer
        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url

    @property
    def period_type(self):
        """Gets the period_type of this Resource.

        订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode=1 一次性计费场景使用），必填

        :return: The period_type of this Resource.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this Resource.

        订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode=1 一次性计费场景使用），必填

        :param period_type: The period_type of this Resource.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this Resource.

        订购周期数

        :return: The period_num of this Resource.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this Resource.

        订购周期数

        :param period_num: The period_num of this Resource.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this Resource.

        是否续订

        :return: The is_auto_renew of this Resource.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this Resource.

        是否续订

        :param is_auto_renew: The is_auto_renew of this Resource.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def add_volumes(self):
        """Gets the add_volumes of this Resource.

        :return: The add_volumes of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AddVolumes`
        """
        return self._add_volumes

    @add_volumes.setter
    def add_volumes(self, add_volumes):
        """Sets the add_volumes of this Resource.

        :param add_volumes: The add_volumes of this Resource.
        :type add_volumes: :class:`huaweicloudsdkworkspace.v2.AddVolumes`
        """
        self._add_volumes = add_volumes

    @property
    def create_desktops(self):
        """Gets the create_desktops of this Resource.

        :return: The create_desktops of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        """
        return self._create_desktops

    @create_desktops.setter
    def create_desktops(self, create_desktops):
        """Sets the create_desktops of this Resource.

        :param create_desktops: The create_desktops of this Resource.
        :type create_desktops: :class:`huaweicloudsdkworkspace.v2.CreateDesktopReq`
        """
        self._create_desktops = create_desktops

    @property
    def deh_hosts(self):
        """Gets the deh_hosts of this Resource.

        :return: The deh_hosts of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Hosts`
        """
        return self._deh_hosts

    @deh_hosts.setter
    def deh_hosts(self, deh_hosts):
        """Sets the deh_hosts of this Resource.

        :param deh_hosts: The deh_hosts of this Resource.
        :type deh_hosts: :class:`huaweicloudsdkworkspace.v2.Hosts`
        """
        self._deh_hosts = deh_hosts

    @property
    def rebuild_desktops(self):
        """Gets the rebuild_desktops of this Resource.

        :return: The rebuild_desktops of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RebuildDesktopsReq`
        """
        return self._rebuild_desktops

    @rebuild_desktops.setter
    def rebuild_desktops(self, rebuild_desktops):
        """Sets the rebuild_desktops of this Resource.

        :param rebuild_desktops: The rebuild_desktops of this Resource.
        :type rebuild_desktops: :class:`huaweicloudsdkworkspace.v2.RebuildDesktopsReq`
        """
        self._rebuild_desktops = rebuild_desktops

    @property
    def attach_desktops(self):
        """Gets the attach_desktops of this Resource.

        :return: The attach_desktops of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AttachInstancesReq`
        """
        return self._attach_desktops

    @attach_desktops.setter
    def attach_desktops(self, attach_desktops):
        """Sets the attach_desktops of this Resource.

        :param attach_desktops: The attach_desktops of this Resource.
        :type attach_desktops: :class:`huaweicloudsdkworkspace.v2.AttachInstancesReq`
        """
        self._attach_desktops = attach_desktops

    @property
    def create_exclusive_hosts(self):
        """Gets the create_exclusive_hosts of this Resource.

        :return: The create_exclusive_hosts of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateExclusiveHostsReq`
        """
        return self._create_exclusive_hosts

    @create_exclusive_hosts.setter
    def create_exclusive_hosts(self, create_exclusive_hosts):
        """Sets the create_exclusive_hosts of this Resource.

        :param create_exclusive_hosts: The create_exclusive_hosts of this Resource.
        :type create_exclusive_hosts: :class:`huaweicloudsdkworkspace.v2.CreateExclusiveHostsReq`
        """
        self._create_exclusive_hosts = create_exclusive_hosts

    @property
    def resize_exclusive_lites(self):
        """Gets the resize_exclusive_lites of this Resource.

        :return: The resize_exclusive_lites of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        """
        return self._resize_exclusive_lites

    @resize_exclusive_lites.setter
    def resize_exclusive_lites(self, resize_exclusive_lites):
        """Sets the resize_exclusive_lites of this Resource.

        :param resize_exclusive_lites: The resize_exclusive_lites of this Resource.
        :type resize_exclusive_lites: :class:`huaweicloudsdkworkspace.v2.ResizeExclusiveLitesReq`
        """
        self._resize_exclusive_lites = resize_exclusive_lites

    @property
    def create_desktop_pool(self):
        """Gets the create_desktop_pool of this Resource.

        :return: The create_desktop_pool of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolReq`
        """
        return self._create_desktop_pool

    @create_desktop_pool.setter
    def create_desktop_pool(self, create_desktop_pool):
        """Sets the create_desktop_pool of this Resource.

        :param create_desktop_pool: The create_desktop_pool of this Resource.
        :type create_desktop_pool: :class:`huaweicloudsdkworkspace.v2.CreateDesktopPoolReq`
        """
        self._create_desktop_pool = create_desktop_pool

    @property
    def expand_desktop_pool(self):
        """Gets the expand_desktop_pool of this Resource.

        :return: The expand_desktop_pool of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolOrderReq`
        """
        return self._expand_desktop_pool

    @expand_desktop_pool.setter
    def expand_desktop_pool(self, expand_desktop_pool):
        """Sets the expand_desktop_pool of this Resource.

        :param expand_desktop_pool: The expand_desktop_pool of this Resource.
        :type expand_desktop_pool: :class:`huaweicloudsdkworkspace.v2.ExpandDesktopPoolOrderReq`
        """
        self._expand_desktop_pool = expand_desktop_pool

    @property
    def apply_desktops_internet(self):
        """Gets the apply_desktops_internet of this Resource.

        :return: The apply_desktops_internet of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternet`
        """
        return self._apply_desktops_internet

    @apply_desktops_internet.setter
    def apply_desktops_internet(self, apply_desktops_internet):
        """Sets the apply_desktops_internet of this Resource.

        :param apply_desktops_internet: The apply_desktops_internet of this Resource.
        :type apply_desktops_internet: :class:`huaweicloudsdkworkspace.v2.ApplyDesktopsInternet`
        """
        self._apply_desktops_internet = apply_desktops_internet

    @property
    def apply_subnet_bandwidth(self):
        """Gets the apply_subnet_bandwidth of this Resource.

        :return: The apply_subnet_bandwidth of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplySubnetBandwidthReq`
        """
        return self._apply_subnet_bandwidth

    @apply_subnet_bandwidth.setter
    def apply_subnet_bandwidth(self, apply_subnet_bandwidth):
        """Sets the apply_subnet_bandwidth of this Resource.

        :param apply_subnet_bandwidth: The apply_subnet_bandwidth of this Resource.
        :type apply_subnet_bandwidth: :class:`huaweicloudsdkworkspace.v2.ApplySubnetBandwidthReq`
        """
        self._apply_subnet_bandwidth = apply_subnet_bandwidth

    @property
    def subscribe_user_sharer(self):
        """Gets the subscribe_user_sharer of this Resource.

        :return: The subscribe_user_sharer of this Resource.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SubscribeUserSharerReq`
        """
        return self._subscribe_user_sharer

    @subscribe_user_sharer.setter
    def subscribe_user_sharer(self, subscribe_user_sharer):
        """Sets the subscribe_user_sharer of this Resource.

        :param subscribe_user_sharer: The subscribe_user_sharer of this Resource.
        :type subscribe_user_sharer: :class:`huaweicloudsdkworkspace.v2.SubscribeUserSharerReq`
        """
        self._subscribe_user_sharer = subscribe_user_sharer

    @property
    def cloud_service_console_url(self):
        """Gets the cloud_service_console_url of this Resource.

        支付后跳转的地址

        :return: The cloud_service_console_url of this Resource.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        """Sets the cloud_service_console_url of this Resource.

        支付后跳转的地址

        :param cloud_service_console_url: The cloud_service_console_url of this Resource.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
