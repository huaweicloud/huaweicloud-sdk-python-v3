# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveFromSharedBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'publicip_info': 'list[RemovePublicipInfo]',
        'size': 'int'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'publicip_info': 'publicip_info',
        'size': 'size'
    }

    def __init__(self, charge_mode=None, publicip_info=None, size=None):
        """RemoveFromSharedBandwidthOption

        The model defined in huaweicloud sdk

        :param charge_mode: 弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的计费类型。（bandwidth/traffic）
        :type charge_mode: str
        :param publicip_info: 功能说明：要从共享带宽中移除的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.RemovePublicipInfo`]
        :param size: 弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的带宽大小。（M）取值范围：默认为1~2000Mbit/s. 可能因为局点配置不同而不同。也跟带宽的计费模式（bandwidth/traffic）相关。
        :type size: int
        """
        
        

        self._charge_mode = None
        self._publicip_info = None
        self._size = None
        self.discriminator = None

        self.charge_mode = charge_mode
        self.publicip_info = publicip_info
        self.size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this RemoveFromSharedBandwidthOption.

        弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的计费类型。（bandwidth/traffic）

        :return: The charge_mode of this RemoveFromSharedBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this RemoveFromSharedBandwidthOption.

        弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的计费类型。（bandwidth/traffic）

        :param charge_mode: The charge_mode of this RemoveFromSharedBandwidthOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def publicip_info(self):
        """Gets the publicip_info of this RemoveFromSharedBandwidthOption.

        功能说明：要从共享带宽中移除的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20

        :return: The publicip_info of this RemoveFromSharedBandwidthOption.
        :rtype: list[:class:`huaweicloudsdkeip.v2.RemovePublicipInfo`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this RemoveFromSharedBandwidthOption.

        功能说明：要从共享带宽中移除的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20

        :param publicip_info: The publicip_info of this RemoveFromSharedBandwidthOption.
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.RemovePublicipInfo`]
        """
        self._publicip_info = publicip_info

    @property
    def size(self):
        """Gets the size of this RemoveFromSharedBandwidthOption.

        弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的带宽大小。（M）取值范围：默认为1~2000Mbit/s. 可能因为局点配置不同而不同。也跟带宽的计费模式（bandwidth/traffic）相关。

        :return: The size of this RemoveFromSharedBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RemoveFromSharedBandwidthOption.

        弹性公网IP从共享带宽移除后，会为此弹性公网IP创建独占带宽进行计费。  此参数表示弹性公网IP从共享带宽移除后，使用的独占带宽的带宽大小。（M）取值范围：默认为1~2000Mbit/s. 可能因为局点配置不同而不同。也跟带宽的计费模式（bandwidth/traffic）相关。

        :param size: The size of this RemoveFromSharedBandwidthOption.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, RemoveFromSharedBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
