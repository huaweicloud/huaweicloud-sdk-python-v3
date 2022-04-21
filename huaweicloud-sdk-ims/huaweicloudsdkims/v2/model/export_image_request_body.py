# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket_url': 'str',
        'file_format': 'str',
        'is_quick_export': 'bool'
    }

    attribute_map = {
        'bucket_url': 'bucket_url',
        'file_format': 'file_format',
        'is_quick_export': 'is_quick_export'
    }

    def __init__(self, bucket_url=None, file_format=None, is_quick_export=None):
        """ExportImageRequestBody

        The model defined in huaweicloud sdk

        :param bucket_url: 目的文件的URL，格式：&lt;bucket&gt;:&lt;file&gt;。 说明：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。
        :type bucket_url: str
        :param file_format: 文件格式，支持qcow2、vhd、zvhd和vmdk。
        :type file_format: str
        :param is_quick_export: 是否使用快速导出，取值为true或者false。 说明：若使用快速导出，则无法指定file_format参数。
        :type is_quick_export: bool
        """
        
        

        self._bucket_url = None
        self._file_format = None
        self._is_quick_export = None
        self.discriminator = None

        self.bucket_url = bucket_url
        self.file_format = file_format
        if is_quick_export is not None:
            self.is_quick_export = is_quick_export

    @property
    def bucket_url(self):
        """Gets the bucket_url of this ExportImageRequestBody.

        目的文件的URL，格式：<bucket>:<file>。 说明：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :return: The bucket_url of this ExportImageRequestBody.
        :rtype: str
        """
        return self._bucket_url

    @bucket_url.setter
    def bucket_url(self, bucket_url):
        """Sets the bucket_url of this ExportImageRequestBody.

        目的文件的URL，格式：<bucket>:<file>。 说明：此处的OBS桶和镜像文件的存储类别必须是OBS标准存储。

        :param bucket_url: The bucket_url of this ExportImageRequestBody.
        :type bucket_url: str
        """
        self._bucket_url = bucket_url

    @property
    def file_format(self):
        """Gets the file_format of this ExportImageRequestBody.

        文件格式，支持qcow2、vhd、zvhd和vmdk。

        :return: The file_format of this ExportImageRequestBody.
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this ExportImageRequestBody.

        文件格式，支持qcow2、vhd、zvhd和vmdk。

        :param file_format: The file_format of this ExportImageRequestBody.
        :type file_format: str
        """
        self._file_format = file_format

    @property
    def is_quick_export(self):
        """Gets the is_quick_export of this ExportImageRequestBody.

        是否使用快速导出，取值为true或者false。 说明：若使用快速导出，则无法指定file_format参数。

        :return: The is_quick_export of this ExportImageRequestBody.
        :rtype: bool
        """
        return self._is_quick_export

    @is_quick_export.setter
    def is_quick_export(self, is_quick_export):
        """Sets the is_quick_export of this ExportImageRequestBody.

        是否使用快速导出，取值为true或者false。 说明：若使用快速导出，则无法指定file_format参数。

        :param is_quick_export: The is_quick_export of this ExportImageRequestBody.
        :type is_quick_export: bool
        """
        self._is_quick_export = is_quick_export

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
        if not isinstance(other, ExportImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
