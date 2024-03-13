# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopoRingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_info_lists': 'list[TopoInstanceInfo]'
    }

    attribute_map = {
        'instance_info_lists': 'instance_info_lists'
    }

    def __init__(self, instance_info_lists=None):
        """TopoRingInfo

        The model defined in huaweicloud sdk

        :param instance_info_lists: 集群实例列表信息
        :type instance_info_lists: list[:class:`huaweicloudsdkdws.v2.TopoInstanceInfo`]
        """
        
        

        self._instance_info_lists = None
        self.discriminator = None

        if instance_info_lists is not None:
            self.instance_info_lists = instance_info_lists

    @property
    def instance_info_lists(self):
        """Gets the instance_info_lists of this TopoRingInfo.

        集群实例列表信息

        :return: The instance_info_lists of this TopoRingInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TopoInstanceInfo`]
        """
        return self._instance_info_lists

    @instance_info_lists.setter
    def instance_info_lists(self, instance_info_lists):
        """Sets the instance_info_lists of this TopoRingInfo.

        集群实例列表信息

        :param instance_info_lists: The instance_info_lists of this TopoRingInfo.
        :type instance_info_lists: list[:class:`huaweicloudsdkdws.v2.TopoInstanceInfo`]
        """
        self._instance_info_lists = instance_info_lists

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
        if not isinstance(other, TopoRingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
