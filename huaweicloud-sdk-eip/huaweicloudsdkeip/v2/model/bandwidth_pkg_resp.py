# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPkgResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'processed_time': 'str',
        'bandwidth_id': 'str',
        'pkg_size': 'int',
        'tenant_id': 'str',
        'billing_info': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'resource_name': 'resourceName',
        'processed_time': 'processedTime',
        'bandwidth_id': 'bandwidthId',
        'pkg_size': 'pkgSize',
        'tenant_id': 'tenantId',
        'billing_info': 'billingInfo',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'status': 'status'
    }

    def __init__(self, resource_id=None, resource_name=None, processed_time=None, bandwidth_id=None, pkg_size=None, tenant_id=None, billing_info=None, start_time=None, end_time=None, status=None):
        """BandwidthPkgResp

        The model defined in huaweicloud sdk

        :param resource_id: - 功能说明：加油包ID - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）
        :type resource_id: str
        :param resource_name: - 功能说明：加油包名称
        :type resource_name: str
        :param processed_time: - 功能说明：资源创建时间，UTC时间格式：2016-03-28T00:00:00Z
        :type processed_time: str
        :param bandwidth_id: - 功能说明：加油包绑定的原带宽ID
        :type bandwidth_id: str
        :param pkg_size: - 功能说明：加油包的大小，即在原始带宽之上提升的带宽大小 - 取值范围：&gt;1M，pkgSize+原始带宽大小 &lt; 云服务带宽接口限制的带宽上限
        :type pkg_size: int
        :param tenant_id: - 功能说明：租户id
        :type tenant_id: str
        :param billing_info: - 功能说明：加油包订单相关信息格式：非空时值为&#39;&#39;orderId:productId&#39;&#39;
        :type billing_info: str
        :param start_time: - 功能说明：加油包起始生效时间，UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime &gt;&#x3D; 服务处理请求的时间
        :type start_time: str
        :param end_time: - 功能说明：加油包结束时间UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime &lt; endTime
        :type end_time: str
        :param status: - 功能说明：加油包资源状态，仅管理员权限可以变更状态 - 取值范围：&#39;&#39;pending&#39;&#39;, &#39;&#39;active&#39;&#39;, &#39;&#39;completed&#39;&#39;, &#39;&#39;error&#39;&#39;
        :type status: str
        """
        
        

        self._resource_id = None
        self._resource_name = None
        self._processed_time = None
        self._bandwidth_id = None
        self._pkg_size = None
        self._tenant_id = None
        self._billing_info = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_name = resource_name
        self.processed_time = processed_time
        self.bandwidth_id = bandwidth_id
        self.pkg_size = pkg_size
        self.tenant_id = tenant_id
        self.billing_info = billing_info
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    @property
    def resource_id(self):
        """Gets the resource_id of this BandwidthPkgResp.

        - 功能说明：加油包ID - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）

        :return: The resource_id of this BandwidthPkgResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BandwidthPkgResp.

        - 功能说明：加油包ID - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）

        :param resource_id: The resource_id of this BandwidthPkgResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this BandwidthPkgResp.

        - 功能说明：加油包名称

        :return: The resource_name of this BandwidthPkgResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this BandwidthPkgResp.

        - 功能说明：加油包名称

        :param resource_name: The resource_name of this BandwidthPkgResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def processed_time(self):
        """Gets the processed_time of this BandwidthPkgResp.

        - 功能说明：资源创建时间，UTC时间格式：2016-03-28T00:00:00Z

        :return: The processed_time of this BandwidthPkgResp.
        :rtype: str
        """
        return self._processed_time

    @processed_time.setter
    def processed_time(self, processed_time):
        """Sets the processed_time of this BandwidthPkgResp.

        - 功能说明：资源创建时间，UTC时间格式：2016-03-28T00:00:00Z

        :param processed_time: The processed_time of this BandwidthPkgResp.
        :type processed_time: str
        """
        self._processed_time = processed_time

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this BandwidthPkgResp.

        - 功能说明：加油包绑定的原带宽ID

        :return: The bandwidth_id of this BandwidthPkgResp.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this BandwidthPkgResp.

        - 功能说明：加油包绑定的原带宽ID

        :param bandwidth_id: The bandwidth_id of this BandwidthPkgResp.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def pkg_size(self):
        """Gets the pkg_size of this BandwidthPkgResp.

        - 功能说明：加油包的大小，即在原始带宽之上提升的带宽大小 - 取值范围：>1M，pkgSize+原始带宽大小 < 云服务带宽接口限制的带宽上限

        :return: The pkg_size of this BandwidthPkgResp.
        :rtype: int
        """
        return self._pkg_size

    @pkg_size.setter
    def pkg_size(self, pkg_size):
        """Sets the pkg_size of this BandwidthPkgResp.

        - 功能说明：加油包的大小，即在原始带宽之上提升的带宽大小 - 取值范围：>1M，pkgSize+原始带宽大小 < 云服务带宽接口限制的带宽上限

        :param pkg_size: The pkg_size of this BandwidthPkgResp.
        :type pkg_size: int
        """
        self._pkg_size = pkg_size

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BandwidthPkgResp.

        - 功能说明：租户id

        :return: The tenant_id of this BandwidthPkgResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BandwidthPkgResp.

        - 功能说明：租户id

        :param tenant_id: The tenant_id of this BandwidthPkgResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def billing_info(self):
        """Gets the billing_info of this BandwidthPkgResp.

        - 功能说明：加油包订单相关信息格式：非空时值为''orderId:productId''

        :return: The billing_info of this BandwidthPkgResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this BandwidthPkgResp.

        - 功能说明：加油包订单相关信息格式：非空时值为''orderId:productId''

        :param billing_info: The billing_info of this BandwidthPkgResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def start_time(self):
        """Gets the start_time of this BandwidthPkgResp.

        - 功能说明：加油包起始生效时间，UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime >= 服务处理请求的时间

        :return: The start_time of this BandwidthPkgResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BandwidthPkgResp.

        - 功能说明：加油包起始生效时间，UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime >= 服务处理请求的时间

        :param start_time: The start_time of this BandwidthPkgResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this BandwidthPkgResp.

        - 功能说明：加油包结束时间UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime < endTime

        :return: The end_time of this BandwidthPkgResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BandwidthPkgResp.

        - 功能说明：加油包结束时间UTC时间格式：2016-03-28T00:00:00Z - 取值范围：startTime < endTime

        :param end_time: The end_time of this BandwidthPkgResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this BandwidthPkgResp.

        - 功能说明：加油包资源状态，仅管理员权限可以变更状态 - 取值范围：''pending'', ''active'', ''completed'', ''error''

        :return: The status of this BandwidthPkgResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BandwidthPkgResp.

        - 功能说明：加油包资源状态，仅管理员权限可以变更状态 - 取值范围：''pending'', ''active'', ''completed'', ''error''

        :param status: The status of this BandwidthPkgResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, BandwidthPkgResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
