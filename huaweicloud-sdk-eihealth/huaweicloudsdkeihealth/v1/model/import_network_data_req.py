# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportNetworkDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_folder': 'str',
        'urls': 'list[str]',
        'md5s': 'list[str]'
    }

    attribute_map = {
        'target_folder': 'target_folder',
        'urls': 'urls',
        'md5s': 'md5s'
    }

    def __init__(self, target_folder=None, urls=None, md5s=None):
        """ImportNetworkDataReq

        The model defined in huaweicloud sdk

        :param target_folder: 所在文件夹
        :type target_folder: str
        :param urls: 导入网上数据的url集
        :type urls: list[str]
        :param md5s: 导入网上数据的md5集
        :type md5s: list[str]
        """
        
        

        self._target_folder = None
        self._urls = None
        self._md5s = None
        self.discriminator = None

        if target_folder is not None:
            self.target_folder = target_folder
        self.urls = urls
        if md5s is not None:
            self.md5s = md5s

    @property
    def target_folder(self):
        """Gets the target_folder of this ImportNetworkDataReq.

        所在文件夹

        :return: The target_folder of this ImportNetworkDataReq.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        """Sets the target_folder of this ImportNetworkDataReq.

        所在文件夹

        :param target_folder: The target_folder of this ImportNetworkDataReq.
        :type target_folder: str
        """
        self._target_folder = target_folder

    @property
    def urls(self):
        """Gets the urls of this ImportNetworkDataReq.

        导入网上数据的url集

        :return: The urls of this ImportNetworkDataReq.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ImportNetworkDataReq.

        导入网上数据的url集

        :param urls: The urls of this ImportNetworkDataReq.
        :type urls: list[str]
        """
        self._urls = urls

    @property
    def md5s(self):
        """Gets the md5s of this ImportNetworkDataReq.

        导入网上数据的md5集

        :return: The md5s of this ImportNetworkDataReq.
        :rtype: list[str]
        """
        return self._md5s

    @md5s.setter
    def md5s(self, md5s):
        """Sets the md5s of this ImportNetworkDataReq.

        导入网上数据的md5集

        :param md5s: The md5s of this ImportNetworkDataReq.
        :type md5s: list[str]
        """
        self._md5s = md5s

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
        if not isinstance(other, ImportNetworkDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
