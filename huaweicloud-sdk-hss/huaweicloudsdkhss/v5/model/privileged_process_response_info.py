# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivilegedProcessResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_file_path': 'str'
    }

    attribute_map = {
        'process_file_path': 'process_file_path'
    }

    def __init__(self, process_file_path=None):
        r"""PrivilegedProcessResponseInfo

        The model defined in huaweicloud sdk

        :param process_file_path: 特权进程文件路径
        :type process_file_path: str
        """
        
        

        self._process_file_path = None
        self.discriminator = None

        if process_file_path is not None:
            self.process_file_path = process_file_path

    @property
    def process_file_path(self):
        r"""Gets the process_file_path of this PrivilegedProcessResponseInfo.

        特权进程文件路径

        :return: The process_file_path of this PrivilegedProcessResponseInfo.
        :rtype: str
        """
        return self._process_file_path

    @process_file_path.setter
    def process_file_path(self, process_file_path):
        r"""Sets the process_file_path of this PrivilegedProcessResponseInfo.

        特权进程文件路径

        :param process_file_path: The process_file_path of this PrivilegedProcessResponseInfo.
        :type process_file_path: str
        """
        self._process_file_path = process_file_path

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
        if not isinstance(other, PrivilegedProcessResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
