# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UploadMetaDataByUrlResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'upload_assets': 'list[UploadAsset]'
    }

    attribute_map = {
        'upload_assets': 'upload_assets'
    }

    def __init__(self, upload_assets=None):
        """UploadMetaDataByUrlResponse - a model defined in huaweicloud sdk"""
        
        super(UploadMetaDataByUrlResponse, self).__init__()

        self._upload_assets = None
        self.discriminator = None

        if upload_assets is not None:
            self.upload_assets = upload_assets

    @property
    def upload_assets(self):
        """Gets the upload_assets of this UploadMetaDataByUrlResponse.

        待拉取创建的媒资元数据

        :return: The upload_assets of this UploadMetaDataByUrlResponse.
        :rtype: list[UploadAsset]
        """
        return self._upload_assets

    @upload_assets.setter
    def upload_assets(self, upload_assets):
        """Sets the upload_assets of this UploadMetaDataByUrlResponse.

        待拉取创建的媒资元数据

        :param upload_assets: The upload_assets of this UploadMetaDataByUrlResponse.
        :type: list[UploadAsset]
        """
        self._upload_assets = upload_assets

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
        if not isinstance(other, UploadMetaDataByUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other