# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDrugJobBasicInfo:

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
        'labels': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'labels': 'labels'
    }

    def __init__(self, name=None, labels=None):
        r"""CreateDrugJobBasicInfo

        The model defined in huaweicloud sdk

        :param name: 作业的名称，取值范围：[5,64]，允许大小写字母、数字、空格、下划线(_)和中划线(-),只能以数字或字母开头
        :type name: str
        :param labels: 标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。
        :type labels: list[str]
        """
        
        

        self._name = None
        self._labels = None
        self.discriminator = None

        self.name = name
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        r"""Gets the name of this CreateDrugJobBasicInfo.

        作业的名称，取值范围：[5,64]，允许大小写字母、数字、空格、下划线(_)和中划线(-),只能以数字或字母开头

        :return: The name of this CreateDrugJobBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDrugJobBasicInfo.

        作业的名称，取值范围：[5,64]，允许大小写字母、数字、空格、下划线(_)和中划线(-),只能以数字或字母开头

        :param name: The name of this CreateDrugJobBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        r"""Gets the labels of this CreateDrugJobBasicInfo.

        标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :return: The labels of this CreateDrugJobBasicInfo.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateDrugJobBasicInfo.

        标签，取值范围[0,5]，单个标签最大长度32字符，支持中文、字母、数字、空格、下划线和中划线，且不能以空格开头或者结尾。

        :param labels: The labels of this CreateDrugJobBasicInfo.
        :type labels: list[str]
        """
        self._labels = labels

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
        if not isinstance(other, CreateDrugJobBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
