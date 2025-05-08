# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hls_init_count': 'int',
        'hls_init_interval': 'int'
    }

    attribute_map = {
        'hls_init_count': 'hls_init_count',
        'hls_init_interval': 'hls_init_interval'
    }

    def __init__(self, hls_init_count=None, hls_init_interval=None):
        r"""VideoProcess

        The model defined in huaweicloud sdk

        :param hls_init_count: 需要单独设置时长的HLS起始分片数量。 取值范围：[0,10]，默认值为：0 与hls_init_interval配合使用，设置前面hls_init_count个HLS分片时长。为0表示不单独配置时长。 
        :type hls_init_count: int
        :param hls_init_interval: 表示前面hls_init_count个HLS分片的时长。 取值范围：[2,10] ，默认值为：5 hls_init_count不为0时，该字段才起作用。 
        :type hls_init_interval: int
        """
        
        

        self._hls_init_count = None
        self._hls_init_interval = None
        self.discriminator = None

        if hls_init_count is not None:
            self.hls_init_count = hls_init_count
        if hls_init_interval is not None:
            self.hls_init_interval = hls_init_interval

    @property
    def hls_init_count(self):
        r"""Gets the hls_init_count of this VideoProcess.

        需要单独设置时长的HLS起始分片数量。 取值范围：[0,10]，默认值为：0 与hls_init_interval配合使用，设置前面hls_init_count个HLS分片时长。为0表示不单独配置时长。 

        :return: The hls_init_count of this VideoProcess.
        :rtype: int
        """
        return self._hls_init_count

    @hls_init_count.setter
    def hls_init_count(self, hls_init_count):
        r"""Sets the hls_init_count of this VideoProcess.

        需要单独设置时长的HLS起始分片数量。 取值范围：[0,10]，默认值为：0 与hls_init_interval配合使用，设置前面hls_init_count个HLS分片时长。为0表示不单独配置时长。 

        :param hls_init_count: The hls_init_count of this VideoProcess.
        :type hls_init_count: int
        """
        self._hls_init_count = hls_init_count

    @property
    def hls_init_interval(self):
        r"""Gets the hls_init_interval of this VideoProcess.

        表示前面hls_init_count个HLS分片的时长。 取值范围：[2,10] ，默认值为：5 hls_init_count不为0时，该字段才起作用。 

        :return: The hls_init_interval of this VideoProcess.
        :rtype: int
        """
        return self._hls_init_interval

    @hls_init_interval.setter
    def hls_init_interval(self, hls_init_interval):
        r"""Sets the hls_init_interval of this VideoProcess.

        表示前面hls_init_count个HLS分片的时长。 取值范围：[2,10] ，默认值为：5 hls_init_count不为0时，该字段才起作用。 

        :param hls_init_interval: The hls_init_interval of this VideoProcess.
        :type hls_init_interval: int
        """
        self._hls_init_interval = hls_init_interval

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
        if not isinstance(other, VideoProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
