# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerExtraMysqlInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_path': 'str'
    }

    attribute_map = {
        'custom_path': 'custom_path'
    }

    def __init__(self, custom_path=None):
        r"""ContainerExtraMysqlInfo

        The model defined in huaweicloud sdk

        :param custom_path: 自定义反制路径
        :type custom_path: str
        """
        
        

        self._custom_path = None
        self.discriminator = None

        if custom_path is not None:
            self.custom_path = custom_path

    @property
    def custom_path(self):
        r"""Gets the custom_path of this ContainerExtraMysqlInfo.

        自定义反制路径

        :return: The custom_path of this ContainerExtraMysqlInfo.
        :rtype: str
        """
        return self._custom_path

    @custom_path.setter
    def custom_path(self, custom_path):
        r"""Sets the custom_path of this ContainerExtraMysqlInfo.

        自定义反制路径

        :param custom_path: The custom_path of this ContainerExtraMysqlInfo.
        :type custom_path: str
        """
        self._custom_path = custom_path

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
        if not isinstance(other, ContainerExtraMysqlInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
