# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDosStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'limit': 'str',
        'offset': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset',
        'ip': 'ip'
    }

    def __init__(self, status=None, limit=None, offset=None, ip=None):
        """ListDDosStatusRequest

        The model defined in huaweicloud sdk

        :param status: 可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞  不带此参数默认所有列表，以neutron查询到的顺序为准。
        :type status: str
        :param limit: 返回结果个数限制，取值范围：1~100
        :type limit: str
        :param offset: 偏移量，取值范围：0~2147483647
        :type offset: str
        :param ip: IP地址，支持IPv4格式和IPv6格式输入，支持部分查询。例如“？ip&#x3D;192.168”，会返回192.168.111.1和10.192.168.8所对应的EIP防护状态。
        :type ip: str
        """
        
        

        self._status = None
        self._limit = None
        self._offset = None
        self._ip = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ip is not None:
            self.ip = ip

    @property
    def status(self):
        """Gets the status of this ListDDosStatusRequest.

        可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞  不带此参数默认所有列表，以neutron查询到的顺序为准。

        :return: The status of this ListDDosStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDDosStatusRequest.

        可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞  不带此参数默认所有列表，以neutron查询到的顺序为准。

        :param status: The status of this ListDDosStatusRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListDDosStatusRequest.

        返回结果个数限制，取值范围：1~100

        :return: The limit of this ListDDosStatusRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDDosStatusRequest.

        返回结果个数限制，取值范围：1~100

        :param limit: The limit of this ListDDosStatusRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDDosStatusRequest.

        偏移量，取值范围：0~2147483647

        :return: The offset of this ListDDosStatusRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDDosStatusRequest.

        偏移量，取值范围：0~2147483647

        :param offset: The offset of this ListDDosStatusRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def ip(self):
        """Gets the ip of this ListDDosStatusRequest.

        IP地址，支持IPv4格式和IPv6格式输入，支持部分查询。例如“？ip=192.168”，会返回192.168.111.1和10.192.168.8所对应的EIP防护状态。

        :return: The ip of this ListDDosStatusRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListDDosStatusRequest.

        IP地址，支持IPv4格式和IPv6格式输入，支持部分查询。例如“？ip=192.168”，会返回192.168.111.1和10.192.168.8所对应的EIP防护状态。

        :param ip: The ip of this ListDDosStatusRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ListDDosStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
