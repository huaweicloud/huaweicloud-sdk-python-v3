# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBandwidthResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_type': 'str',
        'billing_info': 'str',
        'charge_mode': 'str',
        'id': 'str',
        'name': 'str',
        'publicip_info': 'list[PublicipInfoResp]',
        'share_type': 'str',
        'size': 'int',
        'tenant_id': 'str',
        'status': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'bandwidth_type': 'bandwidth_type',
        'billing_info': 'billing_info',
        'charge_mode': 'charge_mode',
        'id': 'id',
        'name': 'name',
        'publicip_info': 'publicip_info',
        'share_type': 'share_type',
        'size': 'size',
        'tenant_id': 'tenant_id',
        'status': 'status',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, bandwidth_type=None, billing_info=None, charge_mode=None, id=None, name=None, publicip_info=None, share_type=None, size=None, tenant_id=None, status=None, public_border_group=None):
        """BatchBandwidthResp

        The model defined in huaweicloud sdk

        :param bandwidth_type: 功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp
        :type bandwidth_type: str
        :param billing_info: 功能说明：账单信息  如果billing_info不为空，说明是包周期的带宽
        :type billing_info: str
        :param charge_mode: 功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。
        :type charge_mode: str
        :param id: 功能说明：带宽唯一标识
        :type id: str
        :param name: 功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param publicip_info: 功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        :param share_type: 功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽
        :type share_type: str
        :param size: 功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。
        :type size: int
        :param tenant_id: 功能说明：用户所属租户ID
        :type tenant_id: str
        :param status: 功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常
        :type status: str
        :param public_border_group: 功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip
        :type public_border_group: str
        """
        
        

        self._bandwidth_type = None
        self._billing_info = None
        self._charge_mode = None
        self._id = None
        self._name = None
        self._publicip_info = None
        self._share_type = None
        self._size = None
        self._tenant_id = None
        self._status = None
        self._public_border_group = None
        self.discriminator = None

        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if billing_info is not None:
            self.billing_info = billing_info
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if publicip_info is not None:
            self.publicip_info = publicip_info
        if share_type is not None:
            self.share_type = share_type
        if size is not None:
            self.size = size
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if status is not None:
            self.status = status
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this BatchBandwidthResp.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :return: The bandwidth_type of this BatchBandwidthResp.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this BatchBandwidthResp.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :param bandwidth_type: The bandwidth_type of this BatchBandwidthResp.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def billing_info(self):
        """Gets the billing_info of this BatchBandwidthResp.

        功能说明：账单信息  如果billing_info不为空，说明是包周期的带宽

        :return: The billing_info of this BatchBandwidthResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this BatchBandwidthResp.

        功能说明：账单信息  如果billing_info不为空，说明是包周期的带宽

        :param billing_info: The billing_info of this BatchBandwidthResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BatchBandwidthResp.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :return: The charge_mode of this BatchBandwidthResp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BatchBandwidthResp.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :param charge_mode: The charge_mode of this BatchBandwidthResp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def id(self):
        """Gets the id of this BatchBandwidthResp.

        功能说明：带宽唯一标识

        :return: The id of this BatchBandwidthResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchBandwidthResp.

        功能说明：带宽唯一标识

        :param id: The id of this BatchBandwidthResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BatchBandwidthResp.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BatchBandwidthResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchBandwidthResp.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BatchBandwidthResp.
        :type name: str
        """
        self._name = name

    @property
    def publicip_info(self):
        """Gets the publicip_info of this BatchBandwidthResp.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :return: The publicip_info of this BatchBandwidthResp.
        :rtype: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this BatchBandwidthResp.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :param publicip_info: The publicip_info of this BatchBandwidthResp.
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        """
        self._publicip_info = publicip_info

    @property
    def share_type(self):
        """Gets the share_type of this BatchBandwidthResp.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :return: The share_type of this BatchBandwidthResp.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this BatchBandwidthResp.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :param share_type: The share_type of this BatchBandwidthResp.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        """Gets the size of this BatchBandwidthResp.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :return: The size of this BatchBandwidthResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BatchBandwidthResp.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :param size: The size of this BatchBandwidthResp.
        :type size: int
        """
        self._size = size

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BatchBandwidthResp.

        功能说明：用户所属租户ID

        :return: The tenant_id of this BatchBandwidthResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BatchBandwidthResp.

        功能说明：用户所属租户ID

        :param tenant_id: The tenant_id of this BatchBandwidthResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def status(self):
        """Gets the status of this BatchBandwidthResp.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :return: The status of this BatchBandwidthResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchBandwidthResp.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :param status: The status of this BatchBandwidthResp.
        :type status: str
        """
        self._status = status

    @property
    def public_border_group(self):
        """Gets the public_border_group of this BatchBandwidthResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip

        :return: The public_border_group of this BatchBandwidthResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this BatchBandwidthResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip

        :param public_border_group: The public_border_group of this BatchBandwidthResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, BatchBandwidthResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
