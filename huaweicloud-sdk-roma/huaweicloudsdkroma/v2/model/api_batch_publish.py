# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiBatchPublish:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apis': 'list[str]',
        'env_id': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'apis': 'apis',
        'env_id': 'env_id',
        'remark': 'remark'
    }

    def __init__(self, apis=None, env_id=None, remark=None):
        r"""ApiBatchPublish

        The model defined in huaweicloud sdk

        :param apis: 需要发布或下线的API ID列表
        :type apis: list[str]
        :param env_id: 环境ID
        :type env_id: str
        :param remark: 对本次发布的描述信息  字符长度不超过255 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        """
        
        

        self._apis = None
        self._env_id = None
        self._remark = None
        self.discriminator = None

        if apis is not None:
            self.apis = apis
        self.env_id = env_id
        if remark is not None:
            self.remark = remark

    @property
    def apis(self):
        r"""Gets the apis of this ApiBatchPublish.

        需要发布或下线的API ID列表

        :return: The apis of this ApiBatchPublish.
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        r"""Sets the apis of this ApiBatchPublish.

        需要发布或下线的API ID列表

        :param apis: The apis of this ApiBatchPublish.
        :type apis: list[str]
        """
        self._apis = apis

    @property
    def env_id(self):
        r"""Gets the env_id of this ApiBatchPublish.

        环境ID

        :return: The env_id of this ApiBatchPublish.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ApiBatchPublish.

        环境ID

        :param env_id: The env_id of this ApiBatchPublish.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def remark(self):
        r"""Gets the remark of this ApiBatchPublish.

        对本次发布的描述信息  字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiBatchPublish.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ApiBatchPublish.

        对本次发布的描述信息  字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiBatchPublish.
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
        if not isinstance(other, ApiBatchPublish):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
