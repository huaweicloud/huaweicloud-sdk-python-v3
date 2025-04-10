# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareVersionRespVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_version': 'object',
        'correlation_version': 'object'
    }

    attribute_map = {
        'basic_version': 'basicVersion',
        'correlation_version': 'correlationVersion'
    }

    def __init__(self, basic_version=None, correlation_version=None):
        r"""CompareVersionRespVo

        The model defined in huaweicloud sdk

        :param basic_version: **参数解释：**  基础版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type basic_version: object
        :param correlation_version: **参数解释：**  当前版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type correlation_version: object
        """
        
        

        self._basic_version = None
        self._correlation_version = None
        self.discriminator = None

        if basic_version is not None:
            self.basic_version = basic_version
        if correlation_version is not None:
            self.correlation_version = correlation_version

    @property
    def basic_version(self):
        r"""Gets the basic_version of this CompareVersionRespVo.

        **参数解释：**  基础版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The basic_version of this CompareVersionRespVo.
        :rtype: object
        """
        return self._basic_version

    @basic_version.setter
    def basic_version(self, basic_version):
        r"""Sets the basic_version of this CompareVersionRespVo.

        **参数解释：**  基础版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param basic_version: The basic_version of this CompareVersionRespVo.
        :type basic_version: object
        """
        self._basic_version = basic_version

    @property
    def correlation_version(self):
        r"""Gets the correlation_version of this CompareVersionRespVo.

        **参数解释：**  当前版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The correlation_version of this CompareVersionRespVo.
        :rtype: object
        """
        return self._correlation_version

    @correlation_version.setter
    def correlation_version(self, correlation_version):
        r"""Sets the correlation_version of this CompareVersionRespVo.

        **参数解释：**  当前版本对象。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param correlation_version: The correlation_version of this CompareVersionRespVo.
        :type correlation_version: object
        """
        self._correlation_version = correlation_version

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
        if not isinstance(other, CompareVersionRespVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
