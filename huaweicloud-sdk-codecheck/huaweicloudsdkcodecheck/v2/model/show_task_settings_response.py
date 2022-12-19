# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'info': 'list[TaskAdvancedSettings]',
        'total': 'int'
    }

    attribute_map = {
        'info': 'info',
        'total': 'total'
    }

    def __init__(self, info=None, total=None):
        """ShowTaskSettingsResponse

        The model defined in huaweicloud sdk

        :param info: 高级选项的相关信息
        :type info: list[:class:`huaweicloudsdkcodecheck.v2.TaskAdvancedSettings`]
        :param total: 总数
        :type total: int
        """
        
        super(ShowTaskSettingsResponse, self).__init__()

        self._info = None
        self._total = None
        self.discriminator = None

        if info is not None:
            self.info = info
        if total is not None:
            self.total = total

    @property
    def info(self):
        """Gets the info of this ShowTaskSettingsResponse.

        高级选项的相关信息

        :return: The info of this ShowTaskSettingsResponse.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.TaskAdvancedSettings`]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ShowTaskSettingsResponse.

        高级选项的相关信息

        :param info: The info of this ShowTaskSettingsResponse.
        :type info: list[:class:`huaweicloudsdkcodecheck.v2.TaskAdvancedSettings`]
        """
        self._info = info

    @property
    def total(self):
        """Gets the total of this ShowTaskSettingsResponse.

        总数

        :return: The total of this ShowTaskSettingsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowTaskSettingsResponse.

        总数

        :param total: The total of this ShowTaskSettingsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ShowTaskSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
