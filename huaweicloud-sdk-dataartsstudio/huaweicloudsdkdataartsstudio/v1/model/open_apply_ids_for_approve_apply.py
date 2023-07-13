# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenApplyIdsForApproveApply:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_result': 'bool',
        'apply_ids': 'list[str]'
    }

    attribute_map = {
        'apply_result': 'apply_result',
        'apply_ids': 'apply_ids'
    }

    def __init__(self, apply_result=None, apply_ids=None):
        """OpenApplyIdsForApproveApply

        The model defined in huaweicloud sdk

        :param apply_result: 申请结果
        :type apply_result: bool
        :param apply_ids: 申请编号列表
        :type apply_ids: list[str]
        """
        
        

        self._apply_result = None
        self._apply_ids = None
        self.discriminator = None

        if apply_result is not None:
            self.apply_result = apply_result
        if apply_ids is not None:
            self.apply_ids = apply_ids

    @property
    def apply_result(self):
        """Gets the apply_result of this OpenApplyIdsForApproveApply.

        申请结果

        :return: The apply_result of this OpenApplyIdsForApproveApply.
        :rtype: bool
        """
        return self._apply_result

    @apply_result.setter
    def apply_result(self, apply_result):
        """Sets the apply_result of this OpenApplyIdsForApproveApply.

        申请结果

        :param apply_result: The apply_result of this OpenApplyIdsForApproveApply.
        :type apply_result: bool
        """
        self._apply_result = apply_result

    @property
    def apply_ids(self):
        """Gets the apply_ids of this OpenApplyIdsForApproveApply.

        申请编号列表

        :return: The apply_ids of this OpenApplyIdsForApproveApply.
        :rtype: list[str]
        """
        return self._apply_ids

    @apply_ids.setter
    def apply_ids(self, apply_ids):
        """Sets the apply_ids of this OpenApplyIdsForApproveApply.

        申请编号列表

        :param apply_ids: The apply_ids of this OpenApplyIdsForApproveApply.
        :type apply_ids: list[str]
        """
        self._apply_ids = apply_ids

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
        if not isinstance(other, OpenApplyIdsForApproveApply):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
