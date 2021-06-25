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
        'templates': 'list[WatermarkTemplate]',
        'total': 'int'
    }

    attribute_map = {
        'templates': 'templates',
        'total': 'total'
    }

    def __init__(self, templates=None, total=None):
        """ListWatermarkTemplateResponse - a model defined in huaweicloud sdk"""
        
        super(ListWatermarkTemplateResponse, self).__init__()

        self._templates = None
        self._total = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if total is not None:
            self.total = total

    @property
    def templates(self):
        """Gets the templates of this ListWatermarkTemplateResponse.


        :return: The templates of this ListWatermarkTemplateResponse.
        :rtype: list[WatermarkTemplate]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListWatermarkTemplateResponse.


        :param templates: The templates of this ListWatermarkTemplateResponse.
        :type: list[WatermarkTemplate]
        """
        self._templates = templates

    @property
    def total(self):
        """Gets the total of this ListWatermarkTemplateResponse.


        :return: The total of this ListWatermarkTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListWatermarkTemplateResponse.


        :param total: The total of this ListWatermarkTemplateResponse.
        :type: int
        """
        self._total = total

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
