# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBlockchainStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bcs': 'Detail',
        'eip': 'Detail',
        'sfs': 'Detail',
        'obs': 'Detail',
        'kafka': 'Detail',
        'cce': 'ComCCE'
    }

    attribute_map = {
        'bcs': 'bcs',
        'eip': 'eip',
        'sfs': 'sfs',
        'obs': 'obs',
        'kafka': 'kafka',
        'cce': 'cce'
    }

    def __init__(self, bcs=None, eip=None, sfs=None, obs=None, kafka=None, cce=None):
        """ShowBlockchainStatusResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bcs = None
        self._eip = None
        self._sfs = None
        self._obs = None
        self._kafka = None
        self._cce = None
        self.discriminator = None

        if bcs is not None:
            self.bcs = bcs
        if eip is not None:
            self.eip = eip
        if sfs is not None:
            self.sfs = sfs
        if obs is not None:
            self.obs = obs
        if kafka is not None:
            self.kafka = kafka
        if cce is not None:
            self.cce = cce

    @property
    def bcs(self):
        """Gets the bcs of this ShowBlockchainStatusResponse.


        :return: The bcs of this ShowBlockchainStatusResponse.
        :rtype: Detail
        """
        return self._bcs

    @bcs.setter
    def bcs(self, bcs):
        """Sets the bcs of this ShowBlockchainStatusResponse.


        :param bcs: The bcs of this ShowBlockchainStatusResponse.
        :type: Detail
        """
        self._bcs = bcs

    @property
    def eip(self):
        """Gets the eip of this ShowBlockchainStatusResponse.


        :return: The eip of this ShowBlockchainStatusResponse.
        :rtype: Detail
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this ShowBlockchainStatusResponse.


        :param eip: The eip of this ShowBlockchainStatusResponse.
        :type: Detail
        """
        self._eip = eip

    @property
    def sfs(self):
        """Gets the sfs of this ShowBlockchainStatusResponse.


        :return: The sfs of this ShowBlockchainStatusResponse.
        :rtype: Detail
        """
        return self._sfs

    @sfs.setter
    def sfs(self, sfs):
        """Sets the sfs of this ShowBlockchainStatusResponse.


        :param sfs: The sfs of this ShowBlockchainStatusResponse.
        :type: Detail
        """
        self._sfs = sfs

    @property
    def obs(self):
        """Gets the obs of this ShowBlockchainStatusResponse.


        :return: The obs of this ShowBlockchainStatusResponse.
        :rtype: Detail
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """Sets the obs of this ShowBlockchainStatusResponse.


        :param obs: The obs of this ShowBlockchainStatusResponse.
        :type: Detail
        """
        self._obs = obs

    @property
    def kafka(self):
        """Gets the kafka of this ShowBlockchainStatusResponse.


        :return: The kafka of this ShowBlockchainStatusResponse.
        :rtype: Detail
        """
        return self._kafka

    @kafka.setter
    def kafka(self, kafka):
        """Sets the kafka of this ShowBlockchainStatusResponse.


        :param kafka: The kafka of this ShowBlockchainStatusResponse.
        :type: Detail
        """
        self._kafka = kafka

    @property
    def cce(self):
        """Gets the cce of this ShowBlockchainStatusResponse.


        :return: The cce of this ShowBlockchainStatusResponse.
        :rtype: ComCCE
        """
        return self._cce

    @cce.setter
    def cce(self, cce):
        """Sets the cce of this ShowBlockchainStatusResponse.


        :param cce: The cce of this ShowBlockchainStatusResponse.
        :type: ComCCE
        """
        self._cce = cce

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
        if not isinstance(other, ShowBlockchainStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
