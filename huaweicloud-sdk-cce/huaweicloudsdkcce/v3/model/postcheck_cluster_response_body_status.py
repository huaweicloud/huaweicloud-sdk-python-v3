# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostcheckClusterResponseBodyStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str'
    }

    attribute_map = {
        'phase': 'phase'
    }

    def __init__(self, phase=None):
        r"""PostcheckClusterResponseBodyStatus

        The model defined in huaweicloud sdk

        :param phase: 状态，取值如下 - Success 成功 - Failed 失败 - Error 错误
        :type phase: str
        """
        
        

        self._phase = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase

    @property
    def phase(self):
        r"""Gets the phase of this PostcheckClusterResponseBodyStatus.

        状态，取值如下 - Success 成功 - Failed 失败 - Error 错误

        :return: The phase of this PostcheckClusterResponseBodyStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this PostcheckClusterResponseBodyStatus.

        状态，取值如下 - Success 成功 - Failed 失败 - Error 错误

        :param phase: The phase of this PostcheckClusterResponseBodyStatus.
        :type phase: str
        """
        self._phase = phase

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
        if not isinstance(other, PostcheckClusterResponseBodyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
