# coding: utf-8

import pprint
import re

import six





class ConfirmAssetUploadReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status'
    }

    def __init__(self, asset_id=None, status=None):
        """ConfirmAssetUploadReq - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._status = None
        self.discriminator = None

        self.asset_id = asset_id
        self.status = status

    @property
    def asset_id(self):
        """Gets the asset_id of this ConfirmAssetUploadReq.

        媒体ID<br/> 

        :return: The asset_id of this ConfirmAssetUploadReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ConfirmAssetUploadReq.

        媒体ID<br/> 

        :param asset_id: The asset_id of this ConfirmAssetUploadReq.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this ConfirmAssetUploadReq.

        上传状态<br/> 

        :return: The status of this ConfirmAssetUploadReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfirmAssetUploadReq.

        上传状态<br/> 

        :param status: The status of this ConfirmAssetUploadReq.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, ConfirmAssetUploadReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other