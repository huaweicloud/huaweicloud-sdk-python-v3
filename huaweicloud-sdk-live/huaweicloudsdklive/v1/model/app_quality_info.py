# coding: utf-8

import pprint
import re

import six





class AppQualityInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'quality_info': 'list[QualityInfo]'
    }

    attribute_map = {
        'app_name': 'app_name',
        'quality_info': 'quality_info'
    }

    def __init__(self, app_name=None, quality_info=None):
        """AppQualityInfo - a model defined in huaweicloud sdk"""
        
        

        self._app_name = None
        self._quality_info = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if quality_info is not None:
            self.quality_info = quality_info

    @property
    def app_name(self):
        """Gets the app_name of this AppQualityInfo.

        应用名称

        :return: The app_name of this AppQualityInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppQualityInfo.

        应用名称

        :param app_name: The app_name of this AppQualityInfo.
        :type: str
        """
        self._app_name = app_name

    @property
    def quality_info(self):
        """Gets the quality_info of this AppQualityInfo.

        视频质量信息

        :return: The quality_info of this AppQualityInfo.
        :rtype: list[QualityInfo]
        """
        return self._quality_info

    @quality_info.setter
    def quality_info(self, quality_info):
        """Sets the quality_info of this AppQualityInfo.

        视频质量信息

        :param quality_info: The quality_info of this AppQualityInfo.
        :type: list[QualityInfo]
        """
        self._quality_info = quality_info

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
        if not isinstance(other, AppQualityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
