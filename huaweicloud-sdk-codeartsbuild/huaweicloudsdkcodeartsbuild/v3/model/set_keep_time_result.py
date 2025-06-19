# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetKeepTimeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_time': 'int'
    }

    attribute_map = {
        'keep_time': 'keep_time'
    }

    def __init__(self, keep_time=None):
        r"""SetKeepTimeResult

        The model defined in huaweicloud sdk

        :param keep_time: 回收站中的任务保留时间
        :type keep_time: int
        """
        
        

        self._keep_time = None
        self.discriminator = None

        if keep_time is not None:
            self.keep_time = keep_time

    @property
    def keep_time(self):
        r"""Gets the keep_time of this SetKeepTimeResult.

        回收站中的任务保留时间

        :return: The keep_time of this SetKeepTimeResult.
        :rtype: int
        """
        return self._keep_time

    @keep_time.setter
    def keep_time(self, keep_time):
        r"""Sets the keep_time of this SetKeepTimeResult.

        回收站中的任务保留时间

        :param keep_time: The keep_time of this SetKeepTimeResult.
        :type keep_time: int
        """
        self._keep_time = keep_time

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
        if not isinstance(other, SetKeepTimeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
