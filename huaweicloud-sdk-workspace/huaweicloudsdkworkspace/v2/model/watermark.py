# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Watermark:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'watermark_enable': 'bool',
        'options': 'WatermarkOptions'
    }

    attribute_map = {
        'watermark_enable': 'watermark_enable',
        'options': 'options'
    }

    def __init__(self, watermark_enable=None, options=None):
        r"""Watermark

        The model defined in huaweicloud sdk

        :param watermark_enable: 是否开启水印策略设置。取值为：false：表示关闭。true：表示开启。
        :type watermark_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.WatermarkOptions`
        """
        
        

        self._watermark_enable = None
        self._options = None
        self.discriminator = None

        if watermark_enable is not None:
            self.watermark_enable = watermark_enable
        if options is not None:
            self.options = options

    @property
    def watermark_enable(self):
        r"""Gets the watermark_enable of this Watermark.

        是否开启水印策略设置。取值为：false：表示关闭。true：表示开启。

        :return: The watermark_enable of this Watermark.
        :rtype: bool
        """
        return self._watermark_enable

    @watermark_enable.setter
    def watermark_enable(self, watermark_enable):
        r"""Sets the watermark_enable of this Watermark.

        是否开启水印策略设置。取值为：false：表示关闭。true：表示开启。

        :param watermark_enable: The watermark_enable of this Watermark.
        :type watermark_enable: bool
        """
        self._watermark_enable = watermark_enable

    @property
    def options(self):
        r"""Gets the options of this Watermark.

        :return: The options of this Watermark.
        :rtype: :class:`huaweicloudsdkworkspace.v2.WatermarkOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this Watermark.

        :param options: The options of this Watermark.
        :type options: :class:`huaweicloudsdkworkspace.v2.WatermarkOptions`
        """
        self._options = options

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
        if not isinstance(other, Watermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
