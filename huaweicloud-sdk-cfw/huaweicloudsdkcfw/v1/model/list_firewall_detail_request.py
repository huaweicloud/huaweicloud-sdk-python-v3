# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'service_type': 'int',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'service_type': 'service_type',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id',
        'name': 'name'
    }

    def __init__(self, offset=None, limit=None, service_type=None, enterprise_project_id=None, fw_instance_id=None, name=None):
        r"""ListFirewallDetailRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param service_type: 服务类型，目前仅支持0互联网防护
        :type service_type: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。
        :type fw_instance_id: str
        :param name: 防火墙名称
        :type name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._service_type = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self._name = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.service_type = service_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if name is not None:
            self.name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListFirewallDetailRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListFirewallDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFirewallDetailRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListFirewallDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFirewallDetailRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListFirewallDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFirewallDetailRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListFirewallDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def service_type(self):
        r"""Gets the service_type of this ListFirewallDetailRequest.

        服务类型，目前仅支持0互联网防护

        :return: The service_type of this ListFirewallDetailRequest.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListFirewallDetailRequest.

        服务类型，目前仅支持0互联网防护

        :param service_type: The service_type of this ListFirewallDetailRequest.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListFirewallDetailRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListFirewallDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListFirewallDetailRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListFirewallDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListFirewallDetailRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :return: The fw_instance_id of this ListFirewallDetailRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListFirewallDetailRequest.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :param fw_instance_id: The fw_instance_id of this ListFirewallDetailRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def name(self):
        r"""Gets the name of this ListFirewallDetailRequest.

        防火墙名称

        :return: The name of this ListFirewallDetailRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFirewallDetailRequest.

        防火墙名称

        :param name: The name of this ListFirewallDetailRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListFirewallDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
