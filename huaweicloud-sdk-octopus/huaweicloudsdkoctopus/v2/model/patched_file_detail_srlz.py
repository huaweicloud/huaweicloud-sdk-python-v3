# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchedFileDetailSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filename': 'str',
        'ready': 'bool'
    }

    attribute_map = {
        'filename': 'filename',
        'ready': 'ready'
    }

    def __init__(self, filename=None, ready=None):
        r"""PatchedFileDetailSrlz

        The model defined in huaweicloud sdk

        :param filename: 文件名
        :type filename: str
        :param ready: 文件状态
        :type ready: bool
        """
        
        

        self._filename = None
        self._ready = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if ready is not None:
            self.ready = ready

    @property
    def filename(self):
        r"""Gets the filename of this PatchedFileDetailSrlz.

        文件名

        :return: The filename of this PatchedFileDetailSrlz.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        r"""Sets the filename of this PatchedFileDetailSrlz.

        文件名

        :param filename: The filename of this PatchedFileDetailSrlz.
        :type filename: str
        """
        self._filename = filename

    @property
    def ready(self):
        r"""Gets the ready of this PatchedFileDetailSrlz.

        文件状态

        :return: The ready of this PatchedFileDetailSrlz.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        r"""Sets the ready of this PatchedFileDetailSrlz.

        文件状态

        :param ready: The ready of this PatchedFileDetailSrlz.
        :type ready: bool
        """
        self._ready = ready

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
        if not isinstance(other, PatchedFileDetailSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
