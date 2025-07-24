# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerInstanceIdSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id_set': 'list[str]'
    }

    attribute_map = {
        'instance_id_set': 'instance_id_set'
    }

    def __init__(self, instance_id_set=None):
        r"""ServerInstanceIdSet

        The model defined in huaweicloud sdk

        :param instance_id_set: instance id set
        :type instance_id_set: list[str]
        """
        
        

        self._instance_id_set = None
        self.discriminator = None

        if instance_id_set is not None:
            self.instance_id_set = instance_id_set

    @property
    def instance_id_set(self):
        r"""Gets the instance_id_set of this ServerInstanceIdSet.

        instance id set

        :return: The instance_id_set of this ServerInstanceIdSet.
        :rtype: list[str]
        """
        return self._instance_id_set

    @instance_id_set.setter
    def instance_id_set(self, instance_id_set):
        r"""Sets the instance_id_set of this ServerInstanceIdSet.

        instance id set

        :param instance_id_set: The instance_id_set of this ServerInstanceIdSet.
        :type instance_id_set: list[str]
        """
        self._instance_id_set = instance_id_set

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
        if not isinstance(other, ServerInstanceIdSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
