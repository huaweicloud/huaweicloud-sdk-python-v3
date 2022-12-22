# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsSwitchDTO:

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
        'ips_type': 'int',
        'status': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'ips_type': 'ips_type',
        'status': 'status'
    }

    def __init__(self, object_id=None, ips_type=None, status=None):
        """IpsSwitchDTO

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        :param ips_type: 补丁类型，1-基础补丁 2&#x3D;虚拟补丁
        :type ips_type: int
        :param status: ips特性开关状态
        :type status: int
        """
        
        

        self._object_id = None
        self._ips_type = None
        self._status = None
        self.discriminator = None

        self.object_id = object_id
        self.ips_type = ips_type
        self.status = status

    @property
    def object_id(self):
        """Gets the object_id of this IpsSwitchDTO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this IpsSwitchDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this IpsSwitchDTO.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this IpsSwitchDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def ips_type(self):
        """Gets the ips_type of this IpsSwitchDTO.

        补丁类型，1-基础补丁 2=虚拟补丁

        :return: The ips_type of this IpsSwitchDTO.
        :rtype: int
        """
        return self._ips_type

    @ips_type.setter
    def ips_type(self, ips_type):
        """Sets the ips_type of this IpsSwitchDTO.

        补丁类型，1-基础补丁 2=虚拟补丁

        :param ips_type: The ips_type of this IpsSwitchDTO.
        :type ips_type: int
        """
        self._ips_type = ips_type

    @property
    def status(self):
        """Gets the status of this IpsSwitchDTO.

        ips特性开关状态

        :return: The status of this IpsSwitchDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IpsSwitchDTO.

        ips特性开关状态

        :param status: The status of this IpsSwitchDTO.
        :type status: int
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
        if not isinstance(other, IpsSwitchDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
