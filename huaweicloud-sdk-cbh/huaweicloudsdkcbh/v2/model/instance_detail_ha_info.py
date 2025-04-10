# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailHaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ha_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'ha_id': 'ha_id',
        'instance_type': 'instance_type'
    }

    def __init__(self, ha_id=None, instance_type=None):
        r"""InstanceDetailHaInfo

        The model defined in huaweicloud sdk

        :param ha_id: 主备ID。
        :type ha_id: str
        :param instance_type: 实例类型。 - master：主 - slave：备
        :type instance_type: str
        """
        
        

        self._ha_id = None
        self._instance_type = None
        self.discriminator = None

        self.ha_id = ha_id
        self.instance_type = instance_type

    @property
    def ha_id(self):
        r"""Gets the ha_id of this InstanceDetailHaInfo.

        主备ID。

        :return: The ha_id of this InstanceDetailHaInfo.
        :rtype: str
        """
        return self._ha_id

    @ha_id.setter
    def ha_id(self, ha_id):
        r"""Sets the ha_id of this InstanceDetailHaInfo.

        主备ID。

        :param ha_id: The ha_id of this InstanceDetailHaInfo.
        :type ha_id: str
        """
        self._ha_id = ha_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this InstanceDetailHaInfo.

        实例类型。 - master：主 - slave：备

        :return: The instance_type of this InstanceDetailHaInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this InstanceDetailHaInfo.

        实例类型。 - master：主 - slave：备

        :param instance_type: The instance_type of this InstanceDetailHaInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, InstanceDetailHaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
