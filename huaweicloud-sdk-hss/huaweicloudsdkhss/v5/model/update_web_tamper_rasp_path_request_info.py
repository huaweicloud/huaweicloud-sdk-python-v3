# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWebTamperRaspPathRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rasp_path': 'str'
    }

    attribute_map = {
        'rasp_path': 'rasp_path'
    }

    def __init__(self, rasp_path=None):
        r"""UpdateWebTamperRaspPathRequestInfo

        The model defined in huaweicloud sdk

        :param rasp_path: rasp path
        :type rasp_path: str
        """
        
        

        self._rasp_path = None
        self.discriminator = None

        if rasp_path is not None:
            self.rasp_path = rasp_path

    @property
    def rasp_path(self):
        r"""Gets the rasp_path of this UpdateWebTamperRaspPathRequestInfo.

        rasp path

        :return: The rasp_path of this UpdateWebTamperRaspPathRequestInfo.
        :rtype: str
        """
        return self._rasp_path

    @rasp_path.setter
    def rasp_path(self, rasp_path):
        r"""Sets the rasp_path of this UpdateWebTamperRaspPathRequestInfo.

        rasp path

        :param rasp_path: The rasp_path of this UpdateWebTamperRaspPathRequestInfo.
        :type rasp_path: str
        """
        self._rasp_path = rasp_path

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
        if not isinstance(other, UpdateWebTamperRaspPathRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
