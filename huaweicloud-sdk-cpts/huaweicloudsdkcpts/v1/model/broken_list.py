# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BrokenList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'brand_brokens': 'BrandBrokens',
        'common_timestamps': 'list[str]',
        'performance_load': 'object',
        'respcode_brokens': 'RespcodeBrokens',
        'rtmp_brokens': 'RtmpBrokens',
        'streaming_error_brokens': 'StreamingErrorBrokens',
        'tps_brokens': 'TpsBrokens',
        'vusers_brokens': 'VusersBrokens'
    }

    attribute_map = {
        'brand_brokens': 'brand_brokens',
        'common_timestamps': 'commonTimestamps',
        'performance_load': 'performance_load',
        'respcode_brokens': 'respcode_brokens',
        'rtmp_brokens': 'rtmp_brokens',
        'streaming_error_brokens': 'streaming_error_brokens',
        'tps_brokens': 'tps_brokens',
        'vusers_brokens': 'vusers_brokens'
    }

    def __init__(self, brand_brokens=None, common_timestamps=None, performance_load=None, respcode_brokens=None, rtmp_brokens=None, streaming_error_brokens=None, tps_brokens=None, vusers_brokens=None):
        """BrokenList

        The model defined in huaweicloud sdk

        :param brand_brokens: 
        :type brand_brokens: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        :param common_timestamps: 时间戳
        :type common_timestamps: list[str]
        :param performance_load: 摸高数据
        :type performance_load: object
        :param respcode_brokens: 
        :type respcode_brokens: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        :param rtmp_brokens: 
        :type rtmp_brokens: :class:`huaweicloudsdkcpts.v1.RtmpBrokens`
        :param streaming_error_brokens: 
        :type streaming_error_brokens: :class:`huaweicloudsdkcpts.v1.StreamingErrorBrokens`
        :param tps_brokens: 
        :type tps_brokens: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        :param vusers_brokens: 
        :type vusers_brokens: :class:`huaweicloudsdkcpts.v1.VusersBrokens`
        """
        
        

        self._brand_brokens = None
        self._common_timestamps = None
        self._performance_load = None
        self._respcode_brokens = None
        self._rtmp_brokens = None
        self._streaming_error_brokens = None
        self._tps_brokens = None
        self._vusers_brokens = None
        self.discriminator = None

        if brand_brokens is not None:
            self.brand_brokens = brand_brokens
        if common_timestamps is not None:
            self.common_timestamps = common_timestamps
        if performance_load is not None:
            self.performance_load = performance_load
        if respcode_brokens is not None:
            self.respcode_brokens = respcode_brokens
        if rtmp_brokens is not None:
            self.rtmp_brokens = rtmp_brokens
        if streaming_error_brokens is not None:
            self.streaming_error_brokens = streaming_error_brokens
        if tps_brokens is not None:
            self.tps_brokens = tps_brokens
        if vusers_brokens is not None:
            self.vusers_brokens = vusers_brokens

    @property
    def brand_brokens(self):
        """Gets the brand_brokens of this BrokenList.

        :return: The brand_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        """
        return self._brand_brokens

    @brand_brokens.setter
    def brand_brokens(self, brand_brokens):
        """Sets the brand_brokens of this BrokenList.

        :param brand_brokens: The brand_brokens of this BrokenList.
        :type brand_brokens: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        """
        self._brand_brokens = brand_brokens

    @property
    def common_timestamps(self):
        """Gets the common_timestamps of this BrokenList.

        时间戳

        :return: The common_timestamps of this BrokenList.
        :rtype: list[str]
        """
        return self._common_timestamps

    @common_timestamps.setter
    def common_timestamps(self, common_timestamps):
        """Sets the common_timestamps of this BrokenList.

        时间戳

        :param common_timestamps: The common_timestamps of this BrokenList.
        :type common_timestamps: list[str]
        """
        self._common_timestamps = common_timestamps

    @property
    def performance_load(self):
        """Gets the performance_load of this BrokenList.

        摸高数据

        :return: The performance_load of this BrokenList.
        :rtype: object
        """
        return self._performance_load

    @performance_load.setter
    def performance_load(self, performance_load):
        """Sets the performance_load of this BrokenList.

        摸高数据

        :param performance_load: The performance_load of this BrokenList.
        :type performance_load: object
        """
        self._performance_load = performance_load

    @property
    def respcode_brokens(self):
        """Gets the respcode_brokens of this BrokenList.

        :return: The respcode_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        """
        return self._respcode_brokens

    @respcode_brokens.setter
    def respcode_brokens(self, respcode_brokens):
        """Sets the respcode_brokens of this BrokenList.

        :param respcode_brokens: The respcode_brokens of this BrokenList.
        :type respcode_brokens: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        """
        self._respcode_brokens = respcode_brokens

    @property
    def rtmp_brokens(self):
        """Gets the rtmp_brokens of this BrokenList.

        :return: The rtmp_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.RtmpBrokens`
        """
        return self._rtmp_brokens

    @rtmp_brokens.setter
    def rtmp_brokens(self, rtmp_brokens):
        """Sets the rtmp_brokens of this BrokenList.

        :param rtmp_brokens: The rtmp_brokens of this BrokenList.
        :type rtmp_brokens: :class:`huaweicloudsdkcpts.v1.RtmpBrokens`
        """
        self._rtmp_brokens = rtmp_brokens

    @property
    def streaming_error_brokens(self):
        """Gets the streaming_error_brokens of this BrokenList.

        :return: The streaming_error_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.StreamingErrorBrokens`
        """
        return self._streaming_error_brokens

    @streaming_error_brokens.setter
    def streaming_error_brokens(self, streaming_error_brokens):
        """Sets the streaming_error_brokens of this BrokenList.

        :param streaming_error_brokens: The streaming_error_brokens of this BrokenList.
        :type streaming_error_brokens: :class:`huaweicloudsdkcpts.v1.StreamingErrorBrokens`
        """
        self._streaming_error_brokens = streaming_error_brokens

    @property
    def tps_brokens(self):
        """Gets the tps_brokens of this BrokenList.

        :return: The tps_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        """
        return self._tps_brokens

    @tps_brokens.setter
    def tps_brokens(self, tps_brokens):
        """Sets the tps_brokens of this BrokenList.

        :param tps_brokens: The tps_brokens of this BrokenList.
        :type tps_brokens: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        """
        self._tps_brokens = tps_brokens

    @property
    def vusers_brokens(self):
        """Gets the vusers_brokens of this BrokenList.

        :return: The vusers_brokens of this BrokenList.
        :rtype: :class:`huaweicloudsdkcpts.v1.VusersBrokens`
        """
        return self._vusers_brokens

    @vusers_brokens.setter
    def vusers_brokens(self, vusers_brokens):
        """Sets the vusers_brokens of this BrokenList.

        :param vusers_brokens: The vusers_brokens of this BrokenList.
        :type vusers_brokens: :class:`huaweicloudsdkcpts.v1.VusersBrokens`
        """
        self._vusers_brokens = vusers_brokens

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
        if not isinstance(other, BrokenList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
