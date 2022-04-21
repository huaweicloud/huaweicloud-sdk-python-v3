# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateErrorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'workflow_urn': 'str',
        'error_detail': 'str'
    }

    attribute_map = {
        'workflow_urn': 'workflow_urn',
        'error_detail': 'error_detail'
    }

    def __init__(self, workflow_urn=None, error_detail=None):
        """OperateErrorInfo

        The model defined in huaweicloud sdk

        :param workflow_urn: 唯一标识ID，流程URN
        :type workflow_urn: str
        :param error_detail: 错误详情
        :type error_detail: str
        """
        
        

        self._workflow_urn = None
        self._error_detail = None
        self.discriminator = None

        if workflow_urn is not None:
            self.workflow_urn = workflow_urn
        if error_detail is not None:
            self.error_detail = error_detail

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this OperateErrorInfo.

        唯一标识ID，流程URN

        :return: The workflow_urn of this OperateErrorInfo.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this OperateErrorInfo.

        唯一标识ID，流程URN

        :param workflow_urn: The workflow_urn of this OperateErrorInfo.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def error_detail(self):
        """Gets the error_detail of this OperateErrorInfo.

        错误详情

        :return: The error_detail of this OperateErrorInfo.
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """Sets the error_detail of this OperateErrorInfo.

        错误详情

        :param error_detail: The error_detail of this OperateErrorInfo.
        :type error_detail: str
        """
        self._error_detail = error_detail

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
        if not isinstance(other, OperateErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
