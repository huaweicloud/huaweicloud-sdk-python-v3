# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIterationV4Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iteration_id': 'int'
    }

    attribute_map = {
        'iteration_id': 'iteration_id'
    }

    def __init__(self, iteration_id=None):
        r"""ShowIterationV4Request

        The model defined in huaweicloud sdk

        :param iteration_id: 迭代id
        :type iteration_id: int
        """
        
        

        self._iteration_id = None
        self.discriminator = None

        self.iteration_id = iteration_id

    @property
    def iteration_id(self):
        r"""Gets the iteration_id of this ShowIterationV4Request.

        迭代id

        :return: The iteration_id of this ShowIterationV4Request.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        r"""Sets the iteration_id of this ShowIterationV4Request.

        迭代id

        :param iteration_id: The iteration_id of this ShowIterationV4Request.
        :type iteration_id: int
        """
        self._iteration_id = iteration_id

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
        if not isinstance(other, ShowIterationV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
