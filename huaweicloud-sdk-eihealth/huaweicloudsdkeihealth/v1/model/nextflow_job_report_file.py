# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowJobReportFile:

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
        'download_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'download_url': 'download_url'
    }

    def __init__(self, name=None, download_url=None):
        """NextflowJobReportFile

        The model defined in huaweicloud sdk

        :param name: 报告文件名
        :type name: str
        :param download_url: 报告文件下载地址
        :type download_url: str
        """
        
        

        self._name = None
        self._download_url = None
        self.discriminator = None

        self.name = name
        self.download_url = download_url

    @property
    def name(self):
        """Gets the name of this NextflowJobReportFile.

        报告文件名

        :return: The name of this NextflowJobReportFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NextflowJobReportFile.

        报告文件名

        :param name: The name of this NextflowJobReportFile.
        :type name: str
        """
        self._name = name

    @property
    def download_url(self):
        """Gets the download_url of this NextflowJobReportFile.

        报告文件下载地址

        :return: The download_url of this NextflowJobReportFile.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this NextflowJobReportFile.

        报告文件下载地址

        :param download_url: The download_url of this NextflowJobReportFile.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, NextflowJobReportFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
