# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteManualBackupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_results': 'list[DeleteBackupResult]'
    }

    attribute_map = {
        'delete_results': 'delete_results'
    }

    def __init__(self, delete_results=None):
        """BatchDeleteManualBackupResponse

        The model defined in huaweicloud sdk

        :param delete_results: 备份删除结果
        :type delete_results: list[:class:`huaweicloudsdkrds.v3.DeleteBackupResult`]
        """
        
        super(BatchDeleteManualBackupResponse, self).__init__()

        self._delete_results = None
        self.discriminator = None

        if delete_results is not None:
            self.delete_results = delete_results

    @property
    def delete_results(self):
        """Gets the delete_results of this BatchDeleteManualBackupResponse.

        备份删除结果

        :return: The delete_results of this BatchDeleteManualBackupResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DeleteBackupResult`]
        """
        return self._delete_results

    @delete_results.setter
    def delete_results(self, delete_results):
        """Sets the delete_results of this BatchDeleteManualBackupResponse.

        备份删除结果

        :param delete_results: The delete_results of this BatchDeleteManualBackupResponse.
        :type delete_results: list[:class:`huaweicloudsdkrds.v3.DeleteBackupResult`]
        """
        self._delete_results = delete_results

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
        if not isinstance(other, BatchDeleteManualBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
