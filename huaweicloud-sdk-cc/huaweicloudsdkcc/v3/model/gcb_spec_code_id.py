# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbSpecCodeId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code_id': 'str'
    }

    attribute_map = {
        'spec_code_id': 'spec_code_id'
    }

    def __init__(self, spec_code_id=None):
        """GcbSpecCodeId

        The model defined in huaweicloud sdk

        :param spec_code_id: 功能说明：线路规格编码UUID。
        :type spec_code_id: str
        """
        
        

        self._spec_code_id = None
        self.discriminator = None

        if spec_code_id is not None:
            self.spec_code_id = spec_code_id

    @property
    def spec_code_id(self):
        """Gets the spec_code_id of this GcbSpecCodeId.

        功能说明：线路规格编码UUID。

        :return: The spec_code_id of this GcbSpecCodeId.
        :rtype: str
        """
        return self._spec_code_id

    @spec_code_id.setter
    def spec_code_id(self, spec_code_id):
        """Sets the spec_code_id of this GcbSpecCodeId.

        功能说明：线路规格编码UUID。

        :param spec_code_id: The spec_code_id of this GcbSpecCodeId.
        :type spec_code_id: str
        """
        self._spec_code_id = spec_code_id

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
        if not isinstance(other, GcbSpecCodeId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
