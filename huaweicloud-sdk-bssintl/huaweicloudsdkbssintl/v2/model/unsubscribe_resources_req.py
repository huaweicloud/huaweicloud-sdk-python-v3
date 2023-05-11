# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnsubscribeResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'unsubscribe_type': 'int',
        'unsubscribe_reason_type': 'int',
        'unsubscribe_reason': 'str'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'unsubscribe_type': 'unsubscribe_type',
        'unsubscribe_reason_type': 'unsubscribe_reason_type',
        'unsubscribe_reason': 'unsubscribe_reason'
    }

    def __init__(self, resource_ids=None, unsubscribe_type=None, unsubscribe_reason_type=None, unsubscribe_reason=None):
        """UnsubscribeResourcesReq

        The model defined in huaweicloud sdk

        :param resource_ids: 资源ID列表。 最大支持1次性输入10个资源ID，只能输入主资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。
        :type resource_ids: list[str]
        :param unsubscribe_type: 退订类型，取值如下： 1：退订资源及其已续费周期。2：只退订资源已续费周期，不退订资源。
        :type unsubscribe_type: int
        :param unsubscribe_reason_type: 退订理由分类，取值如下： 1：产品不好用2：产品功能无法满足需求3：不会操作/操作过于复杂4：对服务不满意5：其他
        :type unsubscribe_reason_type: int
        :param unsubscribe_reason: 退订原因，一般由客户输入。
        :type unsubscribe_reason: str
        """
        
        

        self._resource_ids = None
        self._unsubscribe_type = None
        self._unsubscribe_reason_type = None
        self._unsubscribe_reason = None
        self.discriminator = None

        self.resource_ids = resource_ids
        self.unsubscribe_type = unsubscribe_type
        if unsubscribe_reason_type is not None:
            self.unsubscribe_reason_type = unsubscribe_reason_type
        if unsubscribe_reason is not None:
            self.unsubscribe_reason = unsubscribe_reason

    @property
    def resource_ids(self):
        """Gets the resource_ids of this UnsubscribeResourcesReq.

        资源ID列表。 最大支持1次性输入10个资源ID，只能输入主资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。

        :return: The resource_ids of this UnsubscribeResourcesReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this UnsubscribeResourcesReq.

        资源ID列表。 最大支持1次性输入10个资源ID，只能输入主资源ID。 哪些资源是主资源请根据“查询客户包年/包月资源列表”接口响应参数中的“is_main_resource”来标识。

        :param resource_ids: The resource_ids of this UnsubscribeResourcesReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def unsubscribe_type(self):
        """Gets the unsubscribe_type of this UnsubscribeResourcesReq.

        退订类型，取值如下： 1：退订资源及其已续费周期。2：只退订资源已续费周期，不退订资源。

        :return: The unsubscribe_type of this UnsubscribeResourcesReq.
        :rtype: int
        """
        return self._unsubscribe_type

    @unsubscribe_type.setter
    def unsubscribe_type(self, unsubscribe_type):
        """Sets the unsubscribe_type of this UnsubscribeResourcesReq.

        退订类型，取值如下： 1：退订资源及其已续费周期。2：只退订资源已续费周期，不退订资源。

        :param unsubscribe_type: The unsubscribe_type of this UnsubscribeResourcesReq.
        :type unsubscribe_type: int
        """
        self._unsubscribe_type = unsubscribe_type

    @property
    def unsubscribe_reason_type(self):
        """Gets the unsubscribe_reason_type of this UnsubscribeResourcesReq.

        退订理由分类，取值如下： 1：产品不好用2：产品功能无法满足需求3：不会操作/操作过于复杂4：对服务不满意5：其他

        :return: The unsubscribe_reason_type of this UnsubscribeResourcesReq.
        :rtype: int
        """
        return self._unsubscribe_reason_type

    @unsubscribe_reason_type.setter
    def unsubscribe_reason_type(self, unsubscribe_reason_type):
        """Sets the unsubscribe_reason_type of this UnsubscribeResourcesReq.

        退订理由分类，取值如下： 1：产品不好用2：产品功能无法满足需求3：不会操作/操作过于复杂4：对服务不满意5：其他

        :param unsubscribe_reason_type: The unsubscribe_reason_type of this UnsubscribeResourcesReq.
        :type unsubscribe_reason_type: int
        """
        self._unsubscribe_reason_type = unsubscribe_reason_type

    @property
    def unsubscribe_reason(self):
        """Gets the unsubscribe_reason of this UnsubscribeResourcesReq.

        退订原因，一般由客户输入。

        :return: The unsubscribe_reason of this UnsubscribeResourcesReq.
        :rtype: str
        """
        return self._unsubscribe_reason

    @unsubscribe_reason.setter
    def unsubscribe_reason(self, unsubscribe_reason):
        """Sets the unsubscribe_reason of this UnsubscribeResourcesReq.

        退订原因，一般由客户输入。

        :param unsubscribe_reason: The unsubscribe_reason of this UnsubscribeResourcesReq.
        :type unsubscribe_reason: str
        """
        self._unsubscribe_reason = unsubscribe_reason

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
        if not isinstance(other, UnsubscribeResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
