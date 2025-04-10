# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLakeFormationInstanceScale:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specs': 'list[CreateSpec]'
    }

    attribute_map = {
        'specs': 'specs'
    }

    def __init__(self, specs=None):
        r"""UpdateLakeFormationInstanceScale

        The model defined in huaweicloud sdk

        :param specs: 规格列表
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        
        

        self._specs = None
        self.discriminator = None

        if specs is not None:
            self.specs = specs

    @property
    def specs(self):
        r"""Gets the specs of this UpdateLakeFormationInstanceScale.

        规格列表

        :return: The specs of this UpdateLakeFormationInstanceScale.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        r"""Sets the specs of this UpdateLakeFormationInstanceScale.

        规格列表

        :param specs: The specs of this UpdateLakeFormationInstanceScale.
        :type specs: list[:class:`huaweicloudsdklakeformation.v1.CreateSpec`]
        """
        self._specs = specs

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
        if not isinstance(other, UpdateLakeFormationInstanceScale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
