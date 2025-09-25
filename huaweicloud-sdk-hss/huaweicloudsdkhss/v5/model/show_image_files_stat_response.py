# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageFilesStatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_files_num': 'int',
        'total_files_size': 'int'
    }

    attribute_map = {
        'total_files_num': 'total_files_num',
        'total_files_size': 'total_files_size'
    }

    def __init__(self, total_files_num=None, total_files_size=None):
        r"""ShowImageFilesStatResponse

        The model defined in huaweicloud sdk

        :param total_files_num: 镜像文件总数
        :type total_files_num: int
        :param total_files_size: 镜像文件大小
        :type total_files_size: int
        """
        
        super(ShowImageFilesStatResponse, self).__init__()

        self._total_files_num = None
        self._total_files_size = None
        self.discriminator = None

        if total_files_num is not None:
            self.total_files_num = total_files_num
        if total_files_size is not None:
            self.total_files_size = total_files_size

    @property
    def total_files_num(self):
        r"""Gets the total_files_num of this ShowImageFilesStatResponse.

        镜像文件总数

        :return: The total_files_num of this ShowImageFilesStatResponse.
        :rtype: int
        """
        return self._total_files_num

    @total_files_num.setter
    def total_files_num(self, total_files_num):
        r"""Sets the total_files_num of this ShowImageFilesStatResponse.

        镜像文件总数

        :param total_files_num: The total_files_num of this ShowImageFilesStatResponse.
        :type total_files_num: int
        """
        self._total_files_num = total_files_num

    @property
    def total_files_size(self):
        r"""Gets the total_files_size of this ShowImageFilesStatResponse.

        镜像文件大小

        :return: The total_files_size of this ShowImageFilesStatResponse.
        :rtype: int
        """
        return self._total_files_size

    @total_files_size.setter
    def total_files_size(self, total_files_size):
        r"""Sets the total_files_size of this ShowImageFilesStatResponse.

        镜像文件大小

        :param total_files_size: The total_files_size of this ShowImageFilesStatResponse.
        :type total_files_size: int
        """
        self._total_files_size = total_files_size

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
        if not isinstance(other, ShowImageFilesStatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
