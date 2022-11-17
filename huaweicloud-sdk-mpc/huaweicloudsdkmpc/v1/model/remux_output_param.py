# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemuxOutputParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'segment_duration': 'int',
        'remove_meta': 'bool'
    }

    attribute_map = {
        'format': 'format',
        'segment_duration': 'segment_duration',
        'remove_meta': 'remove_meta'
    }

    def __init__(self, format=None, segment_duration=None, remove_meta=None):
        """RemuxOutputParam

        The model defined in huaweicloud sdk

        :param format: 输出格式。取值范围： - HLS - MP4 
        :type format: str
        :param segment_duration: 分片时长，仅当“format”为“HLS”时有效。  取值范围：[2，10]。  默认值： 5。  单位：秒。 
        :type segment_duration: int
        :param remove_meta: 输出媒体是否去除片源的中metadata自定义信息。默认值：false 
        :type remove_meta: bool
        """
        
        

        self._format = None
        self._segment_duration = None
        self._remove_meta = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if segment_duration is not None:
            self.segment_duration = segment_duration
        if remove_meta is not None:
            self.remove_meta = remove_meta

    @property
    def format(self):
        """Gets the format of this RemuxOutputParam.

        输出格式。取值范围： - HLS - MP4 

        :return: The format of this RemuxOutputParam.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RemuxOutputParam.

        输出格式。取值范围： - HLS - MP4 

        :param format: The format of this RemuxOutputParam.
        :type format: str
        """
        self._format = format

    @property
    def segment_duration(self):
        """Gets the segment_duration of this RemuxOutputParam.

        分片时长，仅当“format”为“HLS”时有效。  取值范围：[2，10]。  默认值： 5。  单位：秒。 

        :return: The segment_duration of this RemuxOutputParam.
        :rtype: int
        """
        return self._segment_duration

    @segment_duration.setter
    def segment_duration(self, segment_duration):
        """Sets the segment_duration of this RemuxOutputParam.

        分片时长，仅当“format”为“HLS”时有效。  取值范围：[2，10]。  默认值： 5。  单位：秒。 

        :param segment_duration: The segment_duration of this RemuxOutputParam.
        :type segment_duration: int
        """
        self._segment_duration = segment_duration

    @property
    def remove_meta(self):
        """Gets the remove_meta of this RemuxOutputParam.

        输出媒体是否去除片源的中metadata自定义信息。默认值：false 

        :return: The remove_meta of this RemuxOutputParam.
        :rtype: bool
        """
        return self._remove_meta

    @remove_meta.setter
    def remove_meta(self, remove_meta):
        """Sets the remove_meta of this RemuxOutputParam.

        输出媒体是否去除片源的中metadata自定义信息。默认值：false 

        :param remove_meta: The remove_meta of this RemuxOutputParam.
        :type remove_meta: bool
        """
        self._remove_meta = remove_meta

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
        if not isinstance(other, RemuxOutputParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
