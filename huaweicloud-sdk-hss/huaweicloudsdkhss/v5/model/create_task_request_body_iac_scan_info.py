# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequestBodyIacScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_type': 'str',
        'file_id_list': 'list[str]'
    }

    attribute_map = {
        'file_type': 'file_type',
        'file_id_list': 'file_id_list'
    }

    def __init__(self, file_type=None, file_id_list=None):
        r"""CreateTaskRequestBodyIacScanInfo

        The model defined in huaweicloud sdk

        :param file_type: 文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件
        :type file_type: str
        :param file_id_list: 需要扫描的文件id列表，可以从文件上传接口“/v5/{project_id}/common/files/batch-upload”的响应数据中获取上传成功的文件id
        :type file_id_list: list[str]
        """
        
        

        self._file_type = None
        self._file_id_list = None
        self.discriminator = None

        self.file_type = file_type
        self.file_id_list = file_id_list

    @property
    def file_type(self):
        r"""Gets the file_type of this CreateTaskRequestBodyIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :return: The file_type of this CreateTaskRequestBodyIacScanInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this CreateTaskRequestBodyIacScanInfo.

        文件类型，包含如下   - dockerfile：Dockerfile文件   - k8s_yaml：k8s yaml文件

        :param file_type: The file_type of this CreateTaskRequestBodyIacScanInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_id_list(self):
        r"""Gets the file_id_list of this CreateTaskRequestBodyIacScanInfo.

        需要扫描的文件id列表，可以从文件上传接口“/v5/{project_id}/common/files/batch-upload”的响应数据中获取上传成功的文件id

        :return: The file_id_list of this CreateTaskRequestBodyIacScanInfo.
        :rtype: list[str]
        """
        return self._file_id_list

    @file_id_list.setter
    def file_id_list(self, file_id_list):
        r"""Sets the file_id_list of this CreateTaskRequestBodyIacScanInfo.

        需要扫描的文件id列表，可以从文件上传接口“/v5/{project_id}/common/files/batch-upload”的响应数据中获取上传成功的文件id

        :param file_id_list: The file_id_list of this CreateTaskRequestBodyIacScanInfo.
        :type file_id_list: list[str]
        """
        self._file_id_list = file_id_list

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
        if not isinstance(other, CreateTaskRequestBodyIacScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
