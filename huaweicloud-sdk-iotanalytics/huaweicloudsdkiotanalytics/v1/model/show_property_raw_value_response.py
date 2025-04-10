# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPropertyRawValueResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamps': 'list[str]',
        'properties': 'list[RawValue]'
    }

    attribute_map = {
        'timestamps': 'timestamps',
        'properties': 'properties'
    }

    def __init__(self, timestamps=None, properties=None):
        r"""ShowPropertyRawValueResponse

        The model defined in huaweicloud sdk

        :param timestamps: 时间序列,使用UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;,示例：2021-02-01T00:00:00.123Z
        :type timestamps: list[str]
        :param properties: 响应属性列表
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.RawValue`]
        """
        
        super(ShowPropertyRawValueResponse, self).__init__()

        self._timestamps = None
        self._properties = None
        self.discriminator = None

        if timestamps is not None:
            self.timestamps = timestamps
        if properties is not None:
            self.properties = properties

    @property
    def timestamps(self):
        r"""Gets the timestamps of this ShowPropertyRawValueResponse.

        时间序列,使用UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z',示例：2021-02-01T00:00:00.123Z

        :return: The timestamps of this ShowPropertyRawValueResponse.
        :rtype: list[str]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        r"""Sets the timestamps of this ShowPropertyRawValueResponse.

        时间序列,使用UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z',示例：2021-02-01T00:00:00.123Z

        :param timestamps: The timestamps of this ShowPropertyRawValueResponse.
        :type timestamps: list[str]
        """
        self._timestamps = timestamps

    @property
    def properties(self):
        r"""Gets the properties of this ShowPropertyRawValueResponse.

        响应属性列表

        :return: The properties of this ShowPropertyRawValueResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.RawValue`]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ShowPropertyRawValueResponse.

        响应属性列表

        :param properties: The properties of this ShowPropertyRawValueResponse.
        :type properties: list[:class:`huaweicloudsdkiotanalytics.v1.RawValue`]
        """
        self._properties = properties

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
        if not isinstance(other, ShowPropertyRawValueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
