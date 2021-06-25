# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateWatermarkTemplateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'upload_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'upload_url': 'upload_url'
    }

    def __init__(self, id=None, upload_url=None):
        """CreateWatermarkTemplateResponse - a model defined in huaweicloud sdk"""
        
        super(CreateWatermarkTemplateResponse, self).__init__()

        self._id = None
        self._upload_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if upload_url is not None:
            self.upload_url = upload_url

    @property
    def id(self):
        """Gets the id of this CreateWatermarkTemplateResponse.

        水印配置模板id<br/> 

        :return: The id of this CreateWatermarkTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateWatermarkTemplateResponse.

        水印配置模板id<br/> 

        :param id: The id of this CreateWatermarkTemplateResponse.
        :type: str
        """
        self._id = id

    @property
    def upload_url(self):
        """Gets the upload_url of this CreateWatermarkTemplateResponse.

        水印图片上传地址<br/> 

        :return: The upload_url of this CreateWatermarkTemplateResponse.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this CreateWatermarkTemplateResponse.

        水印图片上传地址<br/> 

        :param upload_url: The upload_url of this CreateWatermarkTemplateResponse.
        :type: str
        """
        self._upload_url = upload_url

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
        if not isinstance(other, CreateWatermarkTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other