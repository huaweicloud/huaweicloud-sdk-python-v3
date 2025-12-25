# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateBaselineResult:

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
        r"""BatchOperateBaselineResult

        The model defined in huaweicloud sdk

        :param error_ids: 成功id列表
        :type error_ids: list[str]
        :param success_ids: 失败id列表
        :type success_ids: list[str]
        """
        
        

        self._error_ids = None
        self._success_ids = None
        self.discriminator = None

        self.error_ids = error_ids
        self.success_ids = success_ids

    @property
    def error_ids(self):
        r"""Gets the error_ids of this BatchOperateBaselineResult.

        成功id列表

        :return: The error_ids of this BatchOperateBaselineResult.
        :rtype: list[str]
        """
        return self._error_ids

    @error_ids.setter
    def error_ids(self, error_ids):
        r"""Sets the error_ids of this BatchOperateBaselineResult.

        成功id列表

        :param error_ids: The error_ids of this BatchOperateBaselineResult.
        :type error_ids: list[str]
        """
        self._error_ids = error_ids

    @property
    def success_ids(self):
        r"""Gets the success_ids of this BatchOperateBaselineResult.

        失败id列表

        :return: The success_ids of this BatchOperateBaselineResult.
        :rtype: list[str]
        """
        return self._success_ids

    @success_ids.setter
    def success_ids(self, success_ids):
        r"""Sets the success_ids of this BatchOperateBaselineResult.

        失败id列表

        :param success_ids: The success_ids of this BatchOperateBaselineResult.
        :type success_ids: list[str]
        """
        self._success_ids = success_ids

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchOperateBaselineResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
