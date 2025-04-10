# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiActionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'api_id': 'str',
        'env_id': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'action': 'action',
        'api_id': 'api_id',
        'env_id': 'env_id',
        'remark': 'remark'
    }

    def __init__(self, action=None, api_id=None, env_id=None, remark=None):
        r"""ApiActionInfo

        The model defined in huaweicloud sdk

        :param action: 需要进行的操作。 - online：发布 - offline：下线
        :type action: str
        :param api_id: API的编号，即：需要进行发布或下线的API的编号
        :type api_id: str
        :param env_id: 环境的编号，即：API需要发布到哪个环境
        :type env_id: str
        :param remark: 对发布动作的简述。字符长度不超过255 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        """
        
        

        self._action = None
        self._api_id = None
        self._env_id = None
        self._remark = None
        self.discriminator = None

        self.action = action
        self.api_id = api_id
        self.env_id = env_id
        if remark is not None:
            self.remark = remark

    @property
    def action(self):
        r"""Gets the action of this ApiActionInfo.

        需要进行的操作。 - online：发布 - offline：下线

        :return: The action of this ApiActionInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ApiActionInfo.

        需要进行的操作。 - online：发布 - offline：下线

        :param action: The action of this ApiActionInfo.
        :type action: str
        """
        self._action = action

    @property
    def api_id(self):
        r"""Gets the api_id of this ApiActionInfo.

        API的编号，即：需要进行发布或下线的API的编号

        :return: The api_id of this ApiActionInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ApiActionInfo.

        API的编号，即：需要进行发布或下线的API的编号

        :param api_id: The api_id of this ApiActionInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def env_id(self):
        r"""Gets the env_id of this ApiActionInfo.

        环境的编号，即：API需要发布到哪个环境

        :return: The env_id of this ApiActionInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ApiActionInfo.

        环境的编号，即：API需要发布到哪个环境

        :param env_id: The env_id of this ApiActionInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def remark(self):
        r"""Gets the remark of this ApiActionInfo.

        对发布动作的简述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiActionInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ApiActionInfo.

        对发布动作的简述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiActionInfo.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, ApiActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
