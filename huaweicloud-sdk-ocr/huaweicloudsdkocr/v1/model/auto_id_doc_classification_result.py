# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoIdDocClassificationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'location': 'list[list[int]]',
        'confidence': 'float',
        'alarm_result': 'AutoIdDocClassificationAlarmResult',
        'alarm_confidence': 'AutoIdDocClassificationAlarmConfidence'
    }

    attribute_map = {
        'type': 'type',
        'location': 'location',
        'confidence': 'confidence',
        'alarm_result': 'alarm_result',
        'alarm_confidence': 'alarm_confidence'
    }

    def __init__(self, type=None, location=None, confidence=None, alarm_result=None, alarm_confidence=None):
        r"""AutoIdDocClassificationResult

        The model defined in huaweicloud sdk

        :param type: 证件的类型，支持的证件类型如表1所示：   **表1* 支持的证件类型 | 证件类型               | 类型描述                 | | ---------------------- | ------------------------ | | peru_id_card           | 秘鲁身份证               | | cambodian_id_card      | 柬文身份证               | | hongkong_id_card       | 香港身份证               | | macao_id_card          | 澳门身份证               | | myanmar_driver_license | 缅文驾驶证               | | myanmar_id_card        | 缅文身份证               | | passport               | 护照                     | | thailand_id_card       | 泰文身份证               | | id_card                | 中华人民共和国居民身份证 | 
        :type type: str
        :param location: 证件的位置。 
        :type location: list[list[int]]
        :param confidence: 证件位置的置信度。 
        :type confidence: float
        :param alarm_result: 
        :type alarm_result: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmResult`
        :param alarm_confidence: 
        :type alarm_confidence: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmConfidence`
        """
        
        

        self._type = None
        self._location = None
        self._confidence = None
        self._alarm_result = None
        self._alarm_confidence = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if location is not None:
            self.location = location
        if confidence is not None:
            self.confidence = confidence
        if alarm_result is not None:
            self.alarm_result = alarm_result
        if alarm_confidence is not None:
            self.alarm_confidence = alarm_confidence

    @property
    def type(self):
        r"""Gets the type of this AutoIdDocClassificationResult.

        证件的类型，支持的证件类型如表1所示：   **表1* 支持的证件类型 | 证件类型               | 类型描述                 | | ---------------------- | ------------------------ | | peru_id_card           | 秘鲁身份证               | | cambodian_id_card      | 柬文身份证               | | hongkong_id_card       | 香港身份证               | | macao_id_card          | 澳门身份证               | | myanmar_driver_license | 缅文驾驶证               | | myanmar_id_card        | 缅文身份证               | | passport               | 护照                     | | thailand_id_card       | 泰文身份证               | | id_card                | 中华人民共和国居民身份证 | 

        :return: The type of this AutoIdDocClassificationResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AutoIdDocClassificationResult.

        证件的类型，支持的证件类型如表1所示：   **表1* 支持的证件类型 | 证件类型               | 类型描述                 | | ---------------------- | ------------------------ | | peru_id_card           | 秘鲁身份证               | | cambodian_id_card      | 柬文身份证               | | hongkong_id_card       | 香港身份证               | | macao_id_card          | 澳门身份证               | | myanmar_driver_license | 缅文驾驶证               | | myanmar_id_card        | 缅文身份证               | | passport               | 护照                     | | thailand_id_card       | 泰文身份证               | | id_card                | 中华人民共和国居民身份证 | 

        :param type: The type of this AutoIdDocClassificationResult.
        :type type: str
        """
        self._type = type

    @property
    def location(self):
        r"""Gets the location of this AutoIdDocClassificationResult.

        证件的位置。 

        :return: The location of this AutoIdDocClassificationResult.
        :rtype: list[list[int]]
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this AutoIdDocClassificationResult.

        证件的位置。 

        :param location: The location of this AutoIdDocClassificationResult.
        :type location: list[list[int]]
        """
        self._location = location

    @property
    def confidence(self):
        r"""Gets the confidence of this AutoIdDocClassificationResult.

        证件位置的置信度。 

        :return: The confidence of this AutoIdDocClassificationResult.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this AutoIdDocClassificationResult.

        证件位置的置信度。 

        :param confidence: The confidence of this AutoIdDocClassificationResult.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def alarm_result(self):
        r"""Gets the alarm_result of this AutoIdDocClassificationResult.

        :return: The alarm_result of this AutoIdDocClassificationResult.
        :rtype: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmResult`
        """
        return self._alarm_result

    @alarm_result.setter
    def alarm_result(self, alarm_result):
        r"""Sets the alarm_result of this AutoIdDocClassificationResult.

        :param alarm_result: The alarm_result of this AutoIdDocClassificationResult.
        :type alarm_result: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmResult`
        """
        self._alarm_result = alarm_result

    @property
    def alarm_confidence(self):
        r"""Gets the alarm_confidence of this AutoIdDocClassificationResult.

        :return: The alarm_confidence of this AutoIdDocClassificationResult.
        :rtype: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmConfidence`
        """
        return self._alarm_confidence

    @alarm_confidence.setter
    def alarm_confidence(self, alarm_confidence):
        r"""Sets the alarm_confidence of this AutoIdDocClassificationResult.

        :param alarm_confidence: The alarm_confidence of this AutoIdDocClassificationResult.
        :type alarm_confidence: :class:`huaweicloudsdkocr.v1.AutoIdDocClassificationAlarmConfidence`
        """
        self._alarm_confidence = alarm_confidence

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
        if not isinstance(other, AutoIdDocClassificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
