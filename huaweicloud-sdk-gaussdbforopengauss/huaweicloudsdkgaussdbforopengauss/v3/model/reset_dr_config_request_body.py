# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetDrConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opposite_data_cidr': 'str'
    }

    attribute_map = {
        'opposite_data_cidr': 'opposite_data_cidr'
    }

    def __init__(self, opposite_data_cidr=None):
        r"""ResetDrConfigRequestBody

        The model defined in huaweicloud sdk

        :param opposite_data_cidr: 对端子网IP网段或者IP，多个以英文逗号分割。
        :type opposite_data_cidr: str
        """
        
        

        self._opposite_data_cidr = None
        self.discriminator = None

        if opposite_data_cidr is not None:
            self.opposite_data_cidr = opposite_data_cidr

    @property
    def opposite_data_cidr(self):
        r"""Gets the opposite_data_cidr of this ResetDrConfigRequestBody.

        对端子网IP网段或者IP，多个以英文逗号分割。

        :return: The opposite_data_cidr of this ResetDrConfigRequestBody.
        :rtype: str
        """
        return self._opposite_data_cidr

    @opposite_data_cidr.setter
    def opposite_data_cidr(self, opposite_data_cidr):
        r"""Sets the opposite_data_cidr of this ResetDrConfigRequestBody.

        对端子网IP网段或者IP，多个以英文逗号分割。

        :param opposite_data_cidr: The opposite_data_cidr of this ResetDrConfigRequestBody.
        :type opposite_data_cidr: str
        """
        self._opposite_data_cidr = opposite_data_cidr

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
        if not isinstance(other, ResetDrConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
