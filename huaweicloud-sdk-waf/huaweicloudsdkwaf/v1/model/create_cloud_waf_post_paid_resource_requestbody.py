# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudWafPostPaidResourceRequestbody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'console_area': 'str'
    }

    attribute_map = {
        'console_area': 'console_area'
    }

    def __init__(self, console_area=None):
        """CreateCloudWafPostPaidResourceRequestbody

        The model defined in huaweicloud sdk

        :param console_area: 租户所在的站点，hec-hk：华为云国际站
        :type console_area: str
        """
        
        

        self._console_area = None
        self.discriminator = None

        self.console_area = console_area

    @property
    def console_area(self):
        """Gets the console_area of this CreateCloudWafPostPaidResourceRequestbody.

        租户所在的站点，hec-hk：华为云国际站

        :return: The console_area of this CreateCloudWafPostPaidResourceRequestbody.
        :rtype: str
        """
        return self._console_area

    @console_area.setter
    def console_area(self, console_area):
        """Sets the console_area of this CreateCloudWafPostPaidResourceRequestbody.

        租户所在的站点，hec-hk：华为云国际站

        :param console_area: The console_area of this CreateCloudWafPostPaidResourceRequestbody.
        :type console_area: str
        """
        self._console_area = console_area

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
        if not isinstance(other, CreateCloudWafPostPaidResourceRequestbody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
