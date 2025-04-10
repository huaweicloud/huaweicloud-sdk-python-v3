# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeviceTwinResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_visitors': 'ValueInPropertyVisitors',
        'twin': 'ValueInTwinResponse',
        'access_protocol': 'str'
    }

    attribute_map = {
        'property_visitors': 'property_visitors',
        'twin': 'twin',
        'access_protocol': 'access_protocol'
    }

    def __init__(self, property_visitors=None, twin=None, access_protocol=None):
        r"""ShowDeviceTwinResponse

        The model defined in huaweicloud sdk

        :param property_visitors: 
        :type property_visitors: :class:`huaweicloudsdkief.v1.ValueInPropertyVisitors`
        :param twin: 
        :type twin: :class:`huaweicloudsdkief.v1.ValueInTwinResponse`
        :param access_protocol: 访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议
        :type access_protocol: str
        """
        
        super(ShowDeviceTwinResponse, self).__init__()

        self._property_visitors = None
        self._twin = None
        self._access_protocol = None
        self.discriminator = None

        if property_visitors is not None:
            self.property_visitors = property_visitors
        if twin is not None:
            self.twin = twin
        if access_protocol is not None:
            self.access_protocol = access_protocol

    @property
    def property_visitors(self):
        r"""Gets the property_visitors of this ShowDeviceTwinResponse.

        :return: The property_visitors of this ShowDeviceTwinResponse.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInPropertyVisitors`
        """
        return self._property_visitors

    @property_visitors.setter
    def property_visitors(self, property_visitors):
        r"""Sets the property_visitors of this ShowDeviceTwinResponse.

        :param property_visitors: The property_visitors of this ShowDeviceTwinResponse.
        :type property_visitors: :class:`huaweicloudsdkief.v1.ValueInPropertyVisitors`
        """
        self._property_visitors = property_visitors

    @property
    def twin(self):
        r"""Gets the twin of this ShowDeviceTwinResponse.

        :return: The twin of this ShowDeviceTwinResponse.
        :rtype: :class:`huaweicloudsdkief.v1.ValueInTwinResponse`
        """
        return self._twin

    @twin.setter
    def twin(self, twin):
        r"""Sets the twin of this ShowDeviceTwinResponse.

        :param twin: The twin of this ShowDeviceTwinResponse.
        :type twin: :class:`huaweicloudsdkief.v1.ValueInTwinResponse`
        """
        self._twin = twin

    @property
    def access_protocol(self):
        r"""Gets the access_protocol of this ShowDeviceTwinResponse.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议

        :return: The access_protocol of this ShowDeviceTwinResponse.
        :rtype: str
        """
        return self._access_protocol

    @access_protocol.setter
    def access_protocol(self, access_protocol):
        r"""Sets the access_protocol of this ShowDeviceTwinResponse.

        访问协议，有如下选项： - userdefine：自定义协议 - modbus：modbus协议 - opc-ua：opc-ua协议

        :param access_protocol: The access_protocol of this ShowDeviceTwinResponse.
        :type access_protocol: str
        """
        self._access_protocol = access_protocol

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
        if not isinstance(other, ShowDeviceTwinResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
