# coding: utf-8

import pprint
import re

import six





class Thumbnail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tar': 'int',
        'out': 'ObsObjInfo',
        'params': 'ThumbnailPara'
    }

    attribute_map = {
        'tar': 'tar',
        'out': 'out',
        'params': 'params'
    }

    def __init__(self, tar=1, out=None, params=None):
        """Thumbnail - a model defined in huaweicloud sdk"""
        
        

        self._tar = None
        self._out = None
        self._params = None
        self.discriminator = None

        if tar is not None:
            self.tar = tar
        if out is not None:
            self.out = out
        self.params = params

    @property
    def tar(self):
        """Gets the tar of this Thumbnail.

        是否压缩抽帧图片生成tar包 - 0：表示压缩 - 1：表示不压缩 

        :return: The tar of this Thumbnail.
        :rtype: int
        """
        return self._tar

    @tar.setter
    def tar(self, tar):
        """Sets the tar of this Thumbnail.

        是否压缩抽帧图片生成tar包 - 0：表示压缩 - 1：表示不压缩 

        :param tar: The tar of this Thumbnail.
        :type: int
        """
        self._tar = tar

    @property
    def out(self):
        """Gets the out of this Thumbnail.


        :return: The out of this Thumbnail.
        :rtype: ObsObjInfo
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this Thumbnail.


        :param out: The out of this Thumbnail.
        :type: ObsObjInfo
        """
        self._out = out

    @property
    def params(self):
        """Gets the params of this Thumbnail.


        :return: The params of this Thumbnail.
        :rtype: ThumbnailPara
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Thumbnail.


        :param params: The params of this Thumbnail.
        :type: ThumbnailPara
        """
        self._params = params

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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
