# coding: utf-8

import pprint
import re

import six





class ImageDetectionResultDetailPorn:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'confidence': 'object',
        'label': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label'
    }

    def __init__(self, confidence=None, label=None):
        """ImageDetectionResultDetailPorn - a model defined in huaweicloud sdk"""
        
        

        self._confidence = None
        self._label = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label

    @property
    def confidence(self):
        """Gets the confidence of this ImageDetectionResultDetailPorn.


        :return: The confidence of this ImageDetectionResultDetailPorn.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageDetectionResultDetailPorn.


        :param confidence: The confidence of this ImageDetectionResultDetailPorn.
        :type: object
        """
        self._confidence = confidence

    @property
    def label(self):
        """Gets the label of this ImageDetectionResultDetailPorn.


        :return: The label of this ImageDetectionResultDetailPorn.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetectionResultDetailPorn.


        :param label: The label of this ImageDetectionResultDetailPorn.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageDetectionResultDetailPorn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
