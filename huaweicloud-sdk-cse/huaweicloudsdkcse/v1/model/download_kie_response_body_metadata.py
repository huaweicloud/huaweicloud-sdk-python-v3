# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadKieResponseBodyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'annotations': 'object'
    }

    attribute_map = {
        'version': 'version',
        'annotations': 'annotations'
    }

    def __init__(self, version=None, annotations=None):
        """DownloadKieResponseBodyMetadata

        The model defined in huaweicloud sdk

        :param version: 版本号
        :type version: str
        :param annotations: 导出文件的其他信息
        :type annotations: object
        """
        
        

        self._version = None
        self._annotations = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if annotations is not None:
            self.annotations = annotations

    @property
    def version(self):
        """Gets the version of this DownloadKieResponseBodyMetadata.

        版本号

        :return: The version of this DownloadKieResponseBodyMetadata.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DownloadKieResponseBodyMetadata.

        版本号

        :param version: The version of this DownloadKieResponseBodyMetadata.
        :type version: str
        """
        self._version = version

    @property
    def annotations(self):
        """Gets the annotations of this DownloadKieResponseBodyMetadata.

        导出文件的其他信息

        :return: The annotations of this DownloadKieResponseBodyMetadata.
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this DownloadKieResponseBodyMetadata.

        导出文件的其他信息

        :param annotations: The annotations of this DownloadKieResponseBodyMetadata.
        :type annotations: object
        """
        self._annotations = annotations

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
        if not isinstance(other, DownloadKieResponseBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
