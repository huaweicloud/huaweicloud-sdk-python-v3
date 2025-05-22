# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DualActiveRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination_region': 'str',
        'destination_instance_id': 'str'
    }

    attribute_map = {
        'destination_region': 'destination_region',
        'destination_instance_id': 'destination_instance_id'
    }

    def __init__(self, destination_region=None, destination_instance_id=None):
        r"""DualActiveRequestBody

        The model defined in huaweicloud sdk

        :param destination_region: 参数解释 搭建双活目标实例所在的region。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。
        :type destination_region: str
        :param destination_instance_id: 参数解释 搭建双活目标实例ID。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。
        :type destination_instance_id: str
        """
        
        

        self._destination_region = None
        self._destination_instance_id = None
        self.discriminator = None

        self.destination_region = destination_region
        self.destination_instance_id = destination_instance_id

    @property
    def destination_region(self):
        r"""Gets the destination_region of this DualActiveRequestBody.

        参数解释 搭建双活目标实例所在的region。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。

        :return: The destination_region of this DualActiveRequestBody.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this DualActiveRequestBody.

        参数解释 搭建双活目标实例所在的region。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。

        :param destination_region: The destination_region of this DualActiveRequestBody.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_instance_id(self):
        r"""Gets the destination_instance_id of this DualActiveRequestBody.

        参数解释 搭建双活目标实例ID。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。

        :return: The destination_instance_id of this DualActiveRequestBody.
        :rtype: str
        """
        return self._destination_instance_id

    @destination_instance_id.setter
    def destination_instance_id(self, destination_instance_id):
        r"""Sets the destination_instance_id of this DualActiveRequestBody.

        参数解释 搭建双活目标实例ID。 约束限制 不涉及。 取值范围 不涉及。 默认取值 不涉及。

        :param destination_instance_id: The destination_instance_id of this DualActiveRequestBody.
        :type destination_instance_id: str
        """
        self._destination_instance_id = destination_instance_id

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
        if not isinstance(other, DualActiveRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
