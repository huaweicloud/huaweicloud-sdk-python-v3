# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigFormatMutil:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'value': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'value': 'value'
    }

    def __init__(self, mode=None, value=None):
        r"""AccessConfigFormatMutil

        The model defined in huaweicloud sdk

        :param mode: 单行日志。time：日志时间，regular：正则模式。
        :type mode: str
        :param value: 日志时间。 当mode为\&quot;regular\&quot;，则输入正则表达式 当mode为\&quot;time\&quot;，则时间通配符：用日志打印时间来标识一条日志数据，通过时间通配符来匹配日志，每条日志的行首显示日志的打印时间；如果日志中的时间格式为：2019-01-01 23:59:59，时间通配符应该填写为：YYYY-MM-DD hh:mm:ss；如果日志中的时间格式为：19-1-1 23:59:59，时间通配符应该填写为：YY-M-D hh:mm:ss
        :type value: str
        """
        
        

        self._mode = None
        self._value = None
        self.discriminator = None

        self.mode = mode
        self.value = value

    @property
    def mode(self):
        r"""Gets the mode of this AccessConfigFormatMutil.

        单行日志。time：日志时间，regular：正则模式。

        :return: The mode of this AccessConfigFormatMutil.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AccessConfigFormatMutil.

        单行日志。time：日志时间，regular：正则模式。

        :param mode: The mode of this AccessConfigFormatMutil.
        :type mode: str
        """
        self._mode = mode

    @property
    def value(self):
        r"""Gets the value of this AccessConfigFormatMutil.

        日志时间。 当mode为\"regular\"，则输入正则表达式 当mode为\"time\"，则时间通配符：用日志打印时间来标识一条日志数据，通过时间通配符来匹配日志，每条日志的行首显示日志的打印时间；如果日志中的时间格式为：2019-01-01 23:59:59，时间通配符应该填写为：YYYY-MM-DD hh:mm:ss；如果日志中的时间格式为：19-1-1 23:59:59，时间通配符应该填写为：YY-M-D hh:mm:ss

        :return: The value of this AccessConfigFormatMutil.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AccessConfigFormatMutil.

        日志时间。 当mode为\"regular\"，则输入正则表达式 当mode为\"time\"，则时间通配符：用日志打印时间来标识一条日志数据，通过时间通配符来匹配日志，每条日志的行首显示日志的打印时间；如果日志中的时间格式为：2019-01-01 23:59:59，时间通配符应该填写为：YYYY-MM-DD hh:mm:ss；如果日志中的时间格式为：19-1-1 23:59:59，时间通配符应该填写为：YY-M-D hh:mm:ss

        :param value: The value of this AccessConfigFormatMutil.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, AccessConfigFormatMutil):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
