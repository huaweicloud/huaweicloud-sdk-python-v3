# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchedulerHints:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dec_baremetal': 'list[str]'
    }

    attribute_map = {
        'dec_baremetal': 'dec_baremetal'
    }

    def __init__(self, dec_baremetal=None):
        """SchedulerHints - a model defined in huaweicloud sdk"""
        
        

        self._dec_baremetal = None
        self.discriminator = None

        if dec_baremetal is not None:
            self.dec_baremetal = dec_baremetal

    @property
    def dec_baremetal(self):
        """Gets the dec_baremetal of this SchedulerHints.

        是否在专属云中创建裸金属服务器，参数值为share或dedicate。约束：该值不传时默认为share。在专属云中创建裸金属服务器时，必须指定该字段为dedicate。

        :return: The dec_baremetal of this SchedulerHints.
        :rtype: list[str]
        """
        return self._dec_baremetal

    @dec_baremetal.setter
    def dec_baremetal(self, dec_baremetal):
        """Sets the dec_baremetal of this SchedulerHints.

        是否在专属云中创建裸金属服务器，参数值为share或dedicate。约束：该值不传时默认为share。在专属云中创建裸金属服务器时，必须指定该字段为dedicate。

        :param dec_baremetal: The dec_baremetal of this SchedulerHints.
        :type: list[str]
        """
        self._dec_baremetal = dec_baremetal

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
