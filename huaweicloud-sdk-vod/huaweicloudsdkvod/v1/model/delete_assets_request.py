# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAssetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'asset_id': 'list[str]',
        'delete_type': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'delete_type': 'delete_type'
    }

    def __init__(self, asset_id=None, delete_type=None):
        """DeleteAssetsRequest

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID，支持一次删除多个媒资，批量删除时以逗号分隔。
        :type asset_id: list[str]
        :param delete_type: 删除类型，当值为origin时只删除源文件，保留转码后文件。
        :type delete_type: str
        """
        
        

        self._asset_id = None
        self._delete_type = None
        self.discriminator = None

        self.asset_id = asset_id
        if delete_type is not None:
            self.delete_type = delete_type

    @property
    def asset_id(self):
        """Gets the asset_id of this DeleteAssetsRequest.

        媒资ID，支持一次删除多个媒资，批量删除时以逗号分隔。

        :return: The asset_id of this DeleteAssetsRequest.
        :rtype: list[str]
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this DeleteAssetsRequest.

        媒资ID，支持一次删除多个媒资，批量删除时以逗号分隔。

        :param asset_id: The asset_id of this DeleteAssetsRequest.
        :type asset_id: list[str]
        """
        self._asset_id = asset_id

    @property
    def delete_type(self):
        """Gets the delete_type of this DeleteAssetsRequest.

        删除类型，当值为origin时只删除源文件，保留转码后文件。

        :return: The delete_type of this DeleteAssetsRequest.
        :rtype: str
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        """Sets the delete_type of this DeleteAssetsRequest.

        删除类型，当值为origin时只删除源文件，保留转码后文件。

        :param delete_type: The delete_type of this DeleteAssetsRequest.
        :type delete_type: str
        """
        self._delete_type = delete_type

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
        if not isinstance(other, DeleteAssetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
