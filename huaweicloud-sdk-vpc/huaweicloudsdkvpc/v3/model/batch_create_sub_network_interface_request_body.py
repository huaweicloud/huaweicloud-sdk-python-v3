# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSubNetworkInterfaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'sub_network_interface': 'BatchCreateSubNetworkInterfaceOption',
        'count': 'int'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'sub_network_interface': 'sub_network_interface',
        'count': 'count'
    }

    def __init__(self, dry_run=None, sub_network_interface=None, count=None):
        """BatchCreateSubNetworkInterfaceRequestBody

        The model defined in huaweicloud sdk

        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。
        :type dry_run: bool
        :param sub_network_interface: 
        :type sub_network_interface: :class:`huaweicloudsdkvpc.v3.BatchCreateSubNetworkInterfaceOption`
        :param count: 批量创建辅助弹性网卡的个数
        :type count: int
        """
        
        

        self._dry_run = None
        self._sub_network_interface = None
        self._count = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.sub_network_interface = sub_network_interface
        self.count = count

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchCreateSubNetworkInterfaceRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。

        :return: The dry_run of this BatchCreateSubNetworkInterfaceRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchCreateSubNetworkInterfaceRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建辅助弹性网卡。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建辅助弹性网卡。

        :param dry_run: The dry_run of this BatchCreateSubNetworkInterfaceRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def sub_network_interface(self):
        """Gets the sub_network_interface of this BatchCreateSubNetworkInterfaceRequestBody.


        :return: The sub_network_interface of this BatchCreateSubNetworkInterfaceRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.BatchCreateSubNetworkInterfaceOption`
        """
        return self._sub_network_interface

    @sub_network_interface.setter
    def sub_network_interface(self, sub_network_interface):
        """Sets the sub_network_interface of this BatchCreateSubNetworkInterfaceRequestBody.


        :param sub_network_interface: The sub_network_interface of this BatchCreateSubNetworkInterfaceRequestBody.
        :type sub_network_interface: :class:`huaweicloudsdkvpc.v3.BatchCreateSubNetworkInterfaceOption`
        """
        self._sub_network_interface = sub_network_interface

    @property
    def count(self):
        """Gets the count of this BatchCreateSubNetworkInterfaceRequestBody.

        批量创建辅助弹性网卡的个数

        :return: The count of this BatchCreateSubNetworkInterfaceRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchCreateSubNetworkInterfaceRequestBody.

        批量创建辅助弹性网卡的个数

        :param count: The count of this BatchCreateSubNetworkInterfaceRequestBody.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, BatchCreateSubNetworkInterfaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
