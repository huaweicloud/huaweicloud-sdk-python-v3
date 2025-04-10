# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipOperateProtectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'status': 'int',
        'ip_infos': 'list[EipOperateProtectReqIpInfos]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'status': 'status',
        'ip_infos': 'ip_infos'
    }

    def __init__(self, object_id=None, status=None, ip_infos=None):
        r"""EipOperateProtectReq

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。
        :type object_id: str
        :param status: EIP切换的状态，0表示防护中，1表示未防护
        :type status: int
        :param ip_infos: 切换防护状态的EIP信息列表
        :type ip_infos: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        
        

        self._object_id = None
        self._status = None
        self._ip_infos = None
        self.discriminator = None

        self.object_id = object_id
        self.status = status
        self.ip_infos = ip_infos

    @property
    def object_id(self):
        r"""Gets the object_id of this EipOperateProtectReq.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :return: The object_id of this EipOperateProtectReq.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this EipOperateProtectReq.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)获得，通过返回值中的data.records.protect_objects.object_id（.表示各对象之间层级的区分）获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。此处仅取type为0的防护对象id，可通过data.records.protect_objects.type（.表示各对象之间层级的区分）获得。

        :param object_id: The object_id of this EipOperateProtectReq.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def status(self):
        r"""Gets the status of this EipOperateProtectReq.

        EIP切换的状态，0表示防护中，1表示未防护

        :return: The status of this EipOperateProtectReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EipOperateProtectReq.

        EIP切换的状态，0表示防护中，1表示未防护

        :param status: The status of this EipOperateProtectReq.
        :type status: int
        """
        self._status = status

    @property
    def ip_infos(self):
        r"""Gets the ip_infos of this EipOperateProtectReq.

        切换防护状态的EIP信息列表

        :return: The ip_infos of this EipOperateProtectReq.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        return self._ip_infos

    @ip_infos.setter
    def ip_infos(self, ip_infos):
        r"""Sets the ip_infos of this EipOperateProtectReq.

        切换防护状态的EIP信息列表

        :param ip_infos: The ip_infos of this EipOperateProtectReq.
        :type ip_infos: list[:class:`huaweicloudsdkcfw.v1.EipOperateProtectReqIpInfos`]
        """
        self._ip_infos = ip_infos

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
        if not isinstance(other, EipOperateProtectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
