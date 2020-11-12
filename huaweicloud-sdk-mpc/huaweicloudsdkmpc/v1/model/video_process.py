# coding: utf-8

import pprint
import re

import six





class VideoProcess:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rotate': 'int',
        'black_enhance': 'BlackEnhance',
        'adaptation': 'str',
        'upsample': 'int'
    }

    attribute_map = {
        'rotate': 'rotate',
        'black_enhance': 'black_enhance',
        'adaptation': 'adaptation',
        'upsample': 'upsample'
    }

    def __init__(self, rotate=None, black_enhance=None, adaptation='SHORT', upsample=0):
        """VideoProcess - a model defined in huaweicloud sdk"""
        
        

        self._rotate = None
        self._black_enhance = None
        self._adaptation = None
        self._upsample = None
        self.discriminator = None

        if rotate is not None:
            self.rotate = rotate
        if black_enhance is not None:
            self.black_enhance = black_enhance
        if adaptation is not None:
            self.adaptation = adaptation
        if upsample is not None:
            self.upsample = upsample

    @property
    def rotate(self):
        """Gets the rotate of this VideoProcess.

        视频顺时针旋转角度。  - 0：表示不旋转 - 1：表示顺时针旋转90度 - 2：表示顺时针旋转180度 - 3：表示顺时针旋转270度 

        :return: The rotate of this VideoProcess.
        :rtype: int
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this VideoProcess.

        视频顺时针旋转角度。  - 0：表示不旋转 - 1：表示顺时针旋转90度 - 2：表示顺时针旋转180度 - 3：表示顺时针旋转270度 

        :param rotate: The rotate of this VideoProcess.
        :type: int
        """
        self._rotate = rotate

    @property
    def black_enhance(self):
        """Gets the black_enhance of this VideoProcess.


        :return: The black_enhance of this VideoProcess.
        :rtype: BlackEnhance
        """
        return self._black_enhance

    @black_enhance.setter
    def black_enhance(self, black_enhance):
        """Sets the black_enhance of this VideoProcess.


        :param black_enhance: The black_enhance of this VideoProcess.
        :type: BlackEnhance
        """
        self._black_enhance = black_enhance

    @property
    def adaptation(self):
        """Gets the adaptation of this VideoProcess.

        长短边自适应控制字段： - SHORT：表示短边自适应 - LONG：表示长边自适应 - NONE：表示不自适应 

        :return: The adaptation of this VideoProcess.
        :rtype: str
        """
        return self._adaptation

    @adaptation.setter
    def adaptation(self, adaptation):
        """Sets the adaptation of this VideoProcess.

        长短边自适应控制字段： - SHORT：表示短边自适应 - LONG：表示长边自适应 - NONE：表示不自适应 

        :param adaptation: The adaptation of this VideoProcess.
        :type: str
        """
        self._adaptation = adaptation

    @property
    def upsample(self):
        """Gets the upsample of this VideoProcess.

        是否开启上采样，如支持从480P的片源转为720P，可取值为:  - 0：表示上采样关闭， - 1：表示上采样开启. 

        :return: The upsample of this VideoProcess.
        :rtype: int
        """
        return self._upsample

    @upsample.setter
    def upsample(self, upsample):
        """Sets the upsample of this VideoProcess.

        是否开启上采样，如支持从480P的片源转为720P，可取值为:  - 0：表示上采样关闭， - 1：表示上采样开启. 

        :param upsample: The upsample of this VideoProcess.
        :type: int
        """
        self._upsample = upsample

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
        if not isinstance(other, VideoProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
