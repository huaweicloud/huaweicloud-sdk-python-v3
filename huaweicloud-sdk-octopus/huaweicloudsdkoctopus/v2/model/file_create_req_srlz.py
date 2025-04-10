# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileCreateReqSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sha256': 'str',
        'filename': 'str'
    }

    attribute_map = {
        'sha256': 'sha256',
        'filename': 'filename'
    }

    def __init__(self, sha256=None, filename=None):
        r"""FileCreateReqSrlz

        The model defined in huaweicloud sdk

        :param sha256: 文件sha256值
        :type sha256: str
        :param filename: 文件名
        :type filename: str
        """
        
        

        self._sha256 = None
        self._filename = None
        self.discriminator = None

        self.sha256 = sha256
        self.filename = filename

    @property
    def sha256(self):
        r"""Gets the sha256 of this FileCreateReqSrlz.

        文件sha256值

        :return: The sha256 of this FileCreateReqSrlz.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this FileCreateReqSrlz.

        文件sha256值

        :param sha256: The sha256 of this FileCreateReqSrlz.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def filename(self):
        r"""Gets the filename of this FileCreateReqSrlz.

        文件名

        :return: The filename of this FileCreateReqSrlz.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this FileCreateReqSrlz.

        文件名

        :param filename: The filename of this FileCreateReqSrlz.
        :type filename: str
        """
        self._filename = filename

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
        if not isinstance(other, FileCreateReqSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
