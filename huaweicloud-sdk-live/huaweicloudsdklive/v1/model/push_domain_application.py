# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushDomainApplication:

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
        'hls_fragment': 'int',
        'hls_ts_count': 'int',
        'hls_min_frags': 'int'
    }

    attribute_map = {
        'name': 'name',
        'hls_fragment': 'hls_fragment',
        'hls_ts_count': 'hls_ts_count',
        'hls_min_frags': 'hls_min_frags'
    }

    def __init__(self, name=None, hls_fragment=None, hls_ts_count=None, hls_min_frags=None):
        r"""PushDomainApplication

        The model defined in huaweicloud sdk

        :param name: 应用名，默认为live
        :type name: str
        :param hls_fragment: HLS切片时长，单位：s。
        :type hls_fragment: int
        :param hls_ts_count: 每个M3U8文件内ts切片个数
        :type hls_ts_count: int
        :param hls_min_frags: 每个M3U8文件内最小ts分片数
        :type hls_min_frags: int
        """
        
        

        self._name = None
        self._hls_fragment = None
        self._hls_ts_count = None
        self._hls_min_frags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if hls_fragment is not None:
            self.hls_fragment = hls_fragment
        if hls_ts_count is not None:
            self.hls_ts_count = hls_ts_count
        if hls_min_frags is not None:
            self.hls_min_frags = hls_min_frags

    @property
    def name(self):
        r"""Gets the name of this PushDomainApplication.

        应用名，默认为live

        :return: The name of this PushDomainApplication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PushDomainApplication.

        应用名，默认为live

        :param name: The name of this PushDomainApplication.
        :type name: str
        """
        self._name = name

    @property
    def hls_fragment(self):
        r"""Gets the hls_fragment of this PushDomainApplication.

        HLS切片时长，单位：s。

        :return: The hls_fragment of this PushDomainApplication.
        :rtype: int
        """
        return self._hls_fragment

    @hls_fragment.setter
    def hls_fragment(self, hls_fragment):
        r"""Sets the hls_fragment of this PushDomainApplication.

        HLS切片时长，单位：s。

        :param hls_fragment: The hls_fragment of this PushDomainApplication.
        :type hls_fragment: int
        """
        self._hls_fragment = hls_fragment

    @property
    def hls_ts_count(self):
        r"""Gets the hls_ts_count of this PushDomainApplication.

        每个M3U8文件内ts切片个数

        :return: The hls_ts_count of this PushDomainApplication.
        :rtype: int
        """
        return self._hls_ts_count

    @hls_ts_count.setter
    def hls_ts_count(self, hls_ts_count):
        r"""Sets the hls_ts_count of this PushDomainApplication.

        每个M3U8文件内ts切片个数

        :param hls_ts_count: The hls_ts_count of this PushDomainApplication.
        :type hls_ts_count: int
        """
        self._hls_ts_count = hls_ts_count

    @property
    def hls_min_frags(self):
        r"""Gets the hls_min_frags of this PushDomainApplication.

        每个M3U8文件内最小ts分片数

        :return: The hls_min_frags of this PushDomainApplication.
        :rtype: int
        """
        return self._hls_min_frags

    @hls_min_frags.setter
    def hls_min_frags(self, hls_min_frags):
        r"""Sets the hls_min_frags of this PushDomainApplication.

        每个M3U8文件内最小ts分片数

        :param hls_min_frags: The hls_min_frags of this PushDomainApplication.
        :type hls_min_frags: int
        """
        self._hls_min_frags = hls_min_frags

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
        if not isinstance(other, PushDomainApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
