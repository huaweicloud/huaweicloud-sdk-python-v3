# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunFastaPreprocessReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'FastaReceptor',
        'preview_count': 'int',
        'count_limit': 'int'
    }

    attribute_map = {
        'file': 'file',
        'preview_count': 'preview_count',
        'count_limit': 'count_limit'
    }

    def __init__(self, file=None, preview_count=None, count_limit=None):
        r"""RunFastaPreprocessReq

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.FastaReceptor`
        :param preview_count: 预览数量
        :type preview_count: int
        :param count_limit: 计数上限
        :type count_limit: int
        """
        
        

        self._file = None
        self._preview_count = None
        self._count_limit = None
        self.discriminator = None

        self.file = file
        if preview_count is not None:
            self.preview_count = preview_count
        if count_limit is not None:
            self.count_limit = count_limit

    @property
    def file(self):
        r"""Gets the file of this RunFastaPreprocessReq.

        :return: The file of this RunFastaPreprocessReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FastaReceptor`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this RunFastaPreprocessReq.

        :param file: The file of this RunFastaPreprocessReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.FastaReceptor`
        """
        self._file = file

    @property
    def preview_count(self):
        r"""Gets the preview_count of this RunFastaPreprocessReq.

        预览数量

        :return: The preview_count of this RunFastaPreprocessReq.
        :rtype: int
        """
        return self._preview_count

    @preview_count.setter
    def preview_count(self, preview_count):
        r"""Sets the preview_count of this RunFastaPreprocessReq.

        预览数量

        :param preview_count: The preview_count of this RunFastaPreprocessReq.
        :type preview_count: int
        """
        self._preview_count = preview_count

    @property
    def count_limit(self):
        r"""Gets the count_limit of this RunFastaPreprocessReq.

        计数上限

        :return: The count_limit of this RunFastaPreprocessReq.
        :rtype: int
        """
        return self._count_limit

    @count_limit.setter
    def count_limit(self, count_limit):
        r"""Sets the count_limit of this RunFastaPreprocessReq.

        计数上限

        :param count_limit: The count_limit of this RunFastaPreprocessReq.
        :type count_limit: int
        """
        self._count_limit = count_limit

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
        if not isinstance(other, RunFastaPreprocessReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
