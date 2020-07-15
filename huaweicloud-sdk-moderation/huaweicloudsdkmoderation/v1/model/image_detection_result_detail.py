# coding: utf-8

import pprint
import re

import six





class ImageDetectionResultDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'politics': 'list[ImageDetectionResultDetailPolitics]',
        'porn': 'list[ImageDetectionResultDetailPorn]',
        'terrorism': 'list[ImageDetectionResultDetailPorn]',
        'ad': 'list[ImageDetectionResultDetailPorn]'
    }

    attribute_map = {
        'politics': 'politics',
        'porn': 'porn',
        'terrorism': 'terrorism',
        'ad': 'ad'
    }

    def __init__(self, politics=None, porn=None, terrorism=None, ad=None):
        """ImageDetectionResultDetail - a model defined in huaweicloud sdk"""
        
        

        self._politics = None
        self._porn = None
        self._terrorism = None
        self._ad = None
        self.discriminator = None

        if politics is not None:
            self.politics = politics
        if porn is not None:
            self.porn = porn
        if terrorism is not None:
            self.terrorism = terrorism
        if ad is not None:
            self.ad = ad

    @property
    def politics(self):
        """Gets the politics of this ImageDetectionResultDetail.


        :return: The politics of this ImageDetectionResultDetail.
        :rtype: list[ImageDetectionResultDetailPolitics]
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this ImageDetectionResultDetail.


        :param politics: The politics of this ImageDetectionResultDetail.
        :type: list[ImageDetectionResultDetailPolitics]
        """
        self._politics = politics

    @property
    def porn(self):
        """Gets the porn of this ImageDetectionResultDetail.


        :return: The porn of this ImageDetectionResultDetail.
        :rtype: list[ImageDetectionResultDetailPorn]
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this ImageDetectionResultDetail.


        :param porn: The porn of this ImageDetectionResultDetail.
        :type: list[ImageDetectionResultDetailPorn]
        """
        self._porn = porn

    @property
    def terrorism(self):
        """Gets the terrorism of this ImageDetectionResultDetail.


        :return: The terrorism of this ImageDetectionResultDetail.
        :rtype: list[ImageDetectionResultDetailPorn]
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this ImageDetectionResultDetail.


        :param terrorism: The terrorism of this ImageDetectionResultDetail.
        :type: list[ImageDetectionResultDetailPorn]
        """
        self._terrorism = terrorism

    @property
    def ad(self):
        """Gets the ad of this ImageDetectionResultDetail.


        :return: The ad of this ImageDetectionResultDetail.
        :rtype: list[ImageDetectionResultDetailPorn]
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this ImageDetectionResultDetail.


        :param ad: The ad of this ImageDetectionResultDetail.
        :type: list[ImageDetectionResultDetailPorn]
        """
        self._ad = ad

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
        if not isinstance(other, ImageDetectionResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
