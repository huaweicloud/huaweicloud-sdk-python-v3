# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationSubscriptionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'type': 'str',
        'body': 'UpdateRepoNotificationSubscriptionDto'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, repository_id=None, type=None, body=None):
        r"""UpdateNotificationSubscriptionRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param type: **参数解释：** 通知类型。 **取值范围：**   - internal_message，站内信。   - email，邮件。   - qyweixin，企业微信。   - feishu，飞书。   - dingding，钉钉。
        :type type: str
        :param body: Body of the UpdateNotificationSubscriptionRequest
        :type body: :class:`huaweicloudsdkcodehub.v4.UpdateRepoNotificationSubscriptionDto`
        """
        
        

        self._repository_id = None
        self._type = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        self.type = type
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateNotificationSubscriptionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this UpdateNotificationSubscriptionRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateNotificationSubscriptionRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this UpdateNotificationSubscriptionRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def type(self):
        r"""Gets the type of this UpdateNotificationSubscriptionRequest.

        **参数解释：** 通知类型。 **取值范围：**   - internal_message，站内信。   - email，邮件。   - qyweixin，企业微信。   - feishu，飞书。   - dingding，钉钉。

        :return: The type of this UpdateNotificationSubscriptionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateNotificationSubscriptionRequest.

        **参数解释：** 通知类型。 **取值范围：**   - internal_message，站内信。   - email，邮件。   - qyweixin，企业微信。   - feishu，飞书。   - dingding，钉钉。

        :param type: The type of this UpdateNotificationSubscriptionRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        r"""Gets the body of this UpdateNotificationSubscriptionRequest.

        :return: The body of this UpdateNotificationSubscriptionRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepoNotificationSubscriptionDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateNotificationSubscriptionRequest.

        :param body: The body of this UpdateNotificationSubscriptionRequest.
        :type body: :class:`huaweicloudsdkcodehub.v4.UpdateRepoNotificationSubscriptionDto`
        """
        self._body = body

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
        if not isinstance(other, UpdateNotificationSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
