# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSourceIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_ip': 'list[IpsItem]',
        'last_modify': 'int'
    }

    attribute_map = {
        'source_ip': 'source_ip',
        'last_modify': 'last_modify'
    }

    def __init__(self, source_ip=None, last_modify=None):
        """ShowSourceIpResponse

        The model defined in huaweicloud sdk

        :param source_ip: 源站信息列表
        :type source_ip: list[:class:`huaweicloudsdkwaf.v1.IpsItem`]
        :param last_modify: 回源Ip最后更新时间
        :type last_modify: int
        """
        
        super(ShowSourceIpResponse, self).__init__()

        self._source_ip = None
        self._last_modify = None
        self.discriminator = None

        if source_ip is not None:
            self.source_ip = source_ip
        if last_modify is not None:
            self.last_modify = last_modify

    @property
    def source_ip(self):
        """Gets the source_ip of this ShowSourceIpResponse.

        源站信息列表

        :return: The source_ip of this ShowSourceIpResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IpsItem`]
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this ShowSourceIpResponse.

        源站信息列表

        :param source_ip: The source_ip of this ShowSourceIpResponse.
        :type source_ip: list[:class:`huaweicloudsdkwaf.v1.IpsItem`]
        """
        self._source_ip = source_ip

    @property
    def last_modify(self):
        """Gets the last_modify of this ShowSourceIpResponse.

        回源Ip最后更新时间

        :return: The last_modify of this ShowSourceIpResponse.
        :rtype: int
        """
        return self._last_modify

    @last_modify.setter
    def last_modify(self, last_modify):
        """Sets the last_modify of this ShowSourceIpResponse.

        回源Ip最后更新时间

        :param last_modify: The last_modify of this ShowSourceIpResponse.
        :type last_modify: int
        """
        self._last_modify = last_modify

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
        if not isinstance(other, ShowSourceIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
