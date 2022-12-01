# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkipPreCheckInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'skipped_precheck_list': 'list[str]',
        'skip_reason': 'str'
    }

    attribute_map = {
        'skipped_precheck_list': 'skipped_precheck_list',
        'skip_reason': 'skip_reason'
    }

    def __init__(self, skipped_precheck_list=None, skip_reason=None):
        """SkipPreCheckInfo

        The model defined in huaweicloud sdk

        :param skipped_precheck_list: 跳过的预检查项。
        :type skipped_precheck_list: list[str]
        :param skip_reason: 跳过预检查原因。
        :type skip_reason: str
        """
        
        

        self._skipped_precheck_list = None
        self._skip_reason = None
        self.discriminator = None

        self.skipped_precheck_list = skipped_precheck_list
        self.skip_reason = skip_reason

    @property
    def skipped_precheck_list(self):
        """Gets the skipped_precheck_list of this SkipPreCheckInfo.

        跳过的预检查项。

        :return: The skipped_precheck_list of this SkipPreCheckInfo.
        :rtype: list[str]
        """
        return self._skipped_precheck_list

    @skipped_precheck_list.setter
    def skipped_precheck_list(self, skipped_precheck_list):
        """Sets the skipped_precheck_list of this SkipPreCheckInfo.

        跳过的预检查项。

        :param skipped_precheck_list: The skipped_precheck_list of this SkipPreCheckInfo.
        :type skipped_precheck_list: list[str]
        """
        self._skipped_precheck_list = skipped_precheck_list

    @property
    def skip_reason(self):
        """Gets the skip_reason of this SkipPreCheckInfo.

        跳过预检查原因。

        :return: The skip_reason of this SkipPreCheckInfo.
        :rtype: str
        """
        return self._skip_reason

    @skip_reason.setter
    def skip_reason(self, skip_reason):
        """Sets the skip_reason of this SkipPreCheckInfo.

        跳过预检查原因。

        :param skip_reason: The skip_reason of this SkipPreCheckInfo.
        :type skip_reason: str
        """
        self._skip_reason = skip_reason

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
        if not isinstance(other, SkipPreCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
