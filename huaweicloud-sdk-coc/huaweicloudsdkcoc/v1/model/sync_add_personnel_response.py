# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncAddPersonnelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added_ids': 'list[str]',
        'error_ids': 'list[str]'
    }

    attribute_map = {
        'added_ids': 'added_ids',
        'error_ids': 'error_ids'
    }

    def __init__(self, added_ids=None, error_ids=None):
        r"""SyncAddPersonnelResponse

        The model defined in huaweicloud sdk

        :param added_ids: 添加成功的ID
        :type added_ids: list[str]
        :param error_ids: 添加失败的ID
        :type error_ids: list[str]
        """
        
        super(SyncAddPersonnelResponse, self).__init__()

        self._added_ids = None
        self._error_ids = None
        self.discriminator = None

        if added_ids is not None:
            self.added_ids = added_ids
        if error_ids is not None:
            self.error_ids = error_ids

    @property
    def added_ids(self):
        r"""Gets the added_ids of this SyncAddPersonnelResponse.

        添加成功的ID

        :return: The added_ids of this SyncAddPersonnelResponse.
        :rtype: list[str]
        """
        return self._added_ids

    @added_ids.setter
    def added_ids(self, added_ids):
        r"""Sets the added_ids of this SyncAddPersonnelResponse.

        添加成功的ID

        :param added_ids: The added_ids of this SyncAddPersonnelResponse.
        :type added_ids: list[str]
        """
        self._added_ids = added_ids

    @property
    def error_ids(self):
        r"""Gets the error_ids of this SyncAddPersonnelResponse.

        添加失败的ID

        :return: The error_ids of this SyncAddPersonnelResponse.
        :rtype: list[str]
        """
        return self._error_ids

    @error_ids.setter
    def error_ids(self, error_ids):
        r"""Sets the error_ids of this SyncAddPersonnelResponse.

        添加失败的ID

        :param error_ids: The error_ids of this SyncAddPersonnelResponse.
        :type error_ids: list[str]
        """
        self._error_ids = error_ids

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
        if not isinstance(other, SyncAddPersonnelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
