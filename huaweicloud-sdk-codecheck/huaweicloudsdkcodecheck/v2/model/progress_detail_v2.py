# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProgressDetailV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ratio': 'str',
        'info': 'str'
    }

    attribute_map = {
        'ratio': 'ratio',
        'info': 'info'
    }

    def __init__(self, ratio=None, info=None):
        """ProgressDetailV2

        The model defined in huaweicloud sdk

        :param ratio: 进度百分比
        :type ratio: str
        :param info: 中文信息
        :type info: str
        """
        
        

        self._ratio = None
        self._info = None
        self.discriminator = None

        if ratio is not None:
            self.ratio = ratio
        if info is not None:
            self.info = info

    @property
    def ratio(self):
        """Gets the ratio of this ProgressDetailV2.

        进度百分比

        :return: The ratio of this ProgressDetailV2.
        :rtype: str
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this ProgressDetailV2.

        进度百分比

        :param ratio: The ratio of this ProgressDetailV2.
        :type ratio: str
        """
        self._ratio = ratio

    @property
    def info(self):
        """Gets the info of this ProgressDetailV2.

        中文信息

        :return: The info of this ProgressDetailV2.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ProgressDetailV2.

        中文信息

        :param info: The info of this ProgressDetailV2.
        :type info: str
        """
        self._info = info

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
        if not isinstance(other, ProgressDetailV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
