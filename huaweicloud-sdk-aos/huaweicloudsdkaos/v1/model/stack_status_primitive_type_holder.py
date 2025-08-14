# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackStatusPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        r"""StackStatusPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param status: 资源栈的状态 * &#x60;CREATION_COMPLETE&#x60; - 生成空资源栈完成，并没有任何部署 * &#x60;DEPLOYMENT_IN_PROGRESS&#x60; - 正在部署，请等待 * &#x60;DEPLOYMENT_FAILED&#x60; - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * &#x60;DEPLOYMENT_COMPLETE&#x60; - 部署完成 * &#x60;ROLLBACK_IN_PROGRESS&#x60; - 部署失败，正在回滚，请等待 * &#x60;ROLLBACK_FAILED&#x60; - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * &#x60;ROLLBACK_COMPLETE&#x60; - 回滚完成 * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除，请等待 * &#x60;DELETION_FAILED&#x60; - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情
        :type status: str
        """
        
        

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        r"""Gets the status of this StackStatusPrimitiveTypeHolder.

        资源栈的状态 * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署 * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待 * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * `DEPLOYMENT_COMPLETE` - 部署完成 * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待 * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * `ROLLBACK_COMPLETE` - 回滚完成 * `DELETION_IN_PROGRESS` - 正在删除，请等待 * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :return: The status of this StackStatusPrimitiveTypeHolder.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StackStatusPrimitiveTypeHolder.

        资源栈的状态 * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署 * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待 * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * `DEPLOYMENT_COMPLETE` - 部署完成 * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待 * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情 * `ROLLBACK_COMPLETE` - 回滚完成 * `DELETION_IN_PROGRESS` - 正在删除，请等待 * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :param status: The status of this StackStatusPrimitiveTypeHolder.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, StackStatusPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
