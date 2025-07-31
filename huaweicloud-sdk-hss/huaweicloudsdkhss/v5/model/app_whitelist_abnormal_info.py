# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistAbnormalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_type': 'int',
        'abnormal_description': 'str'
    }

    attribute_map = {
        'abnormal_type': 'abnormal_type',
        'abnormal_description': 'abnormal_description'
    }

    def __init__(self, abnormal_type=None, abnormal_description=None):
        r"""AppWhitelistAbnormalInfo

        The model defined in huaweicloud sdk

        :param abnormal_type: 异常类型
        :type abnormal_type: int
        :param abnormal_description: 异常描述
        :type abnormal_description: str
        """
        
        

        self._abnormal_type = None
        self._abnormal_description = None
        self.discriminator = None

        if abnormal_type is not None:
            self.abnormal_type = abnormal_type
        if abnormal_description is not None:
            self.abnormal_description = abnormal_description

    @property
    def abnormal_type(self):
        r"""Gets the abnormal_type of this AppWhitelistAbnormalInfo.

        异常类型

        :return: The abnormal_type of this AppWhitelistAbnormalInfo.
        :rtype: int
        """
        return self._abnormal_type

    @abnormal_type.setter
    def abnormal_type(self, abnormal_type):
        r"""Sets the abnormal_type of this AppWhitelistAbnormalInfo.

        异常类型

        :param abnormal_type: The abnormal_type of this AppWhitelistAbnormalInfo.
        :type abnormal_type: int
        """
        self._abnormal_type = abnormal_type

    @property
    def abnormal_description(self):
        r"""Gets the abnormal_description of this AppWhitelistAbnormalInfo.

        异常描述

        :return: The abnormal_description of this AppWhitelistAbnormalInfo.
        :rtype: str
        """
        return self._abnormal_description

    @abnormal_description.setter
    def abnormal_description(self, abnormal_description):
        r"""Sets the abnormal_description of this AppWhitelistAbnormalInfo.

        异常描述

        :param abnormal_description: The abnormal_description of this AppWhitelistAbnormalInfo.
        :type abnormal_description: str
        """
        self._abnormal_description = abnormal_description

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
        if not isinstance(other, AppWhitelistAbnormalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
