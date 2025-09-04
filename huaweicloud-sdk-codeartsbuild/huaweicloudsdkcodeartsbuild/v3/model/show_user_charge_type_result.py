# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserChargeTypeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'charge_type': 'str',
        'main_resource_list': 'list[ShowUserChargeTypeResultMainResourceList]'
    }

    attribute_map = {
        'type': 'type',
        'charge_type': 'charge_type',
        'main_resource_list': 'main_resource_list'
    }

    def __init__(self, type=None, charge_type=None, main_resource_list=None):
        r"""ShowUserChargeTypeResult

        The model defined in huaweicloud sdk

        :param type: 套餐类型
        :type type: str
        :param charge_type: 计费类型
        :type charge_type: str
        :param main_resource_list: 计费类型
        :type main_resource_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowUserChargeTypeResultMainResourceList`]
        """
        
        

        self._type = None
        self._charge_type = None
        self._main_resource_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if charge_type is not None:
            self.charge_type = charge_type
        if main_resource_list is not None:
            self.main_resource_list = main_resource_list

    @property
    def type(self):
        r"""Gets the type of this ShowUserChargeTypeResult.

        套餐类型

        :return: The type of this ShowUserChargeTypeResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowUserChargeTypeResult.

        套餐类型

        :param type: The type of this ShowUserChargeTypeResult.
        :type type: str
        """
        self._type = type

    @property
    def charge_type(self):
        r"""Gets the charge_type of this ShowUserChargeTypeResult.

        计费类型

        :return: The charge_type of this ShowUserChargeTypeResult.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        r"""Sets the charge_type of this ShowUserChargeTypeResult.

        计费类型

        :param charge_type: The charge_type of this ShowUserChargeTypeResult.
        :type charge_type: str
        """
        self._charge_type = charge_type

    @property
    def main_resource_list(self):
        r"""Gets the main_resource_list of this ShowUserChargeTypeResult.

        计费类型

        :return: The main_resource_list of this ShowUserChargeTypeResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowUserChargeTypeResultMainResourceList`]
        """
        return self._main_resource_list

    @main_resource_list.setter
    def main_resource_list(self, main_resource_list):
        r"""Sets the main_resource_list of this ShowUserChargeTypeResult.

        计费类型

        :param main_resource_list: The main_resource_list of this ShowUserChargeTypeResult.
        :type main_resource_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowUserChargeTypeResultMainResourceList`]
        """
        self._main_resource_list = main_resource_list

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
        if not isinstance(other, ShowUserChargeTypeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
