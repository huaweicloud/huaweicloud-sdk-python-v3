# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartInstanceResizeCheckJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_capacity': 'int',
        'spec_code': 'str'
    }

    attribute_map = {
        'new_capacity': 'new_capacity',
        'spec_code': 'spec_code'
    }

    def __init__(self, new_capacity=None, spec_code=None):
        """StartInstanceResizeCheckJobRequestBody

        The model defined in huaweicloud sdk

        :param new_capacity: 新规格的容量，单位GB
        :type new_capacity: int
        :param spec_code: 新的规格编码
        :type spec_code: str
        """
        
        

        self._new_capacity = None
        self._spec_code = None
        self.discriminator = None

        if new_capacity is not None:
            self.new_capacity = new_capacity
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def new_capacity(self):
        """Gets the new_capacity of this StartInstanceResizeCheckJobRequestBody.

        新规格的容量，单位GB

        :return: The new_capacity of this StartInstanceResizeCheckJobRequestBody.
        :rtype: int
        """
        return self._new_capacity

    @new_capacity.setter
    def new_capacity(self, new_capacity):
        """Sets the new_capacity of this StartInstanceResizeCheckJobRequestBody.

        新规格的容量，单位GB

        :param new_capacity: The new_capacity of this StartInstanceResizeCheckJobRequestBody.
        :type new_capacity: int
        """
        self._new_capacity = new_capacity

    @property
    def spec_code(self):
        """Gets the spec_code of this StartInstanceResizeCheckJobRequestBody.

        新的规格编码

        :return: The spec_code of this StartInstanceResizeCheckJobRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this StartInstanceResizeCheckJobRequestBody.

        新的规格编码

        :param spec_code: The spec_code of this StartInstanceResizeCheckJobRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, StartInstanceResizeCheckJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
