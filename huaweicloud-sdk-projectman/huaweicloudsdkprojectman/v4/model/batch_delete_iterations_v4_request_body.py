# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteIterationsV4RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'iteration_ids': 'list[int]'
    }

    attribute_map = {
        'iteration_ids': 'iteration_ids'
    }

    def __init__(self, iteration_ids=None):
        """BatchDeleteIterationsV4RequestBody

        The model defined in huaweicloud sdk

        :param iteration_ids: 迭代的id
        :type iteration_ids: list[int]
        """
        
        

        self._iteration_ids = None
        self.discriminator = None

        self.iteration_ids = iteration_ids

    @property
    def iteration_ids(self):
        """Gets the iteration_ids of this BatchDeleteIterationsV4RequestBody.

        迭代的id

        :return: The iteration_ids of this BatchDeleteIterationsV4RequestBody.
        :rtype: list[int]
        """
        return self._iteration_ids

    @iteration_ids.setter
    def iteration_ids(self, iteration_ids):
        """Sets the iteration_ids of this BatchDeleteIterationsV4RequestBody.

        迭代的id

        :param iteration_ids: The iteration_ids of this BatchDeleteIterationsV4RequestBody.
        :type iteration_ids: list[int]
        """
        self._iteration_ids = iteration_ids

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
        if not isinstance(other, BatchDeleteIterationsV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
