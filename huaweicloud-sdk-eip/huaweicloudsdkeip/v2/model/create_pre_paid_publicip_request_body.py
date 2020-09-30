# coding: utf-8

import pprint
import re

import six





class CreatePrePaidPublicipRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip': 'CreatePrePaidPublicipOption',
        'bandwidth': 'CreatePublicipBandwidthOption',
        'extend_param': 'CreatePrePaidPublicipExtendParamOption'
    }

    attribute_map = {
        'publicip': 'publicip',
        'bandwidth': 'bandwidth',
        'extend_param': 'extendParam'
    }

    def __init__(self, publicip=None, bandwidth=None, extend_param=None):
        """CreatePrePaidPublicipRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._publicip = None
        self._bandwidth = None
        self._extend_param = None
        self.discriminator = None

        self.publicip = publicip
        self.bandwidth = bandwidth
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def publicip(self):
        """Gets the publicip of this CreatePrePaidPublicipRequestBody.


        :return: The publicip of this CreatePrePaidPublicipRequestBody.
        :rtype: CreatePrePaidPublicipOption
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreatePrePaidPublicipRequestBody.


        :param publicip: The publicip of this CreatePrePaidPublicipRequestBody.
        :type: CreatePrePaidPublicipOption
        """
        self._publicip = publicip

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreatePrePaidPublicipRequestBody.


        :return: The bandwidth of this CreatePrePaidPublicipRequestBody.
        :rtype: CreatePublicipBandwidthOption
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreatePrePaidPublicipRequestBody.


        :param bandwidth: The bandwidth of this CreatePrePaidPublicipRequestBody.
        :type: CreatePublicipBandwidthOption
        """
        self._bandwidth = bandwidth

    @property
    def extend_param(self):
        """Gets the extend_param of this CreatePrePaidPublicipRequestBody.


        :return: The extend_param of this CreatePrePaidPublicipRequestBody.
        :rtype: CreatePrePaidPublicipExtendParamOption
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreatePrePaidPublicipRequestBody.


        :param extend_param: The extend_param of this CreatePrePaidPublicipRequestBody.
        :type: CreatePrePaidPublicipExtendParamOption
        """
        self._extend_param = extend_param

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
        if not isinstance(other, CreatePrePaidPublicipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
