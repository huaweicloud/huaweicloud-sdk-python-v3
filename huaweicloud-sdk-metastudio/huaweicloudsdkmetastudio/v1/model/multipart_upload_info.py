# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultipartUploadInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'part_number': 'str',
        'etag': 'str'
    }

    attribute_map = {
        'part_number': 'part_number',
        'etag': 'etag'
    }

    def __init__(self, part_number=None, etag=None):
        r"""MultipartUploadInfo

        The model defined in huaweicloud sdk

        :param part_number: 分片编号
        :type part_number: str
        :param etag: 分片文件标识
        :type etag: str
        """
        
        

        self._part_number = None
        self._etag = None
        self.discriminator = None

        if part_number is not None:
            self.part_number = part_number
        if etag is not None:
            self.etag = etag

    @property
    def part_number(self):
        r"""Gets the part_number of this MultipartUploadInfo.

        分片编号

        :return: The part_number of this MultipartUploadInfo.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        r"""Sets the part_number of this MultipartUploadInfo.

        分片编号

        :param part_number: The part_number of this MultipartUploadInfo.
        :type part_number: str
        """
        self._part_number = part_number

    @property
    def etag(self):
        r"""Gets the etag of this MultipartUploadInfo.

        分片文件标识

        :return: The etag of this MultipartUploadInfo.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        r"""Sets the etag of this MultipartUploadInfo.

        分片文件标识

        :param etag: The etag of this MultipartUploadInfo.
        :type etag: str
        """
        self._etag = etag

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
        if not isinstance(other, MultipartUploadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
