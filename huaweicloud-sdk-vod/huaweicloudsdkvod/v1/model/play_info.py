# coding: utf-8

import pprint
import re

import six





class PlayInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_type': 'str',
        'url': 'str',
        'encrypted': 'int',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'play_type': 'play_type',
        'url': 'url',
        'encrypted': 'encrypted',
        'meta_data': 'meta_data'
    }

    def __init__(self, play_type=None, url=None, encrypted=None, meta_data=None):
        """PlayInfo - a model defined in huaweicloud sdk"""
        
        

        self._play_type = None
        self._url = None
        self._encrypted = None
        self._meta_data = None
        self.discriminator = None

        if play_type is not None:
            self.play_type = play_type
        if url is not None:
            self.url = url
        if encrypted is not None:
            self.encrypted = encrypted
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def play_type(self):
        """Gets the play_type of this PlayInfo.

        播放协议类型<br/> 

        :return: The play_type of this PlayInfo.
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        """Sets the play_type of this PlayInfo.

        播放协议类型<br/> 

        :param play_type: The play_type of this PlayInfo.
        :type: str
        """
        self._play_type = play_type

    @property
    def url(self):
        """Gets the url of this PlayInfo.

        播放url<br/> 

        :return: The url of this PlayInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PlayInfo.

        播放url<br/> 

        :param url: The url of this PlayInfo.
        :type: str
        """
        self._url = url

    @property
    def encrypted(self):
        """Gets the encrypted of this PlayInfo.

        标记流是否已被加密，取值[0,1] 0表示未加密，1表示已被加密。<br/> 

        :return: The encrypted of this PlayInfo.
        :rtype: int
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this PlayInfo.

        标记流是否已被加密，取值[0,1] 0表示未加密，1表示已被加密。<br/> 

        :param encrypted: The encrypted of this PlayInfo.
        :type: int
        """
        self._encrypted = encrypted

    @property
    def meta_data(self):
        """Gets the meta_data of this PlayInfo.


        :return: The meta_data of this PlayInfo.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this PlayInfo.


        :param meta_data: The meta_data of this PlayInfo.
        :type: MetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, PlayInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other