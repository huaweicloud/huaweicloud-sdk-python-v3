# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PornModerationResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'label': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label'
    }

    def __init__(self, confidence=None, label=None):
        """PornModerationResultDetail

        The model defined in huaweicloud sdk

        :param confidence: 置信度，取值范围 0-1。
        :type confidence: float
        :param label: 当前支持label列表如下： - normal：正常 - porn：色情 
        :type label: str
        """
        
        

        self._confidence = None
        self._label = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label

    @property
    def confidence(self):
        """Gets the confidence of this PornModerationResultDetail.

        置信度，取值范围 0-1。

        :return: The confidence of this PornModerationResultDetail.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this PornModerationResultDetail.

        置信度，取值范围 0-1。

        :param confidence: The confidence of this PornModerationResultDetail.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def label(self):
        """Gets the label of this PornModerationResultDetail.

        当前支持label列表如下： - normal：正常 - porn：色情 

        :return: The label of this PornModerationResultDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PornModerationResultDetail.

        当前支持label列表如下： - normal：正常 - porn：色情 

        :param label: The label of this PornModerationResultDetail.
        :type label: str
        """
        self._label = label

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
        if not isinstance(other, PornModerationResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
