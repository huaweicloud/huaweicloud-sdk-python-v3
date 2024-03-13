# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStorageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format_list': 'str',
        'in_project': 'str'
    }

    attribute_map = {
        'format_list': 'format_list',
        'in_project': 'in_project'
    }

    def __init__(self, format_list=None, in_project=None):
        """ShowStorageRequest

        The model defined in huaweicloud sdk

        :param format_list: 类型列表
        :type format_list: str
        :param in_project: 是否在项目中
        :type in_project: str
        """
        
        

        self._format_list = None
        self._in_project = None
        self.discriminator = None

        if format_list is not None:
            self.format_list = format_list
        if in_project is not None:
            self.in_project = in_project

    @property
    def format_list(self):
        """Gets the format_list of this ShowStorageRequest.

        类型列表

        :return: The format_list of this ShowStorageRequest.
        :rtype: str
        """
        return self._format_list

    @format_list.setter
    def format_list(self, format_list):
        """Sets the format_list of this ShowStorageRequest.

        类型列表

        :param format_list: The format_list of this ShowStorageRequest.
        :type format_list: str
        """
        self._format_list = format_list

    @property
    def in_project(self):
        """Gets the in_project of this ShowStorageRequest.

        是否在项目中

        :return: The in_project of this ShowStorageRequest.
        :rtype: str
        """
        return self._in_project

    @in_project.setter
    def in_project(self, in_project):
        """Sets the in_project of this ShowStorageRequest.

        是否在项目中

        :param in_project: The in_project of this ShowStorageRequest.
        :type in_project: str
        """
        self._in_project = in_project

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
        if not isinstance(other, ShowStorageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
