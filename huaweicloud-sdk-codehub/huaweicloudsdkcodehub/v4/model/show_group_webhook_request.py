# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupWebhookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'hook_id': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'hook_id': 'hook_id'
    }

    def __init__(self, group_id=None, hook_id=None):
        r"""ShowGroupWebhookRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id
        :type group_id: int
        :param hook_id: **参数解释：**  Webhook id。
        :type hook_id: int
        """
        
        

        self._group_id = None
        self._hook_id = None
        self.discriminator = None

        self.group_id = group_id
        self.hook_id = hook_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowGroupWebhookRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :return: The group_id of this ShowGroupWebhookRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowGroupWebhookRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :param group_id: The group_id of this ShowGroupWebhookRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def hook_id(self):
        r"""Gets the hook_id of this ShowGroupWebhookRequest.

        **参数解释：**  Webhook id。

        :return: The hook_id of this ShowGroupWebhookRequest.
        :rtype: int
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this ShowGroupWebhookRequest.

        **参数解释：**  Webhook id。

        :param hook_id: The hook_id of this ShowGroupWebhookRequest.
        :type hook_id: int
        """
        self._hook_id = hook_id

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
        if not isinstance(other, ShowGroupWebhookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
