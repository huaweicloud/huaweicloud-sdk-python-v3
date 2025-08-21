# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectWebhookLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'hook_id': 'int',
        'log_id': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'hook_id': 'hook_id',
        'log_id': 'log_id'
    }

    def __init__(self, project_id=None, hook_id=None, log_id=None):
        r"""ShowProjectWebhookLogRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param hook_id: **参数解释：**  Webhook id。
        :type hook_id: int
        :param log_id: **参数解释：**  Webhook 日志id。
        :type log_id: int
        """
        
        

        self._project_id = None
        self._hook_id = None
        self._log_id = None
        self.discriminator = None

        self.project_id = project_id
        self.hook_id = hook_id
        self.log_id = log_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowProjectWebhookLogRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ShowProjectWebhookLogRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowProjectWebhookLogRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ShowProjectWebhookLogRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def hook_id(self):
        r"""Gets the hook_id of this ShowProjectWebhookLogRequest.

        **参数解释：**  Webhook id。

        :return: The hook_id of this ShowProjectWebhookLogRequest.
        :rtype: int
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this ShowProjectWebhookLogRequest.

        **参数解释：**  Webhook id。

        :param hook_id: The hook_id of this ShowProjectWebhookLogRequest.
        :type hook_id: int
        """
        self._hook_id = hook_id

    @property
    def log_id(self):
        r"""Gets the log_id of this ShowProjectWebhookLogRequest.

        **参数解释：**  Webhook 日志id。

        :return: The log_id of this ShowProjectWebhookLogRequest.
        :rtype: int
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this ShowProjectWebhookLogRequest.

        **参数解释：**  Webhook 日志id。

        :param log_id: The log_id of this ShowProjectWebhookLogRequest.
        :type log_id: int
        """
        self._log_id = log_id

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
        if not isinstance(other, ShowProjectWebhookLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
