# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoIdDocClassificationAlarmResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detect_blur_result': 'bool',
        'detect_glare_result': 'bool',
        'detect_blocking_within_border_result': 'bool',
        'detect_insufficient_lighting_result': 'bool',
        'detect_copy_result': 'bool',
        'detect_border_integrity_result': 'bool',
        'detect_reproduce_result': 'bool'
    }

    attribute_map = {
        'detect_blur_result': 'detect_blur_result',
        'detect_glare_result': 'detect_glare_result',
        'detect_blocking_within_border_result': 'detect_blocking_within_border_result',
        'detect_insufficient_lighting_result': 'detect_insufficient_lighting_result',
        'detect_copy_result': 'detect_copy_result',
        'detect_border_integrity_result': 'detect_border_integrity_result',
        'detect_reproduce_result': 'detect_reproduce_result'
    }

    def __init__(self, detect_blur_result=None, detect_glare_result=None, detect_blocking_within_border_result=None, detect_insufficient_lighting_result=None, detect_copy_result=None, detect_border_integrity_result=None, detect_reproduce_result=None):
        r"""AutoIdDocClassificationAlarmResult

        The model defined in huaweicloud sdk

        :param detect_blur_result: 证件图像模糊告警结果。 - true：表示证件图片较模糊。 - false：表示证件清晰。  
        :type detect_blur_result: bool
        :param detect_glare_result: 证件图像反光告警结果。 - true：表示证件图片存在反光。 - false：表示证件图片不存在反光。 
        :type detect_glare_result: bool
        :param detect_blocking_within_border_result: 证件图像框内遮挡告警结果。 - true：表示证件图片存在框内遮挡。 - false：表示证件图片不存在框内遮挡。 
        :type detect_blocking_within_border_result: bool
        :param detect_insufficient_lighting_result: 证件图像过暗告警结果。 - true：表示证件图片过暗。 - false：表示证件图片光线正常。 
        :type detect_insufficient_lighting_result: bool
        :param detect_copy_result: 证件图像是否黑白复印件告警结果。 - true：表示证件是复印件。 - false：表示证件是原件。  
        :type detect_copy_result: bool
        :param detect_border_integrity_result: 证件图像边框完整性告警结果。 - true：表示边框不完整。 - false：表示边框完整。  
        :type detect_border_integrity_result: bool
        :param detect_reproduce_result: 证件图像是否翻拍告警结果。 - true：表示证件图片经过翻拍。 - false：表示证件图片未经过翻拍。  
        :type detect_reproduce_result: bool
        """
        
        

        self._detect_blur_result = None
        self._detect_glare_result = None
        self._detect_blocking_within_border_result = None
        self._detect_insufficient_lighting_result = None
        self._detect_copy_result = None
        self._detect_border_integrity_result = None
        self._detect_reproduce_result = None
        self.discriminator = None

        if detect_blur_result is not None:
            self.detect_blur_result = detect_blur_result
        if detect_glare_result is not None:
            self.detect_glare_result = detect_glare_result
        if detect_blocking_within_border_result is not None:
            self.detect_blocking_within_border_result = detect_blocking_within_border_result
        if detect_insufficient_lighting_result is not None:
            self.detect_insufficient_lighting_result = detect_insufficient_lighting_result
        if detect_copy_result is not None:
            self.detect_copy_result = detect_copy_result
        if detect_border_integrity_result is not None:
            self.detect_border_integrity_result = detect_border_integrity_result
        if detect_reproduce_result is not None:
            self.detect_reproduce_result = detect_reproduce_result

    @property
    def detect_blur_result(self):
        r"""Gets the detect_blur_result of this AutoIdDocClassificationAlarmResult.

        证件图像模糊告警结果。 - true：表示证件图片较模糊。 - false：表示证件清晰。  

        :return: The detect_blur_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_blur_result

    @detect_blur_result.setter
    def detect_blur_result(self, detect_blur_result):
        r"""Sets the detect_blur_result of this AutoIdDocClassificationAlarmResult.

        证件图像模糊告警结果。 - true：表示证件图片较模糊。 - false：表示证件清晰。  

        :param detect_blur_result: The detect_blur_result of this AutoIdDocClassificationAlarmResult.
        :type detect_blur_result: bool
        """
        self._detect_blur_result = detect_blur_result

    @property
    def detect_glare_result(self):
        r"""Gets the detect_glare_result of this AutoIdDocClassificationAlarmResult.

        证件图像反光告警结果。 - true：表示证件图片存在反光。 - false：表示证件图片不存在反光。 

        :return: The detect_glare_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_glare_result

    @detect_glare_result.setter
    def detect_glare_result(self, detect_glare_result):
        r"""Sets the detect_glare_result of this AutoIdDocClassificationAlarmResult.

        证件图像反光告警结果。 - true：表示证件图片存在反光。 - false：表示证件图片不存在反光。 

        :param detect_glare_result: The detect_glare_result of this AutoIdDocClassificationAlarmResult.
        :type detect_glare_result: bool
        """
        self._detect_glare_result = detect_glare_result

    @property
    def detect_blocking_within_border_result(self):
        r"""Gets the detect_blocking_within_border_result of this AutoIdDocClassificationAlarmResult.

        证件图像框内遮挡告警结果。 - true：表示证件图片存在框内遮挡。 - false：表示证件图片不存在框内遮挡。 

        :return: The detect_blocking_within_border_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_blocking_within_border_result

    @detect_blocking_within_border_result.setter
    def detect_blocking_within_border_result(self, detect_blocking_within_border_result):
        r"""Sets the detect_blocking_within_border_result of this AutoIdDocClassificationAlarmResult.

        证件图像框内遮挡告警结果。 - true：表示证件图片存在框内遮挡。 - false：表示证件图片不存在框内遮挡。 

        :param detect_blocking_within_border_result: The detect_blocking_within_border_result of this AutoIdDocClassificationAlarmResult.
        :type detect_blocking_within_border_result: bool
        """
        self._detect_blocking_within_border_result = detect_blocking_within_border_result

    @property
    def detect_insufficient_lighting_result(self):
        r"""Gets the detect_insufficient_lighting_result of this AutoIdDocClassificationAlarmResult.

        证件图像过暗告警结果。 - true：表示证件图片过暗。 - false：表示证件图片光线正常。 

        :return: The detect_insufficient_lighting_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_insufficient_lighting_result

    @detect_insufficient_lighting_result.setter
    def detect_insufficient_lighting_result(self, detect_insufficient_lighting_result):
        r"""Sets the detect_insufficient_lighting_result of this AutoIdDocClassificationAlarmResult.

        证件图像过暗告警结果。 - true：表示证件图片过暗。 - false：表示证件图片光线正常。 

        :param detect_insufficient_lighting_result: The detect_insufficient_lighting_result of this AutoIdDocClassificationAlarmResult.
        :type detect_insufficient_lighting_result: bool
        """
        self._detect_insufficient_lighting_result = detect_insufficient_lighting_result

    @property
    def detect_copy_result(self):
        r"""Gets the detect_copy_result of this AutoIdDocClassificationAlarmResult.

        证件图像是否黑白复印件告警结果。 - true：表示证件是复印件。 - false：表示证件是原件。  

        :return: The detect_copy_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_copy_result

    @detect_copy_result.setter
    def detect_copy_result(self, detect_copy_result):
        r"""Sets the detect_copy_result of this AutoIdDocClassificationAlarmResult.

        证件图像是否黑白复印件告警结果。 - true：表示证件是复印件。 - false：表示证件是原件。  

        :param detect_copy_result: The detect_copy_result of this AutoIdDocClassificationAlarmResult.
        :type detect_copy_result: bool
        """
        self._detect_copy_result = detect_copy_result

    @property
    def detect_border_integrity_result(self):
        r"""Gets the detect_border_integrity_result of this AutoIdDocClassificationAlarmResult.

        证件图像边框完整性告警结果。 - true：表示边框不完整。 - false：表示边框完整。  

        :return: The detect_border_integrity_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_border_integrity_result

    @detect_border_integrity_result.setter
    def detect_border_integrity_result(self, detect_border_integrity_result):
        r"""Sets the detect_border_integrity_result of this AutoIdDocClassificationAlarmResult.

        证件图像边框完整性告警结果。 - true：表示边框不完整。 - false：表示边框完整。  

        :param detect_border_integrity_result: The detect_border_integrity_result of this AutoIdDocClassificationAlarmResult.
        :type detect_border_integrity_result: bool
        """
        self._detect_border_integrity_result = detect_border_integrity_result

    @property
    def detect_reproduce_result(self):
        r"""Gets the detect_reproduce_result of this AutoIdDocClassificationAlarmResult.

        证件图像是否翻拍告警结果。 - true：表示证件图片经过翻拍。 - false：表示证件图片未经过翻拍。  

        :return: The detect_reproduce_result of this AutoIdDocClassificationAlarmResult.
        :rtype: bool
        """
        return self._detect_reproduce_result

    @detect_reproduce_result.setter
    def detect_reproduce_result(self, detect_reproduce_result):
        r"""Sets the detect_reproduce_result of this AutoIdDocClassificationAlarmResult.

        证件图像是否翻拍告警结果。 - true：表示证件图片经过翻拍。 - false：表示证件图片未经过翻拍。  

        :param detect_reproduce_result: The detect_reproduce_result of this AutoIdDocClassificationAlarmResult.
        :type detect_reproduce_result: bool
        """
        self._detect_reproduce_result = detect_reproduce_result

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
        if not isinstance(other, AutoIdDocClassificationAlarmResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
