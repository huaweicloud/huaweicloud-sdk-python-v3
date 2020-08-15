# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListWatermarkTemplateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'templates': 'list[WatermarkTemplate]',
        'error': 'XCodeError'
    }

    attribute_map = {
        'total': 'total',
        'templates': 'templates',
        'error': 'error'
    }

    def __init__(self, total=None, templates=None, error=None):
        """ListWatermarkTemplateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._templates = None
        self._error = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if templates is not None:
            self.templates = templates
        if error is not None:
            self.error = error

    @property
    def total(self):
        """Gets the total of this ListWatermarkTemplateResponse.

        水印模板总数。

        :return: The total of this ListWatermarkTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListWatermarkTemplateResponse.

        水印模板总数。

        :param total: The total of this ListWatermarkTemplateResponse.
        :type: int
        """
        self._total = total

    @property
    def templates(self):
        """Gets the templates of this ListWatermarkTemplateResponse.

        水印模板

        :return: The templates of this ListWatermarkTemplateResponse.
        :rtype: list[WatermarkTemplate]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListWatermarkTemplateResponse.

        水印模板

        :param templates: The templates of this ListWatermarkTemplateResponse.
        :type: list[WatermarkTemplate]
        """
        self._templates = templates

    @property
    def error(self):
        """Gets the error of this ListWatermarkTemplateResponse.


        :return: The error of this ListWatermarkTemplateResponse.
        :rtype: XCodeError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ListWatermarkTemplateResponse.


        :param error: The error of this ListWatermarkTemplateResponse.
        :type: XCodeError
        """
        self._error = error

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
        if not isinstance(other, ListWatermarkTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
