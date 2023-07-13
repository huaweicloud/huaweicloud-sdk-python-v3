# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenApiParaForPublish:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'action': 'str',
        'time': 'str'
    }

    attribute_map = {
        'api_id': 'api_id',
        'action': 'action',
        'time': 'time'
    }

    def __init__(self, api_id=None, action=None, time=None):
        """OpenApiParaForPublish

        The model defined in huaweicloud sdk

        :param api_id: api编号
        :type api_id: str
        :param action: 操作类型, 包括发布/下线/停用/恢复
        :type action: str
        :param time: 截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。
        :type time: str
        """
        
        

        self._api_id = None
        self._action = None
        self._time = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if action is not None:
            self.action = action
        if time is not None:
            self.time = time

    @property
    def api_id(self):
        """Gets the api_id of this OpenApiParaForPublish.

        api编号

        :return: The api_id of this OpenApiParaForPublish.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this OpenApiParaForPublish.

        api编号

        :param api_id: The api_id of this OpenApiParaForPublish.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def action(self):
        """Gets the action of this OpenApiParaForPublish.

        操作类型, 包括发布/下线/停用/恢复

        :return: The action of this OpenApiParaForPublish.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this OpenApiParaForPublish.

        操作类型, 包括发布/下线/停用/恢复

        :param action: The action of this OpenApiParaForPublish.
        :type action: str
        """
        self._action = action

    @property
    def time(self):
        """Gets the time of this OpenApiParaForPublish.

        截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。

        :return: The time of this OpenApiParaForPublish.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OpenApiParaForPublish.

        截止时间。仅定期执行需要此参数，默认服务器当前时间三天后。

        :param time: The time of this OpenApiParaForPublish.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, OpenApiParaForPublish):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
