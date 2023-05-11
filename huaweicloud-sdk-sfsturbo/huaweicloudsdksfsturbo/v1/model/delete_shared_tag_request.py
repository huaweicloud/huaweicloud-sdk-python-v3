# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSharedTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'key': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'key': 'key'
    }

    def __init__(self, share_id=None, key=None):
        """DeleteSharedTagRequest

        The model defined in huaweicloud sdk

        :param share_id: 共享ID
        :type share_id: str
        :param key: 标签的键,最大长度36个字符。  key不能为空，不能包含非打印字符ASCII(0-31)，“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\”,“,”,“|”,“/”。只能包含大写字母、小写字母、数字，特殊字符\&quot;-\&quot;和\&quot;_\&quot;。  说明：调用删除共享标签接口删除标签时，如果标签的键中存在不被URL直接解析的特殊字符，需要对标签的键进行URL转义处理。
        :type key: str
        """
        
        

        self._share_id = None
        self._key = None
        self.discriminator = None

        self.share_id = share_id
        self.key = key

    @property
    def share_id(self):
        """Gets the share_id of this DeleteSharedTagRequest.

        共享ID

        :return: The share_id of this DeleteSharedTagRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this DeleteSharedTagRequest.

        共享ID

        :param share_id: The share_id of this DeleteSharedTagRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def key(self):
        """Gets the key of this DeleteSharedTagRequest.

        标签的键,最大长度36个字符。  key不能为空，不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。只能包含大写字母、小写字母、数字，特殊字符\"-\"和\"_\"。  说明：调用删除共享标签接口删除标签时，如果标签的键中存在不被URL直接解析的特殊字符，需要对标签的键进行URL转义处理。

        :return: The key of this DeleteSharedTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteSharedTagRequest.

        标签的键,最大长度36个字符。  key不能为空，不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。只能包含大写字母、小写字母、数字，特殊字符\"-\"和\"_\"。  说明：调用删除共享标签接口删除标签时，如果标签的键中存在不被URL直接解析的特殊字符，需要对标签的键进行URL转义处理。

        :param key: The key of this DeleteSharedTagRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeleteSharedTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
