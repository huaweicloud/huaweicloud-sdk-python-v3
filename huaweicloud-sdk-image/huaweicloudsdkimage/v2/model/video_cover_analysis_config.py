# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoCoverAnalysisConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common': 'VideoCoverAnalysisConfigCommon'
    }

    attribute_map = {
        'common': 'common'
    }

    def __init__(self, common=None):
        """VideoCoverAnalysisConfig

        The model defined in huaweicloud sdk

        :param common: 
        :type common: :class:`huaweicloudsdkimage.v2.VideoCoverAnalysisConfigCommon`
        """
        
        

        self._common = None
        self.discriminator = None

        if common is not None:
            self.common = common

    @property
    def common(self):
        """Gets the common of this VideoCoverAnalysisConfig.

        :return: The common of this VideoCoverAnalysisConfig.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoCoverAnalysisConfigCommon`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this VideoCoverAnalysisConfig.

        :param common: The common of this VideoCoverAnalysisConfig.
        :type common: :class:`huaweicloudsdkimage.v2.VideoCoverAnalysisConfigCommon`
        """
        self._common = common

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
        if not isinstance(other, VideoCoverAnalysisConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
