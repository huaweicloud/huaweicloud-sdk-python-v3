# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineDirectoryInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable'
    }

    def __init__(self, name=None, enable=None):
        r"""ShowBaselineDirectoryInfoDataList

        The model defined in huaweicloud sdk

        :param name: 根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表tag（基线检查项的类型） - 当select_type为tag，该字段代表check_type（基线的名称）
        :type name: str
        :param enable: 该项是否被选中
        :type enable: bool
        """
        
        

        self._name = None
        self._enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable is not None:
            self.enable = enable

    @property
    def name(self):
        r"""Gets the name of this ShowBaselineDirectoryInfoDataList.

        根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表tag（基线检查项的类型） - 当select_type为tag，该字段代表check_type（基线的名称）

        :return: The name of this ShowBaselineDirectoryInfoDataList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBaselineDirectoryInfoDataList.

        根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表tag（基线检查项的类型） - 当select_type为tag，该字段代表check_type（基线的名称）

        :param name: The name of this ShowBaselineDirectoryInfoDataList.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this ShowBaselineDirectoryInfoDataList.

        该项是否被选中

        :return: The enable of this ShowBaselineDirectoryInfoDataList.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowBaselineDirectoryInfoDataList.

        该项是否被选中

        :param enable: The enable of this ShowBaselineDirectoryInfoDataList.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, ShowBaselineDirectoryInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
