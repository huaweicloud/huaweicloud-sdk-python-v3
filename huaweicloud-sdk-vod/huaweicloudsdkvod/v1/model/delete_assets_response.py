# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAssetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_result_array': 'list[DeleteResult]'
    }

    attribute_map = {
        'delete_result_array': 'delete_result_array'
    }

    def __init__(self, delete_result_array=None):
        """DeleteAssetsResponse

        The model defined in huaweicloud sdk

        :param delete_result_array: 删除媒资任务的处理结果。
        :type delete_result_array: list[:class:`huaweicloudsdkvod.v1.DeleteResult`]
        """
        
        super(DeleteAssetsResponse, self).__init__()

        self._delete_result_array = None
        self.discriminator = None

        if delete_result_array is not None:
            self.delete_result_array = delete_result_array

    @property
    def delete_result_array(self):
        """Gets the delete_result_array of this DeleteAssetsResponse.

        删除媒资任务的处理结果。

        :return: The delete_result_array of this DeleteAssetsResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.DeleteResult`]
        """
        return self._delete_result_array

    @delete_result_array.setter
    def delete_result_array(self, delete_result_array):
        """Sets the delete_result_array of this DeleteAssetsResponse.

        删除媒资任务的处理结果。

        :param delete_result_array: The delete_result_array of this DeleteAssetsResponse.
        :type delete_result_array: list[:class:`huaweicloudsdkvod.v1.DeleteResult`]
        """
        self._delete_result_array = delete_result_array

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
        if not isinstance(other, DeleteAssetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
