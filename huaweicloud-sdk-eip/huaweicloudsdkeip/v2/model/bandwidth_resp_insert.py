# coding: utf-8

import pprint
import re

import six





class BandwidthRespInsert:


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
        'charge_mode': 'str',
        'id': 'str',
        'name': 'str',
        'publicip_info': 'list[PublicipInfoResp]',
        'billing_info': 'str',
        'share_type': 'str',
        'size': 'int',
        'tenant_id': 'str',
        'enterprise_project_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'bandwidth_type': 'bandwidth_type',
        'charge_mode': 'charge_mode',
        'id': 'id',
        'name': 'name',
        'publicip_info': 'publicip_info',
        'billing_info': 'billing_info',
        'share_type': 'share_type',
        'size': 'size',
        'tenant_id': 'tenant_id',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status'
    }

    def __init__(self, bandwidth_type=None, charge_mode=None, id=None, name=None, publicip_info=None, billing_info=None, share_type=None, size=None, tenant_id=None, enterprise_project_id=None, status=None):
        """BandwidthRespInsert - a model defined in huaweicloud sdk"""
        
        

        self._bandwidth_type = None
        self._charge_mode = None
        self._id = None
        self._name = None
        self._publicip_info = None
        self._billing_info = None
        self._share_type = None
        self._size = None
        self._tenant_id = None
        self._enterprise_project_id = None
        self._status = None
        self.discriminator = None

        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if publicip_info is not None:
            self.publicip_info = publicip_info
        if billing_info is not None:
            self.billing_info = billing_info
        if share_type is not None:
            self.share_type = share_type
        if size is not None:
            self.size = size
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this BandwidthRespInsert.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :return: The bandwidth_type of this BandwidthRespInsert.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this BandwidthRespInsert.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :param bandwidth_type: The bandwidth_type of this BandwidthRespInsert.
        :type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BandwidthRespInsert.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :return: The charge_mode of this BandwidthRespInsert.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BandwidthRespInsert.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :param charge_mode: The charge_mode of this BandwidthRespInsert.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def id(self):
        """Gets the id of this BandwidthRespInsert.

        功能说明：带宽唯一标识

        :return: The id of this BandwidthRespInsert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BandwidthRespInsert.

        功能说明：带宽唯一标识

        :param id: The id of this BandwidthRespInsert.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BandwidthRespInsert.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BandwidthRespInsert.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandwidthRespInsert.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BandwidthRespInsert.
        :type: str
        """
        self._name = name

    @property
    def publicip_info(self):
        """Gets the publicip_info of this BandwidthRespInsert.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :return: The publicip_info of this BandwidthRespInsert.
        :rtype: list[PublicipInfoResp]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this BandwidthRespInsert.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :param publicip_info: The publicip_info of this BandwidthRespInsert.
        :type: list[PublicipInfoResp]
        """
        self._publicip_info = publicip_info

    @property
    def billing_info(self):
        """Gets the billing_info of this BandwidthRespInsert.

        功能说明：账单信息  如果billinginfo不为空，说明是包周期的带宽

        :return: The billing_info of this BandwidthRespInsert.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this BandwidthRespInsert.

        功能说明：账单信息  如果billinginfo不为空，说明是包周期的带宽

        :param billing_info: The billing_info of this BandwidthRespInsert.
        :type: str
        """
        self._billing_info = billing_info

    @property
    def share_type(self):
        """Gets the share_type of this BandwidthRespInsert.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :return: The share_type of this BandwidthRespInsert.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this BandwidthRespInsert.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :param share_type: The share_type of this BandwidthRespInsert.
        :type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        """Gets the size of this BandwidthRespInsert.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :return: The size of this BandwidthRespInsert.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BandwidthRespInsert.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :param size: The size of this BandwidthRespInsert.
        :type: int
        """
        self._size = size

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BandwidthRespInsert.

        功能说明：用户所属租户ID

        :return: The tenant_id of this BandwidthRespInsert.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BandwidthRespInsert.

        功能说明：用户所属租户ID

        :param tenant_id: The tenant_id of this BandwidthRespInsert.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BandwidthRespInsert.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建带宽时，给带宽绑定企业项目ID。

        :return: The enterprise_project_id of this BandwidthRespInsert.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BandwidthRespInsert.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建带宽时，给带宽绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this BandwidthRespInsert.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this BandwidthRespInsert.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :return: The status of this BandwidthRespInsert.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BandwidthRespInsert.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :param status: The status of this BandwidthRespInsert.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BandwidthRespInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
