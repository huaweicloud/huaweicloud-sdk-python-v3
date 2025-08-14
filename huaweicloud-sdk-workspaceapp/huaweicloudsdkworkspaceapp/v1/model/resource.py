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
        'add_volumes': 'AddVolumes',
        'cloud_service_console_url': 'str',
        'create_services': 'CreateServices',
        'is_auto_renew': 'int',
        'period_num': 'int',
        'period_type': 'int',
        'subscription_num': 'int'
    }

    attribute_map = {
        'add_volumes': 'add_volumes',
        'cloud_service_console_url': 'cloud_service_console_url',
        'create_services': 'create_services',
        'is_auto_renew': 'is_auto_renew',
        'period_num': 'period_num',
        'period_type': 'period_type',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, add_volumes=None, cloud_service_console_url=None, create_services=None, is_auto_renew=None, period_num=None, period_type=None, subscription_num=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param add_volumes: 
        :type add_volumes: :class:`huaweicloudsdkworkspaceapp.v1.AddVolumes`
        :param cloud_service_console_url: 支付后跳转的地址。
        :type cloud_service_console_url: str
        :param create_services: 
        :type create_services: :class:`huaweicloudsdkworkspaceapp.v1.CreateServices`
        :param is_auto_renew: 订购关系当前是否是自动续费：0 否 1 是。
        :type is_auto_renew: int
        :param period_num: 订购周期数取值大于0。
        :type period_num: int
        :param period_type: 包周期订单订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode&#x3D;1 一次性计费场景使用），必填。
        :type period_type: int
        :param subscription_num: 订购数量。
        :type subscription_num: int
        """
        
        

        self._add_volumes = None
        self._cloud_service_console_url = None
        self._create_services = None
        self._is_auto_renew = None
        self._period_num = None
        self._period_type = None
        self._subscription_num = None
        self.discriminator = None

        if add_volumes is not None:
            self.add_volumes = add_volumes
        if cloud_service_console_url is not None:
            self.cloud_service_console_url = cloud_service_console_url
        self.create_services = create_services
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if period_num is not None:
            self.period_num = period_num
        if period_type is not None:
            self.period_type = period_type
        self.subscription_num = subscription_num

    @property
    def add_volumes(self):
        r"""Gets the add_volumes of this Resource.

        :return: The add_volumes of this Resource.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AddVolumes`
        """
        return self._add_volumes

    @add_volumes.setter
    def add_volumes(self, add_volumes):
        r"""Sets the add_volumes of this Resource.

        :param add_volumes: The add_volumes of this Resource.
        :type add_volumes: :class:`huaweicloudsdkworkspaceapp.v1.AddVolumes`
        """
        self._add_volumes = add_volumes

    @property
    def cloud_service_console_url(self):
        r"""Gets the cloud_service_console_url of this Resource.

        支付后跳转的地址。

        :return: The cloud_service_console_url of this Resource.
        :rtype: str
        """
        return self._cloud_service_console_url

    @cloud_service_console_url.setter
    def cloud_service_console_url(self, cloud_service_console_url):
        r"""Sets the cloud_service_console_url of this Resource.

        支付后跳转的地址。

        :param cloud_service_console_url: The cloud_service_console_url of this Resource.
        :type cloud_service_console_url: str
        """
        self._cloud_service_console_url = cloud_service_console_url

    @property
    def create_services(self):
        r"""Gets the create_services of this Resource.

        :return: The create_services of this Resource.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateServices`
        """
        return self._create_services

    @create_services.setter
    def create_services(self, create_services):
        r"""Sets the create_services of this Resource.

        :param create_services: The create_services of this Resource.
        :type create_services: :class:`huaweicloudsdkworkspaceapp.v1.CreateServices`
        """
        self._create_services = create_services

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this Resource.

        订购关系当前是否是自动续费：0 否 1 是。

        :return: The is_auto_renew of this Resource.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this Resource.

        订购关系当前是否是自动续费：0 否 1 是。

        :param is_auto_renew: The is_auto_renew of this Resource.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def period_num(self):
        r"""Gets the period_num of this Resource.

        订购周期数取值大于0。

        :return: The period_num of this Resource.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this Resource.

        订购周期数取值大于0。

        :param period_num: The period_num of this Resource.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def period_type(self):
        r"""Gets the period_type of this Resource.

        包周期订单订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode=1 一次性计费场景使用），必填。

        :return: The period_type of this Resource.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this Resource.

        包周期订单订购周期类型：2：月；3：年；4：包小时（仅限带宽加油包购买场景使用）5：绝对时间；（追加附属资源场景使用，比如主机上追加云硬盘）6：一次性（chargingMode=1 一次性计费场景使用），必填。

        :param period_type: The period_type of this Resource.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def subscription_num(self):
        r"""Gets the subscription_num of this Resource.

        订购数量。

        :return: The subscription_num of this Resource.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        r"""Sets the subscription_num of this Resource.

        订购数量。

        :param subscription_num: The subscription_num of this Resource.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

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
