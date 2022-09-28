# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportbrokensInfo:

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
        'common_timestamps': 'list[int]',
        'respcode_brokens': 'RespcodeBrokens',
        'tps_brokens': 'TpsBrokens',
        'vusers_brokens': 'VusersBrokens'
    }

    attribute_map = {
        'brand_brokens': 'brand_brokens',
        'common_timestamps': 'commonTimestamps',
        'respcode_brokens': 'respcode_brokens',
        'tps_brokens': 'tps_brokens',
        'vusers_brokens': 'vusers_brokens'
    }

    def __init__(self, brand_brokens=None, common_timestamps=None, respcode_brokens=None, tps_brokens=None, vusers_brokens=None):
        """ReportbrokensInfo

        The model defined in huaweicloud sdk

        :param brand_brokens: 
        :type brand_brokens: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        :param common_timestamps: 时间戳
        :type common_timestamps: list[int]
        :param respcode_brokens: 
        :type respcode_brokens: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        :param tps_brokens: 
        :type tps_brokens: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        :param vusers_brokens: 
        :type vusers_brokens: :class:`huaweicloudsdkcpts.v1.VusersBrokens`
        """
        
        

        self._brand_brokens = None
        self._common_timestamps = None
        self._respcode_brokens = None
        self._tps_brokens = None
        self._vusers_brokens = None
        self.discriminator = None

        if brand_brokens is not None:
            self.brand_brokens = brand_brokens
        if common_timestamps is not None:
            self.common_timestamps = common_timestamps
        if respcode_brokens is not None:
            self.respcode_brokens = respcode_brokens
        if tps_brokens is not None:
            self.tps_brokens = tps_brokens
        if vusers_brokens is not None:
            self.vusers_brokens = vusers_brokens

    @property
    def brand_brokens(self):
        """Gets the brand_brokens of this ReportbrokensInfo.


        :return: The brand_brokens of this ReportbrokensInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        """
        return self._brand_brokens

    @brand_brokens.setter
    def brand_brokens(self, brand_brokens):
        """Sets the brand_brokens of this ReportbrokensInfo.


        :param brand_brokens: The brand_brokens of this ReportbrokensInfo.
        :type brand_brokens: :class:`huaweicloudsdkcpts.v1.BrandBrokens`
        """
        self._brand_brokens = brand_brokens

    @property
    def common_timestamps(self):
        """Gets the common_timestamps of this ReportbrokensInfo.

        时间戳

        :return: The common_timestamps of this ReportbrokensInfo.
        :rtype: list[int]
        """
        return self._common_timestamps

    @common_timestamps.setter
    def common_timestamps(self, common_timestamps):
        """Sets the common_timestamps of this ReportbrokensInfo.

        时间戳

        :param common_timestamps: The common_timestamps of this ReportbrokensInfo.
        :type common_timestamps: list[int]
        """
        self._common_timestamps = common_timestamps

    @property
    def respcode_brokens(self):
        """Gets the respcode_brokens of this ReportbrokensInfo.


        :return: The respcode_brokens of this ReportbrokensInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        """
        return self._respcode_brokens

    @respcode_brokens.setter
    def respcode_brokens(self, respcode_brokens):
        """Sets the respcode_brokens of this ReportbrokensInfo.


        :param respcode_brokens: The respcode_brokens of this ReportbrokensInfo.
        :type respcode_brokens: :class:`huaweicloudsdkcpts.v1.RespcodeBrokens`
        """
        self._respcode_brokens = respcode_brokens

    @property
    def tps_brokens(self):
        """Gets the tps_brokens of this ReportbrokensInfo.


        :return: The tps_brokens of this ReportbrokensInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        """
        return self._tps_brokens

    @tps_brokens.setter
    def tps_brokens(self, tps_brokens):
        """Sets the tps_brokens of this ReportbrokensInfo.


        :param tps_brokens: The tps_brokens of this ReportbrokensInfo.
        :type tps_brokens: :class:`huaweicloudsdkcpts.v1.TpsBrokens`
        """
        self._tps_brokens = tps_brokens

    @property
    def vusers_brokens(self):
        """Gets the vusers_brokens of this ReportbrokensInfo.


        :return: The vusers_brokens of this ReportbrokensInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.VusersBrokens`
        """
        return self._vusers_brokens

    @vusers_brokens.setter
    def vusers_brokens(self, vusers_brokens):
        """Sets the vusers_brokens of this ReportbrokensInfo.


        :param vusers_brokens: The vusers_brokens of this ReportbrokensInfo.
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
        if not isinstance(other, ReportbrokensInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
