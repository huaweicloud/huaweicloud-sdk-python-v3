# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityRiskResponseImageRiskRiskList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'str',
        'image_num': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'image_num': 'image_num'
    }

    def __init__(self, severity=None, image_num=None):
        r"""SecurityRiskResponseImageRiskRiskList

        The model defined in huaweicloud sdk

        :param severity: **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 
        :type severity: str
        :param image_num: **参数解释**： 镜像数量 **取值范围**: 最小值0，最大值2147483647 
        :type image_num: int
        """
        
        

        self._severity = None
        self._image_num = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if image_num is not None:
            self.image_num = image_num

    @property
    def severity(self):
        r"""Gets the severity of this SecurityRiskResponseImageRiskRiskList.

        **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 

        :return: The severity of this SecurityRiskResponseImageRiskRiskList.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityRiskResponseImageRiskRiskList.

        **参数解释**： 风险级别 **取值范围**: 字符长度0-32位 

        :param severity: The severity of this SecurityRiskResponseImageRiskRiskList.
        :type severity: str
        """
        self._severity = severity

    @property
    def image_num(self):
        r"""Gets the image_num of this SecurityRiskResponseImageRiskRiskList.

        **参数解释**： 镜像数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The image_num of this SecurityRiskResponseImageRiskRiskList.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this SecurityRiskResponseImageRiskRiskList.

        **参数解释**： 镜像数量 **取值范围**: 最小值0，最大值2147483647 

        :param image_num: The image_num of this SecurityRiskResponseImageRiskRiskList.
        :type image_num: int
        """
        self._image_num = image_num

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
        if not isinstance(other, SecurityRiskResponseImageRiskRiskList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
