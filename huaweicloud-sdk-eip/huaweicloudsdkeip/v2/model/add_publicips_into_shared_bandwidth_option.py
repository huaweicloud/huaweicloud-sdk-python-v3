# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPublicipsIntoSharedBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_info': 'list[InsertPublicipInfo]'
    }

    attribute_map = {
        'publicip_info': 'publicip_info'
    }

    def __init__(self, publicip_info=None):
        """AddPublicipsIntoSharedBandwidthOption

        The model defined in huaweicloud sdk

        :param publicip_info: 功能说明：要插入共享带宽的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.InsertPublicipInfo`]
        """
        
        

        self._publicip_info = None
        self.discriminator = None

        self.publicip_info = publicip_info

    @property
    def publicip_info(self):
        """Gets the publicip_info of this AddPublicipsIntoSharedBandwidthOption.

        功能说明：要插入共享带宽的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20

        :return: The publicip_info of this AddPublicipsIntoSharedBandwidthOption.
        :rtype: list[:class:`huaweicloudsdkeip.v2.InsertPublicipInfo`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this AddPublicipsIntoSharedBandwidthOption.

        功能说明：要插入共享带宽的弹性公网IP或者IPv6端口信息  约束：WHOLE类型的带宽支持多个弹性公网IP或者IPv6端口，跟租户的配额相关，默认一个共享带宽的配额为20

        :param publicip_info: The publicip_info of this AddPublicipsIntoSharedBandwidthOption.
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.InsertPublicipInfo`]
        """
        self._publicip_info = publicip_info

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
        if not isinstance(other, AddPublicipsIntoSharedBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
