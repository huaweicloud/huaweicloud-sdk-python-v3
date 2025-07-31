# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequestBodyIacScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_type': 'str'
    }

    attribute_map = {
        'file_type': 'file_type'
    }

    def __init__(self, file_type=None):
        r"""ListTasksRequestBodyIacScanInfo

        The model defined in huaweicloud sdk

        :param file_type: 文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件
        :type file_type: str
        """
        
        

        self._file_type = None
        self.discriminator = None

        if file_type is not None:
            self.file_type = file_type

    @property
    def file_type(self):
        r"""Gets the file_type of this ListTasksRequestBodyIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :return: The file_type of this ListTasksRequestBodyIacScanInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ListTasksRequestBodyIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :param file_type: The file_type of this ListTasksRequestBodyIacScanInfo.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, ListTasksRequestBodyIacScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
