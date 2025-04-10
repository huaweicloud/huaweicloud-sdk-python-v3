# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateInstanceGlobalEipRequestBodyGlobalEip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associate_instance_info': 'AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo',
        'gc_bandwidth_info': 'AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo'
    }

    attribute_map = {
        'associate_instance_info': 'associate_instance_info',
        'gc_bandwidth_info': 'gc_bandwidth_info'
    }

    def __init__(self, associate_instance_info=None, gc_bandwidth_info=None):
        r"""AssociateInstanceGlobalEipRequestBodyGlobalEip

        The model defined in huaweicloud sdk

        :param associate_instance_info: 
        :type associate_instance_info: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo`
        :param gc_bandwidth_info: 
        :type gc_bandwidth_info: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo`
        """
        
        

        self._associate_instance_info = None
        self._gc_bandwidth_info = None
        self.discriminator = None

        if associate_instance_info is not None:
            self.associate_instance_info = associate_instance_info
        if gc_bandwidth_info is not None:
            self.gc_bandwidth_info = gc_bandwidth_info

    @property
    def associate_instance_info(self):
        r"""Gets the associate_instance_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.

        :return: The associate_instance_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.
        :rtype: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo`
        """
        return self._associate_instance_info

    @associate_instance_info.setter
    def associate_instance_info(self, associate_instance_info):
        r"""Sets the associate_instance_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.

        :param associate_instance_info: The associate_instance_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.
        :type associate_instance_info: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo`
        """
        self._associate_instance_info = associate_instance_info

    @property
    def gc_bandwidth_info(self):
        r"""Gets the gc_bandwidth_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.

        :return: The gc_bandwidth_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.
        :rtype: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo`
        """
        return self._gc_bandwidth_info

    @gc_bandwidth_info.setter
    def gc_bandwidth_info(self, gc_bandwidth_info):
        r"""Sets the gc_bandwidth_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.

        :param gc_bandwidth_info: The gc_bandwidth_info of this AssociateInstanceGlobalEipRequestBodyGlobalEip.
        :type gc_bandwidth_info: :class:`huaweicloudsdkgeip.v3.AssociateInstanceGlobalEipRequestBodyGlobalEipGcBandwidthInfo`
        """
        self._gc_bandwidth_info = gc_bandwidth_info

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
        if not isinstance(other, AssociateInstanceGlobalEipRequestBodyGlobalEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
