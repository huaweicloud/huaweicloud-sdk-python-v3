# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OverwriteResultResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_ids': 'str',
        'failed_ids': 'str'
    }

    attribute_map = {
        'success_ids': 'success_ids',
        'failed_ids': 'failed_ids'
    }

    def __init__(self, success_ids=None, failed_ids=None):
        r"""OverwriteResultResp

        The model defined in huaweicloud sdk

        :param success_ids: **参数解释**：已覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 
        :type success_ids: str
        :param failed_ids: **参数解释**：未覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 
        :type failed_ids: str
        """
        
        

        self._success_ids = None
        self._failed_ids = None
        self.discriminator = None

        if success_ids is not None:
            self.success_ids = success_ids
        if failed_ids is not None:
            self.failed_ids = failed_ids

    @property
    def success_ids(self):
        r"""Gets the success_ids of this OverwriteResultResp.

        **参数解释**：已覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 

        :return: The success_ids of this OverwriteResultResp.
        :rtype: str
        """
        return self._success_ids

    @success_ids.setter
    def success_ids(self, success_ids):
        r"""Sets the success_ids of this OverwriteResultResp.

        **参数解释**：已覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 

        :param success_ids: The success_ids of this OverwriteResultResp.
        :type success_ids: str
        """
        self._success_ids = success_ids

    @property
    def failed_ids(self):
        r"""Gets the failed_ids of this OverwriteResultResp.

        **参数解释**：未覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 

        :return: The failed_ids of this OverwriteResultResp.
        :rtype: str
        """
        return self._failed_ids

    @failed_ids.setter
    def failed_ids(self, failed_ids):
        r"""Sets the failed_ids of this OverwriteResultResp.

        **参数解释**：未覆盖的模板ID值。 **取值范围**：长度为[2,64]个字符。 

        :param failed_ids: The failed_ids of this OverwriteResultResp.
        :type failed_ids: str
        """
        self._failed_ids = failed_ids

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
        if not isinstance(other, OverwriteResultResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
