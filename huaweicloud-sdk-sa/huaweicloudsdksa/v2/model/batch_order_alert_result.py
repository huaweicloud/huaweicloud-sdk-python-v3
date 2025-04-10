# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOrderAlertResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_ids': 'list[str]',
        'success_ids': 'list[str]'
    }

    attribute_map = {
        'error_ids': 'error_ids',
        'success_ids': 'success_ids'
    }

    def __init__(self, error_ids=None, success_ids=None):
        r"""BatchOrderAlertResult

        The model defined in huaweicloud sdk

        :param error_ids: 失败id
        :type error_ids: list[str]
        :param success_ids: 成功败id
        :type success_ids: list[str]
        """
        
        

        self._error_ids = None
        self._success_ids = None
        self.discriminator = None

        if error_ids is not None:
            self.error_ids = error_ids
        if success_ids is not None:
            self.success_ids = success_ids

    @property
    def error_ids(self):
        r"""Gets the error_ids of this BatchOrderAlertResult.

        失败id

        :return: The error_ids of this BatchOrderAlertResult.
        :rtype: list[str]
        """
        return self._error_ids

    @error_ids.setter
    def error_ids(self, error_ids):
        r"""Sets the error_ids of this BatchOrderAlertResult.

        失败id

        :param error_ids: The error_ids of this BatchOrderAlertResult.
        :type error_ids: list[str]
        """
        self._error_ids = error_ids

    @property
    def success_ids(self):
        r"""Gets the success_ids of this BatchOrderAlertResult.

        成功败id

        :return: The success_ids of this BatchOrderAlertResult.
        :rtype: list[str]
        """
        return self._success_ids

    @success_ids.setter
    def success_ids(self, success_ids):
        r"""Sets the success_ids of this BatchOrderAlertResult.

        成功败id

        :param success_ids: The success_ids of this BatchOrderAlertResult.
        :type success_ids: list[str]
        """
        self._success_ids = success_ids

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
        if not isinstance(other, BatchOrderAlertResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
