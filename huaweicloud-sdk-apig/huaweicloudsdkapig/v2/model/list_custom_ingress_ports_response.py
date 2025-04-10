# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomIngressPortsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'ingress_port_infos': 'list[IngressPortInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'ingress_port_infos': 'ingress_port_infos'
    }

    def __init__(self, size=None, total=None, ingress_port_infos=None):
        r"""ListCustomIngressPortsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param ingress_port_infos: 实例自定义入方向端口列表。
        :type ingress_port_infos: list[:class:`huaweicloudsdkapig.v2.IngressPortInfo`]
        """
        
        super(ListCustomIngressPortsResponse, self).__init__()

        self._size = None
        self._total = None
        self._ingress_port_infos = None
        self.discriminator = None

        self.size = size
        self.total = total
        if ingress_port_infos is not None:
            self.ingress_port_infos = ingress_port_infos

    @property
    def size(self):
        r"""Gets the size of this ListCustomIngressPortsResponse.

        本次返回的列表长度

        :return: The size of this ListCustomIngressPortsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCustomIngressPortsResponse.

        本次返回的列表长度

        :param size: The size of this ListCustomIngressPortsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCustomIngressPortsResponse.

        满足条件的记录数

        :return: The total of this ListCustomIngressPortsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCustomIngressPortsResponse.

        满足条件的记录数

        :param total: The total of this ListCustomIngressPortsResponse.
        :type total: int
        """
        self._total = total

    @property
    def ingress_port_infos(self):
        r"""Gets the ingress_port_infos of this ListCustomIngressPortsResponse.

        实例自定义入方向端口列表。

        :return: The ingress_port_infos of this ListCustomIngressPortsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.IngressPortInfo`]
        """
        return self._ingress_port_infos

    @ingress_port_infos.setter
    def ingress_port_infos(self, ingress_port_infos):
        r"""Sets the ingress_port_infos of this ListCustomIngressPortsResponse.

        实例自定义入方向端口列表。

        :param ingress_port_infos: The ingress_port_infos of this ListCustomIngressPortsResponse.
        :type ingress_port_infos: list[:class:`huaweicloudsdkapig.v2.IngressPortInfo`]
        """
        self._ingress_port_infos = ingress_port_infos

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
        if not isinstance(other, ListCustomIngressPortsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
