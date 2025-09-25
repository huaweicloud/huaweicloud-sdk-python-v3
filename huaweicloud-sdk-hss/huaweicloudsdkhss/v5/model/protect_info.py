# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cover_area_info': 'ProtectInfoCoverAreaInfo',
        'config_info': 'ProtectInfoConfigInfo',
        'quota_info': 'ProtectInfoQuotaInfo'
    }

    attribute_map = {
        'cover_area_info': 'cover_area_info',
        'config_info': 'config_info',
        'quota_info': 'quota_info'
    }

    def __init__(self, cover_area_info=None, config_info=None, quota_info=None):
        r"""ProtectInfo

        The model defined in huaweicloud sdk

        :param cover_area_info: 
        :type cover_area_info: :class:`huaweicloudsdkhss.v5.ProtectInfoCoverAreaInfo`
        :param config_info: 
        :type config_info: :class:`huaweicloudsdkhss.v5.ProtectInfoConfigInfo`
        :param quota_info: 
        :type quota_info: :class:`huaweicloudsdkhss.v5.ProtectInfoQuotaInfo`
        """
        
        

        self._cover_area_info = None
        self._config_info = None
        self._quota_info = None
        self.discriminator = None

        if cover_area_info is not None:
            self.cover_area_info = cover_area_info
        if config_info is not None:
            self.config_info = config_info
        if quota_info is not None:
            self.quota_info = quota_info

    @property
    def cover_area_info(self):
        r"""Gets the cover_area_info of this ProtectInfo.

        :return: The cover_area_info of this ProtectInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectInfoCoverAreaInfo`
        """
        return self._cover_area_info

    @cover_area_info.setter
    def cover_area_info(self, cover_area_info):
        r"""Sets the cover_area_info of this ProtectInfo.

        :param cover_area_info: The cover_area_info of this ProtectInfo.
        :type cover_area_info: :class:`huaweicloudsdkhss.v5.ProtectInfoCoverAreaInfo`
        """
        self._cover_area_info = cover_area_info

    @property
    def config_info(self):
        r"""Gets the config_info of this ProtectInfo.

        :return: The config_info of this ProtectInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectInfoConfigInfo`
        """
        return self._config_info

    @config_info.setter
    def config_info(self, config_info):
        r"""Sets the config_info of this ProtectInfo.

        :param config_info: The config_info of this ProtectInfo.
        :type config_info: :class:`huaweicloudsdkhss.v5.ProtectInfoConfigInfo`
        """
        self._config_info = config_info

    @property
    def quota_info(self):
        r"""Gets the quota_info of this ProtectInfo.

        :return: The quota_info of this ProtectInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectInfoQuotaInfo`
        """
        return self._quota_info

    @quota_info.setter
    def quota_info(self, quota_info):
        r"""Sets the quota_info of this ProtectInfo.

        :param quota_info: The quota_info of this ProtectInfo.
        :type quota_info: :class:`huaweicloudsdkhss.v5.ProtectInfoQuotaInfo`
        """
        self._quota_info = quota_info

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
        if not isinstance(other, ProtectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
