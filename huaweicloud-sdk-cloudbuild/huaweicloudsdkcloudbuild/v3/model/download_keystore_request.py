# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadKeystoreRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'domain_id': 'domain_id'
    }

    def __init__(self, file_name=None, domain_id=None):
        """DownloadKeystoreRequest

        The model defined in huaweicloud sdk

        :param file_name: 下载的文件名称
        :type file_name: str
        :param domain_id: 租户ID。32位数字、小写字母组合
        :type domain_id: str
        """
        
        

        self._file_name = None
        self._domain_id = None
        self.discriminator = None

        self.file_name = file_name
        self.domain_id = domain_id

    @property
    def file_name(self):
        """Gets the file_name of this DownloadKeystoreRequest.

        下载的文件名称

        :return: The file_name of this DownloadKeystoreRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DownloadKeystoreRequest.

        下载的文件名称

        :param file_name: The file_name of this DownloadKeystoreRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def domain_id(self):
        """Gets the domain_id of this DownloadKeystoreRequest.

        租户ID。32位数字、小写字母组合

        :return: The domain_id of this DownloadKeystoreRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DownloadKeystoreRequest.

        租户ID。32位数字、小写字母组合

        :param domain_id: The domain_id of this DownloadKeystoreRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, DownloadKeystoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
