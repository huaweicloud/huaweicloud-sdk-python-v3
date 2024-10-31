# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStorageModeTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_mode_type': 'str'
    }

    attribute_map = {
        'storage_mode_type': 'storage_mode_type'
    }

    def __init__(self, storage_mode_type=None):
        """ShowStorageModeTypeResponse

        The model defined in huaweicloud sdk

        :param storage_mode_type: 降冷模式。 取值如下： - WHOLE：整个媒资粒度。 - ORIGIN：原文件粒度。 
        :type storage_mode_type: str
        """
        
        super(ShowStorageModeTypeResponse, self).__init__()

        self._storage_mode_type = None
        self.discriminator = None

        if storage_mode_type is not None:
            self.storage_mode_type = storage_mode_type

    @property
    def storage_mode_type(self):
        """Gets the storage_mode_type of this ShowStorageModeTypeResponse.

        降冷模式。 取值如下： - WHOLE：整个媒资粒度。 - ORIGIN：原文件粒度。 

        :return: The storage_mode_type of this ShowStorageModeTypeResponse.
        :rtype: str
        """
        return self._storage_mode_type

    @storage_mode_type.setter
    def storage_mode_type(self, storage_mode_type):
        """Sets the storage_mode_type of this ShowStorageModeTypeResponse.

        降冷模式。 取值如下： - WHOLE：整个媒资粒度。 - ORIGIN：原文件粒度。 

        :param storage_mode_type: The storage_mode_type of this ShowStorageModeTypeResponse.
        :type storage_mode_type: str
        """
        self._storage_mode_type = storage_mode_type

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStorageModeTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
