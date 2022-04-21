# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteScalingConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_configuration_id': 'str'
    }

    attribute_map = {
        'scaling_configuration_id': 'scaling_configuration_id'
    }

    def __init__(self, scaling_configuration_id=None):
        """DeleteScalingConfigRequest

        The model defined in huaweicloud sdk

        :param scaling_configuration_id: 伸缩配置ID。
        :type scaling_configuration_id: str
        """
        
        

        self._scaling_configuration_id = None
        self.discriminator = None

        self.scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this DeleteScalingConfigRequest.

        伸缩配置ID。

        :return: The scaling_configuration_id of this DeleteScalingConfigRequest.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this DeleteScalingConfigRequest.

        伸缩配置ID。

        :param scaling_configuration_id: The scaling_configuration_id of this DeleteScalingConfigRequest.
        :type scaling_configuration_id: str
        """
        self._scaling_configuration_id = scaling_configuration_id

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
        if not isinstance(other, DeleteScalingConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
