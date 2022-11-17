# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'identity_info': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'identity_info': 'identity_info'
    }

    def __init__(self, file_path=None, identity_info=None):
        """VulnRule

        The model defined in huaweicloud sdk

        :param file_path: 问题文件
        :type file_path: str
        :param identity_info: 特征信息
        :type identity_info: str
        """
        
        

        self._file_path = None
        self._identity_info = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if identity_info is not None:
            self.identity_info = identity_info

    @property
    def file_path(self):
        """Gets the file_path of this VulnRule.

        问题文件

        :return: The file_path of this VulnRule.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this VulnRule.

        问题文件

        :param file_path: The file_path of this VulnRule.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def identity_info(self):
        """Gets the identity_info of this VulnRule.

        特征信息

        :return: The identity_info of this VulnRule.
        :rtype: str
        """
        return self._identity_info

    @identity_info.setter
    def identity_info(self, identity_info):
        """Sets the identity_info of this VulnRule.

        特征信息

        :param identity_info: The identity_info of this VulnRule.
        :type identity_info: str
        """
        self._identity_info = identity_info

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
        if not isinstance(other, VulnRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
